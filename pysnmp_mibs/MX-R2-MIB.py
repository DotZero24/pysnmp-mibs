# SNMP MIB module (MX-R2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-R2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:06 2025
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

r2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_R2MIBObjects_ObjectIdentity = ObjectIdentity
r2MIBObjects = _R2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1)
)
_R2Group_ObjectIdentity = ObjectIdentity
r2Group = _R2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100)
)
_R2Table_Object = MibTable
r2Table = _R2Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100)
)
if mibBuilder.loadTexts:
    r2Table.setStatus("current")
_R2Entry_Object = MibTableRow
r2Entry = _R2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1)
)
r2Entry.setIndexNames(
    (0, "MX-R2-MIB", "r2Name"),
)
if mibBuilder.loadTexts:
    r2Entry.setStatus("current")
_R2Name_Type = OctetString
_R2Name_Object = MibTableColumn
r2Name = _R2Name_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 100),
    _R2Name_Type()
)
r2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    r2Name.setStatus("current")


class _R2ChannelRange_Type(OctetString):
    """Custom type r2ChannelRange based on OctetString"""
    defaultValue = OctetString("1-30")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_R2ChannelRange_Type.__name__ = "OctetString"
_R2ChannelRange_Object = MibTableColumn
r2ChannelRange = _R2ChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 200),
    _R2ChannelRange_Type()
)
r2ChannelRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ChannelRange.setStatus("current")


class _R2ChannelAllocationStrategy_Type(Integer32):
    """Custom type r2ChannelAllocationStrategy based on Integer32"""
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


_R2ChannelAllocationStrategy_Type.__name__ = "Integer32"
_R2ChannelAllocationStrategy_Object = MibTableColumn
r2ChannelAllocationStrategy = _R2ChannelAllocationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 300),
    _R2ChannelAllocationStrategy_Type()
)
r2ChannelAllocationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ChannelAllocationStrategy.setStatus("current")


class _R2MaxActiveCalls_Type(Unsigned32):
    """Custom type r2MaxActiveCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_R2MaxActiveCalls_Type.__name__ = "Unsigned32"
_R2MaxActiveCalls_Object = MibTableColumn
r2MaxActiveCalls = _R2MaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 400),
    _R2MaxActiveCalls_Type()
)
r2MaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2MaxActiveCalls.setStatus("current")


class _R2EncodingScheme_Type(Integer32):
    """Custom type r2EncodingScheme based on Integer32"""
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


_R2EncodingScheme_Type.__name__ = "Integer32"
_R2EncodingScheme_Object = MibTableColumn
r2EncodingScheme = _R2EncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 500),
    _R2EncodingScheme_Type()
)
r2EncodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2EncodingScheme.setStatus("current")


class _R2LineSignaling_Type(Integer32):
    """Custom type r2LineSignaling based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("q4212BitsSignaling", 100)
    )


_R2LineSignaling_Type.__name__ = "Integer32"
_R2LineSignaling_Object = MibTableColumn
r2LineSignaling = _R2LineSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 600),
    _R2LineSignaling_Type()
)
r2LineSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2LineSignaling.setStatus("current")


class _R2IncomingDigitSignaling_Type(Integer32):
    """Custom type r2IncomingDigitSignaling based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mfcR2", 100),
          ("dtmfR2", 200))
    )


_R2IncomingDigitSignaling_Type.__name__ = "Integer32"
_R2IncomingDigitSignaling_Object = MibTableColumn
r2IncomingDigitSignaling = _R2IncomingDigitSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 750),
    _R2IncomingDigitSignaling_Type()
)
r2IncomingDigitSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2IncomingDigitSignaling.setStatus("current")


class _R2OutgoingDigitSignaling_Type(Integer32):
    """Custom type r2OutgoingDigitSignaling based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mfcR2", 100),
          ("dtmfR2", 200))
    )


_R2OutgoingDigitSignaling_Type.__name__ = "Integer32"
_R2OutgoingDigitSignaling_Object = MibTableColumn
r2OutgoingDigitSignaling = _R2OutgoingDigitSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 760),
    _R2OutgoingDigitSignaling_Type()
)
r2OutgoingDigitSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2OutgoingDigitSignaling.setStatus("current")


class _R2CountrySelection_Type(Integer32):
    """Custom type r2CountrySelection based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700)
        )
    )
    namedValues = NamedValues(
        *(("brazilR2", 100),
          ("mexicoR2", 200),
          ("argentinaR2", 300),
          ("saudiArabiaR2", 400),
          ("venezuelaR2", 500),
          ("philippinesR2", 600),
          ("iTUTR2", 700))
    )


_R2CountrySelection_Type.__name__ = "Integer32"
_R2CountrySelection_Object = MibTableColumn
r2CountrySelection = _R2CountrySelection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 800),
    _R2CountrySelection_Type()
)
r2CountrySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2CountrySelection.setStatus("current")


class _R2DigitAttenuation_Type(Unsigned32):
    """Custom type r2DigitAttenuation based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_R2DigitAttenuation_Type.__name__ = "Unsigned32"
_R2DigitAttenuation_Object = MibTableColumn
r2DigitAttenuation = _R2DigitAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 100, 1, 900),
    _R2DigitAttenuation_Type()
)
r2DigitAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitAttenuation.setStatus("current")
_R2SignalingVariantsTable_Object = MibTable
r2SignalingVariantsTable = _R2SignalingVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200)
)
if mibBuilder.loadTexts:
    r2SignalingVariantsTable.setStatus("current")
_R2SignalingVariantsEntry_Object = MibTableRow
r2SignalingVariantsEntry = _R2SignalingVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1)
)
r2SignalingVariantsEntry.setIndexNames(
    (0, "MX-R2-MIB", "r2SignalingVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    r2SignalingVariantsEntry.setStatus("current")
_R2SignalingVariantsInterfaceName_Type = OctetString
_R2SignalingVariantsInterfaceName_Object = MibTableColumn
r2SignalingVariantsInterfaceName = _R2SignalingVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 100),
    _R2SignalingVariantsInterfaceName_Type()
)
r2SignalingVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    r2SignalingVariantsInterfaceName.setStatus("current")


class _R2SignalingVariantsOverrideDefault_Type(MxEnableState):
    """Custom type r2SignalingVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_R2SignalingVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_R2SignalingVariantsOverrideDefault_Object = MibTableColumn
r2SignalingVariantsOverrideDefault = _R2SignalingVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 300),
    _R2SignalingVariantsOverrideDefault_Type()
)
r2SignalingVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsOverrideDefault.setStatus("current")


class _R2SignalingVariantsBitsCD_Type(Integer32):
    """Custom type r2SignalingVariantsBitsCD based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_R2SignalingVariantsBitsCD_Type.__name__ = "Integer32"
_R2SignalingVariantsBitsCD_Object = MibTableColumn
r2SignalingVariantsBitsCD = _R2SignalingVariantsBitsCD_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 400),
    _R2SignalingVariantsBitsCD_Type()
)
r2SignalingVariantsBitsCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsBitsCD.setStatus("current")


class _R2SignalingVariantsDnisLength_Type(Unsigned32):
    """Custom type r2SignalingVariantsDnisLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_R2SignalingVariantsDnisLength_Type.__name__ = "Unsigned32"
_R2SignalingVariantsDnisLength_Object = MibTableColumn
r2SignalingVariantsDnisLength = _R2SignalingVariantsDnisLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 500),
    _R2SignalingVariantsDnisLength_Type()
)
r2SignalingVariantsDnisLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsDnisLength.setStatus("current")


class _R2SignalingVariantsAniLength_Type(Unsigned32):
    """Custom type r2SignalingVariantsAniLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_R2SignalingVariantsAniLength_Type.__name__ = "Unsigned32"
_R2SignalingVariantsAniLength_Object = MibTableColumn
r2SignalingVariantsAniLength = _R2SignalingVariantsAniLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 600),
    _R2SignalingVariantsAniLength_Type()
)
r2SignalingVariantsAniLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsAniLength.setStatus("current")


class _R2SignalingVariantsAniRequestEnable_Type(MxEnableState):
    """Custom type r2SignalingVariantsAniRequestEnable based on MxEnableState"""
    defaultValue = 1


_R2SignalingVariantsAniRequestEnable_Type.__name__ = "MxEnableState"
_R2SignalingVariantsAniRequestEnable_Object = MibTableColumn
r2SignalingVariantsAniRequestEnable = _R2SignalingVariantsAniRequestEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 700),
    _R2SignalingVariantsAniRequestEnable_Type()
)
r2SignalingVariantsAniRequestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsAniRequestEnable.setStatus("current")


