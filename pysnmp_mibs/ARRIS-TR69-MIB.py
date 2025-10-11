# SNMP MIB module (ARRIS-TR69-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-TR69-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:26 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrisTR69Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7)
)
if mibBuilder.loadTexts:
    arrisTR69Mib.setRevisions(
        ("1915-07-07 00:00",
         "1915-02-12 00:00",
         "1913-11-04 00:00",
         "1913-04-30 00:00",
         "1913-02-05 00:00",
         "1913-04-11 00:00",
         "1913-03-04 00:00",
         "1912-08-01 00:00",
         "1912-01-19 00:00",
         "1911-07-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisTR69MibObjects_ObjectIdentity = ObjectIdentity
arrisTR69MibObjects = _ArrisTR69MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1)
)
_ArrisTR69Base_ObjectIdentity = ObjectIdentity
arrisTR69Base = _ArrisTR69Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1)
)


class _ArrisTR69EnableCWMP_Type(Integer32):
    """Custom type arrisTR69EnableCWMP based on Integer32"""
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


_ArrisTR69EnableCWMP_Type.__name__ = "Integer32"
_ArrisTR69EnableCWMP_Object = MibScalar
arrisTR69EnableCWMP = _ArrisTR69EnableCWMP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 1),
    _ArrisTR69EnableCWMP_Type()
)
arrisTR69EnableCWMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69EnableCWMP.setStatus("current")


class _ArrisTR69AcsUrl_Type(OctetString):
    """Custom type arrisTR69AcsUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69AcsUrl_Type.__name__ = "OctetString"
_ArrisTR69AcsUrl_Object = MibScalar
arrisTR69AcsUrl = _ArrisTR69AcsUrl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 2),
    _ArrisTR69AcsUrl_Type()
)
arrisTR69AcsUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsUrl.setStatus("current")


class _ArrisTR69AcsUserName_Type(OctetString):
    """Custom type arrisTR69AcsUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69AcsUserName_Type.__name__ = "OctetString"
_ArrisTR69AcsUserName_Object = MibScalar
arrisTR69AcsUserName = _ArrisTR69AcsUserName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 3),
    _ArrisTR69AcsUserName_Type()
)
arrisTR69AcsUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsUserName.setStatus("current")


class _ArrisTR69AcsPassword_Type(OctetString):
    """Custom type arrisTR69AcsPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69AcsPassword_Type.__name__ = "OctetString"
_ArrisTR69AcsPassword_Object = MibScalar
arrisTR69AcsPassword = _ArrisTR69AcsPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 4),
    _ArrisTR69AcsPassword_Type()
)
arrisTR69AcsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsPassword.setStatus("current")


class _ArrisTR69PeriodicInformEnable_Type(Integer32):
    """Custom type arrisTR69PeriodicInformEnable based on Integer32"""
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


_ArrisTR69PeriodicInformEnable_Type.__name__ = "Integer32"
_ArrisTR69PeriodicInformEnable_Object = MibScalar
arrisTR69PeriodicInformEnable = _ArrisTR69PeriodicInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 5),
    _ArrisTR69PeriodicInformEnable_Type()
)
arrisTR69PeriodicInformEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69PeriodicInformEnable.setStatus("current")
_ArrisTR69PeriodicInformInterval_Type = Unsigned32
_ArrisTR69PeriodicInformInterval_Object = MibScalar
arrisTR69PeriodicInformInterval = _ArrisTR69PeriodicInformInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 6),
    _ArrisTR69PeriodicInformInterval_Type()
)
arrisTR69PeriodicInformInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69PeriodicInformInterval.setStatus("current")


class _ArrisTR69PeriodicInformTime_Type(DisplayString):
    """Custom type arrisTR69PeriodicInformTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ArrisTR69PeriodicInformTime_Type.__name__ = "DisplayString"
_ArrisTR69PeriodicInformTime_Object = MibScalar
arrisTR69PeriodicInformTime = _ArrisTR69PeriodicInformTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 7),
    _ArrisTR69PeriodicInformTime_Type()
)
arrisTR69PeriodicInformTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69PeriodicInformTime.setStatus("current")


class _ArrisTR69ParameterKey_Type(OctetString):
    """Custom type arrisTR69ParameterKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrisTR69ParameterKey_Type.__name__ = "OctetString"
_ArrisTR69ParameterKey_Object = MibScalar
arrisTR69ParameterKey = _ArrisTR69ParameterKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 8),
    _ArrisTR69ParameterKey_Type()
)
arrisTR69ParameterKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ParameterKey.setStatus("current")


class _ArrisTR69ConnectionRequestUrl_Type(OctetString):
    """Custom type arrisTR69ConnectionRequestUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69ConnectionRequestUrl_Type.__name__ = "OctetString"
