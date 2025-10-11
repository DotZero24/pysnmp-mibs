# SNMP MIB module (MX-TELIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-TELIF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:15 2025
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

telIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelIfMIBObjects_ObjectIdentity = ObjectIdentity
telIfMIBObjects = _TelIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1)
)


class _CountrySelection_Type(Integer32):
    """Custom type countrySelection based on Integer32"""
    defaultValue = 17000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(900,
              1000,
              1100,
              2000,
              3000,
              4000,
              4500,
              5000,
              6000,
              7000,
              7100,
              10100,
              11000,
              12100,
              14000,
              15000,
              16000,
              17000,
              18000,
              19000,
              20000,
              21000,
              23100,
              23200,
              23300,
              24000)
        )
    )
    namedValues = NamedValues(
        *(("argentina1", 900),
          ("australia1", 1000),
          ("australia2", 1100),
          ("austria1", 2000),
          ("brazil1", 3000),
          ("china1", 4000),
          ("czechRepublic1", 4500),
          ("denmark1", 5000),
          ("france1", 6000),
          ("germany1", 7000),
          ("germany2", 7100),
          ("israel2", 10100),
          ("italy1", 11000),
          ("japan2", 12100),
          ("mexico1", 14000),
          ("netherlands1", 15000),
          ("newZealand1", 16000),
          ("northAmerica1", 17000),
          ("russia1", 18000),
          ("spain1", 19000),
          ("sweden1", 20000),
          ("switzerland1", 21000),
          ("uae2", 23100),
          ("uae3", 23200),
          ("uae4", 23300),
          ("uk1", 24000))
    )


_CountrySelection_Type.__name__ = "Integer32"
_CountrySelection_Object = MibScalar
countrySelection = _CountrySelection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 100),
    _CountrySelection_Type()
)
countrySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countrySelection.setStatus("current")
_CountryCustomizationGroup_ObjectIdentity = ObjectIdentity
countryCustomizationGroup = _CountryCustomizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200)
)
_CountryCustomizationUserGainGroup_ObjectIdentity = ObjectIdentity
countryCustomizationUserGainGroup = _CountryCustomizationUserGainGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100)
)


class _DefaultCountryCustomizationUserGainInputOffset_Type(Integer32):
    """Custom type defaultCountryCustomizationUserGainInputOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_DefaultCountryCustomizationUserGainInputOffset_Type.__name__ = "Integer32"
_DefaultCountryCustomizationUserGainInputOffset_Object = MibScalar
defaultCountryCustomizationUserGainInputOffset = _DefaultCountryCustomizationUserGainInputOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 100),
    _DefaultCountryCustomizationUserGainInputOffset_Type()
)
defaultCountryCustomizationUserGainInputOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationUserGainInputOffset.setStatus("current")


class _DefaultCountryCustomizationUserGainOutputOffset_Type(Integer32):
    """Custom type defaultCountryCustomizationUserGainOutputOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_DefaultCountryCustomizationUserGainOutputOffset_Type.__name__ = "Integer32"
_DefaultCountryCustomizationUserGainOutputOffset_Object = MibScalar
defaultCountryCustomizationUserGainOutputOffset = _DefaultCountryCustomizationUserGainOutputOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 200),
    _DefaultCountryCustomizationUserGainOutputOffset_Type()
)
defaultCountryCustomizationUserGainOutputOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationUserGainOutputOffset.setStatus("current")
_SpecificCountryCustomizationUserGainTable_Object = MibTable
specificCountryCustomizationUserGainTable = _SpecificCountryCustomizationUserGainTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 300)
)
if mibBuilder.loadTexts:
    specificCountryCustomizationUserGainTable.setStatus("current")
_SpecificCountryCustomizationUserGainEntry_Object = MibTableRow
specificCountryCustomizationUserGainEntry = _SpecificCountryCustomizationUserGainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 300, 1)
)
specificCountryCustomizationUserGainEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "specificCountryCustomizationUserGainInterfaceId"),
)
if mibBuilder.loadTexts:
    specificCountryCustomizationUserGainEntry.setStatus("current")
_SpecificCountryCustomizationUserGainInterfaceId_Type = OctetString
_SpecificCountryCustomizationUserGainInterfaceId_Object = MibTableColumn
specificCountryCustomizationUserGainInterfaceId = _SpecificCountryCustomizationUserGainInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 300, 1, 100),
    _SpecificCountryCustomizationUserGainInterfaceId_Type()
)
specificCountryCustomizationUserGainInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificCountryCustomizationUserGainInterfaceId.setStatus("current")


class _SpecificCountryCustomizationUserGainEnableConfig_Type(MxEnableState):
    """Custom type specificCountryCustomizationUserGainEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificCountryCustomizationUserGainEnableConfig_Type.__name__ = "MxEnableState"
_SpecificCountryCustomizationUserGainEnableConfig_Object = MibTableColumn
specificCountryCustomizationUserGainEnableConfig = _SpecificCountryCustomizationUserGainEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 300, 1, 200),
    _SpecificCountryCustomizationUserGainEnableConfig_Type()
)
specificCountryCustomizationUserGainEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationUserGainEnableConfig.setStatus("current")


class _SpecificCountryCustomizationUserGainInputOffset_Type(Integer32):
    """Custom type specificCountryCustomizationUserGainInputOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_SpecificCountryCustomizationUserGainInputOffset_Type.__name__ = "Integer32"
