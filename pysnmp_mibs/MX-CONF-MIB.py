# SNMP MIB module (MX-CONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CONF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:36 2025
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

confMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConfMIBObjects_ObjectIdentity = ObjectIdentity
confMIBObjects = _ConfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1)
)
_ScriptsGroup_ObjectIdentity = ObjectIdentity
scriptsGroup = _ScriptsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100)
)


class _ScriptGenericFileName_Type(OctetString):
    """Custom type scriptGenericFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_ScriptGenericFileName_Type.__name__ = "OctetString"
_ScriptGenericFileName_Object = MibScalar
scriptGenericFileName = _ScriptGenericFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 100),
    _ScriptGenericFileName_Type()
)
scriptGenericFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptGenericFileName.setStatus("current")


class _ScriptSpecificFileName_Type(OctetString):
    """Custom type scriptSpecificFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_ScriptSpecificFileName_Type.__name__ = "OctetString"
_ScriptSpecificFileName_Object = MibScalar
scriptSpecificFileName = _ScriptSpecificFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 200),
    _ScriptSpecificFileName_Type()
)
scriptSpecificFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptSpecificFileName.setStatus("current")


class _ScriptsLocation_Type(OctetString):
    """Custom type scriptsLocation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScriptsLocation_Type.__name__ = "OctetString"
_ScriptsLocation_Object = MibScalar
scriptsLocation = _ScriptsLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 300),
    _ScriptsLocation_Type()
)
scriptsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsLocation.setStatus("current")
_ScriptsTransferGroup_ObjectIdentity = ObjectIdentity
scriptsTransferGroup = _ScriptsTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400)
)


class _ScriptsTransferProtocol_Type(Integer32):
    """Custom type scriptsTransferProtocol based on Integer32"""
    defaultValue = 200

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
        *(("http", 100),
          ("https", 200),
          ("tftp", 300),
          ("ftp", 400),
          ("file", 500))
    )


_ScriptsTransferProtocol_Type.__name__ = "Integer32"
_ScriptsTransferProtocol_Object = MibScalar
scriptsTransferProtocol = _ScriptsTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 100),
    _ScriptsTransferProtocol_Type()
)
scriptsTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferProtocol.setStatus("current")


class _ScriptsTransferUsername_Type(OctetString):
    """Custom type scriptsTransferUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ScriptsTransferUsername_Type.__name__ = "OctetString"
_ScriptsTransferUsername_Object = MibScalar
scriptsTransferUsername = _ScriptsTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 200),
    _ScriptsTransferUsername_Type()
)
scriptsTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferUsername.setStatus("current")


class _ScriptsTransferPassword_Type(OctetString):
    """Custom type scriptsTransferPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ScriptsTransferPassword_Type.__name__ = "OctetString"
_ScriptsTransferPassword_Object = MibScalar
scriptsTransferPassword = _ScriptsTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 300),
    _ScriptsTransferPassword_Type()
)
scriptsTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferPassword.setStatus("current")


class _ScriptsTransferSrvHostname_Type(MxIpHostNamePort):
    """Custom type scriptsTransferSrvHostname based on MxIpHostNamePort"""
    defaultValue = OctetString("0.0.0.0:0")


_ScriptsTransferSrvHostname_Type.__name__ = "MxIpHostNamePort"
_ScriptsTransferSrvHostname_Object = MibScalar
scriptsTransferSrvHostname = _ScriptsTransferSrvHostname_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 400),
    _ScriptsTransferSrvHostname_Type()
)
scriptsTransferSrvHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferSrvHostname.setStatus("current")


class _ScriptsTransferCertificateValidation_Type(Integer32):
    """Custom type scriptsTransferCertificateValidation based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("noValidation", 100),
          ("hostName", 200))
    )


_ScriptsTransferCertificateValidation_Type.__name__ = "Integer32"
_ScriptsTransferCertificateValidation_Object = MibScalar
scriptsTransferCertificateValidation = _ScriptsTransferCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 500),
    _ScriptsTransferCertificateValidation_Type()
)
scriptsTransferCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferCertificateValidation.setStatus("current")