class _R2SignalingVariantsSendAniRequestAfterDnisDigits_Type(Unsigned32):
    """Custom type r2SignalingVariantsSendAniRequestAfterDnisDigits based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_R2SignalingVariantsSendAniRequestAfterDnisDigits_Type.__name__ = "Unsigned32"
_R2SignalingVariantsSendAniRequestAfterDnisDigits_Object = MibTableColumn
r2SignalingVariantsSendAniRequestAfterDnisDigits = _R2SignalingVariantsSendAniRequestAfterDnisDigits_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 800),
    _R2SignalingVariantsSendAniRequestAfterDnisDigits_Type()
)
r2SignalingVariantsSendAniRequestAfterDnisDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsSendAniRequestAfterDnisDigits.setStatus("current")


class _R2SignalingVariantsCollectCallBlocked_Type(MxEnableState):
    """Custom type r2SignalingVariantsCollectCallBlocked based on MxEnableState"""
    defaultValue = 1


_R2SignalingVariantsCollectCallBlocked_Type.__name__ = "MxEnableState"
_R2SignalingVariantsCollectCallBlocked_Object = MibTableColumn
r2SignalingVariantsCollectCallBlocked = _R2SignalingVariantsCollectCallBlocked_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 900),
    _R2SignalingVariantsCollectCallBlocked_Type()
)
r2SignalingVariantsCollectCallBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsCollectCallBlocked.setStatus("current")


class _R2SignalingVariantsAniCategory_Type(Integer32):
    """Custom type r2SignalingVariantsAniCategory based on Integer32"""
    defaultValue = 100

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
              1100)
        )
    )
    namedValues = NamedValues(
        *(("natSubscriberNoPrio", 100),
          ("natSubscriberPrio", 200),
          ("natMaintenance", 300),
          ("natSpare", 400),
          ("natOperator", 500),
          ("natData", 600),
          ("intSubscriberNoPrio", 700),
          ("intData", 800),
          ("intSubscriberPrio", 900),
          ("intOperator", 1000),
          ("collectCall", 1100))
    )


_R2SignalingVariantsAniCategory_Type.__name__ = "Integer32"
_R2SignalingVariantsAniCategory_Object = MibTableColumn
r2SignalingVariantsAniCategory = _R2SignalingVariantsAniCategory_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 920),
    _R2SignalingVariantsAniCategory_Type()
)
r2SignalingVariantsAniCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsAniCategory.setStatus("current")


class _R2SignalingVariantsLineFreeCategory_Type(Integer32):
    """Custom type r2SignalingVariantsLineFreeCategory based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("lineFreeCharge", 100),
          ("lineFreeNoCharge", 200))
    )


_R2SignalingVariantsLineFreeCategory_Type.__name__ = "Integer32"
_R2SignalingVariantsLineFreeCategory_Object = MibTableColumn
r2SignalingVariantsLineFreeCategory = _R2SignalingVariantsLineFreeCategory_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 930),
    _R2SignalingVariantsLineFreeCategory_Type()
)
r2SignalingVariantsLineFreeCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsLineFreeCategory.setStatus("current")


class _R2SignalingVariantsAniRestrictedEnable_Type(MxEnableState):
    """Custom type r2SignalingVariantsAniRestrictedEnable based on MxEnableState"""
    defaultValue = 1


_R2SignalingVariantsAniRestrictedEnable_Type.__name__ = "MxEnableState"
_R2SignalingVariantsAniRestrictedEnable_Object = MibTableColumn
r2SignalingVariantsAniRestrictedEnable = _R2SignalingVariantsAniRestrictedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 950),
    _R2SignalingVariantsAniRestrictedEnable_Type()
)
r2SignalingVariantsAniRestrictedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsAniRestrictedEnable.setStatus("current")


class _R2SignalingVariantsIncomingDeclineMethod_Type(Integer32):
    """Custom type r2SignalingVariantsIncomingDeclineMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("release", 100),
          ("clearBack", 200))
    )


_R2SignalingVariantsIncomingDeclineMethod_Type.__name__ = "Integer32"
_R2SignalingVariantsIncomingDeclineMethod_Object = MibTableColumn
r2SignalingVariantsIncomingDeclineMethod = _R2SignalingVariantsIncomingDeclineMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 970),
    _R2SignalingVariantsIncomingDeclineMethod_Type()
)
r2SignalingVariantsIncomingDeclineMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsIncomingDeclineMethod.setStatus("current")


class _R2SignalingVariantsResetSpecific_Type(Integer32):
    """Custom type r2SignalingVariantsResetSpecific based on Integer32"""
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


_R2SignalingVariantsResetSpecific_Type.__name__ = "Integer32"
_R2SignalingVariantsResetSpecific_Object = MibTableColumn
r2SignalingVariantsResetSpecific = _R2SignalingVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 200, 1, 1000),
    _R2SignalingVariantsResetSpecific_Type()
)
r2SignalingVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2SignalingVariantsResetSpecific.setStatus("current")
_R2TimerVariantsTable_Object = MibTable
r2TimerVariantsTable = _R2TimerVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300)
)
if mibBuilder.loadTexts:
    r2TimerVariantsTable.setStatus("current")
_R2TimerVariantsEntry_Object = MibTableRow
r2TimerVariantsEntry = _R2TimerVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1)
)
r2TimerVariantsEntry.setIndexNames(
    (0, "MX-R2-MIB", "r2TimerVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    r2TimerVariantsEntry.setStatus("current")
_R2TimerVariantsInterfaceName_Type = OctetString
_R2TimerVariantsInterfaceName_Object = MibTableColumn
r2TimerVariantsInterfaceName = _R2TimerVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 100),
    _R2TimerVariantsInterfaceName_Type()
)
r2TimerVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    r2TimerVariantsInterfaceName.setStatus("current")


class _R2TimerVariantsOverrideDefault_Type(MxEnableState):
    """Custom type r2TimerVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_R2TimerVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_R2TimerVariantsOverrideDefault_Object = MibTableColumn
r2TimerVariantsOverrideDefault = _R2TimerVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 300),
    _R2TimerVariantsOverrideDefault_Type()
)
r2TimerVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsOverrideDefault.setStatus("current")


class _R2TimerVariantsSeizureAckTimeout_Type(Integer32):
    """Custom type r2TimerVariantsSeizureAckTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_R2TimerVariantsSeizureAckTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsSeizureAckTimeout_Object = MibTableColumn
r2TimerVariantsSeizureAckTimeout = _R2TimerVariantsSeizureAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 400),
    _R2TimerVariantsSeizureAckTimeout_Type()
)
r2TimerVariantsSeizureAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsSeizureAckTimeout.setStatus("current")


class _R2TimerVariantsFaultSeizureAckTimeout_Type(Integer32):
    """Custom type r2TimerVariantsFaultSeizureAckTimeout based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_R2TimerVariantsFaultSeizureAckTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsFaultSeizureAckTimeout_Object = MibTableColumn
r2TimerVariantsFaultSeizureAckTimeout = _R2TimerVariantsFaultSeizureAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 500),
    _R2TimerVariantsFaultSeizureAckTimeout_Type()
)
r2TimerVariantsFaultSeizureAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsFaultSeizureAckTimeout.setStatus("current")


class _R2TimerVariantsDoubleSeizureTimeout_Type(Integer32):
    """Custom type r2TimerVariantsDoubleSeizureTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_R2TimerVariantsDoubleSeizureTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsDoubleSeizureTimeout_Object = MibTableColumn
r2TimerVariantsDoubleSeizureTimeout = _R2TimerVariantsDoubleSeizureTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 600),
    _R2TimerVariantsDoubleSeizureTimeout_Type()
)
r2TimerVariantsDoubleSeizureTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsDoubleSeizureTimeout.setStatus("current")


class _R2TimerVariantsDoubleAnswerTimeout_Type(Integer32):
    """Custom type r2TimerVariantsDoubleAnswerTimeout based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_R2TimerVariantsDoubleAnswerTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsDoubleAnswerTimeout_Object = MibTableColumn
r2TimerVariantsDoubleAnswerTimeout = _R2TimerVariantsDoubleAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 700),
    _R2TimerVariantsDoubleAnswerTimeout_Type()
)
r2TimerVariantsDoubleAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsDoubleAnswerTimeout.setStatus("current")


class _R2TimerVariantsAnswerTimeout_Type(Integer32):
    """Custom type r2TimerVariantsAnswerTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_R2TimerVariantsAnswerTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsAnswerTimeout_Object = MibTableColumn
r2TimerVariantsAnswerTimeout = _R2TimerVariantsAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 710),
    _R2TimerVariantsAnswerTimeout_Type()
)
r2TimerVariantsAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsAnswerTimeout.setStatus("current")


class _R2TimerVariantsReAnswerTimeout_Type(Integer32):
    """Custom type r2TimerVariantsReAnswerTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_R2TimerVariantsReAnswerTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsReAnswerTimeout_Object = MibTableColumn
r2TimerVariantsReAnswerTimeout = _R2TimerVariantsReAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 720),
    _R2TimerVariantsReAnswerTimeout_Type()
)
r2TimerVariantsReAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsReAnswerTimeout.setStatus("current")


class _R2TimerVariantsReleaseGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsReleaseGuardTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_R2TimerVariantsReleaseGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsReleaseGuardTimeout_Object = MibTableColumn
r2TimerVariantsReleaseGuardTimeout = _R2TimerVariantsReleaseGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 800),
    _R2TimerVariantsReleaseGuardTimeout_Type()
)
r2TimerVariantsReleaseGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsReleaseGuardTimeout.setStatus("current")


