# SNMP MIB module (PACKETPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/PACKETPORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:35 2025
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

(arris,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arris")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

packetPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10)
)
if mibBuilder.loadTexts:
    packetPortMib.setRevisions(
        ("1914-10-16 00:00",
         "1913-10-09 00:00",
         "1910-05-20 00:00",
         "1909-03-16 00:00",
         "1908-08-04 00:00",
         "1908-02-13 00:00",
         "1907-10-24 00:00",
         "1907-10-19 00:00",
         "1907-05-03 00:00",
         "1906-10-16 00:00",
         "1906-05-04 00:00",
         "1905-12-01 00:00",
         "1905-09-09 00:00",
         "1905-06-14 00:00",
         "1905-02-24 00:00",
         "1905-02-05 00:00",
         "1904-12-17 00:00",
         "1904-08-04 00:00",
         "1904-03-10 00:00",
         "1903-06-16 00:00",
         "1903-05-14 00:00",
         "1903-04-17 00:00",
         "1903-04-02 00:00",
         "1903-02-12 00:00",
         "1902-06-22 00:00",
         "1902-02-26 00:00",
         "1901-11-21 00:00",
         "1901-09-10 00:00",
         "1901-04-30 00:00",
         "1900-03-09 01:00",
         "1900-12-11 00:00",
         "1900-11-14 00:00",
         "1900-10-12 00:00",
         "1900-08-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsX509ASN1DEREncodedCertificate(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )



class CodecType(TextualConvention, Integer32):
    status = "obsolete"
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
        *(("g711u", 1),
          ("g711a", 2),
          ("g7231", 3),
          ("g729", 4),
          ("g729a", 5),
          ("g729e", 6),
          ("g726", 7),
          ("g728", 8))
    )



class PacketizationPeriodType(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("ten", 10),
          ("twenty", 20),
          ("thirty", 30))
    )



class SignalingProtocol(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ncs", 1))
    )



class CountryCode(TextualConvention, Integer32):
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("northAmerica57", 1),
          ("chile", 2),
          ("japan", 3),
          ("australia", 4),
          ("austria", 5),
          ("france", 6),
          ("germany", 7),
          ("ireland", 8),
          ("netherlands", 9),
          ("portugal", 10),
          ("spain", 11),
          ("belgium", 12),
          ("poland", 13),
          ("israel", 14),
          ("czechRepublic", 15),
          ("brazil", 16),
          ("northAmerica33", 17),
          ("northAmerica09", 18),
          ("netherlands09", 19),
          ("japan600", 20),
          ("hungary", 21),
          ("sweden", 22),
          ("norway", 23),
          ("slovakia", 24),
          ("japan600L412", 25),
          ("mexico", 26),
          ("panama", 27),
          ("mexicoC", 28),
          ("swiss", 29),
          ("poland1010", 30),
          ("germany2", 31),
          ("northAmerica66", 32),
          ("argentina", 33),
          ("slovenia", 34),
          ("chileT", 35),
          ("unitedKingdom", 36),
          ("romania", 37))
    )



class PpDebugReportingLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8),
          ("level9", 9),
          ("level10", 10))
    )



class PpCallServerType(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("sn03", 1),
          ("tropico", 2),
          ("tb200gr303", 3),
          ("tb200v52", 4),
          ("clarent", 5),
          ("pktcable", 6))
    )



# MIB Managed Objects in the order of their OIDs

_PpConfiguration_ObjectIdentity = ObjectIdentity
ppConfiguration = _PpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1)
)
_PpCfgPortTable_Object = MibTable
ppCfgPortTable = _PpCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ppCfgPortTable.setStatus("current")
_PpCfgPortEntry_Object = MibTableRow
ppCfgPortEntry = _PpCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1)
)
ppCfgPortEntry.setIndexNames(
    (0, "PACKETPORT-MIB", "ppCfgPortPortNumber"),
)
if mibBuilder.loadTexts:
    ppCfgPortEntry.setStatus("current")
_PpCfgPortPortNumber_Type = Integer32
_PpCfgPortPortNumber_Object = MibTableColumn
ppCfgPortPortNumber = _PpCfgPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 1),
    _PpCfgPortPortNumber_Type()
)
ppCfgPortPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppCfgPortPortNumber.setStatus("current")


class _PpCfgPortAdminState_Type(Integer32):
    """Custom type ppCfgPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oos", 1),
          ("is", 2))
    )


_PpCfgPortAdminState_Type.__name__ = "Integer32"
_PpCfgPortAdminState_Object = MibTableColumn
ppCfgPortAdminState = _PpCfgPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 2),
    _PpCfgPortAdminState_Type()
)
ppCfgPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortAdminState.setStatus("current")
_PpCfgPortCallAgentName_Type = DisplayString
_PpCfgPortCallAgentName_Object = MibTableColumn
ppCfgPortCallAgentName = _PpCfgPortCallAgentName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 3),
    _PpCfgPortCallAgentName_Type()
)
ppCfgPortCallAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortCallAgentName.setStatus("current")
_PpCfgPortCallAgentIpAddress_Type = IpAddress
_PpCfgPortCallAgentIpAddress_Object = MibTableColumn
ppCfgPortCallAgentIpAddress = _PpCfgPortCallAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 4),
    _PpCfgPortCallAgentIpAddress_Type()
)
ppCfgPortCallAgentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortCallAgentIpAddress.setStatus("obsolete")
_PpCfgPortProvSignalingProt_Type = SignalingProtocol
_PpCfgPortProvSignalingProt_Object = MibTableColumn
ppCfgPortProvSignalingProt = _PpCfgPortProvSignalingProt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 5),
    _PpCfgPortProvSignalingProt_Type()
)
ppCfgPortProvSignalingProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortProvSignalingProt.setStatus("obsolete")


class _PpCfgPortLoopCurrent_Type(Integer32):
    """Custom type ppCfgPortLoopCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("high", 2))
    )


_PpCfgPortLoopCurrent_Type.__name__ = "Integer32"
_PpCfgPortLoopCurrent_Object = MibTableColumn
ppCfgPortLoopCurrent = _PpCfgPortLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 6),
    _PpCfgPortLoopCurrent_Type()
)
ppCfgPortLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgPortLoopCurrent.setStatus("current")


class _PpCfgPortTpar_Type(Integer32):
    """Custom type ppCfgPortTpar based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 20),
    )


_PpCfgPortTpar_Type.__name__ = "Integer32"
_PpCfgPortTpar_Object = MibTableColumn
ppCfgPortTpar = _PpCfgPortTpar_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 7),
    _PpCfgPortTpar_Type()
)
ppCfgPortTpar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortTpar.setStatus("obsolete")


class _PpCfgPortTcrit_Type(Integer32):
    """Custom type ppCfgPortTcrit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_PpCfgPortTcrit_Type.__name__ = "Integer32"
_PpCfgPortTcrit_Object = MibTableColumn
ppCfgPortTcrit = _PpCfgPortTcrit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 8),
    _PpCfgPortTcrit_Type()
)
ppCfgPortTcrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortTcrit.setStatus("obsolete")


class _PpCfgPortBusyToneTimeOut_Type(Integer32):
    """Custom type ppCfgPortBusyToneTimeOut based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 37),
    )


_PpCfgPortBusyToneTimeOut_Type.__name__ = "Integer32"
_PpCfgPortBusyToneTimeOut_Object = MibTableColumn
ppCfgPortBusyToneTimeOut = _PpCfgPortBusyToneTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 9),
    _PpCfgPortBusyToneTimeOut_Type()
)
ppCfgPortBusyToneTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortBusyToneTimeOut.setStatus("obsolete")


class _PpCfgPortDialToneTimeOut_Type(Integer32):
    """Custom type ppCfgPortDialToneTimeOut based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 20),
    )


