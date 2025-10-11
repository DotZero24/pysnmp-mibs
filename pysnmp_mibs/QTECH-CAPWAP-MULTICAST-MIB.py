# SNMP MIB module (QTECH-CAPWAP-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:01 2025
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

qtechCapwapMulticastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59)
)
if mibBuilder.loadTexts:
    qtechCapwapMulticastMIB.setRevisions(
        ("2009-10-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCapwapMulticastMIBObjects_ObjectIdentity = ObjectIdentity
qtechCapwapMulticastMIBObjects = _QtechCapwapMulticastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 1)
)


class _QtechCapwapMulticastWorkingMode_Type(Integer32):
    """Custom type qtechCapwapMulticastWorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_QtechCapwapMulticastWorkingMode_Type.__name__ = "Integer32"
_QtechCapwapMulticastWorkingMode_Object = MibScalar
qtechCapwapMulticastWorkingMode = _QtechCapwapMulticastWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 1, 1),
    _QtechCapwapMulticastWorkingMode_Type()
)
qtechCapwapMulticastWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCapwapMulticastWorkingMode.setStatus("current")
_QtechCapwapMulticastGroup_Type = IpAddress
_QtechCapwapMulticastGroup_Object = MibScalar
qtechCapwapMulticastGroup = _QtechCapwapMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 1, 2),
    _QtechCapwapMulticastGroup_Type()
)
qtechCapwapMulticastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCapwapMulticastGroup.setStatus("current")
_QtechCapwapMulticastMIBConformance_ObjectIdentity = ObjectIdentity
qtechCapwapMulticastMIBConformance = _QtechCapwapMulticastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2)
)
_QtechCapwapMulticastMIBCompliances_ObjectIdentity = ObjectIdentity
qtechCapwapMulticastMIBCompliances = _QtechCapwapMulticastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 1)
)
_QtechCapwapMulticastMIBGroups_ObjectIdentity = ObjectIdentity
qtechCapwapMulticastMIBGroups = _QtechCapwapMulticastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 2)
)

# Managed Objects groups

qtechCapwapMulticastMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 2, 1)
)
qtechCapwapMulticastMIBGroup.setObjects(
      *(("QTECH-CAPWAP-MULTICAST-MIB", "qtechCapwapMulticastWorkingMode"),
        ("QTECH-CAPWAP-MULTICAST-MIB", "qtechCapwapMulticastGroup"))
)
if mibBuilder.loadTexts:
    qtechCapwapMulticastMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechCapwapMulticastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 1, 1)
)
qtechCapwapMulticastMIBCompliance.setObjects(
    ("QTECH-CAPWAP-MULTICAST-MIB", "qtechCapwapMulticastMIBGroup")
)
if mibBuilder.loadTexts:
    qtechCapwapMulticastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-MULTICAST-MIB",
    **{"qtechCapwapMulticastMIB": qtechCapwapMulticastMIB,
       "qtechCapwapMulticastMIBObjects": qtechCapwapMulticastMIBObjects,
       "qtechCapwapMulticastWorkingMode": qtechCapwapMulticastWorkingMode,
       "qtechCapwapMulticastGroup": qtechCapwapMulticastGroup,
       "qtechCapwapMulticastMIBConformance": qtechCapwapMulticastMIBConformance,
       "qtechCapwapMulticastMIBCompliances": qtechCapwapMulticastMIBCompliances,
       "qtechCapwapMulticastMIBCompliance": qtechCapwapMulticastMIBCompliance,
       "qtechCapwapMulticastMIBGroups": qtechCapwapMulticastMIBGroups,
       "qtechCapwapMulticastMIBGroup": qtechCapwapMulticastMIBGroup}
)
