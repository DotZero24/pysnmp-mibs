# SNMP MIB module (MX-MGCPNCS-EXPERIMENTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-MGCPNCS-EXPERIMENTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:16 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

mgcpncsExperimentalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100)
)
if mibBuilder.loadTexts:
    mgcpncsExperimentalMIB.setRevisions(
        ("2010-08-18 00:00",
         "2009-03-17 00:00",
         "2008-06-13 00:00",
         "2006-06-09 00:00",
         "2006-05-04 00:00",
         "2005-10-17 00:00",
         "2005-04-18 00:00",
         "2005-03-07 00:00",
         "2004-11-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MgcpncsExperimentalMIBObjects_ObjectIdentity = ObjectIdentity
mgcpncsExperimentalMIBObjects = _MgcpncsExperimentalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1)
)
_MgcpncsInterop_ObjectIdentity = ObjectIdentity
mgcpncsInterop = _MgcpncsInterop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5)
)


class _MgcpncsAnswerStreamFormat_Type(Integer32):
    """Custom type mgcpncsAnswerStreamFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("zeroAnswerStream", 1),
          ("removeAnswerStream", 10))
    )


_MgcpncsAnswerStreamFormat_Type.__name__ = "Integer32"
_MgcpncsAnswerStreamFormat_Object = MibScalar
mgcpncsAnswerStreamFormat = _MgcpncsAnswerStreamFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 5),
    _MgcpncsAnswerStreamFormat_Type()
)
mgcpncsAnswerStreamFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsAnswerStreamFormat.setStatus("current")


class _MgcpncsOriginLineSessionIDAndVersionMaxLength_Type(Integer32):
    """Custom type mgcpncsOriginLineSessionIDAndVersionMaxLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("max-32bits", 10),
          ("max-64bits", 20))
    )


_MgcpncsOriginLineSessionIDAndVersionMaxLength_Type.__name__ = "Integer32"
_MgcpncsOriginLineSessionIDAndVersionMaxLength_Object = MibScalar
mgcpncsOriginLineSessionIDAndVersionMaxLength = _MgcpncsOriginLineSessionIDAndVersionMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 10),
    _MgcpncsOriginLineSessionIDAndVersionMaxLength_Type()
)
mgcpncsOriginLineSessionIDAndVersionMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsOriginLineSessionIDAndVersionMaxLength.setStatus("current")


class _MgcpncsG729AnnexBNegotiation_Type(MxEnableState):
    """Custom type mgcpncsG729AnnexBNegotiation based on MxEnableState"""
    defaultValue = 0


_MgcpncsG729AnnexBNegotiation_Type.__name__ = "MxEnableState"
_MgcpncsG729AnnexBNegotiation_Object = MibScalar
mgcpncsG729AnnexBNegotiation = _MgcpncsG729AnnexBNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 15),
    _MgcpncsG729AnnexBNegotiation_Type()
)
mgcpncsG729AnnexBNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsG729AnnexBNegotiation.setStatus("current")


class _MgcpncsValidateOfferAnswerModel_Type(MxEnableState):
    """Custom type mgcpncsValidateOfferAnswerModel based on MxEnableState"""
    defaultValue = 1


_MgcpncsValidateOfferAnswerModel_Type.__name__ = "MxEnableState"
_MgcpncsValidateOfferAnswerModel_Object = MibScalar
mgcpncsValidateOfferAnswerModel = _MgcpncsValidateOfferAnswerModel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 20),
    _MgcpncsValidateOfferAnswerModel_Type()
)
mgcpncsValidateOfferAnswerModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsValidateOfferAnswerModel.setStatus("current")


class _MgcpncsMultipleFaxToneDetection_Type(MxEnableState):
    """Custom type mgcpncsMultipleFaxToneDetection based on MxEnableState"""
    defaultValue = 0


_MgcpncsMultipleFaxToneDetection_Type.__name__ = "MxEnableState"
_MgcpncsMultipleFaxToneDetection_Object = MibScalar
mgcpncsMultipleFaxToneDetection = _MgcpncsMultipleFaxToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 100),
    _MgcpncsMultipleFaxToneDetection_Type()
)
mgcpncsMultipleFaxToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsMultipleFaxToneDetection.setStatus("current")


class _MgcpncsConnectRtpSockets_Type(MxEnableState):
    """Custom type mgcpncsConnectRtpSockets based on MxEnableState"""
    defaultValue = 0


_MgcpncsConnectRtpSockets_Type.__name__ = "MxEnableState"
_MgcpncsConnectRtpSockets_Object = MibScalar
mgcpncsConnectRtpSockets = _MgcpncsConnectRtpSockets_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 150),
    _MgcpncsConnectRtpSockets_Type()
)
mgcpncsConnectRtpSockets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsConnectRtpSockets.setStatus("current")


