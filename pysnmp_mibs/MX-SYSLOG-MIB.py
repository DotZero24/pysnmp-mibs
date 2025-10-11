# SNMP MIB module (MX-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SYSLOG-MIB
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

(ipAddressConfig,
 ipAddressStatus,
 mediatrixConfig) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixConfig")

(MxEnableState,
 MxIpConfigSource,
 MxIpDhcpSiteSpecificCode,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpConfigSource",
    "MxIpDhcpSiteSpecificCode",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSelectConfigSource")

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

syslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17)
)
if mibBuilder.loadTexts:
    syslogMIB.setRevisions(
        ("2004-11-05 00:00",
         "2004-04-27 00:00",
         "2004-02-09 00:00",
         "2002-08-23 00:00",
         "2001-08-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusSyslog_ObjectIdentity = ObjectIdentity
ipAddressStatusSyslog = _IpAddressStatusSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 20)
)


class _SyslogConfigSource_Type(MxIpConfigSource):
    """Custom type syslogConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_SyslogConfigSource_Type.__name__ = "MxIpConfigSource"
_SyslogConfigSource_Object = MibScalar
syslogConfigSource = _SyslogConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 20, 1),
    _SyslogConfigSource_Type()
)
syslogConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogConfigSource.setStatus("current")


class _SyslogHost_Type(MxIpHostName):
    """Custom type syslogHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_SyslogHost_Type.__name__ = "MxIpHostName"
_SyslogHost_Object = MibScalar
syslogHost = _SyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 20, 2),
    _SyslogHost_Type()
)
syslogHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogHost.setStatus("current")


class _SyslogPort_Type(MxIpPort):
    """Custom type syslogPort based on MxIpPort"""
    defaultValue = 514


_SyslogPort_Type.__name__ = "MxIpPort"
_SyslogPort_Object = MibScalar
syslogPort = _SyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 20, 3),
    _SyslogPort_Type()
)
syslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogPort.setStatus("current")
_IpAddressConfigSyslog_ObjectIdentity = ObjectIdentity
ipAddressConfigSyslog = _IpAddressConfigSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20)
)


class _SyslogSelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type syslogSelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_SyslogSelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_SyslogSelectConfigSource_Object = MibScalar
syslogSelectConfigSource = _SyslogSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20, 1),
    _SyslogSelectConfigSource_Type()
)
syslogSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSelectConfigSource.setStatus("current")
_IpAddressConfigSyslogStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigSyslogStatic = _IpAddressConfigSyslogStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20, 10)
)


class _SyslogStaticHost_Type(MxIpHostName):
    """Custom type syslogStaticHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_SyslogStaticHost_Type.__name__ = "MxIpHostName"
_SyslogStaticHost_Object = MibScalar
syslogStaticHost = _SyslogStaticHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20, 10, 1),
    _SyslogStaticHost_Type()
)
syslogStaticHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogStaticHost.setStatus("current")


class _SyslogStaticPort_Type(MxIpPort):
    """Custom type syslogStaticPort based on MxIpPort"""
    defaultValue = 514


_SyslogStaticPort_Type.__name__ = "MxIpPort"
_SyslogStaticPort_Object = MibScalar
syslogStaticPort = _SyslogStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20, 10, 2),
    _SyslogStaticPort_Type()
)
syslogStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogStaticPort.setStatus("current")
_IpAddressConfigSyslogDhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigSyslogDhcp = _IpAddressConfigSyslogDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20, 30)
)


class _SyslogDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type syslogDhcpSiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_SyslogDhcpSiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_SyslogDhcpSiteSpecificCode_Object = MibScalar
syslogDhcpSiteSpecificCode = _SyslogDhcpSiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 20, 30, 1),
    _SyslogDhcpSiteSpecificCode_Type()
)
syslogDhcpSiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDhcpSiteSpecificCode.setStatus("current")
_SyslogMIBObjects_ObjectIdentity = ObjectIdentity
syslogMIBObjects = _SyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1)
)


class _SyslogMsgMaxSeverity_Type(Integer32):
    """Custom type syslogMsgMaxSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SyslogMsgMaxSeverity_Type.__name__ = "Integer32"
_SyslogMsgMaxSeverity_Object = MibScalar
syslogMsgMaxSeverity = _SyslogMsgMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 5),
    _SyslogMsgMaxSeverity_Type()
)
syslogMsgMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgMaxSeverity.setStatus("current")


class _SyslogMsgLocalMaxSeverity_Type(Integer32):
    """Custom type syslogMsgLocalMaxSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SyslogMsgLocalMaxSeverity_Type.__name__ = "Integer32"
_SyslogMsgLocalMaxSeverity_Object = MibScalar
syslogMsgLocalMaxSeverity = _SyslogMsgLocalMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 50),
    _SyslogMsgLocalMaxSeverity_Type()
)
syslogMsgLocalMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgLocalMaxSeverity.setStatus("current")


class _SyslogMsgLocalMaxNbr_Type(Unsigned32):
    """Custom type syslogMsgLocalMaxNbr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SyslogMsgLocalMaxNbr_Type.__name__ = "Unsigned32"
