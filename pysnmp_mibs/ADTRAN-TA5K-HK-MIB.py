# SNMP MIB module (ADTRAN-TA5K-HK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-HK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:41 2025
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

(adGenTa5kHk,
 adGenTa5kHkID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kHk",
    "adGenTa5kHkID")

(adIdentity,
 adIdentityShared,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adIdentityShared",
    "adMgmt",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adTa5kHkModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kHkTable_Object = MibTable
adTa5kHkTable = _AdTa5kHkTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1)
)
if mibBuilder.loadTexts:
    adTa5kHkTable.setStatus("current")
_AdTa5kHkEntry_Object = MibTableRow
adTa5kHkEntry = _AdTa5kHkEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1, 1)
)
adTa5kHkEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kHkEntry.setStatus("current")


class _AdTa5kHkPresent_Type(Integer32):
    """Custom type adTa5kHkPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AdTa5kHkPresent_Type.__name__ = "Integer32"
_AdTa5kHkPresent_Object = MibTableColumn
adTa5kHkPresent = _AdTa5kHkPresent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1, 1, 1),
    _AdTa5kHkPresent_Type()
)
adTa5kHkPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kHkPresent.setStatus("current")
_AdTa5kHkTemp_Type = Integer32
_AdTa5kHkTemp_Object = MibTableColumn
adTa5kHkTemp = _AdTa5kHkTemp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1, 1, 2),
    _AdTa5kHkTemp_Type()
)
adTa5kHkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kHkTemp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-HK-MIB",
    **{"adTa5kHkTable": adTa5kHkTable,
       "adTa5kHkEntry": adTa5kHkEntry,
       "adTa5kHkPresent": adTa5kHkPresent,
       "adTa5kHkTemp": adTa5kHkTemp,
       "adTa5kHkModuleIdentity": adTa5kHkModuleIdentity}
)
