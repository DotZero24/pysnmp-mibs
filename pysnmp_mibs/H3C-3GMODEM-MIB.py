# SNMP MIB module (H3C-3GMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-3GMODEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:33 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3c3GModem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98)
)
if mibBuilder.loadTexts:
    h3c3GModem.setRevisions(
        ("2015-12-01 12:00",
         "2014-09-09 12:00",
         "2009-04-30 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cUIMStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("absent", 1),
          ("initial", 2),
          ("fault", 3),
          ("unprotected", 4),
          ("protected", 5),
          ("pinLocked", 6),
          ("pukLocked", 7),
          ("selfDestruct", 8))
    )



class H3cSmsEncodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("ucs2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3c3GModemObjects_ObjectIdentity = ObjectIdentity
h3c3GModemObjects = _H3c3GModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1)
)
_H3cWirelessCard_ObjectIdentity = ObjectIdentity
h3cWirelessCard = _H3cWirelessCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1)
)
_H3cWirelessCardTable_Object = MibTable
h3cWirelessCardTable = _H3cWirelessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cWirelessCardTable.setStatus("current")
_H3cWirelessCardEntry_Object = MibTableRow
h3cWirelessCardEntry = _H3cWirelessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1)
)
h3cWirelessCardEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3cWirelessCardEntry.setStatus("current")


class _H3cWirelessCardIndex_Type(Integer32):
    """Custom type h3cWirelessCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cWirelessCardIndex_Type.__name__ = "Integer32"
_H3cWirelessCardIndex_Object = MibTableColumn
h3cWirelessCardIndex = _H3cWirelessCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 1),
    _H3cWirelessCardIndex_Type()
)
h3cWirelessCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardIndex.setStatus("current")


class _H3cWirelessCardModelName_Type(SnmpAdminString):
    """Custom type h3cWirelessCardModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardModelName_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardModelName_Object = MibTableColumn
h3cWirelessCardModelName = _H3cWirelessCardModelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 2),
    _H3cWirelessCardModelName_Type()
)
h3cWirelessCardModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardModelName.setStatus("current")


class _H3cWirelessCardMfgName_Type(SnmpAdminString):
    """Custom type h3cWirelessCardMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardMfgName_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardMfgName_Object = MibTableColumn
h3cWirelessCardMfgName = _H3cWirelessCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 3),
    _H3cWirelessCardMfgName_Type()
)
h3cWirelessCardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardMfgName.setStatus("current")


class _H3cWirelessCardDescription_Type(SnmpAdminString):
    """Custom type h3cWirelessCardDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardDescription_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardDescription_Object = MibTableColumn
h3cWirelessCardDescription = _H3cWirelessCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 4),
    _H3cWirelessCardDescription_Type()
)
h3cWirelessCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardDescription.setStatus("current")


class _H3cWirelessCardSerialNumber_Type(SnmpAdminString):
    """Custom type h3cWirelessCardSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cWirelessCardSerialNumber_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardSerialNumber_Object = MibTableColumn
h3cWirelessCardSerialNumber = _H3cWirelessCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 5),
    _H3cWirelessCardSerialNumber_Type()
)
h3cWirelessCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardSerialNumber.setStatus("current")


class _H3cWirelessCardCMIIID_Type(SnmpAdminString):
    """Custom type h3cWirelessCardCMIIID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cWirelessCardCMIIID_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardCMIIID_Object = MibTableColumn
h3cWirelessCardCMIIID = _H3cWirelessCardCMIIID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 6),
    _H3cWirelessCardCMIIID_Type()
)
h3cWirelessCardCMIIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardCMIIID.setStatus("current")


class _H3cWirelessCardHardwareVersion_Type(SnmpAdminString):
    """Custom type h3cWirelessCardHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardHardwareVersion_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardHardwareVersion_Object = MibTableColumn
h3cWirelessCardHardwareVersion = _H3cWirelessCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 7),
    _H3cWirelessCardHardwareVersion_Type()
)
h3cWirelessCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardHardwareVersion.setStatus("current")


class _H3cWirelessCardFirmwareVersion_Type(SnmpAdminString):
    """Custom type h3cWirelessCardFirmwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardFirmwareVersion_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardFirmwareVersion_Object = MibTableColumn
h3cWirelessCardFirmwareVersion = _H3cWirelessCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 8),
    _H3cWirelessCardFirmwareVersion_Type()
)
h3cWirelessCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardFirmwareVersion.setStatus("current")


class _H3cWirelessCardPRLVersion_Type(SnmpAdminString):
    """Custom type h3cWirelessCardPRLVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardPRLVersion_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardPRLVersion_Object = MibTableColumn
h3cWirelessCardPRLVersion = _H3cWirelessCardPRLVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 9),
    _H3cWirelessCardPRLVersion_Type()
)
h3cWirelessCardPRLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardPRLVersion.setStatus("current")
_H3cWirelessCardInterfaceIndex_Type = InterfaceIndex
_H3cWirelessCardInterfaceIndex_Object = MibTableColumn
h3cWirelessCardInterfaceIndex = _H3cWirelessCardInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 10),
    _H3cWirelessCardInterfaceIndex_Type()
)
h3cWirelessCardInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardInterfaceIndex.setStatus("current")


class _H3cWirelessCardModemStatus_Type(Integer32):
    """Custom type h3cWirelessCardModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onLine", 2),
          ("offLine", 3))
    )


_H3cWirelessCardModemStatus_Type.__name__ = "Integer32"
_H3cWirelessCardModemStatus_Object = MibTableColumn
h3cWirelessCardModemStatus = _H3cWirelessCardModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 11),
    _H3cWirelessCardModemStatus_Type()
)
h3cWirelessCardModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardModemStatus.setStatus("current")


class _H3cWirelessCardModemMode_Type(Integer32):
    """Custom type h3cWirelessCardModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("tdscdma", 2),
          ("wcdma", 3),
          ("cdma", 4),
          ("lte", 5))
    )


_H3cWirelessCardModemMode_Type.__name__ = "Integer32"
_H3cWirelessCardModemMode_Object = MibTableColumn
h3cWirelessCardModemMode = _H3cWirelessCardModemMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 12),
    _H3cWirelessCardModemMode_Type()
)
h3cWirelessCardModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardModemMode.setStatus("current")


class _H3cWirelessCardCurNetConn_Type(Integer32):
    """Custom type h3cWirelessCardCurNetConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("noService", 2),
          ("gsm", 3),
          ("gprs", 4),
          ("edge", 5),
          ("hsdpa", 6),
          ("hsupa", 7),
          ("hsupaAndhsdpa", 8),
          ("hspaPlus", 9),
          ("umts", 10),
          ("dchspaPlus", 11),
          ("lte", 12),
          ("onexrtt", 13),
          ("evdo", 14),
          ("onexrttAndevdo", 15),
          ("tdscdma", 16))
    )