_ArrisTR69ConnectionRequestUrl_Object = MibScalar
arrisTR69ConnectionRequestUrl = _ArrisTR69ConnectionRequestUrl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 9),
    _ArrisTR69ConnectionRequestUrl_Type()
)
arrisTR69ConnectionRequestUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ConnectionRequestUrl.setStatus("current")


class _ArrisTR69ConnectionRequestUserName_Type(OctetString):
    """Custom type arrisTR69ConnectionRequestUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69ConnectionRequestUserName_Type.__name__ = "OctetString"
_ArrisTR69ConnectionRequestUserName_Object = MibScalar
arrisTR69ConnectionRequestUserName = _ArrisTR69ConnectionRequestUserName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 10),
    _ArrisTR69ConnectionRequestUserName_Type()
)
arrisTR69ConnectionRequestUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ConnectionRequestUserName.setStatus("current")


class _ArrisTR69ConnectionRequestPassword_Type(OctetString):
    """Custom type arrisTR69ConnectionRequestPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69ConnectionRequestPassword_Type.__name__ = "OctetString"
_ArrisTR69ConnectionRequestPassword_Object = MibScalar
arrisTR69ConnectionRequestPassword = _ArrisTR69ConnectionRequestPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 11),
    _ArrisTR69ConnectionRequestPassword_Type()
)
arrisTR69ConnectionRequestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ConnectionRequestPassword.setStatus("current")


class _ArrisTR69TransportInterface_Type(Integer32):
    """Custom type arrisTR69TransportInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gwInterface", 1),
          ("cmInterface", 2))
    )


_ArrisTR69TransportInterface_Type.__name__ = "Integer32"
_ArrisTR69TransportInterface_Object = MibScalar
arrisTR69TransportInterface = _ArrisTR69TransportInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 12),
    _ArrisTR69TransportInterface_Type()
)
arrisTR69TransportInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69TransportInterface.setStatus("current")
_ArrisTR69CwmpPort_Type = Unsigned32
_ArrisTR69CwmpPort_Object = MibScalar
arrisTR69CwmpPort = _ArrisTR69CwmpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 13),
    _ArrisTR69CwmpPort_Type()
)
arrisTR69CwmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69CwmpPort.setStatus("current")


class _ArrisTR69NameSpacePriOverride_Type(Integer32):
    """Custom type arrisTR69NameSpacePriOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("cwmp10", 2),
          ("cwmp11", 3),
          ("cwmp12", 4),
          ("cwmp13", 5))
    )


_ArrisTR69NameSpacePriOverride_Type.__name__ = "Integer32"
_ArrisTR69NameSpacePriOverride_Object = MibScalar
arrisTR69NameSpacePriOverride = _ArrisTR69NameSpacePriOverride_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 14),
    _ArrisTR69NameSpacePriOverride_Type()
)
arrisTR69NameSpacePriOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69NameSpacePriOverride.setStatus("current")


class _ArrisTR69NameSpaceSecOverride_Type(Integer32):
    """Custom type arrisTR69NameSpaceSecOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("cwmp10", 2),
          ("cwmp11", 3),
          ("cwmp12", 4),
          ("cwmp13", 5))
    )


_ArrisTR69NameSpaceSecOverride_Type.__name__ = "Integer32"
_ArrisTR69NameSpaceSecOverride_Object = MibScalar
arrisTR69NameSpaceSecOverride = _ArrisTR69NameSpaceSecOverride_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 15),
    _ArrisTR69NameSpaceSecOverride_Type()
)
arrisTR69NameSpaceSecOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69NameSpaceSecOverride.setStatus("current")


class _ArrisTR69DataModelSelect_Type(Integer32):
    """Custom type arrisTR69DataModelSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tr098", 0),
          ("tr181", 1))
    )


_ArrisTR69DataModelSelect_Type.__name__ = "Integer32"
_ArrisTR69DataModelSelect_Object = MibScalar
arrisTR69DataModelSelect = _ArrisTR69DataModelSelect_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 16),
    _ArrisTR69DataModelSelect_Type()
)
arrisTR69DataModelSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69DataModelSelect.setStatus("current")
_ArrisTR69RetryMinimumWaitInterval_Type = Unsigned32
_ArrisTR69RetryMinimumWaitInterval_Object = MibScalar
arrisTR69RetryMinimumWaitInterval = _ArrisTR69RetryMinimumWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 17),
    _ArrisTR69RetryMinimumWaitInterval_Type()
)
arrisTR69RetryMinimumWaitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69RetryMinimumWaitInterval.setStatus("current")
_ArrisTR69RetryIntervalMultiplier_Type = Unsigned32
_ArrisTR69RetryIntervalMultiplier_Object = MibScalar
arrisTR69RetryIntervalMultiplier = _ArrisTR69RetryIntervalMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 18),
    _ArrisTR69RetryIntervalMultiplier_Type()
)
arrisTR69RetryIntervalMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69RetryIntervalMultiplier.setStatus("current")


