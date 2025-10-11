# SNMP MIB module (MX-EAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-EAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:35 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EamMIBObjects_ObjectIdentity = ObjectIdentity
eamMIBObjects = _EamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1)
)
_EamGroup_ObjectIdentity = ObjectIdentity
eamGroup = _EamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100)
)
_EamTable_Object = MibTable
eamTable = _EamTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100)
)
if mibBuilder.loadTexts:
    eamTable.setStatus("current")
_EamEntry_Object = MibTableRow
eamEntry = _EamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1)
)
eamEntry.setIndexNames(
    (0, "MX-EAM-MIB", "eamName"),
)
if mibBuilder.loadTexts:
    eamEntry.setStatus("current")
_EamName_Type = OctetString
_EamName_Object = MibTableColumn
eamName = _EamName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 100),
    _EamName_Type()
)
eamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eamName.setStatus("current")


class _EamChannelRange_Type(OctetString):
    """Custom type eamChannelRange based on OctetString"""
    defaultValue = OctetString("1-24")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_EamChannelRange_Type.__name__ = "OctetString"
_EamChannelRange_Object = MibTableColumn
eamChannelRange = _EamChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 200),
    _EamChannelRange_Type()
)
eamChannelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamChannelRange.setStatus("current")


class _EamChannelAllocationStrategy_Type(Integer32):
    """Custom type eamChannelAllocationStrategy based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 100),
          ("descending", 200),
          ("roundRobinAscending", 300),
          ("roundRobinDescending", 400))
    )


_EamChannelAllocationStrategy_Type.__name__ = "Integer32"
_EamChannelAllocationStrategy_Object = MibTableColumn
eamChannelAllocationStrategy = _EamChannelAllocationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 300),
    _EamChannelAllocationStrategy_Type()
)
eamChannelAllocationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamChannelAllocationStrategy.setStatus("current")


class _EamMaxActiveCalls_Type(Unsigned32):
    """Custom type eamMaxActiveCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_EamMaxActiveCalls_Type.__name__ = "Unsigned32"
_EamMaxActiveCalls_Object = MibTableColumn
eamMaxActiveCalls = _EamMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 400),
    _EamMaxActiveCalls_Type()
)
eamMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamMaxActiveCalls.setStatus("current")


class _EamEncodingScheme_Type(Integer32):
    """Custom type eamEncodingScheme based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 100),
          ("g711ulaw", 200))
    )


_EamEncodingScheme_Type.__name__ = "Integer32"
_EamEncodingScheme_Object = MibTableColumn
eamEncodingScheme = _EamEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 500),
    _EamEncodingScheme_Type()
)
eamEncodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamEncodingScheme.setStatus("current")


class _EamSignalingType_Type(Integer32):
    """Custom type eamSignalingType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("winkStart", 100),
          ("immediateStart", 200),
          ("fgb", 300),
          ("fgd", 400))
    )


_EamSignalingType_Type.__name__ = "Integer32"
_EamSignalingType_Object = MibTableColumn
eamSignalingType = _EamSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 600),
    _EamSignalingType_Type()
)
eamSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingType.setStatus("current")


class _EamDigitAttenuation_Type(Unsigned32):
    """Custom type eamDigitAttenuation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_EamDigitAttenuation_Type.__name__ = "Unsigned32"
_EamDigitAttenuation_Object = MibTableColumn
eamDigitAttenuation = _EamDigitAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 100, 1, 700),
    _EamDigitAttenuation_Type()
)
eamDigitAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamDigitAttenuation.setStatus("current")
_EamSignalingVariantsTable_Object = MibTable
eamSignalingVariantsTable = _EamSignalingVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200)
)
if mibBuilder.loadTexts:
    eamSignalingVariantsTable.setStatus("current")
_EamSignalingVariantsEntry_Object = MibTableRow
eamSignalingVariantsEntry = _EamSignalingVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1)
)
eamSignalingVariantsEntry.setIndexNames(
    (0, "MX-EAM-MIB", "eamSignalingVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    eamSignalingVariantsEntry.setStatus("current")
_EamSignalingVariantsInterfaceName_Type = OctetString
_EamSignalingVariantsInterfaceName_Object = MibTableColumn
eamSignalingVariantsInterfaceName = _EamSignalingVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 100),
    _EamSignalingVariantsInterfaceName_Type()
)
eamSignalingVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eamSignalingVariantsInterfaceName.setStatus("current")


class _EamSignalingVariantsOverrideDefault_Type(MxEnableState):
    """Custom type eamSignalingVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_EamSignalingVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_EamSignalingVariantsOverrideDefault_Object = MibTableColumn
eamSignalingVariantsOverrideDefault = _EamSignalingVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 200),
    _EamSignalingVariantsOverrideDefault_Type()
)
eamSignalingVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsOverrideDefault.setStatus("current")


class _EamSignalingVariantsBitsBCD_Type(Integer32):
    """Custom type eamSignalingVariantsBitsBCD based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_EamSignalingVariantsBitsBCD_Type.__name__ = "Integer32"
_EamSignalingVariantsBitsBCD_Object = MibTableColumn
eamSignalingVariantsBitsBCD = _EamSignalingVariantsBitsBCD_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 300),
    _EamSignalingVariantsBitsBCD_Type()
)
eamSignalingVariantsBitsBCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsBitsBCD.setStatus("current")


class _EamSignalingVariantsDnisLength_Type(Unsigned32):
    """Custom type eamSignalingVariantsDnisLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_EamSignalingVariantsDnisLength_Type.__name__ = "Unsigned32"
_EamSignalingVariantsDnisLength_Object = MibTableColumn
eamSignalingVariantsDnisLength = _EamSignalingVariantsDnisLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 400),
    _EamSignalingVariantsDnisLength_Type()
)
eamSignalingVariantsDnisLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsDnisLength.setStatus("current")


