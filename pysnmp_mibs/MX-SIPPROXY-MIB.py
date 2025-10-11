# SNMP MIB module (MX-SIPPROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SIPPROXY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:03 2025
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

sipProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipProxyMIBObjects_ObjectIdentity = ObjectIdentity
sipProxyMIBObjects = _SipProxyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1)
)
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100)
)


class _MonitoringState_Type(Integer32):
    """Custom type monitoringState based on Integer32"""
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
        *(("destinationIsUp", 100),
          ("destinationIsDown", 200),
          ("inactive", 300),
          ("unknown", 400))
    )


_MonitoringState_Type.__name__ = "Integer32"
_MonitoringState_Object = MibScalar
monitoringState = _MonitoringState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 100),
    _MonitoringState_Type()
)
monitoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoringState.setStatus("current")


class _ProxyStatus_Type(Integer32):
    """Custom type proxyStatus based on Integer32"""
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
        *(("starting", 100),
          ("running", 200),
          ("runningInSurvivability", 300),
          ("stopping", 400),
          ("errorPortAlreadyInUse", 500),
          ("errorWaitingForTimeSynchronization", 600),
          ("errorInternal", 700))
    )


_ProxyStatus_Type.__name__ = "Integer32"
_ProxyStatus_Object = MibScalar
proxyStatus = _ProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 200),
    _ProxyStatus_Type()
)
proxyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyStatus.setStatus("current")
_NbActiveCalls_Type = Unsigned32
_NbActiveCalls_Object = MibScalar
nbActiveCalls = _NbActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 250),
    _NbActiveCalls_Type()
)
nbActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbActiveCalls.setStatus("current")
_TlsPersistentConnectionStatusTable_Object = MibTable
tlsPersistentConnectionStatusTable = _TlsPersistentConnectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300)
)
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusTable.setStatus("current")
_TlsPersistentConnectionStatusEntry_Object = MibTableRow
tlsPersistentConnectionStatusEntry = _TlsPersistentConnectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300, 1)
)
tlsPersistentConnectionStatusEntry.setIndexNames(
    (0, "MX-SIPPROXY-MIB", "tlsPersistentConnectionStatusId"),
)
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusEntry.setStatus("current")
_TlsPersistentConnectionStatusId_Type = Unsigned32
_TlsPersistentConnectionStatusId_Object = MibTableColumn
tlsPersistentConnectionStatusId = _TlsPersistentConnectionStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300, 1, 100),
    _TlsPersistentConnectionStatusId_Type()
)
tlsPersistentConnectionStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusId.setStatus("current")
_TlsPersistentConnectionStatusLocalPort_Type = MxAdvancedIpPort
_TlsPersistentConnectionStatusLocalPort_Object = MibTableColumn
tlsPersistentConnectionStatusLocalPort = _TlsPersistentConnectionStatusLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300, 1, 300),
    _TlsPersistentConnectionStatusLocalPort_Type()
)
tlsPersistentConnectionStatusLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusLocalPort.setStatus("current")
_TlsPersistentConnectionStatusRemoteHost_Type = OctetString
_TlsPersistentConnectionStatusRemoteHost_Object = MibTableColumn
tlsPersistentConnectionStatusRemoteHost = _TlsPersistentConnectionStatusRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300, 1, 400),
    _TlsPersistentConnectionStatusRemoteHost_Type()
)
tlsPersistentConnectionStatusRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusRemoteHost.setStatus("current")
_TlsPersistentConnectionStatusRemoteHostIpAddr_Type = OctetString
_TlsPersistentConnectionStatusRemoteHostIpAddr_Object = MibTableColumn
tlsPersistentConnectionStatusRemoteHostIpAddr = _TlsPersistentConnectionStatusRemoteHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300, 1, 450),
    _TlsPersistentConnectionStatusRemoteHostIpAddr_Type()
)
tlsPersistentConnectionStatusRemoteHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusRemoteHostIpAddr.setStatus("current")


class _TlsPersistentConnectionStatusState_Type(Integer32):
    """Custom type tlsPersistentConnectionStatusState based on Integer32"""
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
        *(("up", 100),
          ("down", 200),
          ("waitingShutdown", 300),
          ("waitingUp", 400))
    )