_PpCfgPortDialToneTimeOut_Type.__name__ = "Integer32"
_PpCfgPortDialToneTimeOut_Object = MibTableColumn
ppCfgPortDialToneTimeOut = _PpCfgPortDialToneTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 10),
    _PpCfgPortDialToneTimeOut_Type()
)
ppCfgPortDialToneTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortDialToneTimeOut.setStatus("obsolete")


class _PpCfgPortMsgWaitTimeOut_Type(Integer32):
    """Custom type ppCfgPortMsgWaitTimeOut based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 20),
    )


_PpCfgPortMsgWaitTimeOut_Type.__name__ = "Integer32"
_PpCfgPortMsgWaitTimeOut_Object = MibTableColumn
ppCfgPortMsgWaitTimeOut = _PpCfgPortMsgWaitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 11),
    _PpCfgPortMsgWaitTimeOut_Type()
)
ppCfgPortMsgWaitTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortMsgWaitTimeOut.setStatus("obsolete")


class _PpCfgPortOffHookWarnTimeOut_Type(Integer32):
    """Custom type ppCfgPortOffHookWarnTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PpCfgPortOffHookWarnTimeOut_Type.__name__ = "Integer32"
_PpCfgPortOffHookWarnTimeOut_Object = MibTableColumn
ppCfgPortOffHookWarnTimeOut = _PpCfgPortOffHookWarnTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 12),
    _PpCfgPortOffHookWarnTimeOut_Type()
)
ppCfgPortOffHookWarnTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortOffHookWarnTimeOut.setStatus("obsolete")


class _PpCfgPortRingingTimeOut_Type(Integer32):
    """Custom type ppCfgPortRingingTimeOut based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 225),
    )


_PpCfgPortRingingTimeOut_Type.__name__ = "Integer32"
_PpCfgPortRingingTimeOut_Object = MibTableColumn
ppCfgPortRingingTimeOut = _PpCfgPortRingingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 13),
    _PpCfgPortRingingTimeOut_Type()
)
ppCfgPortRingingTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortRingingTimeOut.setStatus("obsolete")


class _PpCfgPortRingBackTimeOut_Type(Integer32):
    """Custom type ppCfgPortRingBackTimeOut based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(135, 225),
    )


_PpCfgPortRingBackTimeOut_Type.__name__ = "Integer32"
_PpCfgPortRingBackTimeOut_Object = MibTableColumn
ppCfgPortRingBackTimeOut = _PpCfgPortRingBackTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 14),
    _PpCfgPortRingBackTimeOut_Type()
)
ppCfgPortRingBackTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortRingBackTimeOut.setStatus("obsolete")


class _PpCfgPortReorderTimeOut_Type(Integer32):
    """Custom type ppCfgPortReorderTimeOut based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 37),
    )


_PpCfgPortReorderTimeOut_Type.__name__ = "Integer32"
_PpCfgPortReorderTimeOut_Object = MibTableColumn
ppCfgPortReorderTimeOut = _PpCfgPortReorderTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 15),
    _PpCfgPortReorderTimeOut_Type()
)
ppCfgPortReorderTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortReorderTimeOut.setStatus("obsolete")


class _PpCfgPortStutterDialToneTimeOut_Type(Integer32):
    """Custom type ppCfgPortStutterDialToneTimeOut based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 20),
    )


_PpCfgPortStutterDialToneTimeOut_Type.__name__ = "Integer32"
_PpCfgPortStutterDialToneTimeOut_Object = MibTableColumn
ppCfgPortStutterDialToneTimeOut = _PpCfgPortStutterDialToneTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 16),
    _PpCfgPortStutterDialToneTimeOut_Type()
)
ppCfgPortStutterDialToneTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortStutterDialToneTimeOut.setStatus("obsolete")


class _PpCfgPortMaxWaitDelay_Type(Integer32):
    """Custom type ppCfgPortMaxWaitDelay based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(450, 750),
    )


_PpCfgPortMaxWaitDelay_Type.__name__ = "Integer32"
_PpCfgPortMaxWaitDelay_Object = MibTableColumn
ppCfgPortMaxWaitDelay = _PpCfgPortMaxWaitDelay_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 17),
    _PpCfgPortMaxWaitDelay_Type()
)
ppCfgPortMaxWaitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortMaxWaitDelay.setStatus("obsolete")


class _PpCfgPortCallAgentUdpPort_Type(Integer32):
    """Custom type ppCfgPortCallAgentUdpPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PpCfgPortCallAgentUdpPort_Type.__name__ = "Integer32"
_PpCfgPortCallAgentUdpPort_Object = MibTableColumn
ppCfgPortCallAgentUdpPort = _PpCfgPortCallAgentUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 18),
    _PpCfgPortCallAgentUdpPort_Type()
)
ppCfgPortCallAgentUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortCallAgentUdpPort.setStatus("current")


class _PpCfgPortTxGainControl_Type(Integer32):
    """Custom type ppCfgPortTxGainControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2),
    )


_PpCfgPortTxGainControl_Type.__name__ = "Integer32"
_PpCfgPortTxGainControl_Object = MibTableColumn
ppCfgPortTxGainControl = _PpCfgPortTxGainControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 19),
    _PpCfgPortTxGainControl_Type()
)
ppCfgPortTxGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgPortTxGainControl.setStatus("current")


class _PpCfgPortRxGainControl_Type(Integer32):
    """Custom type ppCfgPortRxGainControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2),
    )


_PpCfgPortRxGainControl_Type.__name__ = "Integer32"
_PpCfgPortRxGainControl_Object = MibTableColumn
ppCfgPortRxGainControl = _PpCfgPortRxGainControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 20),
    _PpCfgPortRxGainControl_Type()
)
ppCfgPortRxGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgPortRxGainControl.setStatus("current")


class _PpCfgPortLocUserIndication_Type(Integer32):
    """Custom type ppCfgPortLocUserIndication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("silence", 0),
          ("reorderTone", 1))
    )


_PpCfgPortLocUserIndication_Type.__name__ = "Integer32"
_PpCfgPortLocUserIndication_Object = MibTableColumn
ppCfgPortLocUserIndication = _PpCfgPortLocUserIndication_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 21),
    _PpCfgPortLocUserIndication_Type()
)
ppCfgPortLocUserIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgPortLocUserIndication.setStatus("current")


class _PpCfgPortPacketizationPeriod_Type(PacketizationPeriodType):
    """Custom type ppCfgPortPacketizationPeriod based on PacketizationPeriodType"""
    defaultValue = 10


_PpCfgPortPacketizationPeriod_Type.__name__ = "PacketizationPeriodType"
_PpCfgPortPacketizationPeriod_Object = MibTableColumn
ppCfgPortPacketizationPeriod = _PpCfgPortPacketizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 22),
    _PpCfgPortPacketizationPeriod_Type()
)
ppCfgPortPacketizationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortPacketizationPeriod.setStatus("obsolete")
if mibBuilder.loadTexts:
    ppCfgPortPacketizationPeriod.setUnits("milliseconds")


class _PpCfgPortCodec_Type(CodecType):
    """Custom type ppCfgPortCodec based on CodecType"""
    defaultValue = 2


_PpCfgPortCodec_Type.__name__ = "CodecType"
_PpCfgPortCodec_Object = MibTableColumn
ppCfgPortCodec = _PpCfgPortCodec_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 23),
    _PpCfgPortCodec_Type()
)
ppCfgPortCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgPortCodec.setStatus("obsolete")


class _PpCfgPortDialingMethod_Type(Integer32):
    """Custom type ppCfgPortDialingMethod based on Integer32"""
    defaultValue = 1

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
        *(("tone", 1),
          ("pulse", 2),
          ("toneAndPulse", 3),
          ("pulseWithDTMFRelay", 4),
          ("toneAndPulseWithDTMFRelay", 5))
    )


_PpCfgPortDialingMethod_Type.__name__ = "Integer32"
_PpCfgPortDialingMethod_Object = MibTableColumn
ppCfgPortDialingMethod = _PpCfgPortDialingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 24),
    _PpCfgPortDialingMethod_Type()
)
ppCfgPortDialingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgPortDialingMethod.setStatus("deprecated")


class _PpCfgPortT38MaxDatagram_Type(Integer32):
    """Custom type ppCfgPortT38MaxDatagram based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 65535),
    )


