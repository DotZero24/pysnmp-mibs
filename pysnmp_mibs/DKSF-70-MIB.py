# SNMP MIB module (DKSF-70-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netping/DKSF-70-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:30 2025
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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


# MODULE-IDENTITY

uniPingServerSolutionV3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 70)
)
if mibBuilder.loadTexts:
    uniPingServerSolutionV3.setRevisions(
        ("2022-07-01 00:00",
         "2020-08-19 00:00",
         "2020-06-12 00:00",
         "2019-10-13 00:00",
         "2018-07-01 00:00",
         "2016-08-24 00:00",
         "2015-07-14 00:00",
         "2015-05-29 00:00",
         "2014-12-03 00:00",
         "2014-11-26 00:00",
         "2014-02-02 00:00",
         "2014-01-29 00:00",
         "2014-01-21 00:00",
         "2013-04-11 00:00",
         "2012-05-31 00:00",
         "2012-04-17 00:00",
         "2012-03-23 00:00",
         "2011-09-23 00:00",
         "2011-03-24 00:00",
         "2010-10-14 00:00",
         "2010-09-20 00:00",
         "2010-05-31 00:00",
         "2010-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedPoint1000(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_Lightcom_ObjectIdentity = ObjectIdentity
lightcom = _Lightcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728)
)
_NpTrapInfo_ObjectIdentity = ObjectIdentity
npTrapInfo = _NpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 90)
)
_NpTrapEmailTo_Type = DisplayString
_NpTrapEmailTo_Object = MibScalar
npTrapEmailTo = _NpTrapEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 90, 1),
    _NpTrapEmailTo_Type()
)
npTrapEmailTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTrapEmailTo.setStatus("current")
_NpReboot_ObjectIdentity = ObjectIdentity
npReboot = _NpReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 911)
)
_NpSoftReboot_Type = Integer32
_NpSoftReboot_Object = MibScalar
npSoftReboot = _NpSoftReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 1),
    _NpSoftReboot_Type()
)
npSoftReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSoftReboot.setStatus("current")
_NpResetStack_Type = Integer32
_NpResetStack_Object = MibScalar
npResetStack = _NpResetStack_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 2),
    _NpResetStack_Type()
)
npResetStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npResetStack.setStatus("current")
_NpForcedReboot_Type = Integer32
_NpForcedReboot_Object = MibScalar
npForcedReboot = _NpForcedReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 3),
    _NpForcedReboot_Type()
)
npForcedReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npForcedReboot.setStatus("current")
_NpGsm_ObjectIdentity = ObjectIdentity
npGsm = _NpGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800)
)
_NpGsmInfo_ObjectIdentity = ObjectIdentity
npGsmInfo = _NpGsmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1)
)


class _NpGsmFailed_Type(Integer32):
    """Custom type npGsmFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("fatalError", 2))
    )


_NpGsmFailed_Type.__name__ = "Integer32"
_NpGsmFailed_Object = MibScalar
npGsmFailed = _NpGsmFailed_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1),
    _NpGsmFailed_Type()
)
npGsmFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmFailed.setStatus("current")


class _NpGsmRegistration_Type(Integer32):
    """Custom type npGsmRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("impossible", 0),
          ("homeNetwork", 1),
          ("searching", 2),
          ("denied", 3),
          ("unknown", 4),
          ("roaming", 5),
          ("infoUpdate", 255))
    )


_NpGsmRegistration_Type.__name__ = "Integer32"
_NpGsmRegistration_Object = MibScalar
npGsmRegistration = _NpGsmRegistration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2),
    _NpGsmRegistration_Type()
)
npGsmRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmRegistration.setStatus("current")


class _NpGsmStrength_Type(Integer32):
    """Custom type npGsmStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NpGsmStrength_Type.__name__ = "Integer32"
_NpGsmStrength_Object = MibScalar
npGsmStrength = _NpGsmStrength_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3),
    _NpGsmStrength_Type()
)
npGsmStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmStrength.setStatus("current")
_NpGsmSendSmsUtf8_Type = DisplayString
_NpGsmSendSmsUtf8_Object = MibScalar
npGsmSendSmsUtf8 = _NpGsmSendSmsUtf8_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 9),
    _NpGsmSendSmsUtf8_Type()
)
npGsmSendSmsUtf8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npGsmSendSmsUtf8.setStatus("current")
_NpGsmSendSmsWin1251_Type = DisplayString
_NpGsmSendSmsWin1251_Object = MibScalar
npGsmSendSmsWin1251 = _NpGsmSendSmsWin1251_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 10),
    _NpGsmSendSmsWin1251_Type()
)
npGsmSendSmsWin1251.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npGsmSendSmsWin1251.setStatus("current")
_NpGsmUnparsedRxSmsFrom_Type = DisplayString
_NpGsmUnparsedRxSmsFrom_Object = MibScalar
npGsmUnparsedRxSmsFrom = _NpGsmUnparsedRxSmsFrom_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 11),
    _NpGsmUnparsedRxSmsFrom_Type()
)
npGsmUnparsedRxSmsFrom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npGsmUnparsedRxSmsFrom.setStatus("current")
_NpGsmUnparsedRxSms_Type = DisplayString
_NpGsmUnparsedRxSms_Object = MibScalar
npGsmUnparsedRxSms = _NpGsmUnparsedRxSms_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 12),
    _NpGsmUnparsedRxSms_Type()
)
npGsmUnparsedRxSms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npGsmUnparsedRxSms.setStatus("current")
_NpGsmUnparsedRxSmsUtf8_Type = DisplayString
_NpGsmUnparsedRxSmsUtf8_Object = MibScalar
npGsmUnparsedRxSmsUtf8 = _NpGsmUnparsedRxSmsUtf8_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 13),
    _NpGsmUnparsedRxSmsUtf8_Type()
)
npGsmUnparsedRxSmsUtf8.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npGsmUnparsedRxSmsUtf8.setStatus("current")
_NpGsmTraps_ObjectIdentity = ObjectIdentity
npGsmTraps = _NpGsmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2)
)
_NpGsmTrapPrefix_ObjectIdentity = ObjectIdentity
npGsmTrapPrefix = _NpGsmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0)
)
_NpRelay_ObjectIdentity = ObjectIdentity
npRelay = _NpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5500)
)
_NpRelayTrapData_ObjectIdentity = ObjectIdentity
npRelayTrapData = _NpRelayTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3)
)


class _NpRelayTrapN_Type(Integer32):
    """Custom type npRelayTrapN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NpRelayTrapN_Type.__name__ = "Integer32"
_NpRelayTrapN_Object = MibScalar
npRelayTrapN = _NpRelayTrapN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3, 1),
    _NpRelayTrapN_Type()
)
npRelayTrapN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayTrapN.setStatus("current")


class _NpRelayTrapMode_Type(Integer32):
    """Custom type npRelayTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpRelayTrapMode_Type.__name__ = "Integer32"
_NpRelayTrapMode_Object = MibScalar
npRelayTrapMode = _NpRelayTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3, 2),
    _NpRelayTrapMode_Type()
)
npRelayTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayTrapMode.setStatus("current")
_NpRelayTrapMemo_Type = DisplayString
_NpRelayTrapMemo_Object = MibScalar
npRelayTrapMemo = _NpRelayTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3, 6),
    _NpRelayTrapMemo_Type()
)
npRelayTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayTrapMemo.setStatus("current")


class _NpRelayTrapState_Type(Integer32):
    """Custom type npRelayTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpRelayTrapState_Type.__name__ = "Integer32"
_NpRelayTrapState_Object = MibScalar
npRelayTrapState = _NpRelayTrapState_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3, 15),
    _NpRelayTrapState_Type()
)
npRelayTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayTrapState.setStatus("current")


class _NpRelayTrapCmdSrc_Type(Integer32):
    """Custom type npRelayTrapCmdSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("webInterface", 1),
          ("snmp", 2),
          ("sms", 3),
          ("httpApi", 4),
          ("watchdog", 5),
          ("schedule", 6),
          ("logic", 7))
    )


_NpRelayTrapCmdSrc_Type.__name__ = "Integer32"
_NpRelayTrapCmdSrc_Object = MibScalar
npRelayTrapCmdSrc = _NpRelayTrapCmdSrc_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3, 18),
    _NpRelayTrapCmdSrc_Type()
)
npRelayTrapCmdSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayTrapCmdSrc.setStatus("current")
_NpRelayTrapDateTime_Type = DisplayString
_NpRelayTrapDateTime_Object = MibScalar
npRelayTrapDateTime = _NpRelayTrapDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 3, 19),
    _NpRelayTrapDateTime_Type()
)
npRelayTrapDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayTrapDateTime.setStatus("current")
_NpRelayTable_Object = MibTable
npRelayTable = _NpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5)
)
if mibBuilder.loadTexts:
    npRelayTable.setStatus("current")
_NpRelayEntry_Object = MibTableRow
npRelayEntry = _NpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1)
)
npRelayEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npRelayN"),
)
if mibBuilder.loadTexts:
    npRelayEntry.setStatus("current")


class _NpRelayN_Type(Integer32):
    """Custom type npRelayN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NpRelayN_Type.__name__ = "Integer32"
_NpRelayN_Object = MibTableColumn
npRelayN = _NpRelayN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1),
    _NpRelayN_Type()
)
npRelayN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayN.setStatus("current")


class _NpRelayMode_Type(Integer32):
    """Custom type npRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("off", 0),
          ("on", 1))
    )


_NpRelayMode_Type.__name__ = "Integer32"
_NpRelayMode_Object = MibTableColumn
npRelayMode = _NpRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2),
    _NpRelayMode_Type()
)
npRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayMode.setStatus("current")
_NpRelayStartReset_Type = Integer32
_NpRelayStartReset_Object = MibTableColumn
npRelayStartReset = _NpRelayStartReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3),
    _NpRelayStartReset_Type()
)
npRelayStartReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayStartReset.setStatus("current")
_NpRelayMemo_Type = DisplayString
_NpRelayMemo_Object = MibTableColumn
npRelayMemo = _NpRelayMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6),
    _NpRelayMemo_Type()
)
npRelayMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayMemo.setStatus("current")


class _NpRelayFlip_Type(Integer32):
    """Custom type npRelayFlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("flip", -1)
    )


_NpRelayFlip_Type.__name__ = "Integer32"
_NpRelayFlip_Object = MibTableColumn
npRelayFlip = _NpRelayFlip_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 14),
    _NpRelayFlip_Type()
)
npRelayFlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayFlip.setStatus("current")


