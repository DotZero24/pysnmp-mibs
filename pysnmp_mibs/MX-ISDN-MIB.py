# SNMP MIB module (MX-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-ISDN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:09 2025
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

isdnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IsdnMIBObjects_ObjectIdentity = ObjectIdentity
isdnMIBObjects = _IsdnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1)
)
_PrimaryRateInterfaceGroup_ObjectIdentity = ObjectIdentity
primaryRateInterfaceGroup = _PrimaryRateInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200)
)
_PrimaryRateInterfaceTable_Object = MibTable
primaryRateInterfaceTable = _PrimaryRateInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100)
)
if mibBuilder.loadTexts:
    primaryRateInterfaceTable.setStatus("current")
_PrimaryRateInterfaceEntry_Object = MibTableRow
primaryRateInterfaceEntry = _PrimaryRateInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1)
)
primaryRateInterfaceEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "primaryRateInterfaceName"),
)
if mibBuilder.loadTexts:
    primaryRateInterfaceEntry.setStatus("current")
_PrimaryRateInterfaceName_Type = OctetString
_PrimaryRateInterfaceName_Object = MibTableColumn
primaryRateInterfaceName = _PrimaryRateInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 100),
    _PrimaryRateInterfaceName_Type()
)
primaryRateInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryRateInterfaceName.setStatus("current")


class _PrimaryRateInterfaceEndpointType_Type(Integer32):
    """Custom type primaryRateInterfaceEndpointType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("te", 100),
          ("nt", 200))
    )


_PrimaryRateInterfaceEndpointType_Type.__name__ = "Integer32"
_PrimaryRateInterfaceEndpointType_Object = MibTableColumn
primaryRateInterfaceEndpointType = _PrimaryRateInterfaceEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 200),
    _PrimaryRateInterfaceEndpointType_Type()
)
primaryRateInterfaceEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceEndpointType.setStatus("current")


class _PrimaryRateInterfacePortPinout_Type(Integer32):
    """Custom type primaryRateInterfacePortPinout based on Integer32"""
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
          ("te", 200),
          ("nt", 300))
    )


_PrimaryRateInterfacePortPinout_Type.__name__ = "Integer32"
_PrimaryRateInterfacePortPinout_Object = MibTableColumn
primaryRateInterfacePortPinout = _PrimaryRateInterfacePortPinout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 250),
    _PrimaryRateInterfacePortPinout_Type()
)
primaryRateInterfacePortPinout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfacePortPinout.setStatus("current")


class _PrimaryRateInterfaceLineCoding_Type(Integer32):
    """Custom type primaryRateInterfaceLineCoding based on Integer32"""
    defaultValue = 200

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


_PrimaryRateInterfaceLineCoding_Type.__name__ = "Integer32"
_PrimaryRateInterfaceLineCoding_Object = MibTableColumn
primaryRateInterfaceLineCoding = _PrimaryRateInterfaceLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 400),
    _PrimaryRateInterfaceLineCoding_Type()
)
primaryRateInterfaceLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceLineCoding.setStatus("current")


class _PrimaryRateInterfaceLineFraming_Type(Integer32):
    """Custom type primaryRateInterfaceLineFraming based on Integer32"""
    defaultValue = 300

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


_PrimaryRateInterfaceLineFraming_Type.__name__ = "Integer32"
_PrimaryRateInterfaceLineFraming_Object = MibTableColumn
primaryRateInterfaceLineFraming = _PrimaryRateInterfaceLineFraming_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 500),
    _PrimaryRateInterfaceLineFraming_Type()
)
primaryRateInterfaceLineFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceLineFraming.setStatus("current")


class _PrimaryRateInterfaceNetworkLocation_Type(Integer32):
    """Custom type primaryRateInterfaceNetworkLocation based on Integer32"""
    defaultValue = 100

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
        *(("user", 100),
          ("private", 200),
          ("public", 300),
          ("transit", 400),
          ("international", 500))
    )


_PrimaryRateInterfaceNetworkLocation_Type.__name__ = "Integer32"
_PrimaryRateInterfaceNetworkLocation_Object = MibTableColumn
primaryRateInterfaceNetworkLocation = _PrimaryRateInterfaceNetworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 600),
    _PrimaryRateInterfaceNetworkLocation_Type()
)
primaryRateInterfaceNetworkLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceNetworkLocation.setStatus("current")


class _PrimaryRateInterfacePreferredEncodingScheme_Type(Integer32):
    """Custom type primaryRateInterfacePreferredEncodingScheme based on Integer32"""
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


_PrimaryRateInterfacePreferredEncodingScheme_Type.__name__ = "Integer32"
_PrimaryRateInterfacePreferredEncodingScheme_Object = MibTableColumn
primaryRateInterfacePreferredEncodingScheme = _PrimaryRateInterfacePreferredEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 700),
    _PrimaryRateInterfacePreferredEncodingScheme_Type()
)
primaryRateInterfacePreferredEncodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfacePreferredEncodingScheme.setStatus("current")


class _PrimaryRateInterfaceFallbackEncodingScheme_Type(Integer32):
    """Custom type primaryRateInterfaceFallbackEncodingScheme based on Integer32"""
    defaultValue = 200

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


_PrimaryRateInterfaceFallbackEncodingScheme_Type.__name__ = "Integer32"
_PrimaryRateInterfaceFallbackEncodingScheme_Object = MibTableColumn
primaryRateInterfaceFallbackEncodingScheme = _PrimaryRateInterfaceFallbackEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 750),
    _PrimaryRateInterfaceFallbackEncodingScheme_Type()
)
primaryRateInterfaceFallbackEncodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceFallbackEncodingScheme.setStatus("current")


class _PrimaryRateInterfaceChannelRange_Type(OctetString):
    """Custom type primaryRateInterfaceChannelRange based on OctetString"""
    defaultValue = OctetString("1-30")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_PrimaryRateInterfaceChannelRange_Type.__name__ = "OctetString"
_PrimaryRateInterfaceChannelRange_Object = MibTableColumn
primaryRateInterfaceChannelRange = _PrimaryRateInterfaceChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 800),
    _PrimaryRateInterfaceChannelRange_Type()
)
primaryRateInterfaceChannelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceChannelRange.setStatus("current")


class _PrimaryRateInterfaceIncomingChannelRange_Type(OctetString):
    """Custom type primaryRateInterfaceIncomingChannelRange based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrimaryRateInterfaceIncomingChannelRange_Type.__name__ = "OctetString"
_PrimaryRateInterfaceIncomingChannelRange_Object = MibTableColumn
primaryRateInterfaceIncomingChannelRange = _PrimaryRateInterfaceIncomingChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 830),
    _PrimaryRateInterfaceIncomingChannelRange_Type()
)
primaryRateInterfaceIncomingChannelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceIncomingChannelRange.setStatus("current")


class _PrimaryRateInterfaceOutgoingChannelRange_Type(OctetString):
    """Custom type primaryRateInterfaceOutgoingChannelRange based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrimaryRateInterfaceOutgoingChannelRange_Type.__name__ = "OctetString"
_PrimaryRateInterfaceOutgoingChannelRange_Object = MibTableColumn
primaryRateInterfaceOutgoingChannelRange = _PrimaryRateInterfaceOutgoingChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 860),
    _PrimaryRateInterfaceOutgoingChannelRange_Type()
)
primaryRateInterfaceOutgoingChannelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceOutgoingChannelRange.setStatus("current")


class _PrimaryRateInterfaceChannelAllocationStrategy_Type(Integer32):
    """Custom type primaryRateInterfaceChannelAllocationStrategy based on Integer32"""
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


_PrimaryRateInterfaceChannelAllocationStrategy_Type.__name__ = "Integer32"
_PrimaryRateInterfaceChannelAllocationStrategy_Object = MibTableColumn
primaryRateInterfaceChannelAllocationStrategy = _PrimaryRateInterfaceChannelAllocationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 900),
    _PrimaryRateInterfaceChannelAllocationStrategy_Type()
)
primaryRateInterfaceChannelAllocationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceChannelAllocationStrategy.setStatus("current")


class _PrimaryRateInterfaceMaxActiveCalls_Type(Unsigned32):
    """Custom type primaryRateInterfaceMaxActiveCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PrimaryRateInterfaceMaxActiveCalls_Type.__name__ = "Unsigned32"
_PrimaryRateInterfaceMaxActiveCalls_Object = MibTableColumn
primaryRateInterfaceMaxActiveCalls = _PrimaryRateInterfaceMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1000),
    _PrimaryRateInterfaceMaxActiveCalls_Type()
)
primaryRateInterfaceMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceMaxActiveCalls.setStatus("current")


