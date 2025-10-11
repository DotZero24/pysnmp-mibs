# SNMP MIB module (DLINKPRIME-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:07 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(SyslogFacility,
 SyslogSeverity) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogFacility",
    "SyslogSeverity")


# MODULE-IDENTITY

dlinkPrimeSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21)
)
if mibBuilder.loadTexts:
    dlinkPrimeSyslogMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpSyslogMIBNotifications_ObjectIdentity = ObjectIdentity
dpSyslogMIBNotifications = _DpSyslogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 0)
)
_DpSyslogMIBObjects_ObjectIdentity = ObjectIdentity
dpSyslogMIBObjects = _DpSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1)
)
_DpSyslogGeneral_ObjectIdentity = ObjectIdentity
dpSyslogGeneral = _DpSyslogGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 1)
)
_DpSyslogLogOnEnabled_Type = TruthValue
_DpSyslogLogOnEnabled_Object = MibScalar
dpSyslogLogOnEnabled = _DpSyslogLogOnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 1, 1),
    _DpSyslogLogOnEnabled_Type()
)
dpSyslogLogOnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogLogOnEnabled.setStatus("current")
_DpSyslogLogbuffer_ObjectIdentity = ObjectIdentity
dpSyslogLogbuffer = _DpSyslogLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 2)
)
if mibBuilder.loadTexts:
    dpSyslogLogbuffer.setStatus("current")


class _DpSyslogClearLogBuffer_Type(Integer32):
    """Custom type dpSyslogClearLogBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DpSyslogClearLogBuffer_Type.__name__ = "Integer32"
_DpSyslogClearLogBuffer_Object = MibScalar
dpSyslogClearLogBuffer = _DpSyslogClearLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 2, 1),
    _DpSyslogClearLogBuffer_Type()
)
dpSyslogClearLogBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogClearLogBuffer.setStatus("current")
_DpSyslogLogBufferEnabled_Type = TruthValue
_DpSyslogLogBufferEnabled_Object = MibScalar
dpSyslogLogBufferEnabled = _DpSyslogLogBufferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 2, 2),
    _DpSyslogLogBufferEnabled_Type()
)
dpSyslogLogBufferEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogLogBufferEnabled.setStatus("current")
_DpSyslogServer_ObjectIdentity = ObjectIdentity
dpSyslogServer = _DpSyslogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 3)
)
_DpSyslogServerAddress_Type = IpAddress
_DpSyslogServerAddress_Object = MibScalar
dpSyslogServerAddress = _DpSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 3, 1),
    _DpSyslogServerAddress_Type()
)
dpSyslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogServerAddress.setStatus("current")


class _DpSyslogServerPort_Type(Unsigned32):
    """Custom type dpSyslogServerPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(1024, 65535),
    )


_DpSyslogServerPort_Type.__name__ = "Unsigned32"
_DpSyslogServerPort_Object = MibScalar
dpSyslogServerPort = _DpSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 3, 2),
    _DpSyslogServerPort_Type()
)
dpSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogServerPort.setStatus("current")


class _DpSyslogServerSeverity_Type(Integer32):
    """Custom type dpSyslogServerSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("informational", 2),
          ("all", 3))
    )


_DpSyslogServerSeverity_Type.__name__ = "Integer32"
_DpSyslogServerSeverity_Object = MibScalar
dpSyslogServerSeverity = _DpSyslogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 3, 3),
    _DpSyslogServerSeverity_Type()
)
dpSyslogServerSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogServerSeverity.setStatus("current")


class _DpSyslogServerFacility_Type(Integer32):
    """Custom type dpSyslogServerFacility based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local_0", 0),
          ("local_1", 1),
          ("local_2", 2),
          ("local_3", 3),
          ("local_4", 4),
          ("local_5", 5),
          ("local_6", 6),
          ("local_7", 7))
    )


_DpSyslogServerFacility_Type.__name__ = "Integer32"
_DpSyslogServerFacility_Object = MibScalar
dpSyslogServerFacility = _DpSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 3, 4),
    _DpSyslogServerFacility_Type()
)
dpSyslogServerFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSyslogServerFacility.setStatus("current")
_DpSyslogBufferTableNum_Type = Unsigned32
_DpSyslogBufferTableNum_Object = MibScalar
dpSyslogBufferTableNum = _DpSyslogBufferTableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 4),
    _DpSyslogBufferTableNum_Type()
)
dpSyslogBufferTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpSyslogBufferTableNum.setStatus("current")
_DpSyslogBufferTable_Object = MibTable
dpSyslogBufferTable = _DpSyslogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 5)
)
if mibBuilder.loadTexts:
    dpSyslogBufferTable.setStatus("current")
