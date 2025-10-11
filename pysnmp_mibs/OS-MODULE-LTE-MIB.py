# SNMP MIB module (OS-MODULE-LTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-MODULE-LTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:54 2025
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

(EntityName,
 EntryValidator,
 oaOptiSwitch) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "EntityName",
    "EntryValidator",
    "oaOptiSwitch")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osModuleLte = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42)
)
if mibBuilder.loadTexts:
    osModuleLte.setRevisions(
        ("2023-01-26 00:00",
         "2020-09-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsModuleLteGen_ObjectIdentity = ObjectIdentity
osModuleLteGen = _OsModuleLteGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 1)
)


class _OsModuleLteSupport_Type(Integer32):
    """Custom type osModuleLteSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OsModuleLteSupport_Type.__name__ = "Integer32"
_OsModuleLteSupport_Object = MibScalar
osModuleLteSupport = _OsModuleLteSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 1, 1),
    _OsModuleLteSupport_Type()
)
osModuleLteSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModuleLteSupport.setStatus("current")
_OsModuleLteTables_ObjectIdentity = ObjectIdentity
osModuleLteTables = _OsModuleLteTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2)
)
_OsModLteApnModTable_Object = MibTable
osModLteApnModTable = _OsModLteApnModTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1)
)
if mibBuilder.loadTexts:
    osModLteApnModTable.setStatus("current")
_OsModLteApnModEntry_Object = MibTableRow
osModLteApnModEntry = _OsModLteApnModEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1)
)
osModLteApnModEntry.setIndexNames(
    (0, "OS-MODULE-LTE-MIB", "osModLteApnModName"),
)
if mibBuilder.loadTexts:
    osModLteApnModEntry.setStatus("current")
_OsModLteApnModName_Type = EntityName
_OsModLteApnModName_Object = MibTableColumn
osModLteApnModName = _OsModLteApnModName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1, 2),
    _OsModLteApnModName_Type()
)
osModLteApnModName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osModLteApnModName.setStatus("current")


class _OsModLteApnModPriority_Type(Unsigned32):
    """Custom type osModLteApnModPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_OsModLteApnModPriority_Type.__name__ = "Unsigned32"
_OsModLteApnModPriority_Object = MibTableColumn
osModLteApnModPriority = _OsModLteApnModPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1, 3),
    _OsModLteApnModPriority_Type()
)
osModLteApnModPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModLteApnModPriority.setStatus("current")


class _OsModLteApnModID_Type(DisplayString):
    """Custom type osModLteApnModID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 63),
    )


_OsModLteApnModID_Type.__name__ = "DisplayString"
_OsModLteApnModID_Object = MibTableColumn
osModLteApnModID = _OsModLteApnModID_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1, 4),
    _OsModLteApnModID_Type()
)
osModLteApnModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModLteApnModID.setStatus("current")


class _OsModLteApnModProtocol_Type(Integer32):
    """Custom type osModLteApnModProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4ipv6", 3))
    )


_OsModLteApnModProtocol_Type.__name__ = "Integer32"
_OsModLteApnModProtocol_Object = MibTableColumn
osModLteApnModProtocol = _OsModLteApnModProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1, 5),
    _OsModLteApnModProtocol_Type()
)
osModLteApnModProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModLteApnModProtocol.setStatus("current")