_H3cWirelessCardCurNetConn_Type.__name__ = "Integer32"
_H3cWirelessCardCurNetConn_Object = MibTableColumn
h3cWirelessCardCurNetConn = _H3cWirelessCardCurNetConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 1, 1, 13),
    _H3cWirelessCardCurNetConn_Type()
)
h3cWirelessCardCurNetConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardCurNetConn.setStatus("current")
_H3cSmsGroup_ObjectIdentity = ObjectIdentity
h3cSmsGroup = _H3cSmsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2)
)
_H3cSmsScalarObjects_ObjectIdentity = ObjectIdentity
h3cSmsScalarObjects = _H3cSmsScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 1)
)
_H3cSmsRxNotifSwitch_Type = TruthValue
_H3cSmsRxNotifSwitch_Object = MibScalar
h3cSmsRxNotifSwitch = _H3cSmsRxNotifSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 1, 1),
    _H3cSmsRxNotifSwitch_Type()
)
h3cSmsRxNotifSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmsRxNotifSwitch.setStatus("current")
_H3cSmsOperationTable_Object = MibTable
h3cSmsOperationTable = _H3cSmsOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cSmsOperationTable.setStatus("current")
_H3cSmsOperationEntry_Object = MibTableRow
h3cSmsOperationEntry = _H3cSmsOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 2, 1)
)
h3cSmsOperationEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3cSmsOperationEntry.setStatus("current")


class _H3cSmsDestNumber_Type(SnmpAdminString):
    """Custom type h3cSmsDestNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_H3cSmsDestNumber_Type.__name__ = "SnmpAdminString"
_H3cSmsDestNumber_Object = MibTableColumn
h3cSmsDestNumber = _H3cSmsDestNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 2, 1, 1),
    _H3cSmsDestNumber_Type()
)
h3cSmsDestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmsDestNumber.setStatus("current")


class _H3cSmsEncode_Type(H3cSmsEncodeType):
    """Custom type h3cSmsEncode based on H3cSmsEncodeType"""
    defaultValue = 1


_H3cSmsEncode_Type.__name__ = "H3cSmsEncodeType"
_H3cSmsEncode_Object = MibTableColumn
h3cSmsEncode = _H3cSmsEncode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 2, 1, 2),
    _H3cSmsEncode_Type()
)
h3cSmsEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmsEncode.setStatus("current")


class _H3cSmsContent_Type(OctetString):
    """Custom type h3cSmsContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cSmsContent_Type.__name__ = "OctetString"
_H3cSmsContent_Object = MibTableColumn
h3cSmsContent = _H3cSmsContent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 2, 1, 3),
    _H3cSmsContent_Type()
)
h3cSmsContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmsContent.setStatus("current")


class _H3cSmsSendStatus_Type(Integer32):
    """Custom type h3cSmsSendStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("set2Send", 1),
          ("ready2Send", 2),
          ("sending", 3),
          ("sentAlready", 4),
          ("telnumberInvalid", 5),
          ("paramInvalid", 6),
          ("contentTooLong", 7),
          ("codeError", 8),
          ("unknown", 9),
          ("busy", 10),
          ("notPresent", 11),
          ("notSupport", 12),
          ("initializing", 13),
          ("noCenterNum", 14),
          ("noSim", 15),
          ("simNotReady", 16),
          ("sendAtFailed", 17),
          ("sendDisable", 18))
    )


_H3cSmsSendStatus_Type.__name__ = "Integer32"
_H3cSmsSendStatus_Object = MibTableColumn
h3cSmsSendStatus = _H3cSmsSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 2, 2, 1, 4),
    _H3cSmsSendStatus_Type()
)
h3cSmsSendStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSmsSendStatus.setStatus("current")
_H3cWirelessCardOnlineTable_Object = MibTable
h3cWirelessCardOnlineTable = _H3cWirelessCardOnlineTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cWirelessCardOnlineTable.setStatus("current")
_H3cWirelessCardOnlineEntry_Object = MibTableRow
h3cWirelessCardOnlineEntry = _H3cWirelessCardOnlineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 3, 1)
)
h3cWirelessCardOnlineEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardOnlineTime"),
)
if mibBuilder.loadTexts:
    h3cWirelessCardOnlineEntry.setStatus("current")
_H3cWirelessCardOnlineTime_Type = Unsigned32
_H3cWirelessCardOnlineTime_Object = MibTableColumn
h3cWirelessCardOnlineTime = _H3cWirelessCardOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 3, 1, 1),
    _H3cWirelessCardOnlineTime_Type()
)
h3cWirelessCardOnlineTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWirelessCardOnlineTime.setStatus("current")


class _H3cWirelessCardOnlineType_Type(Integer32):
    """Custom type h3cWirelessCardOnlineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_H3cWirelessCardOnlineType_Type.__name__ = "Integer32"
_H3cWirelessCardOnlineType_Object = MibTableColumn
h3cWirelessCardOnlineType = _H3cWirelessCardOnlineType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 1, 3, 1, 2),
    _H3cWirelessCardOnlineType_Type()
)
h3cWirelessCardOnlineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardOnlineType.setStatus("current")
_H3cUIM_ObjectIdentity = ObjectIdentity
h3cUIM = _H3cUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2)
)
_H3cUIMInfoTable_Object = MibTable
h3cUIMInfoTable = _H3cUIMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cUIMInfoTable.setStatus("current")
_H3cUIMInfoEntry_Object = MibTableRow
h3cUIMInfoEntry = _H3cUIMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1)
)
h3cUIMInfoEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
    (0, "H3C-3GMODEM-MIB", "h3cUIMIndex"),
)
if mibBuilder.loadTexts:
    h3cUIMInfoEntry.setStatus("current")


class _H3cUIMIndex_Type(Integer32):
    """Custom type h3cUIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cUIMIndex_Type.__name__ = "Integer32"
_H3cUIMIndex_Object = MibTableColumn
h3cUIMIndex = _H3cUIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 1),
    _H3cUIMIndex_Type()
)
h3cUIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cUIMIndex.setStatus("current")
_H3cUIMStatus_Type = H3cUIMStatusType
_H3cUIMStatus_Object = MibTableColumn
h3cUIMStatus = _H3cUIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 2),
    _H3cUIMStatus_Type()
)
h3cUIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMStatus.setStatus("current")


class _H3cUIMImsi_Type(SnmpAdminString):
    """Custom type h3cUIMImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cUIMImsi_Type.__name__ = "SnmpAdminString"