class _PrimaryRateInterfaceSignalInformationElementEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceSignalInformationElementEnable based on MxEnableState"""
    defaultValue = 0


_PrimaryRateInterfaceSignalInformationElementEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceSignalInformationElementEnable_Object = MibTableColumn
primaryRateInterfaceSignalInformationElementEnable = _PrimaryRateInterfaceSignalInformationElementEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1050),
    _PrimaryRateInterfaceSignalInformationElementEnable_Type()
)
primaryRateInterfaceSignalInformationElementEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceSignalInformationElementEnable.setStatus("current")


class _PrimaryRateInterfaceInbandToneGenerationEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInbandToneGenerationEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInbandToneGenerationEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInbandToneGenerationEnable_Object = MibTableColumn
primaryRateInterfaceInbandToneGenerationEnable = _PrimaryRateInterfaceInbandToneGenerationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1100),
    _PrimaryRateInterfaceInbandToneGenerationEnable_Type()
)
primaryRateInterfaceInbandToneGenerationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInbandToneGenerationEnable.setStatus("current")


class _PrimaryRateInterfaceInbandDtmfDialingEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInbandDtmfDialingEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInbandDtmfDialingEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInbandDtmfDialingEnable_Object = MibTableColumn
primaryRateInterfaceInbandDtmfDialingEnable = _PrimaryRateInterfaceInbandDtmfDialingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1200),
    _PrimaryRateInterfaceInbandDtmfDialingEnable_Type()
)
primaryRateInterfaceInbandDtmfDialingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInbandDtmfDialingEnable.setStatus("current")


class _PrimaryRateInterfaceOverlapDialingEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceOverlapDialingEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceOverlapDialingEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceOverlapDialingEnable_Object = MibTableColumn
primaryRateInterfaceOverlapDialingEnable = _PrimaryRateInterfaceOverlapDialingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1300),
    _PrimaryRateInterfaceOverlapDialingEnable_Type()
)
primaryRateInterfaceOverlapDialingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceOverlapDialingEnable.setStatus("current")


class _PrimaryRateInterfaceCallingNameMaxLength_Type(Unsigned32):
    """Custom type primaryRateInterfaceCallingNameMaxLength based on Unsigned32"""
    defaultValue = 34

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 82),
    )


_PrimaryRateInterfaceCallingNameMaxLength_Type.__name__ = "Unsigned32"
_PrimaryRateInterfaceCallingNameMaxLength_Object = MibTableColumn
primaryRateInterfaceCallingNameMaxLength = _PrimaryRateInterfaceCallingNameMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1400),
    _PrimaryRateInterfaceCallingNameMaxLength_Type()
)
primaryRateInterfaceCallingNameMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceCallingNameMaxLength.setStatus("current")


class _PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceExclusiveBChannelSelectionEnable based on MxEnableState"""
    defaultValue = 0


_PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Object = MibTableColumn
primaryRateInterfaceExclusiveBChannelSelectionEnable = _PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1500),
    _PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Type()
)
primaryRateInterfaceExclusiveBChannelSelectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceExclusiveBChannelSelectionEnable.setStatus("current")


class _PrimaryRateInterfaceSendingCompleteEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceSendingCompleteEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceSendingCompleteEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceSendingCompleteEnable_Object = MibTableColumn
primaryRateInterfaceSendingCompleteEnable = _PrimaryRateInterfaceSendingCompleteEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1600),
    _PrimaryRateInterfaceSendingCompleteEnable_Type()
)
primaryRateInterfaceSendingCompleteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceSendingCompleteEnable.setStatus("current")


class _PrimaryRateInterfaceClipEnable_Type(Integer32):
    """Custom type primaryRateInterfaceClipEnable based on Integer32"""
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
        *(("userOnly", 0),
          ("enable", 1),
          ("disable", 2))
    )


_PrimaryRateInterfaceClipEnable_Type.__name__ = "Integer32"
_PrimaryRateInterfaceClipEnable_Object = MibTableColumn
primaryRateInterfaceClipEnable = _PrimaryRateInterfaceClipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1700),
    _PrimaryRateInterfaceClipEnable_Type()
)
primaryRateInterfaceClipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceClipEnable.setStatus("current")


class _PrimaryRateInterfaceClirEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceClirEnable based on MxEnableState"""
    defaultValue = 0


_PrimaryRateInterfaceClirEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceClirEnable_Object = MibTableColumn
primaryRateInterfaceClirEnable = _PrimaryRateInterfaceClirEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1725),
    _PrimaryRateInterfaceClirEnable_Type()
)
primaryRateInterfaceClirEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceClirEnable.setStatus("current")


class _PrimaryRateInterfaceClirOverrideEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceClirOverrideEnable based on MxEnableState"""
    defaultValue = 0


_PrimaryRateInterfaceClirOverrideEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceClirOverrideEnable_Object = MibTableColumn
primaryRateInterfaceClirOverrideEnable = _PrimaryRateInterfaceClirOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1750),
    _PrimaryRateInterfaceClirOverrideEnable_Type()
)
primaryRateInterfaceClirOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceClirOverrideEnable.setStatus("current")


class _PrimaryRateInterfaceSendRestartOnStartupEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceSendRestartOnStartupEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceSendRestartOnStartupEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceSendRestartOnStartupEnable_Object = MibTableColumn
primaryRateInterfaceSendRestartOnStartupEnable = _PrimaryRateInterfaceSendRestartOnStartupEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 100, 1, 1800),
    _PrimaryRateInterfaceSendRestartOnStartupEnable_Type()
)
primaryRateInterfaceSendRestartOnStartupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceSendRestartOnStartupEnable.setStatus("current")
_PrimaryRateInterfaceInteropGroup_ObjectIdentity = ObjectIdentity
primaryRateInterfaceInteropGroup = _PrimaryRateInterfaceInteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000)
)
_PrimaryRateInterfaceInteropTable_Object = MibTable
primaryRateInterfaceInteropTable = _PrimaryRateInterfaceInteropTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100)
)
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropTable.setStatus("current")
_PrimaryRateInterfaceInteropEntry_Object = MibTableRow
primaryRateInterfaceInteropEntry = _PrimaryRateInterfaceInteropEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1)
)
primaryRateInterfaceInteropEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "primaryRateInterfaceInteropName"),
)
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropEntry.setStatus("current")
_PrimaryRateInterfaceInteropName_Type = OctetString
_PrimaryRateInterfaceInteropName_Object = MibTableColumn
primaryRateInterfaceInteropName = _PrimaryRateInterfaceInteropName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 100),
    _PrimaryRateInterfaceInteropName_Type()
)
primaryRateInterfaceInteropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropName.setStatus("current")


class _PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropProgressIndicatorInSetupEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Object = MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInSetupEnable = _PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 200),
    _PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Type()
)
primaryRateInterfaceInteropProgressIndicatorInSetupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropProgressIndicatorInSetupEnable.setStatus("current")


class _PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object = MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable = _PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 300),
    _PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type()
)
primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable.setStatus("current")


class _PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object = MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable = _PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 400),
    _PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type()
)
primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setStatus("current")


class _PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropProgressIndicatorInProgressEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Object = MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInProgressEnable = _PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 450),
    _PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Type()
)
primaryRateInterfaceInteropProgressIndicatorInProgressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropProgressIndicatorInProgressEnable.setStatus("current")


class _PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropProgressIndicatorInAlertingEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Object = MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInAlertingEnable = _PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 500),
    _PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Type()
)
primaryRateInterfaceInteropProgressIndicatorInAlertingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropProgressIndicatorInAlertingEnable.setStatus("current")


class _PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropProgressIndicatorInConnectEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Object = MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInConnectEnable = _PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 600),
    _PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Type()
)
primaryRateInterfaceInteropProgressIndicatorInConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropProgressIndicatorInConnectEnable.setStatus("current")


class _PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Type(Unsigned32):
    """Custom type primaryRateInterfaceInteropMaximumFacilityWaitingDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Type.__name__ = "Unsigned32"
_PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Object = MibTableColumn
primaryRateInterfaceInteropMaximumFacilityWaitingDelay = _PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 700),
    _PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Type()
)
primaryRateInterfaceInteropMaximumFacilityWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropMaximumFacilityWaitingDelay.setStatus("current")


class _PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Type(MxEnableState):
    """Custom type primaryRateInterfaceInteropUseImplicitInbandInfoEnable based on MxEnableState"""
    defaultValue = 1


_PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Type.__name__ = "MxEnableState"
_PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Object = MibTableColumn
primaryRateInterfaceInteropUseImplicitInbandInfoEnable = _PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 200, 50000, 100, 1, 800),
    _PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Type()
)
primaryRateInterfaceInteropUseImplicitInbandInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRateInterfaceInteropUseImplicitInbandInfoEnable.setStatus("current")
_BasicRateInterfaceGroup_ObjectIdentity = ObjectIdentity
basicRateInterfaceGroup = _BasicRateInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300)
)
_BasicRateInterfaceTable_Object = MibTable
basicRateInterfaceTable = _BasicRateInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100)
)
if mibBuilder.loadTexts:
    basicRateInterfaceTable.setStatus("current")
_BasicRateInterfaceEntry_Object = MibTableRow
basicRateInterfaceEntry = _BasicRateInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1)
)
basicRateInterfaceEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "basicRateInterfaceName"),
)
if mibBuilder.loadTexts:
    basicRateInterfaceEntry.setStatus("current")
_BasicRateInterfaceName_Type = OctetString
_BasicRateInterfaceName_Object = MibTableColumn
basicRateInterfaceName = _BasicRateInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 100),
    _BasicRateInterfaceName_Type()
)
basicRateInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicRateInterfaceName.setStatus("current")


class _BasicRateInterfaceEndpointType_Type(Integer32):
    """Custom type basicRateInterfaceEndpointType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("te", 100),
          ("nt", 200))
    )


_BasicRateInterfaceEndpointType_Type.__name__ = "Integer32"
_BasicRateInterfaceEndpointType_Object = MibTableColumn
basicRateInterfaceEndpointType = _BasicRateInterfaceEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 200),
    _BasicRateInterfaceEndpointType_Type()
)
basicRateInterfaceEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceEndpointType.setStatus("current")