_SpecificCountryCustomizationUserGainInputOffset_Object = MibTableColumn
specificCountryCustomizationUserGainInputOffset = _SpecificCountryCustomizationUserGainInputOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 300, 1, 300),
    _SpecificCountryCustomizationUserGainInputOffset_Type()
)
specificCountryCustomizationUserGainInputOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationUserGainInputOffset.setStatus("current")


class _SpecificCountryCustomizationUserGainOutputOffset_Type(Integer32):
    """Custom type specificCountryCustomizationUserGainOutputOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_SpecificCountryCustomizationUserGainOutputOffset_Type.__name__ = "Integer32"
_SpecificCountryCustomizationUserGainOutputOffset_Object = MibTableColumn
specificCountryCustomizationUserGainOutputOffset = _SpecificCountryCustomizationUserGainOutputOffset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 100, 300, 1, 400),
    _SpecificCountryCustomizationUserGainOutputOffset_Type()
)
specificCountryCustomizationUserGainOutputOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationUserGainOutputOffset.setStatus("current")
_CountryCustomizationDialingGroup_ObjectIdentity = ObjectIdentity
countryCustomizationDialingGroup = _CountryCustomizationDialingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400)
)


class _DefaultCountryCustomizationDialingOverride_Type(MxEnableState):
    """Custom type defaultCountryCustomizationDialingOverride based on MxEnableState"""
    defaultValue = 0


_DefaultCountryCustomizationDialingOverride_Type.__name__ = "MxEnableState"
_DefaultCountryCustomizationDialingOverride_Object = MibScalar
defaultCountryCustomizationDialingOverride = _DefaultCountryCustomizationDialingOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 100),
    _DefaultCountryCustomizationDialingOverride_Type()
)
defaultCountryCustomizationDialingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationDialingOverride.setStatus("current")


class _DefaultCountryCustomizationDialingInterDtmfDialDelay_Type(Unsigned32):
    """Custom type defaultCountryCustomizationDialingInterDtmfDialDelay based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_DefaultCountryCustomizationDialingInterDtmfDialDelay_Type.__name__ = "Unsigned32"
_DefaultCountryCustomizationDialingInterDtmfDialDelay_Object = MibScalar
defaultCountryCustomizationDialingInterDtmfDialDelay = _DefaultCountryCustomizationDialingInterDtmfDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 200),
    _DefaultCountryCustomizationDialingInterDtmfDialDelay_Type()
)
defaultCountryCustomizationDialingInterDtmfDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationDialingInterDtmfDialDelay.setStatus("current")


class _DefaultCountryCustomizationDialingDtmfDuration_Type(Unsigned32):
    """Custom type defaultCountryCustomizationDialingDtmfDuration based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_DefaultCountryCustomizationDialingDtmfDuration_Type.__name__ = "Unsigned32"
_DefaultCountryCustomizationDialingDtmfDuration_Object = MibScalar
defaultCountryCustomizationDialingDtmfDuration = _DefaultCountryCustomizationDialingDtmfDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 300),
    _DefaultCountryCustomizationDialingDtmfDuration_Type()
)
defaultCountryCustomizationDialingDtmfDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationDialingDtmfDuration.setStatus("current")


class _DefaultCountryCustomizationDialingInterMfR1DialDelay_Type(Unsigned32):
    """Custom type defaultCountryCustomizationDialingInterMfR1DialDelay based on Unsigned32"""
    defaultValue = 68

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_DefaultCountryCustomizationDialingInterMfR1DialDelay_Type.__name__ = "Unsigned32"
_DefaultCountryCustomizationDialingInterMfR1DialDelay_Object = MibScalar
defaultCountryCustomizationDialingInterMfR1DialDelay = _DefaultCountryCustomizationDialingInterMfR1DialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 340),
    _DefaultCountryCustomizationDialingInterMfR1DialDelay_Type()
)
defaultCountryCustomizationDialingInterMfR1DialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationDialingInterMfR1DialDelay.setStatus("current")


class _DefaultCountryCustomizationDialingMfR1Duration_Type(Unsigned32):
    """Custom type defaultCountryCustomizationDialingMfR1Duration based on Unsigned32"""
    defaultValue = 68

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_DefaultCountryCustomizationDialingMfR1Duration_Type.__name__ = "Unsigned32"
_DefaultCountryCustomizationDialingMfR1Duration_Object = MibScalar
defaultCountryCustomizationDialingMfR1Duration = _DefaultCountryCustomizationDialingMfR1Duration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 370),
    _DefaultCountryCustomizationDialingMfR1Duration_Type()
)
defaultCountryCustomizationDialingMfR1Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCountryCustomizationDialingMfR1Duration.setStatus("current")
_SpecificCountryCustomizationDialingTable_Object = MibTable
specificCountryCustomizationDialingTable = _SpecificCountryCustomizationDialingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400)
)
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingTable.setStatus("current")
_SpecificCountryCustomizationDialingEntry_Object = MibTableRow
specificCountryCustomizationDialingEntry = _SpecificCountryCustomizationDialingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1)
)
specificCountryCustomizationDialingEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "specificCountryCustomizationDialingInterfaceId"),
)
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingEntry.setStatus("current")
_SpecificCountryCustomizationDialingInterfaceId_Type = OctetString
_SpecificCountryCustomizationDialingInterfaceId_Object = MibTableColumn
specificCountryCustomizationDialingInterfaceId = _SpecificCountryCustomizationDialingInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 100),
    _SpecificCountryCustomizationDialingInterfaceId_Type()
)
specificCountryCustomizationDialingInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingInterfaceId.setStatus("current")


class _SpecificCountryCustomizationDialingEnableConfig_Type(MxEnableState):
    """Custom type specificCountryCustomizationDialingEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificCountryCustomizationDialingEnableConfig_Type.__name__ = "MxEnableState"
