# SNMP MIB module (MX-CORNET-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CORNET-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:50 2025
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

(corNet,
 ipAddressConfigCorNet,
 ipAddressConfigCorNetStatic,
 ipAddressStatusCorNet) = mibBuilder.importSymbols(
    "MX-CORNET-MIB",
    "corNet",
    "ipAddressConfigCorNet",
    "ipAddressConfigCorNetStatic",
    "ipAddressStatusCorNet")

(ipAddressConfig,
 ipAddressStatus,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixMgmt")

(MxAdvancedIpPort,
 MxEnableState,
 MxIpHostName,
 MxIpPort) = mibBuilder.importSymbols(
    "MX-TC",
    "MxAdvancedIpPort",
    "MxEnableState",
    "MxIpHostName",
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

corNetSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1)
)
if mibBuilder.loadTexts:
    corNetSystemMIB.setRevisions(
        ("2006-07-17 00:00",
         "2005-12-02 00:00",
         "2005-07-07 00:00",
         "2005-06-27 00:00",
         "2005-06-10 00:00",
         "2005-05-16 00:00",
         "2005-05-06 00:00",
         "2004-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusCorNetPbxIfTable_Object = MibTable
ipAddressStatusCorNetPbxIfTable = _IpAddressStatusCorNetPbxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 130, 10)
)
if mibBuilder.loadTexts:
    ipAddressStatusCorNetPbxIfTable.setStatus("current")
_IpAddressStatusCorNetPbxIfEntry_Object = MibTableRow
ipAddressStatusCorNetPbxIfEntry = _IpAddressStatusCorNetPbxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 130, 10, 1)
)
ipAddressStatusCorNetPbxIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ipAddressStatusCorNetPbxIfEntry.setStatus("current")


class _IpAddressStatusCorNetPbxHost_Type(MxIpHostName):
    """Custom type ipAddressStatusCorNetPbxHost based on MxIpHostName"""
    defaultValue = OctetString("")


_IpAddressStatusCorNetPbxHost_Type.__name__ = "MxIpHostName"
_IpAddressStatusCorNetPbxHost_Object = MibTableColumn
ipAddressStatusCorNetPbxHost = _IpAddressStatusCorNetPbxHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 130, 10, 1, 10),
    _IpAddressStatusCorNetPbxHost_Type()
)
ipAddressStatusCorNetPbxHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatusCorNetPbxHost.setStatus("current")


class _IpAddressStatusCorNetPbxPort_Type(MxIpPort):
    """Custom type ipAddressStatusCorNetPbxPort based on MxIpPort"""
    defaultValue = 4060


_IpAddressStatusCorNetPbxPort_Type.__name__ = "MxIpPort"
_IpAddressStatusCorNetPbxPort_Object = MibTableColumn
ipAddressStatusCorNetPbxPort = _IpAddressStatusCorNetPbxPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 130, 10, 1, 20),
    _IpAddressStatusCorNetPbxPort_Type()
)
ipAddressStatusCorNetPbxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatusCorNetPbxPort.setStatus("current")


class _IpAddressStatusCorNetFaultManagementHost_Type(MxIpHostName):
    """Custom type ipAddressStatusCorNetFaultManagementHost based on MxIpHostName"""
    defaultValue = OctetString("")


_IpAddressStatusCorNetFaultManagementHost_Type.__name__ = "MxIpHostName"
_IpAddressStatusCorNetFaultManagementHost_Object = MibScalar
ipAddressStatusCorNetFaultManagementHost = _IpAddressStatusCorNetFaultManagementHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 130, 20),
    _IpAddressStatusCorNetFaultManagementHost_Type()
)
ipAddressStatusCorNetFaultManagementHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatusCorNetFaultManagementHost.setStatus("current")


class _IpAddressStatusCorNetFaultManagementTrapPort_Type(MxIpPort):
    """Custom type ipAddressStatusCorNetFaultManagementTrapPort based on MxIpPort"""
    defaultValue = 162


_IpAddressStatusCorNetFaultManagementTrapPort_Type.__name__ = "MxIpPort"
_IpAddressStatusCorNetFaultManagementTrapPort_Object = MibScalar
ipAddressStatusCorNetFaultManagementTrapPort = _IpAddressStatusCorNetFaultManagementTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 130, 30),
    _IpAddressStatusCorNetFaultManagementTrapPort_Type()
)
ipAddressStatusCorNetFaultManagementTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatusCorNetFaultManagementTrapPort.setStatus("current")
_CorNetFaultManagementStatus_ObjectIdentity = ObjectIdentity
corNetFaultManagementStatus = _CorNetFaultManagementStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 80)
)