_H3cUIMImsi_Object = MibTableColumn
h3cUIMImsi = _H3cUIMImsi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 3),
    _H3cUIMImsi_Type()
)
h3cUIMImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMImsi.setStatus("current")


class _H3cUIMPin_Type(SnmpAdminString):
    """Custom type h3cUIMPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_H3cUIMPin_Type.__name__ = "SnmpAdminString"
_H3cUIMPin_Object = MibTableColumn
h3cUIMPin = _H3cUIMPin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 4),
    _H3cUIMPin_Type()
)
h3cUIMPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMPin.setStatus("current")


class _H3cUIMVoltage_Type(Unsigned32):
    """Custom type h3cUIMVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cUIMVoltage_Type.__name__ = "Unsigned32"
_H3cUIMVoltage_Object = MibTableColumn
h3cUIMVoltage = _H3cUIMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 5),
    _H3cUIMVoltage_Type()
)
h3cUIMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMVoltage.setStatus("current")
if mibBuilder.loadTexts:
    h3cUIMVoltage.setUnits("milli-volt")


class _H3cUIMProvider_Type(SnmpAdminString):
    """Custom type h3cUIMProvider based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cUIMProvider_Type.__name__ = "SnmpAdminString"
_H3cUIMProvider_Object = MibTableColumn
h3cUIMProvider = _H3cUIMProvider_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 6),
    _H3cUIMProvider_Type()
)
h3cUIMProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMProvider.setStatus("current")


class _H3cUIMSignal_Type(Integer32):
    """Custom type h3cUIMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(99, 99),
    )


_H3cUIMSignal_Type.__name__ = "Integer32"
_H3cUIMSignal_Object = MibTableColumn
h3cUIMSignal = _H3cUIMSignal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 7),
    _H3cUIMSignal_Type()
)
h3cUIMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMSignal.setStatus("current")


class _H3cUIMTryPinPukTimes_Type(Unsigned32):
    """Custom type h3cUIMTryPinPukTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cUIMTryPinPukTimes_Type.__name__ = "Unsigned32"
_H3cUIMTryPinPukTimes_Object = MibTableColumn
h3cUIMTryPinPukTimes = _H3cUIMTryPinPukTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 8),
    _H3cUIMTryPinPukTimes_Type()
)
h3cUIMTryPinPukTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMTryPinPukTimes.setStatus("current")


class _H3cUIMOldPin_Type(SnmpAdminString):
    """Custom type h3cUIMOldPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_H3cUIMOldPin_Type.__name__ = "SnmpAdminString"
_H3cUIMOldPin_Object = MibTableColumn
h3cUIMOldPin = _H3cUIMOldPin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 2, 1, 1, 9),
    _H3cUIMOldPin_Type()
)
h3cUIMOldPin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cUIMOldPin.setStatus("current")
_H3c3GCdma_ObjectIdentity = ObjectIdentity
h3c3GCdma = _H3c3GCdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3)
)
_H3c3GCdma1xRttTable_Object = MibTable
h3c3GCdma1xRttTable = _H3c3GCdma1xRttTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3c3GCdma1xRttTable.setStatus("current")
_H3c3GCdma1xRttEntry_Object = MibTableRow
h3c3GCdma1xRttEntry = _H3c3GCdma1xRttEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1)
)
h3c3GCdma1xRttEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3c3GCdma1xRttEntry.setStatus("current")


class _H3c3GCdma1xRttCurrentRssi_Type(Integer32):
    """Custom type h3c3GCdma1xRttCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdma1xRttCurrentRssi_Type.__name__ = "Integer32"
_H3c3GCdma1xRttCurrentRssi_Object = MibTableColumn
h3c3GCdma1xRttCurrentRssi = _H3c3GCdma1xRttCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 1),
    _H3c3GCdma1xRttCurrentRssi_Type()
)
h3c3GCdma1xRttCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttCurrentRssi.setUnits("dBm")


class _H3c3GCdma1xRttRssiMediumThreshold_Type(Integer32):
    """Custom type h3c3GCdma1xRttRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdma1xRttRssiMediumThreshold_Type.__name__ = "Integer32"
_H3c3GCdma1xRttRssiMediumThreshold_Object = MibTableColumn
h3c3GCdma1xRttRssiMediumThreshold = _H3c3GCdma1xRttRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 2),
    _H3c3GCdma1xRttRssiMediumThreshold_Type()
)
h3c3GCdma1xRttRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiMediumThreshold.setUnits("dBm")


class _H3c3GCdma1xRttRssiWeakThreshold_Type(Integer32):
    """Custom type h3c3GCdma1xRttRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdma1xRttRssiWeakThreshold_Type.__name__ = "Integer32"
_H3c3GCdma1xRttRssiWeakThreshold_Object = MibTableColumn
h3c3GCdma1xRttRssiWeakThreshold = _H3c3GCdma1xRttRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 3),
    _H3c3GCdma1xRttRssiWeakThreshold_Type()
)
h3c3GCdma1xRttRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiWeakThreshold.setUnits("dBm")


class _H3c3GCdma1xRttCurServiceStatus_Type(Integer32):
    """Custom type h3c3GCdma1xRttCurServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5))
    )


_H3c3GCdma1xRttCurServiceStatus_Type.__name__ = "Integer32"
_H3c3GCdma1xRttCurServiceStatus_Object = MibTableColumn
h3c3GCdma1xRttCurServiceStatus = _H3c3GCdma1xRttCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 4),
    _H3c3GCdma1xRttCurServiceStatus_Type()
)
h3c3GCdma1xRttCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttCurServiceStatus.setStatus("current")


class _H3c3GCdma1xRttCurRoamingStatus_Type(Integer32):
    """Custom type h3c3GCdma1xRttCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("roaming", 2),
          ("home", 3))
    )


_H3c3GCdma1xRttCurRoamingStatus_Type.__name__ = "Integer32"
_H3c3GCdma1xRttCurRoamingStatus_Object = MibTableColumn
h3c3GCdma1xRttCurRoamingStatus = _H3c3GCdma1xRttCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 5),
    _H3c3GCdma1xRttCurRoamingStatus_Type()
)
h3c3GCdma1xRttCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttCurRoamingStatus.setStatus("current")


class _H3c3GCdma1xRttBID_Type(Unsigned32):
    """Custom type h3c3GCdma1xRttBID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3c3GCdma1xRttBID_Type.__name__ = "Unsigned32"
