# SNMP MIB module (MX-CWMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CWMP-MIB
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

cwmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwmpMIBObjects_ObjectIdentity = ObjectIdentity
cwmpMIBObjects = _CwmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1)
)


class _RootElement_Type(Integer32):
    """Custom type rootElement based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("device", 100),
          ("internetGatewayDevice", 200))
    )


_RootElement_Type.__name__ = "Integer32"
_RootElement_Object = MibScalar
rootElement = _RootElement_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 100),
    _RootElement_Type()
)
rootElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rootElement.setStatus("current")


class _NetworkInterface_Type(OctetString):
    """Custom type networkInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NetworkInterface_Type.__name__ = "OctetString"
_NetworkInterface_Object = MibScalar
networkInterface = _NetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 190),
    _NetworkInterface_Type()
)
networkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkInterface.setStatus("current")


class _ListeningPort_Type(MxAdvancedIpPort):
    """Custom type listeningPort based on MxAdvancedIpPort"""
    defaultValue = 0


_ListeningPort_Type.__name__ = "MxAdvancedIpPort"
_ListeningPort_Object = MibScalar
listeningPort = _ListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 200),
    _ListeningPort_Type()
)
listeningPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listeningPort.setStatus("current")
_AcsGroup_ObjectIdentity = ObjectIdentity
acsGroup = _AcsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000)
)


class _AcsUrlConfigSource_Type(Integer32):
    """Custom type acsUrlConfigSource based on Integer32"""
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
        *(("dhcp", 100),
          ("static", 200),
          ("dhcpWithFailover", 300))
    )


_AcsUrlConfigSource_Type.__name__ = "Integer32"
_AcsUrlConfigSource_Object = MibScalar
acsUrlConfigSource = _AcsUrlConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 100),
    _AcsUrlConfigSource_Type()
)
acsUrlConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsUrlConfigSource.setStatus("current")


class _AcsStaticUrl_Type(OctetString):
    """Custom type acsStaticUrl based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcsStaticUrl_Type.__name__ = "OctetString"
_AcsStaticUrl_Object = MibScalar
acsStaticUrl = _AcsStaticUrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 200),
    _AcsStaticUrl_Type()
)
acsStaticUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsStaticUrl.setStatus("current")


class _Username_Type(OctetString):
    """Custom type username based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Username_Type.__name__ = "OctetString"
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 300),
    _Username_Type()
)
username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _Password_Type(OctetString):
    """Custom type password based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Password_Type.__name__ = "OctetString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 600),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")


class _AcsStatus_Type(Integer32):
    """Custom type acsStatus based on Integer32"""
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
          ("connected", 200),
          ("noUrl", 300),
          ("errorCannotResolve", 400),
          ("errorNotResponding", 500),
          ("errorAuthFailure", 600),
          ("errorOther", 700))
    )


_AcsStatus_Type.__name__ = "Integer32"
_AcsStatus_Object = MibScalar
acsStatus = _AcsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 700),
    _AcsStatus_Type()
)
acsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsStatus.setStatus("current")
_AcsUrl_Type = OctetString
_AcsUrl_Object = MibScalar
acsUrl = _AcsUrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 750),
    _AcsUrl_Type()
)
acsUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsUrl.setStatus("current")


class _ConnectionRequestUsername_Type(OctetString):
    """Custom type connectionRequestUsername based on OctetString"""
    defaultValue = OctetString("admin")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConnectionRequestUsername_Type.__name__ = "OctetString"
_ConnectionRequestUsername_Object = MibScalar
connectionRequestUsername = _ConnectionRequestUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 800),
    _ConnectionRequestUsername_Type()
)
connectionRequestUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRequestUsername.setStatus("current")


class _ConnectionRequestPassword_Type(OctetString):
    """Custom type connectionRequestPassword based on OctetString"""
    defaultValue = OctetString("administrator")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConnectionRequestPassword_Type.__name__ = "OctetString"
_ConnectionRequestPassword_Object = MibScalar
connectionRequestPassword = _ConnectionRequestPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 1000, 900),
    _ConnectionRequestPassword_Type()
)
connectionRequestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRequestPassword.setStatus("current")
_PeriodicInformGroup_ObjectIdentity = ObjectIdentity
periodicInformGroup = _PeriodicInformGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2000)
)


class _PeriodicInformEnable_Type(MxEnableState):
    """Custom type periodicInformEnable based on MxEnableState"""
    defaultValue = 0


_PeriodicInformEnable_Type.__name__ = "MxEnableState"
_PeriodicInformEnable_Object = MibScalar
periodicInformEnable = _PeriodicInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2000, 100),
    _PeriodicInformEnable_Type()
)
periodicInformEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    periodicInformEnable.setStatus("current")


class _PeriodicInformInterval_Type(Unsigned32):
    """Custom type periodicInformInterval based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31536000),
    )