class _ArrisTR69ConnectRequestRealm_Type(DisplayString):
    """Custom type arrisTR69ConnectRequestRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisTR69ConnectRequestRealm_Type.__name__ = "DisplayString"
_ArrisTR69ConnectRequestRealm_Object = MibScalar
arrisTR69ConnectRequestRealm = _ArrisTR69ConnectRequestRealm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 19),
    _ArrisTR69ConnectRequestRealm_Type()
)
arrisTR69ConnectRequestRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ConnectRequestRealm.setStatus("current")


class _ArrisTR69AcsPwdAlgorithm_Type(Integer32):
    """Custom type arrisTR69AcsPwdAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmac-sha1", 1),
          ("hmac-sha256", 2))
    )


_ArrisTR69AcsPwdAlgorithm_Type.__name__ = "Integer32"
_ArrisTR69AcsPwdAlgorithm_Object = MibScalar
arrisTR69AcsPwdAlgorithm = _ArrisTR69AcsPwdAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 20),
    _ArrisTR69AcsPwdAlgorithm_Type()
)
arrisTR69AcsPwdAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsPwdAlgorithm.setStatus("current")


class _ArrisTR69AcsPwdAlgorithmText_Type(DisplayString):
    """Custom type arrisTR69AcsPwdAlgorithmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisTR69AcsPwdAlgorithmText_Type.__name__ = "DisplayString"
_ArrisTR69AcsPwdAlgorithmText_Object = MibScalar
arrisTR69AcsPwdAlgorithmText = _ArrisTR69AcsPwdAlgorithmText_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 21),
    _ArrisTR69AcsPwdAlgorithmText_Type()
)
arrisTR69AcsPwdAlgorithmText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsPwdAlgorithmText.setStatus("current")


class _ArrisTR69AcsPwdAlgorithmKey_Type(DisplayString):
    """Custom type arrisTR69AcsPwdAlgorithmKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisTR69AcsPwdAlgorithmKey_Type.__name__ = "DisplayString"
_ArrisTR69AcsPwdAlgorithmKey_Object = MibScalar
arrisTR69AcsPwdAlgorithmKey = _ArrisTR69AcsPwdAlgorithmKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 22),
    _ArrisTR69AcsPwdAlgorithmKey_Type()
)
arrisTR69AcsPwdAlgorithmKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsPwdAlgorithmKey.setStatus("current")
_ArrisTR69TransportIPVersion_Type = InetVersion
_ArrisTR69TransportIPVersion_Object = MibScalar
arrisTR69TransportIPVersion = _ArrisTR69TransportIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 23),
    _ArrisTR69TransportIPVersion_Type()
)
arrisTR69TransportIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69TransportIPVersion.setStatus("current")


class _ArrisTR69ProvisioningCode_Type(OctetString):
    """Custom type arrisTR69ProvisioningCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR69ProvisioningCode_Type.__name__ = "OctetString"
_ArrisTR69ProvisioningCode_Object = MibScalar
arrisTR69ProvisioningCode = _ArrisTR69ProvisioningCode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 24),
    _ArrisTR69ProvisioningCode_Type()
)
arrisTR69ProvisioningCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ProvisioningCode.setStatus("current")
_ArrisTR69DefaultActiveNotificationThrottle_Type = Unsigned32
_ArrisTR69DefaultActiveNotificationThrottle_Object = MibScalar
arrisTR69DefaultActiveNotificationThrottle = _ArrisTR69DefaultActiveNotificationThrottle_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 25),
    _ArrisTR69DefaultActiveNotificationThrottle_Type()
)
arrisTR69DefaultActiveNotificationThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69DefaultActiveNotificationThrottle.setStatus("current")


class _ArrisTR69DataModelSelectIgnoreNonPuma5_Type(Integer32):
    """Custom type arrisTR69DataModelSelectIgnoreNonPuma5 based on Integer32"""
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


_ArrisTR69DataModelSelectIgnoreNonPuma5_Type.__name__ = "Integer32"
_ArrisTR69DataModelSelectIgnoreNonPuma5_Object = MibScalar
arrisTR69DataModelSelectIgnoreNonPuma5 = _ArrisTR69DataModelSelectIgnoreNonPuma5_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 26),
    _ArrisTR69DataModelSelectIgnoreNonPuma5_Type()
)
arrisTR69DataModelSelectIgnoreNonPuma5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69DataModelSelectIgnoreNonPuma5.setStatus("current")


class _ArrisTR69AcsDiscoveryDhcpOption_Type(Integer32):
    """Custom type arrisTR69AcsDiscoveryDhcpOption based on Integer32"""
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
        *(("none", 0),
          ("option60", 1),
          ("option124", 2))
    )


_ArrisTR69AcsDiscoveryDhcpOption_Type.__name__ = "Integer32"
_ArrisTR69AcsDiscoveryDhcpOption_Object = MibScalar
arrisTR69AcsDiscoveryDhcpOption = _ArrisTR69AcsDiscoveryDhcpOption_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 1, 27),
    _ArrisTR69AcsDiscoveryDhcpOption_Type()
)
arrisTR69AcsDiscoveryDhcpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69AcsDiscoveryDhcpOption.setStatus("current")
_ArrisTR69Setup_ObjectIdentity = ObjectIdentity
arrisTR69Setup = _ArrisTR69Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 2)
)


class _ArrisTR69PersistEnable_Type(Integer32):
    """Custom type arrisTR69PersistEnable based on Integer32"""
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


_ArrisTR69PersistEnable_Type.__name__ = "Integer32"
_ArrisTR69PersistEnable_Object = MibScalar
arrisTR69PersistEnable = _ArrisTR69PersistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 2, 1),
    _ArrisTR69PersistEnable_Type()
)
arrisTR69PersistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69PersistEnable.setStatus("current")
_ArrisTR69Authentication_ObjectIdentity = ObjectIdentity
arrisTR69Authentication = _ArrisTR69Authentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3)
)


class _ArrisTR69ValidateManagementServerCertificate_Type(Integer32):
    """Custom type arrisTR69ValidateManagementServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ArrisTR69ValidateManagementServerCertificate_Type.__name__ = "Integer32"