_TlsPersistentConnectionStatusState_Type.__name__ = "Integer32"
_TlsPersistentConnectionStatusState_Object = MibTableColumn
tlsPersistentConnectionStatusState = _TlsPersistentConnectionStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 100, 300, 1, 500),
    _TlsPersistentConnectionStatusState_Type()
)
tlsPersistentConnectionStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusState.setStatus("current")
_ProxyGroup_ObjectIdentity = ObjectIdentity
proxyGroup = _ProxyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 200)
)


class _SurvivabilityMode_Type(Integer32):
    """Custom type survivabilityMode based on Integer32"""
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
        *(("automatic", 100),
          ("alwaysOn", 200),
          ("disabled", 300))
    )


_SurvivabilityMode_Type.__name__ = "Integer32"
_SurvivabilityMode_Object = MibScalar
survivabilityMode = _SurvivabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 200, 100),
    _SurvivabilityMode_Type()
)
survivabilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    survivabilityMode.setStatus("current")


class _ConfigModifiedStatus_Type(Integer32):
    """Custom type configModifiedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("yes", 100),
          ("no", 200))
    )


_ConfigModifiedStatus_Type.__name__ = "Integer32"
_ConfigModifiedStatus_Object = MibScalar
configModifiedStatus = _ConfigModifiedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 200, 300),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")


class _ConfigAppliedStatus_Type(Integer32):
    """Custom type configAppliedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("yes", 100),
          ("no", 200))
    )


_ConfigAppliedStatus_Type.__name__ = "Integer32"
_ConfigAppliedStatus_Object = MibScalar
configAppliedStatus = _ConfigAppliedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 200, 400),
    _ConfigAppliedStatus_Type()
)
configAppliedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configAppliedStatus.setStatus("current")
_NetworkGroup_ObjectIdentity = ObjectIdentity
networkGroup = _NetworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 300)
)


class _NetworkInterface_Type(OctetString):
    """Custom type networkInterface based on OctetString"""
    defaultValue = OctetString("Uplink")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NetworkInterface_Type.__name__ = "OctetString"
_NetworkInterface_Object = MibScalar
networkInterface = _NetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 300, 100),
    _NetworkInterface_Type()
)
networkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkInterface.setStatus("current")


class _Port_Type(MxAdvancedIpPort):
    """Custom type port based on MxAdvancedIpPort"""
    defaultValue = 0


_Port_Type.__name__ = "MxAdvancedIpPort"
_Port_Object = MibScalar
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 300, 200),
    _Port_Type()
)
port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port.setStatus("current")


class _SecurePort_Type(MxAdvancedIpPort):
    """Custom type securePort based on MxAdvancedIpPort"""
    defaultValue = 0


_SecurePort_Type.__name__ = "MxAdvancedIpPort"
_SecurePort_Object = MibScalar
securePort = _SecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 300, 300),
    _SecurePort_Type()
)
securePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securePort.setStatus("current")
_RegisterGroup_ObjectIdentity = ObjectIdentity
registerGroup = _RegisterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400)
)


class _ContactOverrideEnable_Type(MxEnableState):
    """Custom type contactOverrideEnable based on MxEnableState"""
    defaultValue = 1


_ContactOverrideEnable_Type.__name__ = "MxEnableState"
_ContactOverrideEnable_Object = MibScalar
contactOverrideEnable = _ContactOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 50),
    _ContactOverrideEnable_Type()
)
contactOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactOverrideEnable.setStatus("current")


class _EndpointSurvivabilityExpiration_Type(Unsigned32):
    """Custom type endpointSurvivabilityExpiration based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_EndpointSurvivabilityExpiration_Type.__name__ = "Unsigned32"
_EndpointSurvivabilityExpiration_Object = MibScalar
endpointSurvivabilityExpiration = _EndpointSurvivabilityExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 100),
    _EndpointSurvivabilityExpiration_Type()
)
endpointSurvivabilityExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointSurvivabilityExpiration.setStatus("current")


class _RelayedThrottlingExpiration_Type(Unsigned32):
    """Custom type relayedThrottlingExpiration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 86400),
    )


_RelayedThrottlingExpiration_Type.__name__ = "Unsigned32"
_RelayedThrottlingExpiration_Object = MibScalar
relayedThrottlingExpiration = _RelayedThrottlingExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 200),
    _RelayedThrottlingExpiration_Type()
)
relayedThrottlingExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayedThrottlingExpiration.setStatus("current")


