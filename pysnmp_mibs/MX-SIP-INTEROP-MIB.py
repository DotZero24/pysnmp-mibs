# SNMP MIB module (MX-SIP-INTEROP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SIP-INTEROP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:34 2025
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

sipInteropMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20)
)
if mibBuilder.loadTexts:
    sipInteropMIB.setRevisions(
        ("2010-12-10 00:00",
         "2010-10-05 00:00",
         "2009-10-28 00:00",
         "2009-09-30 00:00",
         "2009-08-10 00:00",
         "2009-04-23 00:00",
         "2009-03-27 00:00",
         "2008-11-26 00:00",
         "2008-11-18 00:00",
         "2008-10-31 00:00",
         "2008-10-17 00:00",
         "2008-06-12 00:00",
         "2008-03-03 00:00",
         "2008-01-11 00:00",
         "2007-08-08 00:00",
         "2007-08-06 00:00",
         "2007-08-01 00:00",
         "2007-07-18 00:00",
         "2007-07-03 00:00",
         "2007-06-20 00:00",
         "2007-06-14 00:00",
         "2007-05-28 00:00",
         "2007-05-03 00:00",
         "2007-04-18 00:00",
         "2007-02-02 00:00",
         "2007-02-23 00:00",
         "2006-05-24 00:00",
         "2005-10-07 00:00",
         "2005-06-28 00:00",
         "2005-05-20 00:00",
         "2005-01-25 00:00",
         "2005-01-10 00:00",
         "2004-12-22 00:00",
         "2004-11-02 00:00",
         "2004-10-25 00:00",
         "2004-10-04 00:00",
         "2004-09-29 00:00",
         "2004-09-21 00:00",
         "2004-07-28 00:00",
         "2004-06-14 00:00",
         "2004-06-02 00:00",
         "2004-04-27 00:00",
         "2004-04-21 00:00",
         "2004-03-25 00:00",
         "2004-02-13 00:00",
         "2003-11-17 00:00",
         "2003-11-06 00:00",
         "2003-11-05 00:00",
         "2003-11-03 00:00",
         "2003-03-11 00:00",
         "2002-10-28 00:00",
         "2002-10-16 00:00",
         "2002-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipInteropMIBObjects_ObjectIdentity = ObjectIdentity
sipInteropMIBObjects = _SipInteropMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1)
)


class _SipInteropReplacesConfig_Type(Integer32):
    """Custom type sipInteropReplacesConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotUseReplaces", 0),
          ("useReplacesWithRequire", 1),
          ("useReplacesNoRequire", 2))
    )


_SipInteropReplacesConfig_Type.__name__ = "Integer32"
_SipInteropReplacesConfig_Object = MibScalar
sipInteropReplacesConfig = _SipInteropReplacesConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 5),
    _SipInteropReplacesConfig_Type()
)
sipInteropReplacesConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropReplacesConfig.setStatus("current")


class _SipInteropTransferVersion_Type(Integer32):
    """Custom type sipInteropTransferVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transfer02", 0),
          ("transfer05UsingRefer02", 1),
          ("sippingTransfer01UsingReferRfc3515", 2))
    )


_SipInteropTransferVersion_Type.__name__ = "Integer32"
_SipInteropTransferVersion_Object = MibScalar
sipInteropTransferVersion = _SipInteropTransferVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 10),
    _SipInteropTransferVersion_Type()
)
sipInteropTransferVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropTransferVersion.setStatus("current")


class _SipInteropSessionTimerVersion_Type(Integer32):
    """Custom type sipInteropSessionTimerVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sessionTimer04", 0),
          ("sessionTimer08", 1))
    )


_SipInteropSessionTimerVersion_Type.__name__ = "Integer32"
_SipInteropSessionTimerVersion_Object = MibScalar
sipInteropSessionTimerVersion = _SipInteropSessionTimerVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 15),
    _SipInteropSessionTimerVersion_Type()
)
sipInteropSessionTimerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropSessionTimerVersion.setStatus("current")


class _SipInteropTransmissionTimeout_Type(Unsigned32):
    """Custom type sipInteropTransmissionTimeout based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SipInteropTransmissionTimeout_Type.__name__ = "Unsigned32"
_SipInteropTransmissionTimeout_Object = MibScalar
sipInteropTransmissionTimeout = _SipInteropTransmissionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 20),
    _SipInteropTransmissionTimeout_Type()
)
sipInteropTransmissionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropTransmissionTimeout.setStatus("current")


class _SipInteropReplacesVersion_Type(Integer32):
    """Custom type sipInteropReplacesVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("replaces01", 0),
          ("replaces03", 1))
    )


_SipInteropReplacesVersion_Type.__name__ = "Integer32"
_SipInteropReplacesVersion_Object = MibScalar
sipInteropReplacesVersion = _SipInteropReplacesVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 25),
    _SipInteropReplacesVersion_Type()
)
sipInteropReplacesVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropReplacesVersion.setStatus("current")


class _SipInteropSymmetricUdpSourcePortEnable_Type(MxEnableState):
    """Custom type sipInteropSymmetricUdpSourcePortEnable based on MxEnableState"""
    defaultValue = 1


_SipInteropSymmetricUdpSourcePortEnable_Type.__name__ = "MxEnableState"
_SipInteropSymmetricUdpSourcePortEnable_Object = MibScalar
sipInteropSymmetricUdpSourcePortEnable = _SipInteropSymmetricUdpSourcePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 30),
    _SipInteropSymmetricUdpSourcePortEnable_Type()
)
sipInteropSymmetricUdpSourcePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropSymmetricUdpSourcePortEnable.setStatus("current")


class _SipInteropMaxForwardsValue_Type(Integer32):
    """Custom type sipInteropMaxForwardsValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 200),
    )