class _R2TimerVariantsInterCallGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsInterCallGuardTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_R2TimerVariantsInterCallGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsInterCallGuardTimeout_Object = MibTableColumn
r2TimerVariantsInterCallGuardTimeout = _R2TimerVariantsInterCallGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 820),
    _R2TimerVariantsInterCallGuardTimeout_Type()
)
r2TimerVariantsInterCallGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsInterCallGuardTimeout.setStatus("current")


class _R2TimerVariantsNoDigitTimeout_Type(Integer32):
    """Custom type r2TimerVariantsNoDigitTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120000),
    )


_R2TimerVariantsNoDigitTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsNoDigitTimeout_Object = MibTableColumn
r2TimerVariantsNoDigitTimeout = _R2TimerVariantsNoDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 830),
    _R2TimerVariantsNoDigitTimeout_Type()
)
r2TimerVariantsNoDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsNoDigitTimeout.setStatus("current")


class _R2TimerVariantsCongestionToneGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsCongestionToneGuardTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_R2TimerVariantsCongestionToneGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsCongestionToneGuardTimeout_Object = MibTableColumn
r2TimerVariantsCongestionToneGuardTimeout = _R2TimerVariantsCongestionToneGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 850),
    _R2TimerVariantsCongestionToneGuardTimeout_Type()
)
r2TimerVariantsCongestionToneGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsCongestionToneGuardTimeout.setStatus("current")


class _R2TimerVariantsUnblockingTimeout_Type(Integer32):
    """Custom type r2TimerVariantsUnblockingTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_R2TimerVariantsUnblockingTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsUnblockingTimeout_Object = MibTableColumn
r2TimerVariantsUnblockingTimeout = _R2TimerVariantsUnblockingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 900),
    _R2TimerVariantsUnblockingTimeout_Type()
)
r2TimerVariantsUnblockingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsUnblockingTimeout.setStatus("current")


class _R2TimerVariantsAddressCompleteTimeout_Type(Integer32):
    """Custom type r2TimerVariantsAddressCompleteTimeout based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_R2TimerVariantsAddressCompleteTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsAddressCompleteTimeout_Object = MibTableColumn
r2TimerVariantsAddressCompleteTimeout = _R2TimerVariantsAddressCompleteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1000),
    _R2TimerVariantsAddressCompleteTimeout_Type()
)
r2TimerVariantsAddressCompleteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsAddressCompleteTimeout.setStatus("current")


class _R2TimerVariantsWaitAnswerTimeout_Type(Integer32):
    """Custom type r2TimerVariantsWaitAnswerTimeout based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_R2TimerVariantsWaitAnswerTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsWaitAnswerTimeout_Object = MibTableColumn
r2TimerVariantsWaitAnswerTimeout = _R2TimerVariantsWaitAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1100),
    _R2TimerVariantsWaitAnswerTimeout_Type()
)
r2TimerVariantsWaitAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsWaitAnswerTimeout.setStatus("current")


class _R2TimerVariantsDigitCompleteTimeout_Type(Integer32):
    """Custom type r2TimerVariantsDigitCompleteTimeout based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_R2TimerVariantsDigitCompleteTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsDigitCompleteTimeout_Object = MibTableColumn
r2TimerVariantsDigitCompleteTimeout = _R2TimerVariantsDigitCompleteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1200),
    _R2TimerVariantsDigitCompleteTimeout_Type()
)
r2TimerVariantsDigitCompleteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsDigitCompleteTimeout.setStatus("current")


class _R2TimerVariantsWaitGroupBResponseCompleteTimeout_Type(Integer32):
    """Custom type r2TimerVariantsWaitGroupBResponseCompleteTimeout based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_R2TimerVariantsWaitGroupBResponseCompleteTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsWaitGroupBResponseCompleteTimeout_Object = MibTableColumn
r2TimerVariantsWaitGroupBResponseCompleteTimeout = _R2TimerVariantsWaitGroupBResponseCompleteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1300),
    _R2TimerVariantsWaitGroupBResponseCompleteTimeout_Type()
)
r2TimerVariantsWaitGroupBResponseCompleteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsWaitGroupBResponseCompleteTimeout.setStatus("current")


class _R2TimerVariantsWaitImmediateResponseCompleteTimeout_Type(Integer32):
    """Custom type r2TimerVariantsWaitImmediateResponseCompleteTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_R2TimerVariantsWaitImmediateResponseCompleteTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsWaitImmediateResponseCompleteTimeout_Object = MibTableColumn
r2TimerVariantsWaitImmediateResponseCompleteTimeout = _R2TimerVariantsWaitImmediateResponseCompleteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1400),
    _R2TimerVariantsWaitImmediateResponseCompleteTimeout_Type()
)
r2TimerVariantsWaitImmediateResponseCompleteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsWaitImmediateResponseCompleteTimeout.setStatus("current")


class _R2TimerVariantsPlayToneGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsPlayToneGuardTimeout based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_R2TimerVariantsPlayToneGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsPlayToneGuardTimeout_Object = MibTableColumn
r2TimerVariantsPlayToneGuardTimeout = _R2TimerVariantsPlayToneGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1500),
    _R2TimerVariantsPlayToneGuardTimeout_Type()
)
r2TimerVariantsPlayToneGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsPlayToneGuardTimeout.setStatus("current")


class _R2TimerVariantsAcceptCallTimeout_Type(Integer32):
    """Custom type r2TimerVariantsAcceptCallTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_R2TimerVariantsAcceptCallTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsAcceptCallTimeout_Object = MibTableColumn
r2TimerVariantsAcceptCallTimeout = _R2TimerVariantsAcceptCallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1600),
    _R2TimerVariantsAcceptCallTimeout_Type()
)
r2TimerVariantsAcceptCallTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsAcceptCallTimeout.setStatus("current")


class _R2TimerVariantsClearForwardGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsClearForwardGuardTimeout based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_R2TimerVariantsClearForwardGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsClearForwardGuardTimeout_Object = MibTableColumn
r2TimerVariantsClearForwardGuardTimeout = _R2TimerVariantsClearForwardGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1700),
    _R2TimerVariantsClearForwardGuardTimeout_Type()
)
r2TimerVariantsClearForwardGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsClearForwardGuardTimeout.setStatus("current")


class _R2TimerVariantsClearBackwardGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsClearBackwardGuardTimeout based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_R2TimerVariantsClearBackwardGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsClearBackwardGuardTimeout_Object = MibTableColumn
r2TimerVariantsClearBackwardGuardTimeout = _R2TimerVariantsClearBackwardGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1800),
    _R2TimerVariantsClearBackwardGuardTimeout_Type()
)
r2TimerVariantsClearBackwardGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsClearBackwardGuardTimeout.setStatus("current")


class _R2TimerVariantsFaultOnAnsweredGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsFaultOnAnsweredGuardTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_R2TimerVariantsFaultOnAnsweredGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsFaultOnAnsweredGuardTimeout_Object = MibTableColumn
r2TimerVariantsFaultOnAnsweredGuardTimeout = _R2TimerVariantsFaultOnAnsweredGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 1900),
    _R2TimerVariantsFaultOnAnsweredGuardTimeout_Type()
)
r2TimerVariantsFaultOnAnsweredGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsFaultOnAnsweredGuardTimeout.setStatus("current")


class _R2TimerVariantsFaultOnClearBackwardGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsFaultOnClearBackwardGuardTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_R2TimerVariantsFaultOnClearBackwardGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsFaultOnClearBackwardGuardTimeout_Object = MibTableColumn
r2TimerVariantsFaultOnClearBackwardGuardTimeout = _R2TimerVariantsFaultOnClearBackwardGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 2000),
    _R2TimerVariantsFaultOnClearBackwardGuardTimeout_Type()
)
r2TimerVariantsFaultOnClearBackwardGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsFaultOnClearBackwardGuardTimeout.setStatus("current")


class _R2TimerVariantsFaultOnSeizeAckGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsFaultOnSeizeAckGuardTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_R2TimerVariantsFaultOnSeizeAckGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsFaultOnSeizeAckGuardTimeout_Object = MibTableColumn
r2TimerVariantsFaultOnSeizeAckGuardTimeout = _R2TimerVariantsFaultOnSeizeAckGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 2100),
    _R2TimerVariantsFaultOnSeizeAckGuardTimeout_Type()
)
r2TimerVariantsFaultOnSeizeAckGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsFaultOnSeizeAckGuardTimeout.setStatus("current")


class _R2TimerVariantsFaultOnSeizeGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsFaultOnSeizeGuardTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_R2TimerVariantsFaultOnSeizeGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsFaultOnSeizeGuardTimeout_Object = MibTableColumn
r2TimerVariantsFaultOnSeizeGuardTimeout = _R2TimerVariantsFaultOnSeizeGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 2200),
    _R2TimerVariantsFaultOnSeizeGuardTimeout_Type()
)
r2TimerVariantsFaultOnSeizeGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsFaultOnSeizeGuardTimeout.setStatus("current")