_PpCfgPortT38MaxDatagram_Type.__name__ = "Integer32"
_PpCfgPortT38MaxDatagram_Object = MibTableColumn
ppCfgPortT38MaxDatagram = _PpCfgPortT38MaxDatagram_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 1, 1, 25),
    _PpCfgPortT38MaxDatagram_Type()
)
ppCfgPortT38MaxDatagram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgPortT38MaxDatagram.setStatus("current")


class _PpCfgMtaAdminState_Type(Integer32):
    """Custom type ppCfgMtaAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oos", 1),
          ("is", 2))
    )


_PpCfgMtaAdminState_Type.__name__ = "Integer32"
_PpCfgMtaAdminState_Object = MibScalar
ppCfgMtaAdminState = _PpCfgMtaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 2),
    _PpCfgMtaAdminState_Type()
)
ppCfgMtaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaAdminState.setStatus("current")
_PpCfgMtaTeleSyslogServIpAddr_Type = IpAddress
_PpCfgMtaTeleSyslogServIpAddr_Object = MibScalar
ppCfgMtaTeleSyslogServIpAddr = _PpCfgMtaTeleSyslogServIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 3),
    _PpCfgMtaTeleSyslogServIpAddr_Type()
)
ppCfgMtaTeleSyslogServIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaTeleSyslogServIpAddr.setStatus("current")
_PpCfgMtaTeleSyslogServName_Type = DisplayString
_PpCfgMtaTeleSyslogServName_Object = MibScalar
ppCfgMtaTeleSyslogServName = _PpCfgMtaTeleSyslogServName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 4),
    _PpCfgMtaTeleSyslogServName_Type()
)
ppCfgMtaTeleSyslogServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaTeleSyslogServName.setStatus("current")
_PpCfgMtaTeleFullyQualName_Type = DisplayString
_PpCfgMtaTeleFullyQualName_Object = MibScalar
ppCfgMtaTeleFullyQualName = _PpCfgMtaTeleFullyQualName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 5),
    _PpCfgMtaTeleFullyQualName_Type()
)
ppCfgMtaTeleFullyQualName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleFullyQualName.setStatus("obsolete")
_PpCfgMtaTeleServProvServIpAddr_Type = IpAddress
_PpCfgMtaTeleServProvServIpAddr_Object = MibScalar
ppCfgMtaTeleServProvServIpAddr = _PpCfgMtaTeleServProvServIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 6),
    _PpCfgMtaTeleServProvServIpAddr_Type()
)
ppCfgMtaTeleServProvServIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleServProvServIpAddr.setStatus("obsolete")
_PpCfgMtaTeleServProvServName_Type = DisplayString
_PpCfgMtaTeleServProvServName_Object = MibScalar
ppCfgMtaTeleServProvServName = _PpCfgMtaTeleServProvServName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 7),
    _PpCfgMtaTeleServProvServName_Type()
)
ppCfgMtaTeleServProvServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleServProvServName.setStatus("obsolete")
_PpCfgMtaTeleServProvDhcpIpAddr_Type = IpAddress
_PpCfgMtaTeleServProvDhcpIpAddr_Object = MibScalar
ppCfgMtaTeleServProvDhcpIpAddr = _PpCfgMtaTeleServProvDhcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 8),
    _PpCfgMtaTeleServProvDhcpIpAddr_Type()
)
ppCfgMtaTeleServProvDhcpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleServProvDhcpIpAddr.setStatus("obsolete")
_PpCfgMtaTeleServProvDhcpName_Type = DisplayString
_PpCfgMtaTeleServProvDhcpName_Object = MibScalar
ppCfgMtaTeleServProvDhcpName = _PpCfgMtaTeleServProvDhcpName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 9),
    _PpCfgMtaTeleServProvDhcpName_Type()
)
ppCfgMtaTeleServProvDhcpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleServProvDhcpName.setStatus("obsolete")
_PpCfgMtaPrimTeleNetDnsAddr_Type = IpAddress
_PpCfgMtaPrimTeleNetDnsAddr_Object = MibScalar
ppCfgMtaPrimTeleNetDnsAddr = _PpCfgMtaPrimTeleNetDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 10),
    _PpCfgMtaPrimTeleNetDnsAddr_Type()
)
ppCfgMtaPrimTeleNetDnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaPrimTeleNetDnsAddr.setStatus("obsolete")
_PpCfgMtaSecTeleNetDnsAddr_Type = IpAddress
_PpCfgMtaSecTeleNetDnsAddr_Object = MibScalar
ppCfgMtaSecTeleNetDnsAddr = _PpCfgMtaSecTeleNetDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 11),
    _PpCfgMtaSecTeleNetDnsAddr_Type()
)
ppCfgMtaSecTeleNetDnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaSecTeleNetDnsAddr.setStatus("obsolete")


class _PpCfgMtaCableTvEnable_Type(Integer32):
    """Custom type ppCfgMtaCableTvEnable based on Integer32"""
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


_PpCfgMtaCableTvEnable_Type.__name__ = "Integer32"
_PpCfgMtaCableTvEnable_Object = MibScalar
ppCfgMtaCableTvEnable = _PpCfgMtaCableTvEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 12),
    _PpCfgMtaCableTvEnable_Type()
)
ppCfgMtaCableTvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaCableTvEnable.setStatus("current")
_PpCfgMtaConfigFileAccName_Type = DisplayString
_PpCfgMtaConfigFileAccName_Object = MibScalar
ppCfgMtaConfigFileAccName = _PpCfgMtaConfigFileAccName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 13),
    _PpCfgMtaConfigFileAccName_Type()
)
ppCfgMtaConfigFileAccName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaConfigFileAccName.setStatus("obsolete")
_PpCfgMtaCountryTemplate_Type = CountryCode
_PpCfgMtaCountryTemplate_Object = MibScalar
ppCfgMtaCountryTemplate = _PpCfgMtaCountryTemplate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 14),
    _PpCfgMtaCountryTemplate_Type()
)
ppCfgMtaCountryTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaCountryTemplate.setStatus("current")


class _PpCfgMtaProvMethodIndicator_Type(Integer32):
    """Custom type ppCfgMtaProvMethodIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleFile", 1),
          ("dualFile", 2))
    )