class _CorNetFaultManagementPacketsLostStatus_Type(Integer32):
    """Custom type corNetFaultManagementPacketsLostStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_CorNetFaultManagementPacketsLostStatus_Type.__name__ = "Integer32"
_CorNetFaultManagementPacketsLostStatus_Object = MibScalar
corNetFaultManagementPacketsLostStatus = _CorNetFaultManagementPacketsLostStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 80, 5),
    _CorNetFaultManagementPacketsLostStatus_Type()
)
corNetFaultManagementPacketsLostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corNetFaultManagementPacketsLostStatus.setStatus("current")


class _CorNetFaultManagementJitterBufferStatus_Type(Integer32):
    """Custom type corNetFaultManagementJitterBufferStatus based on Integer32"""
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
        *(("normal", 0),
          ("overrun", 1),
          ("underrun", 2))
    )


_CorNetFaultManagementJitterBufferStatus_Type.__name__ = "Integer32"
_CorNetFaultManagementJitterBufferStatus_Object = MibScalar
corNetFaultManagementJitterBufferStatus = _CorNetFaultManagementJitterBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 80, 10),
    _CorNetFaultManagementJitterBufferStatus_Type()
)
corNetFaultManagementJitterBufferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corNetFaultManagementJitterBufferStatus.setStatus("current")
_IpAddressConfigCorNetPbxIfTable_Object = MibTable
ipAddressConfigCorNetPbxIfTable = _IpAddressConfigCorNetPbxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10, 10)
)
if mibBuilder.loadTexts:
    ipAddressConfigCorNetPbxIfTable.setStatus("current")
_IpAddressConfigCorNetPbxIfEntry_Object = MibTableRow
ipAddressConfigCorNetPbxIfEntry = _IpAddressConfigCorNetPbxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10, 10, 1)
)
ipAddressConfigCorNetPbxIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ipAddressConfigCorNetPbxIfEntry.setStatus("current")


class _IpAddressConfigCorNetPbxHost_Type(MxIpHostName):
    """Custom type ipAddressConfigCorNetPbxHost based on MxIpHostName"""
    defaultValue = OctetString("")


_IpAddressConfigCorNetPbxHost_Type.__name__ = "MxIpHostName"
_IpAddressConfigCorNetPbxHost_Object = MibTableColumn
ipAddressConfigCorNetPbxHost = _IpAddressConfigCorNetPbxHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10, 10, 1, 10),
    _IpAddressConfigCorNetPbxHost_Type()
)
ipAddressConfigCorNetPbxHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressConfigCorNetPbxHost.setStatus("current")


class _IpAddressConfigCorNetPbxPort_Type(MxIpPort):
    """Custom type ipAddressConfigCorNetPbxPort based on MxIpPort"""
    defaultValue = 4060


_IpAddressConfigCorNetPbxPort_Type.__name__ = "MxIpPort"
_IpAddressConfigCorNetPbxPort_Object = MibTableColumn
ipAddressConfigCorNetPbxPort = _IpAddressConfigCorNetPbxPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10, 10, 1, 20),
    _IpAddressConfigCorNetPbxPort_Type()
)
ipAddressConfigCorNetPbxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressConfigCorNetPbxPort.setStatus("current")


class _IpAddressConfigCorNetFaultManagementHost_Type(MxIpHostName):
    """Custom type ipAddressConfigCorNetFaultManagementHost based on MxIpHostName"""
    defaultValue = OctetString("")


_IpAddressConfigCorNetFaultManagementHost_Type.__name__ = "MxIpHostName"
_IpAddressConfigCorNetFaultManagementHost_Object = MibScalar
ipAddressConfigCorNetFaultManagementHost = _IpAddressConfigCorNetFaultManagementHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10, 20),
    _IpAddressConfigCorNetFaultManagementHost_Type()
)
ipAddressConfigCorNetFaultManagementHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressConfigCorNetFaultManagementHost.setStatus("current")


class _IpAddressConfigCorNetFaultManagementTrapPort_Type(MxIpPort):
    """Custom type ipAddressConfigCorNetFaultManagementTrapPort based on MxIpPort"""
    defaultValue = 162


_IpAddressConfigCorNetFaultManagementTrapPort_Type.__name__ = "MxIpPort"
_IpAddressConfigCorNetFaultManagementTrapPort_Object = MibScalar
ipAddressConfigCorNetFaultManagementTrapPort = _IpAddressConfigCorNetFaultManagementTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10, 30),
    _IpAddressConfigCorNetFaultManagementTrapPort_Type()
)
ipAddressConfigCorNetFaultManagementTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressConfigCorNetFaultManagementTrapPort.setStatus("current")
_CorNetSystemMIBObjects_ObjectIdentity = ObjectIdentity
corNetSystemMIBObjects = _CorNetSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1)
)
_CorNetSystemRegistration_ObjectIdentity = ObjectIdentity
corNetSystemRegistration = _CorNetSystemRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 10)
)
_CorNetSystemRegistrationIfTable_Object = MibTable
corNetSystemRegistrationIfTable = _CorNetSystemRegistrationIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 10, 10)
)
if mibBuilder.loadTexts:
    corNetSystemRegistrationIfTable.setStatus("current")
_CorNetSystemRegistrationIfEntry_Object = MibTableRow
corNetSystemRegistrationIfEntry = _CorNetSystemRegistrationIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 10, 10, 1)
)
corNetSystemRegistrationIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    corNetSystemRegistrationIfEntry.setStatus("current")


class _CorNetSystemRegSubscriberNumber_Type(OctetString):
    """Custom type corNetSystemRegSubscriberNumber based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CorNetSystemRegSubscriberNumber_Type.__name__ = "OctetString"