class _MgcpncsRtpUdpChecksumEnable_Type(MxEnableState):
    """Custom type mgcpncsRtpUdpChecksumEnable based on MxEnableState"""
    defaultValue = 0


_MgcpncsRtpUdpChecksumEnable_Type.__name__ = "MxEnableState"
_MgcpncsRtpUdpChecksumEnable_Object = MibScalar
mgcpncsRtpUdpChecksumEnable = _MgcpncsRtpUdpChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 200),
    _MgcpncsRtpUdpChecksumEnable_Type()
)
mgcpncsRtpUdpChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsRtpUdpChecksumEnable.setStatus("current")


class _MgcpncsT38CapabilitiesUsingAudioCodec98_Type(MxEnableState):
    """Custom type mgcpncsT38CapabilitiesUsingAudioCodec98 based on MxEnableState"""
    defaultValue = 0


_MgcpncsT38CapabilitiesUsingAudioCodec98_Type.__name__ = "MxEnableState"
_MgcpncsT38CapabilitiesUsingAudioCodec98_Object = MibScalar
mgcpncsT38CapabilitiesUsingAudioCodec98 = _MgcpncsT38CapabilitiesUsingAudioCodec98_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 250),
    _MgcpncsT38CapabilitiesUsingAudioCodec98_Type()
)
mgcpncsT38CapabilitiesUsingAudioCodec98.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsT38CapabilitiesUsingAudioCodec98.setStatus("current")


class _MgcpncsImmediateModemToneReporting_Type(MxEnableState):
    """Custom type mgcpncsImmediateModemToneReporting based on MxEnableState"""
    defaultValue = 0


_MgcpncsImmediateModemToneReporting_Type.__name__ = "MxEnableState"
_MgcpncsImmediateModemToneReporting_Object = MibScalar
mgcpncsImmediateModemToneReporting = _MgcpncsImmediateModemToneReporting_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 300),
    _MgcpncsImmediateModemToneReporting_Type()
)
mgcpncsImmediateModemToneReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsImmediateModemToneReporting.setStatus("current")


class _MgcpncsMakeOsiSignalBrief_Type(MxEnableState):
    """Custom type mgcpncsMakeOsiSignalBrief based on MxEnableState"""
    defaultValue = 0


_MgcpncsMakeOsiSignalBrief_Type.__name__ = "MxEnableState"
_MgcpncsMakeOsiSignalBrief_Object = MibScalar
mgcpncsMakeOsiSignalBrief = _MgcpncsMakeOsiSignalBrief_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 350),
    _MgcpncsMakeOsiSignalBrief_Type()
)
mgcpncsMakeOsiSignalBrief.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsMakeOsiSignalBrief.setStatus("current")


class _MgcpncsFakeRfc3407Recognition_Type(MxEnableState):
    """Custom type mgcpncsFakeRfc3407Recognition based on MxEnableState"""
    defaultValue = 0


_MgcpncsFakeRfc3407Recognition_Type.__name__ = "MxEnableState"
_MgcpncsFakeRfc3407Recognition_Object = MibScalar
mgcpncsFakeRfc3407Recognition = _MgcpncsFakeRfc3407Recognition_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 400),
    _MgcpncsFakeRfc3407Recognition_Type()
)
mgcpncsFakeRfc3407Recognition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsFakeRfc3407Recognition.setStatus("current")


class _MgcpncsUseItuT38Format_Type(MxEnableState):
    """Custom type mgcpncsUseItuT38Format based on MxEnableState"""
    defaultValue = 0


_MgcpncsUseItuT38Format_Type.__name__ = "MxEnableState"
_MgcpncsUseItuT38Format_Object = MibScalar
mgcpncsUseItuT38Format = _MgcpncsUseItuT38Format_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 450),
    _MgcpncsUseItuT38Format_Type()
)
mgcpncsUseItuT38Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsUseItuT38Format.setStatus("current")


class _MgcpncsBracketsAroundIpAddressInDomainNameEnable_Type(MxEnableState):
    """Custom type mgcpncsBracketsAroundIpAddressInDomainNameEnable based on MxEnableState"""
    defaultValue = 1


_MgcpncsBracketsAroundIpAddressInDomainNameEnable_Type.__name__ = "MxEnableState"
_MgcpncsBracketsAroundIpAddressInDomainNameEnable_Object = MibScalar
mgcpncsBracketsAroundIpAddressInDomainNameEnable = _MgcpncsBracketsAroundIpAddressInDomainNameEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 500),
    _MgcpncsBracketsAroundIpAddressInDomainNameEnable_Type()
)
mgcpncsBracketsAroundIpAddressInDomainNameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsBracketsAroundIpAddressInDomainNameEnable.setStatus("current")


