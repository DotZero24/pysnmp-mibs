# SNMP MIB module (ADTRAN-TA5K-PBIT-REMAPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-PBIT-REMAPPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:12 2025
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

(adTa5kPbitRemapping,
 adTa5kPbitRemappingID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adTa5kPbitRemapping",
    "adTa5kPbitRemappingID")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adTa5kPbitRemappingModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 38, 1)
)
if mibBuilder.loadTexts:
    adTa5kPbitRemappingModuleIdentity.setRevisions(
        ("2013-02-18 20:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kPbitRemappingProvisioning_ObjectIdentity = ObjectIdentity
adTa5kPbitRemappingProvisioning = _AdTa5kPbitRemappingProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1)
)
_AdTa5kPbitRemappingTable_Object = MibTable
adTa5kPbitRemappingTable = _AdTa5kPbitRemappingTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1, 1)
)
if mibBuilder.loadTexts:
    adTa5kPbitRemappingTable.setStatus("current")
_AdTa5kPbitRemappingEntry_Object = MibTableRow
adTa5kPbitRemappingEntry = _AdTa5kPbitRemappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1, 1, 1)
)
adTa5kPbitRemappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TA5K-PBIT-REMAPPING-MIB", "adTa5kPbitRemappingIngressVlanID"),
    (0, "ADTRAN-TA5K-PBIT-REMAPPING-MIB", "adTa5kPbitRemappingIngressPriority"),
)
if mibBuilder.loadTexts:
    adTa5kPbitRemappingEntry.setStatus("current")


class _AdTa5kPbitRemappingIngressVlanID_Type(Integer32):
    """Custom type adTa5kPbitRemappingIngressVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AdTa5kPbitRemappingIngressVlanID_Type.__name__ = "Integer32"
_AdTa5kPbitRemappingIngressVlanID_Object = MibTableColumn
adTa5kPbitRemappingIngressVlanID = _AdTa5kPbitRemappingIngressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1, 1, 1, 1),
    _AdTa5kPbitRemappingIngressVlanID_Type()
)
adTa5kPbitRemappingIngressVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kPbitRemappingIngressVlanID.setStatus("current")


class _AdTa5kPbitRemappingIngressPriority_Type(Integer32):
    """Custom type adTa5kPbitRemappingIngressPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdTa5kPbitRemappingIngressPriority_Type.__name__ = "Integer32"
_AdTa5kPbitRemappingIngressPriority_Object = MibTableColumn
adTa5kPbitRemappingIngressPriority = _AdTa5kPbitRemappingIngressPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1, 1, 1, 2),
    _AdTa5kPbitRemappingIngressPriority_Type()
)
adTa5kPbitRemappingIngressPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kPbitRemappingIngressPriority.setStatus("current")


class _AdTa5kPbitRemappingNewPriority_Type(Integer32):
    """Custom type adTa5kPbitRemappingNewPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdTa5kPbitRemappingNewPriority_Type.__name__ = "Integer32"
_AdTa5kPbitRemappingNewPriority_Object = MibTableColumn
adTa5kPbitRemappingNewPriority = _AdTa5kPbitRemappingNewPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1, 1, 1, 3),
    _AdTa5kPbitRemappingNewPriority_Type()
)
adTa5kPbitRemappingNewPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTa5kPbitRemappingNewPriority.setStatus("current")
_AdTa5kPbitRemappingRowStatus_Type = RowStatus
_AdTa5kPbitRemappingRowStatus_Object = MibTableColumn
adTa5kPbitRemappingRowStatus = _AdTa5kPbitRemappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 1, 1, 1, 4),
    _AdTa5kPbitRemappingRowStatus_Type()
)
adTa5kPbitRemappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTa5kPbitRemappingRowStatus.setStatus("current")
_AdTa5kPbitRemappingStatus_ObjectIdentity = ObjectIdentity
adTa5kPbitRemappingStatus = _AdTa5kPbitRemappingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 2)
)
_AdTa5kPbitRemappingMaxSupported_Type = Integer32
_AdTa5kPbitRemappingMaxSupported_Object = MibScalar
adTa5kPbitRemappingMaxSupported = _AdTa5kPbitRemappingMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 2, 1),
    _AdTa5kPbitRemappingMaxSupported_Type()
)
adTa5kPbitRemappingMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kPbitRemappingMaxSupported.setStatus("current")
_AdTa5kPbitRemappingLastError_Type = DisplayString
_AdTa5kPbitRemappingLastError_Object = MibScalar
adTa5kPbitRemappingLastError = _AdTa5kPbitRemappingLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 38, 2, 2),
    _AdTa5kPbitRemappingLastError_Type()
)
adTa5kPbitRemappingLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kPbitRemappingLastError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-PBIT-REMAPPING-MIB",
    **{"adTa5kPbitRemappingProvisioning": adTa5kPbitRemappingProvisioning,
       "adTa5kPbitRemappingTable": adTa5kPbitRemappingTable,
       "adTa5kPbitRemappingEntry": adTa5kPbitRemappingEntry,
       "adTa5kPbitRemappingIngressVlanID": adTa5kPbitRemappingIngressVlanID,
       "adTa5kPbitRemappingIngressPriority": adTa5kPbitRemappingIngressPriority,
       "adTa5kPbitRemappingNewPriority": adTa5kPbitRemappingNewPriority,
       "adTa5kPbitRemappingRowStatus": adTa5kPbitRemappingRowStatus,
       "adTa5kPbitRemappingStatus": adTa5kPbitRemappingStatus,
       "adTa5kPbitRemappingMaxSupported": adTa5kPbitRemappingMaxSupported,
       "adTa5kPbitRemappingLastError": adTa5kPbitRemappingLastError,
       "adTa5kPbitRemappingModuleIdentity": adTa5kPbitRemappingModuleIdentity}
)