_ArrisTR69ValidateManagementServerCertificate_Object = MibScalar
arrisTR69ValidateManagementServerCertificate = _ArrisTR69ValidateManagementServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 1),
    _ArrisTR69ValidateManagementServerCertificate_Type()
)
arrisTR69ValidateManagementServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ValidateManagementServerCertificate.setStatus("current")


class _ArrisTR69ValidateDownloadServerCertificate_Type(Integer32):
    """Custom type arrisTR69ValidateDownloadServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ArrisTR69ValidateDownloadServerCertificate_Type.__name__ = "Integer32"
_ArrisTR69ValidateDownloadServerCertificate_Object = MibScalar
arrisTR69ValidateDownloadServerCertificate = _ArrisTR69ValidateDownloadServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 2),
    _ArrisTR69ValidateDownloadServerCertificate_Type()
)
arrisTR69ValidateDownloadServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69ValidateDownloadServerCertificate.setStatus("current")
_ArrisTR69RootCertificateNumberOfEntries_Type = Unsigned32
_ArrisTR69RootCertificateNumberOfEntries_Object = MibScalar
arrisTR69RootCertificateNumberOfEntries = _ArrisTR69RootCertificateNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 3),
    _ArrisTR69RootCertificateNumberOfEntries_Type()
)
arrisTR69RootCertificateNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR69RootCertificateNumberOfEntries.setStatus("current")
_ArrisTR69RootCertificateTable_Object = MibTable
arrisTR69RootCertificateTable = _ArrisTR69RootCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4)
)
if mibBuilder.loadTexts:
    arrisTR69RootCertificateTable.setStatus("current")
_ArrisTR69RootCertificateEntry_Object = MibTableRow
arrisTR69RootCertificateEntry = _ArrisTR69RootCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1)
)
arrisTR69RootCertificateEntry.setIndexNames(
    (0, "ARRIS-TR69-MIB", "arrisTR69RootCertIndex"),
)
if mibBuilder.loadTexts:
    arrisTR69RootCertificateEntry.setStatus("current")
_ArrisTR69RootCertIndex_Type = Unsigned32
_ArrisTR69RootCertIndex_Object = MibTableColumn
arrisTR69RootCertIndex = _ArrisTR69RootCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 1),
    _ArrisTR69RootCertIndex_Type()
)
arrisTR69RootCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisTR69RootCertIndex.setStatus("current")


class _ArrisTR69RootCertEnabled_Type(Integer32):
    """Custom type arrisTR69RootCertEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ArrisTR69RootCertEnabled_Type.__name__ = "Integer32"
_ArrisTR69RootCertEnabled_Object = MibTableColumn
arrisTR69RootCertEnabled = _ArrisTR69RootCertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 2),
    _ArrisTR69RootCertEnabled_Type()
)
arrisTR69RootCertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69RootCertEnabled.setStatus("current")


