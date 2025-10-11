# SNMP MIB module (ZTE-AN-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-LDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:40 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAnL3IfIndex,) = mibBuilder.importSymbols(
    "ZTE-AN-L3-IF-MIB",
    "zxAnL3IfIndex")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnLdpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnLdpGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnLdpGlobalObjects = _ZxAnLdpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1)
)


class _ZxAnLdpMplsEnable_Type(Integer32):
    """Custom type zxAnLdpMplsEnable based on Integer32"""
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


_ZxAnLdpMplsEnable_Type.__name__ = "Integer32"
_ZxAnLdpMplsEnable_Object = MibScalar
zxAnLdpMplsEnable = _ZxAnLdpMplsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 1),
    _ZxAnLdpMplsEnable_Type()
)
zxAnLdpMplsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsEnable.setStatus("current")


class _ZxAnLdpMplsMinLabel_Type(Integer32):
    """Custom type zxAnLdpMplsMinLabel based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnLdpMplsMinLabel_Type.__name__ = "Integer32"
_ZxAnLdpMplsMinLabel_Object = MibScalar
zxAnLdpMplsMinLabel = _ZxAnLdpMplsMinLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 2),
    _ZxAnLdpMplsMinLabel_Type()
)
zxAnLdpMplsMinLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsMinLabel.setStatus("current")


class _ZxAnLdpMplsMaxLabel_Type(Integer32):
    """Custom type zxAnLdpMplsMaxLabel based on Integer32"""
    defaultValue = 100000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnLdpMplsMaxLabel_Type.__name__ = "Integer32"
_ZxAnLdpMplsMaxLabel_Object = MibScalar
zxAnLdpMplsMaxLabel = _ZxAnLdpMplsMaxLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 3),
    _ZxAnLdpMplsMaxLabel_Type()
)
zxAnLdpMplsMaxLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsMaxLabel.setStatus("current")


class _ZxAnLdpMplsLdpRouterId_Type(Integer32):
    """Custom type zxAnLdpMplsLdpRouterId based on Integer32"""
    defaultValue = 0


_ZxAnLdpMplsLdpRouterId_Type.__name__ = "Integer32"
_ZxAnLdpMplsLdpRouterId_Object = MibScalar
zxAnLdpMplsLdpRouterId = _ZxAnLdpMplsLdpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 4),
    _ZxAnLdpMplsLdpRouterId_Type()
)
zxAnLdpMplsLdpRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsLdpRouterId.setStatus("current")


class _ZxAnLdpMplsLdpRouterIdForce_Type(Integer32):
    """Custom type zxAnLdpMplsLdpRouterIdForce based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_ZxAnLdpMplsLdpRouterIdForce_Type.__name__ = "Integer32"
_ZxAnLdpMplsLdpRouterIdForce_Object = MibScalar
zxAnLdpMplsLdpRouterIdForce = _ZxAnLdpMplsLdpRouterIdForce_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 5),
    _ZxAnLdpMplsLdpRouterIdForce_Type()
)
zxAnLdpMplsLdpRouterIdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsLdpRouterIdForce.setStatus("current")


class _ZxAnLdpMplsExplicitNullEnable_Type(Integer32):
    """Custom type zxAnLdpMplsExplicitNullEnable based on Integer32"""
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


_ZxAnLdpMplsExplicitNullEnable_Type.__name__ = "Integer32"
_ZxAnLdpMplsExplicitNullEnable_Object = MibScalar
zxAnLdpMplsExplicitNullEnable = _ZxAnLdpMplsExplicitNullEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 6),
    _ZxAnLdpMplsExplicitNullEnable_Type()
)
zxAnLdpMplsExplicitNullEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsExplicitNullEnable.setStatus("current")


class _ZxAnLdpMplsMinInUseLabel_Type(Integer32):
    """Custom type zxAnLdpMplsMinInUseLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnLdpMplsMinInUseLabel_Type.__name__ = "Integer32"
_ZxAnLdpMplsMinInUseLabel_Object = MibScalar
zxAnLdpMplsMinInUseLabel = _ZxAnLdpMplsMinInUseLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 7),
    _ZxAnLdpMplsMinInUseLabel_Type()
)
zxAnLdpMplsMinInUseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLdpMplsMinInUseLabel.setStatus("current")


class _ZxAnLdpMplsMaxInUseLabel_Type(Integer32):
    """Custom type zxAnLdpMplsMaxInUseLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_ZxAnLdpMplsMaxInUseLabel_Type.__name__ = "Integer32"