class _EndpointThrottlingExpiration_Type(Unsigned32):
    """Custom type endpointThrottlingExpiration based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_EndpointThrottlingExpiration_Type.__name__ = "Unsigned32"
_EndpointThrottlingExpiration_Object = MibScalar
endpointThrottlingExpiration = _EndpointThrottlingExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 300),
    _EndpointThrottlingExpiration_Type()
)
endpointThrottlingExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endpointThrottlingExpiration.setStatus("current")
_RegistrationCacheGroup_ObjectIdentity = ObjectIdentity
registrationCacheGroup = _RegistrationCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400)
)
_RegistrationCacheSearchName_Type = OctetString
_RegistrationCacheSearchName_Object = MibScalar
registrationCacheSearchName = _RegistrationCacheSearchName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 100),
    _RegistrationCacheSearchName_Type()
)
registrationCacheSearchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchName.setStatus("current")


class _RegistrationCacheSearchSort_Type(Integer32):
    """Custom type registrationCacheSearchSort based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("aor", 100),
          ("contact", 200),
          ("receivedTime", 300),
          ("endpointExpiration", 400),
          ("registrarExpiration", 500),
          ("unsorted", 1000))
    )


_RegistrationCacheSearchSort_Type.__name__ = "Integer32"
_RegistrationCacheSearchSort_Object = MibScalar
registrationCacheSearchSort = _RegistrationCacheSearchSort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 200),
    _RegistrationCacheSearchSort_Type()
)
registrationCacheSearchSort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchSort.setStatus("current")
_RegistrationCacheSearchResultTable_Object = MibTable
registrationCacheSearchResultTable = _RegistrationCacheSearchResultTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300)
)
if mibBuilder.loadTexts:
    registrationCacheSearchResultTable.setStatus("current")
_RegistrationCacheSearchResultEntry_Object = MibTableRow
registrationCacheSearchResultEntry = _RegistrationCacheSearchResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1)
)
registrationCacheSearchResultEntry.setIndexNames(
    (0, "MX-SIPPROXY-MIB", "registrationCacheSearchResultId"),
)
if mibBuilder.loadTexts:
    registrationCacheSearchResultEntry.setStatus("current")
_RegistrationCacheSearchResultId_Type = Unsigned32
_RegistrationCacheSearchResultId_Object = MibTableColumn
registrationCacheSearchResultId = _RegistrationCacheSearchResultId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 100),
    _RegistrationCacheSearchResultId_Type()
)
registrationCacheSearchResultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultId.setStatus("current")
_RegistrationCacheSearchResultAor_Type = OctetString
_RegistrationCacheSearchResultAor_Object = MibTableColumn
registrationCacheSearchResultAor = _RegistrationCacheSearchResultAor_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 200),
    _RegistrationCacheSearchResultAor_Type()
)
registrationCacheSearchResultAor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultAor.setStatus("current")
_RegistrationCacheSearchResultContact_Type = OctetString
_RegistrationCacheSearchResultContact_Object = MibTableColumn
registrationCacheSearchResultContact = _RegistrationCacheSearchResultContact_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 300),
    _RegistrationCacheSearchResultContact_Type()
)
registrationCacheSearchResultContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultContact.setStatus("current")
_RegistrationCacheSearchResultReceivedTime_Type = OctetString
_RegistrationCacheSearchResultReceivedTime_Object = MibTableColumn
registrationCacheSearchResultReceivedTime = _RegistrationCacheSearchResultReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 400),
    _RegistrationCacheSearchResultReceivedTime_Type()
)
registrationCacheSearchResultReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultReceivedTime.setStatus("current")
_RegistrationCacheSearchResultEndpointExpiration_Type = OctetString
_RegistrationCacheSearchResultEndpointExpiration_Object = MibTableColumn
registrationCacheSearchResultEndpointExpiration = _RegistrationCacheSearchResultEndpointExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 500),
    _RegistrationCacheSearchResultEndpointExpiration_Type()
)
registrationCacheSearchResultEndpointExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultEndpointExpiration.setStatus("current")
_RegistrationCacheSearchResultRegistrarExpiration_Type = OctetString
_RegistrationCacheSearchResultRegistrarExpiration_Object = MibTableColumn
registrationCacheSearchResultRegistrarExpiration = _RegistrationCacheSearchResultRegistrarExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 550),
    _RegistrationCacheSearchResultRegistrarExpiration_Type()
)
registrationCacheSearchResultRegistrarExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultRegistrarExpiration.setStatus("current")