class _ScriptsTransferCertificateTrustLevel_Type(Integer32):
    """Custom type scriptsTransferCertificateTrustLevel based on Integer32"""
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
        *(("locallyTrusted", 100),
          ("ocspOptional", 200),
          ("ocspMandatory", 300))
    )


_ScriptsTransferCertificateTrustLevel_Type.__name__ = "Integer32"
_ScriptsTransferCertificateTrustLevel_Object = MibScalar
scriptsTransferCertificateTrustLevel = _ScriptsTransferCertificateTrustLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 600),
    _ScriptsTransferCertificateTrustLevel_Type()
)
scriptsTransferCertificateTrustLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferCertificateTrustLevel.setStatus("current")


class _ScriptsTransferCipherSuite_Type(Integer32):
    """Custom type scriptsTransferCipherSuite based on Integer32"""
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
        *(("cS1", 100),
          ("cS2", 200),
          ("cS3", 300))
    )


_ScriptsTransferCipherSuite_Type.__name__ = "Integer32"
_ScriptsTransferCipherSuite_Object = MibScalar
scriptsTransferCipherSuite = _ScriptsTransferCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 700),
    _ScriptsTransferCipherSuite_Type()
)
scriptsTransferCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferCipherSuite.setStatus("current")


class _ScriptsTransferTlsVersion_Type(Integer32):
    """Custom type scriptsTransferTlsVersion based on Integer32"""
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
        *(("sSLv3", 100),
          ("tLSv1", 200),
          ("tLSv1-1", 300),
          ("tLSv1-2", 400))
    )


_ScriptsTransferTlsVersion_Type.__name__ = "Integer32"
_ScriptsTransferTlsVersion_Object = MibScalar
scriptsTransferTlsVersion = _ScriptsTransferTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 800),
    _ScriptsTransferTlsVersion_Type()
)
scriptsTransferTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferTlsVersion.setStatus("current")


class _ScriptsTransferHttpAuthenticationMethod_Type(Integer32):
    """Custom type scriptsTransferHttpAuthenticationMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("normal", 100),
          ("proprietaryV1", 200))
    )


_ScriptsTransferHttpAuthenticationMethod_Type.__name__ = "Integer32"
_ScriptsTransferHttpAuthenticationMethod_Object = MibScalar
scriptsTransferHttpAuthenticationMethod = _ScriptsTransferHttpAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 400, 900),
    _ScriptsTransferHttpAuthenticationMethod_Type()
)
scriptsTransferHttpAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferHttpAuthenticationMethod.setStatus("current")
_AutomaticScriptsTransferGroup_ObjectIdentity = ObjectIdentity
automaticScriptsTransferGroup = _AutomaticScriptsTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500)
)


class _ScriptsTransferOnRestartEnable_Type(MxEnableState):
    """Custom type scriptsTransferOnRestartEnable based on MxEnableState"""
    defaultValue = 0


_ScriptsTransferOnRestartEnable_Type.__name__ = "MxEnableState"
_ScriptsTransferOnRestartEnable_Object = MibScalar
scriptsTransferOnRestartEnable = _ScriptsTransferOnRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 100),
    _ScriptsTransferOnRestartEnable_Type()
)
scriptsTransferOnRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferOnRestartEnable.setStatus("current")


class _ScriptsTransferRetriesNumber_Type(Integer32):
    """Custom type scriptsTransferRetriesNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_ScriptsTransferRetriesNumber_Type.__name__ = "Integer32"
_ScriptsTransferRetriesNumber_Object = MibScalar
scriptsTransferRetriesNumber = _ScriptsTransferRetriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 150),
    _ScriptsTransferRetriesNumber_Type()
)
scriptsTransferRetriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferRetriesNumber.setStatus("current")


class _ScriptsTransferPeriodicEnable_Type(MxEnableState):
    """Custom type scriptsTransferPeriodicEnable based on MxEnableState"""
    defaultValue = 0


