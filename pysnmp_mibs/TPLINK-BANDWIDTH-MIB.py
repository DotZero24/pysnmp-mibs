# SNMP MIB module (TPLINK-BANDWIDTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-BANDWIDTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:49 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkBandWidthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23)
)
if mibBuilder.loadTexts:
    tplinkBandWidthMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkBandWidthMIBObjects_ObjectIdentity = ObjectIdentity
tplinkBandWidthMIBObjects = _TplinkBandWidthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1)
)
_TpRateLimit_ObjectIdentity = ObjectIdentity
tpRateLimit = _TpRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1)
)
_TpRateLimitTable_Object = MibTable
tpRateLimitTable = _TpRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpRateLimitTable.setStatus("current")
_TpRateLimitEntry_Object = MibTableRow
tpRateLimitEntry = _TpRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1)
)
tpRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpRateLimitEntry.setStatus("current")
_TpRateLimitPort_Type = DisplayString
_TpRateLimitPort_Object = MibTableColumn
tpRateLimitPort = _TpRateLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 1),
    _TpRateLimitPort_Type()
)
tpRateLimitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRateLimitPort.setStatus("current")


class _TpRateLimitIngressRate_Type(Integer32):
    """Custom type tpRateLimitIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TpRateLimitIngressRate_Type.__name__ = "Integer32"
_TpRateLimitIngressRate_Object = MibTableColumn
tpRateLimitIngressRate = _TpRateLimitIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 2),
    _TpRateLimitIngressRate_Type()
)
tpRateLimitIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRateLimitIngressRate.setStatus("current")


class _TpRateLimitEgressRate_Type(Integer32):
    """Custom type tpRateLimitEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TpRateLimitEgressRate_Type.__name__ = "Integer32"
_TpRateLimitEgressRate_Object = MibTableColumn
tpRateLimitEgressRate = _TpRateLimitEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 3),
    _TpRateLimitEgressRate_Type()
)
tpRateLimitEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRateLimitEgressRate.setStatus("current")


class _TpRateLimitPortLag_Type(OctetString):
    """Custom type tpRateLimitPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpRateLimitPortLag_Type.__name__ = "OctetString"
_TpRateLimitPortLag_Object = MibTableColumn
tpRateLimitPortLag = _TpRateLimitPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 4),
    _TpRateLimitPortLag_Type()
)
tpRateLimitPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRateLimitPortLag.setStatus("current")
_TpStormControl_ObjectIdentity = ObjectIdentity
tpStormControl = _TpStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2)
)
_TpStormControlTable_Object = MibTable
tpStormControlTable = _TpStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpStormControlTable.setStatus("current")
_TpStormControlEntry_Object = MibTableRow
tpStormControlEntry = _TpStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1)
)
tpStormControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStormControlEntry.setStatus("current")
_TpStormControlPort_Type = DisplayString
_TpStormControlPort_Object = MibTableColumn
tpStormControlPort = _TpStormControlPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 1),
    _TpStormControlPort_Type()
)
tpStormControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlPort.setStatus("current")


class _TpStormControlMode_Type(Integer32):
    """Custom type tpStormControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("ratio", 1),
          ("pps", 2))
    )


_TpStormControlMode_Type.__name__ = "Integer32"
_TpStormControlMode_Object = MibTableColumn
tpStormControlMode = _TpStormControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 2),
    _TpStormControlMode_Type()
)
tpStormControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlMode.setStatus("current")
_TpStormControlBroadCastRate_Type = Integer32
_TpStormControlBroadCastRate_Object = MibTableColumn
tpStormControlBroadCastRate = _TpStormControlBroadCastRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 3),
    _TpStormControlBroadCastRate_Type()
)
tpStormControlBroadCastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlBroadCastRate.setStatus("current")


class _TpStormControlMultiCastRate_Type(Integer32):
    """Custom type tpStormControlMultiCastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1488000),
    )


_TpStormControlMultiCastRate_Type.__name__ = "Integer32"
_TpStormControlMultiCastRate_Object = MibTableColumn
tpStormControlMultiCastRate = _TpStormControlMultiCastRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 4),
    _TpStormControlMultiCastRate_Type()
)
tpStormControlMultiCastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlMultiCastRate.setStatus("current")


class _TpStormControlULRate_Type(Integer32):
    """Custom type tpStormControlULRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1488000),
    )


