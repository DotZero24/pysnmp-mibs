# SNMP MIB module (G6-MISC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-MISC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:05 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78)
)
_TerminalServerConfigTable_Object = MibTable
terminalServerConfigTable = _TerminalServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1)
)
if mibBuilder.loadTexts:
    terminalServerConfigTable.setStatus("current")
_TerminalServerConfigEntry_Object = MibTableRow
terminalServerConfigEntry = _TerminalServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1)
)
terminalServerConfigEntry.setIndexNames(
    (0, "G6-MISC-MIB", "terminalServerConfigIndex"),
)
if mibBuilder.loadTexts:
    terminalServerConfigEntry.setStatus("current")


class _TerminalServerConfigIndex_Type(Integer32):
    """Custom type terminalServerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_TerminalServerConfigIndex_Type.__name__ = "Integer32"
_TerminalServerConfigIndex_Object = MibTableColumn
terminalServerConfigIndex = _TerminalServerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 1),
    _TerminalServerConfigIndex_Type()
)
terminalServerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    terminalServerConfigIndex.setStatus("current")
_TerminalServerConfigDeviceName_Type = DisplayString
_TerminalServerConfigDeviceName_Object = MibTableColumn
terminalServerConfigDeviceName = _TerminalServerConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 2),
    _TerminalServerConfigDeviceName_Type()
)
terminalServerConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigDeviceName.setStatus("current")


class _TerminalServerConfigMode_Type(Integer32):
    """Custom type terminalServerConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 0),
          ("client", 1),
          ("comPort", 2))
    )


_TerminalServerConfigMode_Type.__name__ = "Integer32"
_TerminalServerConfigMode_Object = MibTableColumn
terminalServerConfigMode = _TerminalServerConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 3),
    _TerminalServerConfigMode_Type()
)
terminalServerConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigMode.setStatus("current")


class _TerminalServerConfigRemoteIp_Type(OctetString):
    """Custom type terminalServerConfigRemoteIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TerminalServerConfigRemoteIp_Type.__name__ = "OctetString"
_TerminalServerConfigRemoteIp_Object = MibTableColumn
terminalServerConfigRemoteIp = _TerminalServerConfigRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 4),
    _TerminalServerConfigRemoteIp_Type()
)
terminalServerConfigRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigRemoteIp.setStatus("current")


class _TerminalServerConfigTcpPort_Type(Integer32):
    """Custom type terminalServerConfigTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TerminalServerConfigTcpPort_Type.__name__ = "Integer32"
_TerminalServerConfigTcpPort_Object = MibTableColumn
terminalServerConfigTcpPort = _TerminalServerConfigTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 5),
    _TerminalServerConfigTcpPort_Type()
)
terminalServerConfigTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigTcpPort.setStatus("current")


class _TerminalServerConfigInactivityTimeout_Type(Integer32):
    """Custom type terminalServerConfigInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TerminalServerConfigInactivityTimeout_Type.__name__ = "Integer32"
_TerminalServerConfigInactivityTimeout_Object = MibTableColumn
terminalServerConfigInactivityTimeout = _TerminalServerConfigInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 6),
    _TerminalServerConfigInactivityTimeout_Type()
)
terminalServerConfigInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigInactivityTimeout.setStatus("current")


class _TerminalServerConfigDataRate_Type(Integer32):
    """Custom type terminalServerConfigDataRate based on Integer32"""
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
        *(("ms300", 0),
          ("ms600", 1),
          ("ms1200", 2),
          ("ms2400", 3),
          ("ms4800", 4),
          ("ms9600", 5),
          ("ms19200", 6),
          ("ms38400", 7),
          ("ms57600", 8),
          ("ms115200", 9),
          ("ms230400", 10))
    )


_TerminalServerConfigDataRate_Type.__name__ = "Integer32"
_TerminalServerConfigDataRate_Object = MibTableColumn
terminalServerConfigDataRate = _TerminalServerConfigDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 7),
    _TerminalServerConfigDataRate_Type()
)
terminalServerConfigDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigDataRate.setStatus("current")


class _TerminalServerConfigDatabits_Type(Integer32):
    """Custom type terminalServerConfigDatabits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ms7Bit", 0),
          ("ms8Bit", 1))
    )


_TerminalServerConfigDatabits_Type.__name__ = "Integer32"
_TerminalServerConfigDatabits_Object = MibTableColumn
terminalServerConfigDatabits = _TerminalServerConfigDatabits_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 8),
    _TerminalServerConfigDatabits_Type()
)
terminalServerConfigDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigDatabits.setStatus("current")