class _NpRelayState_Type(Integer32):
    """Custom type npRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpRelayState_Type.__name__ = "Integer32"
_NpRelayState_Object = MibTableColumn
npRelayState = _NpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15),
    _NpRelayState_Type()
)
npRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayState.setStatus("current")
_NpRelayTrap_ObjectIdentity = ObjectIdentity
npRelayTrap = _NpRelayTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6)
)
_NpRelayTrapAllEvents_ObjectIdentity = ObjectIdentity
npRelayTrapAllEvents = _NpRelayTrapAllEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6, 127)
)
_NpExtRelay_ObjectIdentity = ObjectIdentity
npExtRelay = _NpExtRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5600)
)
_NpExtRelayTrapData_ObjectIdentity = ObjectIdentity
npExtRelayTrapData = _NpExtRelayTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3)
)


class _NpExtRelayTrapN_Type(Integer32):
    """Custom type npExtRelayTrapN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpExtRelayTrapN_Type.__name__ = "Integer32"
_NpExtRelayTrapN_Object = MibScalar
npExtRelayTrapN = _NpExtRelayTrapN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3, 1),
    _NpExtRelayTrapN_Type()
)
npExtRelayTrapN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayTrapN.setStatus("current")


class _NpExtRelayTrapMode_Type(Integer32):
    """Custom type npExtRelayTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpExtRelayTrapMode_Type.__name__ = "Integer32"
_NpExtRelayTrapMode_Object = MibScalar
npExtRelayTrapMode = _NpExtRelayTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3, 2),
    _NpExtRelayTrapMode_Type()
)
npExtRelayTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npExtRelayTrapMode.setStatus("current")
_NpExtRelayTrapMemo_Type = DisplayString
_NpExtRelayTrapMemo_Object = MibScalar
npExtRelayTrapMemo = _NpExtRelayTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3, 6),
    _NpExtRelayTrapMemo_Type()
)
npExtRelayTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayTrapMemo.setStatus("current")


class _NpExtRelayTrapState_Type(Integer32):
    """Custom type npExtRelayTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpExtRelayTrapState_Type.__name__ = "Integer32"
_NpExtRelayTrapState_Object = MibScalar
npExtRelayTrapState = _NpExtRelayTrapState_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3, 15),
    _NpExtRelayTrapState_Type()
)
npExtRelayTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayTrapState.setStatus("current")


class _NpExtRelayTrapCmdSrc_Type(Integer32):
    """Custom type npExtRelayTrapCmdSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("webInterface", 1),
          ("snmp", 2),
          ("sms", 3),
          ("httpApi", 4),
          ("watchdog", 5),
          ("schedule", 6),
          ("logic", 7),
          ("button", 8))
    )


_NpExtRelayTrapCmdSrc_Type.__name__ = "Integer32"
_NpExtRelayTrapCmdSrc_Object = MibScalar
npExtRelayTrapCmdSrc = _NpExtRelayTrapCmdSrc_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3, 18),
    _NpExtRelayTrapCmdSrc_Type()
)
npExtRelayTrapCmdSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayTrapCmdSrc.setStatus("current")
_NpExtRelayTrapDateTime_Type = DisplayString
_NpExtRelayTrapDateTime_Object = MibScalar
npExtRelayTrapDateTime = _NpExtRelayTrapDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 3, 19),
    _NpExtRelayTrapDateTime_Type()
)
npExtRelayTrapDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayTrapDateTime.setStatus("current")
_NpExtRelayTable_Object = MibTable
npExtRelayTable = _NpExtRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5)
)
if mibBuilder.loadTexts:
    npExtRelayTable.setStatus("current")
_NpExtRelayEntry_Object = MibTableRow
npExtRelayEntry = _NpExtRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1)
)
npExtRelayEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npExtRelayN"),
)
if mibBuilder.loadTexts:
    npExtRelayEntry.setStatus("current")


class _NpExtRelayN_Type(Integer32):
    """Custom type npExtRelayN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpExtRelayN_Type.__name__ = "Integer32"
_NpExtRelayN_Object = MibTableColumn
npExtRelayN = _NpExtRelayN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1, 1),
    _NpExtRelayN_Type()
)
npExtRelayN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayN.setStatus("current")


class _NpExtRelayMode_Type(Integer32):
    """Custom type npExtRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("off", 0),
          ("on", 1))
    )


_NpExtRelayMode_Type.__name__ = "Integer32"
_NpExtRelayMode_Object = MibTableColumn
npExtRelayMode = _NpExtRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1, 2),
    _NpExtRelayMode_Type()
)
npExtRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npExtRelayMode.setStatus("current")
_NpExtRelayStartReset_Type = Integer32
_NpExtRelayStartReset_Object = MibTableColumn
npExtRelayStartReset = _NpExtRelayStartReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1, 3),
    _NpExtRelayStartReset_Type()
)
npExtRelayStartReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npExtRelayStartReset.setStatus("current")
_NpExtRelayMemo_Type = DisplayString
_NpExtRelayMemo_Object = MibTableColumn
npExtRelayMemo = _NpExtRelayMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1, 6),
    _NpExtRelayMemo_Type()
)
npExtRelayMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayMemo.setStatus("current")


class _NpExtRelayFlip_Type(Integer32):
    """Custom type npExtRelayFlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("flip", -1)
    )


_NpExtRelayFlip_Type.__name__ = "Integer32"
_NpExtRelayFlip_Object = MibTableColumn
npExtRelayFlip = _NpExtRelayFlip_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1, 14),
    _NpExtRelayFlip_Type()
)
npExtRelayFlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npExtRelayFlip.setStatus("current")


class _NpExtRelayState_Type(Integer32):
    """Custom type npExtRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpExtRelayState_Type.__name__ = "Integer32"
_NpExtRelayState_Object = MibTableColumn
npExtRelayState = _NpExtRelayState_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 5, 1, 15),
    _NpExtRelayState_Type()
)
npExtRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npExtRelayState.setStatus("current")
_NpExtRelayTrap_ObjectIdentity = ObjectIdentity
npExtRelayTrap = _NpExtRelayTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6)
)
_NpExtRelayTrapAllEvents_ObjectIdentity = ObjectIdentity
npExtRelayTrapAllEvents = _NpExtRelayTrapAllEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6, 127)
)
_NpIr_ObjectIdentity = ObjectIdentity
npIr = _NpIr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 7900)
)
_NpIrCtrl_ObjectIdentity = ObjectIdentity
npIrCtrl = _NpIrCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1)
)


class _NpIrPlayCmd_Type(Integer32):
    """Custom type npIrPlayCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NpIrPlayCmd_Type.__name__ = "Integer32"
_NpIrPlayCmd_Object = MibScalar
npIrPlayCmd = _NpIrPlayCmd_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1),
    _NpIrPlayCmd_Type()
)
npIrPlayCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIrPlayCmd.setStatus("current")


class _NpIrReset_Type(Integer32):
    """Custom type npIrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIrReset_Type.__name__ = "Integer32"
_NpIrReset_Object = MibScalar
npIrReset = _NpIrReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2),
    _NpIrReset_Type()
)
npIrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIrReset.setStatus("current")


class _NpIrStatus_Type(Integer32):
    """Custom type npIrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("commandCompleted", 0),
          ("protocolError", 1),
          ("commandAccepted", 2),
          ("errorUnknown", 16),
          ("errorBadNumber", 17),
          ("errorEmptyRecord", 18),
          ("errorFlashChip", 19),
          ("errorTimeout", 20),
          ("errorExtBusBusy", 21))
    )


_NpIrStatus_Type.__name__ = "Integer32"
_NpIrStatus_Object = MibScalar
npIrStatus = _NpIrStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3),
    _NpIrStatus_Type()
)
npIrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIrStatus.setStatus("current")
_NpInputAnalog_ObjectIdentity = ObjectIdentity
npInputAnalog = _NpInputAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8200)
)
_NpInputAnalogTable_Object = MibTable
npInputAnalogTable = _NpInputAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1)
)
if mibBuilder.loadTexts:
    npInputAnalogTable.setStatus("current")
_NpInputAnalogEntry_Object = MibTableRow
npInputAnalogEntry = _NpInputAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1)
)
npInputAnalogEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npInputAnalogSensorN"),
)
if mibBuilder.loadTexts:
    npInputAnalogEntry.setStatus("current")


class _NpInputAnalogSensorN_Type(Integer32):
    """Custom type npInputAnalogSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpInputAnalogSensorN_Type.__name__ = "Integer32"
_NpInputAnalogSensorN_Object = MibTableColumn
npInputAnalogSensorN = _NpInputAnalogSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 1),
    _NpInputAnalogSensorN_Type()
)
npInputAnalogSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogSensorN.setStatus("current")


class _NpInputAnalogStatus_Type(Integer32):
    """Custom type npInputAnalogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failure1w", 0),
          ("belowSafe", 1),
          ("safe", 2),
          ("aboveSafe", 3),
          ("failureAnalog", 5))
    )


_NpInputAnalogStatus_Type.__name__ = "Integer32"
_NpInputAnalogStatus_Object = MibTableColumn
npInputAnalogStatus = _NpInputAnalogStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 2),
    _NpInputAnalogStatus_Type()
)
npInputAnalogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogStatus.setStatus("current")
_NpInputAnalogCurrent_Type = Integer32
_NpInputAnalogCurrent_Object = MibTableColumn
npInputAnalogCurrent = _NpInputAnalogCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 3),
    _NpInputAnalogCurrent_Type()
)
npInputAnalogCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogCurrent.setStatus("current")
_NpInputAnalogVoltage_Type = Integer32
_NpInputAnalogVoltage_Object = MibTableColumn
npInputAnalogVoltage = _NpInputAnalogVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 4),
    _NpInputAnalogVoltage_Type()
)
npInputAnalogVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogVoltage.setStatus("current")
_NpInputAnalogResistance_Type = Unsigned32
_NpInputAnalogResistance_Object = MibTableColumn
npInputAnalogResistance = _NpInputAnalogResistance_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 5),
    _NpInputAnalogResistance_Type()
)
npInputAnalogResistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogResistance.setStatus("current")
_NpInputAnalogMemo_Type = DisplayString
_NpInputAnalogMemo_Object = MibTableColumn
npInputAnalogMemo = _NpInputAnalogMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 6),
    _NpInputAnalogMemo_Type()
)
npInputAnalogMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogMemo.setStatus("current")


