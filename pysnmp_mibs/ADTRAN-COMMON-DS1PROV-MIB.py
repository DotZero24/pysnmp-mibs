# SNMP MIB module (ADTRAN-COMMON-DS1PROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-COMMON-DS1PROV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:33 2025
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

(adGenTa5kCommonDs1Prov,
 adGenTa5kCommonDs1ProvID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kCommonDs1Prov",
    "adGenTa5kCommonDs1ProvID")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenCommonDs1ProvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdDs1vgDs1Mgmt_ObjectIdentity = ObjectIdentity
adDs1vgDs1Mgmt = _AdDs1vgDs1Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1)
)
_AdDs1vgT1InterfaceProvisioningTable_Object = MibTable
adDs1vgT1InterfaceProvisioningTable = _AdDs1vgT1InterfaceProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    adDs1vgT1InterfaceProvisioningTable.setStatus("current")
_AdDs1vgT1InterfaceProvisioningTableEntry_Object = MibTableRow
adDs1vgT1InterfaceProvisioningTableEntry = _AdDs1vgT1InterfaceProvisioningTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1)
)
adDs1vgT1InterfaceProvisioningTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adDs1vgT1InterfaceProvisioningTableEntry.setStatus("current")


class _AdDs1vgT1InterfaceProvTableLineBuildout_Type(Integer32):
    """Custom type adDs1vgT1InterfaceProvTableLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lineLength0ft", 1),
          ("lineLength0133ft", 2),
          ("lineLength133266ft", 3),
          ("lineLength266399ft", 4),
          ("lineLength399533ft", 5),
          ("lineLength533655ft", 6))
    )


_AdDs1vgT1InterfaceProvTableLineBuildout_Type.__name__ = "Integer32"
_AdDs1vgT1InterfaceProvTableLineBuildout_Object = MibTableColumn
adDs1vgT1InterfaceProvTableLineBuildout = _AdDs1vgT1InterfaceProvTableLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1, 1),
    _AdDs1vgT1InterfaceProvTableLineBuildout_Type()
)
adDs1vgT1InterfaceProvTableLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDs1vgT1InterfaceProvTableLineBuildout.setStatus("current")


class _AdDs1vgT1InterfaceProvTableLineMode_Type(Integer32):
    """Custom type adDs1vgT1InterfaceProvTableLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gr303cesop", 1),
          ("satop", 2))
    )


_AdDs1vgT1InterfaceProvTableLineMode_Type.__name__ = "Integer32"
_AdDs1vgT1InterfaceProvTableLineMode_Object = MibTableColumn
adDs1vgT1InterfaceProvTableLineMode = _AdDs1vgT1InterfaceProvTableLineMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1, 2),
    _AdDs1vgT1InterfaceProvTableLineMode_Type()
)
adDs1vgT1InterfaceProvTableLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDs1vgT1InterfaceProvTableLineMode.setStatus("current")


class _AdDs1vgT1InterfaceClearPMCounters_Type(Integer32):
    """Custom type adDs1vgT1InterfaceClearPMCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AdDs1vgT1InterfaceClearPMCounters_Type.__name__ = "Integer32"
_AdDs1vgT1InterfaceClearPMCounters_Object = MibTableColumn
adDs1vgT1InterfaceClearPMCounters = _AdDs1vgT1InterfaceClearPMCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1, 3),
    _AdDs1vgT1InterfaceClearPMCounters_Type()
)
adDs1vgT1InterfaceClearPMCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDs1vgT1InterfaceClearPMCounters.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-COMMON-DS1PROV-MIB",
    **{"adDs1vgDs1Mgmt": adDs1vgDs1Mgmt,
       "adDs1vgT1InterfaceProvisioningTable": adDs1vgT1InterfaceProvisioningTable,
       "adDs1vgT1InterfaceProvisioningTableEntry": adDs1vgT1InterfaceProvisioningTableEntry,
       "adDs1vgT1InterfaceProvTableLineBuildout": adDs1vgT1InterfaceProvTableLineBuildout,
       "adDs1vgT1InterfaceProvTableLineMode": adDs1vgT1InterfaceProvTableLineMode,
       "adDs1vgT1InterfaceClearPMCounters": adDs1vgT1InterfaceClearPMCounters,
       "adGenCommonDs1ProvMIB": adGenCommonDs1ProvMIB}
)
