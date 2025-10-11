# SNMP MIB module (ALCATEL-ENT1-AL-SRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-AL-SRV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:27 2025
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

(softentIND1ActiveLeaseSrvMIB,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1ActiveLeaseSrvMIB")

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

alcatelIND1ActiveLeaseSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIB.setRevisions(
        ("2013-06-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ActiveLeaseSrvMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBNotifications = _AlcatelIND1ActiveLeaseSrvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIBNotifications.setStatus("current")
_AlcatelIND1ActiveLeaseSrvMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBObjects = _AlcatelIND1ActiveLeaseSrvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIBObjects.setStatus("current")


class _AlaActiveLeaseSrvGlobalConfigStatus_Type(Integer32):
    """Custom type alaActiveLeaseSrvGlobalConfigStatus based on Integer32"""
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


_AlaActiveLeaseSrvGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaActiveLeaseSrvGlobalConfigStatus_Object = MibScalar
alaActiveLeaseSrvGlobalConfigStatus = _AlaActiveLeaseSrvGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1, 1),
    _AlaActiveLeaseSrvGlobalConfigStatus_Type()
)
alaActiveLeaseSrvGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaActiveLeaseSrvGlobalConfigStatus.setStatus("current")


class _AlaActiveLeaseSrvGlobalRestart_Type(Integer32):
    """Custom type alaActiveLeaseSrvGlobalRestart based on Integer32"""
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


_AlaActiveLeaseSrvGlobalRestart_Type.__name__ = "Integer32"
_AlaActiveLeaseSrvGlobalRestart_Object = MibScalar
alaActiveLeaseSrvGlobalRestart = _AlaActiveLeaseSrvGlobalRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1, 2),
    _AlaActiveLeaseSrvGlobalRestart_Type()
)
alaActiveLeaseSrvGlobalRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaActiveLeaseSrvGlobalRestart.setStatus("current")
_AlcatelIND1ActiveLeaseSrvMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBConformance = _AlcatelIND1ActiveLeaseSrvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIBConformance.setStatus("current")
_AlcatelIND1ActiveLeaseSrvMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBGroups = _AlcatelIND1ActiveLeaseSrvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIBGroups.setStatus("current")
_AlcatelIND1ActiveLeaseSrvMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ActiveLeaseSrvMIBCompliances = _AlcatelIND1ActiveLeaseSrvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIBCompliances.setStatus("current")

# Managed Objects groups

alaActiveLeaseSrvGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 1, 1)
)
alaActiveLeaseSrvGlobalConfigGroup.setObjects(
      *(("ALCATEL-ENT1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalConfigStatus"),
        ("ALCATEL-ENT1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalRestart"))
)
if mibBuilder.loadTexts:
    alaActiveLeaseSrvGlobalConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1ActiveLeaseSrvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 2, 1)
)
alcatelIND1ActiveLeaseSrvMIBCompliance.setObjects(
    ("ALCATEL-ENT1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalConfigGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1ActiveLeaseSrvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-AL-SRV-MIB",
    **{"alcatelIND1ActiveLeaseSrvMIB": alcatelIND1ActiveLeaseSrvMIB,
       "alcatelIND1ActiveLeaseSrvMIBNotifications": alcatelIND1ActiveLeaseSrvMIBNotifications,
       "alcatelIND1ActiveLeaseSrvMIBObjects": alcatelIND1ActiveLeaseSrvMIBObjects,
       "alaActiveLeaseSrvGlobalConfigStatus": alaActiveLeaseSrvGlobalConfigStatus,
       "alaActiveLeaseSrvGlobalRestart": alaActiveLeaseSrvGlobalRestart,
       "alcatelIND1ActiveLeaseSrvMIBConformance": alcatelIND1ActiveLeaseSrvMIBConformance,
       "alcatelIND1ActiveLeaseSrvMIBGroups": alcatelIND1ActiveLeaseSrvMIBGroups,
       "alaActiveLeaseSrvGlobalConfigGroup": alaActiveLeaseSrvGlobalConfigGroup,
       "alcatelIND1ActiveLeaseSrvMIBCompliances": alcatelIND1ActiveLeaseSrvMIBCompliances,
       "alcatelIND1ActiveLeaseSrvMIBCompliance": alcatelIND1ActiveLeaseSrvMIBCompliance}
)