_PpCfgMtaProvMethodIndicator_Type.__name__ = "Integer32"
_PpCfgMtaProvMethodIndicator_Object = MibScalar
ppCfgMtaProvMethodIndicator = _PpCfgMtaProvMethodIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 15),
    _PpCfgMtaProvMethodIndicator_Type()
)
ppCfgMtaProvMethodIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaProvMethodIndicator.setStatus("obsolete")
_PpCfgMtaTeleConfigServerIpAddr_Type = IpAddress
_PpCfgMtaTeleConfigServerIpAddr_Object = MibScalar
ppCfgMtaTeleConfigServerIpAddr = _PpCfgMtaTeleConfigServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 16),
    _PpCfgMtaTeleConfigServerIpAddr_Type()
)
ppCfgMtaTeleConfigServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleConfigServerIpAddr.setStatus("obsolete")
_PpCfgMtaTeleConfigServerName_Type = DisplayString
_PpCfgMtaTeleConfigServerName_Object = MibScalar
ppCfgMtaTeleConfigServerName = _PpCfgMtaTeleConfigServerName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 17),
    _PpCfgMtaTeleConfigServerName_Type()
)
ppCfgMtaTeleConfigServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaTeleConfigServerName.setStatus("obsolete")


class _PpCfgMtaNcsCallSigTos_Type(Integer32):
    """Custom type ppCfgMtaNcsCallSigTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PpCfgMtaNcsCallSigTos_Type.__name__ = "Integer32"
_PpCfgMtaNcsCallSigTos_Object = MibScalar
ppCfgMtaNcsCallSigTos = _PpCfgMtaNcsCallSigTos_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 18),
    _PpCfgMtaNcsCallSigTos_Type()
)
ppCfgMtaNcsCallSigTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaNcsCallSigTos.setStatus("obsolete")


class _PpCfgMtaDataInterface_Type(Integer32):
    """Custom type ppCfgMtaDataInterface based on Integer32"""
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
        *(("eth10baset", 1),
          ("hpna1mbps", 2),
          ("hpna10mbps", 3),
          ("eth100baset4", 4),
          ("eth100basex", 5))
    )


_PpCfgMtaDataInterface_Type.__name__ = "Integer32"
_PpCfgMtaDataInterface_Object = MibScalar
ppCfgMtaDataInterface = _PpCfgMtaDataInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 19),
    _PpCfgMtaDataInterface_Type()
)
ppCfgMtaDataInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaDataInterface.setStatus("current")
_PpCfgMtaCallpFeatureSwitch_Type = Integer32
_PpCfgMtaCallpFeatureSwitch_Object = MibScalar
ppCfgMtaCallpFeatureSwitch = _PpCfgMtaCallpFeatureSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 20),
    _PpCfgMtaCallpFeatureSwitch_Type()
)
ppCfgMtaCallpFeatureSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaCallpFeatureSwitch.setStatus("current")
_PpCfgMtaCallServerType_Type = PpCallServerType
_PpCfgMtaCallServerType_Object = MibScalar
ppCfgMtaCallServerType = _PpCfgMtaCallServerType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 21),
    _PpCfgMtaCallServerType_Type()
)
ppCfgMtaCallServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaCallServerType.setStatus("obsolete")


class _PpCfgMtaInternetIsolationState_Type(Integer32):
    """Custom type ppCfgMtaInternetIsolationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-InActiveMode", 1),
          ("on-ActiveMode", 2))
    )


_PpCfgMtaInternetIsolationState_Type.__name__ = "Integer32"
_PpCfgMtaInternetIsolationState_Object = MibScalar
ppCfgMtaInternetIsolationState = _PpCfgMtaInternetIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 22),
    _PpCfgMtaInternetIsolationState_Type()
)
ppCfgMtaInternetIsolationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaInternetIsolationState.setStatus("obsolete")


class _PpCfgRfc2833DigitPayloadType_Type(Integer32):
    """Custom type ppCfgRfc2833DigitPayloadType based on Integer32"""
    defaultValue = 101

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_PpCfgRfc2833DigitPayloadType_Type.__name__ = "Integer32"
_PpCfgRfc2833DigitPayloadType_Object = MibScalar
ppCfgRfc2833DigitPayloadType = _PpCfgRfc2833DigitPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 23),
    _PpCfgRfc2833DigitPayloadType_Type()
)
ppCfgRfc2833DigitPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgRfc2833DigitPayloadType.setStatus("current")
_PpCfgMtaFeatureSwitch_Type = Integer32
_PpCfgMtaFeatureSwitch_Object = MibScalar
ppCfgMtaFeatureSwitch = _PpCfgMtaFeatureSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 24),
    _PpCfgMtaFeatureSwitch_Type()
)
ppCfgMtaFeatureSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaFeatureSwitch.setStatus("current")


class _PpCfgMtaBatteryReplaceReporting_Type(Integer32):
    """Custom type ppCfgMtaBatteryReplaceReporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("delayed", 2))
    )


_PpCfgMtaBatteryReplaceReporting_Type.__name__ = "Integer32"
_PpCfgMtaBatteryReplaceReporting_Object = MibScalar
ppCfgMtaBatteryReplaceReporting = _PpCfgMtaBatteryReplaceReporting_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 25),
    _PpCfgMtaBatteryReplaceReporting_Type()
)
ppCfgMtaBatteryReplaceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaBatteryReplaceReporting.setStatus("current")


class _PpCfgNsePayloadType_Type(Integer32):
    """Custom type ppCfgNsePayloadType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(97, 127),
    )


_PpCfgNsePayloadType_Type.__name__ = "Integer32"
_PpCfgNsePayloadType_Object = MibScalar
ppCfgNsePayloadType = _PpCfgNsePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 26),
    _PpCfgNsePayloadType_Type()
)
ppCfgNsePayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgNsePayloadType.setStatus("current")
_PpCfgMtaCallpFeatureSwitch2_Type = Integer32
_PpCfgMtaCallpFeatureSwitch2_Object = MibScalar
ppCfgMtaCallpFeatureSwitch2 = _PpCfgMtaCallpFeatureSwitch2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 27),
    _PpCfgMtaCallpFeatureSwitch2_Type()
)
ppCfgMtaCallpFeatureSwitch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaCallpFeatureSwitch2.setStatus("current")
_PpCfgMtaDevSecurity_ObjectIdentity = ObjectIdentity
ppCfgMtaDevSecurity = _PpCfgMtaDevSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 29)
)
_PpCfgMtaDevServiceProviderTestRootCert_ObjectIdentity = ObjectIdentity
ppCfgMtaDevServiceProviderTestRootCert = _PpCfgMtaDevServiceProviderTestRootCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 29, 1)
)
_PpCfgMtaDevSPTestRootCertServer_Type = IpAddress
_PpCfgMtaDevSPTestRootCertServer_Object = MibScalar
ppCfgMtaDevSPTestRootCertServer = _PpCfgMtaDevSPTestRootCertServer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 29, 1, 1),
    _PpCfgMtaDevSPTestRootCertServer_Type()
)
ppCfgMtaDevSPTestRootCertServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaDevSPTestRootCertServer.setStatus("current")


class _PpCfgMtaDevSPTestRootCertFilename_Type(DisplayString):
    """Custom type ppCfgMtaDevSPTestRootCertFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PpCfgMtaDevSPTestRootCertFilename_Type.__name__ = "DisplayString"
_PpCfgMtaDevSPTestRootCertFilename_Object = MibScalar
ppCfgMtaDevSPTestRootCertFilename = _PpCfgMtaDevSPTestRootCertFilename_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 29, 1, 2),
    _PpCfgMtaDevSPTestRootCertFilename_Type()
)
ppCfgMtaDevSPTestRootCertFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaDevSPTestRootCertFilename.setStatus("current")


class _PpCfgMtaDevSPTestRootCertAdminStatus_Type(Integer32):
    """Custom type ppCfgMtaDevSPTestRootCertAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignoreCertSettings", 0),
          ("useEmbeddedTestRootCert", 1),
          ("downloadTestRootCert", 2))
    )