_ScriptsTransferPeriodicEnable_Type.__name__ = "MxEnableState"
_ScriptsTransferPeriodicEnable_Object = MibScalar
scriptsTransferPeriodicEnable = _ScriptsTransferPeriodicEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 200),
    _ScriptsTransferPeriodicEnable_Type()
)
scriptsTransferPeriodicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferPeriodicEnable.setStatus("current")


class _ScriptsTransferPeriodicTimeUnit_Type(Integer32):
    """Custom type scriptsTransferPeriodicTimeUnit based on Integer32"""
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
        *(("minutes", 100),
          ("hours", 200),
          ("days", 300))
    )


_ScriptsTransferPeriodicTimeUnit_Type.__name__ = "Integer32"
_ScriptsTransferPeriodicTimeUnit_Object = MibScalar
scriptsTransferPeriodicTimeUnit = _ScriptsTransferPeriodicTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 300),
    _ScriptsTransferPeriodicTimeUnit_Type()
)
scriptsTransferPeriodicTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferPeriodicTimeUnit.setStatus("current")


class _ScriptsTransferInterval_Type(Unsigned32):
    """Custom type scriptsTransferInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ScriptsTransferInterval_Type.__name__ = "Unsigned32"
_ScriptsTransferInterval_Object = MibScalar
scriptsTransferInterval = _ScriptsTransferInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 400),
    _ScriptsTransferInterval_Type()
)
scriptsTransferInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferInterval.setStatus("current")


class _ScriptsTransferTimeOfDay_Type(Integer32):
    """Custom type scriptsTransferTimeOfDay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_ScriptsTransferTimeOfDay_Type.__name__ = "Integer32"
_ScriptsTransferTimeOfDay_Object = MibScalar
scriptsTransferTimeOfDay = _ScriptsTransferTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 500),
    _ScriptsTransferTimeOfDay_Type()
)
scriptsTransferTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferTimeOfDay.setStatus("obsolete")


class _ScriptsDhcpDownloadEnable_Type(MxEnableState):
    """Custom type scriptsDhcpDownloadEnable based on MxEnableState"""
    defaultValue = 1


_ScriptsDhcpDownloadEnable_Type.__name__ = "MxEnableState"
_ScriptsDhcpDownloadEnable_Object = MibScalar
scriptsDhcpDownloadEnable = _ScriptsDhcpDownloadEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 600),
    _ScriptsDhcpDownloadEnable_Type()
)
scriptsDhcpDownloadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsDhcpDownloadEnable.setStatus("current")


class _ScriptsDhcpOptionsFormat_Type(Integer32):
    """Custom type scriptsDhcpOptionsFormat based on Integer32"""
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
        *(("fullyQualified", 100),
          ("url", 200),
          ("serverHost", 300),
          ("autoDetect", 400))
    )


_ScriptsDhcpOptionsFormat_Type.__name__ = "Integer32"
_ScriptsDhcpOptionsFormat_Object = MibScalar
scriptsDhcpOptionsFormat = _ScriptsDhcpOptionsFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 650),
    _ScriptsDhcpOptionsFormat_Type()
)
scriptsDhcpOptionsFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsDhcpOptionsFormat.setStatus("current")


class _ScriptsTransferOnRestartDhcpScriptMaxDelay_Type(Unsigned32):
    """Custom type scriptsTransferOnRestartDhcpScriptMaxDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_ScriptsTransferOnRestartDhcpScriptMaxDelay_Type.__name__ = "Unsigned32"
_ScriptsTransferOnRestartDhcpScriptMaxDelay_Object = MibScalar
scriptsTransferOnRestartDhcpScriptMaxDelay = _ScriptsTransferOnRestartDhcpScriptMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 660),
    _ScriptsTransferOnRestartDhcpScriptMaxDelay_Type()
)
scriptsTransferOnRestartDhcpScriptMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferOnRestartDhcpScriptMaxDelay.setStatus("current")


class _ScriptsTransferTimeRange_Type(OctetString):
    """Custom type scriptsTransferTimeRange based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ScriptsTransferTimeRange_Type.__name__ = "OctetString"