_H3c3GCdma1xRttBID_Object = MibTableColumn
h3c3GCdma1xRttBID = _H3c3GCdma1xRttBID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 6),
    _H3c3GCdma1xRttBID_Type()
)
h3c3GCdma1xRttBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttBID.setStatus("current")


class _H3c3GCdma1xRttSID_Type(Unsigned32):
    """Custom type h3c3GCdma1xRttSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3c3GCdma1xRttSID_Type.__name__ = "Unsigned32"
_H3c3GCdma1xRttSID_Object = MibTableColumn
h3c3GCdma1xRttSID = _H3c3GCdma1xRttSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 7),
    _H3c3GCdma1xRttSID_Type()
)
h3c3GCdma1xRttSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttSID.setStatus("current")


class _H3c3GCdma1xRttNID_Type(Unsigned32):
    """Custom type h3c3GCdma1xRttNID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3c3GCdma1xRttNID_Type.__name__ = "Unsigned32"
_H3c3GCdma1xRttNID_Object = MibTableColumn
h3c3GCdma1xRttNID = _H3c3GCdma1xRttNID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 1, 1, 8),
    _H3c3GCdma1xRttNID_Type()
)
h3c3GCdma1xRttNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttNID.setStatus("current")
_H3c3GCdmaEvDoTable_Object = MibTable
h3c3GCdmaEvDoTable = _H3c3GCdmaEvDoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoTable.setStatus("current")
_H3c3GCdmaEvDoEntry_Object = MibTableRow
h3c3GCdmaEvDoEntry = _H3c3GCdmaEvDoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1)
)
h3c3GCdmaEvDoEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoEntry.setStatus("current")


class _H3c3GCdmaEvDoCurrentRssi_Type(Integer32):
    """Custom type h3c3GCdmaEvDoCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdmaEvDoCurrentRssi_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoCurrentRssi_Object = MibTableColumn
h3c3GCdmaEvDoCurrentRssi = _H3c3GCdmaEvDoCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1, 1),
    _H3c3GCdmaEvDoCurrentRssi_Type()
)
h3c3GCdmaEvDoCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoCurrentRssi.setUnits("dBm")


class _H3c3GCdmaEvDoRssiMediumThreshold_Type(Integer32):
    """Custom type h3c3GCdmaEvDoRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdmaEvDoRssiMediumThreshold_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoRssiMediumThreshold_Object = MibTableColumn
h3c3GCdmaEvDoRssiMediumThreshold = _H3c3GCdmaEvDoRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1, 2),
    _H3c3GCdmaEvDoRssiMediumThreshold_Type()
)
h3c3GCdmaEvDoRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiMediumThreshold.setUnits("dBm")


class _H3c3GCdmaEvDoRssiWeakThreshold_Type(Integer32):
    """Custom type h3c3GCdmaEvDoRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdmaEvDoRssiWeakThreshold_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoRssiWeakThreshold_Object = MibTableColumn
h3c3GCdmaEvDoRssiWeakThreshold = _H3c3GCdmaEvDoRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1, 3),
    _H3c3GCdmaEvDoRssiWeakThreshold_Type()
)
h3c3GCdmaEvDoRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiWeakThreshold.setUnits("dBm")


class _H3c3GCdmaEvDoCurServiceStatus_Type(Integer32):
    """Custom type h3c3GCdmaEvDoCurServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5))
    )


_H3c3GCdmaEvDoCurServiceStatus_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoCurServiceStatus_Object = MibTableColumn
h3c3GCdmaEvDoCurServiceStatus = _H3c3GCdmaEvDoCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1, 4),
    _H3c3GCdmaEvDoCurServiceStatus_Type()
)
h3c3GCdmaEvDoCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoCurServiceStatus.setStatus("current")


class _H3c3GCdmaEvDoCurRoamingStatus_Type(Integer32):
    """Custom type h3c3GCdmaEvDoCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("roaming", 2),
          ("home", 3))
    )


_H3c3GCdmaEvDoCurRoamingStatus_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoCurRoamingStatus_Object = MibTableColumn
h3c3GCdmaEvDoCurRoamingStatus = _H3c3GCdmaEvDoCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1, 5),
    _H3c3GCdmaEvDoCurRoamingStatus_Type()
)
h3c3GCdmaEvDoCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoCurRoamingStatus.setStatus("current")


class _H3c3GCdmaEvDoSubNetID_Type(SnmpAdminString):
    """Custom type h3c3GCdmaEvDoSubNetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GCdmaEvDoSubNetID_Type.__name__ = "SnmpAdminString"
_H3c3GCdmaEvDoSubNetID_Object = MibTableColumn
h3c3GCdmaEvDoSubNetID = _H3c3GCdmaEvDoSubNetID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 3, 2, 1, 6),
    _H3c3GCdmaEvDoSubNetID_Type()
)
h3c3GCdmaEvDoSubNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoSubNetID.setStatus("current")
_H3c3GGsm_ObjectIdentity = ObjectIdentity
h3c3GGsm = _H3c3GGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4)
)
_H3c3GGsmInfoTable_Object = MibTable
h3c3GGsmInfoTable = _H3c3GGsmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3c3GGsmInfoTable.setStatus("current")
_H3c3GGsmInfoEntry_Object = MibTableRow
h3c3GGsmInfoEntry = _H3c3GGsmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1)
)
h3c3GGsmInfoEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3c3GGsmInfoEntry.setStatus("current")


class _H3c3GGsmCurrentRssi_Type(Integer32):
    """Custom type h3c3GGsmCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_H3c3GGsmCurrentRssi_Type.__name__ = "Integer32"
_H3c3GGsmCurrentRssi_Object = MibTableColumn
h3c3GGsmCurrentRssi = _H3c3GGsmCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 1),
    _H3c3GGsmCurrentRssi_Type()
)
h3c3GGsmCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GGsmCurrentRssi.setUnits("dBm")


class _H3c3GGsmRssiMediumThreshold_Type(Integer32):
    """Custom type h3c3GGsmRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GGsmRssiMediumThreshold_Type.__name__ = "Integer32"
_H3c3GGsmRssiMediumThreshold_Object = MibTableColumn
h3c3GGsmRssiMediumThreshold = _H3c3GGsmRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 2),
    _H3c3GGsmRssiMediumThreshold_Type()
)
h3c3GGsmRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GGsmRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GGsmRssiMediumThreshold.setUnits("dBm")