class _RegistrationCacheSearchResultRegisteredTo_Type(Integer32):
    """Custom type registrationCacheSearchResultRegisteredTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("normal", 100),
          ("local", 200))
    )


_RegistrationCacheSearchResultRegisteredTo_Type.__name__ = "Integer32"
_RegistrationCacheSearchResultRegisteredTo_Object = MibTableColumn
registrationCacheSearchResultRegisteredTo = _RegistrationCacheSearchResultRegisteredTo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 300, 1, 600),
    _RegistrationCacheSearchResultRegisteredTo_Type()
)
registrationCacheSearchResultRegisteredTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationCacheSearchResultRegisteredTo.setStatus("current")
_TotalRegistrationCacheCount_Type = Unsigned32
_TotalRegistrationCacheCount_Object = MibScalar
totalRegistrationCacheCount = _TotalRegistrationCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 400, 400, 400),
    _TotalRegistrationCacheCount_Type()
)
totalRegistrationCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRegistrationCacheCount.setStatus("current")
_MonitoringGroup_ObjectIdentity = ObjectIdentity
monitoringGroup = _MonitoringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 500)
)


class _MonitoringInterval_Type(Unsigned32):
    """Custom type monitoringInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MonitoringInterval_Type.__name__ = "Unsigned32"
_MonitoringInterval_Object = MibScalar
monitoringInterval = _MonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 500, 100),
    _MonitoringInterval_Type()
)
monitoringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitoringInterval.setStatus("current")


class _MonitoringToggleDelay_Type(Unsigned32):
    """Custom type monitoringToggleDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MonitoringToggleDelay_Type.__name__ = "Unsigned32"
_MonitoringToggleDelay_Object = MibScalar
monitoringToggleDelay = _MonitoringToggleDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 500, 200),
    _MonitoringToggleDelay_Type()
)
monitoringToggleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitoringToggleDelay.setStatus("current")


class _MonitoringDestination_Type(MxIpHostNamePort):
    """Custom type monitoringDestination based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_MonitoringDestination_Type.__name__ = "MxIpHostNamePort"
_MonitoringDestination_Object = MibScalar
monitoringDestination = _MonitoringDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 500, 300),
    _MonitoringDestination_Type()
)
monitoringDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitoringDestination.setStatus("current")


class _KeepAliveOptionErrorCodes_Type(OctetString):
    """Custom type keepAliveOptionErrorCodes based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KeepAliveOptionErrorCodes_Type.__name__ = "OctetString"
_KeepAliveOptionErrorCodes_Object = MibScalar
keepAliveOptionErrorCodes = _KeepAliveOptionErrorCodes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 500, 400),
    _KeepAliveOptionErrorCodes_Type()
)
keepAliveOptionErrorCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keepAliveOptionErrorCodes.setStatus("current")
_OptionGroup_ObjectIdentity = ObjectIdentity
optionGroup = _OptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 600)
)


class _SipOptionsMethodSupport_Type(Integer32):
    """Custom type sipOptionsMethodSupport based on Integer32"""
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
        *(("default", 100),
          ("acceptAll", 200),
          ("rejectAll", 300))
    )


_SipOptionsMethodSupport_Type.__name__ = "Integer32"
_SipOptionsMethodSupport_Object = MibScalar
sipOptionsMethodSupport = _SipOptionsMethodSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 600, 100),
    _SipOptionsMethodSupport_Type()
)
sipOptionsMethodSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOptionsMethodSupport.setStatus("current")
_RoutingGroup_ObjectIdentity = ObjectIdentity
routingGroup = _RoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700)
)
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("current")
_RouteEntry_Object = MibTableRow
routeEntry = _RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1)
)
routeEntry.setIndexNames(
    (0, "MX-SIPPROXY-MIB", "routeId"),
)
if mibBuilder.loadTexts:
    routeEntry.setStatus("current")
_RouteId_Type = Unsigned32
_RouteId_Object = MibTableColumn
routeId = _RouteId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 100),
    _RouteId_Type()
)
routeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeId.setStatus("current")


class _RoutePriority_Type(Unsigned32):
    """Custom type routePriority based on Unsigned32"""
    defaultValue = 1


_RoutePriority_Type.__name__ = "Unsigned32"
_RoutePriority_Object = MibTableColumn
routePriority = _RoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 200),
    _RoutePriority_Type()
)
routePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routePriority.setStatus("current")


class _RouteCriteriaType_Type(Integer32):
    """Custom type routeCriteriaType based on Integer32"""
    defaultValue = 200

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
        *(("toUri", 100),
          ("toUser", 200),
          ("toHost", 300),
          ("contactUri", 400),
          ("contactUser", 500),
          ("contactHost", 600))
    )


_RouteCriteriaType_Type.__name__ = "Integer32"
_RouteCriteriaType_Object = MibTableColumn
routeCriteriaType = _RouteCriteriaType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 300),
    _RouteCriteriaType_Type()
)
routeCriteriaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeCriteriaType.setStatus("current")


class _RouteCriteriaExpression_Type(OctetString):
    """Custom type routeCriteriaExpression based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RouteCriteriaExpression_Type.__name__ = "OctetString"