_ZxAnLdpMplsMaxInUseLabel_Object = MibScalar
zxAnLdpMplsMaxInUseLabel = _ZxAnLdpMplsMaxInUseLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 8),
    _ZxAnLdpMplsMaxInUseLabel_Type()
)
zxAnLdpMplsMaxInUseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLdpMplsMaxInUseLabel.setStatus("current")


class _ZxAnLdpMplsSessInitBackoffTime_Type(Integer32):
    """Custom type zxAnLdpMplsSessInitBackoffTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_ZxAnLdpMplsSessInitBackoffTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsSessInitBackoffTime_Object = MibScalar
zxAnLdpMplsSessInitBackoffTime = _ZxAnLdpMplsSessInitBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 9),
    _ZxAnLdpMplsSessInitBackoffTime_Type()
)
zxAnLdpMplsSessInitBackoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsSessInitBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsSessInitBackoffTime.setUnits("seconds")


class _ZxAnLdpMplsSessMaxBackoffTime_Type(Integer32):
    """Custom type zxAnLdpMplsSessMaxBackoffTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_ZxAnLdpMplsSessMaxBackoffTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsSessMaxBackoffTime_Object = MibScalar
zxAnLdpMplsSessMaxBackoffTime = _ZxAnLdpMplsSessMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 10),
    _ZxAnLdpMplsSessMaxBackoffTime_Type()
)
zxAnLdpMplsSessMaxBackoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsSessMaxBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsSessMaxBackoffTime.setUnits("seconds")


class _ZxAnLdpMplsSessKeepAliveTime_Type(Integer32):
    """Custom type zxAnLdpMplsSessKeepAliveTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_ZxAnLdpMplsSessKeepAliveTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsSessKeepAliveTime_Object = MibScalar
zxAnLdpMplsSessKeepAliveTime = _ZxAnLdpMplsSessKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 11),
    _ZxAnLdpMplsSessKeepAliveTime_Type()
)
zxAnLdpMplsSessKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsSessKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsSessKeepAliveTime.setUnits("seconds")


class _ZxAnLdpMplsGrEnable_Type(Integer32):
    """Custom type zxAnLdpMplsGrEnable based on Integer32"""
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


_ZxAnLdpMplsGrEnable_Type.__name__ = "Integer32"
_ZxAnLdpMplsGrEnable_Object = MibScalar
zxAnLdpMplsGrEnable = _ZxAnLdpMplsGrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 12),
    _ZxAnLdpMplsGrEnable_Type()
)
zxAnLdpMplsGrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsGrEnable.setStatus("current")


class _ZxAnLdpMplsGrRecoveryTime_Type(Integer32):
    """Custom type zxAnLdpMplsGrRecoveryTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_ZxAnLdpMplsGrRecoveryTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsGrRecoveryTime_Object = MibScalar
zxAnLdpMplsGrRecoveryTime = _ZxAnLdpMplsGrRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 13),
    _ZxAnLdpMplsGrRecoveryTime_Type()
)
zxAnLdpMplsGrRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsGrRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsGrRecoveryTime.setUnits("seconds")