_ScriptsTransferTimeRange_Object = MibScalar
scriptsTransferTimeRange = _ScriptsTransferTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 500, 700),
    _ScriptsTransferTimeRange_Type()
)
scriptsTransferTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTransferTimeRange.setStatus("current")


class _ScriptsSecretKey_Type(OctetString):
    """Custom type scriptsSecretKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_ScriptsSecretKey_Type.__name__ = "OctetString"
_ScriptsSecretKey_Object = MibScalar
scriptsSecretKey = _ScriptsSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 600),
    _ScriptsSecretKey_Type()
)
scriptsSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsSecretKey.setStatus("current")


class _ScriptsAllowRepeatedExecution_Type(MxEnableState):
    """Custom type scriptsAllowRepeatedExecution based on MxEnableState"""
    defaultValue = 1


_ScriptsAllowRepeatedExecution_Type.__name__ = "MxEnableState"
_ScriptsAllowRepeatedExecution_Object = MibScalar
scriptsAllowRepeatedExecution = _ScriptsAllowRepeatedExecution_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 650),
    _ScriptsAllowRepeatedExecution_Type()
)
scriptsAllowRepeatedExecution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsAllowRepeatedExecution.setStatus("current")
_ScriptExportGroup_ObjectIdentity = ObjectIdentity
scriptExportGroup = _ScriptExportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 1000)
)


class _ScriptExportContent_Type(Integer32):
    """Custom type scriptExportContent based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("allConfig", 100),
          ("modifiedConfig", 200))
    )


_ScriptExportContent_Type.__name__ = "Integer32"
_ScriptExportContent_Object = MibScalar
scriptExportContent = _ScriptExportContent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 1000, 100),
    _ScriptExportContent_Type()
)
scriptExportContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptExportContent.setStatus("current")


class _ScriptExportServiceName_Type(OctetString):
    """Custom type scriptExportServiceName based on OctetString"""
    defaultValue = OctetString("All")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScriptExportServiceName_Type.__name__ = "OctetString"
_ScriptExportServiceName_Object = MibScalar
scriptExportServiceName = _ScriptExportServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 1000, 150),
    _ScriptExportServiceName_Type()
)
scriptExportServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptExportServiceName.setStatus("current")


class _ScriptExportUrl_Type(OctetString):
    """Custom type scriptExportUrl based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ScriptExportUrl_Type.__name__ = "OctetString"
_ScriptExportUrl_Object = MibScalar
scriptExportUrl = _ScriptExportUrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 1000, 200),
    _ScriptExportUrl_Type()
)
scriptExportUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptExportUrl.setStatus("current")


class _ScriptExportSecretKey_Type(OctetString):
    """Custom type scriptExportSecretKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScriptExportSecretKey_Type.__name__ = "OctetString"
_ScriptExportSecretKey_Object = MibScalar
scriptExportSecretKey = _ScriptExportSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 1000, 300),
    _ScriptExportSecretKey_Type()
)
scriptExportSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptExportSecretKey.setStatus("current")
_ScriptsStatsGroup_ObjectIdentity = ObjectIdentity
scriptsStatsGroup = _ScriptsStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000)
)


class _ScriptsStatsCurrentTransferState_Type(Integer32):
    """Custom type scriptsStatsCurrentTransferState based on Integer32"""
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
        *(("idle", 100),
          ("transfering", 200),
          ("running", 300))
    )


_ScriptsStatsCurrentTransferState_Type.__name__ = "Integer32"
_ScriptsStatsCurrentTransferState_Object = MibScalar
scriptsStatsCurrentTransferState = _ScriptsStatsCurrentTransferState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000, 700),
    _ScriptsStatsCurrentTransferState_Type()
)
scriptsStatsCurrentTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptsStatsCurrentTransferState.setStatus("current")


class _ScriptsStatsLastTransferResult_Type(Integer32):
    """Custom type scriptsStatsLastTransferResult based on Integer32"""
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
          ("executionFailed", 300),
          ("transferFailed", 400))
    )


