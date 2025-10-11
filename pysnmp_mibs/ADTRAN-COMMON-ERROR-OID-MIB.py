# SNMP MIB module (ADTRAN-COMMON-ERROR-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-COMMON-ERROR-OID-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:48 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kErrorOid,
 adGenTa5kSErrorOidID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kErrorOid",
    "adGenTa5kSErrorOidID")

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

adGenCommonErrorOidMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kErrorOidMgmt_ObjectIdentity = ObjectIdentity
adTa5kErrorOidMgmt = _AdTa5kErrorOidMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1)
)
_AdTa5kErrorOidTable_Object = MibTable
adTa5kErrorOidTable = _AdTa5kErrorOidTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    adTa5kErrorOidTable.setStatus("current")
_AdTa5kErrorOidTableEntry_Object = MibTableRow
adTa5kErrorOidTableEntry = _AdTa5kErrorOidTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1)
)
adTa5kErrorOidTableEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kErrorOidTableEntry.setStatus("current")


class _AdTa5kDuplicateIndexErrorReporting_Type(DisplayString):
    """Custom type adTa5kDuplicateIndexErrorReporting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AdTa5kDuplicateIndexErrorReporting_Type.__name__ = "DisplayString"
_AdTa5kDuplicateIndexErrorReporting_Object = MibTableColumn
adTa5kDuplicateIndexErrorReporting = _AdTa5kDuplicateIndexErrorReporting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1, 1),
    _AdTa5kDuplicateIndexErrorReporting_Type()
)
adTa5kDuplicateIndexErrorReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDuplicateIndexErrorReporting.setStatus("current")


class _AdTa5kPseudowireErrorReporting_Type(DisplayString):
    """Custom type adTa5kPseudowireErrorReporting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AdTa5kPseudowireErrorReporting_Type.__name__ = "DisplayString"
_AdTa5kPseudowireErrorReporting_Object = MibTableColumn
adTa5kPseudowireErrorReporting = _AdTa5kPseudowireErrorReporting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1, 2),
    _AdTa5kPseudowireErrorReporting_Type()
)
adTa5kPseudowireErrorReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kPseudowireErrorReporting.setStatus("current")


class _AdTa5kPhysicalDs1ErrorReporting_Type(DisplayString):
    """Custom type adTa5kPhysicalDs1ErrorReporting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AdTa5kPhysicalDs1ErrorReporting_Type.__name__ = "DisplayString"
_AdTa5kPhysicalDs1ErrorReporting_Object = MibTableColumn
adTa5kPhysicalDs1ErrorReporting = _AdTa5kPhysicalDs1ErrorReporting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1, 3),
    _AdTa5kPhysicalDs1ErrorReporting_Type()
)
adTa5kPhysicalDs1ErrorReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kPhysicalDs1ErrorReporting.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-COMMON-ERROR-OID-MIB",
    **{"adTa5kErrorOidMgmt": adTa5kErrorOidMgmt,
       "adTa5kErrorOidTable": adTa5kErrorOidTable,
       "adTa5kErrorOidTableEntry": adTa5kErrorOidTableEntry,
       "adTa5kDuplicateIndexErrorReporting": adTa5kDuplicateIndexErrorReporting,
       "adTa5kPseudowireErrorReporting": adTa5kPseudowireErrorReporting,
       "adTa5kPhysicalDs1ErrorReporting": adTa5kPhysicalDs1ErrorReporting,
       "adGenCommonErrorOidMIB": adGenCommonErrorOidMIB}
)