class _H3c3GGsmRssiWeakThreshold_Type(Integer32):
    """Custom type h3c3GGsmRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GGsmRssiWeakThreshold_Type.__name__ = "Integer32"
_H3c3GGsmRssiWeakThreshold_Object = MibTableColumn
h3c3GGsmRssiWeakThreshold = _H3c3GGsmRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 3),
    _H3c3GGsmRssiWeakThreshold_Type()
)
h3c3GGsmRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GGsmRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GGsmRssiWeakThreshold.setUnits("dBm")


class _H3c3GGsmImsi_Type(SnmpAdminString):
    """Custom type h3c3GGsmImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmImsi_Type.__name__ = "SnmpAdminString"
_H3c3GGsmImsi_Object = MibTableColumn
h3c3GGsmImsi = _H3c3GGsmImsi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 4),
    _H3c3GGsmImsi_Type()
)
h3c3GGsmImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmImsi.setStatus("current")


class _H3c3GGsmImei_Type(SnmpAdminString):
    """Custom type h3c3GGsmImei based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmImei_Type.__name__ = "SnmpAdminString"
_H3c3GGsmImei_Object = MibTableColumn
h3c3GGsmImei = _H3c3GGsmImei_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 5),
    _H3c3GGsmImei_Type()
)
h3c3GGsmImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmImei.setStatus("current")


class _H3c3GGsmApn_Type(SnmpAdminString):
    """Custom type h3c3GGsmApn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_H3c3GGsmApn_Type.__name__ = "SnmpAdminString"
_H3c3GGsmApn_Object = MibTableColumn
h3c3GGsmApn = _H3c3GGsmApn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 6),
    _H3c3GGsmApn_Type()
)
h3c3GGsmApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GGsmApn.setStatus("current")


class _H3c3GGsmPacketSessionStatus_Type(Integer32):
    """Custom type h3c3GGsmPacketSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_H3c3GGsmPacketSessionStatus_Type.__name__ = "Integer32"
_H3c3GGsmPacketSessionStatus_Object = MibTableColumn
h3c3GGsmPacketSessionStatus = _H3c3GGsmPacketSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 7),
    _H3c3GGsmPacketSessionStatus_Type()
)
h3c3GGsmPacketSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmPacketSessionStatus.setStatus("current")


class _H3c3GGsmNetworkSelectionMode_Type(Integer32):
    """Custom type h3c3GGsmNetworkSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("automatic", 2),
          ("manual", 3))
    )


_H3c3GGsmNetworkSelectionMode_Type.__name__ = "Integer32"
_H3c3GGsmNetworkSelectionMode_Object = MibTableColumn
h3c3GGsmNetworkSelectionMode = _H3c3GGsmNetworkSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 8),
    _H3c3GGsmNetworkSelectionMode_Type()
)
h3c3GGsmNetworkSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmNetworkSelectionMode.setStatus("current")


class _H3c3GGsmMobileNetworkName_Type(SnmpAdminString):
    """Custom type h3c3GGsmMobileNetworkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmMobileNetworkName_Type.__name__ = "SnmpAdminString"
_H3c3GGsmMobileNetworkName_Object = MibTableColumn
h3c3GGsmMobileNetworkName = _H3c3GGsmMobileNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 9),
    _H3c3GGsmMobileNetworkName_Type()
)
h3c3GGsmMobileNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmMobileNetworkName.setStatus("current")


class _H3c3GGsmLac_Type(SnmpAdminString):
    """Custom type h3c3GGsmLac based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmLac_Type.__name__ = "SnmpAdminString"
_H3c3GGsmLac_Object = MibTableColumn
h3c3GGsmLac = _H3c3GGsmLac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 10),
    _H3c3GGsmLac_Type()
)
h3c3GGsmLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmLac.setStatus("current")


class _H3c3GGsmCellId_Type(SnmpAdminString):
    """Custom type h3c3GGsmCellId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmCellId_Type.__name__ = "SnmpAdminString"
_H3c3GGsmCellId_Object = MibTableColumn
h3c3GGsmCellId = _H3c3GGsmCellId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 11),
    _H3c3GGsmCellId_Type()
)
h3c3GGsmCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmCellId.setStatus("current")


class _H3c3GGsmSimStatus_Type(Integer32):
    """Custom type h3c3GGsmSimStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("notInsert", 3),
          ("networkReject", 4),
          ("blocked", 5))
    )


_H3c3GGsmSimStatus_Type.__name__ = "Integer32"
_H3c3GGsmSimStatus_Object = MibTableColumn
h3c3GGsmSimStatus = _H3c3GGsmSimStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 12),
    _H3c3GGsmSimStatus_Type()
)
h3c3GGsmSimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmSimStatus.setStatus("current")


class _H3c3GGsmCurServiceStatus_Type(Integer32):
    """Custom type h3c3GGsmCurServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5))
    )


_H3c3GGsmCurServiceStatus_Type.__name__ = "Integer32"
_H3c3GGsmCurServiceStatus_Object = MibTableColumn
h3c3GGsmCurServiceStatus = _H3c3GGsmCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 13),
    _H3c3GGsmCurServiceStatus_Type()
)
h3c3GGsmCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmCurServiceStatus.setStatus("current")


class _H3c3GGsmCurRoamingStatus_Type(Integer32):
    """Custom type h3c3GGsmCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("roaming", 2),
          ("home", 3))
    )


_H3c3GGsmCurRoamingStatus_Type.__name__ = "Integer32"
_H3c3GGsmCurRoamingStatus_Object = MibTableColumn
h3c3GGsmCurRoamingStatus = _H3c3GGsmCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 14),
    _H3c3GGsmCurRoamingStatus_Type()
)
h3c3GGsmCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmCurRoamingStatus.setStatus("current")


class _H3c3GGsmMcc_Type(SnmpAdminString):
    """Custom type h3c3GGsmMcc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmMcc_Type.__name__ = "SnmpAdminString"
_H3c3GGsmMcc_Object = MibTableColumn
h3c3GGsmMcc = _H3c3GGsmMcc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 15),
    _H3c3GGsmMcc_Type()
)
h3c3GGsmMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmMcc.setStatus("current")


class _H3c3GGsmMnc_Type(SnmpAdminString):
    """Custom type h3c3GGsmMnc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmMnc_Type.__name__ = "SnmpAdminString"
