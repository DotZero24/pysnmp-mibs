# SNMP MIB module (Dell-CDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/Dell-CDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:09:00 2025
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

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlCDB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 94)
)
if mibBuilder.loadTexts:
    rlCDB.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStartupCDBChanged_Type = TruthValue
_RlStartupCDBChanged_Object = MibScalar
rlStartupCDBChanged = _RlStartupCDBChanged_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 1),
    _RlStartupCDBChanged_Type()
)
rlStartupCDBChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStartupCDBChanged.setStatus("current")
_RlManualReboot_Type = TruthValue
_RlManualReboot_Object = MibScalar
rlManualReboot = _RlManualReboot_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 2),
    _RlManualReboot_Type()
)
rlManualReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlManualReboot.setStatus("current")
_RlStartupCDBEmpty_Type = TruthValue
_RlStartupCDBEmpty_Object = MibScalar
rlStartupCDBEmpty = _RlStartupCDBEmpty_Object(
    (1, 3, 6, 1, 4, 1, 89, 94, 3),
    _RlStartupCDBEmpty_Type()
)
rlStartupCDBEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStartupCDBEmpty.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-CDB-MIB",
    **{"rlCDB": rlCDB,
       "rlStartupCDBChanged": rlStartupCDBChanged,
       "rlManualReboot": rlManualReboot,
       "rlStartupCDBEmpty": rlStartupCDBEmpty}
)