class _NpInputAnalogPower_Type(Integer32):
    """Custom type npInputAnalogPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpInputAnalogPower_Type.__name__ = "Integer32"
_NpInputAnalogPower_Object = MibTableColumn
npInputAnalogPower = _NpInputAnalogPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 7),
    _NpInputAnalogPower_Type()
)
npInputAnalogPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInputAnalogPower.setStatus("current")
_NpInputAnalogReset_Type = Integer32
_NpInputAnalogReset_Object = MibTableColumn
npInputAnalogReset = _NpInputAnalogReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 8),
    _NpInputAnalogReset_Type()
)
npInputAnalogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInputAnalogReset.setStatus("current")
_NpInputAnalogWorkRangeHigh_Type = Integer32
_NpInputAnalogWorkRangeHigh_Object = MibTableColumn
npInputAnalogWorkRangeHigh = _NpInputAnalogWorkRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 11),
    _NpInputAnalogWorkRangeHigh_Type()
)
npInputAnalogWorkRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogWorkRangeHigh.setStatus("current")
_NpInputAnalogSafeRangeHigh_Type = Integer32
_NpInputAnalogSafeRangeHigh_Object = MibTableColumn
npInputAnalogSafeRangeHigh = _NpInputAnalogSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 12),
    _NpInputAnalogSafeRangeHigh_Type()
)
npInputAnalogSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogSafeRangeHigh.setStatus("current")
_NpInputAnalogSafeRangeLow_Type = Integer32
_NpInputAnalogSafeRangeLow_Object = MibTableColumn
npInputAnalogSafeRangeLow = _NpInputAnalogSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 13),
    _NpInputAnalogSafeRangeLow_Type()
)
npInputAnalogSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogSafeRangeLow.setStatus("current")
_NpInputAnalogWorkRangeLow_Type = Integer32
_NpInputAnalogWorkRangeLow_Object = MibTableColumn
npInputAnalogWorkRangeLow = _NpInputAnalogWorkRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 1, 1, 14),
    _NpInputAnalogWorkRangeLow_Type()
)
npInputAnalogWorkRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInputAnalogWorkRangeLow.setStatus("current")
_NpInputAnalogTraps_ObjectIdentity = ObjectIdentity
npInputAnalogTraps = _NpInputAnalogTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2)
)
_NpInputAnalogTrapPrefix_ObjectIdentity = ObjectIdentity
npInputAnalogTrapPrefix = _NpInputAnalogTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 0)
)


class _NpInputAnalogTrapSensorN_Type(Integer32):
    """Custom type npInputAnalogTrapSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpInputAnalogTrapSensorN_Type.__name__ = "Integer32"
_NpInputAnalogTrapSensorN_Object = MibScalar
npInputAnalogTrapSensorN = _NpInputAnalogTrapSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 1),
    _NpInputAnalogTrapSensorN_Type()
)
npInputAnalogTrapSensorN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapSensorN.setStatus("current")


class _NpInputAnalogTrapStatus_Type(Integer32):
    """Custom type npInputAnalogTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failure1w", 0),
          ("belowSafe", 1),
          ("safe", 2),
          ("aboveSafe", 3),
          ("failureAnalog", 5))
    )


_NpInputAnalogTrapStatus_Type.__name__ = "Integer32"
_NpInputAnalogTrapStatus_Object = MibScalar
npInputAnalogTrapStatus = _NpInputAnalogTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 2),
    _NpInputAnalogTrapStatus_Type()
)
npInputAnalogTrapStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapStatus.setStatus("current")
_NpInputAnalogTrapCurrent_Type = Integer32
_NpInputAnalogTrapCurrent_Object = MibScalar
npInputAnalogTrapCurrent = _NpInputAnalogTrapCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 3),
    _NpInputAnalogTrapCurrent_Type()
)
npInputAnalogTrapCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapCurrent.setStatus("current")
_NpInputAnalogTrapVoltage_Type = Integer32
_NpInputAnalogTrapVoltage_Object = MibScalar
npInputAnalogTrapVoltage = _NpInputAnalogTrapVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 4),
    _NpInputAnalogTrapVoltage_Type()
)
npInputAnalogTrapVoltage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapVoltage.setStatus("current")
_NpInputAnalogTrapResistance_Type = Unsigned32
_NpInputAnalogTrapResistance_Object = MibScalar
npInputAnalogTrapResistance = _NpInputAnalogTrapResistance_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 5),
    _NpInputAnalogTrapResistance_Type()
)
npInputAnalogTrapResistance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapResistance.setStatus("current")
_NpInputAnalogTrapMemo_Type = DisplayString
_NpInputAnalogTrapMemo_Object = MibScalar
npInputAnalogTrapMemo = _NpInputAnalogTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 6),
    _NpInputAnalogTrapMemo_Type()
)
npInputAnalogTrapMemo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapMemo.setStatus("current")


class _NpInputAnalogTrapPower_Type(Integer32):
    """Custom type npInputAnalogTrapPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("temporaryOff", 3))
    )


_NpInputAnalogTrapPower_Type.__name__ = "Integer32"
_NpInputAnalogTrapPower_Object = MibScalar
npInputAnalogTrapPower = _NpInputAnalogTrapPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 7),
    _NpInputAnalogTrapPower_Type()
)
npInputAnalogTrapPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapPower.setStatus("current")
_NpInputAnalogTrapWorkRangeHigh_Type = Integer32
_NpInputAnalogTrapWorkRangeHigh_Object = MibScalar
npInputAnalogTrapWorkRangeHigh = _NpInputAnalogTrapWorkRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 11),
    _NpInputAnalogTrapWorkRangeHigh_Type()
)
npInputAnalogTrapWorkRangeHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapWorkRangeHigh.setStatus("current")
_NpInputAnalogTrapSafeRangeHigh_Type = Integer32
_NpInputAnalogTrapSafeRangeHigh_Object = MibScalar
npInputAnalogTrapSafeRangeHigh = _NpInputAnalogTrapSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 12),
    _NpInputAnalogTrapSafeRangeHigh_Type()
)
npInputAnalogTrapSafeRangeHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapSafeRangeHigh.setStatus("current")
_NpInputAnalogTrapSafeRangeLow_Type = Integer32
_NpInputAnalogTrapSafeRangeLow_Object = MibScalar
npInputAnalogTrapSafeRangeLow = _NpInputAnalogTrapSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 13),
    _NpInputAnalogTrapSafeRangeLow_Type()
)
npInputAnalogTrapSafeRangeLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapSafeRangeLow.setStatus("current")
_NpInputAnalogTrapWorkRangeLow_Type = Integer32
_NpInputAnalogTrapWorkRangeLow_Object = MibScalar
npInputAnalogTrapWorkRangeLow = _NpInputAnalogTrapWorkRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 14),
    _NpInputAnalogTrapWorkRangeLow_Type()
)
npInputAnalogTrapWorkRangeLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    npInputAnalogTrapWorkRangeLow.setStatus("current")
_NpCurLoop_ObjectIdentity = ObjectIdentity
npCurLoop = _NpCurLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300)
)
_NpCurLoopTable_Object = MibTable
npCurLoopTable = _NpCurLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1)
)
if mibBuilder.loadTexts:
    npCurLoopTable.setStatus("current")
_NpCurLoopEntry_Object = MibTableRow
npCurLoopEntry = _NpCurLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1)
)
npCurLoopEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npCurLoopN"),
)
if mibBuilder.loadTexts:
    npCurLoopEntry.setStatus("current")


class _NpCurLoopN_Type(Integer32):
    """Custom type npCurLoopN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopN_Type.__name__ = "Integer32"
_NpCurLoopN_Object = MibTableColumn
npCurLoopN = _NpCurLoopN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1),
    _NpCurLoopN_Type()
)
npCurLoopN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopN.setStatus("current")


class _NpCurLoopStatus_Type(Integer32):
    """Custom type npCurLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("alert", 1),
          ("cut", 2),
          ("short", 3),
          ("notPowered", 4))
    )


_NpCurLoopStatus_Type.__name__ = "Integer32"
_NpCurLoopStatus_Object = MibTableColumn
npCurLoopStatus = _NpCurLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2),
    _NpCurLoopStatus_Type()
)
npCurLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopStatus.setStatus("current")


class _NpCurLoopI_Type(Integer32):
    """Custom type npCurLoopI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopI_Type.__name__ = "Integer32"
_NpCurLoopI_Object = MibTableColumn
npCurLoopI = _NpCurLoopI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3),
    _NpCurLoopI_Type()
)
npCurLoopI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopI.setStatus("current")


class _NpCurLoopV_Type(Integer32):
    """Custom type npCurLoopV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopV_Type.__name__ = "Integer32"
_NpCurLoopV_Object = MibTableColumn
npCurLoopV = _NpCurLoopV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4),
    _NpCurLoopV_Type()
)
npCurLoopV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopV.setStatus("current")


class _NpCurLoopR_Type(Integer32):
    """Custom type npCurLoopR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopR_Type.__name__ = "Integer32"
_NpCurLoopR_Object = MibTableColumn
npCurLoopR = _NpCurLoopR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5),
    _NpCurLoopR_Type()
)
npCurLoopR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopR.setStatus("current")


class _NpCurLoopPower_Type(Integer32):
    """Custom type npCurLoopPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("cyclePower", 2))
    )


_NpCurLoopPower_Type.__name__ = "Integer32"
_NpCurLoopPower_Object = MibTableColumn
npCurLoopPower = _NpCurLoopPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7),
    _NpCurLoopPower_Type()
)
npCurLoopPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopPower.setStatus("current")
_NpCurLoopTraps_ObjectIdentity = ObjectIdentity
npCurLoopTraps = _NpCurLoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2)
)
_NpCurLoopTrapPrefix_ObjectIdentity = ObjectIdentity
npCurLoopTrapPrefix = _NpCurLoopTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0)
)


class _NpCurLoopTrapN_Type(Integer32):
    """Custom type npCurLoopTrapN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopTrapN_Type.__name__ = "Integer32"
_NpCurLoopTrapN_Object = MibScalar
npCurLoopTrapN = _NpCurLoopTrapN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 1),
    _NpCurLoopTrapN_Type()
)
npCurLoopTrapN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapN.setStatus("current")


class _NpCurLoopTrapStatus_Type(Integer32):
    """Custom type npCurLoopTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("alert", 1),
          ("cut", 2),
          ("short", 3),
          ("notPowered", 4))
    )


_NpCurLoopTrapStatus_Type.__name__ = "Integer32"
_NpCurLoopTrapStatus_Object = MibScalar
npCurLoopTrapStatus = _NpCurLoopTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 2),
    _NpCurLoopTrapStatus_Type()
)
npCurLoopTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapStatus.setStatus("current")


class _NpCurLoopTrapI_Type(Integer32):
    """Custom type npCurLoopTrapI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapI_Type.__name__ = "Integer32"
_NpCurLoopTrapI_Object = MibScalar
npCurLoopTrapI = _NpCurLoopTrapI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 3),
    _NpCurLoopTrapI_Type()
)
npCurLoopTrapI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapI.setStatus("current")


class _NpCurLoopTrapV_Type(Integer32):
    """Custom type npCurLoopTrapV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapV_Type.__name__ = "Integer32"