class _TerminalServerConfigParity_Type(Integer32):
    """Custom type terminalServerConfigParity based on Integer32"""
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
        *(("none", 0),
          ("odd", 1),
          ("even", 2),
          ("mark", 3),
          ("space", 4))
    )


_TerminalServerConfigParity_Type.__name__ = "Integer32"
_TerminalServerConfigParity_Object = MibTableColumn
terminalServerConfigParity = _TerminalServerConfigParity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 9),
    _TerminalServerConfigParity_Type()
)
terminalServerConfigParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigParity.setStatus("current")


class _TerminalServerConfigStopBits_Type(Integer32):
    """Custom type terminalServerConfigStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ms1Bit", 0),
          ("ms2Bits", 1))
    )


_TerminalServerConfigStopBits_Type.__name__ = "Integer32"
_TerminalServerConfigStopBits_Object = MibTableColumn
terminalServerConfigStopBits = _TerminalServerConfigStopBits_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 10),
    _TerminalServerConfigStopBits_Type()
)
terminalServerConfigStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigStopBits.setStatus("current")


class _TerminalServerConfigFlowControl_Type(Integer32):
    """Custom type terminalServerConfigFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("localXonXoff", 1),
          ("passXonXoff", 2))
    )


_TerminalServerConfigFlowControl_Type.__name__ = "Integer32"
_TerminalServerConfigFlowControl_Object = MibTableColumn
terminalServerConfigFlowControl = _TerminalServerConfigFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 11),
    _TerminalServerConfigFlowControl_Type()
)
terminalServerConfigFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigFlowControl.setStatus("current")


class _TerminalServerConfigForwardingTimer_Type(Integer32):
    """Custom type terminalServerConfigForwardingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TerminalServerConfigForwardingTimer_Type.__name__ = "Integer32"
_TerminalServerConfigForwardingTimer_Object = MibTableColumn
terminalServerConfigForwardingTimer = _TerminalServerConfigForwardingTimer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 12),
    _TerminalServerConfigForwardingTimer_Type()
)
terminalServerConfigForwardingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigForwardingTimer.setStatus("current")


class _TerminalServerConfigCharacterCount_Type(Integer32):
    """Custom type terminalServerConfigCharacterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TerminalServerConfigCharacterCount_Type.__name__ = "Integer32"
_TerminalServerConfigCharacterCount_Object = MibTableColumn
terminalServerConfigCharacterCount = _TerminalServerConfigCharacterCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 13),
    _TerminalServerConfigCharacterCount_Type()
)
terminalServerConfigCharacterCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigCharacterCount.setStatus("current")


class _TerminalServerConfigForwardingCharacter_Type(Integer32):
    """Custom type terminalServerConfigForwardingCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cr", 1),
          ("lf", 2))
    )


_TerminalServerConfigForwardingCharacter_Type.__name__ = "Integer32"
_TerminalServerConfigForwardingCharacter_Object = MibTableColumn
terminalServerConfigForwardingCharacter = _TerminalServerConfigForwardingCharacter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 1, 1, 14),
    _TerminalServerConfigForwardingCharacter_Type()
)
terminalServerConfigForwardingCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalServerConfigForwardingCharacter.setStatus("current")
_SpeakerConfigTable_Object = MibTable
speakerConfigTable = _SpeakerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2)
)
if mibBuilder.loadTexts:
    speakerConfigTable.setStatus("current")
_SpeakerConfigEntry_Object = MibTableRow
speakerConfigEntry = _SpeakerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1)
)
speakerConfigEntry.setIndexNames(
    (0, "G6-MISC-MIB", "speakerConfigIndex"),
)
if mibBuilder.loadTexts:
    speakerConfigEntry.setStatus("current")


class _SpeakerConfigIndex_Type(Integer32):
    """Custom type speakerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SpeakerConfigIndex_Type.__name__ = "Integer32"
_SpeakerConfigIndex_Object = MibTableColumn
speakerConfigIndex = _SpeakerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 1),
    _SpeakerConfigIndex_Type()
)
speakerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speakerConfigIndex.setStatus("current")
_SpeakerConfigPlay_Type = DisplayString
_SpeakerConfigPlay_Object = MibTableColumn
speakerConfigPlay = _SpeakerConfigPlay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 2),
    _SpeakerConfigPlay_Type()
)
speakerConfigPlay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigPlay.setStatus("current")
_SpeakerConfigStop_Type = DisplayString
_SpeakerConfigStop_Object = MibTableColumn
speakerConfigStop = _SpeakerConfigStop_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 3),
    _SpeakerConfigStop_Type()
)
speakerConfigStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigStop.setStatus("current")
_SpeakerConfigVolume_Type = DisplayString
_SpeakerConfigVolume_Object = MibTableColumn
speakerConfigVolume = _SpeakerConfigVolume_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 4),
    _SpeakerConfigVolume_Type()
)
speakerConfigVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigVolume.setStatus("current")
_SpeakerConfigDeviceName_Type = DisplayString
_SpeakerConfigDeviceName_Object = MibTableColumn
speakerConfigDeviceName = _SpeakerConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 5),
    _SpeakerConfigDeviceName_Type()
)
speakerConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigDeviceName.setStatus("current")