class _EamSignalingVariantsAniLength_Type(Unsigned32):
    """Custom type eamSignalingVariantsAniLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_EamSignalingVariantsAniLength_Type.__name__ = "Unsigned32"
_EamSignalingVariantsAniLength_Object = MibTableColumn
eamSignalingVariantsAniLength = _EamSignalingVariantsAniLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 500),
    _EamSignalingVariantsAniLength_Type()
)
eamSignalingVariantsAniLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsAniLength.setStatus("current")


class _EamSignalingVariantsIncomingRegisterSignaling_Type(Integer32):
    """Custom type eamSignalingVariantsIncomingRegisterSignaling based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mfR1", 100),
          ("dtmf", 200))
    )


_EamSignalingVariantsIncomingRegisterSignaling_Type.__name__ = "Integer32"
_EamSignalingVariantsIncomingRegisterSignaling_Object = MibTableColumn
eamSignalingVariantsIncomingRegisterSignaling = _EamSignalingVariantsIncomingRegisterSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 600),
    _EamSignalingVariantsIncomingRegisterSignaling_Type()
)
eamSignalingVariantsIncomingRegisterSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsIncomingRegisterSignaling.setStatus("current")


class _EamSignalingVariantsOutgoingRegisterSignaling_Type(Integer32):
    """Custom type eamSignalingVariantsOutgoingRegisterSignaling based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mfR1", 100),
          ("dtmf", 200))
    )


_EamSignalingVariantsOutgoingRegisterSignaling_Type.__name__ = "Integer32"
_EamSignalingVariantsOutgoingRegisterSignaling_Object = MibTableColumn
eamSignalingVariantsOutgoingRegisterSignaling = _EamSignalingVariantsOutgoingRegisterSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 700),
    _EamSignalingVariantsOutgoingRegisterSignaling_Type()
)
eamSignalingVariantsOutgoingRegisterSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsOutgoingRegisterSignaling.setStatus("current")


class _EamSignalingVariantsIncomingDialMap_Type(OctetString):
    """Custom type eamSignalingVariantsIncomingDialMap based on OctetString"""
    defaultValue = OctetString("%dnis%t")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EamSignalingVariantsIncomingDialMap_Type.__name__ = "OctetString"
_EamSignalingVariantsIncomingDialMap_Object = MibTableColumn
eamSignalingVariantsIncomingDialMap = _EamSignalingVariantsIncomingDialMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 800),
    _EamSignalingVariantsIncomingDialMap_Type()
)
eamSignalingVariantsIncomingDialMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsIncomingDialMap.setStatus("current")


class _EamSignalingVariantsOutgoingDialMap_Type(OctetString):
    """Custom type eamSignalingVariantsOutgoingDialMap based on OctetString"""
    defaultValue = OctetString("%dnis%t")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EamSignalingVariantsOutgoingDialMap_Type.__name__ = "OctetString"
_EamSignalingVariantsOutgoingDialMap_Object = MibTableColumn
eamSignalingVariantsOutgoingDialMap = _EamSignalingVariantsOutgoingDialMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 900),
    _EamSignalingVariantsOutgoingDialMap_Type()
)
eamSignalingVariantsOutgoingDialMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsOutgoingDialMap.setStatus("current")


class _EamSignalingVariantsWaitWink_Type(MxEnableState):
    """Custom type eamSignalingVariantsWaitWink based on MxEnableState"""
    defaultValue = 1


_EamSignalingVariantsWaitWink_Type.__name__ = "MxEnableState"
_EamSignalingVariantsWaitWink_Object = MibTableColumn
eamSignalingVariantsWaitWink = _EamSignalingVariantsWaitWink_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 1000),
    _EamSignalingVariantsWaitWink_Type()
)
eamSignalingVariantsWaitWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsWaitWink.setStatus("current")


class _EamSignalingVariantsWaitWinkAck_Type(MxEnableState):
    """Custom type eamSignalingVariantsWaitWinkAck based on MxEnableState"""
    defaultValue = 0


_EamSignalingVariantsWaitWinkAck_Type.__name__ = "MxEnableState"
_EamSignalingVariantsWaitWinkAck_Object = MibTableColumn
eamSignalingVariantsWaitWinkAck = _EamSignalingVariantsWaitWinkAck_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 1100),
    _EamSignalingVariantsWaitWinkAck_Type()
)
eamSignalingVariantsWaitWinkAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsWaitWinkAck.setStatus("current")


class _EamSignalingVariantsSendWink_Type(MxEnableState):
    """Custom type eamSignalingVariantsSendWink based on MxEnableState"""
    defaultValue = 1


_EamSignalingVariantsSendWink_Type.__name__ = "MxEnableState"
_EamSignalingVariantsSendWink_Object = MibTableColumn
eamSignalingVariantsSendWink = _EamSignalingVariantsSendWink_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 1200),
    _EamSignalingVariantsSendWink_Type()
)
eamSignalingVariantsSendWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsSendWink.setStatus("current")


class _EamSignalingVariantsSendWinkAck_Type(MxEnableState):
    """Custom type eamSignalingVariantsSendWinkAck based on MxEnableState"""
    defaultValue = 0


_EamSignalingVariantsSendWinkAck_Type.__name__ = "MxEnableState"
_EamSignalingVariantsSendWinkAck_Object = MibTableColumn
eamSignalingVariantsSendWinkAck = _EamSignalingVariantsSendWinkAck_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 1300),
    _EamSignalingVariantsSendWinkAck_Type()
)
eamSignalingVariantsSendWinkAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsSendWinkAck.setStatus("current")


class _EamSignalingVariantsResetSpecific_Type(Integer32):
    """Custom type eamSignalingVariantsResetSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("resetSpecific", 10))
    )