class _ZxAnLdpMplsGrNeighKeepAliveTime_Type(Integer32):
    """Custom type zxAnLdpMplsGrNeighKeepAliveTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_ZxAnLdpMplsGrNeighKeepAliveTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsGrNeighKeepAliveTime_Object = MibScalar
zxAnLdpMplsGrNeighKeepAliveTime = _ZxAnLdpMplsGrNeighKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 14),
    _ZxAnLdpMplsGrNeighKeepAliveTime_Type()
)
zxAnLdpMplsGrNeighKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsGrNeighKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsGrNeighKeepAliveTime.setUnits("seconds")


class _ZxAnLdpMplsVpnGrEnable_Type(Integer32):
    """Custom type zxAnLdpMplsVpnGrEnable based on Integer32"""
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


_ZxAnLdpMplsVpnGrEnable_Type.__name__ = "Integer32"
_ZxAnLdpMplsVpnGrEnable_Object = MibScalar
zxAnLdpMplsVpnGrEnable = _ZxAnLdpMplsVpnGrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 15),
    _ZxAnLdpMplsVpnGrEnable_Type()
)
zxAnLdpMplsVpnGrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsVpnGrEnable.setStatus("current")


class _ZxAnLdpMplsHelloHoldTime_Type(Integer32):
    """Custom type zxAnLdpMplsHelloHoldTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_ZxAnLdpMplsHelloHoldTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsHelloHoldTime_Object = MibScalar
zxAnLdpMplsHelloHoldTime = _ZxAnLdpMplsHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 16),
    _ZxAnLdpMplsHelloHoldTime_Type()
)
zxAnLdpMplsHelloHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsHelloHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsHelloHoldTime.setUnits("seconds")


class _ZxAnLdpMplsHelloSendInterval_Type(Integer32):
    """Custom type zxAnLdpMplsHelloSendInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnLdpMplsHelloSendInterval_Type.__name__ = "Integer32"
_ZxAnLdpMplsHelloSendInterval_Object = MibScalar
zxAnLdpMplsHelloSendInterval = _ZxAnLdpMplsHelloSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 17),
    _ZxAnLdpMplsHelloSendInterval_Type()
)
zxAnLdpMplsHelloSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsHelloSendInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsHelloSendInterval.setUnits("seconds")


class _ZxAnLdpMplsTgtHelloHoldTime_Type(Integer32):
    """Custom type zxAnLdpMplsTgtHelloHoldTime based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_ZxAnLdpMplsTgtHelloHoldTime_Type.__name__ = "Integer32"
_ZxAnLdpMplsTgtHelloHoldTime_Object = MibScalar
zxAnLdpMplsTgtHelloHoldTime = _ZxAnLdpMplsTgtHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 18),
    _ZxAnLdpMplsTgtHelloHoldTime_Type()
)
zxAnLdpMplsTgtHelloHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsTgtHelloHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsTgtHelloHoldTime.setUnits("seconds")


class _ZxAnLdpMplsTgtHelloSendInterval_Type(Integer32):
    """Custom type zxAnLdpMplsTgtHelloSendInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnLdpMplsTgtHelloSendInterval_Type.__name__ = "Integer32"
_ZxAnLdpMplsTgtHelloSendInterval_Object = MibScalar
zxAnLdpMplsTgtHelloSendInterval = _ZxAnLdpMplsTgtHelloSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 19),
    _ZxAnLdpMplsTgtHelloSendInterval_Type()
)
zxAnLdpMplsTgtHelloSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsTgtHelloSendInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLdpMplsTgtHelloSendInterval.setUnits("seconds")


class _ZxAnLdpMplsKeepSessWithHelloMsg_Type(Integer32):
    """Custom type zxAnLdpMplsKeepSessWithHelloMsg based on Integer32"""
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


_ZxAnLdpMplsKeepSessWithHelloMsg_Type.__name__ = "Integer32"
_ZxAnLdpMplsKeepSessWithHelloMsg_Object = MibScalar
zxAnLdpMplsKeepSessWithHelloMsg = _ZxAnLdpMplsKeepSessWithHelloMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 20),
    _ZxAnLdpMplsKeepSessWithHelloMsg_Type()
)
zxAnLdpMplsKeepSessWithHelloMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsKeepSessWithHelloMsg.setStatus("current")


class _ZxAnLdpMplsGrHelperEnable_Type(Integer32):
    """Custom type zxAnLdpMplsGrHelperEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnLdpMplsGrHelperEnable_Type.__name__ = "Integer32"
_ZxAnLdpMplsGrHelperEnable_Object = MibScalar
zxAnLdpMplsGrHelperEnable = _ZxAnLdpMplsGrHelperEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 21),
    _ZxAnLdpMplsGrHelperEnable_Type()
)
zxAnLdpMplsGrHelperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsGrHelperEnable.setStatus("current")