class _R2TimerVariantsDeclineGuardTimeout_Type(Integer32):
    """Custom type r2TimerVariantsDeclineGuardTimeout based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2000),
    )


_R2TimerVariantsDeclineGuardTimeout_Type.__name__ = "Integer32"
_R2TimerVariantsDeclineGuardTimeout_Object = MibTableColumn
r2TimerVariantsDeclineGuardTimeout = _R2TimerVariantsDeclineGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 2250),
    _R2TimerVariantsDeclineGuardTimeout_Type()
)
r2TimerVariantsDeclineGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsDeclineGuardTimeout.setStatus("current")


class _R2TimerVariantsResetSpecific_Type(Integer32):
    """Custom type r2TimerVariantsResetSpecific based on Integer32"""
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


_R2TimerVariantsResetSpecific_Type.__name__ = "Integer32"
_R2TimerVariantsResetSpecific_Object = MibTableColumn
r2TimerVariantsResetSpecific = _R2TimerVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 300, 1, 2300),
    _R2TimerVariantsResetSpecific_Type()
)
r2TimerVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2TimerVariantsResetSpecific.setStatus("current")
_R2DigitTimerVariantsTable_Object = MibTable
r2DigitTimerVariantsTable = _R2DigitTimerVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400)
)
if mibBuilder.loadTexts:
    r2DigitTimerVariantsTable.setStatus("current")
_R2DigitTimerVariantsEntry_Object = MibTableRow
r2DigitTimerVariantsEntry = _R2DigitTimerVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1)
)
r2DigitTimerVariantsEntry.setIndexNames(
    (0, "MX-R2-MIB", "r2DigitTimerVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    r2DigitTimerVariantsEntry.setStatus("current")
_R2DigitTimerVariantsInterfaceName_Type = OctetString
_R2DigitTimerVariantsInterfaceName_Object = MibTableColumn
r2DigitTimerVariantsInterfaceName = _R2DigitTimerVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 100),
    _R2DigitTimerVariantsInterfaceName_Type()
)
r2DigitTimerVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsInterfaceName.setStatus("current")


class _R2DigitTimerVariantsOverrideDefault_Type(MxEnableState):
    """Custom type r2DigitTimerVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_R2DigitTimerVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_R2DigitTimerVariantsOverrideDefault_Object = MibTableColumn
r2DigitTimerVariantsOverrideDefault = _R2DigitTimerVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 300),
    _R2DigitTimerVariantsOverrideDefault_Type()
)
r2DigitTimerVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsOverrideDefault.setStatus("current")


class _R2DigitTimerVariantsMfCongestionToneDuration_Type(Integer32):
    """Custom type r2DigitTimerVariantsMfCongestionToneDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120000),
    )


_R2DigitTimerVariantsMfCongestionToneDuration_Type.__name__ = "Integer32"
_R2DigitTimerVariantsMfCongestionToneDuration_Object = MibTableColumn
r2DigitTimerVariantsMfCongestionToneDuration = _R2DigitTimerVariantsMfCongestionToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 350),
    _R2DigitTimerVariantsMfCongestionToneDuration_Type()
)
r2DigitTimerVariantsMfCongestionToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsMfCongestionToneDuration.setStatus("current")


class _R2DigitTimerVariantsMfcPulseInterDigitTimeout_Type(Integer32):
    """Custom type r2DigitTimerVariantsMfcPulseInterDigitTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_R2DigitTimerVariantsMfcPulseInterDigitTimeout_Type.__name__ = "Integer32"
_R2DigitTimerVariantsMfcPulseInterDigitTimeout_Object = MibTableColumn
r2DigitTimerVariantsMfcPulseInterDigitTimeout = _R2DigitTimerVariantsMfcPulseInterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 400),
    _R2DigitTimerVariantsMfcPulseInterDigitTimeout_Type()
)
r2DigitTimerVariantsMfcPulseInterDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsMfcPulseInterDigitTimeout.setStatus("current")


class _R2DigitTimerVariantsMfcPulseMinOnTimeout_Type(Integer32):
    """Custom type r2DigitTimerVariantsMfcPulseMinOnTimeout based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_R2DigitTimerVariantsMfcPulseMinOnTimeout_Type.__name__ = "Integer32"
_R2DigitTimerVariantsMfcPulseMinOnTimeout_Object = MibTableColumn
r2DigitTimerVariantsMfcPulseMinOnTimeout = _R2DigitTimerVariantsMfcPulseMinOnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 500),
    _R2DigitTimerVariantsMfcPulseMinOnTimeout_Type()
)
r2DigitTimerVariantsMfcPulseMinOnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsMfcPulseMinOnTimeout.setStatus("current")


class _R2DigitTimerVariantsMfcMaxSequenceTimeout_Type(Integer32):
    """Custom type r2DigitTimerVariantsMfcMaxSequenceTimeout based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000),
    )


_R2DigitTimerVariantsMfcMaxSequenceTimeout_Type.__name__ = "Integer32"
_R2DigitTimerVariantsMfcMaxSequenceTimeout_Object = MibTableColumn
r2DigitTimerVariantsMfcMaxSequenceTimeout = _R2DigitTimerVariantsMfcMaxSequenceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 600),
    _R2DigitTimerVariantsMfcMaxSequenceTimeout_Type()
)
r2DigitTimerVariantsMfcMaxSequenceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsMfcMaxSequenceTimeout.setStatus("current")


class _R2DigitTimerVariantsMfcMaxOnTimeout_Type(Integer32):
    """Custom type r2DigitTimerVariantsMfcMaxOnTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35000),
    )


_R2DigitTimerVariantsMfcMaxOnTimeout_Type.__name__ = "Integer32"
_R2DigitTimerVariantsMfcMaxOnTimeout_Object = MibTableColumn
r2DigitTimerVariantsMfcMaxOnTimeout = _R2DigitTimerVariantsMfcMaxOnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 700),
    _R2DigitTimerVariantsMfcMaxOnTimeout_Type()
)
r2DigitTimerVariantsMfcMaxOnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsMfcMaxOnTimeout.setStatus("current")


class _R2DigitTimerVariantsMfcMaxOffTimeout_Type(Integer32):
    """Custom type r2DigitTimerVariantsMfcMaxOffTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35000),
    )


_R2DigitTimerVariantsMfcMaxOffTimeout_Type.__name__ = "Integer32"
_R2DigitTimerVariantsMfcMaxOffTimeout_Object = MibTableColumn
r2DigitTimerVariantsMfcMaxOffTimeout = _R2DigitTimerVariantsMfcMaxOffTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 800),
    _R2DigitTimerVariantsMfcMaxOffTimeout_Type()
)
r2DigitTimerVariantsMfcMaxOffTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsMfcMaxOffTimeout.setStatus("current")


class _R2DigitTimerVariantsResetSpecific_Type(Integer32):
    """Custom type r2DigitTimerVariantsResetSpecific based on Integer32"""
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


_R2DigitTimerVariantsResetSpecific_Type.__name__ = "Integer32"
_R2DigitTimerVariantsResetSpecific_Object = MibTableColumn
r2DigitTimerVariantsResetSpecific = _R2DigitTimerVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 400, 1, 900),
    _R2DigitTimerVariantsResetSpecific_Type()
)
r2DigitTimerVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2DigitTimerVariantsResetSpecific.setStatus("current")
_R2LinkTimerVariantsTable_Object = MibTable
r2LinkTimerVariantsTable = _R2LinkTimerVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500)
)
if mibBuilder.loadTexts:
    r2LinkTimerVariantsTable.setStatus("current")
_R2LinkTimerVariantsEntry_Object = MibTableRow
r2LinkTimerVariantsEntry = _R2LinkTimerVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500, 1)
)
r2LinkTimerVariantsEntry.setIndexNames(
    (0, "MX-R2-MIB", "r2LinkTimerVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    r2LinkTimerVariantsEntry.setStatus("current")
_R2LinkTimerVariantsInterfaceName_Type = OctetString
_R2LinkTimerVariantsInterfaceName_Object = MibTableColumn
r2LinkTimerVariantsInterfaceName = _R2LinkTimerVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500, 1, 100),
    _R2LinkTimerVariantsInterfaceName_Type()
)
r2LinkTimerVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    r2LinkTimerVariantsInterfaceName.setStatus("current")


class _R2LinkTimerVariantsOverrideDefault_Type(MxEnableState):
    """Custom type r2LinkTimerVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_R2LinkTimerVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_R2LinkTimerVariantsOverrideDefault_Object = MibTableColumn
r2LinkTimerVariantsOverrideDefault = _R2LinkTimerVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500, 1, 300),
    _R2LinkTimerVariantsOverrideDefault_Type()
)
r2LinkTimerVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2LinkTimerVariantsOverrideDefault.setStatus("current")


class _R2LinkTimerVariantsLinkActivationTimeout_Type(Integer32):
    """Custom type r2LinkTimerVariantsLinkActivationTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_R2LinkTimerVariantsLinkActivationTimeout_Type.__name__ = "Integer32"
_R2LinkTimerVariantsLinkActivationTimeout_Object = MibTableColumn
r2LinkTimerVariantsLinkActivationTimeout = _R2LinkTimerVariantsLinkActivationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500, 1, 400),
    _R2LinkTimerVariantsLinkActivationTimeout_Type()
)
r2LinkTimerVariantsLinkActivationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2LinkTimerVariantsLinkActivationTimeout.setStatus("current")