_RouteCriteriaExpression_Object = MibTableColumn
routeCriteriaExpression = _RouteCriteriaExpression_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 400),
    _RouteCriteriaExpression_Type()
)
routeCriteriaExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeCriteriaExpression.setStatus("current")


class _RouteTargetType_Type(Integer32):
    """Custom type routeTargetType based on Integer32"""
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
        *(("registeredAor", 100),
          ("registeredAorUser", 200),
          ("hardcodedHost", 300))
    )


_RouteTargetType_Type.__name__ = "Integer32"
_RouteTargetType_Object = MibTableColumn
routeTargetType = _RouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 500),
    _RouteTargetType_Type()
)
routeTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTargetType.setStatus("current")


class _RouteTargetUserTransformationName_Type(OctetString):
    """Custom type routeTargetUserTransformationName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RouteTargetUserTransformationName_Type.__name__ = "OctetString"
_RouteTargetUserTransformationName_Object = MibTableColumn
routeTargetUserTransformationName = _RouteTargetUserTransformationName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 600),
    _RouteTargetUserTransformationName_Type()
)
routeTargetUserTransformationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTargetUserTransformationName.setStatus("current")


class _RouteRegisteredUserTransformationName_Type(OctetString):
    """Custom type routeRegisteredUserTransformationName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RouteRegisteredUserTransformationName_Type.__name__ = "OctetString"
_RouteRegisteredUserTransformationName_Object = MibTableColumn
routeRegisteredUserTransformationName = _RouteRegisteredUserTransformationName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 700),
    _RouteRegisteredUserTransformationName_Type()
)
routeRegisteredUserTransformationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeRegisteredUserTransformationName.setStatus("current")