class _OsModLteApnModBand_Type(Unsigned32):
    """Custom type osModLteApnModBand based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_OsModLteApnModBand_Type.__name__ = "Unsigned32"
_OsModLteApnModBand_Object = MibTableColumn
osModLteApnModBand = _OsModLteApnModBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1, 6),
    _OsModLteApnModBand_Type()
)
osModLteApnModBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModLteApnModBand.setStatus("current")
_OsModLteApnModLastActive_Type = TruthValue
_OsModLteApnModLastActive_Object = MibTableColumn
osModLteApnModLastActive = _OsModLteApnModLastActive_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 1, 1, 7),
    _OsModLteApnModLastActive_Type()
)
osModLteApnModLastActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModLteApnModLastActive.setStatus("current")
_OsModLteApnDevTable_Object = MibTable
osModLteApnDevTable = _OsModLteApnDevTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2)
)
if mibBuilder.loadTexts:
    osModLteApnDevTable.setStatus("current")
_OsModLteApnDevEntry_Object = MibTableRow
osModLteApnDevEntry = _OsModLteApnDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1)
)
osModLteApnDevEntry.setIndexNames(
    (0, "OS-MODULE-LTE-MIB", "osModLteApnDevName"),
)
if mibBuilder.loadTexts:
    osModLteApnDevEntry.setStatus("current")
_OsModLteApnDevName_Type = EntityName
_OsModLteApnDevName_Object = MibTableColumn
osModLteApnDevName = _OsModLteApnDevName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 2),
    _OsModLteApnDevName_Type()
)
osModLteApnDevName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osModLteApnDevName.setStatus("current")


class _OsModLteApnDevPriority_Type(Unsigned32):
    """Custom type osModLteApnDevPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_OsModLteApnDevPriority_Type.__name__ = "Unsigned32"
_OsModLteApnDevPriority_Object = MibTableColumn
osModLteApnDevPriority = _OsModLteApnDevPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 3),
    _OsModLteApnDevPriority_Type()
)
osModLteApnDevPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModLteApnDevPriority.setStatus("current")


class _OsModLteApnDevID_Type(DisplayString):
    """Custom type osModLteApnDevID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 63),
    )


_OsModLteApnDevID_Type.__name__ = "DisplayString"
_OsModLteApnDevID_Object = MibTableColumn
osModLteApnDevID = _OsModLteApnDevID_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 4),
    _OsModLteApnDevID_Type()
)
osModLteApnDevID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModLteApnDevID.setStatus("current")


class _OsModLteApnDevProtocol_Type(Integer32):
    """Custom type osModLteApnDevProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4ipv6", 3))
    )


_OsModLteApnDevProtocol_Type.__name__ = "Integer32"
_OsModLteApnDevProtocol_Object = MibTableColumn
osModLteApnDevProtocol = _OsModLteApnDevProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 5),
    _OsModLteApnDevProtocol_Type()
)
osModLteApnDevProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModLteApnDevProtocol.setStatus("current")


class _OsModLteApnDevBand_Type(Unsigned32):
    """Custom type osModLteApnDevBand based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_OsModLteApnDevBand_Type.__name__ = "Unsigned32"
_OsModLteApnDevBand_Object = MibTableColumn
osModLteApnDevBand = _OsModLteApnDevBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 6),
    _OsModLteApnDevBand_Type()
)
osModLteApnDevBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModLteApnDevBand.setStatus("current")
_OsModLteApnDevDefault_Type = TruthValue
_OsModLteApnDevDefault_Object = MibTableColumn
osModLteApnDevDefault = _OsModLteApnDevDefault_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 7),
    _OsModLteApnDevDefault_Type()
)
osModLteApnDevDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModLteApnDevDefault.setStatus("current")
_OsModLteApnDevAdminStatus_Type = EntryValidator
_OsModLteApnDevAdminStatus_Object = MibTableColumn
osModLteApnDevAdminStatus = _OsModLteApnDevAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 2, 1, 98),
    _OsModLteApnDevAdminStatus_Type()
)
osModLteApnDevAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModLteApnDevAdminStatus.setStatus("current")
_OsModFiveGApnModTable_Object = MibTable
osModFiveGApnModTable = _OsModFiveGApnModTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3)
)
if mibBuilder.loadTexts:
    osModFiveGApnModTable.setStatus("current")
_OsModFiveGApnModEntry_Object = MibTableRow
osModFiveGApnModEntry = _OsModFiveGApnModEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1)
)
osModFiveGApnModEntry.setIndexNames(
    (0, "OS-MODULE-LTE-MIB", "osModFiveGApnModName"),
)
if mibBuilder.loadTexts:
    osModFiveGApnModEntry.setStatus("current")
_OsModFiveGApnModName_Type = EntityName
_OsModFiveGApnModName_Object = MibTableColumn
osModFiveGApnModName = _OsModFiveGApnModName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1, 2),
    _OsModFiveGApnModName_Type()
)
osModFiveGApnModName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osModFiveGApnModName.setStatus("current")


class _OsModFiveGApnModPriority_Type(Unsigned32):
    """Custom type osModFiveGApnModPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_OsModFiveGApnModPriority_Type.__name__ = "Unsigned32"