_ScriptsStatsLastTransferResult_Type.__name__ = "Integer32"
_ScriptsStatsLastTransferResult_Object = MibScalar
scriptsStatsLastTransferResult = _ScriptsStatsLastTransferResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000, 800),
    _ScriptsStatsLastTransferResult_Type()
)
scriptsStatsLastTransferResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptsStatsLastTransferResult.setStatus("current")


class _ScriptsStatsLastTransferDateTime_Type(OctetString):
    """Custom type scriptsStatsLastTransferDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScriptsStatsLastTransferDateTime_Type.__name__ = "OctetString"
_ScriptsStatsLastTransferDateTime_Object = MibScalar
scriptsStatsLastTransferDateTime = _ScriptsStatsLastTransferDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000, 900),
    _ScriptsStatsLastTransferDateTime_Type()
)
scriptsStatsLastTransferDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptsStatsLastTransferDateTime.setStatus("current")


class _ScriptsStatsCurrentExportState_Type(Integer32):
    """Custom type scriptsStatsCurrentExportState based on Integer32"""
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
        *(("idle", 100),
          ("transfering", 200),
          ("exporting", 300))
    )


_ScriptsStatsCurrentExportState_Type.__name__ = "Integer32"
_ScriptsStatsCurrentExportState_Object = MibScalar
scriptsStatsCurrentExportState = _ScriptsStatsCurrentExportState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000, 1000),
    _ScriptsStatsCurrentExportState_Type()
)
scriptsStatsCurrentExportState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptsStatsCurrentExportState.setStatus("current")


class _ScriptsStatsLastExportResult_Type(Integer32):
    """Custom type scriptsStatsLastExportResult based on Integer32"""
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
          ("exportationFailed", 300),
          ("transferFailed", 400))
    )


_ScriptsStatsLastExportResult_Type.__name__ = "Integer32"
_ScriptsStatsLastExportResult_Object = MibScalar
scriptsStatsLastExportResult = _ScriptsStatsLastExportResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000, 1100),
    _ScriptsStatsLastExportResult_Type()
)
scriptsStatsLastExportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptsStatsLastExportResult.setStatus("current")


class _ScriptsStatsLastExportDateTime_Type(OctetString):
    """Custom type scriptsStatsLastExportDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScriptsStatsLastExportDateTime_Type.__name__ = "OctetString"
_ScriptsStatsLastExportDateTime_Object = MibScalar
scriptsStatsLastExportDateTime = _ScriptsStatsLastExportDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 100, 10000, 1200),
    _ScriptsStatsLastExportDateTime_Type()
)
scriptsStatsLastExportDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptsStatsLastExportDateTime.setStatus("current")
_ImageGroup_ObjectIdentity = ObjectIdentity
imageGroup = _ImageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200)
)


class _ImageFileName_Type(OctetString):
    """Custom type imageFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_ImageFileName_Type.__name__ = "OctetString"
_ImageFileName_Object = MibScalar
imageFileName = _ImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 100),
    _ImageFileName_Type()
)
imageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageFileName.setStatus("current")


class _ImageLocation_Type(OctetString):
    """Custom type imageLocation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ImageLocation_Type.__name__ = "OctetString"
_ImageLocation_Object = MibScalar
imageLocation = _ImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 200),
    _ImageLocation_Type()
)
imageLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageLocation.setStatus("current")


class _ImageBackupContent_Type(Integer32):
    """Custom type imageBackupContent based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("config", 100),
          ("configAndCertificates", 200))
    )


_ImageBackupContent_Type.__name__ = "Integer32"
_ImageBackupContent_Object = MibScalar
imageBackupContent = _ImageBackupContent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 250),
    _ImageBackupContent_Type()
)
imageBackupContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageBackupContent.setStatus("current")
_ImageTransferGroup_ObjectIdentity = ObjectIdentity
imageTransferGroup = _ImageTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300)
)


class _ImageTransferProtocol_Type(Integer32):
    """Custom type imageTransferProtocol based on Integer32"""
    defaultValue = 200

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
        *(("http", 100),
          ("https", 200),
          ("tftp", 300),
          ("ftp", 400),
          ("file", 500))
    )


_ImageTransferProtocol_Type.__name__ = "Integer32"
_ImageTransferProtocol_Object = MibScalar
imageTransferProtocol = _ImageTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300, 100),
    _ImageTransferProtocol_Type()
)
imageTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferProtocol.setStatus("current")


class _ImageTransferUsername_Type(OctetString):
    """Custom type imageTransferUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageTransferUsername_Type.__name__ = "OctetString"
