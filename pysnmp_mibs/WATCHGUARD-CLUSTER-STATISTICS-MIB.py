# SNMP MIB module (WATCHGUARD-CLUSTER-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/watchguard/WATCHGUARD-CLUSTER-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:17:41 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-SMI",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
if mibBuilder.loadTexts:
    wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgClusterStatusMIB_ObjectIdentity = ObjectIdentity
wgClusterStatusMIB = _WgClusterStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6)
)
if mibBuilder.loadTexts:
    wgClusterStatusMIB.setStatus("current")


class _WgClusterEnabled_Type(Integer32):
    """Custom type wgClusterEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WgClusterEnabled_Type.__name__ = "Integer32"
_WgClusterEnabled_Object = MibScalar
wgClusterEnabled = _WgClusterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1),
    _WgClusterEnabled_Type()
)
wgClusterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClusterEnabled.setStatus("current")


class _WgFirstMemberId_Type(OctetString):
    """Custom type wgFirstMemberId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WgFirstMemberId_Type.__name__ = "OctetString"
_WgFirstMemberId_Object = MibScalar
wgFirstMemberId = _WgFirstMemberId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2),
    _WgFirstMemberId_Type()
)
wgFirstMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFirstMemberId.setStatus("current")


class _WgFirstMemberRole_Type(Integer32):
    """Custom type wgFirstMemberRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("worker", 1),
          ("backup", 2),
          ("master", 3),
          ("idle", 4),
          ("standby", 5))
    )


_WgFirstMemberRole_Type.__name__ = "Integer32"
_WgFirstMemberRole_Object = MibScalar
wgFirstMemberRole = _WgFirstMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 3),
    _WgFirstMemberRole_Type()
)
wgFirstMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFirstMemberRole.setStatus("current")
_WgFirstMemberSystemHealth_Type = Integer32
_WgFirstMemberSystemHealth_Object = MibScalar
wgFirstMemberSystemHealth = _WgFirstMemberSystemHealth_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 4),
    _WgFirstMemberSystemHealth_Type()
)
wgFirstMemberSystemHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFirstMemberSystemHealth.setStatus("current")
_WgFirstMemberHardwareHealth_Type = Integer32
_WgFirstMemberHardwareHealth_Object = MibScalar
wgFirstMemberHardwareHealth = _WgFirstMemberHardwareHealth_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 5),
    _WgFirstMemberHardwareHealth_Type()
)
wgFirstMemberHardwareHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFirstMemberHardwareHealth.setStatus("current")
_WgFirstMemberMonitorPortHealth_Type = Integer32
_WgFirstMemberMonitorPortHealth_Object = MibScalar
wgFirstMemberMonitorPortHealth = _WgFirstMemberMonitorPortHealth_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 6),
    _WgFirstMemberMonitorPortHealth_Type()
)
wgFirstMemberMonitorPortHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFirstMemberMonitorPortHealth.setStatus("current")
_WgFirstMemberWeightAvg_Type = Integer32
_WgFirstMemberWeightAvg_Object = MibScalar
wgFirstMemberWeightAvg = _WgFirstMemberWeightAvg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 7),
    _WgFirstMemberWeightAvg_Type()
)
wgFirstMemberWeightAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFirstMemberWeightAvg.setStatus("current")


class _WgSecondMemberId_Type(OctetString):
    """Custom type wgSecondMemberId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WgSecondMemberId_Type.__name__ = "OctetString"
_WgSecondMemberId_Object = MibScalar
wgSecondMemberId = _WgSecondMemberId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 8),
    _WgSecondMemberId_Type()
)
wgSecondMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSecondMemberId.setStatus("current")


class _WgSecondMemberRole_Type(Integer32):
    """Custom type wgSecondMemberRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("worker", 1),
          ("backup", 2),
          ("master", 3),
          ("idle", 4),
          ("standby", 5))
    )


_WgSecondMemberRole_Type.__name__ = "Integer32"
_WgSecondMemberRole_Object = MibScalar
wgSecondMemberRole = _WgSecondMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 9),
    _WgSecondMemberRole_Type()
)
wgSecondMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSecondMemberRole.setStatus("current")
_WgSecondMemberSystemHealth_Type = Integer32
_WgSecondMemberSystemHealth_Object = MibScalar
wgSecondMemberSystemHealth = _WgSecondMemberSystemHealth_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 10),
    _WgSecondMemberSystemHealth_Type()
)
wgSecondMemberSystemHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSecondMemberSystemHealth.setStatus("current")
_WgSecondMemberHardwareHealth_Type = Integer32
_WgSecondMemberHardwareHealth_Object = MibScalar
wgSecondMemberHardwareHealth = _WgSecondMemberHardwareHealth_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 11),
    _WgSecondMemberHardwareHealth_Type()
)
wgSecondMemberHardwareHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSecondMemberHardwareHealth.setStatus("current")
_WgSecondMemberMonitorPortHealth_Type = Integer32
_WgSecondMemberMonitorPortHealth_Object = MibScalar
wgSecondMemberMonitorPortHealth = _WgSecondMemberMonitorPortHealth_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 12),
    _WgSecondMemberMonitorPortHealth_Type()
)
wgSecondMemberMonitorPortHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSecondMemberMonitorPortHealth.setStatus("current")
_WgSecondMemberWeightAvg_Type = Integer32
_WgSecondMemberWeightAvg_Object = MibScalar
wgSecondMemberWeightAvg = _WgSecondMemberWeightAvg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 13),
    _WgSecondMemberWeightAvg_Type()
)
wgSecondMemberWeightAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgSecondMemberWeightAvg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-CLUSTER-STATISTICS-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgClusterStatusMIB": wgClusterStatusMIB,
       "wgClusterEnabled": wgClusterEnabled,
       "wgFirstMemberId": wgFirstMemberId,
       "wgFirstMemberRole": wgFirstMemberRole,
       "wgFirstMemberSystemHealth": wgFirstMemberSystemHealth,
       "wgFirstMemberHardwareHealth": wgFirstMemberHardwareHealth,
       "wgFirstMemberMonitorPortHealth": wgFirstMemberMonitorPortHealth,
       "wgFirstMemberWeightAvg": wgFirstMemberWeightAvg,
       "wgSecondMemberId": wgSecondMemberId,
       "wgSecondMemberRole": wgSecondMemberRole,
       "wgSecondMemberSystemHealth": wgSecondMemberSystemHealth,
       "wgSecondMemberHardwareHealth": wgSecondMemberHardwareHealth,
       "wgSecondMemberMonitorPortHealth": wgSecondMemberMonitorPortHealth,
       "wgSecondMemberWeightAvg": wgSecondMemberWeightAvg}
)