_SipInteropMaxForwardsValue_Type.__name__ = "Integer32"
_SipInteropMaxForwardsValue_Object = MibScalar
sipInteropMaxForwardsValue = _SipInteropMaxForwardsValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 35),
    _SipInteropMaxForwardsValue_Type()
)
sipInteropMaxForwardsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropMaxForwardsValue.setStatus("current")


class _SipInteropAutomaticRejectionCode_Type(Unsigned32):
    """Custom type sipInteropAutomaticRejectionCode based on Unsigned32"""
    defaultValue = 480

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 699),
    )


_SipInteropAutomaticRejectionCode_Type.__name__ = "Unsigned32"
_SipInteropAutomaticRejectionCode_Object = MibScalar
sipInteropAutomaticRejectionCode = _SipInteropAutomaticRejectionCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 40),
    _SipInteropAutomaticRejectionCode_Type()
)
sipInteropAutomaticRejectionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropAutomaticRejectionCode.setStatus("current")


class _SipInteropSendUAHeaderEnable_Type(MxEnableState):
    """Custom type sipInteropSendUAHeaderEnable based on MxEnableState"""
    defaultValue = 1


_SipInteropSendUAHeaderEnable_Type.__name__ = "MxEnableState"
_SipInteropSendUAHeaderEnable_Object = MibScalar
sipInteropSendUAHeaderEnable = _SipInteropSendUAHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 50),
    _SipInteropSendUAHeaderEnable_Type()
)
sipInteropSendUAHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropSendUAHeaderEnable.setStatus("current")


class _SipInteropUAHeaderConfig_Type(OctetString):
    """Custom type sipInteropUAHeaderConfig based on OctetString"""
    defaultValue = OctetString("MxSipApp/%version%")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipInteropUAHeaderConfig_Type.__name__ = "OctetString"
_SipInteropUAHeaderConfig_Object = MibScalar
sipInteropUAHeaderConfig = _SipInteropUAHeaderConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 55),
    _SipInteropUAHeaderConfig_Type()
)
sipInteropUAHeaderConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropUAHeaderConfig.setStatus("current")


class _SipInteropSdpDirectionAttributeEnable_Type(MxEnableState):
    """Custom type sipInteropSdpDirectionAttributeEnable based on MxEnableState"""
    defaultValue = 1


_SipInteropSdpDirectionAttributeEnable_Type.__name__ = "MxEnableState"
_SipInteropSdpDirectionAttributeEnable_Object = MibScalar
sipInteropSdpDirectionAttributeEnable = _SipInteropSdpDirectionAttributeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 75),
    _SipInteropSdpDirectionAttributeEnable_Type()
)
sipInteropSdpDirectionAttributeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropSdpDirectionAttributeEnable.setStatus("current")


class _SipInteropAllowMultipleActiveMediaInAnswer_Type(MxEnableState):
    """Custom type sipInteropAllowMultipleActiveMediaInAnswer based on MxEnableState"""
    defaultValue = 1


_SipInteropAllowMultipleActiveMediaInAnswer_Type.__name__ = "MxEnableState"
_SipInteropAllowMultipleActiveMediaInAnswer_Object = MibScalar
sipInteropAllowMultipleActiveMediaInAnswer = _SipInteropAllowMultipleActiveMediaInAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 95),
    _SipInteropAllowMultipleActiveMediaInAnswer_Type()
)
sipInteropAllowMultipleActiveMediaInAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropAllowMultipleActiveMediaInAnswer.setStatus("current")


class _SipInteropOnHoldSdpStreamDirection_Type(Integer32):
    """Custom type sipInteropOnHoldSdpStreamDirection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("sendonly", 1))
    )


_SipInteropOnHoldSdpStreamDirection_Type.__name__ = "Integer32"
_SipInteropOnHoldSdpStreamDirection_Object = MibScalar
sipInteropOnHoldSdpStreamDirection = _SipInteropOnHoldSdpStreamDirection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 100),
    _SipInteropOnHoldSdpStreamDirection_Type()
)
sipInteropOnHoldSdpStreamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropOnHoldSdpStreamDirection.setStatus("current")


class _SipInteropOnHoldAnswerSdpStreamDirection_Type(Integer32):
    """Custom type sipInteropOnHoldAnswerSdpStreamDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("recvonly", 1))
    )


_SipInteropOnHoldAnswerSdpStreamDirection_Type.__name__ = "Integer32"
_SipInteropOnHoldAnswerSdpStreamDirection_Object = MibScalar
sipInteropOnHoldAnswerSdpStreamDirection = _SipInteropOnHoldAnswerSdpStreamDirection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 105),
    _SipInteropOnHoldAnswerSdpStreamDirection_Type()
)
sipInteropOnHoldAnswerSdpStreamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropOnHoldAnswerSdpStreamDirection.setStatus("current")


class _SipInteropIgnoreMediaRenegotiationAfterCngDetection_Type(MxEnableState):
    """Custom type sipInteropIgnoreMediaRenegotiationAfterCngDetection based on MxEnableState"""
    defaultValue = 0


_SipInteropIgnoreMediaRenegotiationAfterCngDetection_Type.__name__ = "MxEnableState"
_SipInteropIgnoreMediaRenegotiationAfterCngDetection_Object = MibScalar
sipInteropIgnoreMediaRenegotiationAfterCngDetection = _SipInteropIgnoreMediaRenegotiationAfterCngDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 110),
    _SipInteropIgnoreMediaRenegotiationAfterCngDetection_Type()
)
sipInteropIgnoreMediaRenegotiationAfterCngDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropIgnoreMediaRenegotiationAfterCngDetection.setStatus("current")