_PpCfgMtaDevSPTestRootCertAdminStatus_Type.__name__ = "Integer32"
_PpCfgMtaDevSPTestRootCertAdminStatus_Object = MibScalar
ppCfgMtaDevSPTestRootCertAdminStatus = _PpCfgMtaDevSPTestRootCertAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 29, 1, 3),
    _PpCfgMtaDevSPTestRootCertAdminStatus_Type()
)
ppCfgMtaDevSPTestRootCertAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaDevSPTestRootCertAdminStatus.setStatus("current")


class _PpCfgMtaDevSPTestRootCertDownloadState_Type(Integer32):
    """Custom type ppCfgMtaDevSPTestRootCertDownloadState based on Integer32"""
    defaultValue = 0

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
        *(("noDownload", 0),
          ("downloadRequested", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("failed", 4))
    )


_PpCfgMtaDevSPTestRootCertDownloadState_Type.__name__ = "Integer32"
_PpCfgMtaDevSPTestRootCertDownloadState_Object = MibScalar
ppCfgMtaDevSPTestRootCertDownloadState = _PpCfgMtaDevSPTestRootCertDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 29, 1, 4),
    _PpCfgMtaDevSPTestRootCertDownloadState_Type()
)
ppCfgMtaDevSPTestRootCertDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppCfgMtaDevSPTestRootCertDownloadState.setStatus("current")
_PpCfgDevHttp_ObjectIdentity = ObjectIdentity
ppCfgDevHttp = _PpCfgDevHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 30)
)


class _PpCfgMtaLanHttpAccess_Type(Integer32):
    """Custom type ppCfgMtaLanHttpAccess based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("basic", 2),
          ("advanced", 3),
          ("until-registered", 4))
    )


_PpCfgMtaLanHttpAccess_Type.__name__ = "Integer32"
_PpCfgMtaLanHttpAccess_Object = MibScalar
ppCfgMtaLanHttpAccess = _PpCfgMtaLanHttpAccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 30, 1),
    _PpCfgMtaLanHttpAccess_Type()
)
ppCfgMtaLanHttpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaLanHttpAccess.setStatus("deprecated")


class _PpCfgMtaWanHttpAccess_Type(Integer32):
    """Custom type ppCfgMtaWanHttpAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("basic", 2),
          ("advanced", 3))
    )


_PpCfgMtaWanHttpAccess_Type.__name__ = "Integer32"
_PpCfgMtaWanHttpAccess_Object = MibScalar
ppCfgMtaWanHttpAccess = _PpCfgMtaWanHttpAccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 30, 2),
    _PpCfgMtaWanHttpAccess_Type()
)
ppCfgMtaWanHttpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaWanHttpAccess.setStatus("deprecated")


class _PpCfgMtaClientSeed_Type(OctetString):
    """Custom type ppCfgMtaClientSeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PpCfgMtaClientSeed_Type.__name__ = "OctetString"
_PpCfgMtaClientSeed_Object = MibScalar
ppCfgMtaClientSeed = _PpCfgMtaClientSeed_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 30, 3),
    _PpCfgMtaClientSeed_Type()
)
ppCfgMtaClientSeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaClientSeed.setStatus("obsolete")


class _PpCfgMtaHTTPAdvLink_Type(Integer32):
    """Custom type ppCfgMtaHTTPAdvLink based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-restricted", 1),
          ("restricted", 2))
    )


_PpCfgMtaHTTPAdvLink_Type.__name__ = "Integer32"
_PpCfgMtaHTTPAdvLink_Object = MibScalar
ppCfgMtaHTTPAdvLink = _PpCfgMtaHTTPAdvLink_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 1, 30, 4),
    _PpCfgMtaHTTPAdvLink_Type()
)
ppCfgMtaHTTPAdvLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppCfgMtaHTTPAdvLink.setStatus("obsolete")
_PpSurveillance_ObjectIdentity = ObjectIdentity
ppSurveillance = _PpSurveillance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2)
)
_PpSurvPortTable_Object = MibTable
ppSurvPortTable = _PpSurvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1)
)
if mibBuilder.loadTexts:
    ppSurvPortTable.setStatus("current")
_PpSurvPortEntry_Object = MibTableRow
ppSurvPortEntry = _PpSurvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1)
)
ppSurvPortEntry.setIndexNames(
    (0, "PACKETPORT-MIB", "ppSurvPortNumber"),
)
if mibBuilder.loadTexts:
    ppSurvPortEntry.setStatus("current")
_PpSurvPortNumber_Type = Integer32
_PpSurvPortNumber_Object = MibTableColumn
ppSurvPortNumber = _PpSurvPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1, 1),
    _PpSurvPortNumber_Type()
)
ppSurvPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppSurvPortNumber.setStatus("current")


class _PpSurvPortMaintState_Type(Integer32):
    """Custom type ppSurvPortMaintState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("isnr", 1),
          ("isnr-trafbsy", 2),
          ("istrbl-mismatch", 3),
          ("istrbl-fef", 4),
          ("istrbl-tstf", 5),
          ("istrbl-diag", 6),
          ("istrbl-lcprt", 7),
          ("oosnr-unprov", 8),
          ("oosnr", 9),
          ("oostrbl", 10),
          ("oostrbl-tstf", 11),
          ("oostrbl-diag", 12),
          ("oostrbl-lcprt", 13))
    )


_PpSurvPortMaintState_Type.__name__ = "Integer32"
_PpSurvPortMaintState_Object = MibTableColumn
ppSurvPortMaintState = _PpSurvPortMaintState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1, 2),
    _PpSurvPortMaintState_Type()
)
ppSurvPortMaintState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvPortMaintState.setStatus("current")
_PpSurvPortDigitMap_Type = DisplayString
_PpSurvPortDigitMap_Object = MibTableColumn
ppSurvPortDigitMap = _PpSurvPortDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1, 3),
    _PpSurvPortDigitMap_Type()
)
ppSurvPortDigitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvPortDigitMap.setStatus("obsolete")
_PpSurvPortLcDiagRequest_Type = TruthValue
_PpSurvPortLcDiagRequest_Object = MibTableColumn
ppSurvPortLcDiagRequest = _PpSurvPortLcDiagRequest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1, 4),
    _PpSurvPortLcDiagRequest_Type()
)
ppSurvPortLcDiagRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppSurvPortLcDiagRequest.setStatus("current")
_PpSurvPortDeprovRequest_Type = TruthValue
_PpSurvPortDeprovRequest_Object = MibTableColumn
ppSurvPortDeprovRequest = _PpSurvPortDeprovRequest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1, 5),
    _PpSurvPortDeprovRequest_Type()
)
ppSurvPortDeprovRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppSurvPortDeprovRequest.setStatus("current")


class _PpSurvPortLcDiagLastResult_Type(Integer32):
    """Custom type ppSurvPortLcDiagLastResult based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("diagnostics-passed", 1),
          ("slac-revision-failure", 2),
          ("mpi-failure", 3),
          ("power-or-clock-failure", 4),
          ("pcm-failure", 5),
          ("standby-hook-failure", 6),
          ("active-hook-failure", 7),
          ("vf-failure", 8),
          ("ringing-failure", 9),
          ("invalid-state-to-init-diags", 10),
          ("line-is-unprovisioned", 11),
          ("diagnostics-results-pending", 12))
    )