_PeriodicInformInterval_Type.__name__ = "Unsigned32"
_PeriodicInformInterval_Object = MibScalar
periodicInformInterval = _PeriodicInformInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2000, 200),
    _PeriodicInformInterval_Type()
)
periodicInformInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    periodicInformInterval.setStatus("current")


class _PeriodicInformTime_Type(OctetString):
    """Custom type periodicInformTime based on OctetString"""
    defaultValue = OctetString("0001-01-01T00:00:00Z")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PeriodicInformTime_Type.__name__ = "OctetString"
_PeriodicInformTime_Object = MibScalar
periodicInformTime = _PeriodicInformTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2000, 300),
    _PeriodicInformTime_Type()
)
periodicInformTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    periodicInformTime.setStatus("current")
_Tr069Group_ObjectIdentity = ObjectIdentity
tr069Group = _Tr069Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2100)
)


class _Tr069AnnexFEnable_Type(MxEnableState):
    """Custom type tr069AnnexFEnable based on MxEnableState"""
    defaultValue = 0


_Tr069AnnexFEnable_Type.__name__ = "MxEnableState"
_Tr069AnnexFEnable_Object = MibScalar
tr069AnnexFEnable = _Tr069AnnexFEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2100, 100),
    _Tr069AnnexFEnable_Type()
)
tr069AnnexFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr069AnnexFEnable.setStatus("current")
_Tr104Group_ObjectIdentity = ObjectIdentity
tr104Group = _Tr104Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2900)
)


class _Tr104Enable_Type(MxEnableState):
    """Custom type tr104Enable based on MxEnableState"""
    defaultValue = 0


_Tr104Enable_Type.__name__ = "MxEnableState"
_Tr104Enable_Object = MibScalar
tr104Enable = _Tr104Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 2900, 100),
    _Tr104Enable_Type()
)
tr104Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr104Enable.setStatus("current")
_Tr106Group_ObjectIdentity = ObjectIdentity
tr106Group = _Tr106Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 3000)
)


class _Tr106LanNetworkInterface_Type(OctetString):
    """Custom type tr106LanNetworkInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Tr106LanNetworkInterface_Type.__name__ = "OctetString"
_Tr106LanNetworkInterface_Object = MibScalar
tr106LanNetworkInterface = _Tr106LanNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 3000, 100),
    _Tr106LanNetworkInterface_Type()
)
tr106LanNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr106LanNetworkInterface.setStatus("current")
_Tr111Group_ObjectIdentity = ObjectIdentity
tr111Group = _Tr111Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000)
)


class _Tr111StunEnable_Type(MxEnableState):
    """Custom type tr111StunEnable based on MxEnableState"""
    defaultValue = 0


_Tr111StunEnable_Type.__name__ = "MxEnableState"
_Tr111StunEnable_Object = MibScalar
tr111StunEnable = _Tr111StunEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000, 100),
    _Tr111StunEnable_Type()
)
tr111StunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr111StunEnable.setStatus("current")


class _Tr111NatDetected_Type(Integer32):
    """Custom type tr111NatDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("no", 100),
          ("yes", 200))
    )


_Tr111NatDetected_Type.__name__ = "Integer32"
_Tr111NatDetected_Object = MibScalar
tr111NatDetected = _Tr111NatDetected_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000, 200),
    _Tr111NatDetected_Type()
)
tr111NatDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr111NatDetected.setStatus("current")


