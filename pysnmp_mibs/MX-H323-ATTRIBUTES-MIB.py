# SNMP MIB module (MX-H323-ATTRIBUTES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-H323-ATTRIBUTES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:44 2025
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

(h323,
 ipAddressConfigH323Dhcp,
 ipAddressConfigH323Static,
 ipAddressStatusH323) = mibBuilder.importSymbols(
    "MX-H323-MIB",
    "h323",
    "ipAddressConfigH323Dhcp",
    "ipAddressConfigH323Static",
    "ipAddressStatusH323")

(MxEnableState,
 MxIpAddress,
 MxIpDhcpSiteSpecificCode,
 MxIpPort) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpAddress",
    "MxIpDhcpSiteSpecificCode",
    "MxIpPort")

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

h323AttributesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5)
)
if mibBuilder.loadTexts:
    h323AttributesMIB.setRevisions(
        ("2008-08-25 00:00",
         "2008-03-05 00:00",
         "2005-01-18 00:00",
         "2004-10-15 00:00",
         "2004-07-14 00:00",
         "2004-01-21 00:00",
         "2003-11-05 00:00",
         "2003-05-05 00:00",
         "2003-03-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323AttributesMIBObjects_ObjectIdentity = ObjectIdentity
h323AttributesMIBObjects = _H323AttributesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1)
)
_H323AttributesQ931_ObjectIdentity = ObjectIdentity
h323AttributesQ931 = _H323AttributesQ931_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1)
)
_H323AttributesQ931BearerCapability_ObjectIdentity = ObjectIdentity
h323AttributesQ931BearerCapability = _H323AttributesQ931BearerCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 5)
)


class _H323AttributesInformationTransferCapability_Type(Integer32):
    """Custom type h323AttributesInformationTransferCapability based on Integer32"""
    defaultValue = 1

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
        *(("speech", 0),
          ("unrestrictedDigitalInformation", 1),
          ("restrictedDigitalInformation", 2),
          ("audio31kHz", 3),
          ("udita", 4),
          ("video", 5))
    )


_H323AttributesInformationTransferCapability_Type.__name__ = "Integer32"
_H323AttributesInformationTransferCapability_Object = MibScalar
h323AttributesInformationTransferCapability = _H323AttributesInformationTransferCapability_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 5, 5),
    _H323AttributesInformationTransferCapability_Type()
)
h323AttributesInformationTransferCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesInformationTransferCapability.setStatus("current")
_H323AttributesQ931CalledPartyNumberTable_Object = MibTable
h323AttributesQ931CalledPartyNumberTable = _H323AttributesQ931CalledPartyNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    h323AttributesQ931CalledPartyNumberTable.setStatus("current")
_H323AttributesQ931CalledPartyNumberEntry_Object = MibTableRow
h323AttributesQ931CalledPartyNumberEntry = _H323AttributesQ931CalledPartyNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 15, 1)
)
h323AttributesQ931CalledPartyNumberEntry.setIndexNames(
    (0, "MX-H323-ATTRIBUTES-MIB", "h323AttributesCalledPartyNumberIndex"),
)
if mibBuilder.loadTexts:
    h323AttributesQ931CalledPartyNumberEntry.setStatus("current")
_H323AttributesCalledPartyNumberIndex_Type = Unsigned32
_H323AttributesCalledPartyNumberIndex_Object = MibTableColumn
h323AttributesCalledPartyNumberIndex = _H323AttributesCalledPartyNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 15, 1, 1),
    _H323AttributesCalledPartyNumberIndex_Type()
)
h323AttributesCalledPartyNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323AttributesCalledPartyNumberIndex.setStatus("current")


class _H323AttributesCalledPartyNumberEnable_Type(MxEnableState):
    """Custom type h323AttributesCalledPartyNumberEnable based on MxEnableState"""
    defaultValue = 0


