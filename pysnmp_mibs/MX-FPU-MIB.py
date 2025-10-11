# SNMP MIB module (MX-FPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-FPU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:56 2025
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

fpuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FpuMIBObjects_ObjectIdentity = ObjectIdentity
fpuMIBObjects = _FpuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1)
)
_MfpInstalledInfoTable_Object = MibTable
mfpInstalledInfoTable = _MfpInstalledInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100)
)
if mibBuilder.loadTexts:
    mfpInstalledInfoTable.setStatus("current")
_MfpInstalledInfoEntry_Object = MibTableRow
mfpInstalledInfoEntry = _MfpInstalledInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100, 1)
)
mfpInstalledInfoEntry.setIndexNames(
    (0, "MX-FPU-MIB", "mfpInstalledInfoIndex"),
)
if mibBuilder.loadTexts:
    mfpInstalledInfoEntry.setStatus("current")
_MfpInstalledInfoIndex_Type = Unsigned32
_MfpInstalledInfoIndex_Object = MibTableColumn
mfpInstalledInfoIndex = _MfpInstalledInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100, 1, 50),
    _MfpInstalledInfoIndex_Type()
)
mfpInstalledInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpInstalledInfoIndex.setStatus("current")
_MfpInstalledInfoMfpName_Type = OctetString
_MfpInstalledInfoMfpName_Object = MibTableColumn
mfpInstalledInfoMfpName = _MfpInstalledInfoMfpName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100, 1, 100),
    _MfpInstalledInfoMfpName_Type()
)
mfpInstalledInfoMfpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpInstalledInfoMfpName.setStatus("current")
_MfpInstalledInfoMfpVersion_Type = OctetString
_MfpInstalledInfoMfpVersion_Object = MibTableColumn
mfpInstalledInfoMfpVersion = _MfpInstalledInfoMfpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100, 1, 200),
    _MfpInstalledInfoMfpVersion_Type()
)
mfpInstalledInfoMfpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpInstalledInfoMfpVersion.setStatus("current")


class _MfpInstalledInfoMfpBank_Type(Integer32):
    """Custom type mfpInstalledInfoMfpBank based on Integer32"""
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
        *(("none", 100),
          ("main", 200),
          ("recovery", 300),
          ("mainInUse", 400),
          ("recoveryInUse", 500))
    )


_MfpInstalledInfoMfpBank_Type.__name__ = "Integer32"
_MfpInstalledInfoMfpBank_Object = MibTableColumn
mfpInstalledInfoMfpBank = _MfpInstalledInfoMfpBank_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100, 1, 300),
    _MfpInstalledInfoMfpBank_Type()
)
mfpInstalledInfoMfpBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpInstalledInfoMfpBank.setStatus("current")


class _MfpInstalledInfoMfpProfileName_Type(OctetString):
    """Custom type mfpInstalledInfoMfpProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MfpInstalledInfoMfpProfileName_Type.__name__ = "OctetString"
_MfpInstalledInfoMfpProfileName_Object = MibTableColumn
mfpInstalledInfoMfpProfileName = _MfpInstalledInfoMfpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 100, 1, 400),
    _MfpInstalledInfoMfpProfileName_Type()
)
mfpInstalledInfoMfpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpInstalledInfoMfpProfileName.setStatus("current")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
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
        *(("waitingSystemReady", 100),
          ("idle", 200),
          ("updating", 300),
          ("waitingManualRestart", 400),
          ("rollbacking", 500),
          ("waitingForGracefulRestart", 600))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 110),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _MfpLastInstallationResult_Type(Integer32):
    """Custom type mfpLastInstallationResult based on Integer32"""
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
          ("fail", 300))
    )


_MfpLastInstallationResult_Type.__name__ = "Integer32"
_MfpLastInstallationResult_Object = MibScalar
mfpLastInstallationResult = _MfpLastInstallationResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 125),
    _MfpLastInstallationResult_Type()
)
mfpLastInstallationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpLastInstallationResult.setStatus("current")


class _MfpLastInstallationDateTime_Type(OctetString):
    """Custom type mfpLastInstallationDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MfpLastInstallationDateTime_Type.__name__ = "OctetString"
_MfpLastInstallationDateTime_Object = MibScalar
mfpLastInstallationDateTime = _MfpLastInstallationDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 150),
    _MfpLastInstallationDateTime_Type()
)
mfpLastInstallationDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpLastInstallationDateTime.setStatus("current")


class _MfpRollbackAvailable_Type(Integer32):
    """Custom type mfpRollbackAvailable based on Integer32"""
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


_MfpRollbackAvailable_Type.__name__ = "Integer32"
_MfpRollbackAvailable_Object = MibScalar
mfpRollbackAvailable = _MfpRollbackAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 175),
    _MfpRollbackAvailable_Type()
)
mfpRollbackAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfpRollbackAvailable.setStatus("current")
_MfpRepositoryGroup_ObjectIdentity = ObjectIdentity
mfpRepositoryGroup = _MfpRepositoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400)
)
_MfpTransferGroup_ObjectIdentity = ObjectIdentity
mfpTransferGroup = _MfpTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200)
)


class _MfpTransferUsername_Type(OctetString):
    """Custom type mfpTransferUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MfpTransferUsername_Type.__name__ = "OctetString"
_MfpTransferUsername_Object = MibScalar
mfpTransferUsername = _MfpTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200, 200),
    _MfpTransferUsername_Type()
)
mfpTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpTransferUsername.setStatus("current")


class _MfpTransferPassword_Type(OctetString):
    """Custom type mfpTransferPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MfpTransferPassword_Type.__name__ = "OctetString"