class _BasicRateInterfaceConnectionType_Type(Integer32):
    """Custom type basicRateInterfaceConnectionType based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 100),
          ("pointToMultiPoint", 200))
    )


_BasicRateInterfaceConnectionType_Type.__name__ = "Integer32"
_BasicRateInterfaceConnectionType_Object = MibTableColumn
basicRateInterfaceConnectionType = _BasicRateInterfaceConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 300),
    _BasicRateInterfaceConnectionType_Type()
)
basicRateInterfaceConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceConnectionType.setStatus("current")


class _BasicRateInterfaceNetworkLocation_Type(Integer32):
    """Custom type basicRateInterfaceNetworkLocation based on Integer32"""
    defaultValue = 100

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
        *(("user", 100),
          ("private", 200),
          ("public", 300),
          ("transit", 400),
          ("international", 500))
    )


_BasicRateInterfaceNetworkLocation_Type.__name__ = "Integer32"
_BasicRateInterfaceNetworkLocation_Object = MibTableColumn
basicRateInterfaceNetworkLocation = _BasicRateInterfaceNetworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 600),
    _BasicRateInterfaceNetworkLocation_Type()
)
basicRateInterfaceNetworkLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceNetworkLocation.setStatus("current")


class _BasicRateInterfacePreferredEncodingScheme_Type(Integer32):
    """Custom type basicRateInterfacePreferredEncodingScheme based on Integer32"""
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


_BasicRateInterfacePreferredEncodingScheme_Type.__name__ = "Integer32"
_BasicRateInterfacePreferredEncodingScheme_Object = MibTableColumn
basicRateInterfacePreferredEncodingScheme = _BasicRateInterfacePreferredEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 700),
    _BasicRateInterfacePreferredEncodingScheme_Type()
)
basicRateInterfacePreferredEncodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfacePreferredEncodingScheme.setStatus("current")


class _BasicRateInterfaceFallbackEncodingScheme_Type(Integer32):
    """Custom type basicRateInterfaceFallbackEncodingScheme based on Integer32"""
    defaultValue = 200

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


_BasicRateInterfaceFallbackEncodingScheme_Type.__name__ = "Integer32"
_BasicRateInterfaceFallbackEncodingScheme_Object = MibTableColumn
basicRateInterfaceFallbackEncodingScheme = _BasicRateInterfaceFallbackEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 750),
    _BasicRateInterfaceFallbackEncodingScheme_Type()
)
basicRateInterfaceFallbackEncodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceFallbackEncodingScheme.setStatus("current")


class _BasicRateInterfaceChannelAllocationStrategy_Type(Integer32):
    """Custom type basicRateInterfaceChannelAllocationStrategy based on Integer32"""
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


_BasicRateInterfaceChannelAllocationStrategy_Type.__name__ = "Integer32"
_BasicRateInterfaceChannelAllocationStrategy_Object = MibTableColumn
basicRateInterfaceChannelAllocationStrategy = _BasicRateInterfaceChannelAllocationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 900),
    _BasicRateInterfaceChannelAllocationStrategy_Type()
)
basicRateInterfaceChannelAllocationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceChannelAllocationStrategy.setStatus("current")


class _BasicRateInterfaceMaxActiveCalls_Type(Unsigned32):
    """Custom type basicRateInterfaceMaxActiveCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BasicRateInterfaceMaxActiveCalls_Type.__name__ = "Unsigned32"
_BasicRateInterfaceMaxActiveCalls_Object = MibTableColumn
basicRateInterfaceMaxActiveCalls = _BasicRateInterfaceMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1000),
    _BasicRateInterfaceMaxActiveCalls_Type()
)
basicRateInterfaceMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceMaxActiveCalls.setStatus("current")


class _BasicRateInterfaceSignalInformationElementEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceSignalInformationElementEnable based on MxEnableState"""
    defaultValue = 0


_BasicRateInterfaceSignalInformationElementEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceSignalInformationElementEnable_Object = MibTableColumn
basicRateInterfaceSignalInformationElementEnable = _BasicRateInterfaceSignalInformationElementEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1050),
    _BasicRateInterfaceSignalInformationElementEnable_Type()
)
basicRateInterfaceSignalInformationElementEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceSignalInformationElementEnable.setStatus("current")


class _BasicRateInterfaceInbandToneGenerationEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInbandToneGenerationEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInbandToneGenerationEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInbandToneGenerationEnable_Object = MibTableColumn
basicRateInterfaceInbandToneGenerationEnable = _BasicRateInterfaceInbandToneGenerationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1100),
    _BasicRateInterfaceInbandToneGenerationEnable_Type()
)
basicRateInterfaceInbandToneGenerationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInbandToneGenerationEnable.setStatus("current")


class _BasicRateInterfaceInbandDtmfDialingEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInbandDtmfDialingEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInbandDtmfDialingEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInbandDtmfDialingEnable_Object = MibTableColumn
basicRateInterfaceInbandDtmfDialingEnable = _BasicRateInterfaceInbandDtmfDialingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1200),
    _BasicRateInterfaceInbandDtmfDialingEnable_Type()
)
basicRateInterfaceInbandDtmfDialingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInbandDtmfDialingEnable.setStatus("current")


class _BasicRateInterfaceOverlapDialingEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceOverlapDialingEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceOverlapDialingEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceOverlapDialingEnable_Object = MibTableColumn
basicRateInterfaceOverlapDialingEnable = _BasicRateInterfaceOverlapDialingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1300),
    _BasicRateInterfaceOverlapDialingEnable_Type()
)
basicRateInterfaceOverlapDialingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceOverlapDialingEnable.setStatus("current")


class _BasicRateInterfaceCallingNameMaxLength_Type(Unsigned32):
    """Custom type basicRateInterfaceCallingNameMaxLength based on Unsigned32"""
    defaultValue = 34

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 82),
    )


_BasicRateInterfaceCallingNameMaxLength_Type.__name__ = "Unsigned32"
_BasicRateInterfaceCallingNameMaxLength_Object = MibTableColumn
basicRateInterfaceCallingNameMaxLength = _BasicRateInterfaceCallingNameMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1400),
    _BasicRateInterfaceCallingNameMaxLength_Type()
)
basicRateInterfaceCallingNameMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceCallingNameMaxLength.setStatus("current")


class _BasicRateInterfaceExclusiveBChannelSelectionEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceExclusiveBChannelSelectionEnable based on MxEnableState"""
    defaultValue = 0


_BasicRateInterfaceExclusiveBChannelSelectionEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceExclusiveBChannelSelectionEnable_Object = MibTableColumn
basicRateInterfaceExclusiveBChannelSelectionEnable = _BasicRateInterfaceExclusiveBChannelSelectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1500),
    _BasicRateInterfaceExclusiveBChannelSelectionEnable_Type()
)
basicRateInterfaceExclusiveBChannelSelectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceExclusiveBChannelSelectionEnable.setStatus("current")


class _BasicRateInterfaceSendingCompleteEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceSendingCompleteEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceSendingCompleteEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceSendingCompleteEnable_Object = MibTableColumn
basicRateInterfaceSendingCompleteEnable = _BasicRateInterfaceSendingCompleteEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1600),
    _BasicRateInterfaceSendingCompleteEnable_Type()
)
basicRateInterfaceSendingCompleteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceSendingCompleteEnable.setStatus("current")


class _BasicRateInterfaceClipEnable_Type(Integer32):
    """Custom type basicRateInterfaceClipEnable based on Integer32"""
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
        *(("userOnly", 0),
          ("enable", 1),
          ("disable", 2))
    )


_BasicRateInterfaceClipEnable_Type.__name__ = "Integer32"
_BasicRateInterfaceClipEnable_Object = MibTableColumn
basicRateInterfaceClipEnable = _BasicRateInterfaceClipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1700),
    _BasicRateInterfaceClipEnable_Type()
)
basicRateInterfaceClipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceClipEnable.setStatus("current")


class _BasicRateInterfaceClirEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceClirEnable based on MxEnableState"""
    defaultValue = 0


_BasicRateInterfaceClirEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceClirEnable_Object = MibTableColumn
basicRateInterfaceClirEnable = _BasicRateInterfaceClirEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1725),
    _BasicRateInterfaceClirEnable_Type()
)
basicRateInterfaceClirEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceClirEnable.setStatus("current")


class _BasicRateInterfaceClirOverrideEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceClirOverrideEnable based on MxEnableState"""
    defaultValue = 0


_BasicRateInterfaceClirOverrideEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceClirOverrideEnable_Object = MibTableColumn
basicRateInterfaceClirOverrideEnable = _BasicRateInterfaceClirOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1750),
    _BasicRateInterfaceClirOverrideEnable_Type()
)
basicRateInterfaceClirOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceClirOverrideEnable.setStatus("current")


class _BasicRateInterfaceSendRestartOnStartupEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceSendRestartOnStartupEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceSendRestartOnStartupEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceSendRestartOnStartupEnable_Object = MibTableColumn
basicRateInterfaceSendRestartOnStartupEnable = _BasicRateInterfaceSendRestartOnStartupEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1800),
    _BasicRateInterfaceSendRestartOnStartupEnable_Type()
)
basicRateInterfaceSendRestartOnStartupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceSendRestartOnStartupEnable.setStatus("current")