_CorNetSystemRegSubscriberNumber_Object = MibTableColumn
corNetSystemRegSubscriberNumber = _CorNetSystemRegSubscriberNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 10, 10, 1, 10),
    _CorNetSystemRegSubscriberNumber_Type()
)
corNetSystemRegSubscriberNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemRegSubscriberNumber.setStatus("current")


class _CorNetSystemRegLocationIdentifierNumber_Type(OctetString):
    """Custom type corNetSystemRegLocationIdentifierNumber based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CorNetSystemRegLocationIdentifierNumber_Type.__name__ = "OctetString"
_CorNetSystemRegLocationIdentifierNumber_Object = MibTableColumn
corNetSystemRegLocationIdentifierNumber = _CorNetSystemRegLocationIdentifierNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 10, 10, 1, 20),
    _CorNetSystemRegLocationIdentifierNumber_Type()
)
corNetSystemRegLocationIdentifierNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemRegLocationIdentifierNumber.setStatus("current")
_CorNetSystemInitialization_ObjectIdentity = ObjectIdentity
corNetSystemInitialization = _CorNetSystemInitialization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 20)
)
_CorNetSystemInitializationIfTable_Object = MibTable
corNetSystemInitializationIfTable = _CorNetSystemInitializationIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 20, 10)
)
if mibBuilder.loadTexts:
    corNetSystemInitializationIfTable.setStatus("current")
_CorNetSystemInitializationIfEntry_Object = MibTableRow
corNetSystemInitializationIfEntry = _CorNetSystemInitializationIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 20, 10, 1)
)
corNetSystemInitializationIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    corNetSystemInitializationIfEntry.setStatus("current")


class _CorNetSystemInitEmergencyNumber_Type(OctetString):
    """Custom type corNetSystemInitEmergencyNumber based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CorNetSystemInitEmergencyNumber_Type.__name__ = "OctetString"
_CorNetSystemInitEmergencyNumber_Object = MibTableColumn
corNetSystemInitEmergencyNumber = _CorNetSystemInitEmergencyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 20, 10, 1, 10),
    _CorNetSystemInitEmergencyNumber_Type()
)
corNetSystemInitEmergencyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemInitEmergencyNumber.setStatus("current")
_CorNetSystemSecurity_ObjectIdentity = ObjectIdentity
corNetSystemSecurity = _CorNetSystemSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 25)
)
_CorNetSystemSecurityIfTable_Object = MibTable
corNetSystemSecurityIfTable = _CorNetSystemSecurityIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 25, 10)
)
if mibBuilder.loadTexts:
    corNetSystemSecurityIfTable.setStatus("current")
_CorNetSystemSecurityIfEntry_Object = MibTableRow
corNetSystemSecurityIfEntry = _CorNetSystemSecurityIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 25, 10, 1)
)
corNetSystemSecurityIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    corNetSystemSecurityIfEntry.setStatus("current")


class _CorNetSystemSecurityPassword_Type(OctetString):
    """Custom type corNetSystemSecurityPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CorNetSystemSecurityPassword_Type.__name__ = "OctetString"
_CorNetSystemSecurityPassword_Object = MibTableColumn
corNetSystemSecurityPassword = _CorNetSystemSecurityPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 25, 10, 1, 10),
    _CorNetSystemSecurityPassword_Type()
)
corNetSystemSecurityPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemSecurityPassword.setStatus("current")


class _CorNetSystemSecurityLevel_Type(Integer32):
    """Custom type corNetSystemSecurityLevel based on Integer32"""
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
          ("reduced", 1),
          ("full", 2))
    )


_CorNetSystemSecurityLevel_Type.__name__ = "Integer32"
_CorNetSystemSecurityLevel_Object = MibTableColumn
corNetSystemSecurityLevel = _CorNetSystemSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 25, 10, 1, 50),
    _CorNetSystemSecurityLevel_Type()
)
corNetSystemSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemSecurityLevel.setStatus("current")
_CorNetSystemFaultManagement_ObjectIdentity = ObjectIdentity
corNetSystemFaultManagement = _CorNetSystemFaultManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30)
)


class _CorNetSystemFaultManagementTrapsEnable_Type(MxEnableState):
    """Custom type corNetSystemFaultManagementTrapsEnable based on MxEnableState"""
    defaultValue = 1


_CorNetSystemFaultManagementTrapsEnable_Type.__name__ = "MxEnableState"
_CorNetSystemFaultManagementTrapsEnable_Object = MibScalar
corNetSystemFaultManagementTrapsEnable = _CorNetSystemFaultManagementTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30, 10),
    _CorNetSystemFaultManagementTrapsEnable_Type()
)
corNetSystemFaultManagementTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemFaultManagementTrapsEnable.setStatus("current")


class _CorNetSystemFaultManagementTrapsComputePeriod_Type(Unsigned32):
    """Custom type corNetSystemFaultManagementTrapsComputePeriod based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CorNetSystemFaultManagementTrapsComputePeriod_Type.__name__ = "Unsigned32"
_CorNetSystemFaultManagementTrapsComputePeriod_Object = MibScalar
corNetSystemFaultManagementTrapsComputePeriod = _CorNetSystemFaultManagementTrapsComputePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30, 20),
    _CorNetSystemFaultManagementTrapsComputePeriod_Type()
)
corNetSystemFaultManagementTrapsComputePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemFaultManagementTrapsComputePeriod.setStatus("current")