class _SpeakerConfigDeviceType_Type(Integer32):
    """Custom type speakerConfigDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("genericRtp", 0),
          ("smartaudioController", 1))
    )


_SpeakerConfigDeviceType_Type.__name__ = "Integer32"
_SpeakerConfigDeviceType_Object = MibTableColumn
speakerConfigDeviceType = _SpeakerConfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 6),
    _SpeakerConfigDeviceType_Type()
)
speakerConfigDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigDeviceType.setStatus("current")
_SpeakerConfigOutputRate_Type = Unsigned32
_SpeakerConfigOutputRate_Object = MibTableColumn
speakerConfigOutputRate = _SpeakerConfigOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 7),
    _SpeakerConfigOutputRate_Type()
)
speakerConfigOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigOutputRate.setStatus("current")


class _SpeakerConfigOutputFormat_Type(Integer32):
    """Custom type speakerConfigOutputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mono", 0),
          ("stereo", 1))
    )


_SpeakerConfigOutputFormat_Type.__name__ = "Integer32"
_SpeakerConfigOutputFormat_Object = MibTableColumn
speakerConfigOutputFormat = _SpeakerConfigOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 8),
    _SpeakerConfigOutputFormat_Type()
)
speakerConfigOutputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigOutputFormat.setStatus("current")
_SpeakerConfigHostAddress_Type = DisplayString
_SpeakerConfigHostAddress_Object = MibTableColumn
speakerConfigHostAddress = _SpeakerConfigHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 9),
    _SpeakerConfigHostAddress_Type()
)
speakerConfigHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigHostAddress.setStatus("current")


class _SpeakerConfigUdpPort_Type(Integer32):
    """Custom type speakerConfigUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpeakerConfigUdpPort_Type.__name__ = "Integer32"
_SpeakerConfigUdpPort_Object = MibTableColumn
speakerConfigUdpPort = _SpeakerConfigUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 78, 2, 1, 10),
    _SpeakerConfigUdpPort_Type()
)
speakerConfigUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speakerConfigUdpPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-MISC-MIB",
    **{"management": management,
       "misc": misc,
       "terminalServerConfigTable": terminalServerConfigTable,
       "terminalServerConfigEntry": terminalServerConfigEntry,
       "terminalServerConfigIndex": terminalServerConfigIndex,
       "terminalServerConfigDeviceName": terminalServerConfigDeviceName,
       "terminalServerConfigMode": terminalServerConfigMode,
       "terminalServerConfigRemoteIp": terminalServerConfigRemoteIp,
       "terminalServerConfigTcpPort": terminalServerConfigTcpPort,
       "terminalServerConfigInactivityTimeout": terminalServerConfigInactivityTimeout,
       "terminalServerConfigDataRate": terminalServerConfigDataRate,
       "terminalServerConfigDatabits": terminalServerConfigDatabits,
       "terminalServerConfigParity": terminalServerConfigParity,
       "terminalServerConfigStopBits": terminalServerConfigStopBits,
       "terminalServerConfigFlowControl": terminalServerConfigFlowControl,
       "terminalServerConfigForwardingTimer": terminalServerConfigForwardingTimer,
       "terminalServerConfigCharacterCount": terminalServerConfigCharacterCount,
       "terminalServerConfigForwardingCharacter": terminalServerConfigForwardingCharacter,
       "speakerConfigTable": speakerConfigTable,
       "speakerConfigEntry": speakerConfigEntry,
       "speakerConfigIndex": speakerConfigIndex,
       "speakerConfigPlay": speakerConfigPlay,
       "speakerConfigStop": speakerConfigStop,
       "speakerConfigVolume": speakerConfigVolume,
       "speakerConfigDeviceName": speakerConfigDeviceName,
       "speakerConfigDeviceType": speakerConfigDeviceType,
       "speakerConfigOutputRate": speakerConfigOutputRate,
       "speakerConfigOutputFormat": speakerConfigOutputFormat,
       "speakerConfigHostAddress": speakerConfigHostAddress,
       "speakerConfigUdpPort": speakerConfigUdpPort}
)