class _R2LinkTimerVariantsLinkActivationRetryTimeout_Type(Integer32):
    """Custom type r2LinkTimerVariantsLinkActivationRetryTimeout based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_R2LinkTimerVariantsLinkActivationRetryTimeout_Type.__name__ = "Integer32"
_R2LinkTimerVariantsLinkActivationRetryTimeout_Object = MibTableColumn
r2LinkTimerVariantsLinkActivationRetryTimeout = _R2LinkTimerVariantsLinkActivationRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500, 1, 500),
    _R2LinkTimerVariantsLinkActivationRetryTimeout_Type()
)
r2LinkTimerVariantsLinkActivationRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2LinkTimerVariantsLinkActivationRetryTimeout.setStatus("current")


class _R2LinkTimerVariantsResetSpecific_Type(Integer32):
    """Custom type r2LinkTimerVariantsResetSpecific based on Integer32"""
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


_R2LinkTimerVariantsResetSpecific_Type.__name__ = "Integer32"
_R2LinkTimerVariantsResetSpecific_Object = MibTableColumn
r2LinkTimerVariantsResetSpecific = _R2LinkTimerVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 500, 1, 600),
    _R2LinkTimerVariantsResetSpecific_Type()
)
r2LinkTimerVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2LinkTimerVariantsResetSpecific.setStatus("current")
_R2ToneVariantsTable_Object = MibTable
r2ToneVariantsTable = _R2ToneVariantsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600)
)
if mibBuilder.loadTexts:
    r2ToneVariantsTable.setStatus("current")
_R2ToneVariantsEntry_Object = MibTableRow
r2ToneVariantsEntry = _R2ToneVariantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1)
)
r2ToneVariantsEntry.setIndexNames(
    (0, "MX-R2-MIB", "r2ToneVariantsInterfaceName"),
)
if mibBuilder.loadTexts:
    r2ToneVariantsEntry.setStatus("current")
_R2ToneVariantsInterfaceName_Type = OctetString
_R2ToneVariantsInterfaceName_Object = MibTableColumn
r2ToneVariantsInterfaceName = _R2ToneVariantsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 100),
    _R2ToneVariantsInterfaceName_Type()
)
r2ToneVariantsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    r2ToneVariantsInterfaceName.setStatus("current")


class _R2ToneVariantsOverrideDefault_Type(MxEnableState):
    """Custom type r2ToneVariantsOverrideDefault based on MxEnableState"""
    defaultValue = 0


_R2ToneVariantsOverrideDefault_Type.__name__ = "MxEnableState"
_R2ToneVariantsOverrideDefault_Object = MibTableColumn
r2ToneVariantsOverrideDefault = _R2ToneVariantsOverrideDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 300),
    _R2ToneVariantsOverrideDefault_Type()
)
r2ToneVariantsOverrideDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsOverrideDefault.setStatus("current")


class _R2ToneVariantsFwdGroup1EndOfDnis_Type(Integer32):
    """Custom type r2ToneVariantsFwdGroup1EndOfDnis based on Integer32"""
    defaultValue = 1600

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
          ("i1", 200),
          ("i2", 300),
          ("i3", 400),
          ("i4", 500),
          ("i5", 600),
          ("i6", 700),
          ("i7", 800),
          ("i8", 900),
          ("i9", 1000),
          ("i10", 1100),
          ("i11", 1200),
          ("i12", 1300),
          ("i13", 1400),
          ("i14", 1500),
          ("i15", 1600))
    )


_R2ToneVariantsFwdGroup1EndOfDnis_Type.__name__ = "Integer32"
_R2ToneVariantsFwdGroup1EndOfDnis_Object = MibTableColumn
r2ToneVariantsFwdGroup1EndOfDnis = _R2ToneVariantsFwdGroup1EndOfDnis_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 400),
    _R2ToneVariantsFwdGroup1EndOfDnis_Type()
)
r2ToneVariantsFwdGroup1EndOfDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsFwdGroup1EndOfDnis.setStatus("current")


class _R2ToneVariantsFwdGroup1EndOfAni_Type(Integer32):
    """Custom type r2ToneVariantsFwdGroup1EndOfAni based on Integer32"""
    defaultValue = 1600

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
          ("i1", 200),
          ("i2", 300),
          ("i3", 400),
          ("i4", 500),
          ("i5", 600),
          ("i6", 700),
          ("i7", 800),
          ("i8", 900),
          ("i9", 1000),
          ("i10", 1100),
          ("i11", 1200),
          ("i12", 1300),
          ("i13", 1400),
          ("i14", 1500),
          ("i15", 1600))
    )


_R2ToneVariantsFwdGroup1EndOfAni_Type.__name__ = "Integer32"
_R2ToneVariantsFwdGroup1EndOfAni_Object = MibTableColumn
r2ToneVariantsFwdGroup1EndOfAni = _R2ToneVariantsFwdGroup1EndOfAni_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 500),
    _R2ToneVariantsFwdGroup1EndOfAni_Type()
)
r2ToneVariantsFwdGroup1EndOfAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsFwdGroup1EndOfAni.setStatus("current")


class _R2ToneVariantsFwdGroup1RestrictedAni_Type(Integer32):
    """Custom type r2ToneVariantsFwdGroup1RestrictedAni based on Integer32"""
    defaultValue = 1300

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
          ("i1", 200),
          ("i2", 300),
          ("i3", 400),
          ("i4", 500),
          ("i5", 600),
          ("i6", 700),
          ("i7", 800),
          ("i8", 900),
          ("i9", 1000),
          ("i10", 1100),
          ("i11", 1200),
          ("i12", 1300),
          ("i13", 1400),
          ("i14", 1500),
          ("i15", 1600))
    )


_R2ToneVariantsFwdGroup1RestrictedAni_Type.__name__ = "Integer32"
_R2ToneVariantsFwdGroup1RestrictedAni_Object = MibTableColumn
r2ToneVariantsFwdGroup1RestrictedAni = _R2ToneVariantsFwdGroup1RestrictedAni_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 520),
    _R2ToneVariantsFwdGroup1RestrictedAni_Type()
)
r2ToneVariantsFwdGroup1RestrictedAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsFwdGroup1RestrictedAni.setStatus("current")


class _R2ToneVariantsBwdGroupASendNextDnisDigit_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendNextDnisDigit based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendNextDnisDigit_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendNextDnisDigit_Object = MibTableColumn
r2ToneVariantsBwdGroupASendNextDnisDigit = _R2ToneVariantsBwdGroupASendNextDnisDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 600),
    _R2ToneVariantsBwdGroupASendNextDnisDigit_Type()
)
r2ToneVariantsBwdGroupASendNextDnisDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendNextDnisDigit.setStatus("current")


class _R2ToneVariantsBwdGroupASendPreviousDnisDigit_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendPreviousDnisDigit based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendPreviousDnisDigit_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendPreviousDnisDigit_Object = MibTableColumn
r2ToneVariantsBwdGroupASendPreviousDnisDigit = _R2ToneVariantsBwdGroupASendPreviousDnisDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 700),
    _R2ToneVariantsBwdGroupASendPreviousDnisDigit_Type()
)
r2ToneVariantsBwdGroupASendPreviousDnisDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendPreviousDnisDigit.setStatus("current")


class _R2ToneVariantsBwdGroupASwitchToGroupII_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASwitchToGroupII based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASwitchToGroupII_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASwitchToGroupII_Object = MibTableColumn
r2ToneVariantsBwdGroupASwitchToGroupII = _R2ToneVariantsBwdGroupASwitchToGroupII_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 800),
    _R2ToneVariantsBwdGroupASwitchToGroupII_Type()
)
r2ToneVariantsBwdGroupASwitchToGroupII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASwitchToGroupII.setStatus("current")


class _R2ToneVariantsBwdGroupANetworkCongestion_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupANetworkCongestion based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupANetworkCongestion_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupANetworkCongestion_Object = MibTableColumn
r2ToneVariantsBwdGroupANetworkCongestion = _R2ToneVariantsBwdGroupANetworkCongestion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 900),
    _R2ToneVariantsBwdGroupANetworkCongestion_Type()
)
r2ToneVariantsBwdGroupANetworkCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupANetworkCongestion.setStatus("current")


class _R2ToneVariantsBwdGroupASendCallingPartyCategory_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendCallingPartyCategory based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendCallingPartyCategory_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendCallingPartyCategory_Object = MibTableColumn
r2ToneVariantsBwdGroupASendCallingPartyCategory = _R2ToneVariantsBwdGroupASendCallingPartyCategory_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1000),
    _R2ToneVariantsBwdGroupASendCallingPartyCategory_Type()
)
r2ToneVariantsBwdGroupASendCallingPartyCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendCallingPartyCategory.setStatus("current")


class _R2ToneVariantsBwdGroupAImmediateAccept_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupAImmediateAccept based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupAImmediateAccept_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupAImmediateAccept_Object = MibTableColumn
r2ToneVariantsBwdGroupAImmediateAccept = _R2ToneVariantsBwdGroupAImmediateAccept_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1100),
    _R2ToneVariantsBwdGroupAImmediateAccept_Type()
)
r2ToneVariantsBwdGroupAImmediateAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupAImmediateAccept.setStatus("current")


class _R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendDnisDigitNMinus2 based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Object = MibTableColumn
r2ToneVariantsBwdGroupASendDnisDigitNMinus2 = _R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1200),
    _R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Type()
)
r2ToneVariantsBwdGroupASendDnisDigitNMinus2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendDnisDigitNMinus2.setStatus("current")


class _R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendDnisDigitNMinus3 based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Object = MibTableColumn
r2ToneVariantsBwdGroupASendDnisDigitNMinus3 = _R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1300),
    _R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Type()
)
r2ToneVariantsBwdGroupASendDnisDigitNMinus3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendDnisDigitNMinus3.setStatus("current")


class _R2ToneVariantsBwdGroupARepeatAllDnis_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupARepeatAllDnis based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupARepeatAllDnis_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupARepeatAllDnis_Object = MibTableColumn
r2ToneVariantsBwdGroupARepeatAllDnis = _R2ToneVariantsBwdGroupARepeatAllDnis_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1400),
    _R2ToneVariantsBwdGroupARepeatAllDnis_Type()
)
r2ToneVariantsBwdGroupARepeatAllDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupARepeatAllDnis.setStatus("current")


class _R2ToneVariantsBwdGroupASendNextAniDigit_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendNextAniDigit based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendNextAniDigit_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendNextAniDigit_Object = MibTableColumn
r2ToneVariantsBwdGroupASendNextAniDigit = _R2ToneVariantsBwdGroupASendNextAniDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1500),
    _R2ToneVariantsBwdGroupASendNextAniDigit_Type()
)
r2ToneVariantsBwdGroupASendNextAniDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendNextAniDigit.setStatus("current")


class _R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC based on Integer32"""
    defaultValue = 1600

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
          ("a1", 200),
          ("a2", 300),
          ("a3", 400),
          ("a4", 500),
          ("a5", 600),
          ("a6", 700),
          ("a7", 800),
          ("a8", 900),
          ("a9", 1000),
          ("a10", 1100),
          ("a11", 1200),
          ("a12", 1300),
          ("a13", 1400),
          ("a14", 1500),
          ("a15", 1600))
    )