_TpStormControlULRate_Type.__name__ = "Integer32"
_TpStormControlULRate_Object = MibTableColumn
tpStormControlULRate = _TpStormControlULRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 5),
    _TpStormControlULRate_Type()
)
tpStormControlULRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlULRate.setStatus("current")


class _TpStormControlAction_Type(Integer32):
    """Custom type tpStormControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("shutdown", 1))
    )


_TpStormControlAction_Type.__name__ = "Integer32"
_TpStormControlAction_Object = MibTableColumn
tpStormControlAction = _TpStormControlAction_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 6),
    _TpStormControlAction_Type()
)
tpStormControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlAction.setStatus("current")
_TpStormControlRecoverTime_Type = Integer32
_TpStormControlRecoverTime_Object = MibTableColumn
tpStormControlRecoverTime = _TpStormControlRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 7),
    _TpStormControlRecoverTime_Type()
)
tpStormControlRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlRecoverTime.setStatus("current")


class _TpStormControlPortLag_Type(OctetString):
    """Custom type tpStormControlPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpStormControlPortLag_Type.__name__ = "OctetString"
_TpStormControlPortLag_Object = MibTableColumn
tpStormControlPortLag = _TpStormControlPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 8),
    _TpStormControlPortLag_Type()
)
tpStormControlPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlPortLag.setStatus("current")
_TpStormControlRecover_ObjectIdentity = ObjectIdentity
tpStormControlRecover = _TpStormControlRecover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 3)
)
_TpStormControlRecoverPort_Type = OctetString
_TpStormControlRecoverPort_Object = MibScalar
tpStormControlRecoverPort = _TpStormControlRecoverPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 3, 1),
    _TpStormControlRecoverPort_Type()
)
tpStormControlRecoverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlRecoverPort.setStatus("current")
_TplinkBandWidthNotifications_ObjectIdentity = ObjectIdentity
tplinkBandWidthNotifications = _TplinkBandWidthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2)
)

# Managed Objects groups


# Notification objects

tpBroadcastRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 1)
)
tpBroadcastRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpStormControlPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpStormControlBroadCastRate"))
)
if mibBuilder.loadTexts:
    tpBroadcastRateExceed.setStatus(
        "current"
    )

tpMulticastRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 2)
)
tpMulticastRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpStormControlPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpStormControlMultiCastRate"))
)
if mibBuilder.loadTexts:
    tpMulticastRateExceed.setStatus(
        "current"
    )

tpIngressRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 3)
)
tpIngressRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpRateLimitPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpRateLimitIngressRate"))
)
if mibBuilder.loadTexts:
    tpIngressRateExceed.setStatus(
        "current"
    )

tpEgressRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 4)
)
tpEgressRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpRateLimitPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpRateLimitEgressRate"))
)
if mibBuilder.loadTexts:
    tpEgressRateExceed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-BANDWIDTH-MIB",
    **{"tplinkBandWidthMIB": tplinkBandWidthMIB,
       "tplinkBandWidthMIBObjects": tplinkBandWidthMIBObjects,
       "tpRateLimit": tpRateLimit,
       "tpRateLimitTable": tpRateLimitTable,
       "tpRateLimitEntry": tpRateLimitEntry,
       "tpRateLimitPort": tpRateLimitPort,
       "tpRateLimitIngressRate": tpRateLimitIngressRate,
       "tpRateLimitEgressRate": tpRateLimitEgressRate,
       "tpRateLimitPortLag": tpRateLimitPortLag,
       "tpStormControl": tpStormControl,
       "tpStormControlTable": tpStormControlTable,
       "tpStormControlEntry": tpStormControlEntry,
       "tpStormControlPort": tpStormControlPort,
       "tpStormControlMode": tpStormControlMode,
       "tpStormControlBroadCastRate": tpStormControlBroadCastRate,
       "tpStormControlMultiCastRate": tpStormControlMultiCastRate,
       "tpStormControlULRate": tpStormControlULRate,
       "tpStormControlAction": tpStormControlAction,
       "tpStormControlRecoverTime": tpStormControlRecoverTime,
       "tpStormControlPortLag": tpStormControlPortLag,
       "tpStormControlRecover": tpStormControlRecover,
       "tpStormControlRecoverPort": tpStormControlRecoverPort,
       "tplinkBandWidthNotifications": tplinkBandWidthNotifications,
       "tpBroadcastRateExceed": tpBroadcastRateExceed,
       "tpMulticastRateExceed": tpMulticastRateExceed,
       "tpIngressRateExceed": tpIngressRateExceed,
       "tpEgressRateExceed": tpEgressRateExceed}
)