class _SipInteropMwiMessageSummaryValidation_Type(MxEnableState):
    """Custom type sipInteropMwiMessageSummaryValidation based on MxEnableState"""
    defaultValue = 1


_SipInteropMwiMessageSummaryValidation_Type.__name__ = "MxEnableState"
_SipInteropMwiMessageSummaryValidation_Object = MibScalar
sipInteropMwiMessageSummaryValidation = _SipInteropMwiMessageSummaryValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 125),
    _SipInteropMwiMessageSummaryValidation_Type()
)
sipInteropMwiMessageSummaryValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropMwiMessageSummaryValidation.setStatus("current")


class _SipInteropSipOptionsMethodSupport_Type(Integer32):
    """Custom type sipInteropSipOptionsMethodSupport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("alwaysOk", 1))
    )


_SipInteropSipOptionsMethodSupport_Type.__name__ = "Integer32"
_SipInteropSipOptionsMethodSupport_Object = MibScalar
sipInteropSipOptionsMethodSupport = _SipInteropSipOptionsMethodSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 130),
    _SipInteropSipOptionsMethodSupport_Type()
)
sipInteropSipOptionsMethodSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropSipOptionsMethodSupport.setStatus("current")


class _SipInteropLocalRingOnProvisionalResponse_Type(MxEnableState):
    """Custom type sipInteropLocalRingOnProvisionalResponse based on MxEnableState"""
    defaultValue = 0


_SipInteropLocalRingOnProvisionalResponse_Type.__name__ = "MxEnableState"
_SipInteropLocalRingOnProvisionalResponse_Object = MibScalar
sipInteropLocalRingOnProvisionalResponse = _SipInteropLocalRingOnProvisionalResponse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 150),
    _SipInteropLocalRingOnProvisionalResponse_Type()
)
sipInteropLocalRingOnProvisionalResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropLocalRingOnProvisionalResponse.setStatus("current")


class _SipInteropCallWaitingToneControlViaSipInfo_Type(MxEnableState):
    """Custom type sipInteropCallWaitingToneControlViaSipInfo based on MxEnableState"""
    defaultValue = 0


_SipInteropCallWaitingToneControlViaSipInfo_Type.__name__ = "MxEnableState"
_SipInteropCallWaitingToneControlViaSipInfo_Object = MibScalar
sipInteropCallWaitingToneControlViaSipInfo = _SipInteropCallWaitingToneControlViaSipInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 175),
    _SipInteropCallWaitingToneControlViaSipInfo_Type()
)
sipInteropCallWaitingToneControlViaSipInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropCallWaitingToneControlViaSipInfo.setStatus("current")


class _SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Type(Integer32):
    """Custom type sipInteropSdpOriginLineSessionIDAndVersionMaxLength based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("max-32bits", 10),
          ("max-64bits", 20))
    )


_SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Type.__name__ = "Integer32"
_SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Object = MibScalar
sipInteropSdpOriginLineSessionIDAndVersionMaxLength = _SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 200),
    _SipInteropSdpOriginLineSessionIDAndVersionMaxLength_Type()
)
sipInteropSdpOriginLineSessionIDAndVersionMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropSdpOriginLineSessionIDAndVersionMaxLength.setStatus("current")


class _SipInteropIgnoreUsernameParam_Type(MxEnableState):
    """Custom type sipInteropIgnoreUsernameParam based on MxEnableState"""
    defaultValue = 0


_SipInteropIgnoreUsernameParam_Type.__name__ = "MxEnableState"
_SipInteropIgnoreUsernameParam_Object = MibScalar
sipInteropIgnoreUsernameParam = _SipInteropIgnoreUsernameParam_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 210),
    _SipInteropIgnoreUsernameParam_Type()
)
sipInteropIgnoreUsernameParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropIgnoreUsernameParam.setStatus("current")


class _SipInteropEscapePoundInSipUriUsername_Type(MxEnableState):
    """Custom type sipInteropEscapePoundInSipUriUsername based on MxEnableState"""
    defaultValue = 1


_SipInteropEscapePoundInSipUriUsername_Type.__name__ = "MxEnableState"
_SipInteropEscapePoundInSipUriUsername_Object = MibScalar
sipInteropEscapePoundInSipUriUsername = _SipInteropEscapePoundInSipUriUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 215),
    _SipInteropEscapePoundInSipUriUsername_Type()
)
sipInteropEscapePoundInSipUriUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropEscapePoundInSipUriUsername.setStatus("current")