_SpecificCountryCustomizationDialingEnableConfig_Object = MibTableColumn
specificCountryCustomizationDialingEnableConfig = _SpecificCountryCustomizationDialingEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 200),
    _SpecificCountryCustomizationDialingEnableConfig_Type()
)
specificCountryCustomizationDialingEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingEnableConfig.setStatus("current")


class _SpecificCountryCustomizationDialingOverride_Type(MxEnableState):
    """Custom type specificCountryCustomizationDialingOverride based on MxEnableState"""
    defaultValue = 0


_SpecificCountryCustomizationDialingOverride_Type.__name__ = "MxEnableState"
_SpecificCountryCustomizationDialingOverride_Object = MibTableColumn
specificCountryCustomizationDialingOverride = _SpecificCountryCustomizationDialingOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 300),
    _SpecificCountryCustomizationDialingOverride_Type()
)
specificCountryCustomizationDialingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingOverride.setStatus("current")


class _SpecificCountryCustomizationDialingInterDtmfDialDelay_Type(Unsigned32):
    """Custom type specificCountryCustomizationDialingInterDtmfDialDelay based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_SpecificCountryCustomizationDialingInterDtmfDialDelay_Type.__name__ = "Unsigned32"
_SpecificCountryCustomizationDialingInterDtmfDialDelay_Object = MibTableColumn
specificCountryCustomizationDialingInterDtmfDialDelay = _SpecificCountryCustomizationDialingInterDtmfDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 400),
    _SpecificCountryCustomizationDialingInterDtmfDialDelay_Type()
)
specificCountryCustomizationDialingInterDtmfDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingInterDtmfDialDelay.setStatus("current")


class _SpecificCountryCustomizationDialingDtmfDuration_Type(Unsigned32):
    """Custom type specificCountryCustomizationDialingDtmfDuration based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_SpecificCountryCustomizationDialingDtmfDuration_Type.__name__ = "Unsigned32"
_SpecificCountryCustomizationDialingDtmfDuration_Object = MibTableColumn
specificCountryCustomizationDialingDtmfDuration = _SpecificCountryCustomizationDialingDtmfDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 500),
    _SpecificCountryCustomizationDialingDtmfDuration_Type()
)
specificCountryCustomizationDialingDtmfDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingDtmfDuration.setStatus("current")


class _SpecificCountryCustomizationDialingInterMfR1DialDelay_Type(Unsigned32):
    """Custom type specificCountryCustomizationDialingInterMfR1DialDelay based on Unsigned32"""
    defaultValue = 68

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_SpecificCountryCustomizationDialingInterMfR1DialDelay_Type.__name__ = "Unsigned32"
_SpecificCountryCustomizationDialingInterMfR1DialDelay_Object = MibTableColumn
specificCountryCustomizationDialingInterMfR1DialDelay = _SpecificCountryCustomizationDialingInterMfR1DialDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 600),
    _SpecificCountryCustomizationDialingInterMfR1DialDelay_Type()
)
specificCountryCustomizationDialingInterMfR1DialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingInterMfR1DialDelay.setStatus("current")


class _SpecificCountryCustomizationDialingMfR1Duration_Type(Unsigned32):
    """Custom type specificCountryCustomizationDialingMfR1Duration based on Unsigned32"""
    defaultValue = 68

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_SpecificCountryCustomizationDialingMfR1Duration_Type.__name__ = "Unsigned32"
_SpecificCountryCustomizationDialingMfR1Duration_Object = MibTableColumn
specificCountryCustomizationDialingMfR1Duration = _SpecificCountryCustomizationDialingMfR1Duration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 400, 400, 1, 700),
    _SpecificCountryCustomizationDialingMfR1Duration_Type()
)
specificCountryCustomizationDialingMfR1Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificCountryCustomizationDialingMfR1Duration.setStatus("current")
_CountryCustomizationToneGroup_ObjectIdentity = ObjectIdentity
countryCustomizationToneGroup = _CountryCustomizationToneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500)
)
_CountryToneStatusTable_Object = MibTable
countryToneStatusTable = _CountryToneStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 100)
)
if mibBuilder.loadTexts:
    countryToneStatusTable.setStatus("current")
_CountryToneStatusEntry_Object = MibTableRow
countryToneStatusEntry = _CountryToneStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 100, 1)
)
countryToneStatusEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "countryToneStatusTone"),
)
if mibBuilder.loadTexts:
    countryToneStatusEntry.setStatus("current")


