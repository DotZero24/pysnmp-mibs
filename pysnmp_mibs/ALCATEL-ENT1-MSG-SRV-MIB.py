# SNMP MIB module (ALCATEL-ENT1-MSG-SRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-MSG-SRV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:08:58 2025
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

(softentIND1MsgSrvMIB,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1MsgSrvMIB")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1MsgSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIB.setRevisions(
        ("2013-06-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MsgSrvMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1MsgSrvMIBNotifications = _AlcatelIND1MsgSrvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIBNotifications.setStatus("current")
_AlcatelIND1MsgSrvMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MsgSrvMIBObjects = _AlcatelIND1MsgSrvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIBObjects.setStatus("current")


class _AlaMsgSrvGlobalConfigStatus_Type(Integer32):
    """Custom type alaMsgSrvGlobalConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaMsgSrvGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaMsgSrvGlobalConfigStatus_Object = MibScalar
alaMsgSrvGlobalConfigStatus = _AlaMsgSrvGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1, 1),
    _AlaMsgSrvGlobalConfigStatus_Type()
)
alaMsgSrvGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMsgSrvGlobalConfigStatus.setStatus("current")


class _AlaMsgSrvGlobalRestart_Type(Integer32):
    """Custom type alaMsgSrvGlobalRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("restart", 2))
    )


_AlaMsgSrvGlobalRestart_Type.__name__ = "Integer32"
_AlaMsgSrvGlobalRestart_Object = MibScalar
alaMsgSrvGlobalRestart = _AlaMsgSrvGlobalRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1, 2),
    _AlaMsgSrvGlobalRestart_Type()
)
alaMsgSrvGlobalRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMsgSrvGlobalRestart.setStatus("current")
_AlcatelIND1MsgSrvMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MsgSrvMIBConformance = _AlcatelIND1MsgSrvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIBConformance.setStatus("current")
_AlcatelIND1MsgSrvMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MsgSrvMIBGroups = _AlcatelIND1MsgSrvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIBGroups.setStatus("current")
_AlcatelIND1MsgSrvMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MsgSrvMIBCompliances = _AlcatelIND1MsgSrvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIBCompliances.setStatus("current")

# Managed Objects groups

alaMsgSrvGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 1, 1)
)
alaMsgSrvGlobalConfigGroup.setObjects(
      *(("ALCATEL-ENT1-MSG-SRV-MIB", "alaMsgSrvGlobalConfigStatus"),
        ("ALCATEL-ENT1-MSG-SRV-MIB", "alaMsgSrvGlobalRestart"))
)
if mibBuilder.loadTexts:
    alaMsgSrvGlobalConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1MsgSrvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 2, 1)
)
alcatelIND1MsgSrvMIBCompliance.setObjects(
    ("ALCATEL-ENT1-MSG-SRV-MIB", "alaMsgSrvGlobalConfigGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1MsgSrvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-MSG-SRV-MIB",
    **{"alcatelIND1MsgSrvMIB": alcatelIND1MsgSrvMIB,
       "alcatelIND1MsgSrvMIBNotifications": alcatelIND1MsgSrvMIBNotifications,
       "alcatelIND1MsgSrvMIBObjects": alcatelIND1MsgSrvMIBObjects,
       "alaMsgSrvGlobalConfigStatus": alaMsgSrvGlobalConfigStatus,
       "alaMsgSrvGlobalRestart": alaMsgSrvGlobalRestart,
       "alcatelIND1MsgSrvMIBConformance": alcatelIND1MsgSrvMIBConformance,
       "alcatelIND1MsgSrvMIBGroups": alcatelIND1MsgSrvMIBGroups,
       "alaMsgSrvGlobalConfigGroup": alaMsgSrvGlobalConfigGroup,
       "alcatelIND1MsgSrvMIBCompliances": alcatelIND1MsgSrvMIBCompliances,
       "alcatelIND1MsgSrvMIBCompliance": alcatelIND1MsgSrvMIBCompliance}
)