_EamSignalingVariantsResetSpecific_Type.__name__ = "Integer32"
_EamSignalingVariantsResetSpecific_Object = MibTableColumn
eamSignalingVariantsResetSpecific = _EamSignalingVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 200, 1, 2000),
    _EamSignalingVariantsResetSpecific_Type()
)
eamSignalingVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamSignalingVariantsResetSpecific.setStatus("current")
_EamTimerVariantsTable_Object = MibTable
eamTimerVariantsTable = _EamTimerVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300)
)
if mibBuilder.loadTexts:
    eamTimerVariantsTable.setStatus("current")
_EamTimerVariantsEntry_Object = MibTableRow
eamTimerVariantsEntry = _EamTimerVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1)
)
eamTimerVariantsEntry.setIndexNames(
    (0, "MX-EAM-MIB", "eamTimerVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    eamTimerVariantsEntry.setStatus("current")
_EamTimerVariantsInterfaceName_Type = OctetString
_EamTimerVariantsInterfaceName_Object = MibTableColumn
eamTimerVariantsInterfaceName = _EamTimerVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 100),
    _EamTimerVariantsInterfaceName_Type()
)
eamTimerVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eamTimerVariantsInterfaceName.setStatus("current")


class _EamTimerVariantsOverrideDefault_Type(MxEnableState):
    """Custom type eamTimerVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_EamTimerVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_EamTimerVariantsOverrideDefault_Object = MibTableColumn
eamTimerVariantsOverrideDefault = _EamTimerVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 200),
    _EamTimerVariantsOverrideDefault_Type()
)
eamTimerVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsOverrideDefault.setStatus("current")


class _EamTimerVariantsBwdWaitPreWinkTimeout_Type(Integer32):
    """Custom type eamTimerVariantsBwdWaitPreWinkTimeout based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_EamTimerVariantsBwdWaitPreWinkTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsBwdWaitPreWinkTimeout_Object = MibTableColumn
eamTimerVariantsBwdWaitPreWinkTimeout = _EamTimerVariantsBwdWaitPreWinkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 300),
    _EamTimerVariantsBwdWaitPreWinkTimeout_Type()
)
eamTimerVariantsBwdWaitPreWinkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsBwdWaitPreWinkTimeout.setStatus("current")


class _EamTimerVariantsBwdSendWinkTimeout_Type(Integer32):
    """Custom type eamTimerVariantsBwdSendWinkTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_EamTimerVariantsBwdSendWinkTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsBwdSendWinkTimeout_Object = MibTableColumn
eamTimerVariantsBwdSendWinkTimeout = _EamTimerVariantsBwdSendWinkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 400),
    _EamTimerVariantsBwdSendWinkTimeout_Type()
)
eamTimerVariantsBwdSendWinkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsBwdSendWinkTimeout.setStatus("current")


class _EamTimerVariantsBwdWait1stDigitTimeout_Type(Integer32):
    """Custom type eamTimerVariantsBwdWait1stDigitTimeout based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_EamTimerVariantsBwdWait1stDigitTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsBwdWait1stDigitTimeout_Object = MibTableColumn
eamTimerVariantsBwdWait1stDigitTimeout = _EamTimerVariantsBwdWait1stDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 500),
    _EamTimerVariantsBwdWait1stDigitTimeout_Type()
)
eamTimerVariantsBwdWait1stDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsBwdWait1stDigitTimeout.setStatus("current")


class _EamTimerVariantsBwdClearBackwardTimeout_Type(Integer32):
    """Custom type eamTimerVariantsBwdClearBackwardTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_EamTimerVariantsBwdClearBackwardTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsBwdClearBackwardTimeout_Object = MibTableColumn
eamTimerVariantsBwdClearBackwardTimeout = _EamTimerVariantsBwdClearBackwardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 600),
    _EamTimerVariantsBwdClearBackwardTimeout_Type()
)
eamTimerVariantsBwdClearBackwardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsBwdClearBackwardTimeout.setStatus("current")


class _EamTimerVariantsBwdDigitCompleteTimeout_Type(Integer32):
    """Custom type eamTimerVariantsBwdDigitCompleteTimeout based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_EamTimerVariantsBwdDigitCompleteTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsBwdDigitCompleteTimeout_Object = MibTableColumn
eamTimerVariantsBwdDigitCompleteTimeout = _EamTimerVariantsBwdDigitCompleteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 700),
    _EamTimerVariantsBwdDigitCompleteTimeout_Type()
)
eamTimerVariantsBwdDigitCompleteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsBwdDigitCompleteTimeout.setStatus("current")


class _EamTimerVariantsFwdWaitWinkTimeout_Type(Integer32):
    """Custom type eamTimerVariantsFwdWaitWinkTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamTimerVariantsFwdWaitWinkTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsFwdWaitWinkTimeout_Object = MibTableColumn
eamTimerVariantsFwdWaitWinkTimeout = _EamTimerVariantsFwdWaitWinkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 800),
    _EamTimerVariantsFwdWaitWinkTimeout_Type()
)
eamTimerVariantsFwdWaitWinkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsFwdWaitWinkTimeout.setStatus("current")


class _EamTimerVariantsFwdWaitMaxWinkOnTimeout_Type(Integer32):
    """Custom type eamTimerVariantsFwdWaitMaxWinkOnTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamTimerVariantsFwdWaitMaxWinkOnTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsFwdWaitMaxWinkOnTimeout_Object = MibTableColumn