class _CorNetSystemFaultManagementTrapsReportDelay_Type(Unsigned32):
    """Custom type corNetSystemFaultManagementTrapsReportDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CorNetSystemFaultManagementTrapsReportDelay_Type.__name__ = "Unsigned32"
_CorNetSystemFaultManagementTrapsReportDelay_Object = MibScalar
corNetSystemFaultManagementTrapsReportDelay = _CorNetSystemFaultManagementTrapsReportDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30, 30),
    _CorNetSystemFaultManagementTrapsReportDelay_Type()
)
corNetSystemFaultManagementTrapsReportDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemFaultManagementTrapsReportDelay.setStatus("current")


class _CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Type(Unsigned32):
    """Custom type corNetSystemFaultManagementTrapsMaximumPacketsLostRatio based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Type.__name__ = "Unsigned32"
_CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Object = MibScalar
corNetSystemFaultManagementTrapsMaximumPacketsLostRatio = _CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30, 40),
    _CorNetSystemFaultManagementTrapsMaximumPacketsLostRatio_Type()
)
corNetSystemFaultManagementTrapsMaximumPacketsLostRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemFaultManagementTrapsMaximumPacketsLostRatio.setStatus("current")


class _CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Type(Unsigned32):
    """Custom type corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Type.__name__ = "Unsigned32"
_CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Object = MibScalar
corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio = _CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30, 50),
    _CorNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio_Type()
)
corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio.setStatus("current")


class _CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Type(Unsigned32):
    """Custom type corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Type.__name__ = "Unsigned32"
_CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Object = MibScalar
corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio = _CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 30, 60),
    _CorNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio_Type()
)
corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio.setStatus("current")
_CorNetSystemData_ObjectIdentity = ObjectIdentity
corNetSystemData = _CorNetSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50)
)
_CorNetSystemDataIfTable_Object = MibTable
corNetSystemDataIfTable = _CorNetSystemDataIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50, 10)
)
if mibBuilder.loadTexts:
    corNetSystemDataIfTable.setStatus("current")
_CorNetSystemDataIfEntry_Object = MibTableRow
corNetSystemDataIfEntry = _CorNetSystemDataIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50, 10, 1)
)
corNetSystemDataIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    corNetSystemDataIfEntry.setStatus("current")


class _CorNetSystemDataRfc2198RedundancyLevel_Type(Unsigned32):
    """Custom type corNetSystemDataRfc2198RedundancyLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CorNetSystemDataRfc2198RedundancyLevel_Type.__name__ = "Unsigned32"
_CorNetSystemDataRfc2198RedundancyLevel_Object = MibTableColumn
corNetSystemDataRfc2198RedundancyLevel = _CorNetSystemDataRfc2198RedundancyLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50, 10, 1, 50),
    _CorNetSystemDataRfc2198RedundancyLevel_Type()
)
corNetSystemDataRfc2198RedundancyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemDataRfc2198RedundancyLevel.setStatus("current")


class _CorNetSystemDataRfc2198DefaultPayloadType_Type(Unsigned32):
    """Custom type corNetSystemDataRfc2198DefaultPayloadType based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_CorNetSystemDataRfc2198DefaultPayloadType_Type.__name__ = "Unsigned32"
_CorNetSystemDataRfc2198DefaultPayloadType_Object = MibTableColumn
corNetSystemDataRfc2198DefaultPayloadType = _CorNetSystemDataRfc2198DefaultPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50, 10, 1, 70),
    _CorNetSystemDataRfc2198DefaultPayloadType_Type()
)
corNetSystemDataRfc2198DefaultPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemDataRfc2198DefaultPayloadType.setStatus("current")


class _CorNetSystemDataRfc2833DefaultPayloadType_Type(Unsigned32):
    """Custom type corNetSystemDataRfc2833DefaultPayloadType based on Unsigned32"""
    defaultValue = 98

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_CorNetSystemDataRfc2833DefaultPayloadType_Type.__name__ = "Unsigned32"
_CorNetSystemDataRfc2833DefaultPayloadType_Object = MibTableColumn
corNetSystemDataRfc2833DefaultPayloadType = _CorNetSystemDataRfc2833DefaultPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50, 10, 1, 90),
    _CorNetSystemDataRfc2833DefaultPayloadType_Type()
)
corNetSystemDataRfc2833DefaultPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemDataRfc2833DefaultPayloadType.setStatus("current")


class _CorNetSystemDataVoiceOnlyModeEnable_Type(MxEnableState):
    """Custom type corNetSystemDataVoiceOnlyModeEnable based on MxEnableState"""
    defaultValue = 0


