# SNMP MIB module (MX-SIP-EXPERIMENTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SIP-EXPERIMENTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:51 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

(MxEnableState,
 MxIpHostName) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpHostName")

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

sipExperimentalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10)
)
if mibBuilder.loadTexts:
    sipExperimentalMIB.setRevisions(
        ("2009-08-17 00:00",
         "2008-04-03 00:00",
         "2007-10-31 00:00",
         "2006-02-28 00:00",
         "2003-04-30 00:00",
         "2003-03-11 00:00",
         "2003-01-23 00:00",
         "2002-12-17 00:00",
         "2002-12-02 00:00",
         "2002-07-05 00:00",
         "2002-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipExperimentalMIBObjects_ObjectIdentity = ObjectIdentity
sipExperimentalMIBObjects = _SipExperimentalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1)
)
_SipNatCustom_ObjectIdentity = ObjectIdentity
sipNatCustom = _SipNatCustom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 5)
)


class _SipNatCustomEnable_Type(Integer32):
    """Custom type sipNatCustomEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipNatCustomEnable_Type.__name__ = "Integer32"
_SipNatCustomEnable_Object = MibScalar
sipNatCustomEnable = _SipNatCustomEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 5, 5),
    _SipNatCustomEnable_Type()
)
sipNatCustomEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipNatCustomEnable.setStatus("current")


class _SipNatCustomPublicAddress_Type(MxIpHostName):
    """Custom type sipNatCustomPublicAddress based on MxIpHostName"""
    defaultValue = OctetString("0.0.0.0")


_SipNatCustomPublicAddress_Type.__name__ = "MxIpHostName"
_SipNatCustomPublicAddress_Object = MibScalar
sipNatCustomPublicAddress = _SipNatCustomPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 5, 10),
    _SipNatCustomPublicAddress_Type()
)
sipNatCustomPublicAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipNatCustomPublicAddress.setStatus("current")


class _SipUnregisteredPortBehavior_Type(Integer32):
    """Custom type sipUnregisteredPortBehavior based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disablePort", 0),
          ("enablePort", 1))
    )


_SipUnregisteredPortBehavior_Type.__name__ = "Integer32"
_SipUnregisteredPortBehavior_Object = MibScalar
sipUnregisteredPortBehavior = _SipUnregisteredPortBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 25),
    _SipUnregisteredPortBehavior_Type()
)
sipUnregisteredPortBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUnregisteredPortBehavior.setStatus("current")


class _SipOutboundProxyConfig_Type(Integer32):
    """Custom type sipOutboundProxyConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("looseRouter", 0),
          ("strictRouter", 1))
    )


_SipOutboundProxyConfig_Type.__name__ = "Integer32"
_SipOutboundProxyConfig_Object = MibScalar
sipOutboundProxyConfig = _SipOutboundProxyConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 30),
    _SipOutboundProxyConfig_Type()
)
sipOutboundProxyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOutboundProxyConfig.setStatus("current")


class _SipEnforceOfferAnswerModel_Type(MxEnableState):
    """Custom type sipEnforceOfferAnswerModel based on MxEnableState"""
    defaultValue = 1


_SipEnforceOfferAnswerModel_Type.__name__ = "MxEnableState"
_SipEnforceOfferAnswerModel_Object = MibScalar
sipEnforceOfferAnswerModel = _SipEnforceOfferAnswerModel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 80),
    _SipEnforceOfferAnswerModel_Type()
)
sipEnforceOfferAnswerModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipEnforceOfferAnswerModel.setStatus("current")


class _SipAllowMediaReactivationInAnswerEnable_Type(MxEnableState):
    """Custom type sipAllowMediaReactivationInAnswerEnable based on MxEnableState"""
    defaultValue = 0


_SipAllowMediaReactivationInAnswerEnable_Type.__name__ = "MxEnableState"
_SipAllowMediaReactivationInAnswerEnable_Object = MibScalar
sipAllowMediaReactivationInAnswerEnable = _SipAllowMediaReactivationInAnswerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 85),
    _SipAllowMediaReactivationInAnswerEnable_Type()
)
sipAllowMediaReactivationInAnswerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAllowMediaReactivationInAnswerEnable.setStatus("current")


class _SipAllowAudioAndImageNegotiationEnable_Type(MxEnableState):
    """Custom type sipAllowAudioAndImageNegotiationEnable based on MxEnableState"""
    defaultValue = 0


_SipAllowAudioAndImageNegotiationEnable_Type.__name__ = "MxEnableState"
_SipAllowAudioAndImageNegotiationEnable_Object = MibScalar
sipAllowAudioAndImageNegotiationEnable = _SipAllowAudioAndImageNegotiationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 90),
    _SipAllowAudioAndImageNegotiationEnable_Type()
)
sipAllowAudioAndImageNegotiationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAllowAudioAndImageNegotiationEnable.setStatus("current")


class _SipCodecOrderInAnswer_Type(Integer32):
    """Custom type sipCodecOrderInAnswer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("localOrder", 0),
          ("offerOrder", 1))
    )