_ImageTransferUsername_Object = MibScalar
imageTransferUsername = _ImageTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300, 200),
    _ImageTransferUsername_Type()
)
imageTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferUsername.setStatus("current")


class _ImageTransferPassword_Type(OctetString):
    """Custom type imageTransferPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageTransferPassword_Type.__name__ = "OctetString"
_ImageTransferPassword_Object = MibScalar
imageTransferPassword = _ImageTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300, 300),
    _ImageTransferPassword_Type()
)
imageTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferPassword.setStatus("current")


class _ImageTransferSrvHostname_Type(MxIpHostNamePort):
    """Custom type imageTransferSrvHostname based on MxIpHostNamePort"""
    defaultValue = OctetString("0.0.0.0:0")


_ImageTransferSrvHostname_Type.__name__ = "MxIpHostNamePort"
_ImageTransferSrvHostname_Object = MibScalar
imageTransferSrvHostname = _ImageTransferSrvHostname_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300, 400),
    _ImageTransferSrvHostname_Type()
)
imageTransferSrvHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferSrvHostname.setStatus("current")


class _ImageTransferCipherSuite_Type(Integer32):
    """Custom type imageTransferCipherSuite based on Integer32"""
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
        *(("cS1", 100),
          ("cS2", 200),
          ("cS3", 300))
    )


_ImageTransferCipherSuite_Type.__name__ = "Integer32"
_ImageTransferCipherSuite_Object = MibScalar
imageTransferCipherSuite = _ImageTransferCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300, 500),
    _ImageTransferCipherSuite_Type()
)
imageTransferCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferCipherSuite.setStatus("current")


class _ImageTransferTlsVersion_Type(Integer32):
    """Custom type imageTransferTlsVersion based on Integer32"""
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
        *(("sSLv3", 100),
          ("tLSv1", 200),
          ("tLSv1-1", 300),
          ("tLSv1-2", 400))
    )


_ImageTransferTlsVersion_Type.__name__ = "Integer32"
_ImageTransferTlsVersion_Object = MibScalar
imageTransferTlsVersion = _ImageTransferTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 300, 600),
    _ImageTransferTlsVersion_Type()
)
imageTransferTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferTlsVersion.setStatus("current")
_ImagePrivacyGroup_ObjectIdentity = ObjectIdentity
imagePrivacyGroup = _ImagePrivacyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 400)
)


class _ImagePrivacyAlgo_Type(Integer32):
    """Custom type imagePrivacyAlgo based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("defaultAlgo", 200))
    )


_ImagePrivacyAlgo_Type.__name__ = "Integer32"
_ImagePrivacyAlgo_Object = MibScalar
imagePrivacyAlgo = _ImagePrivacyAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 400, 100),
    _ImagePrivacyAlgo_Type()
)
imagePrivacyAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imagePrivacyAlgo.setStatus("current")