_NpCurLoopTrapV_Object = MibScalar
npCurLoopTrapV = _NpCurLoopTrapV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 4),
    _NpCurLoopTrapV_Type()
)
npCurLoopTrapV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapV.setStatus("current")


class _NpCurLoopTrapR_Type(Integer32):
    """Custom type npCurLoopTrapR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapR_Type.__name__ = "Integer32"
_NpCurLoopTrapR_Object = MibScalar
npCurLoopTrapR = _NpCurLoopTrapR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 5),
    _NpCurLoopTrapR_Type()
)
npCurLoopTrapR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapR.setStatus("current")


class _NpCurLoopTrapPower_Type(Integer32):
    """Custom type npCurLoopTrapPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NpCurLoopTrapPower_Type.__name__ = "Integer32"
_NpCurLoopTrapPower_Object = MibScalar
npCurLoopTrapPower = _NpCurLoopTrapPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 7),
    _NpCurLoopTrapPower_Type()
)
npCurLoopTrapPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopTrapPower.setStatus("current")
_NpRelHumidity_ObjectIdentity = ObjectIdentity
npRelHumidity = _NpRelHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400)
)
_NpRelHumTable_Object = MibTable
npRelHumTable = _NpRelHumTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1)
)
if mibBuilder.loadTexts:
    npRelHumTable.setStatus("current")
_NpRelHumEntry_Object = MibTableRow
npRelHumEntry = _NpRelHumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1)
)
npRelHumEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npRelHumN"),
)
if mibBuilder.loadTexts:
    npRelHumEntry.setStatus("current")


class _NpRelHumN_Type(Integer32):
    """Custom type npRelHumN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpRelHumN_Type.__name__ = "Integer32"
_NpRelHumN_Object = MibTableColumn
npRelHumN = _NpRelHumN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 1),
    _NpRelHumN_Type()
)
npRelHumN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumN.setStatus("current")


class _NpRelHumValue_Type(Integer32):
    """Custom type npRelHumValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumValue_Type.__name__ = "Integer32"
_NpRelHumValue_Object = MibTableColumn
npRelHumValue = _NpRelHumValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 2),
    _NpRelHumValue_Type()
)
npRelHumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumValue.setStatus("current")


class _NpRelHumStatus_Type(Integer32):
    """Custom type npRelHumStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("aboveSafeRange", 3))
    )


_NpRelHumStatus_Type.__name__ = "Integer32"
_NpRelHumStatus_Object = MibTableColumn
npRelHumStatus = _NpRelHumStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 3),
    _NpRelHumStatus_Type()
)
npRelHumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumStatus.setStatus("current")


class _NpRelHumTempValue_Type(Integer32):
    """Custom type npRelHumTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 200),
    )


_NpRelHumTempValue_Type.__name__ = "Integer32"
_NpRelHumTempValue_Object = MibTableColumn
npRelHumTempValue = _NpRelHumTempValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 4),
    _NpRelHumTempValue_Type()
)
npRelHumTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempValue.setStatus("current")


class _NpRelHumTempStatus_Type(Integer32):
    """Custom type npRelHumTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("aboveSafeRange", 3))
    )


_NpRelHumTempStatus_Type.__name__ = "Integer32"
_NpRelHumTempStatus_Object = MibTableColumn
npRelHumTempStatus = _NpRelHumTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 5),
    _NpRelHumTempStatus_Type()
)
npRelHumTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempStatus.setStatus("current")
_NpRelHumMemo_Type = DisplayString
_NpRelHumMemo_Object = MibTableColumn
npRelHumMemo = _NpRelHumMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 6),
    _NpRelHumMemo_Type()
)
npRelHumMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumMemo.setStatus("current")


class _NpRelHumSafeRangeHigh_Type(Integer32):
    """Custom type npRelHumSafeRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSafeRangeHigh_Type.__name__ = "Integer32"
_NpRelHumSafeRangeHigh_Object = MibTableColumn
npRelHumSafeRangeHigh = _NpRelHumSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 7),
    _NpRelHumSafeRangeHigh_Type()
)
npRelHumSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSafeRangeHigh.setStatus("current")


class _NpRelHumSafeRangeLow_Type(Integer32):
    """Custom type npRelHumSafeRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSafeRangeLow_Type.__name__ = "Integer32"
_NpRelHumSafeRangeLow_Object = MibTableColumn
npRelHumSafeRangeLow = _NpRelHumSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 8),
    _NpRelHumSafeRangeLow_Type()
)
npRelHumSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSafeRangeLow.setStatus("current")


class _NpRelHumTempSafeRangeHigh_Type(Integer32):
    """Custom type npRelHumTempSafeRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 150),
    )


_NpRelHumTempSafeRangeHigh_Type.__name__ = "Integer32"
_NpRelHumTempSafeRangeHigh_Object = MibTableColumn
npRelHumTempSafeRangeHigh = _NpRelHumTempSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 9),
    _NpRelHumTempSafeRangeHigh_Type()
)
npRelHumTempSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempSafeRangeHigh.setStatus("current")


class _NpRelHumTempSafeRangeLow_Type(Integer32):
    """Custom type npRelHumTempSafeRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 150),
    )


_NpRelHumTempSafeRangeLow_Type.__name__ = "Integer32"
_NpRelHumTempSafeRangeLow_Object = MibTableColumn
npRelHumTempSafeRangeLow = _NpRelHumTempSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 1, 1, 10),
    _NpRelHumTempSafeRangeLow_Type()
)
npRelHumTempSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTempSafeRangeLow.setStatus("current")
_NpRelHumTrapData_ObjectIdentity = ObjectIdentity
npRelHumTrapData = _NpRelHumTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3)
)


class _NpRelHumTrapDataN_Type(Integer32):
    """Custom type npRelHumTrapDataN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpRelHumTrapDataN_Type.__name__ = "Integer32"
_NpRelHumTrapDataN_Object = MibScalar
npRelHumTrapDataN = _NpRelHumTrapDataN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 1),
    _NpRelHumTrapDataN_Type()
)
npRelHumTrapDataN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataN.setStatus("current")
_NpRelHumTrapDataValue_Type = Integer32
_NpRelHumTrapDataValue_Object = MibScalar
npRelHumTrapDataValue = _NpRelHumTrapDataValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 2),
    _NpRelHumTrapDataValue_Type()
)
npRelHumTrapDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataValue.setStatus("current")


class _NpRelHumTrapDataStatus_Type(Integer32):
    """Custom type npRelHumTrapDataStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("aboveSafeRange", 3))
    )


_NpRelHumTrapDataStatus_Type.__name__ = "Integer32"
_NpRelHumTrapDataStatus_Object = MibScalar
npRelHumTrapDataStatus = _NpRelHumTrapDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 4),
    _NpRelHumTrapDataStatus_Type()
)
npRelHumTrapDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataStatus.setStatus("current")
_NpRelHumTrapDataMemo_Type = DisplayString
_NpRelHumTrapDataMemo_Object = MibScalar
npRelHumTrapDataMemo = _NpRelHumTrapDataMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 6),
    _NpRelHumTrapDataMemo_Type()
)
npRelHumTrapDataMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataMemo.setStatus("current")
_NpRelHumTrapDataSafeRangeHigh_Type = Integer32
_NpRelHumTrapDataSafeRangeHigh_Object = MibScalar
npRelHumTrapDataSafeRangeHigh = _NpRelHumTrapDataSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 7),
    _NpRelHumTrapDataSafeRangeHigh_Type()
)
npRelHumTrapDataSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataSafeRangeHigh.setStatus("current")
_NpRelHumTrapDataSafeRangeLow_Type = Integer32
_NpRelHumTrapDataSafeRangeLow_Object = MibScalar
npRelHumTrapDataSafeRangeLow = _NpRelHumTrapDataSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 3, 8),
    _NpRelHumTrapDataSafeRangeLow_Type()
)
npRelHumTrapDataSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumTrapDataSafeRangeLow.setStatus("current")
_NpRelHumTrap_ObjectIdentity = ObjectIdentity
npRelHumTrap = _NpRelHumTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6)
)
_NpRelHumTrapAllEvents_ObjectIdentity = ObjectIdentity
npRelHumTrapAllEvents = _NpRelHumTrapAllEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 127)
)
_NpRelHumTrapTemp_ObjectIdentity = ObjectIdentity
npRelHumTrapTemp = _NpRelHumTrapTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7)
)
_NpRelHumTrapTempAllEvents_ObjectIdentity = ObjectIdentity
npRelHumTrapTempAllEvents = _NpRelHumTrapTempAllEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 127)
)
_NpThermo_ObjectIdentity = ObjectIdentity
npThermo = _NpThermo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800)
)
_NpThermoTable_Object = MibTable
npThermoTable = _NpThermoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1)
)
if mibBuilder.loadTexts:
    npThermoTable.setStatus("current")
_NpThermoEntry_Object = MibTableRow
npThermoEntry = _NpThermoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1)
)
npThermoEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npThermoSensorN"),
)
if mibBuilder.loadTexts:
    npThermoEntry.setStatus("current")


class _NpThermoSensorN_Type(Integer32):
    """Custom type npThermoSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoSensorN_Type.__name__ = "Integer32"
_NpThermoSensorN_Object = MibTableColumn
npThermoSensorN = _NpThermoSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1),
    _NpThermoSensorN_Type()
)
npThermoSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoSensorN.setStatus("current")


class _NpThermoValue_Type(Integer32):
    """Custom type npThermoValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoValue_Type.__name__ = "Integer32"
_NpThermoValue_Object = MibTableColumn
npThermoValue = _NpThermoValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2),
    _NpThermoValue_Type()
)
npThermoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoValue.setStatus("current")


class _NpThermoStatus_Type(Integer32):
    """Custom type npThermoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("low", 1),
          ("norm", 2),
          ("high", 3))
    )


_NpThermoStatus_Type.__name__ = "Integer32"
_NpThermoStatus_Object = MibTableColumn
npThermoStatus = _NpThermoStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3),
    _NpThermoStatus_Type()
)
npThermoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoStatus.setStatus("current")


class _NpThermoLow_Type(Integer32):
    """Custom type npThermoLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoLow_Type.__name__ = "Integer32"
_NpThermoLow_Object = MibTableColumn
npThermoLow = _NpThermoLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4),
    _NpThermoLow_Type()
)
npThermoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoLow.setStatus("current")


class _NpThermoHigh_Type(Integer32):
    """Custom type npThermoHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoHigh_Type.__name__ = "Integer32"
