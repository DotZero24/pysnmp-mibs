# SNMP MIB module (MX-SCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:18 2025
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

scmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScmMIBObjects_ObjectIdentity = ObjectIdentity
scmMIBObjects = _ScmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1)
)
_ServicesInfoTable_Object = MibTable
servicesInfoTable = _ServicesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100)
)
if mibBuilder.loadTexts:
    servicesInfoTable.setStatus("current")
_ServicesInfoEntry_Object = MibTableRow
servicesInfoEntry = _ServicesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1)
)
servicesInfoEntry.setIndexNames(
    (0, "MX-SCM-MIB", "servicesInfoName"),
)
if mibBuilder.loadTexts:
    servicesInfoEntry.setStatus("current")
_ServicesInfoName_Type = OctetString
_ServicesInfoName_Object = MibTableColumn
servicesInfoName = _ServicesInfoName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1, 100),
    _ServicesInfoName_Type()
)
servicesInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesInfoName.setStatus("current")
_ServicesInfoId_Type = Unsigned32
_ServicesInfoId_Object = MibTableColumn
servicesInfoId = _ServicesInfoId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1, 200),
    _ServicesInfoId_Type()
)
servicesInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesInfoId.setStatus("current")


class _ServicesInfoClass_Type(Integer32):
    """Custom type servicesInfoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("system", 100),
          ("user", 200))
    )


_ServicesInfoClass_Type.__name__ = "Integer32"
_ServicesInfoClass_Object = MibTableColumn
servicesInfoClass = _ServicesInfoClass_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1, 400),
    _ServicesInfoClass_Type()
)
servicesInfoClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesInfoClass.setStatus("current")


class _ServicesInfoStartupType_Type(Integer32):
    """Custom type servicesInfoStartupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("auto", 100),
          ("manual", 200))
    )


_ServicesInfoStartupType_Type.__name__ = "Integer32"
_ServicesInfoStartupType_Object = MibTableColumn
servicesInfoStartupType = _ServicesInfoStartupType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1, 500),
    _ServicesInfoStartupType_Type()
)
servicesInfoStartupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesInfoStartupType.setStatus("current")


class _ServicesInfoExecState_Type(Integer32):
    """Custom type servicesInfoExecState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              65000)
        )
    )
    namedValues = NamedValues(
        *(("started", 100),
          ("starting", 200),
          ("stopped", 300),
          ("stopping", 400),
          ("notResponding", 65000))
    )


_ServicesInfoExecState_Type.__name__ = "Integer32"
_ServicesInfoExecState_Object = MibTableColumn
servicesInfoExecState = _ServicesInfoExecState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1, 600),
    _ServicesInfoExecState_Type()
)
servicesInfoExecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesInfoExecState.setStatus("current")


class _ServicesInfoComment_Type(OctetString):
    """Custom type servicesInfoComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServicesInfoComment_Type.__name__ = "OctetString"
_ServicesInfoComment_Object = MibTableColumn
servicesInfoComment = _ServicesInfoComment_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 100, 1, 700),
    _ServicesInfoComment_Type()
)
servicesInfoComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesInfoComment.setStatus("current")
_ServiceCommandsTable_Object = MibTable
serviceCommandsTable = _ServiceCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 200)
)
if mibBuilder.loadTexts:
    serviceCommandsTable.setStatus("current")
_ServiceCommandsEntry_Object = MibTableRow
serviceCommandsEntry = _ServiceCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 200, 1)
)
serviceCommandsEntry.setIndexNames(
    (0, "MX-SCM-MIB", "serviceCommandsName"),
)
if mibBuilder.loadTexts:
    serviceCommandsEntry.setStatus("current")
_ServiceCommandsName_Type = OctetString
_ServiceCommandsName_Object = MibTableColumn
serviceCommandsName = _ServiceCommandsName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 200, 1, 100),
    _ServiceCommandsName_Type()
)
serviceCommandsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceCommandsName.setStatus("current")


