# SNMP MIB module (ADTRAN-TA5K-ATP-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-ATP-CLI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:47 2025
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

(adGenTa5kAtpCli,
 adGenTa5kAtpCliID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kAtpCli",
    "adGenTa5kAtpCliID")

(adIdentity,
 adIdentityShared,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adIdentityShared",
    "adMgmt",
    "adProducts")

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

adTa5kAtpCliModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kAtpCliTable_Object = MibTable
adTa5kAtpCliTable = _AdTa5kAtpCliTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adTa5kAtpCliTable.setStatus("current")
_AdTa5kAtpCliEntry_Object = MibTableRow
adTa5kAtpCliEntry = _AdTa5kAtpCliEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1, 1)
)
adTa5kAtpCliEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kAtpCliEntry.setStatus("current")
_AdTa5kAtpCliCommand_Type = DisplayString
_AdTa5kAtpCliCommand_Object = MibTableColumn
adTa5kAtpCliCommand = _AdTa5kAtpCliCommand_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1, 1, 1),
    _AdTa5kAtpCliCommand_Type()
)
adTa5kAtpCliCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kAtpCliCommand.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-ATP-CLI-MIB",
    **{"adTa5kAtpCliTable": adTa5kAtpCliTable,
       "adTa5kAtpCliEntry": adTa5kAtpCliEntry,
       "adTa5kAtpCliCommand": adTa5kAtpCliCommand,
       "adTa5kAtpCliModuleIdentity": adTa5kAtpCliModuleIdentity}
)