class _SipInteropRegisterHomeDomainHostOverride_Type(OctetString):
    """Custom type sipInteropRegisterHomeDomainHostOverride based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipInteropRegisterHomeDomainHostOverride_Type.__name__ = "OctetString"
_SipInteropRegisterHomeDomainHostOverride_Object = MibScalar
sipInteropRegisterHomeDomainHostOverride = _SipInteropRegisterHomeDomainHostOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 225),
    _SipInteropRegisterHomeDomainHostOverride_Type()
)
sipInteropRegisterHomeDomainHostOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropRegisterHomeDomainHostOverride.setStatus("current")


class _SipInteropRetryFailedRegistration_Type(MxEnableState):
    """Custom type sipInteropRetryFailedRegistration based on MxEnableState"""
    defaultValue = 1


_SipInteropRetryFailedRegistration_Type.__name__ = "MxEnableState"
_SipInteropRetryFailedRegistration_Object = MibScalar
sipInteropRetryFailedRegistration = _SipInteropRetryFailedRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 235),
    _SipInteropRetryFailedRegistration_Type()
)
sipInteropRetryFailedRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropRetryFailedRegistration.setStatus("current")


class _SipInteropUseSipDomainInRequestURI_Type(MxEnableState):
    """Custom type sipInteropUseSipDomainInRequestURI based on MxEnableState"""
    defaultValue = 0


_SipInteropUseSipDomainInRequestURI_Type.__name__ = "MxEnableState"
_SipInteropUseSipDomainInRequestURI_Object = MibScalar
sipInteropUseSipDomainInRequestURI = _SipInteropUseSipDomainInRequestURI_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 240),
    _SipInteropUseSipDomainInRequestURI_Type()
)
sipInteropUseSipDomainInRequestURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropUseSipDomainInRequestURI.setStatus("current")


class _SipInteropReferredByConfig_Type(Integer32):
    """Custom type sipInteropReferredByConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useSipStackDefault", 0),
          ("useLocalUrl", 1))
    )


_SipInteropReferredByConfig_Type.__name__ = "Integer32"
_SipInteropReferredByConfig_Object = MibScalar
sipInteropReferredByConfig = _SipInteropReferredByConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 250),
    _SipInteropReferredByConfig_Type()
)
sipInteropReferredByConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropReferredByConfig.setStatus("current")


class _SipInteropConferenceServerMechanism_Type(Integer32):
    """Custom type sipInteropConferenceServerMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfc4579WithoutErrorRecovery", 0),
          ("rfc4579WithErrorRecovery", 1))
    )


_SipInteropConferenceServerMechanism_Type.__name__ = "Integer32"
_SipInteropConferenceServerMechanism_Object = MibScalar
sipInteropConferenceServerMechanism = _SipInteropConferenceServerMechanism_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 255),
    _SipInteropConferenceServerMechanism_Type()
)
sipInteropConferenceServerMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropConferenceServerMechanism.setStatus("current")


class _SipInteropUseItuT38Format_Type(MxEnableState):
    """Custom type sipInteropUseItuT38Format based on MxEnableState"""
    defaultValue = 0


_SipInteropUseItuT38Format_Type.__name__ = "MxEnableState"
_SipInteropUseItuT38Format_Object = MibScalar
sipInteropUseItuT38Format = _SipInteropUseItuT38Format_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 275),
    _SipInteropUseItuT38Format_Type()
)
sipInteropUseItuT38Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropUseItuT38Format.setStatus("current")


class _SipInteropT38NoSignalBehavior_Type(Integer32):
    """Custom type sipInteropT38NoSignalBehavior based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("receivingReInvite", 0),
          ("receivingAck", 1))
    )


_SipInteropT38NoSignalBehavior_Type.__name__ = "Integer32"
_SipInteropT38NoSignalBehavior_Object = MibScalar
sipInteropT38NoSignalBehavior = _SipInteropT38NoSignalBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 285),
    _SipInteropT38NoSignalBehavior_Type()
)
sipInteropT38NoSignalBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropT38NoSignalBehavior.setStatus("current")


class _SipInteropBehaviorOnT38InviteRejectedWith606_Type(Integer32):
    """Custom type sipInteropBehaviorOnT38InviteRejectedWith606 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dropCall", 1),
          ("usePreviousMediaNegotiation", 4))
    )


_SipInteropBehaviorOnT38InviteRejectedWith606_Type.__name__ = "Integer32"
_SipInteropBehaviorOnT38InviteRejectedWith606_Object = MibScalar
sipInteropBehaviorOnT38InviteRejectedWith606 = _SipInteropBehaviorOnT38InviteRejectedWith606_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 290),
    _SipInteropBehaviorOnT38InviteRejectedWith606_Type()
)
sipInteropBehaviorOnT38InviteRejectedWith606.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropBehaviorOnT38InviteRejectedWith606.setStatus("current")


class _SipInteropLockDnsSrvRecordPerCallEnable_Type(MxEnableState):
    """Custom type sipInteropLockDnsSrvRecordPerCallEnable based on MxEnableState"""
    defaultValue = 0


_SipInteropLockDnsSrvRecordPerCallEnable_Type.__name__ = "MxEnableState"
_SipInteropLockDnsSrvRecordPerCallEnable_Object = MibScalar
sipInteropLockDnsSrvRecordPerCallEnable = _SipInteropLockDnsSrvRecordPerCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 300),
    _SipInteropLockDnsSrvRecordPerCallEnable_Type()
)
sipInteropLockDnsSrvRecordPerCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropLockDnsSrvRecordPerCallEnable.setStatus("current")


class _SipInteropRemoveOutboundProxyRouteHeader_Type(MxEnableState):
    """Custom type sipInteropRemoveOutboundProxyRouteHeader based on MxEnableState"""
    defaultValue = 0


_SipInteropRemoveOutboundProxyRouteHeader_Type.__name__ = "MxEnableState"
_SipInteropRemoveOutboundProxyRouteHeader_Object = MibScalar
sipInteropRemoveOutboundProxyRouteHeader = _SipInteropRemoveOutboundProxyRouteHeader_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 325),
    _SipInteropRemoveOutboundProxyRouteHeader_Type()
)
sipInteropRemoveOutboundProxyRouteHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropRemoveOutboundProxyRouteHeader.setStatus("current")


class _SipInteropReuseCredentialEnable_Type(MxEnableState):
    """Custom type sipInteropReuseCredentialEnable based on MxEnableState"""
    defaultValue = 1


_SipInteropReuseCredentialEnable_Type.__name__ = "MxEnableState"
_SipInteropReuseCredentialEnable_Object = MibScalar
sipInteropReuseCredentialEnable = _SipInteropReuseCredentialEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 350),
    _SipInteropReuseCredentialEnable_Type()
)
sipInteropReuseCredentialEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropReuseCredentialEnable.setStatus("current")


class _SipInteropUsePAssertedHeader_Type(MxEnableState):
    """Custom type sipInteropUsePAssertedHeader based on MxEnableState"""
    defaultValue = 0


_SipInteropUsePAssertedHeader_Type.__name__ = "MxEnableState"
_SipInteropUsePAssertedHeader_Object = MibScalar
sipInteropUsePAssertedHeader = _SipInteropUsePAssertedHeader_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 360),
    _SipInteropUsePAssertedHeader_Type()
)
sipInteropUsePAssertedHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropUsePAssertedHeader.setStatus("current")


class _SipInteropRingingResponseCode_Type(Integer32):
    """Custom type sipInteropRingingResponseCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("send180Ringing", 0),
          ("send183WithSdp", 1))
    )