class _Tr111StunServerHost_Type(MxIpHostNamePort):
    """Custom type tr111StunServerHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_Tr111StunServerHost_Type.__name__ = "MxIpHostNamePort"
_Tr111StunServerHost_Object = MibScalar
tr111StunServerHost = _Tr111StunServerHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000, 300),
    _Tr111StunServerHost_Type()
)
tr111StunServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr111StunServerHost.setStatus("current")


class _Tr111StunKeepAlivePeriod_Type(OctetString):
    """Custom type tr111StunKeepAlivePeriod based on OctetString"""
    defaultValue = OctetString("60-60")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Tr111StunKeepAlivePeriod_Type.__name__ = "OctetString"
_Tr111StunKeepAlivePeriod_Object = MibScalar
tr111StunKeepAlivePeriod = _Tr111StunKeepAlivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000, 400),
    _Tr111StunKeepAlivePeriod_Type()
)
tr111StunKeepAlivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr111StunKeepAlivePeriod.setStatus("current")


class _Tr111StunUsername_Type(OctetString):
    """Custom type tr111StunUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Tr111StunUsername_Type.__name__ = "OctetString"
_Tr111StunUsername_Object = MibScalar
tr111StunUsername = _Tr111StunUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000, 500),
    _Tr111StunUsername_Type()
)
tr111StunUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr111StunUsername.setStatus("current")


class _Tr111StunStatus_Type(Integer32):
    """Custom type tr111StunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              400,
              500,
              700)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("starting", 100),
          ("connected", 200),
          ("errorCannotResolve", 400),
          ("errorNotResponding", 500),
          ("errorOther", 700))
    )


_Tr111StunStatus_Type.__name__ = "Integer32"
_Tr111StunStatus_Object = MibScalar
tr111StunStatus = _Tr111StunStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4000, 600),
    _Tr111StunStatus_Type()
)
tr111StunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr111StunStatus.setStatus("current")
_DataModelGroup_ObjectIdentity = ObjectIdentity
dataModelGroup = _DataModelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4500)
)


class _NlmLocalLogLogEnable_Type(MxEnableState):
    """Custom type nlmLocalLogLogEnable based on MxEnableState"""
    defaultValue = 0


_NlmLocalLogLogEnable_Type.__name__ = "MxEnableState"
_NlmLocalLogLogEnable_Object = MibScalar
nlmLocalLogLogEnable = _NlmLocalLogLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 4500, 100),
    _NlmLocalLogLogEnable_Type()
)
nlmLocalLogLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlmLocalLogLogEnable.setStatus("current")
_TransportGroup_ObjectIdentity = ObjectIdentity
transportGroup = _TransportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 5000)
)


class _TransportHttpsCipherSuite_Type(Integer32):
    """Custom type transportHttpsCipherSuite based on Integer32"""
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


_TransportHttpsCipherSuite_Type.__name__ = "Integer32"
_TransportHttpsCipherSuite_Object = MibScalar
transportHttpsCipherSuite = _TransportHttpsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 5000, 100),
    _TransportHttpsCipherSuite_Type()
)
transportHttpsCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportHttpsCipherSuite.setStatus("current")


class _TransportHttpsTlsVersion_Type(Integer32):
    """Custom type transportHttpsTlsVersion based on Integer32"""
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


_TransportHttpsTlsVersion_Type.__name__ = "Integer32"
_TransportHttpsTlsVersion_Object = MibScalar
transportHttpsTlsVersion = _TransportHttpsTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 5000, 150),
    _TransportHttpsTlsVersion_Type()
)
transportHttpsTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportHttpsTlsVersion.setStatus("current")


class _TransportCertificateValidation_Type(Integer32):
    """Custom type transportCertificateValidation based on Integer32"""
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


_TransportCertificateValidation_Type.__name__ = "Integer32"
_TransportCertificateValidation_Object = MibScalar
transportCertificateValidation = _TransportCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 5000, 200),
    _TransportCertificateValidation_Type()
)
transportCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportCertificateValidation.setStatus("current")
_InteropGroup_ObjectIdentity = ObjectIdentity
interopGroup = _InteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 50000)
)


class _InteropAllowUnauthenticatedUDPConnectionRequests_Type(MxEnableState):
    """Custom type interopAllowUnauthenticatedUDPConnectionRequests based on MxEnableState"""
    defaultValue = 0


_InteropAllowUnauthenticatedUDPConnectionRequests_Type.__name__ = "MxEnableState"
_InteropAllowUnauthenticatedUDPConnectionRequests_Object = MibScalar
interopAllowUnauthenticatedUDPConnectionRequests = _InteropAllowUnauthenticatedUDPConnectionRequests_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 50000, 100),
    _InteropAllowUnauthenticatedUDPConnectionRequests_Type()
)
interopAllowUnauthenticatedUDPConnectionRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopAllowUnauthenticatedUDPConnectionRequests.setStatus("current")


class _InteropParameterTypeValidation_Type(Integer32):
    """Custom type interopParameterTypeValidation based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("tolerant", 100),
          ("strict", 200))
    )