class _CountryToneStatusTone_Type(Integer32):
    """Custom type countryToneStatusTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              150,
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
              1300)
        )
    )
    namedValues = NamedValues(
        *(("busy", 100),
          ("callWaiting", 150),
          ("confirmation", 200),
          ("congestion", 300),
          ("dial", 400),
          ("hold", 500),
          ("intercept", 600),
          ("messageWaiting", 700),
          ("preemption", 800),
          ("reorder", 900),
          ("ringback", 1000),
          ("roh", 1100),
          ("sit", 1200),
          ("stutter", 1300))
    )


_CountryToneStatusTone_Type.__name__ = "Integer32"
_CountryToneStatusTone_Object = MibTableColumn
countryToneStatusTone = _CountryToneStatusTone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 100, 1, 100),
    _CountryToneStatusTone_Type()
)
countryToneStatusTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countryToneStatusTone.setStatus("current")


class _CountryToneStatusPattern_Type(OctetString):
    """Custom type countryToneStatusPattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CountryToneStatusPattern_Type.__name__ = "OctetString"
_CountryToneStatusPattern_Object = MibTableColumn
countryToneStatusPattern = _CountryToneStatusPattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 100, 1, 300),
    _CountryToneStatusPattern_Type()
)
countryToneStatusPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countryToneStatusPattern.setStatus("current")
_CountryCustomizationToneTable_Object = MibTable
countryCustomizationToneTable = _CountryCustomizationToneTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 200)
)
if mibBuilder.loadTexts:
    countryCustomizationToneTable.setStatus("current")
_CountryCustomizationToneEntry_Object = MibTableRow
countryCustomizationToneEntry = _CountryCustomizationToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 200, 1)
)
countryCustomizationToneEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "countryCustomizationToneTone"),
)
if mibBuilder.loadTexts:
    countryCustomizationToneEntry.setStatus("current")


class _CountryCustomizationToneTone_Type(Integer32):
    """Custom type countryCustomizationToneTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              150,
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
              1300)
        )
    )
    namedValues = NamedValues(
        *(("busy", 100),
          ("callWaiting", 150),
          ("confirmation", 200),
          ("congestion", 300),
          ("dial", 400),
          ("hold", 500),
          ("intercept", 600),
          ("messageWaiting", 700),
          ("preemption", 800),
          ("reorder", 900),
          ("ringback", 1000),
          ("roh", 1100),
          ("sit", 1200),
          ("stutter", 1300))
    )


_CountryCustomizationToneTone_Type.__name__ = "Integer32"
_CountryCustomizationToneTone_Object = MibTableColumn
countryCustomizationToneTone = _CountryCustomizationToneTone_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 200, 1, 100),
    _CountryCustomizationToneTone_Type()
)
countryCustomizationToneTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countryCustomizationToneTone.setStatus("current")


class _CountryCustomizationToneOverride_Type(MxEnableState):
    """Custom type countryCustomizationToneOverride based on MxEnableState"""
    defaultValue = 0


_CountryCustomizationToneOverride_Type.__name__ = "MxEnableState"
_CountryCustomizationToneOverride_Object = MibTableColumn
countryCustomizationToneOverride = _CountryCustomizationToneOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 200, 1, 200),
    _CountryCustomizationToneOverride_Type()
)
countryCustomizationToneOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countryCustomizationToneOverride.setStatus("current")


class _CountryCustomizationTonePattern_Type(OctetString):
    """Custom type countryCustomizationTonePattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CountryCustomizationTonePattern_Type.__name__ = "OctetString"
_CountryCustomizationTonePattern_Object = MibTableColumn
countryCustomizationTonePattern = _CountryCustomizationTonePattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 200, 500, 200, 1, 300),
    _CountryCustomizationTonePattern_Type()
)
countryCustomizationTonePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countryCustomizationTonePattern.setStatus("current")
_MachineDetectionGroup_ObjectIdentity = ObjectIdentity
machineDetectionGroup = _MachineDetectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300)
)


class _DefaultMachineDetectionCngToneDetection_Type(MxEnableState):
    """Custom type defaultMachineDetectionCngToneDetection based on MxEnableState"""
    defaultValue = 1


_DefaultMachineDetectionCngToneDetection_Type.__name__ = "MxEnableState"
_DefaultMachineDetectionCngToneDetection_Object = MibScalar
defaultMachineDetectionCngToneDetection = _DefaultMachineDetectionCngToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 100),
    _DefaultMachineDetectionCngToneDetection_Type()
)
defaultMachineDetectionCngToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMachineDetectionCngToneDetection.setStatus("current")


class _DefaultMachineDetectionCedToneDetection_Type(MxEnableState):
    """Custom type defaultMachineDetectionCedToneDetection based on MxEnableState"""
    defaultValue = 1


_DefaultMachineDetectionCedToneDetection_Type.__name__ = "MxEnableState"
_DefaultMachineDetectionCedToneDetection_Object = MibScalar
defaultMachineDetectionCedToneDetection = _DefaultMachineDetectionCedToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 101),
    _DefaultMachineDetectionCedToneDetection_Type()
)
defaultMachineDetectionCedToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMachineDetectionCedToneDetection.setStatus("current")


class _DefaultMachineDetectionV21ModulationDetection_Type(MxEnableState):
    """Custom type defaultMachineDetectionV21ModulationDetection based on MxEnableState"""
    defaultValue = 1


_DefaultMachineDetectionV21ModulationDetection_Type.__name__ = "MxEnableState"
_DefaultMachineDetectionV21ModulationDetection_Object = MibScalar
defaultMachineDetectionV21ModulationDetection = _DefaultMachineDetectionV21ModulationDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 102),
    _DefaultMachineDetectionV21ModulationDetection_Type()
)
defaultMachineDetectionV21ModulationDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMachineDetectionV21ModulationDetection.setStatus("current")


