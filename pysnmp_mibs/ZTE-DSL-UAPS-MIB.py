# SNMP MIB module (ZTE-DSL-UAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-UAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:06 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

zxDslUapsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslUapsObjects_ObjectIdentity = ObjectIdentity
zxDslUapsObjects = _ZxDslUapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1)
)


class _ZxDslUapsPortMode_Type(Integer32):
    """Custom type zxDslUapsPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uaps", 1),
          ("trunk", 2),
          ("uplink", 3))
    )


_ZxDslUapsPortMode_Type.__name__ = "Integer32"
_ZxDslUapsPortMode_Object = MibScalar
zxDslUapsPortMode = _ZxDslUapsPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 1),
    _ZxDslUapsPortMode_Type()
)
zxDslUapsPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslUapsPortMode.setStatus("current")
_ZxDslUapsPrimaryPort_Type = Integer32
_ZxDslUapsPrimaryPort_Object = MibScalar
zxDslUapsPrimaryPort = _ZxDslUapsPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 2),
    _ZxDslUapsPrimaryPort_Type()
)
zxDslUapsPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslUapsPrimaryPort.setStatus("current")
_ZxDslUapsAutoFailbackEnable_Type = Integer32
_ZxDslUapsAutoFailbackEnable_Object = MibScalar
zxDslUapsAutoFailbackEnable = _ZxDslUapsAutoFailbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 3),
    _ZxDslUapsAutoFailbackEnable_Type()
)
zxDslUapsAutoFailbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslUapsAutoFailbackEnable.setStatus("current")


class _ZxDslUapsProtectionTime_Type(Integer32):
    """Custom type zxDslUapsProtectionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 900),
    )


_ZxDslUapsProtectionTime_Type.__name__ = "Integer32"
_ZxDslUapsProtectionTime_Object = MibScalar
zxDslUapsProtectionTime = _ZxDslUapsProtectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 4),
    _ZxDslUapsProtectionTime_Type()
)
zxDslUapsProtectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslUapsProtectionTime.setStatus("current")
if mibBuilder.loadTexts:
    zxDslUapsProtectionTime.setUnits("second")
_ZxDslUapsForceSwap_Type = Integer32
_ZxDslUapsForceSwap_Object = MibScalar
zxDslUapsForceSwap = _ZxDslUapsForceSwap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 5),
    _ZxDslUapsForceSwap_Type()
)
zxDslUapsForceSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslUapsForceSwap.setStatus("current")


class _ZxDslUapsPortWorkingStatus_Type(Integer32):
    """Custom type zxDslUapsPortWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryPortInWorking", 1),
          ("secondaryPortInWorking", 2))
    )


_ZxDslUapsPortWorkingStatus_Type.__name__ = "Integer32"
_ZxDslUapsPortWorkingStatus_Object = MibScalar
zxDslUapsPortWorkingStatus = _ZxDslUapsPortWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 6),
    _ZxDslUapsPortWorkingStatus_Type()
)
zxDslUapsPortWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslUapsPortWorkingStatus.setStatus("current")


class _ZxDslUapsPortOperStatus_Type(Bits):
    """Custom type zxDslUapsPortOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("primaryPort", 0),
          ("secondaryPort", 1))
    )

_ZxDslUapsPortOperStatus_Type.__name__ = "Bits"
_ZxDslUapsPortOperStatus_Object = MibScalar
zxDslUapsPortOperStatus = _ZxDslUapsPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 7),
    _ZxDslUapsPortOperStatus_Type()
)
zxDslUapsPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslUapsPortOperStatus.setStatus("current")
_ZxDslUapsIsInPrtctTime_Type = TruthValue
_ZxDslUapsIsInPrtctTime_Object = MibScalar
zxDslUapsIsInPrtctTime = _ZxDslUapsIsInPrtctTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 8),
    _ZxDslUapsIsInPrtctTime_Type()
)
zxDslUapsIsInPrtctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslUapsIsInPrtctTime.setStatus("current")


class _ZxDslUapsSwapRequestStatus_Type(Integer32):
    """Custom type zxDslUapsSwapRequestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("existRequest", 1),
          ("noRequest", 2))
    )


_ZxDslUapsSwapRequestStatus_Type.__name__ = "Integer32"
_ZxDslUapsSwapRequestStatus_Object = MibScalar
zxDslUapsSwapRequestStatus = _ZxDslUapsSwapRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 9),
    _ZxDslUapsSwapRequestStatus_Type()
)
zxDslUapsSwapRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslUapsSwapRequestStatus.setStatus("current")


class _ZxDslUapsSwapReason_Type(Bits):
    """Custom type zxDslUapsSwapReason based on Bits"""
    namedValues = NamedValues(
        *(("failback", 0),
          ("failover", 1),
          ("forceSwap", 2))
    )

_ZxDslUapsSwapReason_Type.__name__ = "Bits"
_ZxDslUapsSwapReason_Object = MibScalar
zxDslUapsSwapReason = _ZxDslUapsSwapReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 1, 10),
    _ZxDslUapsSwapReason_Type()
)
zxDslUapsSwapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslUapsSwapReason.setStatus("current")
_ZxDslUapsTraps_ObjectIdentity = ObjectIdentity
zxDslUapsTraps = _ZxDslUapsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 2)
)

# Managed Objects groups


# Notification objects

zxDslUapsSwappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 33, 2, 1)
)
zxDslUapsSwappedTrap.setObjects(
      *(("ZTE-DSL-UAPS-MIB", "zxDslUapsPortWorkingStatus"),
        ("ZTE-DSL-UAPS-MIB", "zxDslUapsPortOperStatus"),
        ("ZTE-DSL-UAPS-MIB", "zxDslUapsSwapReason"))
)
if mibBuilder.loadTexts:
    zxDslUapsSwappedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-UAPS-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxDslUapsMib": zxDslUapsMib,
       "zxDslUapsObjects": zxDslUapsObjects,
       "zxDslUapsPortMode": zxDslUapsPortMode,
       "zxDslUapsPrimaryPort": zxDslUapsPrimaryPort,
       "zxDslUapsAutoFailbackEnable": zxDslUapsAutoFailbackEnable,
       "zxDslUapsProtectionTime": zxDslUapsProtectionTime,
       "zxDslUapsForceSwap": zxDslUapsForceSwap,
       "zxDslUapsPortWorkingStatus": zxDslUapsPortWorkingStatus,
       "zxDslUapsPortOperStatus": zxDslUapsPortOperStatus,
       "zxDslUapsIsInPrtctTime": zxDslUapsIsInPrtctTime,
       "zxDslUapsSwapRequestStatus": zxDslUapsSwapRequestStatus,
       "zxDslUapsSwapReason": zxDslUapsSwapReason,
       "zxDslUapsTraps": zxDslUapsTraps,
       "zxDslUapsSwappedTrap": zxDslUapsSwappedTrap}
)
