# SNMP MIB module (MX-DEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DEBUG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:42 2025
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

(MxIpHostName,
 MxIpPort) = mibBuilder.importSymbols(
    "MX-TC",
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

mxDebugMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5)
)
if mibBuilder.loadTexts:
    mxDebugMIB.setRevisions(
        ("1909-11-27 00:00",
         "1908-08-22 00:00",
         "1908-05-21 00:00",
         "1907-10-24 00:00",
         "1902-07-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MxDebugMIBObjects_ObjectIdentity = ObjectIdentity
mxDebugMIBObjects = _MxDebugMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1)
)
_MxDebugSignalingLog_ObjectIdentity = ObjectIdentity
mxDebugSignalingLog = _MxDebugSignalingLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 5)
)


class _MxDebugSignalingLogEnable_Type(Integer32):
    """Custom type mxDebugSignalingLogEnable based on Integer32"""
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


_MxDebugSignalingLogEnable_Type.__name__ = "Integer32"
_MxDebugSignalingLogEnable_Object = MibScalar
mxDebugSignalingLogEnable = _MxDebugSignalingLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 5, 1),
    _MxDebugSignalingLogEnable_Type()
)
mxDebugSignalingLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugSignalingLogEnable.setStatus("current")


class _MxDebugSignalingLogHost_Type(MxIpHostName):
    """Custom type mxDebugSignalingLogHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_MxDebugSignalingLogHost_Type.__name__ = "MxIpHostName"
_MxDebugSignalingLogHost_Object = MibScalar
mxDebugSignalingLogHost = _MxDebugSignalingLogHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 5, 2),
    _MxDebugSignalingLogHost_Type()
)
mxDebugSignalingLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugSignalingLogHost.setStatus("current")


class _MxDebugSignalingLogPort_Type(MxIpPort):
    """Custom type mxDebugSignalingLogPort based on MxIpPort"""
    defaultValue = 6000


_MxDebugSignalingLogPort_Type.__name__ = "MxIpPort"
_MxDebugSignalingLogPort_Object = MibScalar
mxDebugSignalingLogPort = _MxDebugSignalingLogPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 5, 3),
    _MxDebugSignalingLogPort_Type()
)
mxDebugSignalingLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugSignalingLogPort.setStatus("current")
_MxDebugFax_ObjectIdentity = ObjectIdentity
mxDebugFax = _MxDebugFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 10)
)


class _MxDebugT38OutgoingToSyslog_Type(Integer32):
    """Custom type mxDebugT38OutgoingToSyslog based on Integer32"""
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


_MxDebugT38OutgoingToSyslog_Type.__name__ = "Integer32"
_MxDebugT38OutgoingToSyslog_Object = MibScalar
mxDebugT38OutgoingToSyslog = _MxDebugT38OutgoingToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 10, 5),
    _MxDebugT38OutgoingToSyslog_Type()
)
mxDebugT38OutgoingToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugT38OutgoingToSyslog.setStatus("current")


class _MxDebugT38IncomingToSyslog_Type(Integer32):
    """Custom type mxDebugT38IncomingToSyslog based on Integer32"""
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


_MxDebugT38IncomingToSyslog_Type.__name__ = "Integer32"
_MxDebugT38IncomingToSyslog_Object = MibScalar
mxDebugT38IncomingToSyslog = _MxDebugT38IncomingToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 10, 6),
    _MxDebugT38IncomingToSyslog_Type()
)
mxDebugT38IncomingToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugT38IncomingToSyslog.setStatus("current")


class _MxDebugFaxRelayForDspToSyslog_Type(Integer32):
    """Custom type mxDebugFaxRelayForDspToSyslog based on Integer32"""
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


_MxDebugFaxRelayForDspToSyslog_Type.__name__ = "Integer32"
_MxDebugFaxRelayForDspToSyslog_Object = MibScalar
mxDebugFaxRelayForDspToSyslog = _MxDebugFaxRelayForDspToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 10, 15),
    _MxDebugFaxRelayForDspToSyslog_Type()
)
mxDebugFaxRelayForDspToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugFaxRelayForDspToSyslog.setStatus("current")


class _MxDebugFaxRelayFromDspToSyslog_Type(Integer32):
    """Custom type mxDebugFaxRelayFromDspToSyslog based on Integer32"""
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


_MxDebugFaxRelayFromDspToSyslog_Type.__name__ = "Integer32"
_MxDebugFaxRelayFromDspToSyslog_Object = MibScalar
mxDebugFaxRelayFromDspToSyslog = _MxDebugFaxRelayFromDspToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 10, 16),
    _MxDebugFaxRelayFromDspToSyslog_Type()
)
mxDebugFaxRelayFromDspToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugFaxRelayFromDspToSyslog.setStatus("current")
_MxDebugPcmCapture_ObjectIdentity = ObjectIdentity
mxDebugPcmCapture = _MxDebugPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 60)
)


class _MxDebugPcmCaptureEnable_Type(Integer32):
    """Custom type mxDebugPcmCaptureEnable based on Integer32"""
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


_MxDebugPcmCaptureEnable_Type.__name__ = "Integer32"
_MxDebugPcmCaptureEnable_Object = MibScalar
mxDebugPcmCaptureEnable = _MxDebugPcmCaptureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 60, 5),
    _MxDebugPcmCaptureEnable_Type()
)
mxDebugPcmCaptureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugPcmCaptureEnable.setStatus("current")


class _MxDebugPcmCaptureIpAddress_Type(MxIpHostName):
    """Custom type mxDebugPcmCaptureIpAddress based on MxIpHostName"""
    defaultValue = OctetString("192.168.10.1")


_MxDebugPcmCaptureIpAddress_Type.__name__ = "MxIpHostName"
_MxDebugPcmCaptureIpAddress_Object = MibScalar
mxDebugPcmCaptureIpAddress = _MxDebugPcmCaptureIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 60, 10),
    _MxDebugPcmCaptureIpAddress_Type()
)
mxDebugPcmCaptureIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugPcmCaptureIpAddress.setStatus("current")


class _MxDebugPcmCaptureEndpointNumber_Type(Unsigned32):
    """Custom type mxDebugPcmCaptureEndpointNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MxDebugPcmCaptureEndpointNumber_Type.__name__ = "Unsigned32"