class _BasicRateInterfaceHookFlashKeypad_Type(OctetString):
    """Custom type basicRateInterfaceHookFlashKeypad based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicRateInterfaceHookFlashKeypad_Type.__name__ = "OctetString"
_BasicRateInterfaceHookFlashKeypad_Object = MibTableColumn
basicRateInterfaceHookFlashKeypad = _BasicRateInterfaceHookFlashKeypad_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 1900),
    _BasicRateInterfaceHookFlashKeypad_Type()
)
basicRateInterfaceHookFlashKeypad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceHookFlashKeypad.setStatus("current")


class _BasicRateInterfaceKeypadReceptionTimeout_Type(Unsigned32):
    """Custom type basicRateInterfaceKeypadReceptionTimeout based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BasicRateInterfaceKeypadReceptionTimeout_Type.__name__ = "Unsigned32"
_BasicRateInterfaceKeypadReceptionTimeout_Object = MibTableColumn
basicRateInterfaceKeypadReceptionTimeout = _BasicRateInterfaceKeypadReceptionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 2000),
    _BasicRateInterfaceKeypadReceptionTimeout_Type()
)
basicRateInterfaceKeypadReceptionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceKeypadReceptionTimeout.setStatus("current")


class _BasicRateInterfaceMsn_Type(OctetString):
    """Custom type basicRateInterfaceMsn based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasicRateInterfaceMsn_Type.__name__ = "OctetString"
_BasicRateInterfaceMsn_Object = MibTableColumn
basicRateInterfaceMsn = _BasicRateInterfaceMsn_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 2200),
    _BasicRateInterfaceMsn_Type()
)
basicRateInterfaceMsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceMsn.setStatus("current")


class _BasicRateInterfaceMsn2_Type(OctetString):
    """Custom type basicRateInterfaceMsn2 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicRateInterfaceMsn2_Type.__name__ = "OctetString"
_BasicRateInterfaceMsn2_Object = MibTableColumn
basicRateInterfaceMsn2 = _BasicRateInterfaceMsn2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 2300),
    _BasicRateInterfaceMsn2_Type()
)
basicRateInterfaceMsn2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceMsn2.setStatus("deprecated")


class _BasicRateInterfaceMsn3_Type(OctetString):
    """Custom type basicRateInterfaceMsn3 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BasicRateInterfaceMsn3_Type.__name__ = "OctetString"
_BasicRateInterfaceMsn3_Object = MibTableColumn
basicRateInterfaceMsn3 = _BasicRateInterfaceMsn3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 2400),
    _BasicRateInterfaceMsn3_Type()
)
basicRateInterfaceMsn3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceMsn3.setStatus("deprecated")


class _BasicRateInterfaceTeiNegotiation_Type(Integer32):
    """Custom type basicRateInterfaceTeiNegotiation based on Integer32"""
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
        *(("linkUp", 100),
          ("powerUp", 200),
          ("signalingUp", 300))
    )


_BasicRateInterfaceTeiNegotiation_Type.__name__ = "Integer32"
_BasicRateInterfaceTeiNegotiation_Object = MibTableColumn
basicRateInterfaceTeiNegotiation = _BasicRateInterfaceTeiNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 100, 1, 2500),
    _BasicRateInterfaceTeiNegotiation_Type()
)
basicRateInterfaceTeiNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceTeiNegotiation.setStatus("current")
_BasicRateInterfaceInteropGroup_ObjectIdentity = ObjectIdentity
basicRateInterfaceInteropGroup = _BasicRateInterfaceInteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000)
)
_BasicRateInterfaceInteropTable_Object = MibTable
basicRateInterfaceInteropTable = _BasicRateInterfaceInteropTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100)
)
if mibBuilder.loadTexts:
    basicRateInterfaceInteropTable.setStatus("current")
_BasicRateInterfaceInteropEntry_Object = MibTableRow
basicRateInterfaceInteropEntry = _BasicRateInterfaceInteropEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1)
)
basicRateInterfaceInteropEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "basicRateInterfaceInteropName"),
)
if mibBuilder.loadTexts:
    basicRateInterfaceInteropEntry.setStatus("current")
_BasicRateInterfaceInteropName_Type = OctetString
_BasicRateInterfaceInteropName_Object = MibTableColumn
basicRateInterfaceInteropName = _BasicRateInterfaceInteropName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 100),
    _BasicRateInterfaceInteropName_Type()
)
basicRateInterfaceInteropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropName.setStatus("current")


class _BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropProgressIndicatorInSetupEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Object = MibTableColumn
basicRateInterfaceInteropProgressIndicatorInSetupEnable = _BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 200),
    _BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Type()
)
basicRateInterfaceInteropProgressIndicatorInSetupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropProgressIndicatorInSetupEnable.setStatus("current")


class _BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropProgressIndicatorInSetupAckEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object = MibTableColumn
basicRateInterfaceInteropProgressIndicatorInSetupAckEnable = _BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 300),
    _BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type()
)
basicRateInterfaceInteropProgressIndicatorInSetupAckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropProgressIndicatorInSetupAckEnable.setStatus("current")


class _BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object = MibTableColumn
basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable = _BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 400),
    _BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type()
)
basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setStatus("current")


class _BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropProgressIndicatorInProgressEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Object = MibTableColumn
basicRateInterfaceInteropProgressIndicatorInProgressEnable = _BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 450),
    _BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Type()
)
basicRateInterfaceInteropProgressIndicatorInProgressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropProgressIndicatorInProgressEnable.setStatus("current")


class _BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropProgressIndicatorInAlertingEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Object = MibTableColumn
basicRateInterfaceInteropProgressIndicatorInAlertingEnable = _BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 500),
    _BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Type()
)
basicRateInterfaceInteropProgressIndicatorInAlertingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropProgressIndicatorInAlertingEnable.setStatus("current")


class _BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropProgressIndicatorInConnectEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Object = MibTableColumn
basicRateInterfaceInteropProgressIndicatorInConnectEnable = _BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 600),
    _BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Type()
)
basicRateInterfaceInteropProgressIndicatorInConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropProgressIndicatorInConnectEnable.setStatus("current")


class _BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Type(Unsigned32):
    """Custom type basicRateInterfaceInteropMaximumFacilityWaitingDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Type.__name__ = "Unsigned32"
_BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Object = MibTableColumn
basicRateInterfaceInteropMaximumFacilityWaitingDelay = _BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 700),
    _BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Type()
)
basicRateInterfaceInteropMaximumFacilityWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropMaximumFacilityWaitingDelay.setStatus("current")


class _BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropUseImplicitInbandInfoEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Object = MibTableColumn
basicRateInterfaceInteropUseImplicitInbandInfoEnable = _BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 800),
    _BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Type()
)
basicRateInterfaceInteropUseImplicitInbandInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropUseImplicitInbandInfoEnable.setStatus("current")


class _BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Type(MxEnableState):
    """Custom type basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable based on MxEnableState"""
    defaultValue = 1


_BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Type.__name__ = "MxEnableState"
_BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Object = MibTableColumn
basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable = _BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 300, 50000, 100, 1, 900),
    _BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Type()
)
basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable.setStatus("current")
_BearerChannelGroup_ObjectIdentity = ObjectIdentity
bearerChannelGroup = _BearerChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 400)
)
_BearerChannelInfoTable_Object = MibTable
bearerChannelInfoTable = _BearerChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 400, 100)
)
if mibBuilder.loadTexts:
    bearerChannelInfoTable.setStatus("current")
_BearerChannelInfoEntry_Object = MibTableRow
bearerChannelInfoEntry = _BearerChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 400, 100, 1)
)
bearerChannelInfoEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "bearerChannelInfoIndex"),
)
if mibBuilder.loadTexts:
    bearerChannelInfoEntry.setStatus("current")
_BearerChannelInfoIndex_Type = OctetString
_BearerChannelInfoIndex_Object = MibTableColumn
bearerChannelInfoIndex = _BearerChannelInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 400, 100, 1, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 400, 100, 1, 200),
    _BearerChannelInfoState_Type()
)
bearerChannelInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerChannelInfoState.setStatus("current")
_SignalingChannelGroup_ObjectIdentity = ObjectIdentity
signalingChannelGroup = _SignalingChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500)
)
_SignalingChannelTable_Object = MibTable
signalingChannelTable = _SignalingChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100)
)
if mibBuilder.loadTexts:
    signalingChannelTable.setStatus("current")
_SignalingChannelEntry_Object = MibTableRow
signalingChannelEntry = _SignalingChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1)
)
signalingChannelEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "signalingChannelInterfaceName"),
)
if mibBuilder.loadTexts:
    signalingChannelEntry.setStatus("current")
_SignalingChannelInterfaceName_Type = OctetString
_SignalingChannelInterfaceName_Object = MibTableColumn
signalingChannelInterfaceName = _SignalingChannelInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 100),
    _SignalingChannelInterfaceName_Type()
)
signalingChannelInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingChannelInterfaceName.setStatus("current")


class _SignalingChannelProtocol_Type(Integer32):
    """Custom type signalingChannelProtocol based on Integer32"""
    defaultValue = 100

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
        *(("dss1", 100),
          ("dms100", 200),
          ("ni2", 300),
          ("ess5", 400),
          ("qSig", 500))
    )