class _ArrisTR69RootCertCertificate_Type(OctetString):
    """Custom type arrisTR69RootCertCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_ArrisTR69RootCertCertificate_Type.__name__ = "OctetString"
_ArrisTR69RootCertCertificate_Object = MibTableColumn
arrisTR69RootCertCertificate = _ArrisTR69RootCertCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 3),
    _ArrisTR69RootCertCertificate_Type()
)
arrisTR69RootCertCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69RootCertCertificate.setStatus("current")
_ArrisTR69RootCertLastModif_Type = TimeStamp
_ArrisTR69RootCertLastModif_Object = MibTableColumn
arrisTR69RootCertLastModif = _ArrisTR69RootCertLastModif_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 4),
    _ArrisTR69RootCertLastModif_Type()
)
arrisTR69RootCertLastModif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertLastModif.setStatus("current")


class _ArrisTR69RootCertSerialNumber_Type(DisplayString):
    """Custom type arrisTR69RootCertSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisTR69RootCertSerialNumber_Type.__name__ = "DisplayString"
_ArrisTR69RootCertSerialNumber_Object = MibTableColumn
arrisTR69RootCertSerialNumber = _ArrisTR69RootCertSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 5),
    _ArrisTR69RootCertSerialNumber_Type()
)
arrisTR69RootCertSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertSerialNumber.setStatus("current")


class _ArrisTR69RootCertIssuer_Type(OctetString):
    """Custom type arrisTR69RootCertIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ArrisTR69RootCertIssuer_Type.__name__ = "OctetString"
_ArrisTR69RootCertIssuer_Object = MibTableColumn
arrisTR69RootCertIssuer = _ArrisTR69RootCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 6),
    _ArrisTR69RootCertIssuer_Type()
)
arrisTR69RootCertIssuer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertIssuer.setStatus("current")


class _ArrisTR69RootCertNotBefore_Type(OctetString):
    """Custom type arrisTR69RootCertNotBefore based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ArrisTR69RootCertNotBefore_Type.__name__ = "OctetString"
_ArrisTR69RootCertNotBefore_Object = MibTableColumn
arrisTR69RootCertNotBefore = _ArrisTR69RootCertNotBefore_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 7),
    _ArrisTR69RootCertNotBefore_Type()
)
arrisTR69RootCertNotBefore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertNotBefore.setStatus("current")


class _ArrisTR69RootCertNotAfter_Type(OctetString):
    """Custom type arrisTR69RootCertNotAfter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ArrisTR69RootCertNotAfter_Type.__name__ = "OctetString"
_ArrisTR69RootCertNotAfter_Object = MibTableColumn
arrisTR69RootCertNotAfter = _ArrisTR69RootCertNotAfter_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 8),
    _ArrisTR69RootCertNotAfter_Type()
)
arrisTR69RootCertNotAfter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertNotAfter.setStatus("current")


class _ArrisTR69RootCertSubject_Type(OctetString):
    """Custom type arrisTR69RootCertSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ArrisTR69RootCertSubject_Type.__name__ = "OctetString"
_ArrisTR69RootCertSubject_Object = MibTableColumn
arrisTR69RootCertSubject = _ArrisTR69RootCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 9),
    _ArrisTR69RootCertSubject_Type()
)
arrisTR69RootCertSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertSubject.setStatus("current")


class _ArrisTR69RootCertSubjectAlt_Type(OctetString):
    """Custom type arrisTR69RootCertSubjectAlt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ArrisTR69RootCertSubjectAlt_Type.__name__ = "OctetString"
_ArrisTR69RootCertSubjectAlt_Object = MibTableColumn
arrisTR69RootCertSubjectAlt = _ArrisTR69RootCertSubjectAlt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 10),
    _ArrisTR69RootCertSubjectAlt_Type()
)
arrisTR69RootCertSubjectAlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertSubjectAlt.setStatus("current")


class _ArrisTR69RootCertSignatureAlgorithm_Type(OctetString):
    """Custom type arrisTR69RootCertSignatureAlgorithm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ArrisTR69RootCertSignatureAlgorithm_Type.__name__ = "OctetString"