_InteropParameterTypeValidation_Type.__name__ = "Integer32"
_InteropParameterTypeValidation_Object = MibScalar
interopParameterTypeValidation = _InteropParameterTypeValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 50000, 200),
    _InteropParameterTypeValidation_Type()
)
interopParameterTypeValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopParameterTypeValidation.setStatus("current")


class _InteropMacAddressFormat_Type(Integer32):
    """Custom type interopMacAddressFormat based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 100),
          ("upperCaseWithColon", 200))
    )


_InteropMacAddressFormat_Type.__name__ = "Integer32"
_InteropMacAddressFormat_Object = MibScalar
interopMacAddressFormat = _InteropMacAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 50000, 300),
    _InteropMacAddressFormat_Type()
)
interopMacAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopMacAddressFormat.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3900, 1, 60020, 100),
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
    "MX-CWMP-MIB",
    **{"cwmpMIB": cwmpMIB,
       "cwmpMIBObjects": cwmpMIBObjects,
       "rootElement": rootElement,
       "networkInterface": networkInterface,
       "listeningPort": listeningPort,
       "acsGroup": acsGroup,
       "acsUrlConfigSource": acsUrlConfigSource,
       "acsStaticUrl": acsStaticUrl,
       "username": username,
       "password": password,
       "acsStatus": acsStatus,
       "acsUrl": acsUrl,
       "connectionRequestUsername": connectionRequestUsername,
       "connectionRequestPassword": connectionRequestPassword,
       "periodicInformGroup": periodicInformGroup,
       "periodicInformEnable": periodicInformEnable,
       "periodicInformInterval": periodicInformInterval,
       "periodicInformTime": periodicInformTime,
       "tr069Group": tr069Group,
       "tr069AnnexFEnable": tr069AnnexFEnable,
       "tr104Group": tr104Group,
       "tr104Enable": tr104Enable,
       "tr106Group": tr106Group,
       "tr106LanNetworkInterface": tr106LanNetworkInterface,
       "tr111Group": tr111Group,
       "tr111StunEnable": tr111StunEnable,
       "tr111NatDetected": tr111NatDetected,
       "tr111StunServerHost": tr111StunServerHost,
       "tr111StunKeepAlivePeriod": tr111StunKeepAlivePeriod,
       "tr111StunUsername": tr111StunUsername,
       "tr111StunStatus": tr111StunStatus,
       "dataModelGroup": dataModelGroup,
       "nlmLocalLogLogEnable": nlmLocalLogLogEnable,
       "transportGroup": transportGroup,
       "transportHttpsCipherSuite": transportHttpsCipherSuite,
       "transportHttpsTlsVersion": transportHttpsTlsVersion,
       "transportCertificateValidation": transportCertificateValidation,
       "interopGroup": interopGroup,
       "interopAllowUnauthenticatedUDPConnectionRequests": interopAllowUnauthenticatedUDPConnectionRequests,
       "interopParameterTypeValidation": interopParameterTypeValidation,
       "interopMacAddressFormat": interopMacAddressFormat,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