_H3c3GGsmMnc_Object = MibTableColumn
h3c3GGsmMnc = _H3c3GGsmMnc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 4, 1, 1, 16),
    _H3c3GGsmMnc_Type()
)
h3c3GGsmMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmMnc.setStatus("current")
_H3cLte_ObjectIdentity = ObjectIdentity
h3cLte = _H3cLte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5)
)
_H3cLteInfoTable_Object = MibTable
h3cLteInfoTable = _H3cLteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cLteInfoTable.setStatus("current")
_H3cLteInfoEntry_Object = MibTableRow
h3cLteInfoEntry = _H3cLteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1)
)
h3cLteInfoEntry.setIndexNames(
    (0, "H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3cLteInfoEntry.setStatus("current")
_H3cLteCurrentRsrp_Type = Integer32
_H3cLteCurrentRsrp_Object = MibTableColumn
h3cLteCurrentRsrp = _H3cLteCurrentRsrp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 1),
    _H3cLteCurrentRsrp_Type()
)
h3cLteCurrentRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLteCurrentRsrp.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteCurrentRsrp.setUnits("dBm")
_H3cLteCurrentRsrq_Type = Integer32
_H3cLteCurrentRsrq_Object = MibTableColumn
h3cLteCurrentRsrq = _H3cLteCurrentRsrq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 2),
    _H3cLteCurrentRsrq_Type()
)
h3cLteCurrentRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLteCurrentRsrq.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteCurrentRsrq.setUnits("dB")
_H3cLteCurrentSinr_Type = Integer32
_H3cLteCurrentSinr_Object = MibTableColumn
h3cLteCurrentSinr = _H3cLteCurrentSinr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 3),
    _H3cLteCurrentSinr_Type()
)
h3cLteCurrentSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLteCurrentSinr.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteCurrentSinr.setUnits("dB")
_H3cLteTxPower_Type = Integer32
_H3cLteTxPower_Object = MibTableColumn
h3cLteTxPower = _H3cLteTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 4),
    _H3cLteTxPower_Type()
)
h3cLteTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLteTxPower.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteTxPower.setUnits("dB")


class _H3cLteCurrentRssi_Type(Integer32):
    """Custom type h3cLteCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_H3cLteCurrentRssi_Type.__name__ = "Integer32"
_H3cLteCurrentRssi_Object = MibTableColumn
h3cLteCurrentRssi = _H3cLteCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 5),
    _H3cLteCurrentRssi_Type()
)
h3cLteCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLteCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteCurrentRssi.setUnits("dBm")


class _H3cLteRssiMediumThreshold_Type(Integer32):
    """Custom type h3cLteRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3cLteRssiMediumThreshold_Type.__name__ = "Integer32"
_H3cLteRssiMediumThreshold_Object = MibTableColumn
h3cLteRssiMediumThreshold = _H3cLteRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 6),
    _H3cLteRssiMediumThreshold_Type()
)
h3cLteRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLteRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteRssiMediumThreshold.setUnits("dBm")


class _H3cLteRssiWeakThreshold_Type(Integer32):
    """Custom type h3cLteRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3cLteRssiWeakThreshold_Type.__name__ = "Integer32"
_H3cLteRssiWeakThreshold_Object = MibTableColumn
h3cLteRssiWeakThreshold = _H3cLteRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 1, 5, 1, 1, 7),
    _H3cLteRssiWeakThreshold_Type()
)
h3cLteRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLteRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cLteRssiWeakThreshold.setUnits("dBm")
_H3c3GModemTrap_ObjectIdentity = ObjectIdentity
h3c3GModemTrap = _H3c3GModemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2)
)


class _H3cDevSerialNumber_Type(SnmpAdminString):
    """Custom type h3cDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDevSerialNumber_Type.__name__ = "SnmpAdminString"
_H3cDevSerialNumber_Object = MibScalar
h3cDevSerialNumber = _H3cDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 1),
    _H3cDevSerialNumber_Type()
)
h3cDevSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDevSerialNumber.setStatus("current")


class _H3cDeviceOUI_Type(SnmpAdminString):
    """Custom type h3cDeviceOUI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cDeviceOUI_Type.__name__ = "SnmpAdminString"
_H3cDeviceOUI_Object = MibScalar
h3cDeviceOUI = _H3cDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 2),
    _H3cDeviceOUI_Type()
)
h3cDeviceOUI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDeviceOUI.setStatus("current")


class _H3cAccessMedia_Type(Integer32):
    """Custom type h3cAccessMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("air", 2),
          ("cable", 3))
    )


_H3cAccessMedia_Type.__name__ = "Integer32"
_H3cAccessMedia_Object = MibScalar
h3cAccessMedia = _H3cAccessMedia_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 3),
    _H3cAccessMedia_Type()
)
h3cAccessMedia.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cAccessMedia.setStatus("current")


class _H3c3GCurrentService_Type(Integer32):
    """Custom type h3c3GCurrentService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("oneXRtt", 2),
          ("evDo", 3),
          ("gsm", 4),
          ("lte", 5))
    )


_H3c3GCurrentService_Type.__name__ = "Integer32"
_H3c3GCurrentService_Object = MibScalar
h3c3GCurrentService = _H3c3GCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 4),
    _H3c3GCurrentService_Type()
)
h3c3GCurrentService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3c3GCurrentService.setStatus("current")


class _H3c3GCurrentRssiBind_Type(Integer32):
    """Custom type h3c3GCurrentRssiBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCurrentRssiBind_Type.__name__ = "Integer32"
_H3c3GCurrentRssiBind_Object = MibScalar
h3c3GCurrentRssiBind = _H3c3GCurrentRssiBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 5),
    _H3c3GCurrentRssiBind_Type()
)
h3c3GCurrentRssiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3c3GCurrentRssiBind.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCurrentRssiBind.setUnits("dBm")


class _H3c3GImsiBind_Type(SnmpAdminString):
    """Custom type h3c3GImsiBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3c3GImsiBind_Type.__name__ = "SnmpAdminString"
_H3c3GImsiBind_Object = MibScalar
h3c3GImsiBind = _H3c3GImsiBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 6),
    _H3c3GImsiBind_Type()
)
h3c3GImsiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3c3GImsiBind.setStatus("current")


class _H3cSmsSrcNumberBind_Type(SnmpAdminString):
    """Custom type h3cSmsSrcNumberBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_H3cSmsSrcNumberBind_Type.__name__ = "SnmpAdminString"
_H3cSmsSrcNumberBind_Object = MibScalar
h3cSmsSrcNumberBind = _H3cSmsSrcNumberBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 7),
    _H3cSmsSrcNumberBind_Type()
)
h3cSmsSrcNumberBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSmsSrcNumberBind.setStatus("current")


class _H3cSmsTimeBind_Type(SnmpAdminString):
    """Custom type h3cSmsTimeBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cSmsTimeBind_Type.__name__ = "SnmpAdminString"
_H3cSmsTimeBind_Object = MibScalar
h3cSmsTimeBind = _H3cSmsTimeBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 8),
    _H3cSmsTimeBind_Type()
)
h3cSmsTimeBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSmsTimeBind.setStatus("current")
_H3cSmsEncodeBind_Type = H3cSmsEncodeType
_H3cSmsEncodeBind_Object = MibScalar
h3cSmsEncodeBind = _H3cSmsEncodeBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 9),
    _H3cSmsEncodeBind_Type()
)
h3cSmsEncodeBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSmsEncodeBind.setStatus("current")


class _H3cSmsContentBind_Type(OctetString):
    """Custom type h3cSmsContentBind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_H3cSmsContentBind_Type.__name__ = "OctetString"