_NpThermoHigh_Object = MibTableColumn
npThermoHigh = _NpThermoHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5),
    _NpThermoHigh_Type()
)
npThermoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoHigh.setStatus("current")
_NpThermoMemo_Type = DisplayString
_NpThermoMemo_Object = MibTableColumn
npThermoMemo = _NpThermoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6),
    _NpThermoMemo_Type()
)
npThermoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoMemo.setStatus("current")
_NpThermoValuePrecise_Type = FixedPoint1000
_NpThermoValuePrecise_Object = MibTableColumn
npThermoValuePrecise = _NpThermoValuePrecise_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 7),
    _NpThermoValuePrecise_Type()
)
npThermoValuePrecise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoValuePrecise.setStatus("current")
_NpThermoTraps_ObjectIdentity = ObjectIdentity
npThermoTraps = _NpThermoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2)
)
_NpThermoTrapPrefix_ObjectIdentity = ObjectIdentity
npThermoTrapPrefix = _NpThermoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0)
)


class _NpThermoTrapSensorN_Type(Integer32):
    """Custom type npThermoTrapSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoTrapSensorN_Type.__name__ = "Integer32"
_NpThermoTrapSensorN_Object = MibScalar
npThermoTrapSensorN = _NpThermoTrapSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1),
    _NpThermoTrapSensorN_Type()
)
npThermoTrapSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapSensorN.setStatus("current")


class _NpThermoTrapValue_Type(Integer32):
    """Custom type npThermoTrapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapValue_Type.__name__ = "Integer32"
_NpThermoTrapValue_Object = MibScalar
npThermoTrapValue = _NpThermoTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2),
    _NpThermoTrapValue_Type()
)
npThermoTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapValue.setStatus("current")


class _NpThermoTrapStatus_Type(Integer32):
    """Custom type npThermoTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("low", 1),
          ("norm", 2),
          ("high", 3))
    )


_NpThermoTrapStatus_Type.__name__ = "Integer32"
_NpThermoTrapStatus_Object = MibScalar
npThermoTrapStatus = _NpThermoTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3),
    _NpThermoTrapStatus_Type()
)
npThermoTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapStatus.setStatus("current")


class _NpThermoTrapLow_Type(Integer32):
    """Custom type npThermoTrapLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapLow_Type.__name__ = "Integer32"
_NpThermoTrapLow_Object = MibScalar
npThermoTrapLow = _NpThermoTrapLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4),
    _NpThermoTrapLow_Type()
)
npThermoTrapLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapLow.setStatus("current")


class _NpThermoTrapHigh_Type(Integer32):
    """Custom type npThermoTrapHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapHigh_Type.__name__ = "Integer32"
_NpThermoTrapHigh_Object = MibScalar
npThermoTrapHigh = _NpThermoTrapHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5),
    _NpThermoTrapHigh_Type()
)
npThermoTrapHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapHigh.setStatus("current")
_NpThermoTrapMemo_Type = DisplayString
_NpThermoTrapMemo_Object = MibScalar
npThermoTrapMemo = _NpThermoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6),
    _NpThermoTrapMemo_Type()
)
npThermoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapMemo.setStatus("current")
_NpIo_ObjectIdentity = ObjectIdentity
npIo = _NpIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900)
)
_NpIoTable_Object = MibTable
npIoTable = _NpIoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1)
)
if mibBuilder.loadTexts:
    npIoTable.setStatus("current")
_NpIoEntry_Object = MibTableRow
npIoEntry = _NpIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1)
)
npIoEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npIoLineN"),
)
if mibBuilder.loadTexts:
    npIoEntry.setStatus("current")


class _NpIoLineN_Type(Integer32):
    """Custom type npIoLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpIoLineN_Type.__name__ = "Integer32"
_NpIoLineN_Object = MibTableColumn
npIoLineN = _NpIoLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1),
    _NpIoLineN_Type()
)
npIoLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLineN.setStatus("current")


class _NpIoLevelIn_Type(Integer32):
    """Custom type npIoLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelIn_Type.__name__ = "Integer32"
_NpIoLevelIn_Object = MibTableColumn
npIoLevelIn = _NpIoLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2),
    _NpIoLevelIn_Type()
)
npIoLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLevelIn.setStatus("current")


class _NpIoLevelOut_Type(Integer32):
    """Custom type npIoLevelOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("low", 0),
          ("high", 1))
    )


_NpIoLevelOut_Type.__name__ = "Integer32"
_NpIoLevelOut_Object = MibTableColumn
npIoLevelOut = _NpIoLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3),
    _NpIoLevelOut_Type()
)
npIoLevelOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoLevelOut.setStatus("current")
_NpIoMemo_Type = DisplayString
_NpIoMemo_Object = MibTableColumn
npIoMemo = _NpIoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6),
    _NpIoMemo_Type()
)
npIoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoMemo.setStatus("current")
_NpIoPulseCounter_Type = Counter32
_NpIoPulseCounter_Object = MibTableColumn
npIoPulseCounter = _NpIoPulseCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9),
    _NpIoPulseCounter_Type()
)
npIoPulseCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoPulseCounter.setStatus("current")


class _NpIoSinglePulseDuration_Type(Integer32):
    """Custom type npIoSinglePulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_NpIoSinglePulseDuration_Type.__name__ = "Integer32"
_NpIoSinglePulseDuration_Object = MibTableColumn
npIoSinglePulseDuration = _NpIoSinglePulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12),
    _NpIoSinglePulseDuration_Type()
)
npIoSinglePulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseDuration.setStatus("current")
_NpIoSinglePulseStart_Type = Integer32
_NpIoSinglePulseStart_Object = MibTableColumn
npIoSinglePulseStart = _NpIoSinglePulseStart_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13),
    _NpIoSinglePulseStart_Type()
)
npIoSinglePulseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseStart.setStatus("current")
_NpIoTraps_ObjectIdentity = ObjectIdentity
npIoTraps = _NpIoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2)
)
_NpIoTrapPrefix_ObjectIdentity = ObjectIdentity
npIoTrapPrefix = _NpIoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0)
)


class _NpIoTrapLineN_Type(Integer32):
    """Custom type npIoTrapLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NpIoTrapLineN_Type.__name__ = "Integer32"
_NpIoTrapLineN_Object = MibScalar
npIoTrapLineN = _NpIoTrapLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1),
    _NpIoTrapLineN_Type()
)
npIoTrapLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLineN.setStatus("current")


class _NpIoTrapLevelIn_Type(Integer32):
    """Custom type npIoTrapLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn_Type.__name__ = "Integer32"
_NpIoTrapLevelIn_Object = MibScalar
npIoTrapLevelIn = _NpIoTrapLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2),
    _NpIoTrapLevelIn_Type()
)
npIoTrapLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn.setStatus("current")
_NpIoTrapMemo_Type = DisplayString
_NpIoTrapMemo_Object = MibScalar
npIoTrapMemo = _NpIoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6),
    _NpIoTrapMemo_Type()
)
npIoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapMemo.setStatus("current")
_NpIoTrapLevelLegend_Type = DisplayString
_NpIoTrapLevelLegend_Object = MibScalar
npIoTrapLevelLegend = _NpIoTrapLevelLegend_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 7),
    _NpIoTrapLevelLegend_Type()
)
npIoTrapLevelLegend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelLegend.setStatus("current")
_NpVoltage_ObjectIdentity = ObjectIdentity
npVoltage = _NpVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 9000)
)
_NpVoltageTable_Object = MibTable
npVoltageTable = _NpVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1)
)
if mibBuilder.loadTexts:
    npVoltageTable.setStatus("current")
_NpVoltageEntry_Object = MibTableRow
npVoltageEntry = _NpVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1)
)
npVoltageEntry.setIndexNames(
    (0, "DKSF-70-MIB", "npVoltageN"),
)
if mibBuilder.loadTexts:
    npVoltageEntry.setStatus("current")


class _NpVoltageN_Type(Integer32):
    """Custom type npVoltageN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NpVoltageN_Type.__name__ = "Integer32"
_NpVoltageN_Object = MibTableColumn
npVoltageN = _NpVoltageN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 1),
    _NpVoltageN_Type()
)
npVoltageN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageN.setStatus("current")


class _NpVoltageRMS_Type(Integer32):
    """Custom type npVoltageRMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NpVoltageRMS_Type.__name__ = "Integer32"
_NpVoltageRMS_Object = MibTableColumn
npVoltageRMS = _NpVoltageRMS_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 2),
    _NpVoltageRMS_Type()
)
npVoltageRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageRMS.setStatus("current")


class _NpVoltageStatus_Type(Integer32):
    """Custom type npVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("bad", 2),
          ("warn", 3),
          ("good", 4))
    )


_NpVoltageStatus_Type.__name__ = "Integer32"
_NpVoltageStatus_Object = MibTableColumn
npVoltageStatus = _NpVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 3),
    _NpVoltageStatus_Type()
)
npVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageStatus.setStatus("current")


class _NpVoltageFreq_Type(Integer32):
    """Custom type npVoltageFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NpVoltageFreq_Type.__name__ = "Integer32"
_NpVoltageFreq_Object = MibTableColumn
npVoltageFreq = _NpVoltageFreq_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 4),
    _NpVoltageFreq_Type()
)
npVoltageFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageFreq.setStatus("current")


class _NpVoltageFreqStatus_Type(Integer32):
    """Custom type npVoltageFreqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("bad", 2),
          ("warn", 3),
          ("good", 4))
    )


_NpVoltageFreqStatus_Type.__name__ = "Integer32"
_NpVoltageFreqStatus_Object = MibTableColumn
npVoltageFreqStatus = _NpVoltageFreqStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 5),
    _NpVoltageFreqStatus_Type()
)
npVoltageFreqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageFreqStatus.setStatus("current")
_NpVoltageMemo_Type = DisplayString
_NpVoltageMemo_Object = MibTableColumn
npVoltageMemo = _NpVoltageMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 6),
    _NpVoltageMemo_Type()
)
npVoltageMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageMemo.setStatus("current")
_NpVoltageSagCounter_Type = Counter32
_NpVoltageSagCounter_Object = MibTableColumn
npVoltageSagCounter = _NpVoltageSagCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 10),
    _NpVoltageSagCounter_Type()
)
npVoltageSagCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npVoltageSagCounter.setStatus("current")


class _NpVoltageSagStatus_Type(Integer32):
    """Custom type npVoltageSagStatus based on Integer32"""
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
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("high", 2),
          ("medium", 3),
          ("small", 4),
          ("noSags", 5))
    )


_NpVoltageSagStatus_Type.__name__ = "Integer32"
_NpVoltageSagStatus_Object = MibTableColumn
npVoltageSagStatus = _NpVoltageSagStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 11),
    _NpVoltageSagStatus_Type()
)
npVoltageSagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageSagStatus.setStatus("current")


