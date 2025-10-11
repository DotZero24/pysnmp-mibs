# SNMP MIB module (FS-TIMERANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-TIMERANGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:08 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsTrsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144)
)
if mibBuilder.loadTexts:
    fsTrsMIB.setRevisions(
        ("2015-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTrsMIBObjects_ObjectIdentity = ObjectIdentity
fsTrsMIBObjects = _FsTrsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1)
)
_FsTRTable_Object = MibTable
fsTRTable = _FsTRTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 1)
)
if mibBuilder.loadTexts:
    fsTRTable.setStatus("current")
_FsTREntry_Object = MibTableRow
fsTREntry = _FsTREntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 1, 1)
)
fsTREntry.setIndexNames(
    (0, "FS-TIMERANGE-MIB", "fsTRName"),
)
if mibBuilder.loadTexts:
    fsTREntry.setStatus("current")


class _FsTRName_Type(DisplayString):
    """Custom type fsTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsTRName_Type.__name__ = "DisplayString"
_FsTRName_Object = MibTableColumn
fsTRName = _FsTRName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 1, 1, 1),
    _FsTRName_Type()
)
fsTRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTRName.setStatus("current")


class _FsAbsTRStr_Type(DisplayString):
    """Custom type fsAbsTRStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsAbsTRStr_Type.__name__ = "DisplayString"
_FsAbsTRStr_Object = MibTableColumn
fsAbsTRStr = _FsAbsTRStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 1, 1, 2),
    _FsAbsTRStr_Type()
)
fsAbsTRStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAbsTRStr.setStatus("current")
_FsTRIndex_Type = Integer32
_FsTRIndex_Object = MibTableColumn
fsTRIndex = _FsTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 1, 1, 3),
    _FsTRIndex_Type()
)
fsTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTRIndex.setStatus("current")


class _FsTRMode_Type(Integer32):
    """Custom type fsTRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tr-add", 1),
          ("tr-del", 2))
    )


_FsTRMode_Type.__name__ = "Integer32"
_FsTRMode_Object = MibTableColumn
fsTRMode = _FsTRMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 1, 1, 4),
    _FsTRMode_Type()
)
fsTRMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTRMode.setStatus("current")
_FsTRPeriTable_Object = MibTable
fsTRPeriTable = _FsTRPeriTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 3)
)
if mibBuilder.loadTexts:
    fsTRPeriTable.setStatus("current")
_FsTRPeriEntry_Object = MibTableRow
fsTRPeriEntry = _FsTRPeriEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 3, 1)
)
fsTRPeriEntry.setIndexNames(
    (0, "FS-TIMERANGE-MIB", "fsPeriTRName"),
    (0, "FS-TIMERANGE-MIB", "fsPeriTRStr"),
)
if mibBuilder.loadTexts:
    fsTRPeriEntry.setStatus("current")


class _FsPeriTRName_Type(DisplayString):
    """Custom type fsPeriTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsPeriTRName_Type.__name__ = "DisplayString"
_FsPeriTRName_Object = MibTableColumn
fsPeriTRName = _FsPeriTRName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 3, 1, 1),
    _FsPeriTRName_Type()
)
fsPeriTRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPeriTRName.setStatus("current")


class _FsPeriTRStr_Type(DisplayString):
    """Custom type fsPeriTRStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FsPeriTRStr_Type.__name__ = "DisplayString"
_FsPeriTRStr_Object = MibTableColumn
fsPeriTRStr = _FsPeriTRStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 3, 1, 2),
    _FsPeriTRStr_Type()
)
fsPeriTRStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPeriTRStr.setStatus("current")
_FsPeriTRIndex_Type = Integer32
_FsPeriTRIndex_Object = MibTableColumn
fsPeriTRIndex = _FsPeriTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 3, 1, 3),
    _FsPeriTRIndex_Type()
)
fsPeriTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPeriTRIndex.setStatus("current")


class _FsPeriTRMode_Type(Integer32):
    """Custom type fsPeriTRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("periodic-add", 1),
          ("periodic-del", 2))
    )


_FsPeriTRMode_Type.__name__ = "Integer32"
_FsPeriTRMode_Object = MibTableColumn
fsPeriTRMode = _FsPeriTRMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 144, 1, 3, 1, 4),
    _FsPeriTRMode_Type()
)
fsPeriTRMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPeriTRMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-TIMERANGE-MIB",
    **{"fsTrsMIB": fsTrsMIB,
       "fsTrsMIBObjects": fsTrsMIBObjects,
       "fsTRTable": fsTRTable,
       "fsTREntry": fsTREntry,
       "fsTRName": fsTRName,
       "fsAbsTRStr": fsAbsTRStr,
       "fsTRIndex": fsTRIndex,
       "fsTRMode": fsTRMode,
       "fsTRPeriTable": fsTRPeriTable,
       "fsTRPeriEntry": fsTRPeriEntry,
       "fsPeriTRName": fsPeriTRName,
       "fsPeriTRStr": fsPeriTRStr,
       "fsPeriTRIndex": fsPeriTRIndex,
       "fsPeriTRMode": fsPeriTRMode}
)