_R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Object = MibTableColumn
r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC = _R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1550),
    _R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Type()
)
r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC.setStatus("current")


class _R2ToneVariantsBwdGroupBSendSit_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBSendSit based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBSendSit_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBSendSit_Object = MibTableColumn
r2ToneVariantsBwdGroupBSendSit = _R2ToneVariantsBwdGroupBSendSit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1600),
    _R2ToneVariantsBwdGroupBSendSit_Type()
)
r2ToneVariantsBwdGroupBSendSit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBSendSit.setStatus("current")


class _R2ToneVariantsBwdGroupBUserBusy_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBUserBusy based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBUserBusy_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBUserBusy_Object = MibTableColumn
r2ToneVariantsBwdGroupBUserBusy = _R2ToneVariantsBwdGroupBUserBusy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1700),
    _R2ToneVariantsBwdGroupBUserBusy_Type()
)
r2ToneVariantsBwdGroupBUserBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBUserBusy.setStatus("current")


class _R2ToneVariantsBwdGroupBNetworkCongestion_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBNetworkCongestion based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBNetworkCongestion_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBNetworkCongestion_Object = MibTableColumn
r2ToneVariantsBwdGroupBNetworkCongestion = _R2ToneVariantsBwdGroupBNetworkCongestion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1800),
    _R2ToneVariantsBwdGroupBNetworkCongestion_Type()
)
r2ToneVariantsBwdGroupBNetworkCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBNetworkCongestion.setStatus("current")


class _R2ToneVariantsBwdGroupBUnassignedNumber_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBUnassignedNumber based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBUnassignedNumber_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBUnassignedNumber_Object = MibTableColumn
r2ToneVariantsBwdGroupBUnassignedNumber = _R2ToneVariantsBwdGroupBUnassignedNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 1900),
    _R2ToneVariantsBwdGroupBUnassignedNumber_Type()
)
r2ToneVariantsBwdGroupBUnassignedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBUnassignedNumber.setStatus("current")


class _R2ToneVariantsBwdGroupBLineFreeCharge_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBLineFreeCharge based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBLineFreeCharge_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBLineFreeCharge_Object = MibTableColumn
r2ToneVariantsBwdGroupBLineFreeCharge = _R2ToneVariantsBwdGroupBLineFreeCharge_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2000),
    _R2ToneVariantsBwdGroupBLineFreeCharge_Type()
)
r2ToneVariantsBwdGroupBLineFreeCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBLineFreeCharge.setStatus("current")


class _R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Object = MibTableColumn
r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge = _R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2100),
    _R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Type()
)
r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge.setStatus("current")


class _R2ToneVariantsBwdGroupBLineFreeNoCharge_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBLineFreeNoCharge based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBLineFreeNoCharge_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBLineFreeNoCharge_Object = MibTableColumn
r2ToneVariantsBwdGroupBLineFreeNoCharge = _R2ToneVariantsBwdGroupBLineFreeNoCharge_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2200),
    _R2ToneVariantsBwdGroupBLineFreeNoCharge_Type()
)
r2ToneVariantsBwdGroupBLineFreeNoCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBLineFreeNoCharge.setStatus("current")


class _R2ToneVariantsBwdGroupBLineOutOfOrder_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBLineOutOfOrder based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBLineOutOfOrder_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBLineOutOfOrder_Object = MibTableColumn
r2ToneVariantsBwdGroupBLineOutOfOrder = _R2ToneVariantsBwdGroupBLineOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2300),
    _R2ToneVariantsBwdGroupBLineOutOfOrder_Type()
)
r2ToneVariantsBwdGroupBLineOutOfOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBLineOutOfOrder.setStatus("current")


class _R2ToneVariantsBwdGroupBChangedNumber_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupBChangedNumber based on Integer32"""
    defaultValue = 1600

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
          ("b1", 200),
          ("b2", 300),
          ("b3", 400),
          ("b4", 500),
          ("b5", 600),
          ("b6", 700),
          ("b7", 800),
          ("b8", 900),
          ("b9", 1000),
          ("b10", 1100),
          ("b11", 1200),
          ("b12", 1300),
          ("b13", 1400),
          ("b14", 1500),
          ("b15", 1600))
    )


_R2ToneVariantsBwdGroupBChangedNumber_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupBChangedNumber_Object = MibTableColumn
r2ToneVariantsBwdGroupBChangedNumber = _R2ToneVariantsBwdGroupBChangedNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2350),
    _R2ToneVariantsBwdGroupBChangedNumber_Type()
)
r2ToneVariantsBwdGroupBChangedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupBChangedNumber.setStatus("current")


class _R2ToneVariantsBwdGroupCSendNextAniDigit_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupCSendNextAniDigit based on Integer32"""
    defaultValue = 1600

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
          ("c1", 200),
          ("c2", 300),
          ("c3", 400),
          ("c4", 500),
          ("c5", 600),
          ("c6", 700),
          ("c7", 800),
          ("c8", 900),
          ("c9", 1000),
          ("c10", 1100),
          ("c11", 1200),
          ("c12", 1300),
          ("c13", 1400),
          ("c14", 1500),
          ("c15", 1600))
    )


_R2ToneVariantsBwdGroupCSendNextAniDigit_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupCSendNextAniDigit_Object = MibTableColumn
r2ToneVariantsBwdGroupCSendNextAniDigit = _R2ToneVariantsBwdGroupCSendNextAniDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2355),
    _R2ToneVariantsBwdGroupCSendNextAniDigit_Type()
)
r2ToneVariantsBwdGroupCSendNextAniDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupCSendNextAniDigit.setStatus("current")


class _R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA based on Integer32"""
    defaultValue = 1600

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
          ("c1", 200),
          ("c2", 300),
          ("c3", 400),
          ("c4", 500),
          ("c5", 600),
          ("c6", 700),
          ("c7", 800),
          ("c8", 900),
          ("c9", 1000),
          ("c10", 1100),
          ("c11", 1200),
          ("c12", 1300),
          ("c13", 1400),
          ("c14", 1500),
          ("c15", 1600))
    )


_R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Object = MibTableColumn
r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA = _R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2360),
    _R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Type()
)
r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA.setStatus("current")


class _R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA based on Integer32"""
    defaultValue = 1600

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
          ("c1", 200),
          ("c2", 300),
          ("c3", 400),
          ("c4", 500),
          ("c5", 600),
          ("c6", 700),
          ("c7", 800),
          ("c8", 900),
          ("c9", 1000),
          ("c10", 1100),
          ("c11", 1200),
          ("c12", 1300),
          ("c13", 1400),
          ("c14", 1500),
          ("c15", 1600))
    )


_R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Object = MibTableColumn
r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA = _R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2365),
    _R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Type()
)
r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA.setStatus("current")


