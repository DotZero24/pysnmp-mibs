# SNMP MIB module (ZYXEL-LOAD-SHARING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-LOAD-SHARING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:24 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelLoadSharing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLoadSharingSetup_ObjectIdentity = ObjectIdentity
zyxelLoadSharingSetup = _ZyxelLoadSharingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1)
)
_ZyLoadSharingState_Type = EnabledStatus
_ZyLoadSharingState_Object = MibScalar
zyLoadSharingState = _ZyLoadSharingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 1),
    _ZyLoadSharingState_Type()
)
zyLoadSharingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingState.setStatus("current")


class _ZyLoadSharingCriteria_Type(Integer32):
    """Custom type zyLoadSharingCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srcIp", 1),
          ("srcDstIp", 2))
    )


_ZyLoadSharingCriteria_Type.__name__ = "Integer32"
_ZyLoadSharingCriteria_Object = MibScalar
zyLoadSharingCriteria = _ZyLoadSharingCriteria_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 2),
    _ZyLoadSharingCriteria_Type()
)
zyLoadSharingCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingCriteria.setStatus("current")
_ZyLoadSharingAgingTime_Type = Integer32
_ZyLoadSharingAgingTime_Object = MibScalar
zyLoadSharingAgingTime = _ZyLoadSharingAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 3),
    _ZyLoadSharingAgingTime_Type()
)
zyLoadSharingAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingAgingTime.setStatus("current")
_ZyLoadSharingDiscoverTime_Type = Integer32
_ZyLoadSharingDiscoverTime_Object = MibScalar
zyLoadSharingDiscoverTime = _ZyLoadSharingDiscoverTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 4),
    _ZyLoadSharingDiscoverTime_Type()
)
zyLoadSharingDiscoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingDiscoverTime.setStatus("current")
_ZyLoadSharingMaxPaths_Type = Integer32
_ZyLoadSharingMaxPaths_Object = MibScalar
zyLoadSharingMaxPaths = _ZyLoadSharingMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 5),
    _ZyLoadSharingMaxPaths_Type()
)
zyLoadSharingMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoadSharingMaxPaths.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LOAD-SHARING-MIB",
    **{"zyxelLoadSharing": zyxelLoadSharing,
       "zyxelLoadSharingSetup": zyxelLoadSharingSetup,
       "zyLoadSharingState": zyLoadSharingState,
       "zyLoadSharingCriteria": zyLoadSharingCriteria,
       "zyLoadSharingAgingTime": zyLoadSharingAgingTime,
       "zyLoadSharingDiscoverTime": zyLoadSharingDiscoverTime,
       "zyLoadSharingMaxPaths": zyLoadSharingMaxPaths}
)