_ArrisTR69RootCertSignatureAlgorithm_Object = MibTableColumn
arrisTR69RootCertSignatureAlgorithm = _ArrisTR69RootCertSignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 11),
    _ArrisTR69RootCertSignatureAlgorithm_Type()
)
arrisTR69RootCertSignatureAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisTR69RootCertSignatureAlgorithm.setStatus("current")
_ArrisTR69RootCertObjInstance_Type = Unsigned32
_ArrisTR69RootCertObjInstance_Object = MibTableColumn
arrisTR69RootCertObjInstance = _ArrisTR69RootCertObjInstance_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 1, 3, 4, 1, 12),
    _ArrisTR69RootCertObjInstance_Type()
)
arrisTR69RootCertObjInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisTR69RootCertObjInstance.setStatus("current")
_ArrisTR181MibObjects_ObjectIdentity = ObjectIdentity
arrisTR181MibObjects = _ArrisTR181MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2)
)
_ArrisTR181DeviceInfo_ObjectIdentity = ObjectIdentity
arrisTR181DeviceInfo = _ArrisTR181DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1)
)
_ArrisTR181DeviceInfoFirstUseDate_Type = DateAndTime
_ArrisTR181DeviceInfoFirstUseDate_Object = MibScalar
arrisTR181DeviceInfoFirstUseDate = _ArrisTR181DeviceInfoFirstUseDate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 1),
    _ArrisTR181DeviceInfoFirstUseDate_Type()
)
arrisTR181DeviceInfoFirstUseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoFirstUseDate.setStatus("current")
_ArrisTR181DeviceInfoMemoryStatus_ObjectIdentity = ObjectIdentity
arrisTR181DeviceInfoMemoryStatus = _ArrisTR181DeviceInfoMemoryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 2)
)
_ArrisTR181DeviceInfoMemoryStatusTotal_Type = Unsigned32
_ArrisTR181DeviceInfoMemoryStatusTotal_Object = MibScalar
arrisTR181DeviceInfoMemoryStatusTotal = _ArrisTR181DeviceInfoMemoryStatusTotal_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 2, 1),
    _ArrisTR181DeviceInfoMemoryStatusTotal_Type()
)
arrisTR181DeviceInfoMemoryStatusTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoMemoryStatusTotal.setStatus("current")
_ArrisTR181DeviceInfoMemoryStatusFree_Type = Unsigned32
_ArrisTR181DeviceInfoMemoryStatusFree_Object = MibScalar
arrisTR181DeviceInfoMemoryStatusFree = _ArrisTR181DeviceInfoMemoryStatusFree_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 2, 2),
    _ArrisTR181DeviceInfoMemoryStatusFree_Type()
)
arrisTR181DeviceInfoMemoryStatusFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoMemoryStatusFree.setStatus("current")
_ArrisTR181DeviceInfoProcessStatus_ObjectIdentity = ObjectIdentity
arrisTR181DeviceInfoProcessStatus = _ArrisTR181DeviceInfoProcessStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 3)
)


class _ArrisTR181DeviceInfoProcessStatusCPUUsage_Type(Unsigned32):
    """Custom type arrisTR181DeviceInfoProcessStatusCPUUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArrisTR181DeviceInfoProcessStatusCPUUsage_Type.__name__ = "Unsigned32"
_ArrisTR181DeviceInfoProcessStatusCPUUsage_Object = MibScalar
arrisTR181DeviceInfoProcessStatusCPUUsage = _ArrisTR181DeviceInfoProcessStatusCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 3, 1),
    _ArrisTR181DeviceInfoProcessStatusCPUUsage_Type()
)
arrisTR181DeviceInfoProcessStatusCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusCPUUsage.setStatus("current")
_ArrisTR181DeviceInfoProcessStatusProcess_ObjectIdentity = ObjectIdentity
arrisTR181DeviceInfoProcessStatusProcess = _ArrisTR181DeviceInfoProcessStatusProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4)
)
_ArrisTR181DeviceInfoProcessStatusProcessTable_Object = MibTable
arrisTR181DeviceInfoProcessStatusProcessTable = _ArrisTR181DeviceInfoProcessStatusProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessTable.setStatus("current")
_ArrisTR181DeviceInfoProcessStatusProcessEntry_Object = MibTableRow
arrisTR181DeviceInfoProcessStatusProcessEntry = _ArrisTR181DeviceInfoProcessStatusProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1)
)
arrisTR181DeviceInfoProcessStatusProcessEntry.setIndexNames(
    (0, "ARRIS-TR69-MIB", "arrisTR181DeviceInfoProcessStatusProcessIndex"),
)
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessEntry.setStatus("current")


class _ArrisTR181DeviceInfoProcessStatusProcessIndex_Type(Integer32):
    """Custom type arrisTR181DeviceInfoProcessStatusProcessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_ArrisTR181DeviceInfoProcessStatusProcessIndex_Type.__name__ = "Integer32"
_ArrisTR181DeviceInfoProcessStatusProcessIndex_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessIndex = _ArrisTR181DeviceInfoProcessStatusProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 1),
    _ArrisTR181DeviceInfoProcessStatusProcessIndex_Type()
)
arrisTR181DeviceInfoProcessStatusProcessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessIndex.setStatus("current")
_ArrisTR181DeviceInfoProcessStatusProcessPID_Type = Unsigned32
_ArrisTR181DeviceInfoProcessStatusProcessPID_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessPID = _ArrisTR181DeviceInfoProcessStatusProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 2),
    _ArrisTR181DeviceInfoProcessStatusProcessPID_Type()
)
arrisTR181DeviceInfoProcessStatusProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessPID.setStatus("current")