_PpSurvPortLcDiagLastResult_Type.__name__ = "Integer32"
_PpSurvPortLcDiagLastResult_Object = MibTableColumn
ppSurvPortLcDiagLastResult = _PpSurvPortLcDiagLastResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 1, 1, 6),
    _PpSurvPortLcDiagLastResult_Type()
)
ppSurvPortLcDiagLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvPortLcDiagLastResult.setStatus("current")
_PpSurvMtaCodecCapTable_Object = MibTable
ppSurvMtaCodecCapTable = _PpSurvMtaCodecCapTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 2)
)
if mibBuilder.loadTexts:
    ppSurvMtaCodecCapTable.setStatus("obsolete")
_PpSurvMtaCodecCapEntry_Object = MibTableRow
ppSurvMtaCodecCapEntry = _PpSurvMtaCodecCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 2, 1)
)
ppSurvMtaCodecCapEntry.setIndexNames(
    (0, "PACKETPORT-MIB", "ppSurvMtaCodecCapIndex"),
)
if mibBuilder.loadTexts:
    ppSurvMtaCodecCapEntry.setStatus("obsolete")
_PpSurvMtaCodecCapIndex_Type = Integer32
_PpSurvMtaCodecCapIndex_Object = MibTableColumn
ppSurvMtaCodecCapIndex = _PpSurvMtaCodecCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 2, 1, 1),
    _PpSurvMtaCodecCapIndex_Type()
)
ppSurvMtaCodecCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppSurvMtaCodecCapIndex.setStatus("obsolete")
_PpSurvMtaCodecCapType_Type = CodecType
_PpSurvMtaCodecCapType_Object = MibTableColumn
ppSurvMtaCodecCapType = _PpSurvMtaCodecCapType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 2, 1, 2),
    _PpSurvMtaCodecCapType_Type()
)
ppSurvMtaCodecCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaCodecCapType.setStatus("obsolete")
_PpSurvMtaSigCapTable_Object = MibTable
ppSurvMtaSigCapTable = _PpSurvMtaSigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 3)
)
if mibBuilder.loadTexts:
    ppSurvMtaSigCapTable.setStatus("obsolete")
_PpSurvMtaSigCapEntry_Object = MibTableRow
ppSurvMtaSigCapEntry = _PpSurvMtaSigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 3, 1)
)
ppSurvMtaSigCapEntry.setIndexNames(
    (0, "PACKETPORT-MIB", "ppSurvMtaSigCapIndex"),
)
if mibBuilder.loadTexts:
    ppSurvMtaSigCapEntry.setStatus("obsolete")
_PpSurvMtaSigCapIndex_Type = Integer32
_PpSurvMtaSigCapIndex_Object = MibTableColumn
ppSurvMtaSigCapIndex = _PpSurvMtaSigCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 3, 1, 1),
    _PpSurvMtaSigCapIndex_Type()
)
ppSurvMtaSigCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppSurvMtaSigCapIndex.setStatus("obsolete")
_PpSurvMtaSigCapProtocol_Type = SignalingProtocol
_PpSurvMtaSigCapProtocol_Object = MibTableColumn
ppSurvMtaSigCapProtocol = _PpSurvMtaSigCapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 3, 1, 2),
    _PpSurvMtaSigCapProtocol_Type()
)
ppSurvMtaSigCapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaSigCapProtocol.setStatus("obsolete")
_PpSurvMtaNumberPorts_Type = Integer32
_PpSurvMtaNumberPorts_Object = MibScalar
ppSurvMtaNumberPorts = _PpSurvMtaNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 4),
    _PpSurvMtaNumberPorts_Type()
)
ppSurvMtaNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaNumberPorts.setStatus("current")


class _PpSurvMtaActiveSwBank_Type(Integer32):
    """Custom type ppSurvMtaActiveSwBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_PpSurvMtaActiveSwBank_Type.__name__ = "Integer32"
_PpSurvMtaActiveSwBank_Object = MibScalar
ppSurvMtaActiveSwBank = _PpSurvMtaActiveSwBank_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 5),
    _PpSurvMtaActiveSwBank_Type()
)
ppSurvMtaActiveSwBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaActiveSwBank.setStatus("obsolete")


class _PpSurvMtaPowerSupplyTele_Type(Integer32):
    """Custom type ppSurvMtaPowerSupplyTele based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("tlm-unavailable", 0),
          ("tlm-invalid", 1),
          ("tlm-shutdown-warning", 2),
          ("tlm-batt-reversed-shorted", 3),
          ("tlm-batt-low-replace-ac-fail", 4),
          ("tlm-batt-low-replace", 5),
          ("tlm-batt-low-ac-fail", 6),
          ("tlm-batt-low", 7),
          ("tlm-batt-missing", 8),
          ("tlm-ac-fail-batt-replace", 9),
          ("tlm-replace-batt", 10),
          ("tlm-ac-fail", 11),
          ("tlm-normal", 12),
          ("testInProgress", 13))
    )


_PpSurvMtaPowerSupplyTele_Type.__name__ = "Integer32"
_PpSurvMtaPowerSupplyTele_Object = MibScalar
ppSurvMtaPowerSupplyTele = _PpSurvMtaPowerSupplyTele_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 6),
    _PpSurvMtaPowerSupplyTele_Type()
)
ppSurvMtaPowerSupplyTele.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaPowerSupplyTele.setStatus("current")


class _PpSurvMtaSoftwareLoadBankA_Type(DisplayString):
    """Custom type ppSurvMtaSoftwareLoadBankA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PpSurvMtaSoftwareLoadBankA_Type.__name__ = "DisplayString"
_PpSurvMtaSoftwareLoadBankA_Object = MibScalar
ppSurvMtaSoftwareLoadBankA = _PpSurvMtaSoftwareLoadBankA_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 7),
    _PpSurvMtaSoftwareLoadBankA_Type()
)
ppSurvMtaSoftwareLoadBankA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaSoftwareLoadBankA.setStatus("obsolete")


class _PpSurvMtaSoftwareLoadBankB_Type(DisplayString):
    """Custom type ppSurvMtaSoftwareLoadBankB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PpSurvMtaSoftwareLoadBankB_Type.__name__ = "DisplayString"
_PpSurvMtaSoftwareLoadBankB_Object = MibScalar
ppSurvMtaSoftwareLoadBankB = _PpSurvMtaSoftwareLoadBankB_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 8),
    _PpSurvMtaSoftwareLoadBankB_Type()
)
ppSurvMtaSoftwareLoadBankB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaSoftwareLoadBankB.setStatus("obsolete")


class _PpSurvMtaPeccode_Type(DisplayString):
    """Custom type ppSurvMtaPeccode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PpSurvMtaPeccode_Type.__name__ = "DisplayString"
_PpSurvMtaPeccode_Object = MibScalar
ppSurvMtaPeccode = _PpSurvMtaPeccode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 9),
    _PpSurvMtaPeccode_Type()
)
ppSurvMtaPeccode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaPeccode.setStatus("obsolete")


class _PpSurvMtaMaintState_Type(Integer32):
    """Custom type ppSurvMtaMaintState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isnr", 1),
          ("istrbl", 2),
          ("oos", 3))
    )


_PpSurvMtaMaintState_Type.__name__ = "Integer32"
_PpSurvMtaMaintState_Object = MibScalar
ppSurvMtaMaintState = _PpSurvMtaMaintState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 10),
    _PpSurvMtaMaintState_Type()
)
ppSurvMtaMaintState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaMaintState.setStatus("current")
_PpSurvMtaDeviceIdentifier_Type = DisplayString
_PpSurvMtaDeviceIdentifier_Object = MibScalar
ppSurvMtaDeviceIdentifier = _PpSurvMtaDeviceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 11),
    _PpSurvMtaDeviceIdentifier_Type()
)
ppSurvMtaDeviceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaDeviceIdentifier.setStatus("current")
_PpSurvMtaInitialProvAck_Type = TruthValue
_PpSurvMtaInitialProvAck_Object = MibScalar
ppSurvMtaInitialProvAck = _PpSurvMtaInitialProvAck_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 12),
    _PpSurvMtaInitialProvAck_Type()
)
ppSurvMtaInitialProvAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaInitialProvAck.setStatus("obsolete")