class _ServiceCommandsRestart_Type(Integer32):
    """Custom type serviceCommandsRestart based on Integer32"""
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
          ("restart", 10))
    )


_ServiceCommandsRestart_Type.__name__ = "Integer32"
_ServiceCommandsRestart_Object = MibTableColumn
serviceCommandsRestart = _ServiceCommandsRestart_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 200, 1, 200),
    _ServiceCommandsRestart_Type()
)
serviceCommandsRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceCommandsRestart.setStatus("current")


class _ServiceCommandsStop_Type(Integer32):
    """Custom type serviceCommandsStop based on Integer32"""
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
          ("stop", 10))
    )


_ServiceCommandsStop_Type.__name__ = "Integer32"
_ServiceCommandsStop_Object = MibTableColumn
serviceCommandsStop = _ServiceCommandsStop_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 200, 1, 300),
    _ServiceCommandsStop_Type()
)
serviceCommandsStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceCommandsStop.setStatus("current")


class _ServiceCommandsStart_Type(Integer32):
    """Custom type serviceCommandsStart based on Integer32"""
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
          ("start", 10))
    )


_ServiceCommandsStart_Type.__name__ = "Integer32"
_ServiceCommandsStart_Object = MibTableColumn
serviceCommandsStart = _ServiceCommandsStart_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 200, 1, 400),
    _ServiceCommandsStart_Type()
)
serviceCommandsStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceCommandsStart.setStatus("current")
_ServicesConfigTable_Object = MibTable
servicesConfigTable = _ServicesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 400)
)
if mibBuilder.loadTexts:
    servicesConfigTable.setStatus("current")
_ServicesConfigEntry_Object = MibTableRow
servicesConfigEntry = _ServicesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 400, 1)
)
servicesConfigEntry.setIndexNames(
    (0, "MX-SCM-MIB", "servicesConfigName"),
)
if mibBuilder.loadTexts:
    servicesConfigEntry.setStatus("current")
_ServicesConfigName_Type = OctetString
_ServicesConfigName_Object = MibTableColumn
servicesConfigName = _ServicesConfigName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 400, 1, 100),
    _ServicesConfigName_Type()
)
servicesConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesConfigName.setStatus("current")


class _ServicesConfigStartupType_Type(Integer32):
    """Custom type servicesConfigStartupType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("auto", 100),
          ("manual", 200))
    )


_ServicesConfigStartupType_Type.__name__ = "Integer32"
_ServicesConfigStartupType_Object = MibTableColumn
servicesConfigStartupType = _ServicesConfigStartupType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 400, 1, 200),
    _ServicesConfigStartupType_Type()
)
servicesConfigStartupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicesConfigStartupType.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 400, 1, 60020, 100),
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
    "MX-SCM-MIB",
    **{"scmMIB": scmMIB,
       "scmMIBObjects": scmMIBObjects,
       "servicesInfoTable": servicesInfoTable,
       "servicesInfoEntry": servicesInfoEntry,
       "servicesInfoName": servicesInfoName,
       "servicesInfoId": servicesInfoId,
       "servicesInfoClass": servicesInfoClass,
       "servicesInfoStartupType": servicesInfoStartupType,
       "servicesInfoExecState": servicesInfoExecState,
       "servicesInfoComment": servicesInfoComment,
       "serviceCommandsTable": serviceCommandsTable,
       "serviceCommandsEntry": serviceCommandsEntry,
       "serviceCommandsName": serviceCommandsName,
       "serviceCommandsRestart": serviceCommandsRestart,
       "serviceCommandsStop": serviceCommandsStop,
       "serviceCommandsStart": serviceCommandsStart,
       "servicesConfigTable": servicesConfigTable,
       "servicesConfigEntry": servicesConfigEntry,
       "servicesConfigName": servicesConfigName,
       "servicesConfigStartupType": servicesConfigStartupType,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