class _ArrisTR181DeviceInfoProcessStatusProcessCommand_Type(OctetString):
    """Custom type arrisTR181DeviceInfoProcessStatusProcessCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ArrisTR181DeviceInfoProcessStatusProcessCommand_Type.__name__ = "OctetString"
_ArrisTR181DeviceInfoProcessStatusProcessCommand_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessCommand = _ArrisTR181DeviceInfoProcessStatusProcessCommand_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 3),
    _ArrisTR181DeviceInfoProcessStatusProcessCommand_Type()
)
arrisTR181DeviceInfoProcessStatusProcessCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessCommand.setStatus("current")
_ArrisTR181DeviceInfoProcessStatusProcessSize_Type = Unsigned32
_ArrisTR181DeviceInfoProcessStatusProcessSize_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessSize = _ArrisTR181DeviceInfoProcessStatusProcessSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 4),
    _ArrisTR181DeviceInfoProcessStatusProcessSize_Type()
)
arrisTR181DeviceInfoProcessStatusProcessSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessSize.setStatus("current")


class _ArrisTR181DeviceInfoProcessStatusProcessPriority_Type(Unsigned32):
    """Custom type arrisTR181DeviceInfoProcessStatusProcessPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ArrisTR181DeviceInfoProcessStatusProcessPriority_Type.__name__ = "Unsigned32"
_ArrisTR181DeviceInfoProcessStatusProcessPriority_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessPriority = _ArrisTR181DeviceInfoProcessStatusProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 5),
    _ArrisTR181DeviceInfoProcessStatusProcessPriority_Type()
)
arrisTR181DeviceInfoProcessStatusProcessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessPriority.setStatus("current")
_ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Type = Unsigned32
_ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessCPUTime = _ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 6),
    _ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Type()
)
arrisTR181DeviceInfoProcessStatusProcessCPUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessCPUTime.setStatus("current")