class _MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Type(MxEnableState):
    """Custom type mgcpncsPolarityReversalOnCallingCardServiceToneEnable based on MxEnableState"""
    defaultValue = 0


_MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Type.__name__ = "MxEnableState"
_MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Object = MibScalar
mgcpncsPolarityReversalOnCallingCardServiceToneEnable = _MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 1, 5, 550),
    _MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Type()
)
mgcpncsPolarityReversalOnCallingCardServiceToneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcpncsPolarityReversalOnCallingCardServiceToneEnable.setStatus("current")
_MgcpncsExperimentalConformance_ObjectIdentity = ObjectIdentity
mgcpncsExperimentalConformance = _MgcpncsExperimentalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 2)
)
_MgcpncsExperimentalCompliances_ObjectIdentity = ObjectIdentity
mgcpncsExperimentalCompliances = _MgcpncsExperimentalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 2, 1)
)
_MgcpncsExperimentalGroups_ObjectIdentity = ObjectIdentity
mgcpncsExperimentalGroups = _MgcpncsExperimentalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 2, 2)
)

# Managed Objects groups

mgcpncsExperimentalGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 2, 2, 5)
)
mgcpncsExperimentalGroupVer1.setObjects(
      *(("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsAnswerStreamFormat"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsOriginLineSessionIDAndVersionMaxLength"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsG729AnnexBNegotiation"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsValidateOfferAnswerModel"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsMultipleFaxToneDetection"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsConnectRtpSockets"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsRtpUdpChecksumEnable"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsT38CapabilitiesUsingAudioCodec98"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsImmediateModemToneReporting"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsMakeOsiSignalBrief"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsFakeRfc3407Recognition"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsUseItuT38Format"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsBracketsAroundIpAddressInDomainNameEnable"),
        ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsPolarityReversalOnCallingCardServiceToneEnable"))
)
if mibBuilder.loadTexts:
    mgcpncsExperimentalGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mgcpncsExperimentalBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 100, 2, 1, 5)
)
mgcpncsExperimentalBasicComplVer1.setObjects(
    ("MX-MGCPNCS-EXPERIMENTAL-MIB", "mgcpncsExperimentalGroupVer1")
)
if mibBuilder.loadTexts:
    mgcpncsExperimentalBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-MGCPNCS-EXPERIMENTAL-MIB",
    **{"mgcpncsExperimentalMIB": mgcpncsExperimentalMIB,
       "mgcpncsExperimentalMIBObjects": mgcpncsExperimentalMIBObjects,
       "mgcpncsInterop": mgcpncsInterop,
       "mgcpncsAnswerStreamFormat": mgcpncsAnswerStreamFormat,
       "mgcpncsOriginLineSessionIDAndVersionMaxLength": mgcpncsOriginLineSessionIDAndVersionMaxLength,
       "mgcpncsG729AnnexBNegotiation": mgcpncsG729AnnexBNegotiation,
       "mgcpncsValidateOfferAnswerModel": mgcpncsValidateOfferAnswerModel,
       "mgcpncsMultipleFaxToneDetection": mgcpncsMultipleFaxToneDetection,
       "mgcpncsConnectRtpSockets": mgcpncsConnectRtpSockets,
       "mgcpncsRtpUdpChecksumEnable": mgcpncsRtpUdpChecksumEnable,
       "mgcpncsT38CapabilitiesUsingAudioCodec98": mgcpncsT38CapabilitiesUsingAudioCodec98,
       "mgcpncsImmediateModemToneReporting": mgcpncsImmediateModemToneReporting,
       "mgcpncsMakeOsiSignalBrief": mgcpncsMakeOsiSignalBrief,
       "mgcpncsFakeRfc3407Recognition": mgcpncsFakeRfc3407Recognition,
       "mgcpncsUseItuT38Format": mgcpncsUseItuT38Format,
       "mgcpncsBracketsAroundIpAddressInDomainNameEnable": mgcpncsBracketsAroundIpAddressInDomainNameEnable,
       "mgcpncsPolarityReversalOnCallingCardServiceToneEnable": mgcpncsPolarityReversalOnCallingCardServiceToneEnable,
       "mgcpncsExperimentalConformance": mgcpncsExperimentalConformance,
       "mgcpncsExperimentalCompliances": mgcpncsExperimentalCompliances,
       "mgcpncsExperimentalBasicComplVer1": mgcpncsExperimentalBasicComplVer1,
       "mgcpncsExperimentalGroups": mgcpncsExperimentalGroups,
       "mgcpncsExperimentalGroupVer1": mgcpncsExperimentalGroupVer1}
)