_OsModFiveGApnModPriority_Object = MibTableColumn
osModFiveGApnModPriority = _OsModFiveGApnModPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1, 3),
    _OsModFiveGApnModPriority_Type()
)
osModFiveGApnModPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModFiveGApnModPriority.setStatus("current")


class _OsModFiveGApnModID_Type(DisplayString):
    """Custom type osModFiveGApnModID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 63),
    )


_OsModFiveGApnModID_Type.__name__ = "DisplayString"
_OsModFiveGApnModID_Object = MibTableColumn
osModFiveGApnModID = _OsModFiveGApnModID_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1, 4),
    _OsModFiveGApnModID_Type()
)
osModFiveGApnModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModFiveGApnModID.setStatus("current")


class _OsModFiveGApnModProtocol_Type(Integer32):
    """Custom type osModFiveGApnModProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4ipv6", 3))
    )


_OsModFiveGApnModProtocol_Type.__name__ = "Integer32"
_OsModFiveGApnModProtocol_Object = MibTableColumn
osModFiveGApnModProtocol = _OsModFiveGApnModProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1, 5),
    _OsModFiveGApnModProtocol_Type()
)
osModFiveGApnModProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModFiveGApnModProtocol.setStatus("current")


class _OsModFiveGApnModBand_Type(Unsigned32):
    """Custom type osModFiveGApnModBand based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_OsModFiveGApnModBand_Type.__name__ = "Unsigned32"
_OsModFiveGApnModBand_Object = MibTableColumn
osModFiveGApnModBand = _OsModFiveGApnModBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1, 6),
    _OsModFiveGApnModBand_Type()
)
osModFiveGApnModBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModFiveGApnModBand.setStatus("current")
_OsModFiveGApnModLastActive_Type = TruthValue
_OsModFiveGApnModLastActive_Object = MibTableColumn
osModFiveGApnModLastActive = _OsModFiveGApnModLastActive_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 3, 1, 7),
    _OsModFiveGApnModLastActive_Type()
)
osModFiveGApnModLastActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModFiveGApnModLastActive.setStatus("current")
_OsModFiveGApnDevTable_Object = MibTable
osModFiveGApnDevTable = _OsModFiveGApnDevTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4)
)
if mibBuilder.loadTexts:
    osModFiveGApnDevTable.setStatus("current")
_OsModFiveGApnDevEntry_Object = MibTableRow
osModFiveGApnDevEntry = _OsModFiveGApnDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1)
)
osModFiveGApnDevEntry.setIndexNames(
    (0, "OS-MODULE-LTE-MIB", "osModFiveGApnDevName"),
)
if mibBuilder.loadTexts:
    osModFiveGApnDevEntry.setStatus("current")
_OsModFiveGApnDevName_Type = EntityName
_OsModFiveGApnDevName_Object = MibTableColumn
osModFiveGApnDevName = _OsModFiveGApnDevName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 2),
    _OsModFiveGApnDevName_Type()
)
osModFiveGApnDevName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osModFiveGApnDevName.setStatus("current")


class _OsModFiveGApnDevPriority_Type(Unsigned32):
    """Custom type osModFiveGApnDevPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_OsModFiveGApnDevPriority_Type.__name__ = "Unsigned32"