class _DefaultMachineDetectionBehaviorOnCedToneDetection_Type(Integer32):
    """Custom type defaultMachineDetectionBehaviorOnCedToneDetection based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 100),
          ("faxmode", 200))
    )


_DefaultMachineDetectionBehaviorOnCedToneDetection_Type.__name__ = "Integer32"
_DefaultMachineDetectionBehaviorOnCedToneDetection_Object = MibScalar
defaultMachineDetectionBehaviorOnCedToneDetection = _DefaultMachineDetectionBehaviorOnCedToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 110),
    _DefaultMachineDetectionBehaviorOnCedToneDetection_Type()
)
defaultMachineDetectionBehaviorOnCedToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMachineDetectionBehaviorOnCedToneDetection.setStatus("current")
_SpecificMachineDetectionTable_Object = MibTable
specificMachineDetectionTable = _SpecificMachineDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200)
)
if mibBuilder.loadTexts:
    specificMachineDetectionTable.setStatus("current")
_SpecificMachineDetectionEntry_Object = MibTableRow
specificMachineDetectionEntry = _SpecificMachineDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1)
)
specificMachineDetectionEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "specificMachineDetectionInterfaceId"),
)
if mibBuilder.loadTexts:
    specificMachineDetectionEntry.setStatus("current")
_SpecificMachineDetectionInterfaceId_Type = OctetString
_SpecificMachineDetectionInterfaceId_Object = MibTableColumn
specificMachineDetectionInterfaceId = _SpecificMachineDetectionInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1, 100),
    _SpecificMachineDetectionInterfaceId_Type()
)
specificMachineDetectionInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificMachineDetectionInterfaceId.setStatus("current")


class _SpecificMachineDetectionEnableConfig_Type(MxEnableState):
    """Custom type specificMachineDetectionEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificMachineDetectionEnableConfig_Type.__name__ = "MxEnableState"
_SpecificMachineDetectionEnableConfig_Object = MibTableColumn
specificMachineDetectionEnableConfig = _SpecificMachineDetectionEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1, 200),
    _SpecificMachineDetectionEnableConfig_Type()
)
specificMachineDetectionEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificMachineDetectionEnableConfig.setStatus("current")


class _SpecificMachineDetectionCngToneDetection_Type(MxEnableState):
    """Custom type specificMachineDetectionCngToneDetection based on MxEnableState"""
    defaultValue = 1


_SpecificMachineDetectionCngToneDetection_Type.__name__ = "MxEnableState"
_SpecificMachineDetectionCngToneDetection_Object = MibTableColumn
specificMachineDetectionCngToneDetection = _SpecificMachineDetectionCngToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1, 300),
    _SpecificMachineDetectionCngToneDetection_Type()
)
specificMachineDetectionCngToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificMachineDetectionCngToneDetection.setStatus("current")


class _SpecificMachineDetectionCedToneDetection_Type(MxEnableState):
    """Custom type specificMachineDetectionCedToneDetection based on MxEnableState"""
    defaultValue = 1


_SpecificMachineDetectionCedToneDetection_Type.__name__ = "MxEnableState"
_SpecificMachineDetectionCedToneDetection_Object = MibTableColumn
specificMachineDetectionCedToneDetection = _SpecificMachineDetectionCedToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1, 310),
    _SpecificMachineDetectionCedToneDetection_Type()
)
specificMachineDetectionCedToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificMachineDetectionCedToneDetection.setStatus("current")


class _SpecificMachineDetectionV21ModulationDetection_Type(MxEnableState):
    """Custom type specificMachineDetectionV21ModulationDetection based on MxEnableState"""
    defaultValue = 1


_SpecificMachineDetectionV21ModulationDetection_Type.__name__ = "MxEnableState"
_SpecificMachineDetectionV21ModulationDetection_Object = MibTableColumn
specificMachineDetectionV21ModulationDetection = _SpecificMachineDetectionV21ModulationDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1, 320),
    _SpecificMachineDetectionV21ModulationDetection_Type()
)
specificMachineDetectionV21ModulationDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificMachineDetectionV21ModulationDetection.setStatus("current")