_SignalingChannelProtocol_Type.__name__ = "Integer32"
_SignalingChannelProtocol_Object = MibTableColumn
signalingChannelProtocol = _SignalingChannelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 200),
    _SignalingChannelProtocol_Type()
)
signalingChannelProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelProtocol.setStatus("current")


class _SignalingChannelFacilityServicesEnable_Type(MxEnableState):
    """Custom type signalingChannelFacilityServicesEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelFacilityServicesEnable_Type.__name__ = "MxEnableState"
_SignalingChannelFacilityServicesEnable_Object = MibTableColumn
signalingChannelFacilityServicesEnable = _SignalingChannelFacilityServicesEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 250),
    _SignalingChannelFacilityServicesEnable_Type()
)
signalingChannelFacilityServicesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelFacilityServicesEnable.setStatus("current")


class _SignalingChannelColpEnable_Type(MxEnableState):
    """Custom type signalingChannelColpEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelColpEnable_Type.__name__ = "MxEnableState"
_SignalingChannelColpEnable_Object = MibTableColumn
signalingChannelColpEnable = _SignalingChannelColpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 300),
    _SignalingChannelColpEnable_Type()
)
signalingChannelColpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelColpEnable.setStatus("current")


class _SignalingChannelColrEnable_Type(MxEnableState):
    """Custom type signalingChannelColrEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelColrEnable_Type.__name__ = "MxEnableState"
_SignalingChannelColrEnable_Object = MibTableColumn
signalingChannelColrEnable = _SignalingChannelColrEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 400),
    _SignalingChannelColrEnable_Type()
)
signalingChannelColrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelColrEnable.setStatus("current")


class _SignalingChannelColrOverrideEnable_Type(MxEnableState):
    """Custom type signalingChannelColrOverrideEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelColrOverrideEnable_Type.__name__ = "MxEnableState"
_SignalingChannelColrOverrideEnable_Object = MibTableColumn
signalingChannelColrOverrideEnable = _SignalingChannelColrOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 500),
    _SignalingChannelColrOverrideEnable_Type()
)
signalingChannelColrOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelColrOverrideEnable.setStatus("current")


class _SignalingChannelConpEnable_Type(MxEnableState):
    """Custom type signalingChannelConpEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelConpEnable_Type.__name__ = "MxEnableState"
_SignalingChannelConpEnable_Object = MibTableColumn
signalingChannelConpEnable = _SignalingChannelConpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 510),
    _SignalingChannelConpEnable_Type()
)
signalingChannelConpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelConpEnable.setStatus("current")


class _SignalingChannelOutgoingNotifyEnable_Type(MxEnableState):
    """Custom type signalingChannelOutgoingNotifyEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelOutgoingNotifyEnable_Type.__name__ = "MxEnableState"
_SignalingChannelOutgoingNotifyEnable_Object = MibTableColumn
signalingChannelOutgoingNotifyEnable = _SignalingChannelOutgoingNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 600),
    _SignalingChannelOutgoingNotifyEnable_Type()
)
signalingChannelOutgoingNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelOutgoingNotifyEnable.setStatus("current")


class _SignalingChannelAcceptedProgressCauses_Type(OctetString):
    """Custom type signalingChannelAcceptedProgressCauses based on OctetString"""
    defaultValue = OctetString("1-127")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SignalingChannelAcceptedProgressCauses_Type.__name__ = "OctetString"
_SignalingChannelAcceptedProgressCauses_Object = MibTableColumn
signalingChannelAcceptedProgressCauses = _SignalingChannelAcceptedProgressCauses_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 700),
    _SignalingChannelAcceptedProgressCauses_Type()
)
signalingChannelAcceptedProgressCauses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelAcceptedProgressCauses.setStatus("current")


class _SignalingChannelAutoCancelTimeout_Type(Unsigned32):
    """Custom type signalingChannelAutoCancelTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_SignalingChannelAutoCancelTimeout_Type.__name__ = "Unsigned32"
_SignalingChannelAutoCancelTimeout_Object = MibTableColumn
signalingChannelAutoCancelTimeout = _SignalingChannelAutoCancelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 800),
    _SignalingChannelAutoCancelTimeout_Type()
)
signalingChannelAutoCancelTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelAutoCancelTimeout.setStatus("current")


class _SignalingChannelDateTimeIeSupport_Type(Integer32):
    """Custom type signalingChannelDateTimeIeSupport based on Integer32"""
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
        *(("none", 100),
          ("localTime", 200),
          ("utc", 300))
    )


_SignalingChannelDateTimeIeSupport_Type.__name__ = "Integer32"
_SignalingChannelDateTimeIeSupport_Object = MibTableColumn
signalingChannelDateTimeIeSupport = _SignalingChannelDateTimeIeSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 900),
    _SignalingChannelDateTimeIeSupport_Type()
)
signalingChannelDateTimeIeSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDateTimeIeSupport.setStatus("current")


class _SignalingChannelMaintenanceServiceCallTermination_Type(Integer32):
    """Custom type signalingChannelMaintenanceServiceCallTermination based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("graceful", 100),
          ("abrupt", 200))
    )


_SignalingChannelMaintenanceServiceCallTermination_Type.__name__ = "Integer32"
_SignalingChannelMaintenanceServiceCallTermination_Object = MibTableColumn
signalingChannelMaintenanceServiceCallTermination = _SignalingChannelMaintenanceServiceCallTermination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10000),
    _SignalingChannelMaintenanceServiceCallTermination_Type()
)
signalingChannelMaintenanceServiceCallTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelMaintenanceServiceCallTermination.setStatus("current")


class _SignalingChannelLinkEstablishment_Type(Integer32):
    """Custom type signalingChannelLinkEstablishment based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("onDemand", 100),
          ("permanent", 200))
    )


_SignalingChannelLinkEstablishment_Type.__name__ = "Integer32"
_SignalingChannelLinkEstablishment_Object = MibTableColumn
signalingChannelLinkEstablishment = _SignalingChannelLinkEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10100),
    _SignalingChannelLinkEstablishment_Type()
)
signalingChannelLinkEstablishment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelLinkEstablishment.setStatus("current")


class _SignalingChannelLinkEstablishmentTimer_Type(Unsigned32):
    """Custom type signalingChannelLinkEstablishmentTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_SignalingChannelLinkEstablishmentTimer_Type.__name__ = "Unsigned32"
_SignalingChannelLinkEstablishmentTimer_Object = MibTableColumn
signalingChannelLinkEstablishmentTimer = _SignalingChannelLinkEstablishmentTimer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10110),
    _SignalingChannelLinkEstablishmentTimer_Type()
)
signalingChannelLinkEstablishmentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelLinkEstablishmentTimer.setStatus("current")


class _SignalingChannelAcceptedStatusCauses_Type(OctetString):
    """Custom type signalingChannelAcceptedStatusCauses based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SignalingChannelAcceptedStatusCauses_Type.__name__ = "OctetString"
_SignalingChannelAcceptedStatusCauses_Object = MibTableColumn
signalingChannelAcceptedStatusCauses = _SignalingChannelAcceptedStatusCauses_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10200),
    _SignalingChannelAcceptedStatusCauses_Type()
)
signalingChannelAcceptedStatusCauses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelAcceptedStatusCauses.setStatus("current")


class _SignalingChannelSendIsdnProgress_Type(Integer32):
    """Custom type signalingChannelSendIsdnProgress based on Integer32"""
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
        *(("sendAll", 100),
          ("sendInband", 200),
          ("sendAlerting", 300))
    )


_SignalingChannelSendIsdnProgress_Type.__name__ = "Integer32"
_SignalingChannelSendIsdnProgress_Object = MibTableColumn
signalingChannelSendIsdnProgress = _SignalingChannelSendIsdnProgress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10300),
    _SignalingChannelSendIsdnProgress_Type()
)
signalingChannelSendIsdnProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelSendIsdnProgress.setStatus("current")


class _SignalingChannelSendProgressIndicatorIE_Type(Integer32):
    """Custom type signalingChannelSendProgressIndicatorIE based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("sendAll", 100),
          ("sendInbandOnly", 200))
    )


_SignalingChannelSendProgressIndicatorIE_Type.__name__ = "Integer32"
_SignalingChannelSendProgressIndicatorIE_Object = MibTableColumn
signalingChannelSendProgressIndicatorIE = _SignalingChannelSendProgressIndicatorIE_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10400),
    _SignalingChannelSendProgressIndicatorIE_Type()
)
signalingChannelSendProgressIndicatorIE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelSendProgressIndicatorIE.setStatus("current")


class _SignalingChannelAocESupport_Type(Integer32):
    """Custom type signalingChannelAocESupport based on Integer32"""
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
        *(("no", 100),
          ("transparent", 200),
          ("automatic", 300),
          ("explicit", 400))
    )


_SignalingChannelAocESupport_Type.__name__ = "Integer32"
_SignalingChannelAocESupport_Object = MibTableColumn
signalingChannelAocESupport = _SignalingChannelAocESupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10600),
    _SignalingChannelAocESupport_Type()
)
signalingChannelAocESupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelAocESupport.setStatus("current")


class _SignalingChannelAocDSupport_Type(Integer32):
    """Custom type signalingChannelAocDSupport based on Integer32"""
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
        *(("no", 100),
          ("transparent", 200),
          ("automatic", 300),
          ("explicit", 400))
    )


_SignalingChannelAocDSupport_Type.__name__ = "Integer32"
_SignalingChannelAocDSupport_Object = MibTableColumn
signalingChannelAocDSupport = _SignalingChannelAocDSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10620),
    _SignalingChannelAocDSupport_Type()
)
signalingChannelAocDSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelAocDSupport.setStatus("current")