_H323AttributesCalledPartyNumberEnable_Type.__name__ = "MxEnableState"
_H323AttributesCalledPartyNumberEnable_Object = MibTableColumn
h323AttributesCalledPartyNumberEnable = _H323AttributesCalledPartyNumberEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 15, 1, 5),
    _H323AttributesCalledPartyNumberEnable_Type()
)
h323AttributesCalledPartyNumberEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesCalledPartyNumberEnable.setStatus("current")


class _H323AttributesCalledPartyNumberDigitMap_Type(OctetString):
    """Custom type h323AttributesCalledPartyNumberDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H323AttributesCalledPartyNumberDigitMap_Type.__name__ = "OctetString"
_H323AttributesCalledPartyNumberDigitMap_Object = MibTableColumn
h323AttributesCalledPartyNumberDigitMap = _H323AttributesCalledPartyNumberDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 15, 1, 10),
    _H323AttributesCalledPartyNumberDigitMap_Type()
)
h323AttributesCalledPartyNumberDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesCalledPartyNumberDigitMap.setStatus("current")


class _H323AttributesCalledPartyNumberTypeOfNumber_Type(Integer32):
    """Custom type h323AttributesCalledPartyNumberTypeOfNumber based on Integer32"""
    defaultValue = 1

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
        *(("internationalNumber", 0),
          ("nationalNumber", 1),
          ("subscriberNumber", 2),
          ("privateNumber", 3),
          ("unknown", 4))
    )


_H323AttributesCalledPartyNumberTypeOfNumber_Type.__name__ = "Integer32"
_H323AttributesCalledPartyNumberTypeOfNumber_Object = MibTableColumn
h323AttributesCalledPartyNumberTypeOfNumber = _H323AttributesCalledPartyNumberTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 1, 15, 1, 15),
    _H323AttributesCalledPartyNumberTypeOfNumber_Type()
)
h323AttributesCalledPartyNumberTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesCalledPartyNumberTypeOfNumber.setStatus("current")
_H323IfSignalingAttributesTable_Object = MibTable
h323IfSignalingAttributesTable = _H323IfSignalingAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5)
)
if mibBuilder.loadTexts:
    h323IfSignalingAttributesTable.setStatus("current")
_H323IfSignalingAttributesEntry_Object = MibTableRow
h323IfSignalingAttributesEntry = _H323IfSignalingAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5, 1)
)
h323IfSignalingAttributesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323IfSignalingAttributesEntry.setStatus("current")


class _H323AttributesEarlyH245Enable_Type(MxEnableState):
    """Custom type h323AttributesEarlyH245Enable based on MxEnableState"""
    defaultValue = 1


_H323AttributesEarlyH245Enable_Type.__name__ = "MxEnableState"
_H323AttributesEarlyH245Enable_Object = MibTableColumn
h323AttributesEarlyH245Enable = _H323AttributesEarlyH245Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5, 1, 5),
    _H323AttributesEarlyH245Enable_Type()
)
h323AttributesEarlyH245Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesEarlyH245Enable.setStatus("current")


class _H323AttributesH245TunnelingEnable_Type(MxEnableState):
    """Custom type h323AttributesH245TunnelingEnable based on MxEnableState"""
    defaultValue = 0


_H323AttributesH245TunnelingEnable_Type.__name__ = "MxEnableState"
_H323AttributesH245TunnelingEnable_Object = MibTableColumn
h323AttributesH245TunnelingEnable = _H323AttributesH245TunnelingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5, 1, 10),
    _H323AttributesH245TunnelingEnable_Type()
)
h323AttributesH245TunnelingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesH245TunnelingEnable.setStatus("current")


class _H323AttributesFastConnectEnable_Type(MxEnableState):
    """Custom type h323AttributesFastConnectEnable based on MxEnableState"""
    defaultValue = 1


_H323AttributesFastConnectEnable_Type.__name__ = "MxEnableState"
_H323AttributesFastConnectEnable_Object = MibTableColumn
h323AttributesFastConnectEnable = _H323AttributesFastConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5, 1, 15),
    _H323AttributesFastConnectEnable_Type()
)
h323AttributesFastConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesFastConnectEnable.setStatus("current")


class _H323AttributesParallelH245Enable_Type(MxEnableState):
    """Custom type h323AttributesParallelH245Enable based on MxEnableState"""
    defaultValue = 0


_H323AttributesParallelH245Enable_Type.__name__ = "MxEnableState"
_H323AttributesParallelH245Enable_Object = MibTableColumn
h323AttributesParallelH245Enable = _H323AttributesParallelH245Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5, 1, 20),
    _H323AttributesParallelH245Enable_Type()
)
h323AttributesParallelH245Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesParallelH245Enable.setStatus("current")


class _H323AttributesVoiceCapabilitySendingMethod_Type(Integer32):
    """Custom type h323AttributesVoiceCapabilitySendingMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 0),
          ("detailed", 1))
    )


