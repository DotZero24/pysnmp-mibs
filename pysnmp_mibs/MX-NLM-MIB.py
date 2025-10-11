# SNMP MIB module (MX-NLM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-NLM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:57 2025
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

nlmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NlmMIBObjects_ObjectIdentity = ObjectIdentity
nlmMIBObjects = _NlmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1)
)
_SyslogGroup_ObjectIdentity = ObjectIdentity
syslogGroup = _SyslogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 100)
)


class _SyslogRemoteHost_Type(MxIpHostNamePort):
    """Custom type syslogRemoteHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_SyslogRemoteHost_Type.__name__ = "MxIpHostNamePort"
_SyslogRemoteHost_Object = MibScalar
syslogRemoteHost = _SyslogRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 100, 100),
    _SyslogRemoteHost_Type()
)
syslogRemoteHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogRemoteHost.setStatus("current")


class _SyslogMessageFormat_Type(OctetString):
    """Custom type syslogMessageFormat based on OctetString"""
    defaultValue = OctetString("%servicetextkey: %serviceid-%servicename: %msgid-%message")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SyslogMessageFormat_Type.__name__ = "OctetString"
_SyslogMessageFormat_Object = MibScalar
syslogMessageFormat = _SyslogMessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 100, 200),
    _SyslogMessageFormat_Type()
)
syslogMessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMessageFormat.setStatus("current")
_EventsTable_Object = MibTable
eventsTable = _EventsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200)
)
if mibBuilder.loadTexts:
    eventsTable.setStatus("current")
_EventsEntry_Object = MibTableRow
eventsEntry = _EventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1)
)
eventsEntry.setIndexNames(
    (0, "MX-NLM-MIB", "eventsIndex"),
)
if mibBuilder.loadTexts:
    eventsEntry.setStatus("current")
_EventsIndex_Type = Unsigned32
_EventsIndex_Object = MibTableColumn
eventsIndex = _EventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 100),
    _EventsIndex_Type()
)
eventsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsIndex.setStatus("current")


class _EventsActivation_Type(MxEnableState):
    """Custom type eventsActivation based on MxEnableState"""
    defaultValue = 1


_EventsActivation_Type.__name__ = "MxEnableState"
_EventsActivation_Object = MibTableColumn
eventsActivation = _EventsActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 200),
    _EventsActivation_Type()
)
eventsActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventsActivation.setStatus("current")


class _EventsType_Type(Integer32):
    """Custom type eventsType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("notification", 100)
    )


_EventsType_Type.__name__ = "Integer32"
_EventsType_Object = MibTableColumn
eventsType = _EventsType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 300),
    _EventsType_Type()
)
eventsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventsType.setStatus("current")


class _EventsCriteria_Type(OctetString):
    """Custom type eventsCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EventsCriteria_Type.__name__ = "OctetString"
_EventsCriteria_Object = MibTableColumn
eventsCriteria = _EventsCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 400),
    _EventsCriteria_Type()
)
eventsCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventsCriteria.setStatus("current")


class _EventsAction_Type(Integer32):
    """Custom type eventsAction based on Integer32"""
    defaultValue = 100

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
        *(("sendViaSyslog", 100),
          ("sendViaSip", 200),
          ("logLocally", 300),
          ("logToFile", 400))
    )


_EventsAction_Type.__name__ = "Integer32"
_EventsAction_Object = MibTableColumn
eventsAction = _EventsAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 500),
    _EventsAction_Type()
)
eventsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventsAction.setStatus("current")


class _EventsConfigStatus_Type(Integer32):
    """Custom type eventsConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("invalid", 200),
          ("notSupported", 300))
    )


_EventsConfigStatus_Type.__name__ = "Integer32"
_EventsConfigStatus_Object = MibTableColumn
eventsConfigStatus = _EventsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 600),
    _EventsConfigStatus_Type()
)
eventsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsConfigStatus.setStatus("current")


class _EventsDelete_Type(Integer32):
    """Custom type eventsDelete based on Integer32"""
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


_EventsDelete_Type.__name__ = "Integer32"
_EventsDelete_Object = MibTableColumn
eventsDelete = _EventsDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 200, 1, 10000),
    _EventsDelete_Type()
)
eventsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventsDelete.setStatus("current")
_LocalLogGroup_ObjectIdentity = ObjectIdentity
localLogGroup = _LocalLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300)
)
_LocalLogMaxNbEntries_Type = Unsigned32
_LocalLogMaxNbEntries_Object = MibScalar
localLogMaxNbEntries = _LocalLogMaxNbEntries_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 100),
    _LocalLogMaxNbEntries_Type()
)
localLogMaxNbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMaxNbEntries.setStatus("current")
_LocalLogNbErrorEntries_Type = Unsigned32
_LocalLogNbErrorEntries_Object = MibScalar
localLogNbErrorEntries = _LocalLogNbErrorEntries_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 200),
    _LocalLogNbErrorEntries_Type()
)
localLogNbErrorEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogNbErrorEntries.setStatus("current")
_LocalLogNbCriticalEntries_Type = Unsigned32
_LocalLogNbCriticalEntries_Object = MibScalar
localLogNbCriticalEntries = _LocalLogNbCriticalEntries_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 300),
    _LocalLogNbCriticalEntries_Type()
)
localLogNbCriticalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogNbCriticalEntries.setStatus("current")
_LocalLogMessagesTable_Object = MibTable
localLogMessagesTable = _LocalLogMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500)
)
if mibBuilder.loadTexts:
    localLogMessagesTable.setStatus("current")