eamTimerVariantsFwdWaitMaxWinkOnTimeout = _EamTimerVariantsFwdWaitMaxWinkOnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 900),
    _EamTimerVariantsFwdWaitMaxWinkOnTimeout_Type()
)
eamTimerVariantsFwdWaitMaxWinkOnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsFwdWaitMaxWinkOnTimeout.setStatus("current")


class _EamTimerVariantsFwdWaitPreDialTimeout_Type(Integer32):
    """Custom type eamTimerVariantsFwdWaitPreDialTimeout based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_EamTimerVariantsFwdWaitPreDialTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsFwdWaitPreDialTimeout_Object = MibTableColumn
eamTimerVariantsFwdWaitPreDialTimeout = _EamTimerVariantsFwdWaitPreDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 1000),
    _EamTimerVariantsFwdWaitPreDialTimeout_Type()
)
eamTimerVariantsFwdWaitPreDialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsFwdWaitPreDialTimeout.setStatus("current")


class _EamTimerVariantsFwdWaitAnswerTimeout_Type(Integer32):
    """Custom type eamTimerVariantsFwdWaitAnswerTimeout based on Integer32"""
    defaultValue = 180000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_EamTimerVariantsFwdWaitAnswerTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsFwdWaitAnswerTimeout_Object = MibTableColumn
eamTimerVariantsFwdWaitAnswerTimeout = _EamTimerVariantsFwdWaitAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 1100),
    _EamTimerVariantsFwdWaitAnswerTimeout_Type()
)
eamTimerVariantsFwdWaitAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsFwdWaitAnswerTimeout.setStatus("current")


class _EamTimerVariantsFwdClearForwardTimeout_Type(Integer32):
    """Custom type eamTimerVariantsFwdClearForwardTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_EamTimerVariantsFwdClearForwardTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsFwdClearForwardTimeout_Object = MibTableColumn
eamTimerVariantsFwdClearForwardTimeout = _EamTimerVariantsFwdClearForwardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 1200),
    _EamTimerVariantsFwdClearForwardTimeout_Type()
)
eamTimerVariantsFwdClearForwardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsFwdClearForwardTimeout.setStatus("current")


class _EamTimerVariantsReleaseGuardTimeout_Type(Integer32):
    """Custom type eamTimerVariantsReleaseGuardTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamTimerVariantsReleaseGuardTimeout_Type.__name__ = "Integer32"
_EamTimerVariantsReleaseGuardTimeout_Object = MibTableColumn
eamTimerVariantsReleaseGuardTimeout = _EamTimerVariantsReleaseGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 1300),
    _EamTimerVariantsReleaseGuardTimeout_Type()
)
eamTimerVariantsReleaseGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsReleaseGuardTimeout.setStatus("current")


class _EamTimerVariantsResetSpecific_Type(Integer32):
    """Custom type eamTimerVariantsResetSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("resetSpecific", 10))
    )


_EamTimerVariantsResetSpecific_Type.__name__ = "Integer32"
_EamTimerVariantsResetSpecific_Object = MibTableColumn
eamTimerVariantsResetSpecific = _EamTimerVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 300, 1, 1900),
    _EamTimerVariantsResetSpecific_Type()
)
eamTimerVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamTimerVariantsResetSpecific.setStatus("current")
_EamDigitTimerVariantsTable_Object = MibTable
eamDigitTimerVariantsTable = _EamDigitTimerVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400)
)
if mibBuilder.loadTexts:
    eamDigitTimerVariantsTable.setStatus("current")
_EamDigitTimerVariantsEntry_Object = MibTableRow
eamDigitTimerVariantsEntry = _EamDigitTimerVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400, 1)
)
eamDigitTimerVariantsEntry.setIndexNames(
    (0, "MX-EAM-MIB", "eamDigitTimerVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    eamDigitTimerVariantsEntry.setStatus("current")
_EamDigitTimerVariantsInterfaceName_Type = OctetString
_EamDigitTimerVariantsInterfaceName_Object = MibTableColumn
eamDigitTimerVariantsInterfaceName = _EamDigitTimerVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400, 1, 100),
    _EamDigitTimerVariantsInterfaceName_Type()
)
eamDigitTimerVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eamDigitTimerVariantsInterfaceName.setStatus("current")


class _EamDigitTimerVariantsOverrideDefault_Type(MxEnableState):
    """Custom type eamDigitTimerVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_EamDigitTimerVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_EamDigitTimerVariantsOverrideDefault_Object = MibTableColumn
eamDigitTimerVariantsOverrideDefault = _EamDigitTimerVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400, 1, 200),
    _EamDigitTimerVariantsOverrideDefault_Type()
)
eamDigitTimerVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamDigitTimerVariantsOverrideDefault.setStatus("current")


class _EamDigitTimerVariantsKPOnTimeout_Type(Integer32):
    """Custom type eamDigitTimerVariantsKPOnTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamDigitTimerVariantsKPOnTimeout_Type.__name__ = "Integer32"
_EamDigitTimerVariantsKPOnTimeout_Object = MibTableColumn
eamDigitTimerVariantsKPOnTimeout = _EamDigitTimerVariantsKPOnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400, 1, 300),
    _EamDigitTimerVariantsKPOnTimeout_Type()
)
eamDigitTimerVariantsKPOnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamDigitTimerVariantsKPOnTimeout.setStatus("current")


class _EamDigitTimerVariantsKPOffTimeout_Type(Integer32):
    """Custom type eamDigitTimerVariantsKPOffTimeout based on Integer32"""
    defaultValue = 68

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamDigitTimerVariantsKPOffTimeout_Type.__name__ = "Integer32"
_EamDigitTimerVariantsKPOffTimeout_Object = MibTableColumn
eamDigitTimerVariantsKPOffTimeout = _EamDigitTimerVariantsKPOffTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400, 1, 400),
    _EamDigitTimerVariantsKPOffTimeout_Type()
)
eamDigitTimerVariantsKPOffTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamDigitTimerVariantsKPOffTimeout.setStatus("current")