_H3cSmsContentBind_Object = MibScalar
h3cSmsContentBind = _H3cSmsContentBind_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 2, 10),
    _H3cSmsContentBind_Type()
)
h3cSmsContentBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSmsContentBind.setStatus("current")
_H3c3GModemTraps_ObjectIdentity = ObjectIdentity
h3c3GModemTraps = _H3c3GModemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3)
)
_H3c3GModemTrapPrefix_ObjectIdentity = ObjectIdentity
h3c3GModemTrapPrefix = _H3c3GModemTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cWirelessCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 1)
)
h3cWirelessCardInserted.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cUIMImsi"))
)
if mibBuilder.loadTexts:
    h3cWirelessCardInserted.setStatus(
        "current"
    )

h3cWirelessCardPulledOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 2)
)
h3cWirelessCardPulledOut.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cUIMImsi"))
)
if mibBuilder.loadTexts:
    h3cWirelessCardPulledOut.setStatus(
        "current"
    )

h3cUIMPinInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 3)
)
h3cUIMPinInvalid.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cUIMImsi"))
)
if mibBuilder.loadTexts:
    h3cUIMPinInvalid.setStatus(
        "current"
    )

h3cUIMPinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 4)
)
h3cUIMPinChanged.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cUIMImsi"),
        ("H3C-3GMODEM-MIB", "h3cUIMOldPin"),
        ("H3C-3GMODEM-MIB", "h3cUIMPin"))
)
if mibBuilder.loadTexts:
    h3cUIMPinChanged.setStatus(
        "current"
    )

h3cAccessMediaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 5)
)
h3cAccessMediaChanged.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cUIMImsi"),
        ("H3C-3GMODEM-MIB", "h3cAccessMedia"))
)
if mibBuilder.loadTexts:
    h3cAccessMediaChanged.setStatus(
        "current"
    )

h3c3GRssiStrongSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 6)
)
h3c3GRssiStrongSignalTrap.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3c3GCurrentService"),
        ("H3C-3GMODEM-MIB", "h3c3GCurrentRssiBind"),
        ("H3C-3GMODEM-MIB", "h3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    h3c3GRssiStrongSignalTrap.setStatus(
        "current"
    )

h3c3GRssiMediumSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 7)
)
h3c3GRssiMediumSignalTrap.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3c3GCurrentService"),
        ("H3C-3GMODEM-MIB", "h3c3GCurrentRssiBind"),
        ("H3C-3GMODEM-MIB", "h3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    h3c3GRssiMediumSignalTrap.setStatus(
        "current"
    )

h3c3GRssiWeakSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 8)
)
h3c3GRssiWeakSignalTrap.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("H3C-3GMODEM-MIB", "h3cDeviceOUI"),
        ("H3C-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("H3C-3GMODEM-MIB", "h3c3GCurrentService"),
        ("H3C-3GMODEM-MIB", "h3c3GCurrentRssiBind"),
        ("H3C-3GMODEM-MIB", "h3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    h3c3GRssiWeakSignalTrap.setStatus(
        "current"
    )

h3cSmsTxNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 9)
)
h3cSmsTxNotification.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("H3C-3GMODEM-MIB", "h3cSmsSendStatus"))
)
if mibBuilder.loadTexts:
    h3cSmsTxNotification.setStatus(
        "current"
    )