class _PpSurvMtaCurrSwFilename_Type(DisplayString):
    """Custom type ppSurvMtaCurrSwFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PpSurvMtaCurrSwFilename_Type.__name__ = "DisplayString"
_PpSurvMtaCurrSwFilename_Object = MibScalar
ppSurvMtaCurrSwFilename = _PpSurvMtaCurrSwFilename_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 13),
    _PpSurvMtaCurrSwFilename_Type()
)
ppSurvMtaCurrSwFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaCurrSwFilename.setStatus("current")
_PpSurvMtaProvStatusAck_Type = TruthValue
_PpSurvMtaProvStatusAck_Object = MibScalar
ppSurvMtaProvStatusAck = _PpSurvMtaProvStatusAck_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 14),
    _PpSurvMtaProvStatusAck_Type()
)
ppSurvMtaProvStatusAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaProvStatusAck.setStatus("obsolete")


class _PpSurvMtaProvState_Type(Integer32):
    """Custom type ppSurvMtaProvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("inProgress", 2),
          ("fail", 3))
    )


_PpSurvMtaProvState_Type.__name__ = "Integer32"
_PpSurvMtaProvState_Object = MibScalar
ppSurvMtaProvState = _PpSurvMtaProvState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 15),
    _PpSurvMtaProvState_Type()
)
ppSurvMtaProvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaProvState.setStatus("obsolete")
_PpSurvMtaDevCorrelationId_Type = Integer32
_PpSurvMtaDevCorrelationId_Object = MibScalar
ppSurvMtaDevCorrelationId = _PpSurvMtaDevCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 16),
    _PpSurvMtaDevCorrelationId_Type()
)
ppSurvMtaDevCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaDevCorrelationId.setStatus("obsolete")
_PpSurvMtaBoxIdentifier_Type = Integer32
_PpSurvMtaBoxIdentifier_Object = MibScalar
ppSurvMtaBoxIdentifier = _PpSurvMtaBoxIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 17),
    _PpSurvMtaBoxIdentifier_Type()
)
ppSurvMtaBoxIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppSurvMtaBoxIdentifier.setStatus("current")
_PpSurvMtaDevDebug_ObjectIdentity = ObjectIdentity
ppSurvMtaDevDebug = _PpSurvMtaDevDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 18)
)
_PpSurvMtaDevDebugLevelControlTable_Object = MibTable
ppSurvMtaDevDebugLevelControlTable = _PpSurvMtaDevDebugLevelControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 18, 1)
)
if mibBuilder.loadTexts:
    ppSurvMtaDevDebugLevelControlTable.setStatus("current")
_PpSurvMtaDevDebugLevelControlEntry_Object = MibTableRow
ppSurvMtaDevDebugLevelControlEntry = _PpSurvMtaDevDebugLevelControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 18, 1, 1)
)
ppSurvMtaDevDebugLevelControlEntry.setIndexNames(
    (0, "PACKETPORT-MIB", "ppSurvMtaDevDebugModule"),
)
if mibBuilder.loadTexts:
    ppSurvMtaDevDebugLevelControlEntry.setStatus("current")


class _PpSurvMtaDevDebugModule_Type(Integer32):
    """Custom type ppSurvMtaDevDebugModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("generic", 1),
          ("callP", 2),
          ("dsp", 3),
          ("lineCard", 4),
          ("ppMtc", 5),
          ("rtp", 6))
    )


_PpSurvMtaDevDebugModule_Type.__name__ = "Integer32"
_PpSurvMtaDevDebugModule_Object = MibTableColumn
ppSurvMtaDevDebugModule = _PpSurvMtaDevDebugModule_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 18, 1, 1, 1),
    _PpSurvMtaDevDebugModule_Type()
)
ppSurvMtaDevDebugModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppSurvMtaDevDebugModule.setStatus("current")
_PpSurvMtaDevDebugReportingLevel_Type = PpDebugReportingLevel
_PpSurvMtaDevDebugReportingLevel_Object = MibTableColumn
ppSurvMtaDevDebugReportingLevel = _PpSurvMtaDevDebugReportingLevel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 18, 1, 1, 2),
    _PpSurvMtaDevDebugReportingLevel_Type()
)
ppSurvMtaDevDebugReportingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppSurvMtaDevDebugReportingLevel.setStatus("current")
_PpSurvMtaDevAlarms_ObjectIdentity = ObjectIdentity
ppSurvMtaDevAlarms = _PpSurvMtaDevAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 19)
)


class _PpSurvMtaDevAlarmRetryTimer_Type(Integer32):
    """Custom type ppSurvMtaDevAlarmRetryTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30)
        )
    )
    namedValues = NamedValues(
        *(("noRetry", 0),
          ("thirty", 30))
    )