class _SignalingChannelCallReroutingBehavior_Type(Integer32):
    """Custom type signalingChannelCallReroutingBehavior based on Integer32"""
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
        *(("unsupported", 100),
          ("relayReroute", 200),
          ("processLocally", 300))
    )


_SignalingChannelCallReroutingBehavior_Type.__name__ = "Integer32"
_SignalingChannelCallReroutingBehavior_Object = MibTableColumn
signalingChannelCallReroutingBehavior = _SignalingChannelCallReroutingBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10700),
    _SignalingChannelCallReroutingBehavior_Type()
)
signalingChannelCallReroutingBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelCallReroutingBehavior.setStatus("current")


class _SignalingChannelDefaultCallingTon_Type(Integer32):
    """Custom type signalingChannelDefaultCallingTon based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 100),
          ("international", 200),
          ("national", 300),
          ("networkSpecific", 400),
          ("subscriber", 500),
          ("abbreviated", 600))
    )


_SignalingChannelDefaultCallingTon_Type.__name__ = "Integer32"
_SignalingChannelDefaultCallingTon_Object = MibTableColumn
signalingChannelDefaultCallingTon = _SignalingChannelDefaultCallingTon_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10800),
    _SignalingChannelDefaultCallingTon_Type()
)
signalingChannelDefaultCallingTon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDefaultCallingTon.setStatus("current")


class _SignalingChannelDefaultCallingNpi_Type(Integer32):
    """Custom type signalingChannelDefaultCallingNpi based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 100),
          ("isdnTelephony", 200),
          ("data", 300),
          ("telex", 400),
          ("nationalStandard", 500),
          ("private", 600))
    )


_SignalingChannelDefaultCallingNpi_Type.__name__ = "Integer32"
_SignalingChannelDefaultCallingNpi_Object = MibTableColumn
signalingChannelDefaultCallingNpi = _SignalingChannelDefaultCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 10900),
    _SignalingChannelDefaultCallingNpi_Type()
)
signalingChannelDefaultCallingNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDefaultCallingNpi.setStatus("current")


class _SignalingChannelDefaultCallingPi_Type(Integer32):
    """Custom type signalingChannelDefaultCallingPi based on Integer32"""
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
        *(("presentationAllowed", 100),
          ("presentationRestricted", 200),
          ("notAvailable", 300))
    )


_SignalingChannelDefaultCallingPi_Type.__name__ = "Integer32"
_SignalingChannelDefaultCallingPi_Object = MibTableColumn
signalingChannelDefaultCallingPi = _SignalingChannelDefaultCallingPi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11000),
    _SignalingChannelDefaultCallingPi_Type()
)
signalingChannelDefaultCallingPi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDefaultCallingPi.setStatus("current")


class _SignalingChannelDefaultCallingSi_Type(Integer32):
    """Custom type signalingChannelDefaultCallingSi based on Integer32"""
    defaultValue = 500

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
        *(("userProvidedNotScreened", 100),
          ("userProvidedVerifiedAndPassed", 200),
          ("userProvidedVerifiedAndFailed", 300),
          ("networkProvided", 400),
          ("contextDependent", 500))
    )


_SignalingChannelDefaultCallingSi_Type.__name__ = "Integer32"
_SignalingChannelDefaultCallingSi_Object = MibTableColumn
signalingChannelDefaultCallingSi = _SignalingChannelDefaultCallingSi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11100),
    _SignalingChannelDefaultCallingSi_Type()
)
signalingChannelDefaultCallingSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDefaultCallingSi.setStatus("current")


class _SignalingChannelDefaultCalledTon_Type(Integer32):
    """Custom type signalingChannelDefaultCalledTon based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 100),
          ("international", 200),
          ("national", 300),
          ("networkSpecific", 400),
          ("subscriber", 500),
          ("abbreviated", 600))
    )


_SignalingChannelDefaultCalledTon_Type.__name__ = "Integer32"
_SignalingChannelDefaultCalledTon_Object = MibTableColumn
signalingChannelDefaultCalledTon = _SignalingChannelDefaultCalledTon_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11200),
    _SignalingChannelDefaultCalledTon_Type()
)
signalingChannelDefaultCalledTon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDefaultCalledTon.setStatus("current")


class _SignalingChannelDefaultCalledNpi_Type(Integer32):
    """Custom type signalingChannelDefaultCalledNpi based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 100),
          ("isdnTelephony", 200),
          ("data", 300),
          ("telex", 400),
          ("nationalStandard", 500),
          ("private", 600))
    )


_SignalingChannelDefaultCalledNpi_Type.__name__ = "Integer32"
_SignalingChannelDefaultCalledNpi_Object = MibTableColumn
signalingChannelDefaultCalledNpi = _SignalingChannelDefaultCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11300),
    _SignalingChannelDefaultCalledNpi_Type()
)
signalingChannelDefaultCalledNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelDefaultCalledNpi.setStatus("current")


class _SignalingChannelUserSuspendedHandling_Type(Integer32):
    """Custom type signalingChannelUserSuspendedHandling based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 100),
          ("disconnect", 200))
    )


_SignalingChannelUserSuspendedHandling_Type.__name__ = "Integer32"
_SignalingChannelUserSuspendedHandling_Object = MibTableColumn
signalingChannelUserSuspendedHandling = _SignalingChannelUserSuspendedHandling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11400),
    _SignalingChannelUserSuspendedHandling_Type()
)
signalingChannelUserSuspendedHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelUserSuspendedHandling.setStatus("current")


class _SignalingChannelStrictHandlingErrorConditions_Type(MxEnableState):
    """Custom type signalingChannelStrictHandlingErrorConditions based on MxEnableState"""
    defaultValue = 0


_SignalingChannelStrictHandlingErrorConditions_Type.__name__ = "MxEnableState"
_SignalingChannelStrictHandlingErrorConditions_Object = MibTableColumn
signalingChannelStrictHandlingErrorConditions = _SignalingChannelStrictHandlingErrorConditions_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11500),
    _SignalingChannelStrictHandlingErrorConditions_Type()
)
signalingChannelStrictHandlingErrorConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelStrictHandlingErrorConditions.setStatus("current")


class _SignalingChannelMcidEnable_Type(MxEnableState):
    """Custom type signalingChannelMcidEnable based on MxEnableState"""
    defaultValue = 0


_SignalingChannelMcidEnable_Type.__name__ = "MxEnableState"
_SignalingChannelMcidEnable_Object = MibTableColumn
signalingChannelMcidEnable = _SignalingChannelMcidEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 100, 1, 11600),
    _SignalingChannelMcidEnable_Type()
)
signalingChannelMcidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelMcidEnable.setStatus("current")
_SignalingChannelInfoTable_Object = MibTable
signalingChannelInfoTable = _SignalingChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 200)
)
if mibBuilder.loadTexts:
    signalingChannelInfoTable.setStatus("current")
_SignalingChannelInfoEntry_Object = MibTableRow
signalingChannelInfoEntry = _SignalingChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 200, 1)
)
signalingChannelInfoEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "signalingChannelInfoInterfaceName"),
)
if mibBuilder.loadTexts:
    signalingChannelInfoEntry.setStatus("current")
_SignalingChannelInfoInterfaceName_Type = OctetString
_SignalingChannelInfoInterfaceName_Object = MibTableColumn
signalingChannelInfoInterfaceName = _SignalingChannelInfoInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 200, 1, 100),
    _SignalingChannelInfoInterfaceName_Type()
)
signalingChannelInfoInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingChannelInfoInterfaceName.setStatus("current")


class _SignalingChannelInfoState_Type(Integer32):
    """Custom type signalingChannelInfoState based on Integer32"""
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


_SignalingChannelInfoState_Type.__name__ = "Integer32"
_SignalingChannelInfoState_Object = MibTableColumn
signalingChannelInfoState = _SignalingChannelInfoState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 200, 1, 200),
    _SignalingChannelInfoState_Type()
)
signalingChannelInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingChannelInfoState.setStatus("current")
_SignalingChannelInteropGroup_ObjectIdentity = ObjectIdentity
signalingChannelInteropGroup = _SignalingChannelInteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000)
)
_SignalingChannelInteropTable_Object = MibTable
signalingChannelInteropTable = _SignalingChannelInteropTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100)
)
if mibBuilder.loadTexts:
    signalingChannelInteropTable.setStatus("current")
_SignalingChannelInteropEntry_Object = MibTableRow
signalingChannelInteropEntry = _SignalingChannelInteropEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1)
)
signalingChannelInteropEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "signalingChannelInteropInterfaceName"),
)
if mibBuilder.loadTexts:
    signalingChannelInteropEntry.setStatus("current")
_SignalingChannelInteropInterfaceName_Type = OctetString
_SignalingChannelInteropInterfaceName_Object = MibTableColumn
signalingChannelInteropInterfaceName = _SignalingChannelInteropInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1, 100),
    _SignalingChannelInteropInterfaceName_Type()
)
signalingChannelInteropInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingChannelInteropInterfaceName.setStatus("current")


class _SignalingChannelInteropCallProceedingDelay_Type(Unsigned32):
    """Custom type signalingChannelInteropCallProceedingDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_SignalingChannelInteropCallProceedingDelay_Type.__name__ = "Unsigned32"