_DpSyslogBufferEntry_Object = MibTableRow
dpSyslogBufferEntry = _DpSyslogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 5, 1)
)
dpSyslogBufferEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpSyslogBufferEntry.setStatus("current")
_DpSyslogBufferLevel_Type = DisplayString
_DpSyslogBufferLevel_Object = MibTableColumn
dpSyslogBufferLevel = _DpSyslogBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 5, 1, 1),
    _DpSyslogBufferLevel_Type()
)
dpSyslogBufferLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpSyslogBufferLevel.setStatus("current")
_DpSyslogBufferDateAndTime_Type = DisplayString
_DpSyslogBufferDateAndTime_Object = MibTableColumn
dpSyslogBufferDateAndTime = _DpSyslogBufferDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 5, 1, 2),
    _DpSyslogBufferDateAndTime_Type()
)
dpSyslogBufferDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpSyslogBufferDateAndTime.setStatus("current")
_DpSyslogBufferDescription_Type = DisplayString
_DpSyslogBufferDescription_Object = MibTableColumn
dpSyslogBufferDescription = _DpSyslogBufferDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 1, 5, 1, 3),
    _DpSyslogBufferDescription_Type()
)
dpSyslogBufferDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpSyslogBufferDescription.setStatus("current")
_DpSyslogMIBConformance_ObjectIdentity = ObjectIdentity
dpSyslogMIBConformance = _DpSyslogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 2)
)
_DpSyslogMIBCompliances_ObjectIdentity = ObjectIdentity
dpSyslogMIBCompliances = _DpSyslogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 2, 1)
)
_DpSyslogMIBGroups_ObjectIdentity = ObjectIdentity
dpSyslogMIBGroups = _DpSyslogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 2, 1, 2)
)

# Managed Objects groups

dpSyslogGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 2, 1, 2, 1)
)
dpSyslogGeneralGroup.setObjects(
      *(("DLINKPRIME-SYSLOG-MIB", "dpSyslogClearLogBuffer"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogLogBufferEnabled"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogBufferTableNum"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogBufferDateAndTime"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogBufferDescription"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogLogOnEnabled"))
)
if mibBuilder.loadTexts:
    dpSyslogGeneralGroup.setStatus("current")

dpSyslogLogServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 2, 1, 2, 2)
)
dpSyslogLogServerGroup.setObjects(
      *(("DLINKPRIME-SYSLOG-MIB", "dpSyslogServerPort"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogServerSeverity"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogServerFacility"))
)
if mibBuilder.loadTexts:
    dpSyslogLogServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpSyslogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 21, 2, 1, 1)
)
dpSyslogMIBCompliance.setObjects(
      *(("DLINKPRIME-SYSLOG-MIB", "dpSyslogGeneralGroup"),
        ("DLINKPRIME-SYSLOG-MIB", "dpSyslogLogServerGroup"))
)
if mibBuilder.loadTexts:
    dpSyslogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SYSLOG-MIB",
    **{"dlinkPrimeSyslogMIB": dlinkPrimeSyslogMIB,
       "dpSyslogMIBNotifications": dpSyslogMIBNotifications,
       "dpSyslogMIBObjects": dpSyslogMIBObjects,
       "dpSyslogGeneral": dpSyslogGeneral,
       "dpSyslogLogOnEnabled": dpSyslogLogOnEnabled,
       "dpSyslogLogbuffer": dpSyslogLogbuffer,
       "dpSyslogClearLogBuffer": dpSyslogClearLogBuffer,
       "dpSyslogLogBufferEnabled": dpSyslogLogBufferEnabled,
       "dpSyslogServer": dpSyslogServer,
       "dpSyslogServerAddress": dpSyslogServerAddress,
       "dpSyslogServerPort": dpSyslogServerPort,
       "dpSyslogServerSeverity": dpSyslogServerSeverity,
       "dpSyslogServerFacility": dpSyslogServerFacility,
       "dpSyslogBufferTableNum": dpSyslogBufferTableNum,
       "dpSyslogBufferTable": dpSyslogBufferTable,
       "dpSyslogBufferEntry": dpSyslogBufferEntry,
       "dpSyslogBufferLevel": dpSyslogBufferLevel,
       "dpSyslogBufferDateAndTime": dpSyslogBufferDateAndTime,
       "dpSyslogBufferDescription": dpSyslogBufferDescription,
       "dpSyslogMIBConformance": dpSyslogMIBConformance,
       "dpSyslogMIBCompliances": dpSyslogMIBCompliances,
       "dpSyslogMIBCompliance": dpSyslogMIBCompliance,
       "dpSyslogMIBGroups": dpSyslogMIBGroups,
       "dpSyslogGeneralGroup": dpSyslogGeneralGroup,
       "dpSyslogLogServerGroup": dpSyslogLogServerGroup}
)