_SipInteropRingingResponseCode_Type.__name__ = "Integer32"
_SipInteropRingingResponseCode_Object = MibScalar
sipInteropRingingResponseCode = _SipInteropRingingResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 375),
    _SipInteropRingingResponseCode_Type()
)
sipInteropRingingResponseCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropRingingResponseCode.setStatus("current")


class _SipInteropRejectCodeForNoRessource_Type(Integer32):
    """Custom type sipInteropRejectCodeForNoRessource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("temporarilyUnavailable", 0),
          ("busyHere", 1))
    )


_SipInteropRejectCodeForNoRessource_Type.__name__ = "Integer32"
_SipInteropRejectCodeForNoRessource_Object = MibScalar
sipInteropRejectCodeForNoRessource = _SipInteropRejectCodeForNoRessource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 400),
    _SipInteropRejectCodeForNoRessource_Type()
)
sipInteropRejectCodeForNoRessource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropRejectCodeForNoRessource.setStatus("current")


class _SipInteropAckUnsupportedInfoRequests_Type(MxEnableState):
    """Custom type sipInteropAckUnsupportedInfoRequests based on MxEnableState"""
    defaultValue = 0


_SipInteropAckUnsupportedInfoRequests_Type.__name__ = "MxEnableState"
_SipInteropAckUnsupportedInfoRequests_Object = MibScalar
sipInteropAckUnsupportedInfoRequests = _SipInteropAckUnsupportedInfoRequests_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 415),
    _SipInteropAckUnsupportedInfoRequests_Type()
)
sipInteropAckUnsupportedInfoRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropAckUnsupportedInfoRequests.setStatus("current")


class _SipInteropBranchMatchingMethod_Type(Integer32):
    """Custom type sipInteropBranchMatchingMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfc2543", 0),
          ("rfc3261", 1))
    )


_SipInteropBranchMatchingMethod_Type.__name__ = "Integer32"
_SipInteropBranchMatchingMethod_Object = MibScalar
sipInteropBranchMatchingMethod = _SipInteropBranchMatchingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 425),
    _SipInteropBranchMatchingMethod_Type()
)
sipInteropBranchMatchingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropBranchMatchingMethod.setStatus("current")


class _SipInteropIgnoreViaBranchIdInCancelEnable_Type(MxEnableState):
    """Custom type sipInteropIgnoreViaBranchIdInCancelEnable based on MxEnableState"""
    defaultValue = 0


_SipInteropIgnoreViaBranchIdInCancelEnable_Type.__name__ = "MxEnableState"
_SipInteropIgnoreViaBranchIdInCancelEnable_Object = MibScalar
sipInteropIgnoreViaBranchIdInCancelEnable = _SipInteropIgnoreViaBranchIdInCancelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 432),
    _SipInteropIgnoreViaBranchIdInCancelEnable_Type()
)
sipInteropIgnoreViaBranchIdInCancelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropIgnoreViaBranchIdInCancelEnable.setStatus("current")


class _SipInteropDefaultRegistrationExpiration_Type(Unsigned32):
    """Custom type sipInteropDefaultRegistrationExpiration based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_SipInteropDefaultRegistrationExpiration_Type.__name__ = "Unsigned32"
_SipInteropDefaultRegistrationExpiration_Object = MibScalar
sipInteropDefaultRegistrationExpiration = _SipInteropDefaultRegistrationExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 438),
    _SipInteropDefaultRegistrationExpiration_Type()
)
sipInteropDefaultRegistrationExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropDefaultRegistrationExpiration.setStatus("current")


class _SipInteropDefaultPublicationExpiration_Type(Unsigned32):
    """Custom type sipInteropDefaultPublicationExpiration based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_SipInteropDefaultPublicationExpiration_Type.__name__ = "Unsigned32"
_SipInteropDefaultPublicationExpiration_Object = MibScalar
sipInteropDefaultPublicationExpiration = _SipInteropDefaultPublicationExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 439),
    _SipInteropDefaultPublicationExpiration_Type()
)
sipInteropDefaultPublicationExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropDefaultPublicationExpiration.setStatus("current")