_MfpTransferPassword_Object = MibScalar
mfpTransferPassword = _MfpTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200, 300),
    _MfpTransferPassword_Type()
)
mfpTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpTransferPassword.setStatus("current")


class _MfpTransferCertificateValidation_Type(Integer32):
    """Custom type mfpTransferCertificateValidation based on Integer32"""
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


_MfpTransferCertificateValidation_Type.__name__ = "Integer32"
_MfpTransferCertificateValidation_Object = MibScalar
mfpTransferCertificateValidation = _MfpTransferCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200, 500),
    _MfpTransferCertificateValidation_Type()
)
mfpTransferCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpTransferCertificateValidation.setStatus("current")


class _MfpTransferCertificateTrustLevel_Type(Integer32):
    """Custom type mfpTransferCertificateTrustLevel based on Integer32"""
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


_MfpTransferCertificateTrustLevel_Type.__name__ = "Integer32"
_MfpTransferCertificateTrustLevel_Object = MibScalar
mfpTransferCertificateTrustLevel = _MfpTransferCertificateTrustLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200, 600),
    _MfpTransferCertificateTrustLevel_Type()
)
mfpTransferCertificateTrustLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpTransferCertificateTrustLevel.setStatus("current")


class _MfpTransferCipherSuite_Type(Integer32):
    """Custom type mfpTransferCipherSuite based on Integer32"""
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


_MfpTransferCipherSuite_Type.__name__ = "Integer32"
_MfpTransferCipherSuite_Object = MibScalar
mfpTransferCipherSuite = _MfpTransferCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200, 700),
    _MfpTransferCipherSuite_Type()
)
mfpTransferCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpTransferCipherSuite.setStatus("current")


class _MfpTransferTlsVersion_Type(Integer32):
    """Custom type mfpTransferTlsVersion based on Integer32"""
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


_MfpTransferTlsVersion_Type.__name__ = "Integer32"
_MfpTransferTlsVersion_Object = MibScalar
mfpTransferTlsVersion = _MfpTransferTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 400, 200, 800),
    _MfpTransferTlsVersion_Type()
)
mfpTransferTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpTransferTlsVersion.setStatus("current")


class _MfpUrl_Type(OctetString):
    """Custom type mfpUrl based on OctetString"""
    defaultValue = OctetString("")


_MfpUrl_Type.__name__ = "OctetString"
_MfpUrl_Object = MibScalar
mfpUrl = _MfpUrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 450),
    _MfpUrl_Type()
)
mfpUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfpUrl.setStatus("current")


class _AutomaticRestartEnable_Type(MxEnableState):
    """Custom type automaticRestartEnable based on MxEnableState"""
    defaultValue = 0


_AutomaticRestartEnable_Type.__name__ = "MxEnableState"
_AutomaticRestartEnable_Object = MibScalar
automaticRestartEnable = _AutomaticRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 500),
    _AutomaticRestartEnable_Type()
)
automaticRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automaticRestartEnable.setStatus("current")


class _AutomaticRestartGraceDelay_Type(Unsigned32):
    """Custom type automaticRestartGraceDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_AutomaticRestartGraceDelay_Type.__name__ = "Unsigned32"
_AutomaticRestartGraceDelay_Object = MibScalar
automaticRestartGraceDelay = _AutomaticRestartGraceDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 600),
    _AutomaticRestartGraceDelay_Type()
)
automaticRestartGraceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automaticRestartGraceDelay.setStatus("current")


class _DefaultSettingsOnInstall_Type(MxEnableState):
    """Custom type defaultSettingsOnInstall based on MxEnableState"""
    defaultValue = 0


_DefaultSettingsOnInstall_Type.__name__ = "MxEnableState"
_DefaultSettingsOnInstall_Object = MibScalar
defaultSettingsOnInstall = _DefaultSettingsOnInstall_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 700),
    _DefaultSettingsOnInstall_Type()
)
defaultSettingsOnInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSettingsOnInstall.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1300, 1, 60020, 100),
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
    "MX-FPU-MIB",
    **{"fpuMIB": fpuMIB,
       "fpuMIBObjects": fpuMIBObjects,
       "mfpInstalledInfoTable": mfpInstalledInfoTable,
       "mfpInstalledInfoEntry": mfpInstalledInfoEntry,
       "mfpInstalledInfoIndex": mfpInstalledInfoIndex,
       "mfpInstalledInfoMfpName": mfpInstalledInfoMfpName,
       "mfpInstalledInfoMfpVersion": mfpInstalledInfoMfpVersion,
       "mfpInstalledInfoMfpBank": mfpInstalledInfoMfpBank,
       "mfpInstalledInfoMfpProfileName": mfpInstalledInfoMfpProfileName,
       "status": status,
       "mfpLastInstallationResult": mfpLastInstallationResult,
       "mfpLastInstallationDateTime": mfpLastInstallationDateTime,
       "mfpRollbackAvailable": mfpRollbackAvailable,
       "mfpRepositoryGroup": mfpRepositoryGroup,
       "mfpTransferGroup": mfpTransferGroup,
       "mfpTransferUsername": mfpTransferUsername,
       "mfpTransferPassword": mfpTransferPassword,
       "mfpTransferCertificateValidation": mfpTransferCertificateValidation,
       "mfpTransferCertificateTrustLevel": mfpTransferCertificateTrustLevel,
       "mfpTransferCipherSuite": mfpTransferCipherSuite,
       "mfpTransferTlsVersion": mfpTransferTlsVersion,
       "mfpUrl": mfpUrl,
       "automaticRestartEnable": automaticRestartEnable,
       "automaticRestartGraceDelay": automaticRestartGraceDelay,
       "defaultSettingsOnInstall": defaultSettingsOnInstall,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