class _EamDigitTimerVariantsResetSpecific_Type(Integer32):
    """Custom type eamDigitTimerVariantsResetSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("resetSpecific", 10))
    )


_EamDigitTimerVariantsResetSpecific_Type.__name__ = "Integer32"
_EamDigitTimerVariantsResetSpecific_Object = MibTableColumn
eamDigitTimerVariantsResetSpecific = _EamDigitTimerVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 400, 1, 900),
    _EamDigitTimerVariantsResetSpecific_Type()
)
eamDigitTimerVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamDigitTimerVariantsResetSpecific.setStatus("current")
_EamLinkTimerVariantsTable_Object = MibTable
eamLinkTimerVariantsTable = _EamLinkTimerVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500)
)
if mibBuilder.loadTexts:
    eamLinkTimerVariantsTable.setStatus("current")
_EamLinkTimerVariantsEntry_Object = MibTableRow
eamLinkTimerVariantsEntry = _EamLinkTimerVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500, 1)
)
eamLinkTimerVariantsEntry.setIndexNames(
    (0, "MX-EAM-MIB", "eamLinkTimerVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    eamLinkTimerVariantsEntry.setStatus("current")
_EamLinkTimerVariantsInterfaceName_Type = OctetString
_EamLinkTimerVariantsInterfaceName_Object = MibTableColumn
eamLinkTimerVariantsInterfaceName = _EamLinkTimerVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500, 1, 100),
    _EamLinkTimerVariantsInterfaceName_Type()
)
eamLinkTimerVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eamLinkTimerVariantsInterfaceName.setStatus("current")


class _EamLinkTimerVariantsOverrideDefault_Type(MxEnableState):
    """Custom type eamLinkTimerVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_EamLinkTimerVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_EamLinkTimerVariantsOverrideDefault_Object = MibTableColumn
eamLinkTimerVariantsOverrideDefault = _EamLinkTimerVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500, 1, 200),
    _EamLinkTimerVariantsOverrideDefault_Type()
)
eamLinkTimerVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamLinkTimerVariantsOverrideDefault.setStatus("current")


class _EamLinkTimerVariantsLinkActivationTimeout_Type(Integer32):
    """Custom type eamLinkTimerVariantsLinkActivationTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamLinkTimerVariantsLinkActivationTimeout_Type.__name__ = "Integer32"
_EamLinkTimerVariantsLinkActivationTimeout_Object = MibTableColumn
eamLinkTimerVariantsLinkActivationTimeout = _EamLinkTimerVariantsLinkActivationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500, 1, 300),
    _EamLinkTimerVariantsLinkActivationTimeout_Type()
)
eamLinkTimerVariantsLinkActivationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamLinkTimerVariantsLinkActivationTimeout.setStatus("current")


class _EamLinkTimerVariantsLinkActivationRetryTimeout_Type(Integer32):
    """Custom type eamLinkTimerVariantsLinkActivationRetryTimeout based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EamLinkTimerVariantsLinkActivationRetryTimeout_Type.__name__ = "Integer32"
_EamLinkTimerVariantsLinkActivationRetryTimeout_Object = MibTableColumn
eamLinkTimerVariantsLinkActivationRetryTimeout = _EamLinkTimerVariantsLinkActivationRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500, 1, 400),
    _EamLinkTimerVariantsLinkActivationRetryTimeout_Type()
)
eamLinkTimerVariantsLinkActivationRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamLinkTimerVariantsLinkActivationRetryTimeout.setStatus("current")


class _EamLinkTimerVariantsResetSpecific_Type(Integer32):
    """Custom type eamLinkTimerVariantsResetSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("resetSpecific", 10))
    )


_EamLinkTimerVariantsResetSpecific_Type.__name__ = "Integer32"
_EamLinkTimerVariantsResetSpecific_Object = MibTableColumn
eamLinkTimerVariantsResetSpecific = _EamLinkTimerVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 500, 1, 900),
    _EamLinkTimerVariantsResetSpecific_Type()
)
eamLinkTimerVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamLinkTimerVariantsResetSpecific.setStatus("current")
_EamToneVariantsTable_Object = MibTable
eamToneVariantsTable = _EamToneVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600)
)
if mibBuilder.loadTexts:
    eamToneVariantsTable.setStatus("current")
_EamToneVariantsEntry_Object = MibTableRow
eamToneVariantsEntry = _EamToneVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600, 1)
)
eamToneVariantsEntry.setIndexNames(
    (0, "MX-EAM-MIB", "eamToneVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    eamToneVariantsEntry.setStatus("current")
_EamToneVariantsInterfaceName_Type = OctetString
_EamToneVariantsInterfaceName_Object = MibTableColumn
eamToneVariantsInterfaceName = _EamToneVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600, 1, 100),
    _EamToneVariantsInterfaceName_Type()
)
eamToneVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eamToneVariantsInterfaceName.setStatus("current")


class _EamToneVariantsOverrideDefault_Type(MxEnableState):
    """Custom type eamToneVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_EamToneVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_EamToneVariantsOverrideDefault_Object = MibTableColumn
eamToneVariantsOverrideDefault = _EamToneVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600, 1, 200),
    _EamToneVariantsOverrideDefault_Type()
)
eamToneVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamToneVariantsOverrideDefault.setStatus("current")