class _NpVoltageSagSmallThreshold_Type(Integer32):
    """Custom type npVoltageSagSmallThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpVoltageSagSmallThreshold_Type.__name__ = "Integer32"
_NpVoltageSagSmallThreshold_Object = MibTableColumn
npVoltageSagSmallThreshold = _NpVoltageSagSmallThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 12),
    _NpVoltageSagSmallThreshold_Type()
)
npVoltageSagSmallThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npVoltageSagSmallThreshold.setStatus("current")


class _NpVoltageSagMediumThreshold_Type(Integer32):
    """Custom type npVoltageSagMediumThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpVoltageSagMediumThreshold_Type.__name__ = "Integer32"
_NpVoltageSagMediumThreshold_Object = MibTableColumn
npVoltageSagMediumThreshold = _NpVoltageSagMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 13),
    _NpVoltageSagMediumThreshold_Type()
)
npVoltageSagMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npVoltageSagMediumThreshold.setStatus("current")


class _NpVoltageSagBigThreshold_Type(Integer32):
    """Custom type npVoltageSagBigThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpVoltageSagBigThreshold_Type.__name__ = "Integer32"
_NpVoltageSagBigThreshold_Object = MibTableColumn
npVoltageSagBigThreshold = _NpVoltageSagBigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 14),
    _NpVoltageSagBigThreshold_Type()
)
npVoltageSagBigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npVoltageSagBigThreshold.setStatus("current")


class _NpVoltageStandard_Type(Integer32):
    """Custom type npVoltageStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 240),
    )


_NpVoltageStandard_Type.__name__ = "Integer32"
_NpVoltageStandard_Object = MibTableColumn
npVoltageStandard = _NpVoltageStandard_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 20),
    _NpVoltageStandard_Type()
)
npVoltageStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npVoltageStandard.setStatus("current")


class _NpVoltagePeak_Type(Integer32):
    """Custom type npVoltagePeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NpVoltagePeak_Type.__name__ = "Integer32"
_NpVoltagePeak_Object = MibTableColumn
npVoltagePeak = _NpVoltagePeak_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 30),
    _NpVoltagePeak_Type()
)
npVoltagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltagePeak.setStatus("current")


class _NpVoltagePeakStatus_Type(Integer32):
    """Custom type npVoltagePeakStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("dangerous", 2),
          ("noPeaks", 3))
    )


_NpVoltagePeakStatus_Type.__name__ = "Integer32"
_NpVoltagePeakStatus_Object = MibTableColumn
npVoltagePeakStatus = _NpVoltagePeakStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 1, 1, 31),
    _NpVoltagePeakStatus_Type()
)
npVoltagePeakStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltagePeakStatus.setStatus("current")
_NpVoltageTraps_ObjectIdentity = ObjectIdentity
npVoltageTraps = _NpVoltageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2)
)
_NpVoltageTrapPrefix_ObjectIdentity = ObjectIdentity
npVoltageTrapPrefix = _NpVoltageTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 0)
)


class _NpVoltageTrapN_Type(Integer32):
    """Custom type npVoltageTrapN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NpVoltageTrapN_Type.__name__ = "Integer32"
_NpVoltageTrapN_Object = MibScalar
npVoltageTrapN = _NpVoltageTrapN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 1),
    _NpVoltageTrapN_Type()
)
npVoltageTrapN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapN.setStatus("current")


class _NpVoltageTrapRMS_Type(Integer32):
    """Custom type npVoltageTrapRMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NpVoltageTrapRMS_Type.__name__ = "Integer32"
_NpVoltageTrapRMS_Object = MibScalar
npVoltageTrapRMS = _NpVoltageTrapRMS_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 2),
    _NpVoltageTrapRMS_Type()
)
npVoltageTrapRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapRMS.setStatus("current")


class _NpVoltageTrapStatus_Type(Integer32):
    """Custom type npVoltageTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("bad", 2),
          ("warn", 3),
          ("good", 4))
    )


_NpVoltageTrapStatus_Type.__name__ = "Integer32"
_NpVoltageTrapStatus_Object = MibScalar
npVoltageTrapStatus = _NpVoltageTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 3),
    _NpVoltageTrapStatus_Type()
)
npVoltageTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapStatus.setStatus("current")


class _NpVoltageTrapFreq_Type(Integer32):
    """Custom type npVoltageTrapFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NpVoltageTrapFreq_Type.__name__ = "Integer32"
_NpVoltageTrapFreq_Object = MibScalar
npVoltageTrapFreq = _NpVoltageTrapFreq_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 4),
    _NpVoltageTrapFreq_Type()
)
npVoltageTrapFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapFreq.setStatus("current")


class _NpVoltageTrapFreqStatus_Type(Integer32):
    """Custom type npVoltageTrapFreqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("bad", 2),
          ("warn", 3),
          ("good", 4))
    )


_NpVoltageTrapFreqStatus_Type.__name__ = "Integer32"
_NpVoltageTrapFreqStatus_Object = MibScalar
npVoltageTrapFreqStatus = _NpVoltageTrapFreqStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 5),
    _NpVoltageTrapFreqStatus_Type()
)
npVoltageTrapFreqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapFreqStatus.setStatus("current")
_NpVoltageTrapMemo_Type = DisplayString
_NpVoltageTrapMemo_Object = MibScalar
npVoltageTrapMemo = _NpVoltageTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 6),
    _NpVoltageTrapMemo_Type()
)
npVoltageTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapMemo.setStatus("current")
_NpVoltageTrapSagCounter_Type = Counter32
_NpVoltageTrapSagCounter_Object = MibScalar
npVoltageTrapSagCounter = _NpVoltageTrapSagCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 10),
    _NpVoltageTrapSagCounter_Type()
)
npVoltageTrapSagCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapSagCounter.setStatus("current")


class _NpVoltageTrapSagStatus_Type(Integer32):
    """Custom type npVoltageTrapSagStatus based on Integer32"""
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
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("high", 2),
          ("medium", 3),
          ("small", 4),
          ("noSags", 5))
    )


_NpVoltageTrapSagStatus_Type.__name__ = "Integer32"
_NpVoltageTrapSagStatus_Object = MibScalar
npVoltageTrapSagStatus = _NpVoltageTrapSagStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 11),
    _NpVoltageTrapSagStatus_Type()
)
npVoltageTrapSagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapSagStatus.setStatus("current")


class _NpVoltageTrapPeak_Type(Integer32):
    """Custom type npVoltageTrapPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NpVoltageTrapPeak_Type.__name__ = "Integer32"
_NpVoltageTrapPeak_Object = MibScalar
npVoltageTrapPeak = _NpVoltageTrapPeak_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 30),
    _NpVoltageTrapPeak_Type()
)
npVoltageTrapPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapPeak.setStatus("current")