_SyslogMsgLocalMaxNbr_Object = MibScalar
syslogMsgLocalMaxNbr = _SyslogMsgLocalMaxNbr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 100),
    _SyslogMsgLocalMaxNbr_Type()
)
syslogMsgLocalMaxNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgLocalMaxNbr.setStatus("current")
_SyslogLocalMsgTable_Object = MibTable
syslogLocalMsgTable = _SyslogLocalMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 150)
)
if mibBuilder.loadTexts:
    syslogLocalMsgTable.setStatus("current")
_SyslogLocalMsgEntry_Object = MibTableRow
syslogLocalMsgEntry = _SyslogLocalMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 150, 50)
)
syslogLocalMsgEntry.setIndexNames(
    (0, "MX-SYSLOG-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    syslogLocalMsgEntry.setStatus("current")


class _SyslogMsgLocalSeverity_Type(OctetString):
    """Custom type syslogMsgLocalSeverity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SyslogMsgLocalSeverity_Type.__name__ = "OctetString"
_SyslogMsgLocalSeverity_Object = MibTableColumn
syslogMsgLocalSeverity = _SyslogMsgLocalSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 150, 50, 50),
    _SyslogMsgLocalSeverity_Type()
)
syslogMsgLocalSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgLocalSeverity.setStatus("current")


class _SyslogMsgLocalTime_Type(OctetString):
    """Custom type syslogMsgLocalTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SyslogMsgLocalTime_Type.__name__ = "OctetString"
_SyslogMsgLocalTime_Object = MibTableColumn
syslogMsgLocalTime = _SyslogMsgLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 150, 50, 100),
    _SyslogMsgLocalTime_Type()
)
syslogMsgLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgLocalTime.setStatus("current")


class _SyslogMsgLocalModule_Type(OctetString):
    """Custom type syslogMsgLocalModule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SyslogMsgLocalModule_Type.__name__ = "OctetString"
_SyslogMsgLocalModule_Object = MibTableColumn
syslogMsgLocalModule = _SyslogMsgLocalModule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 150, 50, 150),
    _SyslogMsgLocalModule_Type()
)
syslogMsgLocalModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgLocalModule.setStatus("current")


class _SyslogMsgLocalMsg_Type(OctetString):
    """Custom type syslogMsgLocalMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SyslogMsgLocalMsg_Type.__name__ = "OctetString"
_SyslogMsgLocalMsg_Object = MibTableColumn
syslogMsgLocalMsg = _SyslogMsgLocalMsg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 150, 50, 200),
    _SyslogMsgLocalMsg_Type()
)
syslogMsgLocalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgLocalMsg.setStatus("current")
_SyslogMsgCustomization_ObjectIdentity = ObjectIdentity
syslogMsgCustomization = _SyslogMsgCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 200)
)


class _SyslogMsgDisplayMacAddress_Type(MxEnableState):
    """Custom type syslogMsgDisplayMacAddress based on MxEnableState"""
    defaultValue = 0


_SyslogMsgDisplayMacAddress_Type.__name__ = "MxEnableState"
_SyslogMsgDisplayMacAddress_Object = MibScalar
syslogMsgDisplayMacAddress = _SyslogMsgDisplayMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 200, 50),
    _SyslogMsgDisplayMacAddress_Type()
)
syslogMsgDisplayMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgDisplayMacAddress.setStatus("current")


class _SyslogMsgDisplayTime_Type(MxEnableState):
    """Custom type syslogMsgDisplayTime based on MxEnableState"""
    defaultValue = 1


_SyslogMsgDisplayTime_Type.__name__ = "MxEnableState"
_SyslogMsgDisplayTime_Object = MibScalar
syslogMsgDisplayTime = _SyslogMsgDisplayTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 200, 150),
    _SyslogMsgDisplayTime_Type()
)
syslogMsgDisplayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgDisplayTime.setStatus("current")