class _ZxAnLdpMplsLabelControlMode_Type(Integer32):
    """Custom type zxAnLdpMplsLabelControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordered", 1),
          ("independent", 2))
    )


_ZxAnLdpMplsLabelControlMode_Type.__name__ = "Integer32"
_ZxAnLdpMplsLabelControlMode_Object = MibScalar
zxAnLdpMplsLabelControlMode = _ZxAnLdpMplsLabelControlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 22),
    _ZxAnLdpMplsLabelControlMode_Type()
)
zxAnLdpMplsLabelControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsLabelControlMode.setStatus("current")


class _ZxAnLdpMplsLabelRetentionMode_Type(Integer32):
    """Custom type zxAnLdpMplsLabelRetentionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_ZxAnLdpMplsLabelRetentionMode_Type.__name__ = "Integer32"
_ZxAnLdpMplsLabelRetentionMode_Object = MibScalar
zxAnLdpMplsLabelRetentionMode = _ZxAnLdpMplsLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 23),
    _ZxAnLdpMplsLabelRetentionMode_Type()
)
zxAnLdpMplsLabelRetentionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsLabelRetentionMode.setStatus("current")


class _ZxAnLdpMplsPktWithLabelEnable_Type(Integer32):
    """Custom type zxAnLdpMplsPktWithLabelEnable based on Integer32"""
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


_ZxAnLdpMplsPktWithLabelEnable_Type.__name__ = "Integer32"
_ZxAnLdpMplsPktWithLabelEnable_Object = MibScalar
zxAnLdpMplsPktWithLabelEnable = _ZxAnLdpMplsPktWithLabelEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 1, 24),
    _ZxAnLdpMplsPktWithLabelEnable_Type()
)
zxAnLdpMplsPktWithLabelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpMplsPktWithLabelEnable.setStatus("current")
_ZxAnLdpObjects_ObjectIdentity = ObjectIdentity
zxAnLdpObjects = _ZxAnLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2)
)
_ZxAnLdpTargetSessionTable_Object = MibTable
zxAnLdpTargetSessionTable = _ZxAnLdpTargetSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnLdpTargetSessionTable.setStatus("current")
_ZxAnLdpTargetSessionEntry_Object = MibTableRow
zxAnLdpTargetSessionEntry = _ZxAnLdpTargetSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 3, 1)
)
zxAnLdpTargetSessionEntry.setIndexNames(
    (0, "ZTE-AN-LDP-MIB", "zxAnLdpTargetIpAddrType"),
    (0, "ZTE-AN-LDP-MIB", "zxAnLdpTargetIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnLdpTargetSessionEntry.setStatus("current")
_ZxAnLdpTargetIpAddrType_Type = InetAddressType
_ZxAnLdpTargetIpAddrType_Object = MibTableColumn
zxAnLdpTargetIpAddrType = _ZxAnLdpTargetIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 3, 1, 1),
    _ZxAnLdpTargetIpAddrType_Type()
)
zxAnLdpTargetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLdpTargetIpAddrType.setStatus("current")
_ZxAnLdpTargetIpAddr_Type = InetAddress
_ZxAnLdpTargetIpAddr_Object = MibTableColumn
zxAnLdpTargetIpAddr = _ZxAnLdpTargetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 3, 1, 2),
    _ZxAnLdpTargetIpAddr_Type()
)
zxAnLdpTargetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLdpTargetIpAddr.setStatus("current")