_SignalingChannelInteropCallProceedingDelay_Object = MibTableColumn
signalingChannelInteropCallProceedingDelay = _SignalingChannelInteropCallProceedingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1, 200),
    _SignalingChannelInteropCallProceedingDelay_Type()
)
signalingChannelInteropCallProceedingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelInteropCallProceedingDelay.setStatus("current")


class _SignalingChannelInteropCallingNameDelivery_Type(Integer32):
    """Custom type signalingChannelInteropCallingNameDelivery based on Integer32"""
    defaultValue = 400

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
        *(("facilityIe", 100),
          ("displayIe", 200),
          ("userUserIe", 300),
          ("signalingProtocol", 400))
    )


_SignalingChannelInteropCallingNameDelivery_Type.__name__ = "Integer32"
_SignalingChannelInteropCallingNameDelivery_Object = MibTableColumn
signalingChannelInteropCallingNameDelivery = _SignalingChannelInteropCallingNameDelivery_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1, 300),
    _SignalingChannelInteropCallingNameDelivery_Type()
)
signalingChannelInteropCallingNameDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelInteropCallingNameDelivery.setStatus("current")


class _SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Type(MxEnableState):
    """Custom type signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream based on MxEnableState"""
    defaultValue = 0


_SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Type.__name__ = "MxEnableState"
_SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Object = MibTableColumn
signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream = _SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1, 500),
    _SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Type()
)
signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream.setStatus("current")


class _SignalingChannelInteropInteropConsecutiveChannelIndicator_Type(MxEnableState):
    """Custom type signalingChannelInteropInteropConsecutiveChannelIndicator based on MxEnableState"""
    defaultValue = 0


_SignalingChannelInteropInteropConsecutiveChannelIndicator_Type.__name__ = "MxEnableState"
_SignalingChannelInteropInteropConsecutiveChannelIndicator_Object = MibTableColumn
signalingChannelInteropInteropConsecutiveChannelIndicator = _SignalingChannelInteropInteropConsecutiveChannelIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1, 600),
    _SignalingChannelInteropInteropConsecutiveChannelIndicator_Type()
)
signalingChannelInteropInteropConsecutiveChannelIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelInteropInteropConsecutiveChannelIndicator.setStatus("current")


class _SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Type(MxEnableState):
    """Custom type signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry based on MxEnableState"""
    defaultValue = 1


_SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Type.__name__ = "MxEnableState"
_SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Object = MibTableColumn
signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry = _SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 500, 50000, 100, 1, 700),
    _SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Type()
)
signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry.setStatus("current")
_PhysicalGroup_ObjectIdentity = ObjectIdentity
physicalGroup = _PhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600)
)
_PhysicalLinkInfoTable_Object = MibTable
physicalLinkInfoTable = _PhysicalLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 100)
)
if mibBuilder.loadTexts:
    physicalLinkInfoTable.setStatus("current")
_PhysicalLinkInfoEntry_Object = MibTableRow
physicalLinkInfoEntry = _PhysicalLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 100, 1)
)
physicalLinkInfoEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "physicalLinkInfoInterfaceName"),
)
if mibBuilder.loadTexts:
    physicalLinkInfoEntry.setStatus("current")
_PhysicalLinkInfoInterfaceName_Type = OctetString
_PhysicalLinkInfoInterfaceName_Object = MibTableColumn
physicalLinkInfoInterfaceName = _PhysicalLinkInfoInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 100, 1, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 100, 1, 200),
    _PhysicalLinkInfoState_Type()
)
physicalLinkInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInfoState.setStatus("current")
_PhysicalLinkTable_Object = MibTable
physicalLinkTable = _PhysicalLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 200)
)
if mibBuilder.loadTexts:
    physicalLinkTable.setStatus("current")
_PhysicalLinkEntry_Object = MibTableRow
physicalLinkEntry = _PhysicalLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 200, 1)
)
physicalLinkEntry.setIndexNames(
    (0, "MX-ISDN-MIB", "physicalLinkInterfaceName"),
)
if mibBuilder.loadTexts:
    physicalLinkEntry.setStatus("current")
_PhysicalLinkInterfaceName_Type = OctetString
_PhysicalLinkInterfaceName_Object = MibTableColumn
physicalLinkInterfaceName = _PhysicalLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 200, 1, 100),
    _PhysicalLinkInterfaceName_Type()
)
physicalLinkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInterfaceName.setStatus("current")