class _SipInteropAuthenticationQop_Type(Integer32):
    """Custom type sipInteropAuthenticationQop based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auth", 0),
          ("auth-int", 1))
    )


_SipInteropAuthenticationQop_Type.__name__ = "Integer32"
_SipInteropAuthenticationQop_Object = MibScalar
sipInteropAuthenticationQop = _SipInteropAuthenticationQop_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 444),
    _SipInteropAuthenticationQop_Type()
)
sipInteropAuthenticationQop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropAuthenticationQop.setStatus("current")


class _SipInteropProxyAuthenticationUriParametersEnable_Type(MxEnableState):
    """Custom type sipInteropProxyAuthenticationUriParametersEnable based on MxEnableState"""
    defaultValue = 1


_SipInteropProxyAuthenticationUriParametersEnable_Type.__name__ = "MxEnableState"
_SipInteropProxyAuthenticationUriParametersEnable_Object = MibScalar
sipInteropProxyAuthenticationUriParametersEnable = _SipInteropProxyAuthenticationUriParametersEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 445),
    _SipInteropProxyAuthenticationUriParametersEnable_Type()
)
sipInteropProxyAuthenticationUriParametersEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropProxyAuthenticationUriParametersEnable.setStatus("current")


class _SipInteropUseDtmfPayloadTypeFoundInAnswer_Type(MxEnableState):
    """Custom type sipInteropUseDtmfPayloadTypeFoundInAnswer based on MxEnableState"""
    defaultValue = 0


_SipInteropUseDtmfPayloadTypeFoundInAnswer_Type.__name__ = "MxEnableState"
_SipInteropUseDtmfPayloadTypeFoundInAnswer_Object = MibScalar
sipInteropUseDtmfPayloadTypeFoundInAnswer = _SipInteropUseDtmfPayloadTypeFoundInAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 447),
    _SipInteropUseDtmfPayloadTypeFoundInAnswer_Type()
)
sipInteropUseDtmfPayloadTypeFoundInAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropUseDtmfPayloadTypeFoundInAnswer.setStatus("current")


class _SipInteropAllowAsymmetricDtmfPayloadType_Type(MxEnableState):
    """Custom type sipInteropAllowAsymmetricDtmfPayloadType based on MxEnableState"""
    defaultValue = 0


_SipInteropAllowAsymmetricDtmfPayloadType_Type.__name__ = "MxEnableState"
_SipInteropAllowAsymmetricDtmfPayloadType_Object = MibScalar
sipInteropAllowAsymmetricDtmfPayloadType = _SipInteropAllowAsymmetricDtmfPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 448),
    _SipInteropAllowAsymmetricDtmfPayloadType_Type()
)
sipInteropAllowAsymmetricDtmfPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropAllowAsymmetricDtmfPayloadType.setStatus("current")


class _SipInteropFromUriDomainSelection_Type(Integer32):
    """Custom type sipInteropFromUriDomainSelection based on Integer32"""
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
        *(("sipDomain", 0),
          ("localHostWanAddress", 1),
          ("localHostFqdn", 2))
    )


_SipInteropFromUriDomainSelection_Type.__name__ = "Integer32"
_SipInteropFromUriDomainSelection_Object = MibScalar
sipInteropFromUriDomainSelection = _SipInteropFromUriDomainSelection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 449),
    _SipInteropFromUriDomainSelection_Type()
)
sipInteropFromUriDomainSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropFromUriDomainSelection.setStatus("current")
_SipInteropDtmfTransportBySipProtocol_ObjectIdentity = ObjectIdentity
sipInteropDtmfTransportBySipProtocol = _SipInteropDtmfTransportBySipProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 450)
)


class _SipInteropDtmfTransportMethod_Type(Integer32):
    """Custom type sipInteropDtmfTransportMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("draftChoudhuriSipInfoDigit00", 0),
          ("infoDtmfRelay", 1))
    )


_SipInteropDtmfTransportMethod_Type.__name__ = "Integer32"
_SipInteropDtmfTransportMethod_Object = MibScalar
sipInteropDtmfTransportMethod = _SipInteropDtmfTransportMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 450, 50),
    _SipInteropDtmfTransportMethod_Type()
)
sipInteropDtmfTransportMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropDtmfTransportMethod.setStatus("current")


class _SipInteropDtmfTransportDuration_Type(Integer32):
    """Custom type sipInteropDtmfTransportDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_SipInteropDtmfTransportDuration_Type.__name__ = "Integer32"
_SipInteropDtmfTransportDuration_Object = MibScalar
sipInteropDtmfTransportDuration = _SipInteropDtmfTransportDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 450, 100),
    _SipInteropDtmfTransportDuration_Type()
)
sipInteropDtmfTransportDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropDtmfTransportDuration.setStatus("current")
_SipInteropInternationalCodeMapping_ObjectIdentity = ObjectIdentity
sipInteropInternationalCodeMapping = _SipInteropInternationalCodeMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 500)
)


class _SipInteropInternationalCodeMappingEnable_Type(MxEnableState):
    """Custom type sipInteropInternationalCodeMappingEnable based on MxEnableState"""
    defaultValue = 0


_SipInteropInternationalCodeMappingEnable_Type.__name__ = "MxEnableState"
_SipInteropInternationalCodeMappingEnable_Object = MibScalar
sipInteropInternationalCodeMappingEnable = _SipInteropInternationalCodeMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 500, 50),
    _SipInteropInternationalCodeMappingEnable_Type()
)
sipInteropInternationalCodeMappingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropInternationalCodeMappingEnable.setStatus("current")


class _SipInteropInternationalCodeMappingString_Type(OctetString):
    """Custom type sipInteropInternationalCodeMappingString based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SipInteropInternationalCodeMappingString_Type.__name__ = "OctetString"
