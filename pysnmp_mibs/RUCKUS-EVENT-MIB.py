# SNMP MIB module (RUCKUS-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:42 2025
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

(ruckusEvents,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusEvents")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusEventTraps_ObjectIdentity = ObjectIdentity
ruckusEventTraps = _RuckusEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 1)
)
_RuckusEventObjects_ObjectIdentity = ObjectIdentity
ruckusEventObjects = _RuckusEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 2)
)
_RuckusEventClientMacAddr_Type = OctetString
_RuckusEventClientMacAddr_Object = MibScalar
ruckusEventClientMacAddr = _RuckusEventClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 2, 15),
    _RuckusEventClientMacAddr_Type()
)
ruckusEventClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusEventClientMacAddr.setStatus("current")
_RuckusEventSetErrorOID_Type = ObjectIdentifier
_RuckusEventSetErrorOID_Object = MibScalar
ruckusEventSetErrorOID = _RuckusEventSetErrorOID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 2, 20),
    _RuckusEventSetErrorOID_Type()
)
ruckusEventSetErrorOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusEventSetErrorOID.setStatus("current")

# Managed Objects groups


# Notification objects

ruckusEventAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 1)
)
ruckusEventAssocTrap.setObjects(
    ("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr")
)
if mibBuilder.loadTexts:
    ruckusEventAssocTrap.setStatus(
        "current"
    )

ruckusEventDiassocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 2)
)
ruckusEventDiassocTrap.setObjects(
    ("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr")
)
if mibBuilder.loadTexts:
    ruckusEventDiassocTrap.setStatus(
        "current"
    )

ruckusEventSetErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 3)
)
ruckusEventSetErrorTrap.setObjects(
    ("RUCKUS-EVENT-MIB", "ruckusEventSetErrorOID")
)
if mibBuilder.loadTexts:
    ruckusEventSetErrorTrap.setStatus(
        "current"
    )

ruckusEventConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 25)
)
ruckusEventConnectTrap.setObjects(
    ("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr")
)
if mibBuilder.loadTexts:
    ruckusEventConnectTrap.setStatus(
        "current"
    )

ruckusEventDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 26)
)
ruckusEventDisconnectTrap.setObjects(
    ("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr")
)
if mibBuilder.loadTexts:
    ruckusEventDisconnectTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-EVENT-MIB",
    **{"ruckusEventMIB": ruckusEventMIB,
       "ruckusEventTraps": ruckusEventTraps,
       "ruckusEventAssocTrap": ruckusEventAssocTrap,
       "ruckusEventDiassocTrap": ruckusEventDiassocTrap,
       "ruckusEventSetErrorTrap": ruckusEventSetErrorTrap,
       "ruckusEventConnectTrap": ruckusEventConnectTrap,
       "ruckusEventDisconnectTrap": ruckusEventDisconnectTrap,
       "ruckusEventObjects": ruckusEventObjects,
       "ruckusEventClientMacAddr": ruckusEventClientMacAddr,
       "ruckusEventSetErrorOID": ruckusEventSetErrorOID}
)