class _SpecificMachineDetectionBehaviorOnCedToneDetection_Type(Integer32):
    """Custom type specificMachineDetectionBehaviorOnCedToneDetection based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 100),
          ("faxmode", 200))
    )


_SpecificMachineDetectionBehaviorOnCedToneDetection_Type.__name__ = "Integer32"
_SpecificMachineDetectionBehaviorOnCedToneDetection_Object = MibTableColumn
specificMachineDetectionBehaviorOnCedToneDetection = _SpecificMachineDetectionBehaviorOnCedToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 300, 200, 1, 400),
    _SpecificMachineDetectionBehaviorOnCedToneDetection_Type()
)
specificMachineDetectionBehaviorOnCedToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificMachineDetectionBehaviorOnCedToneDetection.setStatus("current")
_MusicOnHoldStreamingGroup_ObjectIdentity = ObjectIdentity
musicOnHoldStreamingGroup = _MusicOnHoldStreamingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 400)
)


class _MusicOnHoldStreamingEnable_Type(MxEnableState):
    """Custom type musicOnHoldStreamingEnable based on MxEnableState"""
    defaultValue = 0


_MusicOnHoldStreamingEnable_Type.__name__ = "MxEnableState"
_MusicOnHoldStreamingEnable_Object = MibScalar
musicOnHoldStreamingEnable = _MusicOnHoldStreamingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 400, 100),
    _MusicOnHoldStreamingEnable_Type()
)
musicOnHoldStreamingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    musicOnHoldStreamingEnable.setStatus("current")
_CallWaitingToneGroup_ObjectIdentity = ObjectIdentity
callWaitingToneGroup = _CallWaitingToneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 500)
)
_DistinctiveCallWaitingToneTable_Object = MibTable
distinctiveCallWaitingToneTable = _DistinctiveCallWaitingToneTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 500, 100)
)
if mibBuilder.loadTexts:
    distinctiveCallWaitingToneTable.setStatus("current")
_DistinctiveCallWaitingToneEntry_Object = MibTableRow
distinctiveCallWaitingToneEntry = _DistinctiveCallWaitingToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 500, 100, 1)
)
distinctiveCallWaitingToneEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "distinctiveCallWaitingToneIndex"),
)
if mibBuilder.loadTexts:
    distinctiveCallWaitingToneEntry.setStatus("current")


class _DistinctiveCallWaitingToneIndex_Type(Unsigned32):
    """Custom type distinctiveCallWaitingToneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DistinctiveCallWaitingToneIndex_Type.__name__ = "Unsigned32"
_DistinctiveCallWaitingToneIndex_Object = MibTableColumn
distinctiveCallWaitingToneIndex = _DistinctiveCallWaitingToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 500, 100, 1, 100),
    _DistinctiveCallWaitingToneIndex_Type()
)
distinctiveCallWaitingToneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distinctiveCallWaitingToneIndex.setStatus("current")


class _DistinctiveCallWaitingToneToneId_Type(OctetString):
    """Custom type distinctiveCallWaitingToneToneId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DistinctiveCallWaitingToneToneId_Type.__name__ = "OctetString"
_DistinctiveCallWaitingToneToneId_Object = MibTableColumn
distinctiveCallWaitingToneToneId = _DistinctiveCallWaitingToneToneId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 500, 100, 1, 200),
    _DistinctiveCallWaitingToneToneId_Type()
)
distinctiveCallWaitingToneToneId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distinctiveCallWaitingToneToneId.setStatus("current")


class _DistinctiveCallWaitingTonePattern_Type(OctetString):
    """Custom type distinctiveCallWaitingTonePattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DistinctiveCallWaitingTonePattern_Type.__name__ = "OctetString"
_DistinctiveCallWaitingTonePattern_Object = MibTableColumn
distinctiveCallWaitingTonePattern = _DistinctiveCallWaitingTonePattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 500, 100, 1, 300),
    _DistinctiveCallWaitingTonePattern_Type()
)
distinctiveCallWaitingTonePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distinctiveCallWaitingTonePattern.setStatus("current")
_InteropGroup_ObjectIdentity = ObjectIdentity
interopGroup = _InteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000)
)
_InteropDtmfDetectionTable_Object = MibTable
interopDtmfDetectionTable = _InteropDtmfDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100)
)
if mibBuilder.loadTexts:
    interopDtmfDetectionTable.setStatus("current")
_InteropDtmfDetectionEntry_Object = MibTableRow
interopDtmfDetectionEntry = _InteropDtmfDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1)
)
interopDtmfDetectionEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "interopDtmfDetectionInterfaceId"),
)
if mibBuilder.loadTexts:
    interopDtmfDetectionEntry.setStatus("current")
_InteropDtmfDetectionInterfaceId_Type = OctetString
_InteropDtmfDetectionInterfaceId_Object = MibTableColumn
interopDtmfDetectionInterfaceId = _InteropDtmfDetectionInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 100),
    _InteropDtmfDetectionInterfaceId_Type()
)
interopDtmfDetectionInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interopDtmfDetectionInterfaceId.setStatus("current")


class _InteropDtmfDetectionRiseTimeCriteria_Type(Integer32):
    """Custom type interopDtmfDetectionRiseTimeCriteria based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("checkSr", 100),
          ("confirmSnr", 200))
    )


_InteropDtmfDetectionRiseTimeCriteria_Type.__name__ = "Integer32"
_InteropDtmfDetectionRiseTimeCriteria_Object = MibTableColumn
interopDtmfDetectionRiseTimeCriteria = _InteropDtmfDetectionRiseTimeCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 200),
    _InteropDtmfDetectionRiseTimeCriteria_Type()
)
interopDtmfDetectionRiseTimeCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfDetectionRiseTimeCriteria.setStatus("current")


class _InteropDtmfDetectionPositiveTwist_Type(Unsigned32):
    """Custom type interopDtmfDetectionPositiveTwist based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_InteropDtmfDetectionPositiveTwist_Type.__name__ = "Unsigned32"
_InteropDtmfDetectionPositiveTwist_Object = MibTableColumn
interopDtmfDetectionPositiveTwist = _InteropDtmfDetectionPositiveTwist_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 300),
    _InteropDtmfDetectionPositiveTwist_Type()
)
interopDtmfDetectionPositiveTwist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfDetectionPositiveTwist.setStatus("current")