_CorNetSystemDataVoiceOnlyModeEnable_Type.__name__ = "MxEnableState"
_CorNetSystemDataVoiceOnlyModeEnable_Object = MibTableColumn
corNetSystemDataVoiceOnlyModeEnable = _CorNetSystemDataVoiceOnlyModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 50, 10, 1, 150),
    _CorNetSystemDataVoiceOnlyModeEnable_Type()
)
corNetSystemDataVoiceOnlyModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemDataVoiceOnlyModeEnable.setStatus("current")
_CorNetSystemServices_ObjectIdentity = ObjectIdentity
corNetSystemServices = _CorNetSystemServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100)
)
_CorNetSystemServicesTable_Object = MibTable
corNetSystemServicesTable = _CorNetSystemServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100)
)
if mibBuilder.loadTexts:
    corNetSystemServicesTable.setStatus("current")
_CorNetSystemServicesEntry_Object = MibTableRow
corNetSystemServicesEntry = _CorNetSystemServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1)
)
corNetSystemServicesEntry.setIndexNames(
    (0, "MX-CORNET-SYSTEM-MIB", "corNetSystemServicesIndex"),
)
if mibBuilder.loadTexts:
    corNetSystemServicesEntry.setStatus("current")


class _CorNetSystemServicesIndex_Type(Unsigned32):
    """Custom type corNetSystemServicesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CorNetSystemServicesIndex_Type.__name__ = "Unsigned32"
_CorNetSystemServicesIndex_Object = MibTableColumn
corNetSystemServicesIndex = _CorNetSystemServicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 5),
    _CorNetSystemServicesIndex_Type()
)
corNetSystemServicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    corNetSystemServicesIndex.setStatus("current")


class _CorNetSystemServiceName_Type(OctetString):
    """Custom type corNetSystemServiceName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CorNetSystemServiceName_Type.__name__ = "OctetString"
_CorNetSystemServiceName_Object = MibTableColumn
corNetSystemServiceName = _CorNetSystemServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 10),
    _CorNetSystemServiceName_Type()
)
corNetSystemServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServiceName.setStatus("current")


class _CorNetSystemServiceEnable_Type(MxEnableState):
    """Custom type corNetSystemServiceEnable based on MxEnableState"""
    defaultValue = 0


_CorNetSystemServiceEnable_Type.__name__ = "MxEnableState"
_CorNetSystemServiceEnable_Object = MibTableColumn
corNetSystemServiceEnable = _CorNetSystemServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 15),
    _CorNetSystemServiceEnable_Type()
)
corNetSystemServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServiceEnable.setStatus("current")


class _CorNetSystemServiceKbKeyCode_Type(Unsigned32):
    """Custom type corNetSystemServiceKbKeyCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CorNetSystemServiceKbKeyCode_Type.__name__ = "Unsigned32"
_CorNetSystemServiceKbKeyCode_Object = MibTableColumn
corNetSystemServiceKbKeyCode = _CorNetSystemServiceKbKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 20),
    _CorNetSystemServiceKbKeyCode_Type()
)
corNetSystemServiceKbKeyCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServiceKbKeyCode.setStatus("current")


class _CorNetSystemServiceActivationSequence_Type(OctetString):
    """Custom type corNetSystemServiceActivationSequence based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CorNetSystemServiceActivationSequence_Type.__name__ = "OctetString"
_CorNetSystemServiceActivationSequence_Object = MibTableColumn
corNetSystemServiceActivationSequence = _CorNetSystemServiceActivationSequence_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 25),
    _CorNetSystemServiceActivationSequence_Type()
)
corNetSystemServiceActivationSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServiceActivationSequence.setStatus("current")


class _CorNetSystemService2StageFlag_Type(Integer32):
    """Custom type corNetSystemService2StageFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CorNetSystemService2StageFlag_Type.__name__ = "Integer32"
_CorNetSystemService2StageFlag_Object = MibTableColumn
corNetSystemService2StageFlag = _CorNetSystemService2StageFlag_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 30),
    _CorNetSystemService2StageFlag_Type()
)
corNetSystemService2StageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemService2StageFlag.setStatus("current")


class _CorNetSystemServiceFirstDigitTimer_Type(Unsigned32):
    """Custom type corNetSystemServiceFirstDigitTimer based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_CorNetSystemServiceFirstDigitTimer_Type.__name__ = "Unsigned32"
_CorNetSystemServiceFirstDigitTimer_Object = MibTableColumn
corNetSystemServiceFirstDigitTimer = _CorNetSystemServiceFirstDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 100, 1, 35),
    _CorNetSystemServiceFirstDigitTimer_Type()
)
corNetSystemServiceFirstDigitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServiceFirstDigitTimer.setStatus("current")


class _CorNetSystemCallFeaturesEnable_Type(MxEnableState):
    """Custom type corNetSystemCallFeaturesEnable based on MxEnableState"""
    defaultValue = 0


_CorNetSystemCallFeaturesEnable_Type.__name__ = "MxEnableState"
_CorNetSystemCallFeaturesEnable_Object = MibScalar
corNetSystemCallFeaturesEnable = _CorNetSystemCallFeaturesEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 150),
    _CorNetSystemCallFeaturesEnable_Type()
)
corNetSystemCallFeaturesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemCallFeaturesEnable.setStatus("current")