h3cSmsRxNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 98, 3, 0, 10)
)
h3cSmsRxNotification.setObjects(
      *(("H3C-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("H3C-3GMODEM-MIB", "h3cSmsSrcNumberBind"),
        ("H3C-3GMODEM-MIB", "h3cSmsTimeBind"),
        ("H3C-3GMODEM-MIB", "h3cSmsEncodeBind"),
        ("H3C-3GMODEM-MIB", "h3cSmsContentBind"))
)
if mibBuilder.loadTexts:
    h3cSmsRxNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-3GMODEM-MIB",
    **{"H3cUIMStatusType": H3cUIMStatusType,
       "H3cSmsEncodeType": H3cSmsEncodeType,
       "h3c3GModem": h3c3GModem,
       "h3c3GModemObjects": h3c3GModemObjects,
       "h3cWirelessCard": h3cWirelessCard,
       "h3cWirelessCardTable": h3cWirelessCardTable,
       "h3cWirelessCardEntry": h3cWirelessCardEntry,
       "h3cWirelessCardIndex": h3cWirelessCardIndex,
       "h3cWirelessCardModelName": h3cWirelessCardModelName,
       "h3cWirelessCardMfgName": h3cWirelessCardMfgName,
       "h3cWirelessCardDescription": h3cWirelessCardDescription,
       "h3cWirelessCardSerialNumber": h3cWirelessCardSerialNumber,
       "h3cWirelessCardCMIIID": h3cWirelessCardCMIIID,
       "h3cWirelessCardHardwareVersion": h3cWirelessCardHardwareVersion,
       "h3cWirelessCardFirmwareVersion": h3cWirelessCardFirmwareVersion,
       "h3cWirelessCardPRLVersion": h3cWirelessCardPRLVersion,
       "h3cWirelessCardInterfaceIndex": h3cWirelessCardInterfaceIndex,
       "h3cWirelessCardModemStatus": h3cWirelessCardModemStatus,
       "h3cWirelessCardModemMode": h3cWirelessCardModemMode,
       "h3cWirelessCardCurNetConn": h3cWirelessCardCurNetConn,
       "h3cSmsGroup": h3cSmsGroup,
       "h3cSmsScalarObjects": h3cSmsScalarObjects,
       "h3cSmsRxNotifSwitch": h3cSmsRxNotifSwitch,
       "h3cSmsOperationTable": h3cSmsOperationTable,
       "h3cSmsOperationEntry": h3cSmsOperationEntry,
       "h3cSmsDestNumber": h3cSmsDestNumber,
       "h3cSmsEncode": h3cSmsEncode,
       "h3cSmsContent": h3cSmsContent,
       "h3cSmsSendStatus": h3cSmsSendStatus,
       "h3cWirelessCardOnlineTable": h3cWirelessCardOnlineTable,
       "h3cWirelessCardOnlineEntry": h3cWirelessCardOnlineEntry,
       "h3cWirelessCardOnlineTime": h3cWirelessCardOnlineTime,
       "h3cWirelessCardOnlineType": h3cWirelessCardOnlineType,
       "h3cUIM": h3cUIM,
       "h3cUIMInfoTable": h3cUIMInfoTable,
       "h3cUIMInfoEntry": h3cUIMInfoEntry,
       "h3cUIMIndex": h3cUIMIndex,
       "h3cUIMStatus": h3cUIMStatus,
       "h3cUIMImsi": h3cUIMImsi,
       "h3cUIMPin": h3cUIMPin,
       "h3cUIMVoltage": h3cUIMVoltage,
       "h3cUIMProvider": h3cUIMProvider,
       "h3cUIMSignal": h3cUIMSignal,
       "h3cUIMTryPinPukTimes": h3cUIMTryPinPukTimes,
       "h3cUIMOldPin": h3cUIMOldPin,
       "h3c3GCdma": h3c3GCdma,
       "h3c3GCdma1xRttTable": h3c3GCdma1xRttTable,
       "h3c3GCdma1xRttEntry": h3c3GCdma1xRttEntry,
       "h3c3GCdma1xRttCurrentRssi": h3c3GCdma1xRttCurrentRssi,
       "h3c3GCdma1xRttRssiMediumThreshold": h3c3GCdma1xRttRssiMediumThreshold,
       "h3c3GCdma1xRttRssiWeakThreshold": h3c3GCdma1xRttRssiWeakThreshold,
       "h3c3GCdma1xRttCurServiceStatus": h3c3GCdma1xRttCurServiceStatus,
       "h3c3GCdma1xRttCurRoamingStatus": h3c3GCdma1xRttCurRoamingStatus,
       "h3c3GCdma1xRttBID": h3c3GCdma1xRttBID,
       "h3c3GCdma1xRttSID": h3c3GCdma1xRttSID,
       "h3c3GCdma1xRttNID": h3c3GCdma1xRttNID,
       "h3c3GCdmaEvDoTable": h3c3GCdmaEvDoTable,
       "h3c3GCdmaEvDoEntry": h3c3GCdmaEvDoEntry,
       "h3c3GCdmaEvDoCurrentRssi": h3c3GCdmaEvDoCurrentRssi,
       "h3c3GCdmaEvDoRssiMediumThreshold": h3c3GCdmaEvDoRssiMediumThreshold,
       "h3c3GCdmaEvDoRssiWeakThreshold": h3c3GCdmaEvDoRssiWeakThreshold,
       "h3c3GCdmaEvDoCurServiceStatus": h3c3GCdmaEvDoCurServiceStatus,
       "h3c3GCdmaEvDoCurRoamingStatus": h3c3GCdmaEvDoCurRoamingStatus,
       "h3c3GCdmaEvDoSubNetID": h3c3GCdmaEvDoSubNetID,
       "h3c3GGsm": h3c3GGsm,
       "h3c3GGsmInfoTable": h3c3GGsmInfoTable,
       "h3c3GGsmInfoEntry": h3c3GGsmInfoEntry,
       "h3c3GGsmCurrentRssi": h3c3GGsmCurrentRssi,
       "h3c3GGsmRssiMediumThreshold": h3c3GGsmRssiMediumThreshold,
       "h3c3GGsmRssiWeakThreshold": h3c3GGsmRssiWeakThreshold,
       "h3c3GGsmImsi": h3c3GGsmImsi,
       "h3c3GGsmImei": h3c3GGsmImei,
       "h3c3GGsmApn": h3c3GGsmApn,
       "h3c3GGsmPacketSessionStatus": h3c3GGsmPacketSessionStatus,
       "h3c3GGsmNetworkSelectionMode": h3c3GGsmNetworkSelectionMode,
       "h3c3GGsmMobileNetworkName": h3c3GGsmMobileNetworkName,
       "h3c3GGsmLac": h3c3GGsmLac,
       "h3c3GGsmCellId": h3c3GGsmCellId,
       "h3c3GGsmSimStatus": h3c3GGsmSimStatus,
       "h3c3GGsmCurServiceStatus": h3c3GGsmCurServiceStatus,
       "h3c3GGsmCurRoamingStatus": h3c3GGsmCurRoamingStatus,
       "h3c3GGsmMcc": h3c3GGsmMcc,
       "h3c3GGsmMnc": h3c3GGsmMnc,
       "h3cLte": h3cLte,
       "h3cLteInfoTable": h3cLteInfoTable,
       "h3cLteInfoEntry": h3cLteInfoEntry,
       "h3cLteCurrentRsrp": h3cLteCurrentRsrp,
       "h3cLteCurrentRsrq": h3cLteCurrentRsrq,
       "h3cLteCurrentSinr": h3cLteCurrentSinr,
       "h3cLteTxPower": h3cLteTxPower,
       "h3cLteCurrentRssi": h3cLteCurrentRssi,
       "h3cLteRssiMediumThreshold": h3cLteRssiMediumThreshold,
       "h3cLteRssiWeakThreshold": h3cLteRssiWeakThreshold,
       "h3c3GModemTrap": h3c3GModemTrap,
       "h3cDevSerialNumber": h3cDevSerialNumber,
       "h3cDeviceOUI": h3cDeviceOUI,
       "h3cAccessMedia": h3cAccessMedia,
       "h3c3GCurrentService": h3c3GCurrentService,
       "h3c3GCurrentRssiBind": h3c3GCurrentRssiBind,
       "h3c3GImsiBind": h3c3GImsiBind,
       "h3cSmsSrcNumberBind": h3cSmsSrcNumberBind,
       "h3cSmsTimeBind": h3cSmsTimeBind,
       "h3cSmsEncodeBind": h3cSmsEncodeBind,
       "h3cSmsContentBind": h3cSmsContentBind,
       "h3c3GModemTraps": h3c3GModemTraps,
       "h3c3GModemTrapPrefix": h3c3GModemTrapPrefix,
       "h3cWirelessCardInserted": h3cWirelessCardInserted,
       "h3cWirelessCardPulledOut": h3cWirelessCardPulledOut,
       "h3cUIMPinInvalid": h3cUIMPinInvalid,
       "h3cUIMPinChanged": h3cUIMPinChanged,
       "h3cAccessMediaChanged": h3cAccessMediaChanged,
       "h3c3GRssiStrongSignalTrap": h3c3GRssiStrongSignalTrap,
       "h3c3GRssiMediumSignalTrap": h3c3GRssiMediumSignalTrap,
       "h3c3GRssiWeakSignalTrap": h3c3GRssiWeakSignalTrap,
       "h3cSmsTxNotification": h3cSmsTxNotification,
       "h3cSmsRxNotification": h3cSmsRxNotification}
)