_PpSurvMtaDevAlarmRetryTimer_Type.__name__ = "Integer32"
_PpSurvMtaDevAlarmRetryTimer_Object = MibScalar
ppSurvMtaDevAlarmRetryTimer = _PpSurvMtaDevAlarmRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 10, 2, 19, 1),
    _PpSurvMtaDevAlarmRetryTimer_Type()
)
ppSurvMtaDevAlarmRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppSurvMtaDevAlarmRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    ppSurvMtaDevAlarmRetryTimer.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETPORT-MIB",
    **{"DocsX509ASN1DEREncodedCertificate": DocsX509ASN1DEREncodedCertificate,
       "CodecType": CodecType,
       "PacketizationPeriodType": PacketizationPeriodType,
       "SignalingProtocol": SignalingProtocol,
       "CountryCode": CountryCode,
       "PpDebugReportingLevel": PpDebugReportingLevel,
       "PpCallServerType": PpCallServerType,
       "packetPortMib": packetPortMib,
       "ppConfiguration": ppConfiguration,
       "ppCfgPortTable": ppCfgPortTable,
       "ppCfgPortEntry": ppCfgPortEntry,
       "ppCfgPortPortNumber": ppCfgPortPortNumber,
       "ppCfgPortAdminState": ppCfgPortAdminState,
       "ppCfgPortCallAgentName": ppCfgPortCallAgentName,
       "ppCfgPortCallAgentIpAddress": ppCfgPortCallAgentIpAddress,
       "ppCfgPortProvSignalingProt": ppCfgPortProvSignalingProt,
       "ppCfgPortLoopCurrent": ppCfgPortLoopCurrent,
       "ppCfgPortTpar": ppCfgPortTpar,
       "ppCfgPortTcrit": ppCfgPortTcrit,
       "ppCfgPortBusyToneTimeOut": ppCfgPortBusyToneTimeOut,
       "ppCfgPortDialToneTimeOut": ppCfgPortDialToneTimeOut,
       "ppCfgPortMsgWaitTimeOut": ppCfgPortMsgWaitTimeOut,
       "ppCfgPortOffHookWarnTimeOut": ppCfgPortOffHookWarnTimeOut,
       "ppCfgPortRingingTimeOut": ppCfgPortRingingTimeOut,
       "ppCfgPortRingBackTimeOut": ppCfgPortRingBackTimeOut,
       "ppCfgPortReorderTimeOut": ppCfgPortReorderTimeOut,
       "ppCfgPortStutterDialToneTimeOut": ppCfgPortStutterDialToneTimeOut,
       "ppCfgPortMaxWaitDelay": ppCfgPortMaxWaitDelay,
       "ppCfgPortCallAgentUdpPort": ppCfgPortCallAgentUdpPort,
       "ppCfgPortTxGainControl": ppCfgPortTxGainControl,
       "ppCfgPortRxGainControl": ppCfgPortRxGainControl,
       "ppCfgPortLocUserIndication": ppCfgPortLocUserIndication,
       "ppCfgPortPacketizationPeriod": ppCfgPortPacketizationPeriod,
       "ppCfgPortCodec": ppCfgPortCodec,
       "ppCfgPortDialingMethod": ppCfgPortDialingMethod,
       "ppCfgPortT38MaxDatagram": ppCfgPortT38MaxDatagram,
       "ppCfgMtaAdminState": ppCfgMtaAdminState,
       "ppCfgMtaTeleSyslogServIpAddr": ppCfgMtaTeleSyslogServIpAddr,
       "ppCfgMtaTeleSyslogServName": ppCfgMtaTeleSyslogServName,
       "ppCfgMtaTeleFullyQualName": ppCfgMtaTeleFullyQualName,
       "ppCfgMtaTeleServProvServIpAddr": ppCfgMtaTeleServProvServIpAddr,
       "ppCfgMtaTeleServProvServName": ppCfgMtaTeleServProvServName,
       "ppCfgMtaTeleServProvDhcpIpAddr": ppCfgMtaTeleServProvDhcpIpAddr,
       "ppCfgMtaTeleServProvDhcpName": ppCfgMtaTeleServProvDhcpName,
       "ppCfgMtaPrimTeleNetDnsAddr": ppCfgMtaPrimTeleNetDnsAddr,
       "ppCfgMtaSecTeleNetDnsAddr": ppCfgMtaSecTeleNetDnsAddr,
       "ppCfgMtaCableTvEnable": ppCfgMtaCableTvEnable,
       "ppCfgMtaConfigFileAccName": ppCfgMtaConfigFileAccName,
       "ppCfgMtaCountryTemplate": ppCfgMtaCountryTemplate,
       "ppCfgMtaProvMethodIndicator": ppCfgMtaProvMethodIndicator,
       "ppCfgMtaTeleConfigServerIpAddr": ppCfgMtaTeleConfigServerIpAddr,
       "ppCfgMtaTeleConfigServerName": ppCfgMtaTeleConfigServerName,
       "ppCfgMtaNcsCallSigTos": ppCfgMtaNcsCallSigTos,
       "ppCfgMtaDataInterface": ppCfgMtaDataInterface,
       "ppCfgMtaCallpFeatureSwitch": ppCfgMtaCallpFeatureSwitch,
       "ppCfgMtaCallServerType": ppCfgMtaCallServerType,
       "ppCfgMtaInternetIsolationState": ppCfgMtaInternetIsolationState,
       "ppCfgRfc2833DigitPayloadType": ppCfgRfc2833DigitPayloadType,
       "ppCfgMtaFeatureSwitch": ppCfgMtaFeatureSwitch,
       "ppCfgMtaBatteryReplaceReporting": ppCfgMtaBatteryReplaceReporting,
       "ppCfgNsePayloadType": ppCfgNsePayloadType,
       "ppCfgMtaCallpFeatureSwitch2": ppCfgMtaCallpFeatureSwitch2,
       "ppCfgMtaDevSecurity": ppCfgMtaDevSecurity,
       "ppCfgMtaDevServiceProviderTestRootCert": ppCfgMtaDevServiceProviderTestRootCert,
       "ppCfgMtaDevSPTestRootCertServer": ppCfgMtaDevSPTestRootCertServer,
       "ppCfgMtaDevSPTestRootCertFilename": ppCfgMtaDevSPTestRootCertFilename,
       "ppCfgMtaDevSPTestRootCertAdminStatus": ppCfgMtaDevSPTestRootCertAdminStatus,
       "ppCfgMtaDevSPTestRootCertDownloadState": ppCfgMtaDevSPTestRootCertDownloadState,
       "ppCfgDevHttp": ppCfgDevHttp,
       "ppCfgMtaLanHttpAccess": ppCfgMtaLanHttpAccess,
       "ppCfgMtaWanHttpAccess": ppCfgMtaWanHttpAccess,
       "ppCfgMtaClientSeed": ppCfgMtaClientSeed,
       "ppCfgMtaHTTPAdvLink": ppCfgMtaHTTPAdvLink,
       "ppSurveillance": ppSurveillance,
       "ppSurvPortTable": ppSurvPortTable,
       "ppSurvPortEntry": ppSurvPortEntry,
       "ppSurvPortNumber": ppSurvPortNumber,
       "ppSurvPortMaintState": ppSurvPortMaintState,
       "ppSurvPortDigitMap": ppSurvPortDigitMap,
       "ppSurvPortLcDiagRequest": ppSurvPortLcDiagRequest,
       "ppSurvPortDeprovRequest": ppSurvPortDeprovRequest,
       "ppSurvPortLcDiagLastResult": ppSurvPortLcDiagLastResult,
       "ppSurvMtaCodecCapTable": ppSurvMtaCodecCapTable,
       "ppSurvMtaCodecCapEntry": ppSurvMtaCodecCapEntry,
       "ppSurvMtaCodecCapIndex": ppSurvMtaCodecCapIndex,
       "ppSurvMtaCodecCapType": ppSurvMtaCodecCapType,
       "ppSurvMtaSigCapTable": ppSurvMtaSigCapTable,
       "ppSurvMtaSigCapEntry": ppSurvMtaSigCapEntry,
       "ppSurvMtaSigCapIndex": ppSurvMtaSigCapIndex,
       "ppSurvMtaSigCapProtocol": ppSurvMtaSigCapProtocol,
       "ppSurvMtaNumberPorts": ppSurvMtaNumberPorts,
       "ppSurvMtaActiveSwBank": ppSurvMtaActiveSwBank,
       "ppSurvMtaPowerSupplyTele": ppSurvMtaPowerSupplyTele,
       "ppSurvMtaSoftwareLoadBankA": ppSurvMtaSoftwareLoadBankA,
       "ppSurvMtaSoftwareLoadBankB": ppSurvMtaSoftwareLoadBankB,
       "ppSurvMtaPeccode": ppSurvMtaPeccode,
       "ppSurvMtaMaintState": ppSurvMtaMaintState,
       "ppSurvMtaDeviceIdentifier": ppSurvMtaDeviceIdentifier,
       "ppSurvMtaInitialProvAck": ppSurvMtaInitialProvAck,
       "ppSurvMtaCurrSwFilename": ppSurvMtaCurrSwFilename,
       "ppSurvMtaProvStatusAck": ppSurvMtaProvStatusAck,
       "ppSurvMtaProvState": ppSurvMtaProvState,
       "ppSurvMtaDevCorrelationId": ppSurvMtaDevCorrelationId,
       "ppSurvMtaBoxIdentifier": ppSurvMtaBoxIdentifier,
       "ppSurvMtaDevDebug": ppSurvMtaDevDebug,
       "ppSurvMtaDevDebugLevelControlTable": ppSurvMtaDevDebugLevelControlTable,
       "ppSurvMtaDevDebugLevelControlEntry": ppSurvMtaDevDebugLevelControlEntry,
       "ppSurvMtaDevDebugModule": ppSurvMtaDevDebugModule,
       "ppSurvMtaDevDebugReportingLevel": ppSurvMtaDevDebugReportingLevel,
       "ppSurvMtaDevAlarms": ppSurvMtaDevAlarms,
       "ppSurvMtaDevAlarmRetryTimer": ppSurvMtaDevAlarmRetryTimer}
)