class _CorNetSystemServices2StageEndingMethod_Type(Integer32):
    """Custom type corNetSystemServices2StageEndingMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("timer", 0),
          ("endCharacter", 1))
    )


_CorNetSystemServices2StageEndingMethod_Type.__name__ = "Integer32"
_CorNetSystemServices2StageEndingMethod_Object = MibScalar
corNetSystemServices2StageEndingMethod = _CorNetSystemServices2StageEndingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 200),
    _CorNetSystemServices2StageEndingMethod_Type()
)
corNetSystemServices2StageEndingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServices2StageEndingMethod.setStatus("current")


class _CorNetSystemServices2StageTimeout_Type(Unsigned32):
    """Custom type corNetSystemServices2StageTimeout based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_CorNetSystemServices2StageTimeout_Type.__name__ = "Unsigned32"
_CorNetSystemServices2StageTimeout_Object = MibScalar
corNetSystemServices2StageTimeout = _CorNetSystemServices2StageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 250),
    _CorNetSystemServices2StageTimeout_Type()
)
corNetSystemServices2StageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServices2StageTimeout.setStatus("current")


class _CorNetSystemServices2StageEndKey_Type(OctetString):
    """Custom type corNetSystemServices2StageEndKey based on OctetString"""
    defaultValue = OctetString("#")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CorNetSystemServices2StageEndKey_Type.__name__ = "OctetString"
_CorNetSystemServices2StageEndKey_Object = MibScalar
corNetSystemServices2StageEndKey = _CorNetSystemServices2StageEndKey_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 300),
    _CorNetSystemServices2StageEndKey_Type()
)
corNetSystemServices2StageEndKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServices2StageEndKey.setStatus("current")


