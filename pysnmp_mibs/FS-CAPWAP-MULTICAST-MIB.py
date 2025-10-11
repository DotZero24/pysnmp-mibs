# SNMP MIB module (FS-CAPWAP-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CAPWAP-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:34 2025
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

fsCapwapMulticastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59)
)
if mibBuilder.loadTexts:
    fsCapwapMulticastMIB.setRevisions(
        ("2009-10-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCapwapMulticastMIBObjects_ObjectIdentity = ObjectIdentity
fsCapwapMulticastMIBObjects = _FsCapwapMulticastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 1)
)


class _FsCapwapMulticastWorkingMode_Type(Integer32):
    """Custom type fsCapwapMulticastWorkingMode based on Integer32"""
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


_FsCapwapMulticastWorkingMode_Type.__name__ = "Integer32"
_FsCapwapMulticastWorkingMode_Object = MibScalar
fsCapwapMulticastWorkingMode = _FsCapwapMulticastWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 1, 1),
    _FsCapwapMulticastWorkingMode_Type()
)
fsCapwapMulticastWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapMulticastWorkingMode.setStatus("current")
_FsCapwapMulticastGroup_Type = IpAddress
_FsCapwapMulticastGroup_Object = MibScalar
fsCapwapMulticastGroup = _FsCapwapMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 1, 2),
    _FsCapwapMulticastGroup_Type()
)
fsCapwapMulticastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapMulticastGroup.setStatus("current")
_FsCapwapMulticastMIBConformance_ObjectIdentity = ObjectIdentity
fsCapwapMulticastMIBConformance = _FsCapwapMulticastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2)
)
_FsCapwapMulticastMIBCompliances_ObjectIdentity = ObjectIdentity
fsCapwapMulticastMIBCompliances = _FsCapwapMulticastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 1)
)
_FsCapwapMulticastMIBGroups_ObjectIdentity = ObjectIdentity
fsCapwapMulticastMIBGroups = _FsCapwapMulticastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 2)
)

# Managed Objects groups

fsCapwapMulticastMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 2, 1)
)
fsCapwapMulticastMIBGroup.setObjects(
      *(("FS-CAPWAP-MULTICAST-MIB", "fsCapwapMulticastWorkingMode"),
        ("FS-CAPWAP-MULTICAST-MIB", "fsCapwapMulticastGroup"))
)
if mibBuilder.loadTexts:
    fsCapwapMulticastMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsCapwapMulticastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 1, 1)
)
fsCapwapMulticastMIBCompliance.setObjects(
    ("FS-CAPWAP-MULTICAST-MIB", "fsCapwapMulticastMIBGroup")
)
if mibBuilder.loadTexts:
    fsCapwapMulticastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CAPWAP-MULTICAST-MIB",
    **{"fsCapwapMulticastMIB": fsCapwapMulticastMIB,
       "fsCapwapMulticastMIBObjects": fsCapwapMulticastMIBObjects,
       "fsCapwapMulticastWorkingMode": fsCapwapMulticastWorkingMode,
       "fsCapwapMulticastGroup": fsCapwapMulticastGroup,
       "fsCapwapMulticastMIBConformance": fsCapwapMulticastMIBConformance,
       "fsCapwapMulticastMIBCompliances": fsCapwapMulticastMIBCompliances,
       "fsCapwapMulticastMIBCompliance": fsCapwapMulticastMIBCompliance,
       "fsCapwapMulticastMIBGroups": fsCapwapMulticastMIBGroups,
       "fsCapwapMulticastMIBGroup": fsCapwapMulticastMIBGroup}
)