_H323AttributesVoiceCapabilitySendingMethod_Type.__name__ = "Integer32"
_H323AttributesVoiceCapabilitySendingMethod_Object = MibTableColumn
h323AttributesVoiceCapabilitySendingMethod = _H323AttributesVoiceCapabilitySendingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 5, 1, 25),
    _H323AttributesVoiceCapabilitySendingMethod_Type()
)
h323AttributesVoiceCapabilitySendingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesVoiceCapabilitySendingMethod.setStatus("current")
_H323IfTelephonyAttributesTable_Object = MibTable
h323IfTelephonyAttributesTable = _H323IfTelephonyAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 10)
)
if mibBuilder.loadTexts:
    h323IfTelephonyAttributesTable.setStatus("current")
_H323IfTelephonyAttributesEntry_Object = MibTableRow
h323IfTelephonyAttributesEntry = _H323IfTelephonyAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 10, 1)
)
h323IfTelephonyAttributesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323IfTelephonyAttributesEntry.setStatus("current")


class _H323AttributesDirectGatewayCallEnable_Type(MxEnableState):
    """Custom type h323AttributesDirectGatewayCallEnable based on MxEnableState"""
    defaultValue = 0


_H323AttributesDirectGatewayCallEnable_Type.__name__ = "MxEnableState"
_H323AttributesDirectGatewayCallEnable_Object = MibTableColumn
h323AttributesDirectGatewayCallEnable = _H323AttributesDirectGatewayCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 10, 1, 5),
    _H323AttributesDirectGatewayCallEnable_Type()
)
h323AttributesDirectGatewayCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesDirectGatewayCallEnable.setStatus("current")


class _H323AttributesDirectGatewayCallHost_Type(MxIpAddress):
    """Custom type h323AttributesDirectGatewayCallHost based on MxIpAddress"""
    defaultValue = OctetString("")


_H323AttributesDirectGatewayCallHost_Type.__name__ = "MxIpAddress"
_H323AttributesDirectGatewayCallHost_Object = MibTableColumn
h323AttributesDirectGatewayCallHost = _H323AttributesDirectGatewayCallHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 1, 10, 1, 10),
    _H323AttributesDirectGatewayCallHost_Type()
)
h323AttributesDirectGatewayCallHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AttributesDirectGatewayCallHost.setStatus("current")
_H323AttributesConformance_ObjectIdentity = ObjectIdentity
h323AttributesConformance = _H323AttributesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2)
)
_H323AttributesCompliances_ObjectIdentity = ObjectIdentity
h323AttributesCompliances = _H323AttributesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2, 1)
)
_H323AttributesGroups_ObjectIdentity = ObjectIdentity
h323AttributesGroups = _H323AttributesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2, 2)
)

# Managed Objects groups

h323AttributesSignalingGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2, 2, 5)
)
h323AttributesSignalingGroupVer1.setObjects(
      *(("MX-H323-ATTRIBUTES-MIB", "h323AttributesEarlyH245Enable"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesH245TunnelingEnable"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesFastConnectEnable"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesParallelH245Enable"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesVoiceCapabilitySendingMethod"))
)
if mibBuilder.loadTexts:
    h323AttributesSignalingGroupVer1.setStatus("current")