class _PhysicalLinkL1TimerT3_Type(Unsigned32):
    """Custom type physicalLinkL1TimerT3 based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_PhysicalLinkL1TimerT3_Type.__name__ = "Unsigned32"
_PhysicalLinkL1TimerT3_Object = MibTableColumn
physicalLinkL1TimerT3 = _PhysicalLinkL1TimerT3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 200, 1, 200),
    _PhysicalLinkL1TimerT3_Type()
)
physicalLinkL1TimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkL1TimerT3.setStatus("current")


class _PhysicalLinkClockMode_Type(Integer32):
    """Custom type physicalLinkClockMode based on Integer32"""
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


_PhysicalLinkClockMode_Type.__name__ = "Integer32"
_PhysicalLinkClockMode_Object = MibTableColumn
physicalLinkClockMode = _PhysicalLinkClockMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 200, 1, 300),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 600, 200, 1, 400),
    _PhysicalLinkMonitorLinkStateEnable_Type()
)
physicalLinkMonitorLinkStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkMonitorLinkStateEnable.setStatus("current")
_AutoConfigure_ObjectIdentity = ObjectIdentity
autoConfigure = _AutoConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 700)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 700, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 700, 200),
    _LastAutoConfigureResult_Type()
)
lastAutoConfigureResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAutoConfigureResult.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1850, 1, 60020, 100),
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
    "MX-ISDN-MIB",
    **{"isdnMIB": isdnMIB,
       "isdnMIBObjects": isdnMIBObjects,
       "primaryRateInterfaceGroup": primaryRateInterfaceGroup,
       "primaryRateInterfaceTable": primaryRateInterfaceTable,
       "primaryRateInterfaceEntry": primaryRateInterfaceEntry,
       "primaryRateInterfaceName": primaryRateInterfaceName,
       "primaryRateInterfaceEndpointType": primaryRateInterfaceEndpointType,
       "primaryRateInterfacePortPinout": primaryRateInterfacePortPinout,
       "primaryRateInterfaceLineCoding": primaryRateInterfaceLineCoding,
       "primaryRateInterfaceLineFraming": primaryRateInterfaceLineFraming,
       "primaryRateInterfaceNetworkLocation": primaryRateInterfaceNetworkLocation,
       "primaryRateInterfacePreferredEncodingScheme": primaryRateInterfacePreferredEncodingScheme,
       "primaryRateInterfaceFallbackEncodingScheme": primaryRateInterfaceFallbackEncodingScheme,
       "primaryRateInterfaceChannelRange": primaryRateInterfaceChannelRange,
       "primaryRateInterfaceIncomingChannelRange": primaryRateInterfaceIncomingChannelRange,
       "primaryRateInterfaceOutgoingChannelRange": primaryRateInterfaceOutgoingChannelRange,
       "primaryRateInterfaceChannelAllocationStrategy": primaryRateInterfaceChannelAllocationStrategy,
       "primaryRateInterfaceMaxActiveCalls": primaryRateInterfaceMaxActiveCalls,
       "primaryRateInterfaceSignalInformationElementEnable": primaryRateInterfaceSignalInformationElementEnable,
       "primaryRateInterfaceInbandToneGenerationEnable": primaryRateInterfaceInbandToneGenerationEnable,
       "primaryRateInterfaceInbandDtmfDialingEnable": primaryRateInterfaceInbandDtmfDialingEnable,
       "primaryRateInterfaceOverlapDialingEnable": primaryRateInterfaceOverlapDialingEnable,
       "primaryRateInterfaceCallingNameMaxLength": primaryRateInterfaceCallingNameMaxLength,
       "primaryRateInterfaceExclusiveBChannelSelectionEnable": primaryRateInterfaceExclusiveBChannelSelectionEnable,
       "primaryRateInterfaceSendingCompleteEnable": primaryRateInterfaceSendingCompleteEnable,
       "primaryRateInterfaceClipEnable": primaryRateInterfaceClipEnable,
       "primaryRateInterfaceClirEnable": primaryRateInterfaceClirEnable,
       "primaryRateInterfaceClirOverrideEnable": primaryRateInterfaceClirOverrideEnable,
       "primaryRateInterfaceSendRestartOnStartupEnable": primaryRateInterfaceSendRestartOnStartupEnable,
       "primaryRateInterfaceInteropGroup": primaryRateInterfaceInteropGroup,
       "primaryRateInterfaceInteropTable": primaryRateInterfaceInteropTable,
       "primaryRateInterfaceInteropEntry": primaryRateInterfaceInteropEntry,
       "primaryRateInterfaceInteropName": primaryRateInterfaceInteropName,
       "primaryRateInterfaceInteropProgressIndicatorInSetupEnable": primaryRateInterfaceInteropProgressIndicatorInSetupEnable,
       "primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable": primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable,
       "primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable": primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable,
       "primaryRateInterfaceInteropProgressIndicatorInProgressEnable": primaryRateInterfaceInteropProgressIndicatorInProgressEnable,
       "primaryRateInterfaceInteropProgressIndicatorInAlertingEnable": primaryRateInterfaceInteropProgressIndicatorInAlertingEnable,
       "primaryRateInterfaceInteropProgressIndicatorInConnectEnable": primaryRateInterfaceInteropProgressIndicatorInConnectEnable,
       "primaryRateInterfaceInteropMaximumFacilityWaitingDelay": primaryRateInterfaceInteropMaximumFacilityWaitingDelay,
       "primaryRateInterfaceInteropUseImplicitInbandInfoEnable": primaryRateInterfaceInteropUseImplicitInbandInfoEnable,
       "basicRateInterfaceGroup": basicRateInterfaceGroup,
       "basicRateInterfaceTable": basicRateInterfaceTable,
       "basicRateInterfaceEntry": basicRateInterfaceEntry,
       "basicRateInterfaceName": basicRateInterfaceName,
       "basicRateInterfaceEndpointType": basicRateInterfaceEndpointType,
       "basicRateInterfaceConnectionType": basicRateInterfaceConnectionType,
       "basicRateInterfaceNetworkLocation": basicRateInterfaceNetworkLocation,
       "basicRateInterfacePreferredEncodingScheme": basicRateInterfacePreferredEncodingScheme,
       "basicRateInterfaceFallbackEncodingScheme": basicRateInterfaceFallbackEncodingScheme,
       "basicRateInterfaceChannelAllocationStrategy": basicRateInterfaceChannelAllocationStrategy,
       "basicRateInterfaceMaxActiveCalls": basicRateInterfaceMaxActiveCalls,
       "basicRateInterfaceSignalInformationElementEnable": basicRateInterfaceSignalInformationElementEnable,
       "basicRateInterfaceInbandToneGenerationEnable": basicRateInterfaceInbandToneGenerationEnable,
       "basicRateInterfaceInbandDtmfDialingEnable": basicRateInterfaceInbandDtmfDialingEnable,
       "basicRateInterfaceOverlapDialingEnable": basicRateInterfaceOverlapDialingEnable,
       "basicRateInterfaceCallingNameMaxLength": basicRateInterfaceCallingNameMaxLength,
       "basicRateInterfaceExclusiveBChannelSelectionEnable": basicRateInterfaceExclusiveBChannelSelectionEnable,
       "basicRateInterfaceSendingCompleteEnable": basicRateInterfaceSendingCompleteEnable,
       "basicRateInterfaceClipEnable": basicRateInterfaceClipEnable,
       "basicRateInterfaceClirEnable": basicRateInterfaceClirEnable,
       "basicRateInterfaceClirOverrideEnable": basicRateInterfaceClirOverrideEnable,
       "basicRateInterfaceSendRestartOnStartupEnable": basicRateInterfaceSendRestartOnStartupEnable,
       "basicRateInterfaceHookFlashKeypad": basicRateInterfaceHookFlashKeypad,
       "basicRateInterfaceKeypadReceptionTimeout": basicRateInterfaceKeypadReceptionTimeout,
       "basicRateInterfaceMsn": basicRateInterfaceMsn,
       "basicRateInterfaceMsn2": basicRateInterfaceMsn2,
       "basicRateInterfaceMsn3": basicRateInterfaceMsn3,
       "basicRateInterfaceTeiNegotiation": basicRateInterfaceTeiNegotiation,
       "basicRateInterfaceInteropGroup": basicRateInterfaceInteropGroup,
       "basicRateInterfaceInteropTable": basicRateInterfaceInteropTable,
       "basicRateInterfaceInteropEntry": basicRateInterfaceInteropEntry,
       "basicRateInterfaceInteropName": basicRateInterfaceInteropName,
       "basicRateInterfaceInteropProgressIndicatorInSetupEnable": basicRateInterfaceInteropProgressIndicatorInSetupEnable,
       "basicRateInterfaceInteropProgressIndicatorInSetupAckEnable": basicRateInterfaceInteropProgressIndicatorInSetupAckEnable,
       "basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable": basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable,
       "basicRateInterfaceInteropProgressIndicatorInProgressEnable": basicRateInterfaceInteropProgressIndicatorInProgressEnable,
       "basicRateInterfaceInteropProgressIndicatorInAlertingEnable": basicRateInterfaceInteropProgressIndicatorInAlertingEnable,
       "basicRateInterfaceInteropProgressIndicatorInConnectEnable": basicRateInterfaceInteropProgressIndicatorInConnectEnable,
       "basicRateInterfaceInteropMaximumFacilityWaitingDelay": basicRateInterfaceInteropMaximumFacilityWaitingDelay,
       "basicRateInterfaceInteropUseImplicitInbandInfoEnable": basicRateInterfaceInteropUseImplicitInbandInfoEnable,
       "basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable": basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable,
       "bearerChannelGroup": bearerChannelGroup,
       "bearerChannelInfoTable": bearerChannelInfoTable,
       "bearerChannelInfoEntry": bearerChannelInfoEntry,
       "bearerChannelInfoIndex": bearerChannelInfoIndex,
       "bearerChannelInfoState": bearerChannelInfoState,
       "signalingChannelGroup": signalingChannelGroup,
       "signalingChannelTable": signalingChannelTable,
       "signalingChannelEntry": signalingChannelEntry,
       "signalingChannelInterfaceName": signalingChannelInterfaceName,
       "signalingChannelProtocol": signalingChannelProtocol,
       "signalingChannelFacilityServicesEnable": signalingChannelFacilityServicesEnable,
       "signalingChannelColpEnable": signalingChannelColpEnable,
       "signalingChannelColrEnable": signalingChannelColrEnable,
       "signalingChannelColrOverrideEnable": signalingChannelColrOverrideEnable,
       "signalingChannelConpEnable": signalingChannelConpEnable,
       "signalingChannelOutgoingNotifyEnable": signalingChannelOutgoingNotifyEnable,
       "signalingChannelAcceptedProgressCauses": signalingChannelAcceptedProgressCauses,
       "signalingChannelAutoCancelTimeout": signalingChannelAutoCancelTimeout,
       "signalingChannelDateTimeIeSupport": signalingChannelDateTimeIeSupport,
       "signalingChannelMaintenanceServiceCallTermination": signalingChannelMaintenanceServiceCallTermination,
       "signalingChannelLinkEstablishment": signalingChannelLinkEstablishment,
       "signalingChannelLinkEstablishmentTimer": signalingChannelLinkEstablishmentTimer,
       "signalingChannelAcceptedStatusCauses": signalingChannelAcceptedStatusCauses,
       "signalingChannelSendIsdnProgress": signalingChannelSendIsdnProgress,
       "signalingChannelSendProgressIndicatorIE": signalingChannelSendProgressIndicatorIE,
       "signalingChannelAocESupport": signalingChannelAocESupport,
       "signalingChannelAocDSupport": signalingChannelAocDSupport,
       "signalingChannelCallReroutingBehavior": signalingChannelCallReroutingBehavior,
       "signalingChannelDefaultCallingTon": signalingChannelDefaultCallingTon,
       "signalingChannelDefaultCallingNpi": signalingChannelDefaultCallingNpi,
       "signalingChannelDefaultCallingPi": signalingChannelDefaultCallingPi,
       "signalingChannelDefaultCallingSi": signalingChannelDefaultCallingSi,
       "signalingChannelDefaultCalledTon": signalingChannelDefaultCalledTon,
       "signalingChannelDefaultCalledNpi": signalingChannelDefaultCalledNpi,
       "signalingChannelUserSuspendedHandling": signalingChannelUserSuspendedHandling,
       "signalingChannelStrictHandlingErrorConditions": signalingChannelStrictHandlingErrorConditions,
       "signalingChannelMcidEnable": signalingChannelMcidEnable,
       "signalingChannelInfoTable": signalingChannelInfoTable,
       "signalingChannelInfoEntry": signalingChannelInfoEntry,
       "signalingChannelInfoInterfaceName": signalingChannelInfoInterfaceName,
       "signalingChannelInfoState": signalingChannelInfoState,
       "signalingChannelInteropGroup": signalingChannelInteropGroup,
       "signalingChannelInteropTable": signalingChannelInteropTable,
       "signalingChannelInteropEntry": signalingChannelInteropEntry,
       "signalingChannelInteropInterfaceName": signalingChannelInteropInterfaceName,
       "signalingChannelInteropCallProceedingDelay": signalingChannelInteropCallProceedingDelay,
       "signalingChannelInteropCallingNameDelivery": signalingChannelInteropCallingNameDelivery,
       "signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream": signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream,
       "signalingChannelInteropInteropConsecutiveChannelIndicator": signalingChannelInteropInteropConsecutiveChannelIndicator,
       "signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry": signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry,
       "physicalGroup": physicalGroup,
       "physicalLinkInfoTable": physicalLinkInfoTable,
       "physicalLinkInfoEntry": physicalLinkInfoEntry,
       "physicalLinkInfoInterfaceName": physicalLinkInfoInterfaceName,
       "physicalLinkInfoState": physicalLinkInfoState,
       "physicalLinkTable": physicalLinkTable,
       "physicalLinkEntry": physicalLinkEntry,
       "physicalLinkInterfaceName": physicalLinkInterfaceName,
       "physicalLinkL1TimerT3": physicalLinkL1TimerT3,
       "physicalLinkClockMode": physicalLinkClockMode,
       "physicalLinkMonitorLinkStateEnable": physicalLinkMonitorLinkStateEnable,
       "autoConfigure": autoConfigure,
       "autoConfigureStatus": autoConfigureStatus,
       "lastAutoConfigureResult": lastAutoConfigureResult,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