class _ZxAnLdpTargetDistributionMode_Type(Integer32):
    """Custom type zxAnLdpTargetDistributionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dod", 1),
          ("du", 2))
    )


_ZxAnLdpTargetDistributionMode_Type.__name__ = "Integer32"
_ZxAnLdpTargetDistributionMode_Object = MibTableColumn
zxAnLdpTargetDistributionMode = _ZxAnLdpTargetDistributionMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 3, 1, 3),
    _ZxAnLdpTargetDistributionMode_Type()
)
zxAnLdpTargetDistributionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpTargetDistributionMode.setStatus("current")
_ZxAnLdpTargetSessionRowStatus_Type = RowStatus
_ZxAnLdpTargetSessionRowStatus_Object = MibTableColumn
zxAnLdpTargetSessionRowStatus = _ZxAnLdpTargetSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 3, 1, 20),
    _ZxAnLdpTargetSessionRowStatus_Type()
)
zxAnLdpTargetSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpTargetSessionRowStatus.setStatus("current")
_ZxAnLdpSessionTable_Object = MibTable
zxAnLdpSessionTable = _ZxAnLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnLdpSessionTable.setStatus("current")
_ZxAnLdpSessionEntry_Object = MibTableRow
zxAnLdpSessionEntry = _ZxAnLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1)
)
zxAnLdpSessionEntry.setIndexNames(
    (0, "ZTE-AN-LDP-MIB", "zxAnLdpPeerIpAddrType"),
    (0, "ZTE-AN-LDP-MIB", "zxAnLdpPeerIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnLdpSessionEntry.setStatus("current")
_ZxAnLdpPeerIpAddrType_Type = InetAddressType
_ZxAnLdpPeerIpAddrType_Object = MibTableColumn
zxAnLdpPeerIpAddrType = _ZxAnLdpPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 1),
    _ZxAnLdpPeerIpAddrType_Type()
)
zxAnLdpPeerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLdpPeerIpAddrType.setStatus("current")
_ZxAnLdpPeerIpAddr_Type = InetAddress
_ZxAnLdpPeerIpAddr_Object = MibTableColumn
zxAnLdpPeerIpAddr = _ZxAnLdpPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 2),
    _ZxAnLdpPeerIpAddr_Type()
)
zxAnLdpPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLdpPeerIpAddr.setStatus("current")


class _ZxAnLdpMd5Pwd_Type(DisplayString):
    """Custom type zxAnLdpMd5Pwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 80),
    )


_ZxAnLdpMd5Pwd_Type.__name__ = "DisplayString"
_ZxAnLdpMd5Pwd_Object = MibTableColumn
zxAnLdpMd5Pwd = _ZxAnLdpMd5Pwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 3),
    _ZxAnLdpMd5Pwd_Type()
)
zxAnLdpMd5Pwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpMd5Pwd.setStatus("current")


class _ZxAnLdpMd5PwdConfStatus_Type(Integer32):
    """Custom type zxAnLdpMd5PwdConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPwd", 1),
          ("withPwd", 2))
    )


_ZxAnLdpMd5PwdConfStatus_Type.__name__ = "Integer32"
_ZxAnLdpMd5PwdConfStatus_Object = MibTableColumn
zxAnLdpMd5PwdConfStatus = _ZxAnLdpMd5PwdConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 4),
    _ZxAnLdpMd5PwdConfStatus_Type()
)
zxAnLdpMd5PwdConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLdpMd5PwdConfStatus.setStatus("current")


class _ZxAnLdpMd5PwdEncrypt_Type(Integer32):
    """Custom type zxAnLdpMd5PwdEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noEncrypt", 1),
          ("encrypt", 2))
    )


_ZxAnLdpMd5PwdEncrypt_Type.__name__ = "Integer32"
_ZxAnLdpMd5PwdEncrypt_Object = MibTableColumn
zxAnLdpMd5PwdEncrypt = _ZxAnLdpMd5PwdEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 5),
    _ZxAnLdpMd5PwdEncrypt_Type()
)
zxAnLdpMd5PwdEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpMd5PwdEncrypt.setStatus("current")