class _RouteHardcodedHostPort_Type(MxIpHostNamePort):
    """Custom type routeHardcodedHostPort based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_RouteHardcodedHostPort_Type.__name__ = "MxIpHostNamePort"
_RouteHardcodedHostPort_Object = MibTableColumn
routeHardcodedHostPort = _RouteHardcodedHostPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 800),
    _RouteHardcodedHostPort_Type()
)
routeHardcodedHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeHardcodedHostPort.setStatus("current")


class _RouteConfigStatus_Type(Integer32):
    """Custom type routeConfigStatus based on Integer32"""
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
        *(("valid", 100),
          ("priorityDuplicate", 200),
          ("missingHardcodedHostport", 300),
          ("inexistentTargetUserTransformation", 400),
          ("inexistentRegisteredUserTransformation", 500),
          ("invalid", 600))
    )


_RouteConfigStatus_Type.__name__ = "Integer32"
_RouteConfigStatus_Object = MibTableColumn
routeConfigStatus = _RouteConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 2000),
    _RouteConfigStatus_Type()
)
routeConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeConfigStatus.setStatus("current")


class _RouteDelete_Type(Integer32):
    """Custom type routeDelete based on Integer32"""
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
          ("delete", 10))
    )


_RouteDelete_Type.__name__ = "Integer32"
_RouteDelete_Object = MibTableColumn
routeDelete = _RouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 100, 1, 2100),
    _RouteDelete_Type()
)
routeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDelete.setStatus("current")
_UserTransformationsTable_Object = MibTable
userTransformationsTable = _UserTransformationsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300)
)
if mibBuilder.loadTexts:
    userTransformationsTable.setStatus("current")
_UserTransformationsEntry_Object = MibTableRow
userTransformationsEntry = _UserTransformationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1)
)
userTransformationsEntry.setIndexNames(
    (0, "MX-SIPPROXY-MIB", "userTransformationsId"),
)
if mibBuilder.loadTexts:
    userTransformationsEntry.setStatus("current")
_UserTransformationsId_Type = Unsigned32
_UserTransformationsId_Object = MibTableColumn
userTransformationsId = _UserTransformationsId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 100),
    _UserTransformationsId_Type()
)
userTransformationsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTransformationsId.setStatus("current")


class _UserTransformationsPriority_Type(Unsigned32):
    """Custom type userTransformationsPriority based on Unsigned32"""
    defaultValue = 1


_UserTransformationsPriority_Type.__name__ = "Unsigned32"
_UserTransformationsPriority_Object = MibTableColumn
userTransformationsPriority = _UserTransformationsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 200),
    _UserTransformationsPriority_Type()
)
userTransformationsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTransformationsPriority.setStatus("current")


class _UserTransformationsName_Type(OctetString):
    """Custom type userTransformationsName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_UserTransformationsName_Type.__name__ = "OctetString"
_UserTransformationsName_Object = MibTableColumn
userTransformationsName = _UserTransformationsName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 300),
    _UserTransformationsName_Type()
)
userTransformationsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTransformationsName.setStatus("current")


class _UserTransformationsCriteria_Type(OctetString):
    """Custom type userTransformationsCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_UserTransformationsCriteria_Type.__name__ = "OctetString"
_UserTransformationsCriteria_Object = MibTableColumn
userTransformationsCriteria = _UserTransformationsCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 400),
    _UserTransformationsCriteria_Type()
)
userTransformationsCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTransformationsCriteria.setStatus("current")


class _UserTransformationsPattern_Type(OctetString):
    """Custom type userTransformationsPattern based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_UserTransformationsPattern_Type.__name__ = "OctetString"
_UserTransformationsPattern_Object = MibTableColumn
userTransformationsPattern = _UserTransformationsPattern_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 500),
    _UserTransformationsPattern_Type()
)
userTransformationsPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTransformationsPattern.setStatus("current")


class _UserTransformationsConfigStatus_Type(Integer32):
    """Custom type userTransformationsConfigStatus based on Integer32"""
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
        *(("valid", 100),
          ("priorityDuplicate", 200),
          ("missingName", 300),
          ("invalid", 400))
    )


_UserTransformationsConfigStatus_Type.__name__ = "Integer32"
_UserTransformationsConfigStatus_Object = MibTableColumn
userTransformationsConfigStatus = _UserTransformationsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 2000),
    _UserTransformationsConfigStatus_Type()
)
userTransformationsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTransformationsConfigStatus.setStatus("current")


class _UserTransformationsDelete_Type(Integer32):
    """Custom type userTransformationsDelete based on Integer32"""
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
          ("delete", 10))
    )


_UserTransformationsDelete_Type.__name__ = "Integer32"
_UserTransformationsDelete_Object = MibTableColumn
userTransformationsDelete = _UserTransformationsDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 700, 300, 1, 2100),
    _UserTransformationsDelete_Type()
)
userTransformationsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTransformationsDelete.setStatus("current")
_InteropGroup_ObjectIdentity = ObjectIdentity
interopGroup = _InteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 800)
)