class _ArrisTR181DeviceInfoProcessStatusProcessState_Type(OctetString):
    """Custom type arrisTR181DeviceInfoProcessStatusProcessState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrisTR181DeviceInfoProcessStatusProcessState_Type.__name__ = "OctetString"
_ArrisTR181DeviceInfoProcessStatusProcessState_Object = MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessState = _ArrisTR181DeviceInfoProcessStatusProcessState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7, 2, 1, 4, 1, 1, 7),
    _ArrisTR181DeviceInfoProcessStatusProcessState_Type()
)
arrisTR181DeviceInfoProcessStatusProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisTR181DeviceInfoProcessStatusProcessState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-TR69-MIB",
    **{"arrisTR69Mib": arrisTR69Mib,
       "arrisTR69MibObjects": arrisTR69MibObjects,
       "arrisTR69Base": arrisTR69Base,
       "arrisTR69EnableCWMP": arrisTR69EnableCWMP,
       "arrisTR69AcsUrl": arrisTR69AcsUrl,
       "arrisTR69AcsUserName": arrisTR69AcsUserName,
       "arrisTR69AcsPassword": arrisTR69AcsPassword,
       "arrisTR69PeriodicInformEnable": arrisTR69PeriodicInformEnable,
       "arrisTR69PeriodicInformInterval": arrisTR69PeriodicInformInterval,
       "arrisTR69PeriodicInformTime": arrisTR69PeriodicInformTime,
       "arrisTR69ParameterKey": arrisTR69ParameterKey,
       "arrisTR69ConnectionRequestUrl": arrisTR69ConnectionRequestUrl,
       "arrisTR69ConnectionRequestUserName": arrisTR69ConnectionRequestUserName,
       "arrisTR69ConnectionRequestPassword": arrisTR69ConnectionRequestPassword,
       "arrisTR69TransportInterface": arrisTR69TransportInterface,
       "arrisTR69CwmpPort": arrisTR69CwmpPort,
       "arrisTR69NameSpacePriOverride": arrisTR69NameSpacePriOverride,
       "arrisTR69NameSpaceSecOverride": arrisTR69NameSpaceSecOverride,
       "arrisTR69DataModelSelect": arrisTR69DataModelSelect,
       "arrisTR69RetryMinimumWaitInterval": arrisTR69RetryMinimumWaitInterval,
       "arrisTR69RetryIntervalMultiplier": arrisTR69RetryIntervalMultiplier,
       "arrisTR69ConnectRequestRealm": arrisTR69ConnectRequestRealm,
       "arrisTR69AcsPwdAlgorithm": arrisTR69AcsPwdAlgorithm,
       "arrisTR69AcsPwdAlgorithmText": arrisTR69AcsPwdAlgorithmText,
       "arrisTR69AcsPwdAlgorithmKey": arrisTR69AcsPwdAlgorithmKey,
       "arrisTR69TransportIPVersion": arrisTR69TransportIPVersion,
       "arrisTR69ProvisioningCode": arrisTR69ProvisioningCode,
       "arrisTR69DefaultActiveNotificationThrottle": arrisTR69DefaultActiveNotificationThrottle,
       "arrisTR69DataModelSelectIgnoreNonPuma5": arrisTR69DataModelSelectIgnoreNonPuma5,
       "arrisTR69AcsDiscoveryDhcpOption": arrisTR69AcsDiscoveryDhcpOption,
       "arrisTR69Setup": arrisTR69Setup,
       "arrisTR69PersistEnable": arrisTR69PersistEnable,
       "arrisTR69Authentication": arrisTR69Authentication,
       "arrisTR69ValidateManagementServerCertificate": arrisTR69ValidateManagementServerCertificate,
       "arrisTR69ValidateDownloadServerCertificate": arrisTR69ValidateDownloadServerCertificate,
       "arrisTR69RootCertificateNumberOfEntries": arrisTR69RootCertificateNumberOfEntries,
       "arrisTR69RootCertificateTable": arrisTR69RootCertificateTable,
       "arrisTR69RootCertificateEntry": arrisTR69RootCertificateEntry,
       "arrisTR69RootCertIndex": arrisTR69RootCertIndex,
       "arrisTR69RootCertEnabled": arrisTR69RootCertEnabled,
       "arrisTR69RootCertCertificate": arrisTR69RootCertCertificate,
       "arrisTR69RootCertLastModif": arrisTR69RootCertLastModif,
       "arrisTR69RootCertSerialNumber": arrisTR69RootCertSerialNumber,
       "arrisTR69RootCertIssuer": arrisTR69RootCertIssuer,
       "arrisTR69RootCertNotBefore": arrisTR69RootCertNotBefore,
       "arrisTR69RootCertNotAfter": arrisTR69RootCertNotAfter,
       "arrisTR69RootCertSubject": arrisTR69RootCertSubject,
       "arrisTR69RootCertSubjectAlt": arrisTR69RootCertSubjectAlt,
       "arrisTR69RootCertSignatureAlgorithm": arrisTR69RootCertSignatureAlgorithm,
       "arrisTR69RootCertObjInstance": arrisTR69RootCertObjInstance,
       "arrisTR181MibObjects": arrisTR181MibObjects,
       "arrisTR181DeviceInfo": arrisTR181DeviceInfo,
       "arrisTR181DeviceInfoFirstUseDate": arrisTR181DeviceInfoFirstUseDate,
       "arrisTR181DeviceInfoMemoryStatus": arrisTR181DeviceInfoMemoryStatus,
       "arrisTR181DeviceInfoMemoryStatusTotal": arrisTR181DeviceInfoMemoryStatusTotal,
       "arrisTR181DeviceInfoMemoryStatusFree": arrisTR181DeviceInfoMemoryStatusFree,
       "arrisTR181DeviceInfoProcessStatus": arrisTR181DeviceInfoProcessStatus,
       "arrisTR181DeviceInfoProcessStatusCPUUsage": arrisTR181DeviceInfoProcessStatusCPUUsage,
       "arrisTR181DeviceInfoProcessStatusProcess": arrisTR181DeviceInfoProcessStatusProcess,
       "arrisTR181DeviceInfoProcessStatusProcessTable": arrisTR181DeviceInfoProcessStatusProcessTable,
       "arrisTR181DeviceInfoProcessStatusProcessEntry": arrisTR181DeviceInfoProcessStatusProcessEntry,
       "arrisTR181DeviceInfoProcessStatusProcessIndex": arrisTR181DeviceInfoProcessStatusProcessIndex,
       "arrisTR181DeviceInfoProcessStatusProcessPID": arrisTR181DeviceInfoProcessStatusProcessPID,
       "arrisTR181DeviceInfoProcessStatusProcessCommand": arrisTR181DeviceInfoProcessStatusProcessCommand,
       "arrisTR181DeviceInfoProcessStatusProcessSize": arrisTR181DeviceInfoProcessStatusProcessSize,
       "arrisTR181DeviceInfoProcessStatusProcessPriority": arrisTR181DeviceInfoProcessStatusProcessPriority,
       "arrisTR181DeviceInfoProcessStatusProcessCPUTime": arrisTR181DeviceInfoProcessStatusProcessCPUTime,
       "arrisTR181DeviceInfoProcessStatusProcessState": arrisTR181DeviceInfoProcessStatusProcessState}
)