class _EamToneVariantsKpTone_Type(Integer32):
    """Custom type eamToneVariantsKpTone based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("mF0", 200),
          ("mF1", 300),
          ("mF2", 400),
          ("mF3", 500),
          ("mF4", 600),
          ("mF5", 700),
          ("mF6", 800),
          ("mF7", 900),
          ("mF8", 1000),
          ("mF9", 1100),
          ("mF10", 1200),
          ("mF11", 1300),
          ("mF12", 1400),
          ("mF13", 1500),
          ("mF14", 1600))
    )


_EamToneVariantsKpTone_Type.__name__ = "Integer32"
_EamToneVariantsKpTone_Object = MibTableColumn
eamToneVariantsKpTone = _EamToneVariantsKpTone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600, 1, 300),
    _EamToneVariantsKpTone_Type()
)
eamToneVariantsKpTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamToneVariantsKpTone.setStatus("current")


class _EamToneVariantsStTone_Type(Integer32):
    """Custom type eamToneVariantsStTone based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("mF0", 200),
          ("mF1", 300),
          ("mF2", 400),
          ("mF3", 500),
          ("mF4", 600),
          ("mF5", 700),
          ("mF6", 800),
          ("mF7", 900),
          ("mF8", 1000),
          ("mF9", 1100),
          ("mF10", 1200),
          ("mF11", 1300),
          ("mF12", 1400),
          ("mF13", 1500),
          ("mF14", 1600))
    )


_EamToneVariantsStTone_Type.__name__ = "Integer32"
_EamToneVariantsStTone_Object = MibTableColumn
eamToneVariantsStTone = _EamToneVariantsStTone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600, 1, 400),
    _EamToneVariantsStTone_Type()
)
eamToneVariantsStTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamToneVariantsStTone.setStatus("current")


class _EamToneVariantsResetSpecific_Type(Integer32):
    """Custom type eamToneVariantsResetSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("resetSpecific", 10))
    )


_EamToneVariantsResetSpecific_Type.__name__ = "Integer32"
_EamToneVariantsResetSpecific_Object = MibTableColumn
eamToneVariantsResetSpecific = _EamToneVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 100, 600, 1, 900),
    _EamToneVariantsResetSpecific_Type()
)
eamToneVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eamToneVariantsResetSpecific.setStatus("current")
_BearerChannelGroup_ObjectIdentity = ObjectIdentity
bearerChannelGroup = _BearerChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 200)
)
_BearerChannelInfoTable_Object = MibTable
bearerChannelInfoTable = _BearerChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 200, 100)
)
if mibBuilder.loadTexts:
    bearerChannelInfoTable.setStatus("current")
_BearerChannelInfoEntry_Object = MibTableRow
bearerChannelInfoEntry = _BearerChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 200, 100, 1)
)
bearerChannelInfoEntry.setIndexNames(
    (0, "MX-EAM-MIB", "bearerChannelInfoIndex"),
)
if mibBuilder.loadTexts:
    bearerChannelInfoEntry.setStatus("current")
_BearerChannelInfoIndex_Type = OctetString
_BearerChannelInfoIndex_Object = MibTableColumn
bearerChannelInfoIndex = _BearerChannelInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 200, 100, 1, 100),
    _BearerChannelInfoIndex_Type()
)
bearerChannelInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerChannelInfoIndex.setStatus("current")


class _BearerChannelInfoState_Type(Integer32):
    """Custom type bearerChannelInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("idle", 100),
          ("inUse", 200),
          ("maintenance", 300),
          ("error", 400),
          ("disabled", 500))
    )


_BearerChannelInfoState_Type.__name__ = "Integer32"
_BearerChannelInfoState_Object = MibTableColumn
bearerChannelInfoState = _BearerChannelInfoState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 200, 100, 1, 200),
    _BearerChannelInfoState_Type()
)
bearerChannelInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerChannelInfoState.setStatus("current")
_PhysicalGroup_ObjectIdentity = ObjectIdentity
physicalGroup = _PhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300)
)
_PhysicalLinkInfoTable_Object = MibTable
physicalLinkInfoTable = _PhysicalLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 100)
)
if mibBuilder.loadTexts:
    physicalLinkInfoTable.setStatus("current")
_PhysicalLinkInfoEntry_Object = MibTableRow
physicalLinkInfoEntry = _PhysicalLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 100, 1)
)
physicalLinkInfoEntry.setIndexNames(
    (0, "MX-EAM-MIB", "physicalLinkInfoInterfaceName"),
)
if mibBuilder.loadTexts:
    physicalLinkInfoEntry.setStatus("current")
_PhysicalLinkInfoInterfaceName_Type = OctetString
_PhysicalLinkInfoInterfaceName_Object = MibTableColumn
physicalLinkInfoInterfaceName = _PhysicalLinkInfoInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 100, 1, 100),
    _PhysicalLinkInfoInterfaceName_Type()
)
physicalLinkInfoInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInfoInterfaceName.setStatus("current")


class _PhysicalLinkInfoState_Type(Integer32):
    """Custom type physicalLinkInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("up", 100),
          ("down", 200))
    )


_PhysicalLinkInfoState_Type.__name__ = "Integer32"
_PhysicalLinkInfoState_Object = MibTableColumn
physicalLinkInfoState = _PhysicalLinkInfoState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 100, 1, 200),
    _PhysicalLinkInfoState_Type()
)
physicalLinkInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInfoState.setStatus("current")
_PhysicalLinkTable_Object = MibTable
physicalLinkTable = _PhysicalLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200)
)
if mibBuilder.loadTexts:
    physicalLinkTable.setStatus("current")
_PhysicalLinkEntry_Object = MibTableRow
physicalLinkEntry = _PhysicalLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1)
)
physicalLinkEntry.setIndexNames(
    (0, "MX-EAM-MIB", "physicalLinkInterfaceName"),
)
if mibBuilder.loadTexts:
    physicalLinkEntry.setStatus("current")
_PhysicalLinkInterfaceName_Type = OctetString
_PhysicalLinkInterfaceName_Object = MibTableColumn
physicalLinkInterfaceName = _PhysicalLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1, 100),
    _PhysicalLinkInterfaceName_Type()
)
physicalLinkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInterfaceName.setStatus("current")


class _PhysicalLinkLineCoding_Type(Integer32):
    """Custom type physicalLinkLineCoding based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("b8zs", 100),
          ("hdb3", 200),
          ("ami", 300))
    )