class _InteropRequestTransactionTimeout_Type(Unsigned32):
    """Custom type interopRequestTransactionTimeout based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_InteropRequestTransactionTimeout_Type.__name__ = "Unsigned32"
_InteropRequestTransactionTimeout_Object = MibScalar
interopRequestTransactionTimeout = _InteropRequestTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 800, 100),
    _InteropRequestTransactionTimeout_Type()
)
interopRequestTransactionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopRequestTransactionTimeout.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4600, 1, 60020, 100),
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
    "MX-SIPPROXY-MIB",
    **{"sipProxyMIB": sipProxyMIB,
       "sipProxyMIBObjects": sipProxyMIBObjects,
       "statusGroup": statusGroup,
       "monitoringState": monitoringState,
       "proxyStatus": proxyStatus,
       "nbActiveCalls": nbActiveCalls,
       "tlsPersistentConnectionStatusTable": tlsPersistentConnectionStatusTable,
       "tlsPersistentConnectionStatusEntry": tlsPersistentConnectionStatusEntry,
       "tlsPersistentConnectionStatusId": tlsPersistentConnectionStatusId,
       "tlsPersistentConnectionStatusLocalPort": tlsPersistentConnectionStatusLocalPort,
       "tlsPersistentConnectionStatusRemoteHost": tlsPersistentConnectionStatusRemoteHost,
       "tlsPersistentConnectionStatusRemoteHostIpAddr": tlsPersistentConnectionStatusRemoteHostIpAddr,
       "tlsPersistentConnectionStatusState": tlsPersistentConnectionStatusState,
       "proxyGroup": proxyGroup,
       "survivabilityMode": survivabilityMode,
       "configModifiedStatus": configModifiedStatus,
       "configAppliedStatus": configAppliedStatus,
       "networkGroup": networkGroup,
       "networkInterface": networkInterface,
       "port": port,
       "securePort": securePort,
       "registerGroup": registerGroup,
       "contactOverrideEnable": contactOverrideEnable,
       "endpointSurvivabilityExpiration": endpointSurvivabilityExpiration,
       "relayedThrottlingExpiration": relayedThrottlingExpiration,
       "endpointThrottlingExpiration": endpointThrottlingExpiration,
       "registrationCacheGroup": registrationCacheGroup,
       "registrationCacheSearchName": registrationCacheSearchName,
       "registrationCacheSearchSort": registrationCacheSearchSort,
       "registrationCacheSearchResultTable": registrationCacheSearchResultTable,
       "registrationCacheSearchResultEntry": registrationCacheSearchResultEntry,
       "registrationCacheSearchResultId": registrationCacheSearchResultId,
       "registrationCacheSearchResultAor": registrationCacheSearchResultAor,
       "registrationCacheSearchResultContact": registrationCacheSearchResultContact,
       "registrationCacheSearchResultReceivedTime": registrationCacheSearchResultReceivedTime,
       "registrationCacheSearchResultEndpointExpiration": registrationCacheSearchResultEndpointExpiration,
       "registrationCacheSearchResultRegistrarExpiration": registrationCacheSearchResultRegistrarExpiration,
       "registrationCacheSearchResultRegisteredTo": registrationCacheSearchResultRegisteredTo,
       "totalRegistrationCacheCount": totalRegistrationCacheCount,
       "monitoringGroup": monitoringGroup,
       "monitoringInterval": monitoringInterval,
       "monitoringToggleDelay": monitoringToggleDelay,
       "monitoringDestination": monitoringDestination,
       "keepAliveOptionErrorCodes": keepAliveOptionErrorCodes,
       "optionGroup": optionGroup,
       "sipOptionsMethodSupport": sipOptionsMethodSupport,
       "routingGroup": routingGroup,
       "routeTable": routeTable,
       "routeEntry": routeEntry,
       "routeId": routeId,
       "routePriority": routePriority,
       "routeCriteriaType": routeCriteriaType,
       "routeCriteriaExpression": routeCriteriaExpression,
       "routeTargetType": routeTargetType,
       "routeTargetUserTransformationName": routeTargetUserTransformationName,
       "routeRegisteredUserTransformationName": routeRegisteredUserTransformationName,
       "routeHardcodedHostPort": routeHardcodedHostPort,
       "routeConfigStatus": routeConfigStatus,
       "routeDelete": routeDelete,
       "userTransformationsTable": userTransformationsTable,
       "userTransformationsEntry": userTransformationsEntry,
       "userTransformationsId": userTransformationsId,
       "userTransformationsPriority": userTransformationsPriority,
       "userTransformationsName": userTransformationsName,
       "userTransformationsCriteria": userTransformationsCriteria,
       "userTransformationsPattern": userTransformationsPattern,
       "userTransformationsConfigStatus": userTransformationsConfigStatus,
       "userTransformationsDelete": userTransformationsDelete,
       "interopGroup": interopGroup,
       "interopRequestTransactionTimeout": interopRequestTransactionTimeout,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