class _ZxAnLdpSessionReset_Type(Integer32):
    """Custom type zxAnLdpSessionReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_ZxAnLdpSessionReset_Type.__name__ = "Integer32"
_ZxAnLdpSessionReset_Object = MibTableColumn
zxAnLdpSessionReset = _ZxAnLdpSessionReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 6),
    _ZxAnLdpSessionReset_Type()
)
zxAnLdpSessionReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLdpSessionReset.setStatus("current")
_ZxAnLdpSessionRowStatus_Type = RowStatus
_ZxAnLdpSessionRowStatus_Object = MibTableColumn
zxAnLdpSessionRowStatus = _ZxAnLdpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 4, 1, 20),
    _ZxAnLdpSessionRowStatus_Type()
)
zxAnLdpSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpSessionRowStatus.setStatus("current")
_ZxAnLdpL3IfEntityTable_Object = MibTable
zxAnLdpL3IfEntityTable = _ZxAnLdpL3IfEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnLdpL3IfEntityTable.setStatus("current")
_ZxAnLdpL3IfEntityEntry_Object = MibTableRow
zxAnLdpL3IfEntityEntry = _ZxAnLdpL3IfEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5, 1)
)
zxAnLdpL3IfEntityEntry.setIndexNames(
    (0, "ZTE-AN-L3-IF-MIB", "zxAnL3IfIndex"),
)
if mibBuilder.loadTexts:
    zxAnLdpL3IfEntityEntry.setStatus("current")


class _ZxAnLdpL3IfTransAddrMode_Type(Integer32):
    """Custom type zxAnLdpL3IfTransAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 0),
          ("ifIp", 1),
          ("specifyIp", 2))
    )


_ZxAnLdpL3IfTransAddrMode_Type.__name__ = "Integer32"
_ZxAnLdpL3IfTransAddrMode_Object = MibTableColumn
zxAnLdpL3IfTransAddrMode = _ZxAnLdpL3IfTransAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5, 1, 1),
    _ZxAnLdpL3IfTransAddrMode_Type()
)
zxAnLdpL3IfTransAddrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpL3IfTransAddrMode.setStatus("current")
_ZxAnLdpL3IfTransAddrType_Type = InetAddressType
_ZxAnLdpL3IfTransAddrType_Object = MibTableColumn
zxAnLdpL3IfTransAddrType = _ZxAnLdpL3IfTransAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5, 1, 2),
    _ZxAnLdpL3IfTransAddrType_Type()
)
zxAnLdpL3IfTransAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpL3IfTransAddrType.setStatus("current")
_ZxAnLdpL3IfTransAddr_Type = InetAddress
_ZxAnLdpL3IfTransAddr_Object = MibTableColumn
zxAnLdpL3IfTransAddr = _ZxAnLdpL3IfTransAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5, 1, 3),
    _ZxAnLdpL3IfTransAddr_Type()
)
zxAnLdpL3IfTransAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpL3IfTransAddr.setStatus("current")