_PhysicalLinkLineCoding_Type.__name__ = "Integer32"
_PhysicalLinkLineCoding_Object = MibTableColumn
physicalLinkLineCoding = _PhysicalLinkLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1, 200),
    _PhysicalLinkLineCoding_Type()
)
physicalLinkLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkLineCoding.setStatus("current")


class _PhysicalLinkLineFraming_Type(Integer32):
    """Custom type physicalLinkLineFraming based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("sf", 100),
          ("esf", 200),
          ("crc4", 300),
          ("noCrc4", 400))
    )


_PhysicalLinkLineFraming_Type.__name__ = "Integer32"
_PhysicalLinkLineFraming_Object = MibTableColumn
physicalLinkLineFraming = _PhysicalLinkLineFraming_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1, 300),
    _PhysicalLinkLineFraming_Type()
)
physicalLinkLineFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkLineFraming.setStatus("current")


class _PhysicalLinkClockMode_Type(Integer32):
    """Custom type physicalLinkClockMode based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("master", 100),
          ("slave", 200))
    )


_PhysicalLinkClockMode_Type.__name__ = "Integer32"
_PhysicalLinkClockMode_Object = MibTableColumn
physicalLinkClockMode = _PhysicalLinkClockMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1, 400),
    _PhysicalLinkClockMode_Type()
)
physicalLinkClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkClockMode.setStatus("current")


class _PhysicalLinkMonitorLinkStateEnable_Type(MxEnableState):
    """Custom type physicalLinkMonitorLinkStateEnable based on MxEnableState"""
    defaultValue = 1


_PhysicalLinkMonitorLinkStateEnable_Type.__name__ = "MxEnableState"
_PhysicalLinkMonitorLinkStateEnable_Object = MibTableColumn
physicalLinkMonitorLinkStateEnable = _PhysicalLinkMonitorLinkStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1, 500),
    _PhysicalLinkMonitorLinkStateEnable_Type()
)
physicalLinkMonitorLinkStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkMonitorLinkStateEnable.setStatus("current")


class _PhysicalLinkPortPinout_Type(Integer32):
    """Custom type physicalLinkPortPinout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("auto", 100),
          ("master", 200),
          ("slave", 300))
    )


_PhysicalLinkPortPinout_Type.__name__ = "Integer32"
_PhysicalLinkPortPinout_Object = MibTableColumn
physicalLinkPortPinout = _PhysicalLinkPortPinout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 300, 200, 1, 600),
    _PhysicalLinkPortPinout_Type()
)
physicalLinkPortPinout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkPortPinout.setStatus("current")
_AutoConfigure_ObjectIdentity = ObjectIdentity
autoConfigure = _AutoConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 400)
)


class _AutoConfigureStatus_Type(Integer32):
    """Custom type autoConfigureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("idle", 100),
          ("sensing", 200))
    )


_AutoConfigureStatus_Type.__name__ = "Integer32"
_AutoConfigureStatus_Object = MibScalar
autoConfigureStatus = _AutoConfigureStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 400, 100),
    _AutoConfigureStatus_Type()
)
autoConfigureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoConfigureStatus.setStatus("current")