class _SyslogMsgDisplayTimeFormat_Type(Integer32):
    """Custom type syslogMsgDisplayTimeFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pseudoRfcFormat", 0),
          ("trueRfcFormat", 1))
    )


_SyslogMsgDisplayTimeFormat_Type.__name__ = "Integer32"
_SyslogMsgDisplayTimeFormat_Object = MibScalar
syslogMsgDisplayTimeFormat = _SyslogMsgDisplayTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 200, 175),
    _SyslogMsgDisplayTimeFormat_Type()
)
syslogMsgDisplayTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgDisplayTimeFormat.setStatus("current")


class _SyslogMsgDisplayLocalHost_Type(MxEnableState):
    """Custom type syslogMsgDisplayLocalHost based on MxEnableState"""
    defaultValue = 1


_SyslogMsgDisplayLocalHost_Type.__name__ = "MxEnableState"
_SyslogMsgDisplayLocalHost_Object = MibScalar
syslogMsgDisplayLocalHost = _SyslogMsgDisplayLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 1, 200, 200),
    _SyslogMsgDisplayLocalHost_Type()
)
syslogMsgDisplayLocalHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgDisplayLocalHost.setStatus("current")
_SyslogConformance_ObjectIdentity = ObjectIdentity
syslogConformance = _SyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2)
)
_SyslogCompliances_ObjectIdentity = ObjectIdentity
syslogCompliances = _SyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2, 1)
)
_SyslogGroups_ObjectIdentity = ObjectIdentity
syslogGroups = _SyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2, 2)
)

# Managed Objects groups

syslogBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2, 2, 1)
)
syslogBasicGroupVer1.setObjects(
      *(("MX-SYSLOG-MIB", "syslogMsgMaxSeverity"),
        ("MX-SYSLOG-MIB", "syslogMsgLocalMaxSeverity"),
        ("MX-SYSLOG-MIB", "syslogMsgLocalMaxNbr"),
        ("MX-SYSLOG-MIB", "syslogMsgLocalTime"),
        ("MX-SYSLOG-MIB", "syslogMsgLocalSeverity"),
        ("MX-SYSLOG-MIB", "syslogMsgLocalModule"),
        ("MX-SYSLOG-MIB", "syslogMsgLocalMsg"))
)
if mibBuilder.loadTexts:
    syslogBasicGroupVer1.setStatus("current")

syslogServerGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2, 2, 2)
)
syslogServerGroupVer1.setObjects(
      *(("MX-SYSLOG-MIB", "syslogConfigSource"),
        ("MX-SYSLOG-MIB", "syslogHost"),
        ("MX-SYSLOG-MIB", "syslogPort"),
        ("MX-SYSLOG-MIB", "syslogSelectConfigSource"),
        ("MX-SYSLOG-MIB", "syslogStaticHost"),
        ("MX-SYSLOG-MIB", "syslogStaticPort"),
        ("MX-SYSLOG-MIB", "syslogDhcpSiteSpecificCode"))
)
if mibBuilder.loadTexts:
    syslogServerGroupVer1.setStatus("current")

syslogMsgCustomizationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2, 2, 50)
)
syslogMsgCustomizationGroupVer1.setObjects(
      *(("MX-SYSLOG-MIB", "syslogMsgDisplayMacAddress"),
        ("MX-SYSLOG-MIB", "syslogMsgDisplayTime"),
        ("MX-SYSLOG-MIB", "syslogMsgDisplayTimeFormat"),
        ("MX-SYSLOG-MIB", "syslogMsgDisplayLocalHost"))
)
if mibBuilder.loadTexts:
    syslogMsgCustomizationGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

syslogBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 17, 2, 1, 1)
)
syslogBasicComplVer1.setObjects(
      *(("MX-SYSLOG-MIB", "syslogBasicGroupVer1"),
        ("MX-SYSLOG-MIB", "syslogServerGroupVer1"),
        ("MX-SYSLOG-MIB", "syslogMsgCustomizationGroupVer1"))
)
if mibBuilder.loadTexts:
    syslogBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SYSLOG-MIB",
    **{"ipAddressStatusSyslog": ipAddressStatusSyslog,
       "syslogConfigSource": syslogConfigSource,
       "syslogHost": syslogHost,
       "syslogPort": syslogPort,
       "ipAddressConfigSyslog": ipAddressConfigSyslog,
       "syslogSelectConfigSource": syslogSelectConfigSource,
       "ipAddressConfigSyslogStatic": ipAddressConfigSyslogStatic,
       "syslogStaticHost": syslogStaticHost,
       "syslogStaticPort": syslogStaticPort,
       "ipAddressConfigSyslogDhcp": ipAddressConfigSyslogDhcp,
       "syslogDhcpSiteSpecificCode": syslogDhcpSiteSpecificCode,
       "syslogMIB": syslogMIB,
       "syslogMIBObjects": syslogMIBObjects,
       "syslogMsgMaxSeverity": syslogMsgMaxSeverity,
       "syslogMsgLocalMaxSeverity": syslogMsgLocalMaxSeverity,
       "syslogMsgLocalMaxNbr": syslogMsgLocalMaxNbr,
       "syslogLocalMsgTable": syslogLocalMsgTable,
       "syslogLocalMsgEntry": syslogLocalMsgEntry,
       "syslogMsgLocalSeverity": syslogMsgLocalSeverity,
       "syslogMsgLocalTime": syslogMsgLocalTime,
       "syslogMsgLocalModule": syslogMsgLocalModule,
       "syslogMsgLocalMsg": syslogMsgLocalMsg,
       "syslogMsgCustomization": syslogMsgCustomization,
       "syslogMsgDisplayMacAddress": syslogMsgDisplayMacAddress,
       "syslogMsgDisplayTime": syslogMsgDisplayTime,
       "syslogMsgDisplayTimeFormat": syslogMsgDisplayTimeFormat,
       "syslogMsgDisplayLocalHost": syslogMsgDisplayLocalHost,
       "syslogConformance": syslogConformance,
       "syslogCompliances": syslogCompliances,
       "syslogBasicComplVer1": syslogBasicComplVer1,
       "syslogGroups": syslogGroups,
       "syslogBasicGroupVer1": syslogBasicGroupVer1,
       "syslogServerGroupVer1": syslogServerGroupVer1,
       "syslogMsgCustomizationGroupVer1": syslogMsgCustomizationGroupVer1}
)