_LocalLogMessagesEntry_Object = MibTableRow
localLogMessagesEntry = _LocalLogMessagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1)
)
localLogMessagesEntry.setIndexNames(
    (0, "MX-NLM-MIB", "localLogMessagesIndex"),
)
if mibBuilder.loadTexts:
    localLogMessagesEntry.setStatus("current")
_LocalLogMessagesIndex_Type = Unsigned32
_LocalLogMessagesIndex_Object = MibTableColumn
localLogMessagesIndex = _LocalLogMessagesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 100),
    _LocalLogMessagesIndex_Type()
)
localLogMessagesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesIndex.setStatus("current")
_LocalLogMessagesLocalTime_Type = OctetString
_LocalLogMessagesLocalTime_Object = MibTableColumn
localLogMessagesLocalTime = _LocalLogMessagesLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 200),
    _LocalLogMessagesLocalTime_Type()
)
localLogMessagesLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesLocalTime.setStatus("current")
_LocalLogMessagesServiceNumkey_Type = Unsigned32
_LocalLogMessagesServiceNumkey_Object = MibTableColumn
localLogMessagesServiceNumkey = _LocalLogMessagesServiceNumkey_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 300),
    _LocalLogMessagesServiceNumkey_Type()
)
localLogMessagesServiceNumkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesServiceNumkey.setStatus("current")
_LocalLogMessagesNotificationId_Type = Unsigned32
_LocalLogMessagesNotificationId_Object = MibTableColumn
localLogMessagesNotificationId = _LocalLogMessagesNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 400),
    _LocalLogMessagesNotificationId_Type()
)
localLogMessagesNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesNotificationId.setStatus("current")


class _LocalLogMessagesSeverity_Type(Integer32):
    """Custom type localLogMessagesSeverity based on Integer32"""
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
        *(("debug", 100),
          ("information", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_LocalLogMessagesSeverity_Type.__name__ = "Integer32"
_LocalLogMessagesSeverity_Object = MibTableColumn
localLogMessagesSeverity = _LocalLogMessagesSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 500),
    _LocalLogMessagesSeverity_Type()
)
localLogMessagesSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesSeverity.setStatus("current")
_LocalLogMessagesServiceTextkey_Type = OctetString
_LocalLogMessagesServiceTextkey_Object = MibTableColumn
localLogMessagesServiceTextkey = _LocalLogMessagesServiceTextkey_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 600),
    _LocalLogMessagesServiceTextkey_Type()
)
localLogMessagesServiceTextkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesServiceTextkey.setStatus("current")
_LocalLogMessagesMessage_Type = OctetString
_LocalLogMessagesMessage_Object = MibTableColumn
localLogMessagesMessage = _LocalLogMessagesMessage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 300, 500, 1, 700),
    _LocalLogMessagesMessage_Type()
)
localLogMessagesMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localLogMessagesMessage.setStatus("current")
_LogFileGroup_ObjectIdentity = ObjectIdentity
logFileGroup = _LogFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 400)
)


class _LogFileBaseName_Type(OctetString):
    """Custom type logFileBaseName based on OctetString"""
    defaultValue = OctetString("Notifications")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LogFileBaseName_Type.__name__ = "OctetString"
_LogFileBaseName_Object = MibScalar
logFileBaseName = _LogFileBaseName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 400, 100),
    _LogFileBaseName_Type()
)
logFileBaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logFileBaseName.setStatus("current")


class _LogFileMaxSize_Type(Unsigned32):
    """Custom type logFileMaxSize based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_LogFileMaxSize_Type.__name__ = "Unsigned32"
_LogFileMaxSize_Object = MibScalar
logFileMaxSize = _LogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 400, 200),
    _LogFileMaxSize_Type()
)
logFileMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logFileMaxSize.setStatus("current")


class _LogFileMaxNb_Type(Unsigned32):
    """Custom type logFileMaxNb based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LogFileMaxNb_Type.__name__ = "Unsigned32"