class _ZxAnLdpL3IfDistributionMode_Type(Integer32):
    """Custom type zxAnLdpL3IfDistributionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dod", 1),
          ("du", 2))
    )


_ZxAnLdpL3IfDistributionMode_Type.__name__ = "Integer32"
_ZxAnLdpL3IfDistributionMode_Object = MibTableColumn
zxAnLdpL3IfDistributionMode = _ZxAnLdpL3IfDistributionMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5, 1, 4),
    _ZxAnLdpL3IfDistributionMode_Type()
)
zxAnLdpL3IfDistributionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpL3IfDistributionMode.setStatus("current")
_ZxAnLdpL3IfEntityRowStatus_Type = RowStatus
_ZxAnLdpL3IfEntityRowStatus_Object = MibTableColumn
zxAnLdpL3IfEntityRowStatus = _ZxAnLdpL3IfEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 55, 2, 5, 1, 20),
    _ZxAnLdpL3IfEntityRowStatus_Type()
)
zxAnLdpL3IfEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLdpL3IfEntityRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-LDP-MIB",
    **{"zxAnLdpMib": zxAnLdpMib,
       "zxAnLdpGlobalObjects": zxAnLdpGlobalObjects,
       "zxAnLdpMplsEnable": zxAnLdpMplsEnable,
       "zxAnLdpMplsMinLabel": zxAnLdpMplsMinLabel,
       "zxAnLdpMplsMaxLabel": zxAnLdpMplsMaxLabel,
       "zxAnLdpMplsLdpRouterId": zxAnLdpMplsLdpRouterId,
       "zxAnLdpMplsLdpRouterIdForce": zxAnLdpMplsLdpRouterIdForce,
       "zxAnLdpMplsExplicitNullEnable": zxAnLdpMplsExplicitNullEnable,
       "zxAnLdpMplsMinInUseLabel": zxAnLdpMplsMinInUseLabel,
       "zxAnLdpMplsMaxInUseLabel": zxAnLdpMplsMaxInUseLabel,
       "zxAnLdpMplsSessInitBackoffTime": zxAnLdpMplsSessInitBackoffTime,
       "zxAnLdpMplsSessMaxBackoffTime": zxAnLdpMplsSessMaxBackoffTime,
       "zxAnLdpMplsSessKeepAliveTime": zxAnLdpMplsSessKeepAliveTime,
       "zxAnLdpMplsGrEnable": zxAnLdpMplsGrEnable,
       "zxAnLdpMplsGrRecoveryTime": zxAnLdpMplsGrRecoveryTime,
       "zxAnLdpMplsGrNeighKeepAliveTime": zxAnLdpMplsGrNeighKeepAliveTime,
       "zxAnLdpMplsVpnGrEnable": zxAnLdpMplsVpnGrEnable,
       "zxAnLdpMplsHelloHoldTime": zxAnLdpMplsHelloHoldTime,
       "zxAnLdpMplsHelloSendInterval": zxAnLdpMplsHelloSendInterval,
       "zxAnLdpMplsTgtHelloHoldTime": zxAnLdpMplsTgtHelloHoldTime,
       "zxAnLdpMplsTgtHelloSendInterval": zxAnLdpMplsTgtHelloSendInterval,
       "zxAnLdpMplsKeepSessWithHelloMsg": zxAnLdpMplsKeepSessWithHelloMsg,
       "zxAnLdpMplsGrHelperEnable": zxAnLdpMplsGrHelperEnable,
       "zxAnLdpMplsLabelControlMode": zxAnLdpMplsLabelControlMode,
       "zxAnLdpMplsLabelRetentionMode": zxAnLdpMplsLabelRetentionMode,
       "zxAnLdpMplsPktWithLabelEnable": zxAnLdpMplsPktWithLabelEnable,
       "zxAnLdpObjects": zxAnLdpObjects,
       "zxAnLdpTargetSessionTable": zxAnLdpTargetSessionTable,
       "zxAnLdpTargetSessionEntry": zxAnLdpTargetSessionEntry,
       "zxAnLdpTargetIpAddrType": zxAnLdpTargetIpAddrType,
       "zxAnLdpTargetIpAddr": zxAnLdpTargetIpAddr,
       "zxAnLdpTargetDistributionMode": zxAnLdpTargetDistributionMode,
       "zxAnLdpTargetSessionRowStatus": zxAnLdpTargetSessionRowStatus,
       "zxAnLdpSessionTable": zxAnLdpSessionTable,
       "zxAnLdpSessionEntry": zxAnLdpSessionEntry,
       "zxAnLdpPeerIpAddrType": zxAnLdpPeerIpAddrType,
       "zxAnLdpPeerIpAddr": zxAnLdpPeerIpAddr,
       "zxAnLdpMd5Pwd": zxAnLdpMd5Pwd,
       "zxAnLdpMd5PwdConfStatus": zxAnLdpMd5PwdConfStatus,
       "zxAnLdpMd5PwdEncrypt": zxAnLdpMd5PwdEncrypt,
       "zxAnLdpSessionReset": zxAnLdpSessionReset,
       "zxAnLdpSessionRowStatus": zxAnLdpSessionRowStatus,
       "zxAnLdpL3IfEntityTable": zxAnLdpL3IfEntityTable,
       "zxAnLdpL3IfEntityEntry": zxAnLdpL3IfEntityEntry,
       "zxAnLdpL3IfTransAddrMode": zxAnLdpL3IfTransAddrMode,
       "zxAnLdpL3IfTransAddrType": zxAnLdpL3IfTransAddrType,
       "zxAnLdpL3IfTransAddr": zxAnLdpL3IfTransAddr,
       "zxAnLdpL3IfDistributionMode": zxAnLdpL3IfDistributionMode,
       "zxAnLdpL3IfEntityRowStatus": zxAnLdpL3IfEntityRowStatus}
)