_OsModFiveGApnDevPriority_Object = MibTableColumn
osModFiveGApnDevPriority = _OsModFiveGApnDevPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 3),
    _OsModFiveGApnDevPriority_Type()
)
osModFiveGApnDevPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModFiveGApnDevPriority.setStatus("current")


class _OsModFiveGApnDevID_Type(DisplayString):
    """Custom type osModFiveGApnDevID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 63),
    )


_OsModFiveGApnDevID_Type.__name__ = "DisplayString"
_OsModFiveGApnDevID_Object = MibTableColumn
osModFiveGApnDevID = _OsModFiveGApnDevID_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 4),
    _OsModFiveGApnDevID_Type()
)
osModFiveGApnDevID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModFiveGApnDevID.setStatus("current")


class _OsModFiveGApnDevProtocol_Type(Integer32):
    """Custom type osModFiveGApnDevProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4ipv6", 3))
    )


_OsModFiveGApnDevProtocol_Type.__name__ = "Integer32"
_OsModFiveGApnDevProtocol_Object = MibTableColumn
osModFiveGApnDevProtocol = _OsModFiveGApnDevProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 5),
    _OsModFiveGApnDevProtocol_Type()
)
osModFiveGApnDevProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModFiveGApnDevProtocol.setStatus("current")


