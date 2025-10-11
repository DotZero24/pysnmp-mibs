# SNMP MIB module (QTECH-CAPWAP-MULTICAST6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-MULTICAST6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:17 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechCapwapMulticast6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85)
)
if mibBuilder.loadTexts:
    qtechCapwapMulticast6MIB.setRevisions(
        ("2010-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCapwapMulticast6MIBObjects_ObjectIdentity = ObjectIdentity
qtechCapwapMulticast6MIBObjects = _QtechCapwapMulticast6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 1)
)


class _QtechCapwapMulticast6WorkingMode_Type(Integer32):
    """Custom type qtechCapwapMulticast6WorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("unicast", 2),
          ("multicast", 3))
    )


_QtechCapwapMulticast6WorkingMode_Type.__name__ = "Integer32"
_QtechCapwapMulticast6WorkingMode_Object = MibScalar
qtechCapwapMulticast6WorkingMode = _QtechCapwapMulticast6WorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 1, 1),
    _QtechCapwapMulticast6WorkingMode_Type()
)
qtechCapwapMulticast6WorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCapwapMulticast6WorkingMode.setStatus("current")
_QtechCapwapMulticast6Group_Type = InetAddress
_QtechCapwapMulticast6Group_Object = MibScalar
qtechCapwapMulticast6Group = _QtechCapwapMulticast6Group_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 1, 2),
    _QtechCapwapMulticast6Group_Type()
)
qtechCapwapMulticast6Group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCapwapMulticast6Group.setStatus("current")
_QtechCapwapMulticast6MIBConformance_ObjectIdentity = ObjectIdentity
qtechCapwapMulticast6MIBConformance = _QtechCapwapMulticast6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2)
)
_QtechCapwapMulticast6MIBCompliances_ObjectIdentity = ObjectIdentity
qtechCapwapMulticast6MIBCompliances = _QtechCapwapMulticast6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 1)
)
_QtechCapwapMulticast6MIBGroups_ObjectIdentity = ObjectIdentity
qtechCapwapMulticast6MIBGroups = _QtechCapwapMulticast6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 2)
)

# Managed Objects groups

qtechCapwapMulticast6MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 2, 1)
)
qtechCapwapMulticast6MIBGroup.setObjects(
      *(("QTECH-CAPWAP-MULTICAST6-MIB", "qtechCapwapMulticast6WorkingMode"),
        ("QTECH-CAPWAP-MULTICAST6-MIB", "qtechCapwapMulticast6Group"))
)
if mibBuilder.loadTexts:
    qtechCapwapMulticast6MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechCapwapMulticast6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 1, 1)
)
qtechCapwapMulticast6MIBCompliance.setObjects(
    ("QTECH-CAPWAP-MULTICAST6-MIB", "qtechCapwapMulticast6MIBGroup")
)
if mibBuilder.loadTexts:
    qtechCapwapMulticast6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-MULTICAST6-MIB",
    **{"qtechCapwapMulticast6MIB": qtechCapwapMulticast6MIB,
       "qtechCapwapMulticast6MIBObjects": qtechCapwapMulticast6MIBObjects,
       "qtechCapwapMulticast6WorkingMode": qtechCapwapMulticast6WorkingMode,
       "qtechCapwapMulticast6Group": qtechCapwapMulticast6Group,
       "qtechCapwapMulticast6MIBConformance": qtechCapwapMulticast6MIBConformance,
       "qtechCapwapMulticast6MIBCompliances": qtechCapwapMulticast6MIBCompliances,
       "qtechCapwapMulticast6MIBCompliance": qtechCapwapMulticast6MIBCompliance,
       "qtechCapwapMulticast6MIBGroups": qtechCapwapMulticast6MIBGroups,
       "qtechCapwapMulticast6MIBGroup": qtechCapwapMulticast6MIBGroup}
)