class _R2ToneVariantsBwdGroupCNetworkCongestion_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupCNetworkCongestion based on Integer32"""
    defaultValue = 1600

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
          ("c1", 200),
          ("c2", 300),
          ("c3", 400),
          ("c4", 500),
          ("c5", 600),
          ("c6", 700),
          ("c7", 800),
          ("c8", 900),
          ("c9", 1000),
          ("c10", 1100),
          ("c11", 1200),
          ("c12", 1300),
          ("c13", 1400),
          ("c14", 1500),
          ("c15", 1600))
    )


_R2ToneVariantsBwdGroupCNetworkCongestion_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupCNetworkCongestion_Object = MibTableColumn
r2ToneVariantsBwdGroupCNetworkCongestion = _R2ToneVariantsBwdGroupCNetworkCongestion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2370),
    _R2ToneVariantsBwdGroupCNetworkCongestion_Type()
)
r2ToneVariantsBwdGroupCNetworkCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupCNetworkCongestion.setStatus("current")


class _R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA based on Integer32"""
    defaultValue = 1600

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
          ("c1", 200),
          ("c2", 300),
          ("c3", 400),
          ("c4", 500),
          ("c5", 600),
          ("c6", 700),
          ("c7", 800),
          ("c8", 900),
          ("c9", 1000),
          ("c10", 1100),
          ("c11", 1200),
          ("c12", 1300),
          ("c13", 1400),
          ("c14", 1500),
          ("c15", 1600))
    )


_R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Object = MibTableColumn
r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA = _R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2375),
    _R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Type()
)
r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA.setStatus("current")


class _R2ToneVariantsBwdGroupCSwitchGroupII_Type(Integer32):
    """Custom type r2ToneVariantsBwdGroupCSwitchGroupII based on Integer32"""
    defaultValue = 1600

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
          ("c1", 200),
          ("c2", 300),
          ("c3", 400),
          ("c4", 500),
          ("c5", 600),
          ("c6", 700),
          ("c7", 800),
          ("c8", 900),
          ("c9", 1000),
          ("c10", 1100),
          ("c11", 1200),
          ("c12", 1300),
          ("c13", 1400),
          ("c14", 1500),
          ("c15", 1600))
    )


_R2ToneVariantsBwdGroupCSwitchGroupII_Type.__name__ = "Integer32"
_R2ToneVariantsBwdGroupCSwitchGroupII_Object = MibTableColumn
r2ToneVariantsBwdGroupCSwitchGroupII = _R2ToneVariantsBwdGroupCSwitchGroupII_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2380),
    _R2ToneVariantsBwdGroupCSwitchGroupII_Type()
)
r2ToneVariantsBwdGroupCSwitchGroupII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsBwdGroupCSwitchGroupII.setStatus("current")


class _R2ToneVariantsResetSpecific_Type(Integer32):
    """Custom type r2ToneVariantsResetSpecific based on Integer32"""
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


_R2ToneVariantsResetSpecific_Type.__name__ = "Integer32"
_R2ToneVariantsResetSpecific_Object = MibTableColumn
r2ToneVariantsResetSpecific = _R2ToneVariantsResetSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 100, 600, 1, 2400),
    _R2ToneVariantsResetSpecific_Type()
)
r2ToneVariantsResetSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2ToneVariantsResetSpecific.setStatus("current")
_BearerChannelGroup_ObjectIdentity = ObjectIdentity
bearerChannelGroup = _BearerChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 200)
)
_BearerChannelInfoTable_Object = MibTable
bearerChannelInfoTable = _BearerChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 200, 100)
)
if mibBuilder.loadTexts:
    bearerChannelInfoTable.setStatus("current")
_BearerChannelInfoEntry_Object = MibTableRow
bearerChannelInfoEntry = _BearerChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 200, 100, 1)
)
bearerChannelInfoEntry.setIndexNames(
    (0, "MX-R2-MIB", "bearerChannelInfoIndex"),
)
if mibBuilder.loadTexts:
    bearerChannelInfoEntry.setStatus("current")
_BearerChannelInfoIndex_Type = OctetString
_BearerChannelInfoIndex_Object = MibTableColumn
bearerChannelInfoIndex = _BearerChannelInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 200, 100, 1, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 200, 100, 1, 200),
    _BearerChannelInfoState_Type()
)
bearerChannelInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerChannelInfoState.setStatus("current")
_PhysicalGroup_ObjectIdentity = ObjectIdentity
physicalGroup = _PhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300)
)
_PhysicalLinkInfoTable_Object = MibTable
physicalLinkInfoTable = _PhysicalLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 100)
)
if mibBuilder.loadTexts:
    physicalLinkInfoTable.setStatus("current")
_PhysicalLinkInfoEntry_Object = MibTableRow
physicalLinkInfoEntry = _PhysicalLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 100, 1)
)
physicalLinkInfoEntry.setIndexNames(
    (0, "MX-R2-MIB", "physicalLinkInfoInterfaceName"),
)
if mibBuilder.loadTexts:
    physicalLinkInfoEntry.setStatus("current")
_PhysicalLinkInfoInterfaceName_Type = OctetString
_PhysicalLinkInfoInterfaceName_Object = MibTableColumn
physicalLinkInfoInterfaceName = _PhysicalLinkInfoInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 100, 1, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 100, 1, 200),
    _PhysicalLinkInfoState_Type()
)
physicalLinkInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInfoState.setStatus("current")
_PhysicalLinkTable_Object = MibTable
physicalLinkTable = _PhysicalLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200)
)
if mibBuilder.loadTexts:
    physicalLinkTable.setStatus("current")
_PhysicalLinkEntry_Object = MibTableRow
physicalLinkEntry = _PhysicalLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1)
)
physicalLinkEntry.setIndexNames(
    (0, "MX-R2-MIB", "physicalLinkInterfaceName"),
)
if mibBuilder.loadTexts:
    physicalLinkEntry.setStatus("current")
_PhysicalLinkInterfaceName_Type = OctetString
_PhysicalLinkInterfaceName_Object = MibTableColumn
physicalLinkInterfaceName = _PhysicalLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1, 100),
    _PhysicalLinkInterfaceName_Type()
)
physicalLinkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLinkInterfaceName.setStatus("current")


class _PhysicalLinkLineCoding_Type(Integer32):
    """Custom type physicalLinkLineCoding based on Integer32"""
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


_PhysicalLinkLineCoding_Type.__name__ = "Integer32"
_PhysicalLinkLineCoding_Object = MibTableColumn
physicalLinkLineCoding = _PhysicalLinkLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1, 200),
    _PhysicalLinkLineCoding_Type()
)
physicalLinkLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkLineCoding.setStatus("current")


class _PhysicalLinkLineFraming_Type(Integer32):
    """Custom type physicalLinkLineFraming based on Integer32"""
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


