# SNMP MIB module (ZTE-DSL-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:02 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zte,
 zxDsl) = mibBuilder.importSymbols(
    "ZTE-DSL-MIB",
    "zte",
    "zxDsl")


# MODULE-IDENTITY

zxDslEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxDslEventObjects_ObjectIdentity = ObjectIdentity
zxDslEventObjects = _ZxDslEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1)
)


class _ZxDslTrapSendEnable_Type(Integer32):
    """Custom type zxDslTrapSendEnable based on Integer32"""
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


_ZxDslTrapSendEnable_Type.__name__ = "Integer32"
_ZxDslTrapSendEnable_Object = MibScalar
zxDslTrapSendEnable = _ZxDslTrapSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 1),
    _ZxDslTrapSendEnable_Type()
)
zxDslTrapSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslTrapSendEnable.setStatus("current")


class _ZxDslEventCurrentEventId_Type(Integer32):
    """Custom type zxDslEventCurrentEventId based on Integer32"""
    defaultValue = 0


_ZxDslEventCurrentEventId_Type.__name__ = "Integer32"
_ZxDslEventCurrentEventId_Object = MibScalar
zxDslEventCurrentEventId = _ZxDslEventCurrentEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 2),
    _ZxDslEventCurrentEventId_Type()
)
zxDslEventCurrentEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEventCurrentEventId.setStatus("current")
_ZxDslEventConfirmEventId_Type = Integer32
_ZxDslEventConfirmEventId_Object = MibScalar
zxDslEventConfirmEventId = _ZxDslEventConfirmEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 3),
    _ZxDslEventConfirmEventId_Type()
)
zxDslEventConfirmEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEventConfirmEventId.setStatus("current")
_ZxDslEventSynchUnconfirmedEvents_Type = Integer32
_ZxDslEventSynchUnconfirmedEvents_Object = MibScalar
zxDslEventSynchUnconfirmedEvents = _ZxDslEventSynchUnconfirmedEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 4),
    _ZxDslEventSynchUnconfirmedEvents_Type()
)
zxDslEventSynchUnconfirmedEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEventSynchUnconfirmedEvents.setStatus("current")
_ZxDslEventCurrUnconfirmedEventCounter_Type = Integer32
_ZxDslEventCurrUnconfirmedEventCounter_Object = MibScalar
zxDslEventCurrUnconfirmedEventCounter = _ZxDslEventCurrUnconfirmedEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 5),
    _ZxDslEventCurrUnconfirmedEventCounter_Type()
)
zxDslEventCurrUnconfirmedEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslEventCurrUnconfirmedEventCounter.setStatus("current")
_ZxDslEventNmsHelloTrapMgmt_ObjectIdentity = ObjectIdentity
zxDslEventNmsHelloTrapMgmt = _ZxDslEventNmsHelloTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 6)
)


class _ZxDslEventNmsHelloTrapEnable_Type(Integer32):
    """Custom type zxDslEventNmsHelloTrapEnable based on Integer32"""
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


_ZxDslEventNmsHelloTrapEnable_Type.__name__ = "Integer32"
_ZxDslEventNmsHelloTrapEnable_Object = MibScalar
zxDslEventNmsHelloTrapEnable = _ZxDslEventNmsHelloTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 6, 1),
    _ZxDslEventNmsHelloTrapEnable_Type()
)
zxDslEventNmsHelloTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEventNmsHelloTrapEnable.setStatus("current")


class _ZxDslEventNmsHelloTrapInterval_Type(Integer32):
    """Custom type zxDslEventNmsHelloTrapInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ZxDslEventNmsHelloTrapInterval_Type.__name__ = "Integer32"
_ZxDslEventNmsHelloTrapInterval_Object = MibScalar
zxDslEventNmsHelloTrapInterval = _ZxDslEventNmsHelloTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 1, 6, 2),
    _ZxDslEventNmsHelloTrapInterval_Type()
)
zxDslEventNmsHelloTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslEventNmsHelloTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxDslEventNmsHelloTrapInterval.setUnits("second")
_ZxDslEventTrapObjects_ObjectIdentity = ObjectIdentity
zxDslEventTrapObjects = _ZxDslEventTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 2)
)

# Managed Objects groups


# Notification objects

zxDslDisabledTrapSend = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 2, 1)
)
if mibBuilder.loadTexts:
    zxDslDisabledTrapSend.setStatus(
        "current"
    )

zxDslEnabledTrapSend = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 37, 2, 2)
)
if mibBuilder.loadTexts:
    zxDslEnabledTrapSend.setStatus(
        "current"
    )

zxAnEventNmsHelloTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 6, 2)
)
if mibBuilder.loadTexts:
    zxAnEventNmsHelloTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-EVENT-MIB",
    **{"zxDslEventMib": zxDslEventMib,
       "zxDslEventObjects": zxDslEventObjects,
       "zxDslTrapSendEnable": zxDslTrapSendEnable,
       "zxDslEventCurrentEventId": zxDslEventCurrentEventId,
       "zxDslEventConfirmEventId": zxDslEventConfirmEventId,
       "zxDslEventSynchUnconfirmedEvents": zxDslEventSynchUnconfirmedEvents,
       "zxDslEventCurrUnconfirmedEventCounter": zxDslEventCurrUnconfirmedEventCounter,
       "zxDslEventNmsHelloTrapMgmt": zxDslEventNmsHelloTrapMgmt,
       "zxDslEventNmsHelloTrapEnable": zxDslEventNmsHelloTrapEnable,
       "zxDslEventNmsHelloTrapInterval": zxDslEventNmsHelloTrapInterval,
       "zxDslEventTrapObjects": zxDslEventTrapObjects,
       "zxDslDisabledTrapSend": zxDslDisabledTrapSend,
       "zxDslEnabledTrapSend": zxDslEnabledTrapSend,
       "zxAnEventNmsHelloTrap": zxAnEventNmsHelloTrap}
)
