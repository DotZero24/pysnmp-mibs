# SNMP MIB module (FS-CAPWAP-MULTICAST6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CAPWAP-MULTICAST6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:41 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

fsCapwapMulticast6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85)
)
if mibBuilder.loadTexts:
    fsCapwapMulticast6MIB.setRevisions(
        ("2010-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCapwapMulticast6MIBObjects_ObjectIdentity = ObjectIdentity
fsCapwapMulticast6MIBObjects = _FsCapwapMulticast6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 1)
)


class _FsCapwapMulticast6WorkingMode_Type(Integer32):
    """Custom type fsCapwapMulticast6WorkingMode based on Integer32"""
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


_FsCapwapMulticast6WorkingMode_Type.__name__ = "Integer32"
_FsCapwapMulticast6WorkingMode_Object = MibScalar
fsCapwapMulticast6WorkingMode = _FsCapwapMulticast6WorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 1, 1),
    _FsCapwapMulticast6WorkingMode_Type()
)
fsCapwapMulticast6WorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapMulticast6WorkingMode.setStatus("current")
_FsCapwapMulticast6Group_Type = InetAddress
_FsCapwapMulticast6Group_Object = MibScalar
fsCapwapMulticast6Group = _FsCapwapMulticast6Group_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 1, 2),
    _FsCapwapMulticast6Group_Type()
)
fsCapwapMulticast6Group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapMulticast6Group.setStatus("current")
_FsCapwapMulticast6MIBConformance_ObjectIdentity = ObjectIdentity
fsCapwapMulticast6MIBConformance = _FsCapwapMulticast6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2)
)
_FsCapwapMulticast6MIBCompliances_ObjectIdentity = ObjectIdentity
fsCapwapMulticast6MIBCompliances = _FsCapwapMulticast6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 1)
)
_FsCapwapMulticast6MIBGroups_ObjectIdentity = ObjectIdentity
fsCapwapMulticast6MIBGroups = _FsCapwapMulticast6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 2)
)

# Managed Objects groups

fsCapwapMulticast6MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 2, 1)
)
fsCapwapMulticast6MIBGroup.setObjects(
      *(("FS-CAPWAP-MULTICAST6-MIB", "fsCapwapMulticast6WorkingMode"),
        ("FS-CAPWAP-MULTICAST6-MIB", "fsCapwapMulticast6Group"))
)
if mibBuilder.loadTexts:
    fsCapwapMulticast6MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsCapwapMulticast6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 1, 1)
)
fsCapwapMulticast6MIBCompliance.setObjects(
    ("FS-CAPWAP-MULTICAST6-MIB", "fsCapwapMulticast6MIBGroup")
)
if mibBuilder.loadTexts:
    fsCapwapMulticast6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CAPWAP-MULTICAST6-MIB",
    **{"fsCapwapMulticast6MIB": fsCapwapMulticast6MIB,
       "fsCapwapMulticast6MIBObjects": fsCapwapMulticast6MIBObjects,
       "fsCapwapMulticast6WorkingMode": fsCapwapMulticast6WorkingMode,
       "fsCapwapMulticast6Group": fsCapwapMulticast6Group,
       "fsCapwapMulticast6MIBConformance": fsCapwapMulticast6MIBConformance,
       "fsCapwapMulticast6MIBCompliances": fsCapwapMulticast6MIBCompliances,
       "fsCapwapMulticast6MIBCompliance": fsCapwapMulticast6MIBCompliance,
       "fsCapwapMulticast6MIBGroups": fsCapwapMulticast6MIBGroups,
       "fsCapwapMulticast6MIBGroup": fsCapwapMulticast6MIBGroup}
)