class _InteropDtmfDetectionNegativeTwist_Type(Unsigned32):
    """Custom type interopDtmfDetectionNegativeTwist based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_InteropDtmfDetectionNegativeTwist_Type.__name__ = "Unsigned32"
_InteropDtmfDetectionNegativeTwist_Object = MibTableColumn
interopDtmfDetectionNegativeTwist = _InteropDtmfDetectionNegativeTwist_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 350),
    _InteropDtmfDetectionNegativeTwist_Type()
)
interopDtmfDetectionNegativeTwist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfDetectionNegativeTwist.setStatus("current")


class _InteropDtmfDetectionMaxPowerThreshold_Type(Integer32):
    """Custom type interopDtmfDetectionMaxPowerThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 1),
    )


_InteropDtmfDetectionMaxPowerThreshold_Type.__name__ = "Integer32"
_InteropDtmfDetectionMaxPowerThreshold_Object = MibTableColumn
interopDtmfDetectionMaxPowerThreshold = _InteropDtmfDetectionMaxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 400),
    _InteropDtmfDetectionMaxPowerThreshold_Type()
)
interopDtmfDetectionMaxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfDetectionMaxPowerThreshold.setStatus("current")


class _InteropDtmfDetectionMinPowerThreshold_Type(Integer32):
    """Custom type interopDtmfDetectionMinPowerThreshold based on Integer32"""
    defaultValue = -30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, -10),
    )


_InteropDtmfDetectionMinPowerThreshold_Type.__name__ = "Integer32"
_InteropDtmfDetectionMinPowerThreshold_Object = MibTableColumn
interopDtmfDetectionMinPowerThreshold = _InteropDtmfDetectionMinPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 450),
    _InteropDtmfDetectionMinPowerThreshold_Type()
)
interopDtmfDetectionMinPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfDetectionMinPowerThreshold.setStatus("current")


class _InteropDtmfDetectionBreakPowerThreshold_Type(Integer32):
    """Custom type interopDtmfDetectionBreakPowerThreshold based on Integer32"""
    defaultValue = -32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, -12),
    )


_InteropDtmfDetectionBreakPowerThreshold_Type.__name__ = "Integer32"
_InteropDtmfDetectionBreakPowerThreshold_Object = MibTableColumn
interopDtmfDetectionBreakPowerThreshold = _InteropDtmfDetectionBreakPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 100, 1, 500),
    _InteropDtmfDetectionBreakPowerThreshold_Type()
)
interopDtmfDetectionBreakPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfDetectionBreakPowerThreshold.setStatus("current")
_InteropStartCallInVbdTable_Object = MibTable
interopStartCallInVbdTable = _InteropStartCallInVbdTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 200)
)
if mibBuilder.loadTexts:
    interopStartCallInVbdTable.setStatus("current")
_InteropStartCallInVbdEntry_Object = MibTableRow
interopStartCallInVbdEntry = _InteropStartCallInVbdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 200, 1)
)
interopStartCallInVbdEntry.setIndexNames(
    (0, "MX-TELIF-MIB", "interopStartCallInVbdInterfaceId"),
)
if mibBuilder.loadTexts:
    interopStartCallInVbdEntry.setStatus("current")
_InteropStartCallInVbdInterfaceId_Type = OctetString
_InteropStartCallInVbdInterfaceId_Object = MibTableColumn
interopStartCallInVbdInterfaceId = _InteropStartCallInVbdInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 200, 1, 100),
    _InteropStartCallInVbdInterfaceId_Type()
)
interopStartCallInVbdInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interopStartCallInVbdInterfaceId.setStatus("current")


class _InteropStartCallInVbdEnable_Type(MxEnableState):
    """Custom type interopStartCallInVbdEnable based on MxEnableState"""
    defaultValue = 0