_LogFileMaxNb_Object = MibScalar
logFileMaxNb = _LogFileMaxNb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 400, 300),
    _LogFileMaxNb_Type()
)
logFileMaxNb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logFileMaxNb.setStatus("current")
_PCaptureGroup_ObjectIdentity = ObjectIdentity
pCaptureGroup = _PCaptureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500)
)


class _PCaptureState_Type(Integer32):
    """Custom type pCaptureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("requested", 200),
          ("completed", 300),
          ("undefinedFailure", 400),
          ("urlFailure", 500),
          ("filterFailure", 600),
          ("authenticationFailure", 700),
          ("hostUnreachableFailure", 800),
          ("tlsCertificateFailure", 900),
          ("sizeLimitFailure", 1000),
          ("linkFailure", 1100))
    )


_PCaptureState_Type.__name__ = "Integer32"
_PCaptureState_Object = MibScalar
pCaptureState = _PCaptureState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 100),
    _PCaptureState_Type()
)
pCaptureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCaptureState.setStatus("current")


class _PCaptureNbFrames_Type(Unsigned32):
    """Custom type pCaptureNbFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_PCaptureNbFrames_Type.__name__ = "Unsigned32"
_PCaptureNbFrames_Object = MibScalar
pCaptureNbFrames = _PCaptureNbFrames_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 200),
    _PCaptureNbFrames_Type()
)
pCaptureNbFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureNbFrames.setStatus("current")


class _PCaptureNbSecs_Type(Unsigned32):
    """Custom type pCaptureNbSecs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2678400),
    )


_PCaptureNbSecs_Type.__name__ = "Unsigned32"
_PCaptureNbSecs_Object = MibScalar
pCaptureNbSecs = _PCaptureNbSecs_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 300),
    _PCaptureNbSecs_Type()
)
pCaptureNbSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureNbSecs.setStatus("current")


class _PCaptureFilter_Type(OctetString):
    """Custom type pCaptureFilter based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PCaptureFilter_Type.__name__ = "OctetString"
_PCaptureFilter_Object = MibScalar
pCaptureFilter = _PCaptureFilter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 400),
    _PCaptureFilter_Type()
)
pCaptureFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureFilter.setStatus("current")


class _PCaptureFileUrl_Type(OctetString):
    """Custom type pCaptureFileUrl based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PCaptureFileUrl_Type.__name__ = "OctetString"
_PCaptureFileUrl_Object = MibScalar
pCaptureFileUrl = _PCaptureFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 500),
    _PCaptureFileUrl_Type()
)
pCaptureFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureFileUrl.setStatus("current")


class _PCaptureLinkName_Type(OctetString):
    """Custom type pCaptureLinkName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_PCaptureLinkName_Type.__name__ = "OctetString"
_PCaptureLinkName_Object = MibScalar
pCaptureLinkName = _PCaptureLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 550),
    _PCaptureLinkName_Type()
)
pCaptureLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureLinkName.setStatus("current")
_PCaptureTransferGroup_ObjectIdentity = ObjectIdentity
pCaptureTransferGroup = _PCaptureTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 800)
)


class _PCaptureTransferCertificateValidation_Type(Integer32):
    """Custom type pCaptureTransferCertificateValidation based on Integer32"""
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


_PCaptureTransferCertificateValidation_Type.__name__ = "Integer32"
_PCaptureTransferCertificateValidation_Object = MibScalar
pCaptureTransferCertificateValidation = _PCaptureTransferCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 800, 100),
    _PCaptureTransferCertificateValidation_Type()
)
pCaptureTransferCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureTransferCertificateValidation.setStatus("current")


class _PCaptureTransferCertificateTrustLevel_Type(Integer32):
    """Custom type pCaptureTransferCertificateTrustLevel based on Integer32"""
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


_PCaptureTransferCertificateTrustLevel_Type.__name__ = "Integer32"
_PCaptureTransferCertificateTrustLevel_Object = MibScalar
pCaptureTransferCertificateTrustLevel = _PCaptureTransferCertificateTrustLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 800, 200),
    _PCaptureTransferCertificateTrustLevel_Type()
)
pCaptureTransferCertificateTrustLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureTransferCertificateTrustLevel.setStatus("current")


class _PCaptureTransferCipherSuite_Type(Integer32):
    """Custom type pCaptureTransferCipherSuite based on Integer32"""
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


_PCaptureTransferCipherSuite_Type.__name__ = "Integer32"
_PCaptureTransferCipherSuite_Object = MibScalar
pCaptureTransferCipherSuite = _PCaptureTransferCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 800, 300),
    _PCaptureTransferCipherSuite_Type()
)
pCaptureTransferCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureTransferCipherSuite.setStatus("current")


class _PCaptureTransferTlsVersion_Type(Integer32):
    """Custom type pCaptureTransferTlsVersion based on Integer32"""
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