class _LastAutoConfigureResult_Type(Integer32):
    """Custom type lastAutoConfigureResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("success", 200),
          ("fail", 300),
          ("aborted", 400))
    )


_LastAutoConfigureResult_Type.__name__ = "Integer32"
_LastAutoConfigureResult_Object = MibScalar
lastAutoConfigureResult = _LastAutoConfigureResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 400, 200),
    _LastAutoConfigureResult_Type()
)
lastAutoConfigureResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAutoConfigureResult.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1880, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-EAM-MIB",
    **{"eamMIB": eamMIB,
       "eamMIBObjects": eamMIBObjects,
       "eamGroup": eamGroup,
       "eamTable": eamTable,
       "eamEntry": eamEntry,
       "eamName": eamName,
       "eamChannelRange": eamChannelRange,
       "eamChannelAllocationStrategy": eamChannelAllocationStrategy,
       "eamMaxActiveCalls": eamMaxActiveCalls,
       "eamEncodingScheme": eamEncodingScheme,
       "eamSignalingType": eamSignalingType,
       "eamDigitAttenuation": eamDigitAttenuation,
       "eamSignalingVariantsTable": eamSignalingVariantsTable,
       "eamSignalingVariantsEntry": eamSignalingVariantsEntry,
       "eamSignalingVariantsInterfaceName": eamSignalingVariantsInterfaceName,
       "eamSignalingVariantsOverrideDefault": eamSignalingVariantsOverrideDefault,
       "eamSignalingVariantsBitsBCD": eamSignalingVariantsBitsBCD,
       "eamSignalingVariantsDnisLength": eamSignalingVariantsDnisLength,
       "eamSignalingVariantsAniLength": eamSignalingVariantsAniLength,
       "eamSignalingVariantsIncomingRegisterSignaling": eamSignalingVariantsIncomingRegisterSignaling,
       "eamSignalingVariantsOutgoingRegisterSignaling": eamSignalingVariantsOutgoingRegisterSignaling,
       "eamSignalingVariantsIncomingDialMap": eamSignalingVariantsIncomingDialMap,
       "eamSignalingVariantsOutgoingDialMap": eamSignalingVariantsOutgoingDialMap,
       "eamSignalingVariantsWaitWink": eamSignalingVariantsWaitWink,
       "eamSignalingVariantsWaitWinkAck": eamSignalingVariantsWaitWinkAck,
       "eamSignalingVariantsSendWink": eamSignalingVariantsSendWink,
       "eamSignalingVariantsSendWinkAck": eamSignalingVariantsSendWinkAck,
       "eamSignalingVariantsResetSpecific": eamSignalingVariantsResetSpecific,
       "eamTimerVariantsTable": eamTimerVariantsTable,
       "eamTimerVariantsEntry": eamTimerVariantsEntry,
       "eamTimerVariantsInterfaceName": eamTimerVariantsInterfaceName,
       "eamTimerVariantsOverrideDefault": eamTimerVariantsOverrideDefault,
       "eamTimerVariantsBwdWaitPreWinkTimeout": eamTimerVariantsBwdWaitPreWinkTimeout,
       "eamTimerVariantsBwdSendWinkTimeout": eamTimerVariantsBwdSendWinkTimeout,
       "eamTimerVariantsBwdWait1stDigitTimeout": eamTimerVariantsBwdWait1stDigitTimeout,
       "eamTimerVariantsBwdClearBackwardTimeout": eamTimerVariantsBwdClearBackwardTimeout,
       "eamTimerVariantsBwdDigitCompleteTimeout": eamTimerVariantsBwdDigitCompleteTimeout,
       "eamTimerVariantsFwdWaitWinkTimeout": eamTimerVariantsFwdWaitWinkTimeout,
       "eamTimerVariantsFwdWaitMaxWinkOnTimeout": eamTimerVariantsFwdWaitMaxWinkOnTimeout,
       "eamTimerVariantsFwdWaitPreDialTimeout": eamTimerVariantsFwdWaitPreDialTimeout,
       "eamTimerVariantsFwdWaitAnswerTimeout": eamTimerVariantsFwdWaitAnswerTimeout,
       "eamTimerVariantsFwdClearForwardTimeout": eamTimerVariantsFwdClearForwardTimeout,
       "eamTimerVariantsReleaseGuardTimeout": eamTimerVariantsReleaseGuardTimeout,
       "eamTimerVariantsResetSpecific": eamTimerVariantsResetSpecific,
       "eamDigitTimerVariantsTable": eamDigitTimerVariantsTable,
       "eamDigitTimerVariantsEntry": eamDigitTimerVariantsEntry,
       "eamDigitTimerVariantsInterfaceName": eamDigitTimerVariantsInterfaceName,
       "eamDigitTimerVariantsOverrideDefault": eamDigitTimerVariantsOverrideDefault,
       "eamDigitTimerVariantsKPOnTimeout": eamDigitTimerVariantsKPOnTimeout,
       "eamDigitTimerVariantsKPOffTimeout": eamDigitTimerVariantsKPOffTimeout,
       "eamDigitTimerVariantsResetSpecific": eamDigitTimerVariantsResetSpecific,
       "eamLinkTimerVariantsTable": eamLinkTimerVariantsTable,
       "eamLinkTimerVariantsEntry": eamLinkTimerVariantsEntry,
       "eamLinkTimerVariantsInterfaceName": eamLinkTimerVariantsInterfaceName,
       "eamLinkTimerVariantsOverrideDefault": eamLinkTimerVariantsOverrideDefault,
       "eamLinkTimerVariantsLinkActivationTimeout": eamLinkTimerVariantsLinkActivationTimeout,
       "eamLinkTimerVariantsLinkActivationRetryTimeout": eamLinkTimerVariantsLinkActivationRetryTimeout,
       "eamLinkTimerVariantsResetSpecific": eamLinkTimerVariantsResetSpecific,
       "eamToneVariantsTable": eamToneVariantsTable,
       "eamToneVariantsEntry": eamToneVariantsEntry,
       "eamToneVariantsInterfaceName": eamToneVariantsInterfaceName,
       "eamToneVariantsOverrideDefault": eamToneVariantsOverrideDefault,
       "eamToneVariantsKpTone": eamToneVariantsKpTone,
       "eamToneVariantsStTone": eamToneVariantsStTone,
       "eamToneVariantsResetSpecific": eamToneVariantsResetSpecific,
       "bearerChannelGroup": bearerChannelGroup,
       "bearerChannelInfoTable": bearerChannelInfoTable,
       "bearerChannelInfoEntry": bearerChannelInfoEntry,
       "bearerChannelInfoIndex": bearerChannelInfoIndex,
       "bearerChannelInfoState": bearerChannelInfoState,
       "physicalGroup": physicalGroup,
       "physicalLinkInfoTable": physicalLinkInfoTable,
       "physicalLinkInfoEntry": physicalLinkInfoEntry,
       "physicalLinkInfoInterfaceName": physicalLinkInfoInterfaceName,
       "physicalLinkInfoState": physicalLinkInfoState,
       "physicalLinkTable": physicalLinkTable,
       "physicalLinkEntry": physicalLinkEntry,
       "physicalLinkInterfaceName": physicalLinkInterfaceName,
       "physicalLinkLineCoding": physicalLinkLineCoding,
       "physicalLinkLineFraming": physicalLinkLineFraming,
       "physicalLinkClockMode": physicalLinkClockMode,
       "physicalLinkMonitorLinkStateEnable": physicalLinkMonitorLinkStateEnable,
       "physicalLinkPortPinout": physicalLinkPortPinout,
       "autoConfigure": autoConfigure,
       "autoConfigureStatus": autoConfigureStatus,
       "lastAutoConfigureResult": lastAutoConfigureResult,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
