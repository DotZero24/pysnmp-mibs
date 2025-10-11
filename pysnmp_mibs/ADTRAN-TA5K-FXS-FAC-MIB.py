# SNMP MIB module (ADTRAN-TA5K-FXS-FAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-FXS-FAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:24 2025
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

(adTa5kFxsFac,
 adTa5kFxsFacID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adTa5kFxsFac",
    "adTa5kFxsFacID")

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

adTa5kFxsFacIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 35, 1)
)
if mibBuilder.loadTexts:
    adTa5kFxsFacIdentity.setRevisions(
        ("2011-11-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kFxsFacLimitedThlTable_Object = MibTable
adTa5kFxsFacLimitedThlTable = _AdTa5kFxsFacLimitedThlTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1)
)
if mibBuilder.loadTexts:
    adTa5kFxsFacLimitedThlTable.setStatus("current")
_AdTa5kFxsFacLimitedThlEntry_Object = MibTableRow
adTa5kFxsFacLimitedThlEntry = _AdTa5kFxsFacLimitedThlEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1)
)
adTa5kFxsFacLimitedThlEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kFxsFacLimitedThlEntry.setStatus("current")


class _AdTa5kFxsFacLimitedThlStart_Type(Integer32):
    """Custom type adTa5kFxsFacLimitedThlStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("begin", 1)
    )


_AdTa5kFxsFacLimitedThlStart_Type.__name__ = "Integer32"
_AdTa5kFxsFacLimitedThlStart_Object = MibTableColumn
adTa5kFxsFacLimitedThlStart = _AdTa5kFxsFacLimitedThlStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1, 1),
    _AdTa5kFxsFacLimitedThlStart_Type()
)
adTa5kFxsFacLimitedThlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kFxsFacLimitedThlStart.setStatus("current")


class _AdTa5kFxsFacLimitedThlStatus_Type(Integer32):
    """Custom type adTa5kFxsFacLimitedThlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("complete", 2),
          ("fault", 3),
          ("running", 4))
    )


_AdTa5kFxsFacLimitedThlStatus_Type.__name__ = "Integer32"
_AdTa5kFxsFacLimitedThlStatus_Object = MibTableColumn
adTa5kFxsFacLimitedThlStatus = _AdTa5kFxsFacLimitedThlStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1, 2),
    _AdTa5kFxsFacLimitedThlStatus_Type()
)
adTa5kFxsFacLimitedThlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kFxsFacLimitedThlStatus.setStatus("current")


class _AdTa5kFxsFacLimitedThlResults_Type(OctetString):
    """Custom type adTa5kFxsFacLimitedThlResults based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_AdTa5kFxsFacLimitedThlResults_Type.__name__ = "OctetString"
_AdTa5kFxsFacLimitedThlResults_Object = MibTableColumn
adTa5kFxsFacLimitedThlResults = _AdTa5kFxsFacLimitedThlResults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1, 3),
    _AdTa5kFxsFacLimitedThlResults_Type()
)
adTa5kFxsFacLimitedThlResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kFxsFacLimitedThlResults.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-FXS-FAC-MIB",
    **{"adTa5kFxsFacLimitedThlTable": adTa5kFxsFacLimitedThlTable,
       "adTa5kFxsFacLimitedThlEntry": adTa5kFxsFacLimitedThlEntry,
       "adTa5kFxsFacLimitedThlStart": adTa5kFxsFacLimitedThlStart,
       "adTa5kFxsFacLimitedThlStatus": adTa5kFxsFacLimitedThlStatus,
       "adTa5kFxsFacLimitedThlResults": adTa5kFxsFacLimitedThlResults,
       "adTa5kFxsFacIdentity": adTa5kFxsFacIdentity}
)
