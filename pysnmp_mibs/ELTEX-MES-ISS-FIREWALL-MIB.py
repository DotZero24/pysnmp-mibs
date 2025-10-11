# SNMP MIB module (ELTEX-MES-ISS-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:49 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssFwlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27)
)
if mibBuilder.loadTexts:
    eltMesIssFwlMIB.setRevisions(
        ("2021-04-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssFwlObjects_ObjectIdentity = ObjectIdentity
eltMesIssFwlObjects = _EltMesIssFwlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1)
)
_EltMesIssFwlGlobals_ObjectIdentity = ObjectIdentity
eltMesIssFwlGlobals = _EltMesIssFwlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 1)
)
_EltMesIssFwlNotificationInterval_Type = Integer32
_EltMesIssFwlNotificationInterval_Object = MibScalar
eltMesIssFwlNotificationInterval = _EltMesIssFwlNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 1, 1),
    _EltMesIssFwlNotificationInterval_Type()
)
eltMesIssFwlNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssFwlNotificationInterval.setStatus("current")
_EltMesIssFwlTcpSynLimit_ObjectIdentity = ObjectIdentity
eltMesIssFwlTcpSynLimit = _EltMesIssFwlTcpSynLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2)
)


class _EltMesIssFwlTcpSynLimitEnable_Type(TruthValue):
    """Custom type eltMesIssFwlTcpSynLimitEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssFwlTcpSynLimitEnable_Type.__name__ = "TruthValue"
_EltMesIssFwlTcpSynLimitEnable_Object = MibScalar
eltMesIssFwlTcpSynLimitEnable = _EltMesIssFwlTcpSynLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 1),
    _EltMesIssFwlTcpSynLimitEnable_Type()
)
eltMesIssFwlTcpSynLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssFwlTcpSynLimitEnable.setStatus("current")
_EltMesIssFwlTcpSynLimitInterfaceTable_Object = MibTable
eltMesIssFwlTcpSynLimitInterfaceTable = _EltMesIssFwlTcpSynLimitInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltMesIssFwlTcpSynLimitInterfaceTable.setStatus("current")
_EltMesIssFwlTcpSynLimitInterfaceEntry_Object = MibTableRow
eltMesIssFwlTcpSynLimitInterfaceEntry = _EltMesIssFwlTcpSynLimitInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 2, 1)
)
eltMesIssFwlTcpSynLimitInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssFwlTcpSynLimitInterfaceEntry.setStatus("current")
_EltMesIssFwlTcpSynLimitValue_Type = Integer32
_EltMesIssFwlTcpSynLimitValue_Object = MibTableColumn
eltMesIssFwlTcpSynLimitValue = _EltMesIssFwlTcpSynLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 2, 1, 1),
    _EltMesIssFwlTcpSynLimitValue_Type()
)
eltMesIssFwlTcpSynLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssFwlTcpSynLimitValue.setStatus("current")
_EltMesIssFwlNotifications_ObjectIdentity = ObjectIdentity
eltMesIssFwlNotifications = _EltMesIssFwlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-FIREWALL-MIB",
    **{"eltMesIssFwlMIB": eltMesIssFwlMIB,
       "eltMesIssFwlObjects": eltMesIssFwlObjects,
       "eltMesIssFwlGlobals": eltMesIssFwlGlobals,
       "eltMesIssFwlNotificationInterval": eltMesIssFwlNotificationInterval,
       "eltMesIssFwlTcpSynLimit": eltMesIssFwlTcpSynLimit,
       "eltMesIssFwlTcpSynLimitEnable": eltMesIssFwlTcpSynLimitEnable,
       "eltMesIssFwlTcpSynLimitInterfaceTable": eltMesIssFwlTcpSynLimitInterfaceTable,
       "eltMesIssFwlTcpSynLimitInterfaceEntry": eltMesIssFwlTcpSynLimitInterfaceEntry,
       "eltMesIssFwlTcpSynLimitValue": eltMesIssFwlTcpSynLimitValue,
       "eltMesIssFwlNotifications": eltMesIssFwlNotifications}
)