_PCaptureTransferTlsVersion_Type.__name__ = "Integer32"
_PCaptureTransferTlsVersion_Object = MibScalar
pCaptureTransferTlsVersion = _PCaptureTransferTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 500, 800, 400),
    _PCaptureTransferTlsVersion_Type()
)
pCaptureTransferTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCaptureTransferTlsVersion.setStatus("current")
_DiagLogGroup_ObjectIdentity = ObjectIdentity
diagLogGroup = _DiagLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 600)
)


class _DiagLogAutomaticDump_Type(MxEnableState):
    """Custom type diagLogAutomaticDump based on MxEnableState"""
    defaultValue = 1


_DiagLogAutomaticDump_Type.__name__ = "MxEnableState"
_DiagLogAutomaticDump_Object = MibScalar
diagLogAutomaticDump = _DiagLogAutomaticDump_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 600, 100),
    _DiagLogAutomaticDump_Type()
)
diagLogAutomaticDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagLogAutomaticDump.setStatus("current")
_TacGroup_ObjectIdentity = ObjectIdentity
tacGroup = _TacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 10000)
)


class _DiagnosticTracesEnable_Type(MxEnableState):
    """Custom type diagnosticTracesEnable based on MxEnableState"""
    defaultValue = 0


_DiagnosticTracesEnable_Type.__name__ = "MxEnableState"
_DiagnosticTracesEnable_Object = MibScalar
diagnosticTracesEnable = _DiagnosticTracesEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 10000, 100),
    _DiagnosticTracesEnable_Type()
)
diagnosticTracesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagnosticTracesEnable.setStatus("current")


class _DiagnosticTracesFilter_Type(OctetString):
    """Custom type diagnosticTracesFilter based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DiagnosticTracesFilter_Type.__name__ = "OctetString"
_DiagnosticTracesFilter_Object = MibScalar
diagnosticTracesFilter = _DiagnosticTracesFilter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 10000, 200),
    _DiagnosticTracesFilter_Type()
)
diagnosticTracesFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagnosticTracesFilter.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1100, 1, 60020, 100),
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
    "MX-NLM-MIB",
    **{"nlmMIB": nlmMIB,
       "nlmMIBObjects": nlmMIBObjects,
       "syslogGroup": syslogGroup,
       "syslogRemoteHost": syslogRemoteHost,
       "syslogMessageFormat": syslogMessageFormat,
       "eventsTable": eventsTable,
       "eventsEntry": eventsEntry,
       "eventsIndex": eventsIndex,
       "eventsActivation": eventsActivation,
       "eventsType": eventsType,
       "eventsCriteria": eventsCriteria,
       "eventsAction": eventsAction,
       "eventsConfigStatus": eventsConfigStatus,
       "eventsDelete": eventsDelete,
       "localLogGroup": localLogGroup,
       "localLogMaxNbEntries": localLogMaxNbEntries,
       "localLogNbErrorEntries": localLogNbErrorEntries,
       "localLogNbCriticalEntries": localLogNbCriticalEntries,
       "localLogMessagesTable": localLogMessagesTable,
       "localLogMessagesEntry": localLogMessagesEntry,
       "localLogMessagesIndex": localLogMessagesIndex,
       "localLogMessagesLocalTime": localLogMessagesLocalTime,
       "localLogMessagesServiceNumkey": localLogMessagesServiceNumkey,
       "localLogMessagesNotificationId": localLogMessagesNotificationId,
       "localLogMessagesSeverity": localLogMessagesSeverity,
       "localLogMessagesServiceTextkey": localLogMessagesServiceTextkey,
       "localLogMessagesMessage": localLogMessagesMessage,
       "logFileGroup": logFileGroup,
       "logFileBaseName": logFileBaseName,
       "logFileMaxSize": logFileMaxSize,
       "logFileMaxNb": logFileMaxNb,
       "pCaptureGroup": pCaptureGroup,
       "pCaptureState": pCaptureState,
       "pCaptureNbFrames": pCaptureNbFrames,
       "pCaptureNbSecs": pCaptureNbSecs,
       "pCaptureFilter": pCaptureFilter,
       "pCaptureFileUrl": pCaptureFileUrl,
       "pCaptureLinkName": pCaptureLinkName,
       "pCaptureTransferGroup": pCaptureTransferGroup,
       "pCaptureTransferCertificateValidation": pCaptureTransferCertificateValidation,
       "pCaptureTransferCertificateTrustLevel": pCaptureTransferCertificateTrustLevel,
       "pCaptureTransferCipherSuite": pCaptureTransferCipherSuite,
       "pCaptureTransferTlsVersion": pCaptureTransferTlsVersion,
       "diagLogGroup": diagLogGroup,
       "diagLogAutomaticDump": diagLogAutomaticDump,
       "tacGroup": tacGroup,
       "diagnosticTracesEnable": diagnosticTracesEnable,
       "diagnosticTracesFilter": diagnosticTracesFilter,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