_InteropStartCallInVbdEnable_Type.__name__ = "MxEnableState"
_InteropStartCallInVbdEnable_Object = MibTableColumn
interopStartCallInVbdEnable = _InteropStartCallInVbdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 50000, 200, 1, 200),
    _InteropStartCallInVbdEnable_Type()
)
interopStartCallInVbdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopStartCallInVbdEnable.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1775, 1, 60020, 100),
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
    "MX-TELIF-MIB",
    **{"telIfMIB": telIfMIB,
       "telIfMIBObjects": telIfMIBObjects,
       "countrySelection": countrySelection,
       "countryCustomizationGroup": countryCustomizationGroup,
       "countryCustomizationUserGainGroup": countryCustomizationUserGainGroup,
       "defaultCountryCustomizationUserGainInputOffset": defaultCountryCustomizationUserGainInputOffset,
       "defaultCountryCustomizationUserGainOutputOffset": defaultCountryCustomizationUserGainOutputOffset,
       "specificCountryCustomizationUserGainTable": specificCountryCustomizationUserGainTable,
       "specificCountryCustomizationUserGainEntry": specificCountryCustomizationUserGainEntry,
       "specificCountryCustomizationUserGainInterfaceId": specificCountryCustomizationUserGainInterfaceId,
       "specificCountryCustomizationUserGainEnableConfig": specificCountryCustomizationUserGainEnableConfig,
       "specificCountryCustomizationUserGainInputOffset": specificCountryCustomizationUserGainInputOffset,
       "specificCountryCustomizationUserGainOutputOffset": specificCountryCustomizationUserGainOutputOffset,
       "countryCustomizationDialingGroup": countryCustomizationDialingGroup,
       "defaultCountryCustomizationDialingOverride": defaultCountryCustomizationDialingOverride,
       "defaultCountryCustomizationDialingInterDtmfDialDelay": defaultCountryCustomizationDialingInterDtmfDialDelay,
       "defaultCountryCustomizationDialingDtmfDuration": defaultCountryCustomizationDialingDtmfDuration,
       "defaultCountryCustomizationDialingInterMfR1DialDelay": defaultCountryCustomizationDialingInterMfR1DialDelay,
       "defaultCountryCustomizationDialingMfR1Duration": defaultCountryCustomizationDialingMfR1Duration,
       "specificCountryCustomizationDialingTable": specificCountryCustomizationDialingTable,
       "specificCountryCustomizationDialingEntry": specificCountryCustomizationDialingEntry,
       "specificCountryCustomizationDialingInterfaceId": specificCountryCustomizationDialingInterfaceId,
       "specificCountryCustomizationDialingEnableConfig": specificCountryCustomizationDialingEnableConfig,
       "specificCountryCustomizationDialingOverride": specificCountryCustomizationDialingOverride,
       "specificCountryCustomizationDialingInterDtmfDialDelay": specificCountryCustomizationDialingInterDtmfDialDelay,
       "specificCountryCustomizationDialingDtmfDuration": specificCountryCustomizationDialingDtmfDuration,
       "specificCountryCustomizationDialingInterMfR1DialDelay": specificCountryCustomizationDialingInterMfR1DialDelay,
       "specificCountryCustomizationDialingMfR1Duration": specificCountryCustomizationDialingMfR1Duration,
       "countryCustomizationToneGroup": countryCustomizationToneGroup,
       "countryToneStatusTable": countryToneStatusTable,
       "countryToneStatusEntry": countryToneStatusEntry,
       "countryToneStatusTone": countryToneStatusTone,
       "countryToneStatusPattern": countryToneStatusPattern,
       "countryCustomizationToneTable": countryCustomizationToneTable,
       "countryCustomizationToneEntry": countryCustomizationToneEntry,
       "countryCustomizationToneTone": countryCustomizationToneTone,
       "countryCustomizationToneOverride": countryCustomizationToneOverride,
       "countryCustomizationTonePattern": countryCustomizationTonePattern,
       "machineDetectionGroup": machineDetectionGroup,
       "defaultMachineDetectionCngToneDetection": defaultMachineDetectionCngToneDetection,
       "defaultMachineDetectionCedToneDetection": defaultMachineDetectionCedToneDetection,
       "defaultMachineDetectionV21ModulationDetection": defaultMachineDetectionV21ModulationDetection,
       "defaultMachineDetectionBehaviorOnCedToneDetection": defaultMachineDetectionBehaviorOnCedToneDetection,
       "specificMachineDetectionTable": specificMachineDetectionTable,
       "specificMachineDetectionEntry": specificMachineDetectionEntry,
       "specificMachineDetectionInterfaceId": specificMachineDetectionInterfaceId,
       "specificMachineDetectionEnableConfig": specificMachineDetectionEnableConfig,
       "specificMachineDetectionCngToneDetection": specificMachineDetectionCngToneDetection,
       "specificMachineDetectionCedToneDetection": specificMachineDetectionCedToneDetection,
       "specificMachineDetectionV21ModulationDetection": specificMachineDetectionV21ModulationDetection,
       "specificMachineDetectionBehaviorOnCedToneDetection": specificMachineDetectionBehaviorOnCedToneDetection,
       "musicOnHoldStreamingGroup": musicOnHoldStreamingGroup,
       "musicOnHoldStreamingEnable": musicOnHoldStreamingEnable,
       "callWaitingToneGroup": callWaitingToneGroup,
       "distinctiveCallWaitingToneTable": distinctiveCallWaitingToneTable,
       "distinctiveCallWaitingToneEntry": distinctiveCallWaitingToneEntry,
       "distinctiveCallWaitingToneIndex": distinctiveCallWaitingToneIndex,
       "distinctiveCallWaitingToneToneId": distinctiveCallWaitingToneToneId,
       "distinctiveCallWaitingTonePattern": distinctiveCallWaitingTonePattern,
       "interopGroup": interopGroup,
       "interopDtmfDetectionTable": interopDtmfDetectionTable,
       "interopDtmfDetectionEntry": interopDtmfDetectionEntry,
       "interopDtmfDetectionInterfaceId": interopDtmfDetectionInterfaceId,
       "interopDtmfDetectionRiseTimeCriteria": interopDtmfDetectionRiseTimeCriteria,
       "interopDtmfDetectionPositiveTwist": interopDtmfDetectionPositiveTwist,
       "interopDtmfDetectionNegativeTwist": interopDtmfDetectionNegativeTwist,
       "interopDtmfDetectionMaxPowerThreshold": interopDtmfDetectionMaxPowerThreshold,
       "interopDtmfDetectionMinPowerThreshold": interopDtmfDetectionMinPowerThreshold,
       "interopDtmfDetectionBreakPowerThreshold": interopDtmfDetectionBreakPowerThreshold,
       "interopStartCallInVbdTable": interopStartCallInVbdTable,
       "interopStartCallInVbdEntry": interopStartCallInVbdEntry,
       "interopStartCallInVbdInterfaceId": interopStartCallInVbdInterfaceId,
       "interopStartCallInVbdEnable": interopStartCallInVbdEnable,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