class _OsModFiveGApnDevBand_Type(Unsigned32):
    """Custom type osModFiveGApnDevBand based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_OsModFiveGApnDevBand_Type.__name__ = "Unsigned32"
_OsModFiveGApnDevBand_Object = MibTableColumn
osModFiveGApnDevBand = _OsModFiveGApnDevBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 6),
    _OsModFiveGApnDevBand_Type()
)
osModFiveGApnDevBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModFiveGApnDevBand.setStatus("current")
_OsModFiveGApnDevDefault_Type = TruthValue
_OsModFiveGApnDevDefault_Object = MibTableColumn
osModFiveGApnDevDefault = _OsModFiveGApnDevDefault_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 7),
    _OsModFiveGApnDevDefault_Type()
)
osModFiveGApnDevDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osModFiveGApnDevDefault.setStatus("current")
_OsModFiveGApnDevAdminStatus_Type = EntryValidator
_OsModFiveGApnDevAdminStatus_Object = MibTableColumn
osModFiveGApnDevAdminStatus = _OsModFiveGApnDevAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 2, 4, 1, 98),
    _OsModFiveGApnDevAdminStatus_Type()
)
osModFiveGApnDevAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osModFiveGApnDevAdminStatus.setStatus("current")
_OsMLteConformance_ObjectIdentity = ObjectIdentity
osMLteConformance = _OsMLteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 100)
)
_OsMLteMIBCompliances_ObjectIdentity = ObjectIdentity
osMLteMIBCompliances = _OsMLteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 100, 1)
)
_OsMLteMIBGroups_ObjectIdentity = ObjectIdentity
osMLteMIBGroups = _OsMLteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 100, 2)
)

# Managed Objects groups

osModuleLteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 100, 2, 1)
)
osModuleLteGroup.setObjects(
    ("OS-MODULE-LTE-MIB", "osModuleLteSupport")
)
if mibBuilder.loadTexts:
    osModuleLteGroup.setStatus("current")

osModuleLteOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 100, 2, 2)
)
osModuleLteOptGroup.setObjects(
      *(("OS-MODULE-LTE-MIB", "osModuleLteSupport"),
        ("OS-MODULE-LTE-MIB", "osModLteApnModPriority"),
        ("OS-MODULE-LTE-MIB", "osModLteApnModID"),
        ("OS-MODULE-LTE-MIB", "osModLteApnModProtocol"),
        ("OS-MODULE-LTE-MIB", "osModLteApnModBand"),
        ("OS-MODULE-LTE-MIB", "osModLteApnModLastActive"),
        ("OS-MODULE-LTE-MIB", "osModLteApnDevPriority"),
        ("OS-MODULE-LTE-MIB", "osModLteApnDevID"),
        ("OS-MODULE-LTE-MIB", "osModLteApnDevProtocol"),
        ("OS-MODULE-LTE-MIB", "osModLteApnDevBand"),
        ("OS-MODULE-LTE-MIB", "osModLteApnDevDefault"),
        ("OS-MODULE-LTE-MIB", "osModLteApnDevAdminStatus"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnModPriority"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnModID"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnModProtocol"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnModBand"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnModLastActive"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnDevPriority"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnDevID"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnDevProtocol"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnDevBand"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnDevDefault"),
        ("OS-MODULE-LTE-MIB", "osModFiveGApnDevAdminStatus"))
)
if mibBuilder.loadTexts:
    osModuleLteOptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osModLteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 42, 100, 1, 1)
)
osModLteMIBCompliance.setObjects(
      *(("OS-MODULE-LTE-MIB", "osModuleLteGroup"),
        ("OS-MODULE-LTE-MIB", "osModuleLteOptGroup"))
)
if mibBuilder.loadTexts:
    osModLteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-MODULE-LTE-MIB",
    **{"osModuleLte": osModuleLte,
       "osModuleLteGen": osModuleLteGen,
       "osModuleLteSupport": osModuleLteSupport,
       "osModuleLteTables": osModuleLteTables,
       "osModLteApnModTable": osModLteApnModTable,
       "osModLteApnModEntry": osModLteApnModEntry,
       "osModLteApnModName": osModLteApnModName,
       "osModLteApnModPriority": osModLteApnModPriority,
       "osModLteApnModID": osModLteApnModID,
       "osModLteApnModProtocol": osModLteApnModProtocol,
       "osModLteApnModBand": osModLteApnModBand,
       "osModLteApnModLastActive": osModLteApnModLastActive,
       "osModLteApnDevTable": osModLteApnDevTable,
       "osModLteApnDevEntry": osModLteApnDevEntry,
       "osModLteApnDevName": osModLteApnDevName,
       "osModLteApnDevPriority": osModLteApnDevPriority,
       "osModLteApnDevID": osModLteApnDevID,
       "osModLteApnDevProtocol": osModLteApnDevProtocol,
       "osModLteApnDevBand": osModLteApnDevBand,
       "osModLteApnDevDefault": osModLteApnDevDefault,
       "osModLteApnDevAdminStatus": osModLteApnDevAdminStatus,
       "osModFiveGApnModTable": osModFiveGApnModTable,
       "osModFiveGApnModEntry": osModFiveGApnModEntry,
       "osModFiveGApnModName": osModFiveGApnModName,
       "osModFiveGApnModPriority": osModFiveGApnModPriority,
       "osModFiveGApnModID": osModFiveGApnModID,
       "osModFiveGApnModProtocol": osModFiveGApnModProtocol,
       "osModFiveGApnModBand": osModFiveGApnModBand,
       "osModFiveGApnModLastActive": osModFiveGApnModLastActive,
       "osModFiveGApnDevTable": osModFiveGApnDevTable,
       "osModFiveGApnDevEntry": osModFiveGApnDevEntry,
       "osModFiveGApnDevName": osModFiveGApnDevName,
       "osModFiveGApnDevPriority": osModFiveGApnDevPriority,
       "osModFiveGApnDevID": osModFiveGApnDevID,
       "osModFiveGApnDevProtocol": osModFiveGApnDevProtocol,
       "osModFiveGApnDevBand": osModFiveGApnDevBand,
       "osModFiveGApnDevDefault": osModFiveGApnDevDefault,
       "osModFiveGApnDevAdminStatus": osModFiveGApnDevAdminStatus,
       "osMLteConformance": osMLteConformance,
       "osMLteMIBCompliances": osMLteMIBCompliances,
       "osModLteMIBCompliance": osModLteMIBCompliance,
       "osMLteMIBGroups": osMLteMIBGroups,
       "osModuleLteGroup": osModuleLteGroup,
       "osModuleLteOptGroup": osModuleLteOptGroup}
)
