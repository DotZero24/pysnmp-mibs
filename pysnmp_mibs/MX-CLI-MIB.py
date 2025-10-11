# SNMP MIB module (MX-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CLI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:49 2025
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

cliMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CliMIBObjects_ObjectIdentity = ObjectIdentity
cliMIBObjects = _CliMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1)
)


class _InactivityTimeOut_Type(Unsigned32):
    """Custom type inactivityTimeOut based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_InactivityTimeOut_Type.__name__ = "Unsigned32"
_InactivityTimeOut_Object = MibScalar
inactivityTimeOut = _InactivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 100),
    _InactivityTimeOut_Type()
)
inactivityTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inactivityTimeOut.setStatus("current")


class _WelcomeMessage_Type(OctetString):
    """Custom type welcomeMessage based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_WelcomeMessage_Type.__name__ = "OctetString"
_WelcomeMessage_Object = MibScalar
welcomeMessage = _WelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 200),
    _WelcomeMessage_Type()
)
welcomeMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    welcomeMessage.setStatus("current")
_TelnetGroup_ObjectIdentity = ObjectIdentity
telnetGroup = _TelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1000)
)


class _EnableTelnet_Type(MxEnableState):
    """Custom type enableTelnet based on MxEnableState"""
    defaultValue = 0


_EnableTelnet_Type.__name__ = "MxEnableState"
_EnableTelnet_Object = MibScalar
enableTelnet = _EnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1000, 100),
    _EnableTelnet_Type()
)
enableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTelnet.setStatus("current")


class _TelnetPort_Type(MxIpPort):
    """Custom type telnetPort based on MxIpPort"""
    defaultValue = 23


_TelnetPort_Type.__name__ = "MxIpPort"
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1000, 200),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")
_SshGroup_ObjectIdentity = ObjectIdentity
sshGroup = _SshGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1100)
)


class _EnableSsh_Type(MxEnableState):
    """Custom type enableSsh based on MxEnableState"""
    defaultValue = 1


_EnableSsh_Type.__name__ = "MxEnableState"
_EnableSsh_Object = MibScalar
enableSsh = _EnableSsh_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1100, 100),
    _EnableSsh_Type()
)
enableSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSsh.setStatus("current")


class _SshPort_Type(MxIpPort):
    """Custom type sshPort based on MxIpPort"""
    defaultValue = 22


_SshPort_Type.__name__ = "MxIpPort"
_SshPort_Object = MibScalar
sshPort = _SshPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1100, 200),
    _SshPort_Type()
)
sshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPort.setStatus("current")


class _SshSecurityLevel_Type(Integer32):
    """Custom type sshSecurityLevel based on Integer32"""
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
        *(("permissive", 100),
          ("standard", 200),
          ("mostSecure", 300))
    )


_SshSecurityLevel_Type.__name__ = "Integer32"
_SshSecurityLevel_Object = MibScalar
sshSecurityLevel = _SshSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 1100, 300),
    _SshSecurityLevel_Type()
)
sshSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSecurityLevel.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2700, 1, 60020, 100),
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
    "MX-CLI-MIB",
    **{"cliMIB": cliMIB,
       "cliMIBObjects": cliMIBObjects,
       "inactivityTimeOut": inactivityTimeOut,
       "welcomeMessage": welcomeMessage,
       "telnetGroup": telnetGroup,
       "enableTelnet": enableTelnet,
       "telnetPort": telnetPort,
       "sshGroup": sshGroup,
       "enableSsh": enableSsh,
       "sshPort": sshPort,
       "sshSecurityLevel": sshSecurityLevel,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
