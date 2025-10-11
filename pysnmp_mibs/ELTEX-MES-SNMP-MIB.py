# SNMP MIB module (ELTEX-MES-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:47:58 2025
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

(usmUserEntry,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserEntry")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eltMesSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesSnmpMIBObjects_ObjectIdentity = ObjectIdentity
eltMesSnmpMIBObjects = _EltMesSnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1)
)
_EltMesSnmpUser_ObjectIdentity = ObjectIdentity
eltMesSnmpUser = _EltMesSnmpUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1, 1)
)
_EltMesSnmpUserGlobals_ObjectIdentity = ObjectIdentity
eltMesSnmpUserGlobals = _EltMesSnmpUserGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1, 1, 1)
)
_EltMesSnmpUserConfig_ObjectIdentity = ObjectIdentity
eltMesSnmpUserConfig = _EltMesSnmpUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1, 1, 2)
)
_EltSnmpUserTable_Object = MibTable
eltSnmpUserTable = _EltSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltSnmpUserTable.setStatus("current")
_EltSnmpUserEntry_Object = MibTableRow
eltSnmpUserEntry = _EltSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltSnmpUserEntry.setStatus("current")
_EltSnmpUserPrivProtocol_Type = AutonomousType
_EltSnmpUserPrivProtocol_Object = MibTableColumn
eltSnmpUserPrivProtocol = _EltSnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 1, 1, 2, 1, 1, 1),
    _EltSnmpUserPrivProtocol_Type()
)
eltSnmpUserPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltSnmpUserPrivProtocol.setStatus("current")
_EltMesSnmpMIBNotifications_ObjectIdentity = ObjectIdentity
eltMesSnmpMIBNotifications = _EltMesSnmpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 12, 2)
)
usmUserEntry.registerAugmentions(
    ("ELTEX-MES-SNMP-MIB",
     "eltSnmpUserEntry")
)
eltSnmpUserEntry.setIndexNames(*usmUserEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SNMP-MIB",
    **{"eltMesSnmp": eltMesSnmp,
       "eltMesSnmpMIBObjects": eltMesSnmpMIBObjects,
       "eltMesSnmpUser": eltMesSnmpUser,
       "eltMesSnmpUserGlobals": eltMesSnmpUserGlobals,
       "eltMesSnmpUserConfig": eltMesSnmpUserConfig,
       "eltSnmpUserTable": eltSnmpUserTable,
       "eltSnmpUserEntry": eltSnmpUserEntry,
       "eltSnmpUserPrivProtocol": eltSnmpUserPrivProtocol,
       "eltMesSnmpMIBNotifications": eltMesSnmpMIBNotifications}
)