_SipInteropInternationalCodeMappingString_Object = MibScalar
sipInteropInternationalCodeMappingString = _SipInteropInternationalCodeMappingString_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 1, 500, 100),
    _SipInteropInternationalCodeMappingString_Type()
)
sipInteropInternationalCodeMappingString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInteropInternationalCodeMappingString.setStatus("current")
_SipInteropConformance_ObjectIdentity = ObjectIdentity
sipInteropConformance = _SipInteropConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 2)
)
_SipInteropCompliances_ObjectIdentity = ObjectIdentity
sipInteropCompliances = _SipInteropCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 2, 1)
)
_SipInteropGroups_ObjectIdentity = ObjectIdentity
sipInteropGroups = _SipInteropGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 2, 2)
)

# Managed Objects groups

sipInteropGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 2, 2, 5)
)
sipInteropGroupVer1.setObjects(
      *(("MX-SIP-INTEROP-MIB", "sipInteropReplacesConfig"),
        ("MX-SIP-INTEROP-MIB", "sipInteropTransferVersion"),
        ("MX-SIP-INTEROP-MIB", "sipInteropSessionTimerVersion"),
        ("MX-SIP-INTEROP-MIB", "sipInteropTransmissionTimeout"),
        ("MX-SIP-INTEROP-MIB", "sipInteropReplacesVersion"),
        ("MX-SIP-INTEROP-MIB", "sipInteropSymmetricUdpSourcePortEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropMaxForwardsValue"),
        ("MX-SIP-INTEROP-MIB", "sipInteropAutomaticRejectionCode"),
        ("MX-SIP-INTEROP-MIB", "sipInteropSendUAHeaderEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropUAHeaderConfig"),
        ("MX-SIP-INTEROP-MIB", "sipInteropSdpDirectionAttributeEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropAllowMultipleActiveMediaInAnswer"),
        ("MX-SIP-INTEROP-MIB", "sipInteropOnHoldSdpStreamDirection"),
        ("MX-SIP-INTEROP-MIB", "sipInteropOnHoldAnswerSdpStreamDirection"),
        ("MX-SIP-INTEROP-MIB", "sipInteropIgnoreMediaRenegotiationAfterCngDetection"),
        ("MX-SIP-INTEROP-MIB", "sipInteropMwiMessageSummaryValidation"),
        ("MX-SIP-INTEROP-MIB", "sipInteropSipOptionsMethodSupport"),
        ("MX-SIP-INTEROP-MIB", "sipInteropLocalRingOnProvisionalResponse"),
        ("MX-SIP-INTEROP-MIB", "sipInteropCallWaitingToneControlViaSipInfo"),
        ("MX-SIP-INTEROP-MIB", "sipInteropSdpOriginLineSessionIDAndVersionMaxLength"),
        ("MX-SIP-INTEROP-MIB", "sipInteropIgnoreUsernameParam"),
        ("MX-SIP-INTEROP-MIB", "sipInteropRegisterHomeDomainHostOverride"),
        ("MX-SIP-INTEROP-MIB", "sipInteropRetryFailedRegistration"),
        ("MX-SIP-INTEROP-MIB", "sipInteropReferredByConfig"),
        ("MX-SIP-INTEROP-MIB", "sipInteropConferenceServerMechanism"),
        ("MX-SIP-INTEROP-MIB", "sipInteropUseItuT38Format"),
        ("MX-SIP-INTEROP-MIB", "sipInteropT38NoSignalBehavior"),
        ("MX-SIP-INTEROP-MIB", "sipInteropBehaviorOnT38InviteRejectedWith606"),
        ("MX-SIP-INTEROP-MIB", "sipInteropLockDnsSrvRecordPerCallEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropRemoveOutboundProxyRouteHeader"),
        ("MX-SIP-INTEROP-MIB", "sipInteropReuseCredentialEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropUsePAssertedHeader"),
        ("MX-SIP-INTEROP-MIB", "sipInteropRingingResponseCode"),
        ("MX-SIP-INTEROP-MIB", "sipInteropRejectCodeForNoRessource"),
        ("MX-SIP-INTEROP-MIB", "sipInteropAckUnsupportedInfoRequests"),
        ("MX-SIP-INTEROP-MIB", "sipInteropBranchMatchingMethod"),
        ("MX-SIP-INTEROP-MIB", "sipInteropIgnoreViaBranchIdInCancelEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropDefaultRegistrationExpiration"),
        ("MX-SIP-INTEROP-MIB", "sipInteropDefaultPublicationExpiration"),
        ("MX-SIP-INTEROP-MIB", "sipInteropAuthenticationQop"),
        ("MX-SIP-INTEROP-MIB", "sipInteropProxyAuthenticationUriParametersEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropUseDtmfPayloadTypeFoundInAnswer"),
        ("MX-SIP-INTEROP-MIB", "sipInteropAllowAsymmetricDtmfPayloadType"),
        ("MX-SIP-INTEROP-MIB", "sipInteropFromUriDomainSelection"),
        ("MX-SIP-INTEROP-MIB", "sipInteropDtmfTransportMethod"),
        ("MX-SIP-INTEROP-MIB", "sipInteropDtmfTransportDuration"),
        ("MX-SIP-INTEROP-MIB", "sipInteropInternationalCodeMappingEnable"),
        ("MX-SIP-INTEROP-MIB", "sipInteropInternationalCodeMappingString"))
)
if mibBuilder.loadTexts:
    sipInteropGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipInteropBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 20, 2, 1, 1)
)
sipInteropBasicComplVer1.setObjects(
    ("MX-SIP-INTEROP-MIB", "sipInteropGroupVer1")
)
if mibBuilder.loadTexts:
    sipInteropBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SIP-INTEROP-MIB",
    **{"sipInteropMIB": sipInteropMIB,
       "sipInteropMIBObjects": sipInteropMIBObjects,
       "sipInteropReplacesConfig": sipInteropReplacesConfig,
       "sipInteropTransferVersion": sipInteropTransferVersion,
       "sipInteropSessionTimerVersion": sipInteropSessionTimerVersion,
       "sipInteropTransmissionTimeout": sipInteropTransmissionTimeout,
       "sipInteropReplacesVersion": sipInteropReplacesVersion,
       "sipInteropSymmetricUdpSourcePortEnable": sipInteropSymmetricUdpSourcePortEnable,
       "sipInteropMaxForwardsValue": sipInteropMaxForwardsValue,
       "sipInteropAutomaticRejectionCode": sipInteropAutomaticRejectionCode,
       "sipInteropSendUAHeaderEnable": sipInteropSendUAHeaderEnable,
       "sipInteropUAHeaderConfig": sipInteropUAHeaderConfig,
       "sipInteropSdpDirectionAttributeEnable": sipInteropSdpDirectionAttributeEnable,
       "sipInteropAllowMultipleActiveMediaInAnswer": sipInteropAllowMultipleActiveMediaInAnswer,
       "sipInteropOnHoldSdpStreamDirection": sipInteropOnHoldSdpStreamDirection,
       "sipInteropOnHoldAnswerSdpStreamDirection": sipInteropOnHoldAnswerSdpStreamDirection,
       "sipInteropIgnoreMediaRenegotiationAfterCngDetection": sipInteropIgnoreMediaRenegotiationAfterCngDetection,
       "sipInteropMwiMessageSummaryValidation": sipInteropMwiMessageSummaryValidation,
       "sipInteropSipOptionsMethodSupport": sipInteropSipOptionsMethodSupport,
       "sipInteropLocalRingOnProvisionalResponse": sipInteropLocalRingOnProvisionalResponse,
       "sipInteropCallWaitingToneControlViaSipInfo": sipInteropCallWaitingToneControlViaSipInfo,
       "sipInteropSdpOriginLineSessionIDAndVersionMaxLength": sipInteropSdpOriginLineSessionIDAndVersionMaxLength,
       "sipInteropIgnoreUsernameParam": sipInteropIgnoreUsernameParam,
       "sipInteropEscapePoundInSipUriUsername": sipInteropEscapePoundInSipUriUsername,
       "sipInteropRegisterHomeDomainHostOverride": sipInteropRegisterHomeDomainHostOverride,
       "sipInteropRetryFailedRegistration": sipInteropRetryFailedRegistration,
       "sipInteropUseSipDomainInRequestURI": sipInteropUseSipDomainInRequestURI,
       "sipInteropReferredByConfig": sipInteropReferredByConfig,
       "sipInteropConferenceServerMechanism": sipInteropConferenceServerMechanism,
       "sipInteropUseItuT38Format": sipInteropUseItuT38Format,
       "sipInteropT38NoSignalBehavior": sipInteropT38NoSignalBehavior,
       "sipInteropBehaviorOnT38InviteRejectedWith606": sipInteropBehaviorOnT38InviteRejectedWith606,
       "sipInteropLockDnsSrvRecordPerCallEnable": sipInteropLockDnsSrvRecordPerCallEnable,
       "sipInteropRemoveOutboundProxyRouteHeader": sipInteropRemoveOutboundProxyRouteHeader,
       "sipInteropReuseCredentialEnable": sipInteropReuseCredentialEnable,
       "sipInteropUsePAssertedHeader": sipInteropUsePAssertedHeader,
       "sipInteropRingingResponseCode": sipInteropRingingResponseCode,
       "sipInteropRejectCodeForNoRessource": sipInteropRejectCodeForNoRessource,
       "sipInteropAckUnsupportedInfoRequests": sipInteropAckUnsupportedInfoRequests,
       "sipInteropBranchMatchingMethod": sipInteropBranchMatchingMethod,
       "sipInteropIgnoreViaBranchIdInCancelEnable": sipInteropIgnoreViaBranchIdInCancelEnable,
       "sipInteropDefaultRegistrationExpiration": sipInteropDefaultRegistrationExpiration,
       "sipInteropDefaultPublicationExpiration": sipInteropDefaultPublicationExpiration,
       "sipInteropAuthenticationQop": sipInteropAuthenticationQop,
       "sipInteropProxyAuthenticationUriParametersEnable": sipInteropProxyAuthenticationUriParametersEnable,
       "sipInteropUseDtmfPayloadTypeFoundInAnswer": sipInteropUseDtmfPayloadTypeFoundInAnswer,
       "sipInteropAllowAsymmetricDtmfPayloadType": sipInteropAllowAsymmetricDtmfPayloadType,
       "sipInteropFromUriDomainSelection": sipInteropFromUriDomainSelection,
       "sipInteropDtmfTransportBySipProtocol": sipInteropDtmfTransportBySipProtocol,
       "sipInteropDtmfTransportMethod": sipInteropDtmfTransportMethod,
       "sipInteropDtmfTransportDuration": sipInteropDtmfTransportDuration,
       "sipInteropInternationalCodeMapping": sipInteropInternationalCodeMapping,
       "sipInteropInternationalCodeMappingEnable": sipInteropInternationalCodeMappingEnable,
       "sipInteropInternationalCodeMappingString": sipInteropInternationalCodeMappingString,
       "sipInteropConformance": sipInteropConformance,
       "sipInteropCompliances": sipInteropCompliances,
       "sipInteropBasicComplVer1": sipInteropBasicComplVer1,
       "sipInteropGroups": sipInteropGroups,
       "sipInteropGroupVer1": sipInteropGroupVer1}
)