h323AttributesTelephonyGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2, 2, 10)
)
h323AttributesTelephonyGroupVer1.setObjects(
      *(("MX-H323-ATTRIBUTES-MIB", "h323AttributesDirectGatewayCallEnable"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesDirectGatewayCallHost"))
)
if mibBuilder.loadTexts:
    h323AttributesTelephonyGroupVer1.setStatus("current")

h323AttributesQ931GroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2, 2, 15)
)
h323AttributesQ931GroupVer1.setObjects(
      *(("MX-H323-ATTRIBUTES-MIB", "h323AttributesInformationTransferCapability"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesCalledPartyNumberIndex"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesCalledPartyNumberEnable"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesCalledPartyNumberDigitMap"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesCalledPartyNumberTypeOfNumber"))
)
if mibBuilder.loadTexts:
    h323AttributesQ931GroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h323AttributesBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 20, 30, 5, 2, 1, 5)
)
h323AttributesBasicComplVer1.setObjects(
      *(("MX-H323-ATTRIBUTES-MIB", "h323AttributesSignalingGroupVer1"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesTelephonyGroupVer1"),
        ("MX-H323-ATTRIBUTES-MIB", "h323AttributesQ931GroupVer1"))
)
if mibBuilder.loadTexts:
    h323AttributesBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-H323-ATTRIBUTES-MIB",
    **{"h323AttributesMIB": h323AttributesMIB,
       "h323AttributesMIBObjects": h323AttributesMIBObjects,
       "h323AttributesQ931": h323AttributesQ931,
       "h323AttributesQ931BearerCapability": h323AttributesQ931BearerCapability,
       "h323AttributesInformationTransferCapability": h323AttributesInformationTransferCapability,
       "h323AttributesQ931CalledPartyNumberTable": h323AttributesQ931CalledPartyNumberTable,
       "h323AttributesQ931CalledPartyNumberEntry": h323AttributesQ931CalledPartyNumberEntry,
       "h323AttributesCalledPartyNumberIndex": h323AttributesCalledPartyNumberIndex,
       "h323AttributesCalledPartyNumberEnable": h323AttributesCalledPartyNumberEnable,
       "h323AttributesCalledPartyNumberDigitMap": h323AttributesCalledPartyNumberDigitMap,
       "h323AttributesCalledPartyNumberTypeOfNumber": h323AttributesCalledPartyNumberTypeOfNumber,
       "h323IfSignalingAttributesTable": h323IfSignalingAttributesTable,
       "h323IfSignalingAttributesEntry": h323IfSignalingAttributesEntry,
       "h323AttributesEarlyH245Enable": h323AttributesEarlyH245Enable,
       "h323AttributesH245TunnelingEnable": h323AttributesH245TunnelingEnable,
       "h323AttributesFastConnectEnable": h323AttributesFastConnectEnable,
       "h323AttributesParallelH245Enable": h323AttributesParallelH245Enable,
       "h323AttributesVoiceCapabilitySendingMethod": h323AttributesVoiceCapabilitySendingMethod,
       "h323IfTelephonyAttributesTable": h323IfTelephonyAttributesTable,
       "h323IfTelephonyAttributesEntry": h323IfTelephonyAttributesEntry,
       "h323AttributesDirectGatewayCallEnable": h323AttributesDirectGatewayCallEnable,
       "h323AttributesDirectGatewayCallHost": h323AttributesDirectGatewayCallHost,
       "h323AttributesConformance": h323AttributesConformance,
       "h323AttributesCompliances": h323AttributesCompliances,
       "h323AttributesBasicComplVer1": h323AttributesBasicComplVer1,
       "h323AttributesGroups": h323AttributesGroups,
       "h323AttributesSignalingGroupVer1": h323AttributesSignalingGroupVer1,
       "h323AttributesTelephonyGroupVer1": h323AttributesTelephonyGroupVer1,
       "h323AttributesQ931GroupVer1": h323AttributesQ931GroupVer1}
)