class _NpVoltageTrapPeakStatus_Type(Integer32):
    """Custom type npVoltageTrapPeakStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sensorFailed", 0),
          ("noVoltage", 1),
          ("dangerous", 2),
          ("noPeaks", 3))
    )


_NpVoltageTrapPeakStatus_Type.__name__ = "Integer32"
_NpVoltageTrapPeakStatus_Object = MibScalar
npVoltageTrapPeakStatus = _NpVoltageTrapPeakStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 31),
    _NpVoltageTrapPeakStatus_Type()
)
npVoltageTrapPeakStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npVoltageTrapPeakStatus.setStatus("current")

# Managed Objects groups


# Notification objects

npGsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)
)
npGsmTrap.setObjects(
      *(("DKSF-70-MIB", "npGsmFailed"),
        ("DKSF-70-MIB", "npGsmRegistration"),
        ("DKSF-70-MIB", "npGsmStrength"))
)
if mibBuilder.loadTexts:
    npGsmTrap.setStatus(
        "current"
    )

npGsmTrapUnparsedSms = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 2)
)
npGsmTrapUnparsedSms.setObjects(
      *(("DKSF-70-MIB", "npGsmUnparsedRxSmsFrom"),
        ("DKSF-70-MIB", "npGsmUnparsedRxSms"),
        ("DKSF-70-MIB", "npGsmUnparsedRxSmsUtf8"))
)
if mibBuilder.loadTexts:
    npGsmTrapUnparsedSms.setStatus(
        "current"
    )

npRelayTrapOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6, 100)
)
npRelayTrapOff.setObjects(
      *(("DKSF-70-MIB", "npRelayTrapN"),
        ("DKSF-70-MIB", "npRelayTrapMode"),
        ("DKSF-70-MIB", "npRelayTrapMemo"),
        ("DKSF-70-MIB", "npRelayTrapState"),
        ("DKSF-70-MIB", "npRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npRelayTrapOff.setStatus(
        "current"
    )

npRelayTrapOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6, 101)
)
npRelayTrapOn.setObjects(
      *(("DKSF-70-MIB", "npRelayTrapN"),
        ("DKSF-70-MIB", "npRelayTrapMode"),
        ("DKSF-70-MIB", "npRelayTrapMemo"),
        ("DKSF-70-MIB", "npRelayTrapState"),
        ("DKSF-70-MIB", "npRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npRelayTrapOn.setStatus(
        "current"
    )

npRelayTrapModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6, 102)
)
npRelayTrapModeChange.setObjects(
      *(("DKSF-70-MIB", "npRelayTrapN"),
        ("DKSF-70-MIB", "npRelayTrapMode"),
        ("DKSF-70-MIB", "npRelayTrapMemo"),
        ("DKSF-70-MIB", "npRelayTrapState"),
        ("DKSF-70-MIB", "npRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npRelayTrapModeChange.setStatus(
        "current"
    )

npRelayTrapReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6, 103)
)
npRelayTrapReset.setObjects(
      *(("DKSF-70-MIB", "npRelayTrapN"),
        ("DKSF-70-MIB", "npRelayTrapMode"),
        ("DKSF-70-MIB", "npRelayTrapMemo"),
        ("DKSF-70-MIB", "npRelayTrapState"),
        ("DKSF-70-MIB", "npRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npRelayTrapReset.setStatus(
        "current"
    )

npRelayTrapAllChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 6, 127, 99)
)
npRelayTrapAllChannels.setObjects(
      *(("DKSF-70-MIB", "npRelayTrapN"),
        ("DKSF-70-MIB", "npRelayTrapMode"),
        ("DKSF-70-MIB", "npRelayTrapMemo"),
        ("DKSF-70-MIB", "npRelayTrapState"),
        ("DKSF-70-MIB", "npRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npRelayTrapAllChannels.setStatus(
        "current"
    )

npExtRelayTrapOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6, 100)
)
npExtRelayTrapOff.setObjects(
      *(("DKSF-70-MIB", "npExtRelayTrapN"),
        ("DKSF-70-MIB", "npExtRelayTrapMode"),
        ("DKSF-70-MIB", "npExtRelayTrapMemo"),
        ("DKSF-70-MIB", "npExtRelayTrapState"),
        ("DKSF-70-MIB", "npExtRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npExtRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npExtRelayTrapOff.setStatus(
        "current"
    )

npExtRelayTrapOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6, 101)
)
npExtRelayTrapOn.setObjects(
      *(("DKSF-70-MIB", "npExtRelayTrapN"),
        ("DKSF-70-MIB", "npExtRelayTrapMode"),
        ("DKSF-70-MIB", "npExtRelayTrapMemo"),
        ("DKSF-70-MIB", "npExtRelayTrapState"),
        ("DKSF-70-MIB", "npExtRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npExtRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npExtRelayTrapOn.setStatus(
        "current"
    )

npExtRelayTrapModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6, 102)
)
npExtRelayTrapModeChange.setObjects(
      *(("DKSF-70-MIB", "npExtRelayTrapN"),
        ("DKSF-70-MIB", "npExtRelayTrapMode"),
        ("DKSF-70-MIB", "npExtRelayTrapMemo"),
        ("DKSF-70-MIB", "npExtRelayTrapState"),
        ("DKSF-70-MIB", "npExtRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npExtRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npExtRelayTrapModeChange.setStatus(
        "current"
    )

npExtRelayTrapReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6, 103)
)
npExtRelayTrapReset.setObjects(
      *(("DKSF-70-MIB", "npExtRelayTrapN"),
        ("DKSF-70-MIB", "npExtRelayTrapMode"),
        ("DKSF-70-MIB", "npExtRelayTrapMemo"),
        ("DKSF-70-MIB", "npExtRelayTrapState"),
        ("DKSF-70-MIB", "npExtRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npExtRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npExtRelayTrapReset.setStatus(
        "current"
    )

npExtRelayTrapAllChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 5600, 6, 127, 99)
)
npExtRelayTrapAllChannels.setObjects(
      *(("DKSF-70-MIB", "npExtRelayTrapN"),
        ("DKSF-70-MIB", "npExtRelayTrapMode"),
        ("DKSF-70-MIB", "npExtRelayTrapMemo"),
        ("DKSF-70-MIB", "npExtRelayTrapState"),
        ("DKSF-70-MIB", "npExtRelayTrapCmdSrc"),
        ("DKSF-70-MIB", "npExtRelayTrapDateTime"))
)
if mibBuilder.loadTexts:
    npExtRelayTrapAllChannels.setStatus(
        "current"
    )

npInputAnalogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8200, 2, 0, 1)
)
npInputAnalogTrap.setObjects(
      *(("DKSF-70-MIB", "npInputAnalogTrapSensorN"),
        ("DKSF-70-MIB", "npInputAnalogTrapStatus"),
        ("DKSF-70-MIB", "npInputAnalogTrapCurrent"),
        ("DKSF-70-MIB", "npInputAnalogTrapVoltage"),
        ("DKSF-70-MIB", "npInputAnalogTrapResistance"),
        ("DKSF-70-MIB", "npInputAnalogTrapMemo"),
        ("DKSF-70-MIB", "npInputAnalogTrapPower"),
        ("DKSF-70-MIB", "npInputAnalogTrapWorkRangeHigh"),
        ("DKSF-70-MIB", "npInputAnalogTrapSafeRangeHigh"),
        ("DKSF-70-MIB", "npInputAnalogTrapSafeRangeLow"),
        ("DKSF-70-MIB", "npInputAnalogTrapWorkRangeLow"))
)
if mibBuilder.loadTexts:
    npInputAnalogTrap.setStatus(
        "current"
    )

npCurLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0, 1)
)
npCurLoopTrap.setObjects(
      *(("DKSF-70-MIB", "npCurLoopTrapN"),
        ("DKSF-70-MIB", "npCurLoopTrapStatus"),
        ("DKSF-70-MIB", "npCurLoopTrapI"),
        ("DKSF-70-MIB", "npCurLoopTrapV"),
        ("DKSF-70-MIB", "npCurLoopTrapR"),
        ("DKSF-70-MIB", "npCurLoopTrapPower"),
        ("DKSF-70-MIB", "npTrapEmailTo"))
)
if mibBuilder.loadTexts:
    npCurLoopTrap.setStatus(
        "current"
    )

npRelHumTrapFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 100)
)
npRelHumTrapFail.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapFail.setStatus(
        "current"
    )

npRelHumTrapBelowSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 101)
)
npRelHumTrapBelowSafe.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapBelowSafe.setStatus(
        "current"
    )

npRelHumTrapSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 102)
)
npRelHumTrapSafe.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapSafe.setStatus(
        "current"
    )

npRelHumTrapAboveSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 103)
)
npRelHumTrapAboveSafe.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapAboveSafe.setStatus(
        "current"
    )

npRelHumTrapAllChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 6, 127, 99)
)
npRelHumTrapAllChannels.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapAllChannels.setStatus(
        "current"
    )

npRelHumTrapTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 100)
)
npRelHumTrapTempFail.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempFail.setStatus(
        "current"
    )

npRelHumTrapTempBelowSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 101)
)
npRelHumTrapTempBelowSafe.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempBelowSafe.setStatus(
        "current"
    )

npRelHumTrapTempSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 102)
)
npRelHumTrapTempSafe.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempSafe.setStatus(
        "current"
    )

npRelHumTrapTempAboveSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 103)
)
npRelHumTrapTempAboveSafe.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempAboveSafe.setStatus(
        "current"
    )

npRelHumTrapTempAllChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 7, 127, 99)
)
npRelHumTrapTempAllChannels.setObjects(
      *(("DKSF-70-MIB", "npRelHumTrapDataN"),
        ("DKSF-70-MIB", "npRelHumTrapDataStatus"),
        ("DKSF-70-MIB", "npRelHumTrapDataValue"),
        ("DKSF-70-MIB", "npRelHumTrapDataMemo"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeHigh"),
        ("DKSF-70-MIB", "npRelHumTrapDataSafeRangeLow"))
)
if mibBuilder.loadTexts:
    npRelHumTrapTempAllChannels.setStatus(
        "current"
    )

npThermoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)
)
npThermoTrap.setObjects(
      *(("DKSF-70-MIB", "npThermoTrapSensorN"),
        ("DKSF-70-MIB", "npThermoTrapValue"),
        ("DKSF-70-MIB", "npThermoTrapStatus"),
        ("DKSF-70-MIB", "npThermoTrapLow"),
        ("DKSF-70-MIB", "npThermoTrapHigh"),
        ("DKSF-70-MIB", "npThermoTrapMemo"))
)
if mibBuilder.loadTexts:
    npThermoTrap.setStatus(
        "current"
    )

npIoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)
)
npIoTrap.setObjects(
      *(("DKSF-70-MIB", "npIoTrapLineN"),
        ("DKSF-70-MIB", "npIoTrapLevelIn"),
        ("DKSF-70-MIB", "npIoTrapMemo"),
        ("DKSF-70-MIB", "npIoTrapLevelLegend"))
)
if mibBuilder.loadTexts:
    npIoTrap.setStatus(
        "current"
    )

npVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 9000, 2, 0, 1)
)
npVoltageTrap.setObjects(
      *(("DKSF-70-MIB", "npVoltageTrapN"),
        ("DKSF-70-MIB", "npVoltageTrapRMS"),
        ("DKSF-70-MIB", "npVoltageTrapStatus"),
        ("DKSF-70-MIB", "npVoltageTrapFreq"),
        ("DKSF-70-MIB", "npVoltageTrapFreqStatus"),
        ("DKSF-70-MIB", "npVoltageTrapMemo"),
        ("DKSF-70-MIB", "npVoltageTrapSagCounter"),
        ("DKSF-70-MIB", "npVoltageTrapSagStatus"),
        ("DKSF-70-MIB", "npVoltageTrapPeakStatus"))
)
if mibBuilder.loadTexts:
    npVoltageTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKSF-70-MIB",
    **{"FixedPoint1000": FixedPoint1000,
       "lightcom": lightcom,
       "uniPingServerSolutionV3": uniPingServerSolutionV3,
       "npTrapInfo": npTrapInfo,
       "npTrapEmailTo": npTrapEmailTo,
       "npReboot": npReboot,
       "npSoftReboot": npSoftReboot,
       "npResetStack": npResetStack,
       "npForcedReboot": npForcedReboot,
       "npGsm": npGsm,
       "npGsmInfo": npGsmInfo,
       "npGsmFailed": npGsmFailed,
       "npGsmRegistration": npGsmRegistration,
       "npGsmStrength": npGsmStrength,
       "npGsmSendSmsUtf8": npGsmSendSmsUtf8,
       "npGsmSendSmsWin1251": npGsmSendSmsWin1251,
       "npGsmUnparsedRxSmsFrom": npGsmUnparsedRxSmsFrom,
       "npGsmUnparsedRxSms": npGsmUnparsedRxSms,
       "npGsmUnparsedRxSmsUtf8": npGsmUnparsedRxSmsUtf8,
       "npGsmTraps": npGsmTraps,
       "npGsmTrapPrefix": npGsmTrapPrefix,
       "npGsmTrap": npGsmTrap,
       "npGsmTrapUnparsedSms": npGsmTrapUnparsedSms,
       "npRelay": npRelay,
       "npRelayTrapData": npRelayTrapData,
       "npRelayTrapN": npRelayTrapN,
       "npRelayTrapMode": npRelayTrapMode,
       "npRelayTrapMemo": npRelayTrapMemo,
       "npRelayTrapState": npRelayTrapState,
       "npRelayTrapCmdSrc": npRelayTrapCmdSrc,
       "npRelayTrapDateTime": npRelayTrapDateTime,
       "npRelayTable": npRelayTable,
       "npRelayEntry": npRelayEntry,
       "npRelayN": npRelayN,
       "npRelayMode": npRelayMode,
       "npRelayStartReset": npRelayStartReset,
       "npRelayMemo": npRelayMemo,
       "npRelayFlip": npRelayFlip,
       "npRelayState": npRelayState,
       "npRelayTrap": npRelayTrap,
       "npRelayTrapOff": npRelayTrapOff,
       "npRelayTrapOn": npRelayTrapOn,
       "npRelayTrapModeChange": npRelayTrapModeChange,
       "npRelayTrapReset": npRelayTrapReset,
       "npRelayTrapAllEvents": npRelayTrapAllEvents,
       "npRelayTrapAllChannels": npRelayTrapAllChannels,
       "npExtRelay": npExtRelay,
       "npExtRelayTrapData": npExtRelayTrapData,
       "npExtRelayTrapN": npExtRelayTrapN,
       "npExtRelayTrapMode": npExtRelayTrapMode,
       "npExtRelayTrapMemo": npExtRelayTrapMemo,
       "npExtRelayTrapState": npExtRelayTrapState,
       "npExtRelayTrapCmdSrc": npExtRelayTrapCmdSrc,
       "npExtRelayTrapDateTime": npExtRelayTrapDateTime,
       "npExtRelayTable": npExtRelayTable,
       "npExtRelayEntry": npExtRelayEntry,
       "npExtRelayN": npExtRelayN,
       "npExtRelayMode": npExtRelayMode,
       "npExtRelayStartReset": npExtRelayStartReset,
       "npExtRelayMemo": npExtRelayMemo,
       "npExtRelayFlip": npExtRelayFlip,
       "npExtRelayState": npExtRelayState,
       "npExtRelayTrap": npExtRelayTrap,
       "npExtRelayTrapOff": npExtRelayTrapOff,
       "npExtRelayTrapOn": npExtRelayTrapOn,
       "npExtRelayTrapModeChange": npExtRelayTrapModeChange,
       "npExtRelayTrapReset": npExtRelayTrapReset,
       "npExtRelayTrapAllEvents": npExtRelayTrapAllEvents,
       "npExtRelayTrapAllChannels": npExtRelayTrapAllChannels,
       "npIr": npIr,
       "npIrCtrl": npIrCtrl,
       "npIrPlayCmd": npIrPlayCmd,
       "npIrReset": npIrReset,
       "npIrStatus": npIrStatus,
       "npInputAnalog": npInputAnalog,
       "npInputAnalogTable": npInputAnalogTable,
       "npInputAnalogEntry": npInputAnalogEntry,
       "npInputAnalogSensorN": npInputAnalogSensorN,
       "npInputAnalogStatus": npInputAnalogStatus,
       "npInputAnalogCurrent": npInputAnalogCurrent,
       "npInputAnalogVoltage": npInputAnalogVoltage,
       "npInputAnalogResistance": npInputAnalogResistance,
       "npInputAnalogMemo": npInputAnalogMemo,
       "npInputAnalogPower": npInputAnalogPower,
       "npInputAnalogReset": npInputAnalogReset,
       "npInputAnalogWorkRangeHigh": npInputAnalogWorkRangeHigh,
       "npInputAnalogSafeRangeHigh": npInputAnalogSafeRangeHigh,
       "npInputAnalogSafeRangeLow": npInputAnalogSafeRangeLow,
       "npInputAnalogWorkRangeLow": npInputAnalogWorkRangeLow,
       "npInputAnalogTraps": npInputAnalogTraps,
       "npInputAnalogTrapPrefix": npInputAnalogTrapPrefix,
       "npInputAnalogTrap": npInputAnalogTrap,
       "npInputAnalogTrapSensorN": npInputAnalogTrapSensorN,
       "npInputAnalogTrapStatus": npInputAnalogTrapStatus,
       "npInputAnalogTrapCurrent": npInputAnalogTrapCurrent,
       "npInputAnalogTrapVoltage": npInputAnalogTrapVoltage,
       "npInputAnalogTrapResistance": npInputAnalogTrapResistance,
       "npInputAnalogTrapMemo": npInputAnalogTrapMemo,
       "npInputAnalogTrapPower": npInputAnalogTrapPower,
       "npInputAnalogTrapWorkRangeHigh": npInputAnalogTrapWorkRangeHigh,
       "npInputAnalogTrapSafeRangeHigh": npInputAnalogTrapSafeRangeHigh,
       "npInputAnalogTrapSafeRangeLow": npInputAnalogTrapSafeRangeLow,
       "npInputAnalogTrapWorkRangeLow": npInputAnalogTrapWorkRangeLow,
       "npCurLoop": npCurLoop,
       "npCurLoopTable": npCurLoopTable,
       "npCurLoopEntry": npCurLoopEntry,
       "npCurLoopN": npCurLoopN,
       "npCurLoopStatus": npCurLoopStatus,
       "npCurLoopI": npCurLoopI,
       "npCurLoopV": npCurLoopV,
       "npCurLoopR": npCurLoopR,
       "npCurLoopPower": npCurLoopPower,
       "npCurLoopTraps": npCurLoopTraps,
       "npCurLoopTrapPrefix": npCurLoopTrapPrefix,
       "npCurLoopTrap": npCurLoopTrap,
       "npCurLoopTrapN": npCurLoopTrapN,
       "npCurLoopTrapStatus": npCurLoopTrapStatus,
       "npCurLoopTrapI": npCurLoopTrapI,
       "npCurLoopTrapV": npCurLoopTrapV,
       "npCurLoopTrapR": npCurLoopTrapR,
       "npCurLoopTrapPower": npCurLoopTrapPower,
       "npRelHumidity": npRelHumidity,
       "npRelHumTable": npRelHumTable,
       "npRelHumEntry": npRelHumEntry,
       "npRelHumN": npRelHumN,
       "npRelHumValue": npRelHumValue,
       "npRelHumStatus": npRelHumStatus,
       "npRelHumTempValue": npRelHumTempValue,
       "npRelHumTempStatus": npRelHumTempStatus,
       "npRelHumMemo": npRelHumMemo,
       "npRelHumSafeRangeHigh": npRelHumSafeRangeHigh,
       "npRelHumSafeRangeLow": npRelHumSafeRangeLow,
       "npRelHumTempSafeRangeHigh": npRelHumTempSafeRangeHigh,
       "npRelHumTempSafeRangeLow": npRelHumTempSafeRangeLow,
       "npRelHumTrapData": npRelHumTrapData,
       "npRelHumTrapDataN": npRelHumTrapDataN,
       "npRelHumTrapDataValue": npRelHumTrapDataValue,
       "npRelHumTrapDataStatus": npRelHumTrapDataStatus,
       "npRelHumTrapDataMemo": npRelHumTrapDataMemo,
       "npRelHumTrapDataSafeRangeHigh": npRelHumTrapDataSafeRangeHigh,
       "npRelHumTrapDataSafeRangeLow": npRelHumTrapDataSafeRangeLow,
       "npRelHumTrap": npRelHumTrap,
       "npRelHumTrapFail": npRelHumTrapFail,
       "npRelHumTrapBelowSafe": npRelHumTrapBelowSafe,
       "npRelHumTrapSafe": npRelHumTrapSafe,
       "npRelHumTrapAboveSafe": npRelHumTrapAboveSafe,
       "npRelHumTrapAllEvents": npRelHumTrapAllEvents,
       "npRelHumTrapAllChannels": npRelHumTrapAllChannels,
       "npRelHumTrapTemp": npRelHumTrapTemp,
       "npRelHumTrapTempFail": npRelHumTrapTempFail,
       "npRelHumTrapTempBelowSafe": npRelHumTrapTempBelowSafe,
       "npRelHumTrapTempSafe": npRelHumTrapTempSafe,
       "npRelHumTrapTempAboveSafe": npRelHumTrapTempAboveSafe,
       "npRelHumTrapTempAllEvents": npRelHumTrapTempAllEvents,
       "npRelHumTrapTempAllChannels": npRelHumTrapTempAllChannels,
       "npThermo": npThermo,
       "npThermoTable": npThermoTable,
       "npThermoEntry": npThermoEntry,
       "npThermoSensorN": npThermoSensorN,
       "npThermoValue": npThermoValue,
       "npThermoStatus": npThermoStatus,
       "npThermoLow": npThermoLow,
       "npThermoHigh": npThermoHigh,
       "npThermoMemo": npThermoMemo,
       "npThermoValuePrecise": npThermoValuePrecise,
       "npThermoTraps": npThermoTraps,
       "npThermoTrapPrefix": npThermoTrapPrefix,
       "npThermoTrap": npThermoTrap,
       "npThermoTrapSensorN": npThermoTrapSensorN,
       "npThermoTrapValue": npThermoTrapValue,
       "npThermoTrapStatus": npThermoTrapStatus,
       "npThermoTrapLow": npThermoTrapLow,
       "npThermoTrapHigh": npThermoTrapHigh,
       "npThermoTrapMemo": npThermoTrapMemo,
       "npIo": npIo,
       "npIoTable": npIoTable,
       "npIoEntry": npIoEntry,
       "npIoLineN": npIoLineN,
       "npIoLevelIn": npIoLevelIn,
       "npIoLevelOut": npIoLevelOut,
       "npIoMemo": npIoMemo,
       "npIoPulseCounter": npIoPulseCounter,
       "npIoSinglePulseDuration": npIoSinglePulseDuration,
       "npIoSinglePulseStart": npIoSinglePulseStart,
       "npIoTraps": npIoTraps,
       "npIoTrapPrefix": npIoTrapPrefix,
       "npIoTrap": npIoTrap,
       "npIoTrapLineN": npIoTrapLineN,
       "npIoTrapLevelIn": npIoTrapLevelIn,
       "npIoTrapMemo": npIoTrapMemo,
       "npIoTrapLevelLegend": npIoTrapLevelLegend,
       "npVoltage": npVoltage,
       "npVoltageTable": npVoltageTable,
       "npVoltageEntry": npVoltageEntry,
       "npVoltageN": npVoltageN,
       "npVoltageRMS": npVoltageRMS,
       "npVoltageStatus": npVoltageStatus,
       "npVoltageFreq": npVoltageFreq,
       "npVoltageFreqStatus": npVoltageFreqStatus,
       "npVoltageMemo": npVoltageMemo,
       "npVoltageSagCounter": npVoltageSagCounter,
       "npVoltageSagStatus": npVoltageSagStatus,
       "npVoltageSagSmallThreshold": npVoltageSagSmallThreshold,
       "npVoltageSagMediumThreshold": npVoltageSagMediumThreshold,
       "npVoltageSagBigThreshold": npVoltageSagBigThreshold,
       "npVoltageStandard": npVoltageStandard,
       "npVoltagePeak": npVoltagePeak,
       "npVoltagePeakStatus": npVoltagePeakStatus,
       "npVoltageTraps": npVoltageTraps,
       "npVoltageTrapPrefix": npVoltageTrapPrefix,
       "npVoltageTrap": npVoltageTrap,
       "npVoltageTrapN": npVoltageTrapN,
       "npVoltageTrapRMS": npVoltageTrapRMS,
       "npVoltageTrapStatus": npVoltageTrapStatus,
       "npVoltageTrapFreq": npVoltageTrapFreq,
       "npVoltageTrapFreqStatus": npVoltageTrapFreqStatus,
       "npVoltageTrapMemo": npVoltageTrapMemo,
       "npVoltageTrapSagCounter": npVoltageTrapSagCounter,
       "npVoltageTrapSagStatus": npVoltageTrapSagStatus,
       "npVoltageTrapPeak": npVoltageTrapPeak,
       "npVoltageTrapPeakStatus": npVoltageTrapPeakStatus}
)