_SipCodecOrderInAnswer_Type.__name__ = "Integer32"
_SipCodecOrderInAnswer_Object = MibScalar
sipCodecOrderInAnswer = _SipCodecOrderInAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 95),
    _SipCodecOrderInAnswer_Type()
)
sipCodecOrderInAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCodecOrderInAnswer.setStatus("current")


class _SipRtpUdpChecksumEnable_Type(MxEnableState):
    """Custom type sipRtpUdpChecksumEnable based on MxEnableState"""
    defaultValue = 0


_SipRtpUdpChecksumEnable_Type.__name__ = "MxEnableState"
_SipRtpUdpChecksumEnable_Object = MibScalar
sipRtpUdpChecksumEnable = _SipRtpUdpChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 1, 130),
    _SipRtpUdpChecksumEnable_Type()
)
sipRtpUdpChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRtpUdpChecksumEnable.setStatus("current")
_SipExperimentalConformance_ObjectIdentity = ObjectIdentity
sipExperimentalConformance = _SipExperimentalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 2)
)
_SipExperimentalCompliances_ObjectIdentity = ObjectIdentity
sipExperimentalCompliances = _SipExperimentalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 2, 1)
)
_SipExperimentalGroups_ObjectIdentity = ObjectIdentity
sipExperimentalGroups = _SipExperimentalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 2, 2)
)

# Managed Objects groups

sipExperimentalGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 2, 2, 5)
)
sipExperimentalGroupVer1.setObjects(
      *(("MX-SIP-EXPERIMENTAL-MIB", "sipNatCustomEnable"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipNatCustomPublicAddress"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipUnregisteredPortBehavior"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipOutboundProxyConfig"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipEnforceOfferAnswerModel"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipRtpUdpChecksumEnable"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipAllowMediaReactivationInAnswerEnable"),
        ("MX-SIP-EXPERIMENTAL-MIB", "sipAllowAudioAndImageNegotiationEnable"))
)
if mibBuilder.loadTexts:
    sipExperimentalGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipExperimentalBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 10, 2, 1, 1)
)
sipExperimentalBasicComplVer1.setObjects(
    ("MX-SIP-EXPERIMENTAL-MIB", "sipExperimentalGroupVer1")
)
if mibBuilder.loadTexts:
    sipExperimentalBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SIP-EXPERIMENTAL-MIB",
    **{"sipExperimentalMIB": sipExperimentalMIB,
       "sipExperimentalMIBObjects": sipExperimentalMIBObjects,
       "sipNatCustom": sipNatCustom,
       "sipNatCustomEnable": sipNatCustomEnable,
       "sipNatCustomPublicAddress": sipNatCustomPublicAddress,
       "sipUnregisteredPortBehavior": sipUnregisteredPortBehavior,
       "sipOutboundProxyConfig": sipOutboundProxyConfig,
       "sipEnforceOfferAnswerModel": sipEnforceOfferAnswerModel,
       "sipAllowMediaReactivationInAnswerEnable": sipAllowMediaReactivationInAnswerEnable,
       "sipAllowAudioAndImageNegotiationEnable": sipAllowAudioAndImageNegotiationEnable,
       "sipCodecOrderInAnswer": sipCodecOrderInAnswer,
       "sipRtpUdpChecksumEnable": sipRtpUdpChecksumEnable,
       "sipExperimentalConformance": sipExperimentalConformance,
       "sipExperimentalCompliances": sipExperimentalCompliances,
       "sipExperimentalBasicComplVer1": sipExperimentalBasicComplVer1,
       "sipExperimentalGroups": sipExperimentalGroups,
       "sipExperimentalGroupVer1": sipExperimentalGroupVer1}
)