class _CorNetSystemServicesTimeoutInterDigit_Type(Unsigned32):
    """Custom type corNetSystemServicesTimeoutInterDigit based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_CorNetSystemServicesTimeoutInterDigit_Type.__name__ = "Unsigned32"
_CorNetSystemServicesTimeoutInterDigit_Object = MibScalar
corNetSystemServicesTimeoutInterDigit = _CorNetSystemServicesTimeoutInterDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 1, 100, 350),
    _CorNetSystemServicesTimeoutInterDigit_Type()
)
corNetSystemServicesTimeoutInterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetSystemServicesTimeoutInterDigit.setStatus("current")
_CorNetSystemConformance_ObjectIdentity = ObjectIdentity
corNetSystemConformance = _CorNetSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2)
)
_CorNetSystemCompliances_ObjectIdentity = ObjectIdentity
corNetSystemCompliances = _CorNetSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 1)
)
_CorNetSystemGroups_ObjectIdentity = ObjectIdentity
corNetSystemGroups = _CorNetSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2)
)
_CorNetSystemEvents_ObjectIdentity = ObjectIdentity
corNetSystemEvents = _CorNetSystemEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3)
)
_CorNetSystemFaultManagementNotifications_ObjectIdentity = ObjectIdentity
corNetSystemFaultManagementNotifications = _CorNetSystemFaultManagementNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3, 5)
)

# Managed Objects groups

corNetSystemRegistrationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 5)
)
corNetSystemRegistrationGroupVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetSystemRegSubscriberNumber"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemRegLocationIdentifierNumber"))
)
if mibBuilder.loadTexts:
    corNetSystemRegistrationGroupVer1.setStatus("current")

corNetSystemInitializationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 10)
)
corNetSystemInitializationGroupVer1.setObjects(
    ("MX-CORNET-SYSTEM-MIB", "corNetSystemInitEmergencyNumber")
)
if mibBuilder.loadTexts:
    corNetSystemInitializationGroupVer1.setStatus("current")

corNetSystemSecurityGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 13)
)
corNetSystemSecurityGroupVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetSystemSecurityPassword"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemSecurityLevel"))
)
if mibBuilder.loadTexts:
    corNetSystemSecurityGroupVer1.setStatus("current")

corNetSystemFaultManagementGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 15)
)
corNetSystemFaultManagementGroupVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementTrapsEnable"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementTrapsComputePeriod"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementTrapsReportDelay"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementTrapsMaximumPacketsLostRatio"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementPacketsLostStatus"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementJitterBufferStatus"),
        ("MX-CORNET-SYSTEM-MIB", "ipAddressConfigCorNetFaultManagementHost"),
        ("MX-CORNET-SYSTEM-MIB", "ipAddressConfigCorNetFaultManagementTrapPort"),
        ("MX-CORNET-SYSTEM-MIB", "ipAddressStatusCorNetFaultManagementHost"),
        ("MX-CORNET-SYSTEM-MIB", "ipAddressStatusCorNetFaultManagementTrapPort"))
)
if mibBuilder.loadTexts:
    corNetSystemFaultManagementGroupVer1.setStatus("current")

corNetSystemDataGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 50)
)
corNetSystemDataGroupVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetSystemDataRfc2198RedundancyLevel"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemDataRfc2198DefaultPayloadType"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemDataRfc2833DefaultPayloadType"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemDataVoiceOnlyModeEnable"))
)
if mibBuilder.loadTexts:
    corNetSystemDataGroupVer1.setStatus("current")

corNetSystemServicesGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 100)
)
corNetSystemServicesGroupVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetSystemServicesIndex"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServiceName"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServiceEnable"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServiceKbKeyCode"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServiceActivationSequence"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemService2StageFlag"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServiceFirstDigitTimer"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemCallFeaturesEnable"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServices2StageEndingMethod"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServices2StageTimeout"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServices2StageEndKey"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServicesTimeoutInterDigit"))
)
if mibBuilder.loadTexts:
    corNetSystemServicesGroupVer1.setStatus("current")


# Notification objects

corNetFaultManagementRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3, 5, 1050)
)
corNetFaultManagementRebootTrap.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "sysObjectID"),
        ("MX-CORNET-SYSTEM-MIB", "sysMacAddress"))
)
if mibBuilder.loadTexts:
    corNetFaultManagementRebootTrap.setStatus(
        "current"
    )

corNetFaultManagementAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3, 5, 1150)
)
corNetFaultManagementAuthenticationFailureTrap.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "sysObjectID"),
        ("MX-CORNET-SYSTEM-MIB", "sysMacAddress"))
)
if mibBuilder.loadTexts:
    corNetFaultManagementAuthenticationFailureTrap.setStatus(
        "current"
    )

corNetFaultManagementLanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3, 5, 1250)
)
corNetFaultManagementLanTrap.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "sysObjectID"),
        ("MX-CORNET-SYSTEM-MIB", "sysMacAddress"))
)
if mibBuilder.loadTexts:
    corNetFaultManagementLanTrap.setStatus(
        "current"
    )

corNetFaultManagementPacketsLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3, 5, 1350)
)
corNetFaultManagementPacketsLostTrap.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "sysObjectID"),
        ("MX-CORNET-SYSTEM-MIB", "sysMacAddress"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementPacketsLostStatus"))
)
if mibBuilder.loadTexts:
    corNetFaultManagementPacketsLostTrap.setStatus(
        "current"
    )

corNetFaultManagementJitterBufferTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 3, 5, 1450)
)
corNetFaultManagementJitterBufferTrap.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "sysObjectID"),
        ("MX-CORNET-SYSTEM-MIB", "sysMacAddress"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementJitterBufferStatus"))
)
if mibBuilder.loadTexts:
    corNetFaultManagementJitterBufferTrap.setStatus(
        "current"
    )


# Notifications groups

corNetSystemFaultManagementNotificationsGroupVer1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 2, 20)
)
corNetSystemFaultManagementNotificationsGroupVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementRebootTrap"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementAuthenticationFailureTrap"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementLanTrap"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementPacketsLostTrap"),
        ("MX-CORNET-SYSTEM-MIB", "corNetFaultManagementJitterBufferTrap"))
)
if mibBuilder.loadTexts:
    corNetSystemFaultManagementNotificationsGroupVer1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

corNetSystemBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 20, 40, 1, 2, 1, 5)
)
corNetSystemBasicComplVer1.setObjects(
      *(("MX-CORNET-SYSTEM-MIB", "corNetSystemRegistrationGroupVer1"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemInitializationGroupVer1"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemSecurityGroupVer1"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemFaultManagementGroupVer1"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemDataGroupVer1"),
        ("MX-CORNET-SYSTEM-MIB", "corNetSystemServicesGroupVer1"))
)
if mibBuilder.loadTexts:
    corNetSystemBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-CORNET-SYSTEM-MIB",
    **{"ipAddressStatusCorNetPbxIfTable": ipAddressStatusCorNetPbxIfTable,
       "ipAddressStatusCorNetPbxIfEntry": ipAddressStatusCorNetPbxIfEntry,
       "ipAddressStatusCorNetPbxHost": ipAddressStatusCorNetPbxHost,
       "ipAddressStatusCorNetPbxPort": ipAddressStatusCorNetPbxPort,
       "ipAddressStatusCorNetFaultManagementHost": ipAddressStatusCorNetFaultManagementHost,
       "ipAddressStatusCorNetFaultManagementTrapPort": ipAddressStatusCorNetFaultManagementTrapPort,
       "corNetFaultManagementStatus": corNetFaultManagementStatus,
       "corNetFaultManagementPacketsLostStatus": corNetFaultManagementPacketsLostStatus,
       "corNetFaultManagementJitterBufferStatus": corNetFaultManagementJitterBufferStatus,
       "ipAddressConfigCorNetPbxIfTable": ipAddressConfigCorNetPbxIfTable,
       "ipAddressConfigCorNetPbxIfEntry": ipAddressConfigCorNetPbxIfEntry,
       "ipAddressConfigCorNetPbxHost": ipAddressConfigCorNetPbxHost,
       "ipAddressConfigCorNetPbxPort": ipAddressConfigCorNetPbxPort,
       "ipAddressConfigCorNetFaultManagementHost": ipAddressConfigCorNetFaultManagementHost,
       "ipAddressConfigCorNetFaultManagementTrapPort": ipAddressConfigCorNetFaultManagementTrapPort,
       "corNetSystemMIB": corNetSystemMIB,
       "corNetSystemMIBObjects": corNetSystemMIBObjects,
       "corNetSystemRegistration": corNetSystemRegistration,
       "corNetSystemRegistrationIfTable": corNetSystemRegistrationIfTable,
       "corNetSystemRegistrationIfEntry": corNetSystemRegistrationIfEntry,
       "corNetSystemRegSubscriberNumber": corNetSystemRegSubscriberNumber,
       "corNetSystemRegLocationIdentifierNumber": corNetSystemRegLocationIdentifierNumber,
       "corNetSystemInitialization": corNetSystemInitialization,
       "corNetSystemInitializationIfTable": corNetSystemInitializationIfTable,
       "corNetSystemInitializationIfEntry": corNetSystemInitializationIfEntry,
       "corNetSystemInitEmergencyNumber": corNetSystemInitEmergencyNumber,
       "corNetSystemSecurity": corNetSystemSecurity,
       "corNetSystemSecurityIfTable": corNetSystemSecurityIfTable,
       "corNetSystemSecurityIfEntry": corNetSystemSecurityIfEntry,
       "corNetSystemSecurityPassword": corNetSystemSecurityPassword,
       "corNetSystemSecurityLevel": corNetSystemSecurityLevel,
       "corNetSystemFaultManagement": corNetSystemFaultManagement,
       "corNetSystemFaultManagementTrapsEnable": corNetSystemFaultManagementTrapsEnable,
       "corNetSystemFaultManagementTrapsComputePeriod": corNetSystemFaultManagementTrapsComputePeriod,
       "corNetSystemFaultManagementTrapsReportDelay": corNetSystemFaultManagementTrapsReportDelay,
       "corNetSystemFaultManagementTrapsMaximumPacketsLostRatio": corNetSystemFaultManagementTrapsMaximumPacketsLostRatio,
       "corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio": corNetSystemFaultManagementTrapsMaximumJitterBufferOverrunRatio,
       "corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio": corNetSystemFaultManagementTrapsMaximumJitterBufferUnderrunRatio,
       "corNetSystemData": corNetSystemData,
       "corNetSystemDataIfTable": corNetSystemDataIfTable,
       "corNetSystemDataIfEntry": corNetSystemDataIfEntry,
       "corNetSystemDataRfc2198RedundancyLevel": corNetSystemDataRfc2198RedundancyLevel,
       "corNetSystemDataRfc2198DefaultPayloadType": corNetSystemDataRfc2198DefaultPayloadType,
       "corNetSystemDataRfc2833DefaultPayloadType": corNetSystemDataRfc2833DefaultPayloadType,
       "corNetSystemDataVoiceOnlyModeEnable": corNetSystemDataVoiceOnlyModeEnable,
       "corNetSystemServices": corNetSystemServices,
       "corNetSystemServicesTable": corNetSystemServicesTable,
       "corNetSystemServicesEntry": corNetSystemServicesEntry,
       "corNetSystemServicesIndex": corNetSystemServicesIndex,
       "corNetSystemServiceName": corNetSystemServiceName,
       "corNetSystemServiceEnable": corNetSystemServiceEnable,
       "corNetSystemServiceKbKeyCode": corNetSystemServiceKbKeyCode,
       "corNetSystemServiceActivationSequence": corNetSystemServiceActivationSequence,
       "corNetSystemService2StageFlag": corNetSystemService2StageFlag,
       "corNetSystemServiceFirstDigitTimer": corNetSystemServiceFirstDigitTimer,
       "corNetSystemCallFeaturesEnable": corNetSystemCallFeaturesEnable,
       "corNetSystemServices2StageEndingMethod": corNetSystemServices2StageEndingMethod,
       "corNetSystemServices2StageTimeout": corNetSystemServices2StageTimeout,
       "corNetSystemServices2StageEndKey": corNetSystemServices2StageEndKey,
       "corNetSystemServicesTimeoutInterDigit": corNetSystemServicesTimeoutInterDigit,
       "corNetSystemConformance": corNetSystemConformance,
       "corNetSystemCompliances": corNetSystemCompliances,
       "corNetSystemBasicComplVer1": corNetSystemBasicComplVer1,
       "corNetSystemGroups": corNetSystemGroups,
       "corNetSystemRegistrationGroupVer1": corNetSystemRegistrationGroupVer1,
       "corNetSystemInitializationGroupVer1": corNetSystemInitializationGroupVer1,
       "corNetSystemSecurityGroupVer1": corNetSystemSecurityGroupVer1,
       "corNetSystemFaultManagementGroupVer1": corNetSystemFaultManagementGroupVer1,
       "corNetSystemFaultManagementNotificationsGroupVer1": corNetSystemFaultManagementNotificationsGroupVer1,
       "corNetSystemDataGroupVer1": corNetSystemDataGroupVer1,
       "corNetSystemServicesGroupVer1": corNetSystemServicesGroupVer1,
       "corNetSystemEvents": corNetSystemEvents,
       "corNetSystemFaultManagementNotifications": corNetSystemFaultManagementNotifications,
       "corNetFaultManagementRebootTrap": corNetFaultManagementRebootTrap,
       "corNetFaultManagementAuthenticationFailureTrap": corNetFaultManagementAuthenticationFailureTrap,
       "corNetFaultManagementLanTrap": corNetFaultManagementLanTrap,
       "corNetFaultManagementPacketsLostTrap": corNetFaultManagementPacketsLostTrap,
       "corNetFaultManagementJitterBufferTrap": corNetFaultManagementJitterBufferTrap}
)