_MxDebugPcmCaptureEndpointNumber_Object = MibScalar
mxDebugPcmCaptureEndpointNumber = _MxDebugPcmCaptureEndpointNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 60, 20),
    _MxDebugPcmCaptureEndpointNumber_Type()
)
mxDebugPcmCaptureEndpointNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugPcmCaptureEndpointNumber.setStatus("current")
_MxDebugDspStats_ObjectIdentity = ObjectIdentity
mxDebugDspStats = _MxDebugDspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 70)
)


class _MxDebugDspStatsEnable_Type(Integer32):
    """Custom type mxDebugDspStatsEnable based on Integer32"""
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


_MxDebugDspStatsEnable_Type.__name__ = "Integer32"
_MxDebugDspStatsEnable_Object = MibScalar
mxDebugDspStatsEnable = _MxDebugDspStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 70, 5),
    _MxDebugDspStatsEnable_Type()
)
mxDebugDspStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugDspStatsEnable.setStatus("current")


class _MxDebugDspStatsInterval_Type(Unsigned32):
    """Custom type mxDebugDspStatsInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MxDebugDspStatsInterval_Type.__name__ = "Unsigned32"
_MxDebugDspStatsInterval_Object = MibScalar
mxDebugDspStatsInterval = _MxDebugDspStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 70, 10),
    _MxDebugDspStatsInterval_Type()
)
mxDebugDspStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugDspStatsInterval.setStatus("current")


class _MxDebugDspStatsFilter_Type(Unsigned32):
    """Custom type mxDebugDspStatsFilter based on Unsigned32"""
    defaultValue = 0


_MxDebugDspStatsFilter_Type.__name__ = "Unsigned32"
_MxDebugDspStatsFilter_Object = MibScalar
mxDebugDspStatsFilter = _MxDebugDspStatsFilter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 1, 70, 15),
    _MxDebugDspStatsFilter_Type()
)
mxDebugDspStatsFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxDebugDspStatsFilter.setStatus("current")
_MxDebugConformance_ObjectIdentity = ObjectIdentity
mxDebugConformance = _MxDebugConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2)
)
_MxDebugCompliances_ObjectIdentity = ObjectIdentity
mxDebugCompliances = _MxDebugCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2, 1)
)
_MxDebugGroups_ObjectIdentity = ObjectIdentity
mxDebugGroups = _MxDebugGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2, 2)
)

# Managed Objects groups

mxDebugSignalingLogGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2, 2, 10)
)
mxDebugSignalingLogGroupVer1.setObjects(
      *(("MX-DEBUG-MIB", "mxDebugSignalingLogEnable"),
        ("MX-DEBUG-MIB", "mxDebugSignalingLogHost"),
        ("MX-DEBUG-MIB", "mxDebugSignalingLogPort"))
)
if mibBuilder.loadTexts:
    mxDebugSignalingLogGroupVer1.setStatus("current")

mxDebugFaxGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2, 2, 20)
)
mxDebugFaxGroupVer1.setObjects(
      *(("MX-DEBUG-MIB", "mxDebugT38OutgoingToSyslog"),
        ("MX-DEBUG-MIB", "mxDebugT38IncomingToSyslog"),
        ("MX-DEBUG-MIB", "mxDebugFaxRelayForDspToSyslog"),
        ("MX-DEBUG-MIB", "mxDebugFaxRelayFromDspToSyslog"))
)
if mibBuilder.loadTexts:
    mxDebugFaxGroupVer1.setStatus("current")

mxDebugPcmCaptureGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2, 2, 30)
)
mxDebugPcmCaptureGroupVer1.setObjects(
      *(("MX-DEBUG-MIB", "mxDebugPcmCaptureEnable"),
        ("MX-DEBUG-MIB", "mxDebugPcmCaptureIpAddress"))
)
if mibBuilder.loadTexts:
    mxDebugPcmCaptureGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mxDebugComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 5, 2, 1, 10)
)
mxDebugComplVer1.setObjects(
      *(("MX-DEBUG-MIB", "mxDebugSignalingLogGroupVer1"),
        ("MX-DEBUG-MIB", "mxDebugFaxGroupVer1"),
        ("MX-DEBUG-MIB", "mxDebugPcmCaptureGroupVer1"))
)
if mibBuilder.loadTexts:
    mxDebugComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-DEBUG-MIB",
    **{"mxDebugMIB": mxDebugMIB,
       "mxDebugMIBObjects": mxDebugMIBObjects,
       "mxDebugSignalingLog": mxDebugSignalingLog,
       "mxDebugSignalingLogEnable": mxDebugSignalingLogEnable,
       "mxDebugSignalingLogHost": mxDebugSignalingLogHost,
       "mxDebugSignalingLogPort": mxDebugSignalingLogPort,
       "mxDebugFax": mxDebugFax,
       "mxDebugT38OutgoingToSyslog": mxDebugT38OutgoingToSyslog,
       "mxDebugT38IncomingToSyslog": mxDebugT38IncomingToSyslog,
       "mxDebugFaxRelayForDspToSyslog": mxDebugFaxRelayForDspToSyslog,
       "mxDebugFaxRelayFromDspToSyslog": mxDebugFaxRelayFromDspToSyslog,
       "mxDebugPcmCapture": mxDebugPcmCapture,
       "mxDebugPcmCaptureEnable": mxDebugPcmCaptureEnable,
       "mxDebugPcmCaptureIpAddress": mxDebugPcmCaptureIpAddress,
       "mxDebugPcmCaptureEndpointNumber": mxDebugPcmCaptureEndpointNumber,
       "mxDebugDspStats": mxDebugDspStats,
       "mxDebugDspStatsEnable": mxDebugDspStatsEnable,
       "mxDebugDspStatsInterval": mxDebugDspStatsInterval,
       "mxDebugDspStatsFilter": mxDebugDspStatsFilter,
       "mxDebugConformance": mxDebugConformance,
       "mxDebugCompliances": mxDebugCompliances,
       "mxDebugComplVer1": mxDebugComplVer1,
       "mxDebugGroups": mxDebugGroups,
       "mxDebugSignalingLogGroupVer1": mxDebugSignalingLogGroupVer1,
       "mxDebugFaxGroupVer1": mxDebugFaxGroupVer1,
       "mxDebugPcmCaptureGroupVer1": mxDebugPcmCaptureGroupVer1}
)