_PhysicalLinkLineFraming_Type.__name__ = "Integer32"
_PhysicalLinkLineFraming_Object = MibTableColumn
physicalLinkLineFraming = _PhysicalLinkLineFraming_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1, 300),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1, 400),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1, 500),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 300, 200, 1, 600),
    _PhysicalLinkPortPinout_Type()
)
physicalLinkPortPinout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalLinkPortPinout.setStatus("current")
_AutoConfigure_ObjectIdentity = ObjectIdentity
autoConfigure = _AutoConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 400)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 400, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 400, 200),
    _LastAutoConfigureResult_Type()
)
lastAutoConfigureResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAutoConfigureResult.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1875, 1, 60020, 100),
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
    "MX-R2-MIB",
    **{"r2MIB": r2MIB,
       "r2MIBObjects": r2MIBObjects,
       "r2Group": r2Group,
       "r2Table": r2Table,
       "r2Entry": r2Entry,
       "r2Name": r2Name,
       "r2ChannelRange": r2ChannelRange,
       "r2ChannelAllocationStrategy": r2ChannelAllocationStrategy,
       "r2MaxActiveCalls": r2MaxActiveCalls,
       "r2EncodingScheme": r2EncodingScheme,
       "r2LineSignaling": r2LineSignaling,
       "r2IncomingDigitSignaling": r2IncomingDigitSignaling,
       "r2OutgoingDigitSignaling": r2OutgoingDigitSignaling,
       "r2CountrySelection": r2CountrySelection,
       "r2DigitAttenuation": r2DigitAttenuation,
       "r2SignalingVariantsTable": r2SignalingVariantsTable,
       "r2SignalingVariantsEntry": r2SignalingVariantsEntry,
       "r2SignalingVariantsInterfaceName": r2SignalingVariantsInterfaceName,
       "r2SignalingVariantsOverrideDefault": r2SignalingVariantsOverrideDefault,
       "r2SignalingVariantsBitsCD": r2SignalingVariantsBitsCD,
       "r2SignalingVariantsDnisLength": r2SignalingVariantsDnisLength,
       "r2SignalingVariantsAniLength": r2SignalingVariantsAniLength,
       "r2SignalingVariantsAniRequestEnable": r2SignalingVariantsAniRequestEnable,
       "r2SignalingVariantsSendAniRequestAfterDnisDigits": r2SignalingVariantsSendAniRequestAfterDnisDigits,
       "r2SignalingVariantsCollectCallBlocked": r2SignalingVariantsCollectCallBlocked,
       "r2SignalingVariantsAniCategory": r2SignalingVariantsAniCategory,
       "r2SignalingVariantsLineFreeCategory": r2SignalingVariantsLineFreeCategory,
       "r2SignalingVariantsAniRestrictedEnable": r2SignalingVariantsAniRestrictedEnable,
       "r2SignalingVariantsIncomingDeclineMethod": r2SignalingVariantsIncomingDeclineMethod,
       "r2SignalingVariantsResetSpecific": r2SignalingVariantsResetSpecific,
       "r2TimerVariantsTable": r2TimerVariantsTable,
       "r2TimerVariantsEntry": r2TimerVariantsEntry,
       "r2TimerVariantsInterfaceName": r2TimerVariantsInterfaceName,
       "r2TimerVariantsOverrideDefault": r2TimerVariantsOverrideDefault,
       "r2TimerVariantsSeizureAckTimeout": r2TimerVariantsSeizureAckTimeout,
       "r2TimerVariantsFaultSeizureAckTimeout": r2TimerVariantsFaultSeizureAckTimeout,
       "r2TimerVariantsDoubleSeizureTimeout": r2TimerVariantsDoubleSeizureTimeout,
       "r2TimerVariantsDoubleAnswerTimeout": r2TimerVariantsDoubleAnswerTimeout,
       "r2TimerVariantsAnswerTimeout": r2TimerVariantsAnswerTimeout,
       "r2TimerVariantsReAnswerTimeout": r2TimerVariantsReAnswerTimeout,
       "r2TimerVariantsReleaseGuardTimeout": r2TimerVariantsReleaseGuardTimeout,
       "r2TimerVariantsInterCallGuardTimeout": r2TimerVariantsInterCallGuardTimeout,
       "r2TimerVariantsNoDigitTimeout": r2TimerVariantsNoDigitTimeout,
       "r2TimerVariantsCongestionToneGuardTimeout": r2TimerVariantsCongestionToneGuardTimeout,
       "r2TimerVariantsUnblockingTimeout": r2TimerVariantsUnblockingTimeout,
       "r2TimerVariantsAddressCompleteTimeout": r2TimerVariantsAddressCompleteTimeout,
       "r2TimerVariantsWaitAnswerTimeout": r2TimerVariantsWaitAnswerTimeout,
       "r2TimerVariantsDigitCompleteTimeout": r2TimerVariantsDigitCompleteTimeout,
       "r2TimerVariantsWaitGroupBResponseCompleteTimeout": r2TimerVariantsWaitGroupBResponseCompleteTimeout,
       "r2TimerVariantsWaitImmediateResponseCompleteTimeout": r2TimerVariantsWaitImmediateResponseCompleteTimeout,
       "r2TimerVariantsPlayToneGuardTimeout": r2TimerVariantsPlayToneGuardTimeout,
       "r2TimerVariantsAcceptCallTimeout": r2TimerVariantsAcceptCallTimeout,
       "r2TimerVariantsClearForwardGuardTimeout": r2TimerVariantsClearForwardGuardTimeout,
       "r2TimerVariantsClearBackwardGuardTimeout": r2TimerVariantsClearBackwardGuardTimeout,
       "r2TimerVariantsFaultOnAnsweredGuardTimeout": r2TimerVariantsFaultOnAnsweredGuardTimeout,
       "r2TimerVariantsFaultOnClearBackwardGuardTimeout": r2TimerVariantsFaultOnClearBackwardGuardTimeout,
       "r2TimerVariantsFaultOnSeizeAckGuardTimeout": r2TimerVariantsFaultOnSeizeAckGuardTimeout,
       "r2TimerVariantsFaultOnSeizeGuardTimeout": r2TimerVariantsFaultOnSeizeGuardTimeout,
       "r2TimerVariantsDeclineGuardTimeout": r2TimerVariantsDeclineGuardTimeout,
       "r2TimerVariantsResetSpecific": r2TimerVariantsResetSpecific,
       "r2DigitTimerVariantsTable": r2DigitTimerVariantsTable,
       "r2DigitTimerVariantsEntry": r2DigitTimerVariantsEntry,
       "r2DigitTimerVariantsInterfaceName": r2DigitTimerVariantsInterfaceName,
       "r2DigitTimerVariantsOverrideDefault": r2DigitTimerVariantsOverrideDefault,
       "r2DigitTimerVariantsMfCongestionToneDuration": r2DigitTimerVariantsMfCongestionToneDuration,
       "r2DigitTimerVariantsMfcPulseInterDigitTimeout": r2DigitTimerVariantsMfcPulseInterDigitTimeout,
       "r2DigitTimerVariantsMfcPulseMinOnTimeout": r2DigitTimerVariantsMfcPulseMinOnTimeout,
       "r2DigitTimerVariantsMfcMaxSequenceTimeout": r2DigitTimerVariantsMfcMaxSequenceTimeout,
       "r2DigitTimerVariantsMfcMaxOnTimeout": r2DigitTimerVariantsMfcMaxOnTimeout,
       "r2DigitTimerVariantsMfcMaxOffTimeout": r2DigitTimerVariantsMfcMaxOffTimeout,
       "r2DigitTimerVariantsResetSpecific": r2DigitTimerVariantsResetSpecific,
       "r2LinkTimerVariantsTable": r2LinkTimerVariantsTable,
       "r2LinkTimerVariantsEntry": r2LinkTimerVariantsEntry,
       "r2LinkTimerVariantsInterfaceName": r2LinkTimerVariantsInterfaceName,
       "r2LinkTimerVariantsOverrideDefault": r2LinkTimerVariantsOverrideDefault,
       "r2LinkTimerVariantsLinkActivationTimeout": r2LinkTimerVariantsLinkActivationTimeout,
       "r2LinkTimerVariantsLinkActivationRetryTimeout": r2LinkTimerVariantsLinkActivationRetryTimeout,
       "r2LinkTimerVariantsResetSpecific": r2LinkTimerVariantsResetSpecific,
       "r2ToneVariantsTable": r2ToneVariantsTable,
       "r2ToneVariantsEntry": r2ToneVariantsEntry,
       "r2ToneVariantsInterfaceName": r2ToneVariantsInterfaceName,
       "r2ToneVariantsOverrideDefault": r2ToneVariantsOverrideDefault,
       "r2ToneVariantsFwdGroup1EndOfDnis": r2ToneVariantsFwdGroup1EndOfDnis,
       "r2ToneVariantsFwdGroup1EndOfAni": r2ToneVariantsFwdGroup1EndOfAni,
       "r2ToneVariantsFwdGroup1RestrictedAni": r2ToneVariantsFwdGroup1RestrictedAni,
       "r2ToneVariantsBwdGroupASendNextDnisDigit": r2ToneVariantsBwdGroupASendNextDnisDigit,
       "r2ToneVariantsBwdGroupASendPreviousDnisDigit": r2ToneVariantsBwdGroupASendPreviousDnisDigit,
       "r2ToneVariantsBwdGroupASwitchToGroupII": r2ToneVariantsBwdGroupASwitchToGroupII,
       "r2ToneVariantsBwdGroupANetworkCongestion": r2ToneVariantsBwdGroupANetworkCongestion,
       "r2ToneVariantsBwdGroupASendCallingPartyCategory": r2ToneVariantsBwdGroupASendCallingPartyCategory,
       "r2ToneVariantsBwdGroupAImmediateAccept": r2ToneVariantsBwdGroupAImmediateAccept,
       "r2ToneVariantsBwdGroupASendDnisDigitNMinus2": r2ToneVariantsBwdGroupASendDnisDigitNMinus2,
       "r2ToneVariantsBwdGroupASendDnisDigitNMinus3": r2ToneVariantsBwdGroupASendDnisDigitNMinus3,
       "r2ToneVariantsBwdGroupARepeatAllDnis": r2ToneVariantsBwdGroupARepeatAllDnis,
       "r2ToneVariantsBwdGroupASendNextAniDigit": r2ToneVariantsBwdGroupASendNextAniDigit,
       "r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC": r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC,
       "r2ToneVariantsBwdGroupBSendSit": r2ToneVariantsBwdGroupBSendSit,
       "r2ToneVariantsBwdGroupBUserBusy": r2ToneVariantsBwdGroupBUserBusy,
       "r2ToneVariantsBwdGroupBNetworkCongestion": r2ToneVariantsBwdGroupBNetworkCongestion,
       "r2ToneVariantsBwdGroupBUnassignedNumber": r2ToneVariantsBwdGroupBUnassignedNumber,
       "r2ToneVariantsBwdGroupBLineFreeCharge": r2ToneVariantsBwdGroupBLineFreeCharge,
       "r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge": r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge,
       "r2ToneVariantsBwdGroupBLineFreeNoCharge": r2ToneVariantsBwdGroupBLineFreeNoCharge,
       "r2ToneVariantsBwdGroupBLineOutOfOrder": r2ToneVariantsBwdGroupBLineOutOfOrder,
       "r2ToneVariantsBwdGroupBChangedNumber": r2ToneVariantsBwdGroupBChangedNumber,
       "r2ToneVariantsBwdGroupCSendNextAniDigit": r2ToneVariantsBwdGroupCSendNextAniDigit,
       "r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA": r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA,
       "r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA": r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA,
       "r2ToneVariantsBwdGroupCNetworkCongestion": r2ToneVariantsBwdGroupCNetworkCongestion,
       "r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA": r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA,
       "r2ToneVariantsBwdGroupCSwitchGroupII": r2ToneVariantsBwdGroupCSwitchGroupII,
       "r2ToneVariantsResetSpecific": r2ToneVariantsResetSpecific,
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