class _ImageSecretKey_Type(OctetString):
    """Custom type imageSecretKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ImageSecretKey_Type.__name__ = "OctetString"
_ImageSecretKey_Object = MibScalar
imageSecretKey = _ImageSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 400, 200),
    _ImageSecretKey_Type()
)
imageSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageSecretKey.setStatus("current")


class _ImageBackupStatus_Type(Integer32):
    """Custom type imageBackupStatus based on Integer32"""
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
          ("success", 200),
          ("failed", 300))
    )


_ImageBackupStatus_Type.__name__ = "Integer32"
_ImageBackupStatus_Object = MibScalar
imageBackupStatus = _ImageBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 600),
    _ImageBackupStatus_Type()
)
imageBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageBackupStatus.setStatus("current")


class _ImageRestoreStatus_Type(Integer32):
    """Custom type imageRestoreStatus based on Integer32"""
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
          ("applyFailed", 300),
          ("loadFailed", 400))
    )


_ImageRestoreStatus_Type.__name__ = "Integer32"
_ImageRestoreStatus_Object = MibScalar
imageRestoreStatus = _ImageRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 200, 800),
    _ImageRestoreStatus_Type()
)
imageRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageRestoreStatus.setStatus("current")
_AliasGroup_ObjectIdentity = ObjectIdentity
aliasGroup = _AliasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300)
)
_MacrosTable_Object = MibTable
macrosTable = _MacrosTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 100)
)
if mibBuilder.loadTexts:
    macrosTable.setStatus("current")
_MacrosEntry_Object = MibTableRow
macrosEntry = _MacrosEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 100, 1)
)
macrosEntry.setIndexNames(
    (0, "MX-CONF-MIB", "macrosName"),
)
if mibBuilder.loadTexts:
    macrosEntry.setStatus("current")


class _MacrosName_Type(OctetString):
    """Custom type macrosName based on OctetString"""
    defaultValue = OctetString("")


_MacrosName_Type.__name__ = "OctetString"
_MacrosName_Object = MibTableColumn
macrosName = _MacrosName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 100, 1, 100),
    _MacrosName_Type()
)
macrosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macrosName.setStatus("current")


class _MacrosDescription_Type(OctetString):
    """Custom type macrosDescription based on OctetString"""
    defaultValue = OctetString("")


_MacrosDescription_Type.__name__ = "OctetString"
_MacrosDescription_Object = MibTableColumn
macrosDescription = _MacrosDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 100, 1, 200),
    _MacrosDescription_Type()
)
macrosDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macrosDescription.setStatus("current")
_AliasTable_Object = MibTable
aliasTable = _AliasTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 200)
)
if mibBuilder.loadTexts:
    aliasTable.setStatus("current")
_AliasEntry_Object = MibTableRow
aliasEntry = _AliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 200, 1)
)
aliasEntry.setIndexNames(
    (0, "MX-CONF-MIB", "aliasName"),
)
if mibBuilder.loadTexts:
    aliasEntry.setStatus("current")


class _AliasName_Type(OctetString):
    """Custom type aliasName based on OctetString"""
    defaultValue = OctetString("")


_AliasName_Type.__name__ = "OctetString"
_AliasName_Object = MibTableColumn
aliasName = _AliasName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 200, 1, 100),
    _AliasName_Type()
)
aliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aliasName.setStatus("current")
_AliasEntity_Type = OctetString
_AliasEntity_Object = MibTableColumn
aliasEntity = _AliasEntity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 200, 1, 200),
    _AliasEntity_Type()
)
aliasEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aliasEntity.setStatus("current")


class _AliasType_Type(Integer32):
    """Custom type aliasType based on Integer32"""
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
        *(("module", 100),
          ("object", 200),
          ("columnar", 300))
    )


_AliasType_Type.__name__ = "Integer32"
_AliasType_Object = MibTableColumn
aliasType = _AliasType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 200, 1, 300),
    _AliasType_Type()
)
aliasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aliasType.setStatus("current")
_AliasContext_Type = OctetString
_AliasContext_Object = MibTableColumn
aliasContext = _AliasContext_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 300, 200, 1, 400),
    _AliasContext_Type()
)
aliasContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aliasContext.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 800, 1, 60020, 100),
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
    "MX-CONF-MIB",
    **{"confMIB": confMIB,
       "confMIBObjects": confMIBObjects,
       "scriptsGroup": scriptsGroup,
       "scriptGenericFileName": scriptGenericFileName,
       "scriptSpecificFileName": scriptSpecificFileName,
       "scriptsLocation": scriptsLocation,
       "scriptsTransferGroup": scriptsTransferGroup,
       "scriptsTransferProtocol": scriptsTransferProtocol,
       "scriptsTransferUsername": scriptsTransferUsername,
       "scriptsTransferPassword": scriptsTransferPassword,
       "scriptsTransferSrvHostname": scriptsTransferSrvHostname,
       "scriptsTransferCertificateValidation": scriptsTransferCertificateValidation,
       "scriptsTransferCertificateTrustLevel": scriptsTransferCertificateTrustLevel,
       "scriptsTransferCipherSuite": scriptsTransferCipherSuite,
       "scriptsTransferTlsVersion": scriptsTransferTlsVersion,
       "scriptsTransferHttpAuthenticationMethod": scriptsTransferHttpAuthenticationMethod,
       "automaticScriptsTransferGroup": automaticScriptsTransferGroup,
       "scriptsTransferOnRestartEnable": scriptsTransferOnRestartEnable,
       "scriptsTransferRetriesNumber": scriptsTransferRetriesNumber,
       "scriptsTransferPeriodicEnable": scriptsTransferPeriodicEnable,
       "scriptsTransferPeriodicTimeUnit": scriptsTransferPeriodicTimeUnit,
       "scriptsTransferInterval": scriptsTransferInterval,
       "scriptsTransferTimeOfDay": scriptsTransferTimeOfDay,
       "scriptsDhcpDownloadEnable": scriptsDhcpDownloadEnable,
       "scriptsDhcpOptionsFormat": scriptsDhcpOptionsFormat,
       "scriptsTransferOnRestartDhcpScriptMaxDelay": scriptsTransferOnRestartDhcpScriptMaxDelay,
       "scriptsTransferTimeRange": scriptsTransferTimeRange,
       "scriptsSecretKey": scriptsSecretKey,
       "scriptsAllowRepeatedExecution": scriptsAllowRepeatedExecution,
       "scriptExportGroup": scriptExportGroup,
       "scriptExportContent": scriptExportContent,
       "scriptExportServiceName": scriptExportServiceName,
       "scriptExportUrl": scriptExportUrl,
       "scriptExportSecretKey": scriptExportSecretKey,
       "scriptsStatsGroup": scriptsStatsGroup,
       "scriptsStatsCurrentTransferState": scriptsStatsCurrentTransferState,
       "scriptsStatsLastTransferResult": scriptsStatsLastTransferResult,
       "scriptsStatsLastTransferDateTime": scriptsStatsLastTransferDateTime,
       "scriptsStatsCurrentExportState": scriptsStatsCurrentExportState,
       "scriptsStatsLastExportResult": scriptsStatsLastExportResult,
       "scriptsStatsLastExportDateTime": scriptsStatsLastExportDateTime,
       "imageGroup": imageGroup,
       "imageFileName": imageFileName,
       "imageLocation": imageLocation,
       "imageBackupContent": imageBackupContent,
       "imageTransferGroup": imageTransferGroup,
       "imageTransferProtocol": imageTransferProtocol,
       "imageTransferUsername": imageTransferUsername,
       "imageTransferPassword": imageTransferPassword,
       "imageTransferSrvHostname": imageTransferSrvHostname,
       "imageTransferCipherSuite": imageTransferCipherSuite,
       "imageTransferTlsVersion": imageTransferTlsVersion,
       "imagePrivacyGroup": imagePrivacyGroup,
       "imagePrivacyAlgo": imagePrivacyAlgo,
       "imageSecretKey": imageSecretKey,
       "imageBackupStatus": imageBackupStatus,
       "imageRestoreStatus": imageRestoreStatus,
       "aliasGroup": aliasGroup,
       "macrosTable": macrosTable,
       "macrosEntry": macrosEntry,
       "macrosName": macrosName,
       "macrosDescription": macrosDescription,
       "aliasTable": aliasTable,
       "aliasEntry": aliasEntry,
       "aliasName": aliasName,
       "aliasEntity": aliasEntity,
       "aliasType": aliasType,
       "aliasContext": aliasContext,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
