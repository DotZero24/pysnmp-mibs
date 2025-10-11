# SNMP MIB module (INFINET-EXTCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-EXTCES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:04 2025
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

(externalDevices,) = mibBuilder.importSymbols(
    "INFINET-EXTDEVICES-MIB",
    "externalDevices")

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

cesOverWlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1)
)
if mibBuilder.loadTexts:
    cesOverWlan.setRevisions(
        ("2007-06-18 19:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesOverWlanUnit0_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0 = _CesOverWlanUnit0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1)
)
_CesOverWlanUnit0Settings_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0Settings = _CesOverWlanUnit0Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1)
)


class _CesOverWlanUnit0Enabled_Type(Integer32):
    """Custom type cesOverWlanUnit0Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CesOverWlanUnit0Enabled_Type.__name__ = "Integer32"
_CesOverWlanUnit0Enabled_Object = MibScalar
cesOverWlanUnit0Enabled = _CesOverWlanUnit0Enabled_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 1),
    _CesOverWlanUnit0Enabled_Type()
)
cesOverWlanUnit0Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Enabled.setStatus("current")


class _CesOverWlanUnit0Mode_Type(Integer32):
    """Custom type cesOverWlanUnit0Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              6,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("e1-internal", 0),
          ("e1-loopback", 2),
          ("e1-recovery", 3),
          ("e1-line", 4),
          ("t1-internal", 6),
          ("t1-loopback", 8),
          ("t1-recovery", 9),
          ("t1-line", 10))
    )


_CesOverWlanUnit0Mode_Type.__name__ = "Integer32"
_CesOverWlanUnit0Mode_Object = MibScalar
cesOverWlanUnit0Mode = _CesOverWlanUnit0Mode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 2),
    _CesOverWlanUnit0Mode_Type()
)
cesOverWlanUnit0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0Mode.setStatus("current")


class _CesOverWlanUnit0MaxJitter_Type(Integer32):
    """Custom type cesOverWlanUnit0MaxJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CesOverWlanUnit0MaxJitter_Type.__name__ = "Integer32"
_CesOverWlanUnit0MaxJitter_Object = MibScalar
cesOverWlanUnit0MaxJitter = _CesOverWlanUnit0MaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 3),
    _CesOverWlanUnit0MaxJitter_Type()
)
cesOverWlanUnit0MaxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0MaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    cesOverWlanUnit0MaxJitter.setUnits("milliseconds")


class _CesOverWlanUnit0FramesPerPacket_Type(Integer32):
    """Custom type cesOverWlanUnit0FramesPerPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CesOverWlanUnit0FramesPerPacket_Type.__name__ = "Integer32"
_CesOverWlanUnit0FramesPerPacket_Object = MibScalar
cesOverWlanUnit0FramesPerPacket = _CesOverWlanUnit0FramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 4),
    _CesOverWlanUnit0FramesPerPacket_Type()
)
cesOverWlanUnit0FramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0FramesPerPacket.setStatus("current")
if mibBuilder.loadTexts:
    cesOverWlanUnit0FramesPerPacket.setUnits("frames")
_CesOverWlanUnit0BandwithLimit_Type = Unsigned32
_CesOverWlanUnit0BandwithLimit_Object = MibScalar
cesOverWlanUnit0BandwithLimit = _CesOverWlanUnit0BandwithLimit_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 5),
    _CesOverWlanUnit0BandwithLimit_Type()
)
cesOverWlanUnit0BandwithLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0BandwithLimit.setStatus("current")
_CesOverWlanUnit0PortMap_Type = Unsigned32
_CesOverWlanUnit0PortMap_Object = MibScalar
cesOverWlanUnit0PortMap = _CesOverWlanUnit0PortMap_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 6),
    _CesOverWlanUnit0PortMap_Type()
)
cesOverWlanUnit0PortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PortMap.setStatus("current")
_CesOverWlanMIBConformance_ObjectIdentity = ObjectIdentity
cesOverWlanMIBConformance = _CesOverWlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 2)
)

# Managed Objects groups

cesOverWlanGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 2, 1)
)
cesOverWlanGroups.setObjects(
      *(("INFINET-EXTCES-MIB", "cesOverWlanUnit0Enabled"),
        ("INFINET-EXTCES-MIB", "cesOverWlanUnit0Mode"),
        ("INFINET-EXTCES-MIB", "cesOverWlanUnit0MaxJitter"),
        ("INFINET-EXTCES-MIB", "cesOverWlanUnit0FramesPerPacket"),
        ("INFINET-EXTCES-MIB", "cesOverWlanUnit0BandwithLimit"),
        ("INFINET-EXTCES-MIB", "cesOverWlanUnit0PortMap"))
)
if mibBuilder.loadTexts:
    cesOverWlanGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-EXTCES-MIB",
    **{"cesOverWlan": cesOverWlan,
       "cesOverWlanUnit0": cesOverWlanUnit0,
       "cesOverWlanUnit0Settings": cesOverWlanUnit0Settings,
       "cesOverWlanUnit0Enabled": cesOverWlanUnit0Enabled,
       "cesOverWlanUnit0Mode": cesOverWlanUnit0Mode,
       "cesOverWlanUnit0MaxJitter": cesOverWlanUnit0MaxJitter,
       "cesOverWlanUnit0FramesPerPacket": cesOverWlanUnit0FramesPerPacket,
       "cesOverWlanUnit0BandwithLimit": cesOverWlanUnit0BandwithLimit,
       "cesOverWlanUnit0PortMap": cesOverWlanUnit0PortMap,
       "cesOverWlanMIBConformance": cesOverWlanMIBConformance,
       "cesOverWlanGroups": cesOverWlanGroups}
)
