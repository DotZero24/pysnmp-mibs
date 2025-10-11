# SNMP MIB module (RAISECOM-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:47 2025
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

(optSysMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "optSysMgmt")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

raisecomNotifisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcNotifsConfObjects_ObjectIdentity = ObjectIdentity
rcNotifsConfObjects = _RcNotifsConfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1)
)


class _RcNotifsTrapVersion_Type(Integer32):
    """Custom type rcNotifsTrapVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2))
    )


_RcNotifsTrapVersion_Type.__name__ = "Integer32"
_RcNotifsTrapVersion_Object = MibScalar
rcNotifsTrapVersion = _RcNotifsTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 1),
    _RcNotifsTrapVersion_Type()
)
rcNotifsTrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapVersion.setStatus("current")


class _RcNotifsTrapEnable_Type(TruthValue):
    """Custom type rcNotifsTrapEnable based on TruthValue"""
    defaultValue = 1


_RcNotifsTrapEnable_Type.__name__ = "TruthValue"
_RcNotifsTrapEnable_Object = MibScalar
rcNotifsTrapEnable = _RcNotifsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 3),
    _RcNotifsTrapEnable_Type()
)
rcNotifsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapEnable.setStatus("current")
_RcNotifsTrapTotalNumber_Type = Integer32
_RcNotifsTrapTotalNumber_Object = MibScalar
rcNotifsTrapTotalNumber = _RcNotifsTrapTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 5),
    _RcNotifsTrapTotalNumber_Type()
)
rcNotifsTrapTotalNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapTotalNumber.setStatus("current")
_RcNotifsTrapLocation_Type = DisplayString
_RcNotifsTrapLocation_Object = MibScalar
rcNotifsTrapLocation = _RcNotifsTrapLocation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 6),
    _RcNotifsTrapLocation_Type()
)
rcNotifsTrapLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapLocation.setStatus("current")


class _RcNotifsTrapFilterSwitch_Type(Integer32):
    """Custom type rcNotifsTrapFilterSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("locked_off", 3))
    )


_RcNotifsTrapFilterSwitch_Type.__name__ = "Integer32"
_RcNotifsTrapFilterSwitch_Object = MibScalar
rcNotifsTrapFilterSwitch = _RcNotifsTrapFilterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 7),
    _RcNotifsTrapFilterSwitch_Type()
)
rcNotifsTrapFilterSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapFilterSwitch.setStatus("current")
_RcNotifsAlarmOutputGroup_Type = Integer32
_RcNotifsAlarmOutputGroup_Object = MibScalar
rcNotifsAlarmOutputGroup = _RcNotifsAlarmOutputGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 8),
    _RcNotifsAlarmOutputGroup_Type()
)
rcNotifsAlarmOutputGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsAlarmOutputGroup.setStatus("current")
_RcNotifsTrapSinkTable_Object = MibTable
rcNotifsTrapSinkTable = _RcNotifsTrapSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    rcNotifsTrapSinkTable.setStatus("current")
_RcNotifsTrapSinkEntry_Object = MibTableRow
rcNotifsTrapSinkEntry = _RcNotifsTrapSinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 10, 1)
)
rcNotifsTrapSinkEntry.setIndexNames(
    (0, "RAISECOM-NOTIFICATION-MIB", "rcNotifsTrapIndex"),
)
if mibBuilder.loadTexts:
    rcNotifsTrapSinkEntry.setStatus("current")


class _RcNotifsTrapIndex_Type(Integer32):
    """Custom type rcNotifsTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcNotifsTrapIndex_Type.__name__ = "Integer32"
_RcNotifsTrapIndex_Object = MibTableColumn
rcNotifsTrapIndex = _RcNotifsTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 10, 1, 1),
    _RcNotifsTrapIndex_Type()
)
rcNotifsTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapIndex.setStatus("current")
_RcNotifsTrapTarget_Type = IpAddress
_RcNotifsTrapTarget_Object = MibTableColumn
rcNotifsTrapTarget = _RcNotifsTrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 10, 1, 2),
    _RcNotifsTrapTarget_Type()
)
rcNotifsTrapTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapTarget.setStatus("current")


class _RcNotifsTrapPort_Type(Integer32):
    """Custom type rcNotifsTrapPort based on Integer32"""
    defaultValue = 162


_RcNotifsTrapPort_Type.__name__ = "Integer32"
_RcNotifsTrapPort_Object = MibTableColumn
rcNotifsTrapPort = _RcNotifsTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 10, 1, 3),
    _RcNotifsTrapPort_Type()
)
rcNotifsTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapPort.setStatus("current")
_RcNotifsAlarmFilterTable_Object = MibTable
rcNotifsAlarmFilterTable = _RcNotifsAlarmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11)
)
if mibBuilder.loadTexts:
    rcNotifsAlarmFilterTable.setStatus("current")
_RcNotifsAlarmFilterEntry_Object = MibTableRow
rcNotifsAlarmFilterEntry = _RcNotifsAlarmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1)
)
rcNotifsAlarmFilterEntry.setIndexNames(
    (1, "RAISECOM-NOTIFICATION-MIB", "rcNotifsFilterAlarmTrapOID"),
)
if mibBuilder.loadTexts:
    rcNotifsAlarmFilterEntry.setStatus("current")
_RcNotifsFilterAlarmTrapOID_Type = ObjectIdentifier
_RcNotifsFilterAlarmTrapOID_Object = MibTableColumn
rcNotifsFilterAlarmTrapOID = _RcNotifsFilterAlarmTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1, 1),
    _RcNotifsFilterAlarmTrapOID_Type()
)
rcNotifsFilterAlarmTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsFilterAlarmTrapOID.setStatus("current")


class _RcNotifsAlarmTrapEnable_Type(TruthValue):
    """Custom type rcNotifsAlarmTrapEnable based on TruthValue"""
    defaultValue = 1


_RcNotifsAlarmTrapEnable_Type.__name__ = "TruthValue"
_RcNotifsAlarmTrapEnable_Object = MibTableColumn
rcNotifsAlarmTrapEnable = _RcNotifsAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1, 2),
    _RcNotifsAlarmTrapEnable_Type()
)
rcNotifsAlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmTrapEnable.setStatus("current")


class _RcNotifsAlarmTrapLogEnable_Type(TruthValue):
    """Custom type rcNotifsAlarmTrapLogEnable based on TruthValue"""
    defaultValue = 1


_RcNotifsAlarmTrapLogEnable_Type.__name__ = "TruthValue"
_RcNotifsAlarmTrapLogEnable_Object = MibTableColumn
rcNotifsAlarmTrapLogEnable = _RcNotifsAlarmTrapLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1, 3),
    _RcNotifsAlarmTrapLogEnable_Type()
)
rcNotifsAlarmTrapLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmTrapLogEnable.setStatus("current")


class _RcNotifsAlarmFilterControl_Type(TruthValue):
    """Custom type rcNotifsAlarmFilterControl based on TruthValue"""
    defaultValue = 1


_RcNotifsAlarmFilterControl_Type.__name__ = "TruthValue"
_RcNotifsAlarmFilterControl_Object = MibTableColumn
rcNotifsAlarmFilterControl = _RcNotifsAlarmFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1, 4),
    _RcNotifsAlarmFilterControl_Type()
)
rcNotifsAlarmFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmFilterControl.setStatus("current")


class _RcNotifsAlarmOutputEnable_Type(Integer32):
    """Custom type rcNotifsAlarmOutputEnable based on Integer32"""
    defaultValue = 0


_RcNotifsAlarmOutputEnable_Type.__name__ = "Integer32"
_RcNotifsAlarmOutputEnable_Object = MibTableColumn
rcNotifsAlarmOutputEnable = _RcNotifsAlarmOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1, 5),
    _RcNotifsAlarmOutputEnable_Type()
)
rcNotifsAlarmOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmOutputEnable.setStatus("current")


class _RcNotifsAlarmMonitoringDisable_Type(TruthValue):
    """Custom type rcNotifsAlarmMonitoringDisable based on TruthValue"""
    defaultValue = 2


_RcNotifsAlarmMonitoringDisable_Type.__name__ = "TruthValue"
_RcNotifsAlarmMonitoringDisable_Object = MibTableColumn
rcNotifsAlarmMonitoringDisable = _RcNotifsAlarmMonitoringDisable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 11, 1, 6),
    _RcNotifsAlarmMonitoringDisable_Type()
)
rcNotifsAlarmMonitoringDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmMonitoringDisable.setStatus("current")
_RcNotifsPortFilterConfig_ObjectIdentity = ObjectIdentity
rcNotifsPortFilterConfig = _RcNotifsPortFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15)
)
_RcNotifsPortFilterIndexNext_Type = Integer32
_RcNotifsPortFilterIndexNext_Object = MibScalar
rcNotifsPortFilterIndexNext = _RcNotifsPortFilterIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15, 1),
    _RcNotifsPortFilterIndexNext_Type()
)
rcNotifsPortFilterIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsPortFilterIndexNext.setStatus("current")
_RcNotifsPortFilterTable_Object = MibTable
rcNotifsPortFilterTable = _RcNotifsPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15, 2)
)
if mibBuilder.loadTexts:
    rcNotifsPortFilterTable.setStatus("current")
_RcNotifsPortFilterEntry_Object = MibTableRow
rcNotifsPortFilterEntry = _RcNotifsPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15, 2, 1)
)
rcNotifsPortFilterEntry.setIndexNames(
    (0, "RAISECOM-NOTIFICATION-MIB", "rcNotifsPortFilterIndex"),
)
if mibBuilder.loadTexts:
    rcNotifsPortFilterEntry.setStatus("current")
_RcNotifsPortFilterIndex_Type = Integer32
_RcNotifsPortFilterIndex_Object = MibTableColumn
rcNotifsPortFilterIndex = _RcNotifsPortFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15, 2, 1, 1),
    _RcNotifsPortFilterIndex_Type()
)
rcNotifsPortFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsPortFilterIndex.setStatus("current")
_RcNotifsPortIfIndex_Type = Integer32
_RcNotifsPortIfIndex_Object = MibTableColumn
rcNotifsPortIfIndex = _RcNotifsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15, 2, 1, 2),
    _RcNotifsPortIfIndex_Type()
)
rcNotifsPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortIfIndex.setStatus("current")
_RcNotifsPortFilterRowStatus_Type = RowStatus
_RcNotifsPortFilterRowStatus_Object = MibTableColumn
rcNotifsPortFilterRowStatus = _RcNotifsPortFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 15, 2, 1, 3),
    _RcNotifsPortFilterRowStatus_Type()
)
rcNotifsPortFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortFilterRowStatus.setStatus("current")


class _RcNotifsTrapPhysicalID_Type(OctetString):
    """Custom type rcNotifsTrapPhysicalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RcNotifsTrapPhysicalID_Type.__name__ = "OctetString"
_RcNotifsTrapPhysicalID_Object = MibScalar
rcNotifsTrapPhysicalID = _RcNotifsTrapPhysicalID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 20),
    _RcNotifsTrapPhysicalID_Type()
)
rcNotifsTrapPhysicalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapPhysicalID.setStatus("current")
_RcNotifsTrapIfIndex_Type = Integer32
_RcNotifsTrapIfIndex_Object = MibScalar
rcNotifsTrapIfIndex = _RcNotifsTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 21),
    _RcNotifsTrapIfIndex_Type()
)
rcNotifsTrapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapIfIndex.setStatus("current")
_RcNotifsTrapBindVariable1_Type = Integer32
_RcNotifsTrapBindVariable1_Object = MibScalar
rcNotifsTrapBindVariable1 = _RcNotifsTrapBindVariable1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 22),
    _RcNotifsTrapBindVariable1_Type()
)
rcNotifsTrapBindVariable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapBindVariable1.setStatus("current")
_RcNotifsTrapBindVariable2_Type = Integer32
_RcNotifsTrapBindVariable2_Object = MibScalar
rcNotifsTrapBindVariable2 = _RcNotifsTrapBindVariable2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 23),
    _RcNotifsTrapBindVariable2_Type()
)
rcNotifsTrapBindVariable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapBindVariable2.setStatus("current")
_RcNotifsTrapBindVariable3_Type = Integer32
_RcNotifsTrapBindVariable3_Object = MibScalar
rcNotifsTrapBindVariable3 = _RcNotifsTrapBindVariable3_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 24),
    _RcNotifsTrapBindVariable3_Type()
)
rcNotifsTrapBindVariable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapBindVariable3.setStatus("current")
_RcNotifsTrapBindIpAddress_Type = Integer32
_RcNotifsTrapBindIpAddress_Object = MibScalar
rcNotifsTrapBindIpAddress = _RcNotifsTrapBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 25),
    _RcNotifsTrapBindIpAddress_Type()
)
rcNotifsTrapBindIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapBindIpAddress.setStatus("current")


class _RcNotifsTrapInhibitEnable_Type(Integer32):
    """Custom type rcNotifsTrapInhibitEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RcNotifsTrapInhibitEnable_Type.__name__ = "Integer32"
_RcNotifsTrapInhibitEnable_Object = MibScalar
rcNotifsTrapInhibitEnable = _RcNotifsTrapInhibitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 30),
    _RcNotifsTrapInhibitEnable_Type()
)
rcNotifsTrapInhibitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapInhibitEnable.setStatus("current")


class _RcNotifsTrapDelayEnable_Type(Integer32):
    """Custom type rcNotifsTrapDelayEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RcNotifsTrapDelayEnable_Type.__name__ = "Integer32"
_RcNotifsTrapDelayEnable_Object = MibScalar
rcNotifsTrapDelayEnable = _RcNotifsTrapDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 40),
    _RcNotifsTrapDelayEnable_Type()
)
rcNotifsTrapDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapDelayEnable.setStatus("current")
_RcNotifsTrapDelayStartingTime_Type = Integer32
_RcNotifsTrapDelayStartingTime_Object = MibScalar
rcNotifsTrapDelayStartingTime = _RcNotifsTrapDelayStartingTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 41),
    _RcNotifsTrapDelayStartingTime_Type()
)
rcNotifsTrapDelayStartingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapDelayStartingTime.setStatus("current")
_RcNotifsTrapDelayEndTime_Type = Integer32
_RcNotifsTrapDelayEndTime_Object = MibScalar
rcNotifsTrapDelayEndTime = _RcNotifsTrapDelayEndTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 42),
    _RcNotifsTrapDelayEndTime_Type()
)
rcNotifsTrapDelayEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapDelayEndTime.setStatus("current")


class _RcNotifsTrapAutoSaveEnable_Type(Integer32):
    """Custom type rcNotifsTrapAutoSaveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RcNotifsTrapAutoSaveEnable_Type.__name__ = "Integer32"
_RcNotifsTrapAutoSaveEnable_Object = MibScalar
rcNotifsTrapAutoSaveEnable = _RcNotifsTrapAutoSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 45),
    _RcNotifsTrapAutoSaveEnable_Type()
)
rcNotifsTrapAutoSaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapAutoSaveEnable.setStatus("current")
_RcNotifsPortAlarmFilterConfig_ObjectIdentity = ObjectIdentity
rcNotifsPortAlarmFilterConfig = _RcNotifsPortAlarmFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60)
)
_RcNotifsPortAlarmFilterTableSize_Type = Integer32
_RcNotifsPortAlarmFilterTableSize_Object = MibScalar
rcNotifsPortAlarmFilterTableSize = _RcNotifsPortAlarmFilterTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 10),
    _RcNotifsPortAlarmFilterTableSize_Type()
)
rcNotifsPortAlarmFilterTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterTableSize.setStatus("current")
_RcNotifsPortAlarmFilterTable_Object = MibTable
rcNotifsPortAlarmFilterTable = _RcNotifsPortAlarmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11)
)
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterTable.setStatus("current")
_RcNotifsPortAlarmFilterEntry_Object = MibTableRow
rcNotifsPortAlarmFilterEntry = _RcNotifsPortAlarmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11, 1)
)
rcNotifsPortAlarmFilterEntry.setIndexNames(
    (0, "RAISECOM-NOTIFICATION-MIB", "rcNotifsPortAlarmFilterPhysicalID"),
    (0, "RAISECOM-NOTIFICATION-MIB", "rcNotifsPortAlarmFilterIfIndex"),
)
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterEntry.setStatus("current")


class _RcNotifsPortAlarmFilterPhysicalID_Type(OctetString):
    """Custom type rcNotifsPortAlarmFilterPhysicalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RcNotifsPortAlarmFilterPhysicalID_Type.__name__ = "OctetString"
_RcNotifsPortAlarmFilterPhysicalID_Object = MibTableColumn
rcNotifsPortAlarmFilterPhysicalID = _RcNotifsPortAlarmFilterPhysicalID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11, 1, 1),
    _RcNotifsPortAlarmFilterPhysicalID_Type()
)
rcNotifsPortAlarmFilterPhysicalID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterPhysicalID.setStatus("current")
_RcNotifsPortAlarmFilterIfIndex_Type = Integer32
_RcNotifsPortAlarmFilterIfIndex_Object = MibTableColumn
rcNotifsPortAlarmFilterIfIndex = _RcNotifsPortAlarmFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11, 1, 2),
    _RcNotifsPortAlarmFilterIfIndex_Type()
)
rcNotifsPortAlarmFilterIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterIfIndex.setStatus("current")


class _RcNotifsPortAlarmFilterTrapEnable_Type(OctetString):
    """Custom type rcNotifsPortAlarmFilterTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 512),
    )


_RcNotifsPortAlarmFilterTrapEnable_Type.__name__ = "OctetString"
_RcNotifsPortAlarmFilterTrapEnable_Object = MibTableColumn
rcNotifsPortAlarmFilterTrapEnable = _RcNotifsPortAlarmFilterTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11, 1, 10),
    _RcNotifsPortAlarmFilterTrapEnable_Type()
)
rcNotifsPortAlarmFilterTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterTrapEnable.setStatus("current")


class _RcNotifsPortAlarmFilterMonitoringDisable_Type(OctetString):
    """Custom type rcNotifsPortAlarmFilterMonitoringDisable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 512),
    )


_RcNotifsPortAlarmFilterMonitoringDisable_Type.__name__ = "OctetString"
_RcNotifsPortAlarmFilterMonitoringDisable_Object = MibTableColumn
rcNotifsPortAlarmFilterMonitoringDisable = _RcNotifsPortAlarmFilterMonitoringDisable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11, 1, 11),
    _RcNotifsPortAlarmFilterMonitoringDisable_Type()
)
rcNotifsPortAlarmFilterMonitoringDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterMonitoringDisable.setStatus("current")
_RcNotifsPortAlarmFilterRowStatus_Type = RowStatus
_RcNotifsPortAlarmFilterRowStatus_Object = MibTableColumn
rcNotifsPortAlarmFilterRowStatus = _RcNotifsPortAlarmFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 60, 11, 1, 30),
    _RcNotifsPortAlarmFilterRowStatus_Type()
)
rcNotifsPortAlarmFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmFilterRowStatus.setStatus("current")
_RcNotifsPortAlarmInverseConfig_ObjectIdentity = ObjectIdentity
rcNotifsPortAlarmInverseConfig = _RcNotifsPortAlarmInverseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61)
)


class _RcNotifsAlarmInverseMode_Type(Integer32):
    """Custom type rcNotifsAlarmInverseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("auto", 2),
          ("manual", 3))
    )


_RcNotifsAlarmInverseMode_Type.__name__ = "Integer32"
_RcNotifsAlarmInverseMode_Object = MibScalar
rcNotifsAlarmInverseMode = _RcNotifsAlarmInverseMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 9),
    _RcNotifsAlarmInverseMode_Type()
)
rcNotifsAlarmInverseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmInverseMode.setStatus("current")
_RcNotifsPortAlarmInverseTableSize_Type = Integer32
_RcNotifsPortAlarmInverseTableSize_Object = MibScalar
rcNotifsPortAlarmInverseTableSize = _RcNotifsPortAlarmInverseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 10),
    _RcNotifsPortAlarmInverseTableSize_Type()
)
rcNotifsPortAlarmInverseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmInverseTableSize.setStatus("current")
_RcNotifsPortAlarmInverseTable_Object = MibTable
rcNotifsPortAlarmInverseTable = _RcNotifsPortAlarmInverseTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 11)
)
if mibBuilder.loadTexts:
    rcNotifsPortAlarmInverseTable.setStatus("current")
_RcNotifsPortAlarmInverseEntry_Object = MibTableRow
rcNotifsPortAlarmInverseEntry = _RcNotifsPortAlarmInverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 11, 1)
)
rcNotifsPortAlarmInverseEntry.setIndexNames(
    (0, "RAISECOM-NOTIFICATION-MIB", "rcNotifsPortAlarmInversePhysicalID"),
    (0, "RAISECOM-NOTIFICATION-MIB", "rcNotifsPortAlarmInverseIfIndex"),
)
if mibBuilder.loadTexts:
    rcNotifsPortAlarmInverseEntry.setStatus("current")


class _RcNotifsPortAlarmInversePhysicalID_Type(OctetString):
    """Custom type rcNotifsPortAlarmInversePhysicalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RcNotifsPortAlarmInversePhysicalID_Type.__name__ = "OctetString"
_RcNotifsPortAlarmInversePhysicalID_Object = MibTableColumn
rcNotifsPortAlarmInversePhysicalID = _RcNotifsPortAlarmInversePhysicalID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 11, 1, 1),
    _RcNotifsPortAlarmInversePhysicalID_Type()
)
rcNotifsPortAlarmInversePhysicalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmInversePhysicalID.setStatus("current")
_RcNotifsPortAlarmInverseIfIndex_Type = Integer32
_RcNotifsPortAlarmInverseIfIndex_Object = MibTableColumn
rcNotifsPortAlarmInverseIfIndex = _RcNotifsPortAlarmInverseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 11, 1, 2),
    _RcNotifsPortAlarmInverseIfIndex_Type()
)
rcNotifsPortAlarmInverseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmInverseIfIndex.setStatus("current")


class _RcNotifsPortAlarmInverseEnable_Type(Integer32):
    """Custom type rcNotifsPortAlarmInverseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RcNotifsPortAlarmInverseEnable_Type.__name__ = "Integer32"
_RcNotifsPortAlarmInverseEnable_Object = MibTableColumn
rcNotifsPortAlarmInverseEnable = _RcNotifsPortAlarmInverseEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 11, 1, 4),
    _RcNotifsPortAlarmInverseEnable_Type()
)
rcNotifsPortAlarmInverseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsPortAlarmInverseEnable.setStatus("current")


class _RcNotifsAlarmInverseBatchEnable_Type(OctetString):
    """Custom type rcNotifsAlarmInverseBatchEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RcNotifsAlarmInverseBatchEnable_Type.__name__ = "OctetString"
_RcNotifsAlarmInverseBatchEnable_Object = MibScalar
rcNotifsAlarmInverseBatchEnable = _RcNotifsAlarmInverseBatchEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 61, 12),
    _RcNotifsAlarmInverseBatchEnable_Type()
)
rcNotifsAlarmInverseBatchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsAlarmInverseBatchEnable.setStatus("current")


class _RcNotifsTrapRepeatIndex_Type(OctetString):
    """Custom type rcNotifsTrapRepeatIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcNotifsTrapRepeatIndex_Type.__name__ = "OctetString"
_RcNotifsTrapRepeatIndex_Object = MibScalar
rcNotifsTrapRepeatIndex = _RcNotifsTrapRepeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 70),
    _RcNotifsTrapRepeatIndex_Type()
)
rcNotifsTrapRepeatIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapRepeatIndex.setStatus("current")
_RcNotifsTrapCurrentIndex_Type = Integer32
_RcNotifsTrapCurrentIndex_Object = MibScalar
rcNotifsTrapCurrentIndex = _RcNotifsTrapCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 71),
    _RcNotifsTrapCurrentIndex_Type()
)
rcNotifsTrapCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNotifsTrapCurrentIndex.setStatus("current")


class _RcNotifsTrapRelateEnable_Type(Integer32):
    """Custom type rcNotifsTrapRelateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RcNotifsTrapRelateEnable_Type.__name__ = "Integer32"
_RcNotifsTrapRelateEnable_Object = MibScalar
rcNotifsTrapRelateEnable = _RcNotifsTrapRelateEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 72),
    _RcNotifsTrapRelateEnable_Type()
)
rcNotifsTrapRelateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapRelateEnable.setStatus("current")
_RcNotifsTrapRelateDelayTimes_Type = Integer32
_RcNotifsTrapRelateDelayTimes_Object = MibScalar
rcNotifsTrapRelateDelayTimes = _RcNotifsTrapRelateDelayTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 1, 73),
    _RcNotifsTrapRelateDelayTimes_Type()
)
rcNotifsTrapRelateDelayTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcNotifsTrapRelateDelayTimes.setStatus("current")
_RcNotifsObjects_ObjectIdentity = ObjectIdentity
rcNotifsObjects = _RcNotifsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2)
)
_RcCurNotifsAlarmTableSize_Type = Integer32
_RcCurNotifsAlarmTableSize_Object = MibScalar
rcCurNotifsAlarmTableSize = _RcCurNotifsAlarmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 1),
    _RcCurNotifsAlarmTableSize_Type()
)
rcCurNotifsAlarmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmTableSize.setStatus("current")
_RcCurNotifsAlarmTable_Object = MibTable
rcCurNotifsAlarmTable = _RcCurNotifsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    rcCurNotifsAlarmTable.setStatus("current")
_RcCurNotifsAlarmEntry_Object = MibTableRow
rcCurNotifsAlarmEntry = _RcCurNotifsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1)
)
rcCurNotifsAlarmEntry.setIndexNames(
    (0, "RAISECOM-NOTIFICATION-MIB", "rcCurNotifsAlarmIndex"),
)
if mibBuilder.loadTexts:
    rcCurNotifsAlarmEntry.setStatus("current")
_RcCurNotifsAlarmIndex_Type = Integer32
_RcCurNotifsAlarmIndex_Object = MibTableColumn
rcCurNotifsAlarmIndex = _RcCurNotifsAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1, 1),
    _RcCurNotifsAlarmIndex_Type()
)
rcCurNotifsAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmIndex.setStatus("current")
_RcCurNotifsAlarmType_Type = ObjectIdentifier
_RcCurNotifsAlarmType_Object = MibTableColumn
rcCurNotifsAlarmType = _RcCurNotifsAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1, 2),
    _RcCurNotifsAlarmType_Type()
)
rcCurNotifsAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmType.setStatus("current")
_RcCurNotifsAlarmBindVarNum_Type = Integer32
_RcCurNotifsAlarmBindVarNum_Object = MibTableColumn
rcCurNotifsAlarmBindVarNum = _RcCurNotifsAlarmBindVarNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1, 3),
    _RcCurNotifsAlarmBindVarNum_Type()
)
rcCurNotifsAlarmBindVarNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmBindVarNum.setStatus("current")
_RcCurNotifsAlarmBindVar_Type = OctetString
_RcCurNotifsAlarmBindVar_Object = MibTableColumn
rcCurNotifsAlarmBindVar = _RcCurNotifsAlarmBindVar_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1, 4),
    _RcCurNotifsAlarmBindVar_Type()
)
rcCurNotifsAlarmBindVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmBindVar.setStatus("current")
_RcCurNotifsAlarmDeclareTime_Type = TimeStamp
_RcCurNotifsAlarmDeclareTime_Object = MibTableColumn
rcCurNotifsAlarmDeclareTime = _RcCurNotifsAlarmDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1, 5),
    _RcCurNotifsAlarmDeclareTime_Type()
)
rcCurNotifsAlarmDeclareTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmDeclareTime.setStatus("current")
_RcCurNotifsAlarmRelativeTime_Type = Counter64
_RcCurNotifsAlarmRelativeTime_Object = MibTableColumn
rcCurNotifsAlarmRelativeTime = _RcCurNotifsAlarmRelativeTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 2, 1, 6),
    _RcCurNotifsAlarmRelativeTime_Type()
)
rcCurNotifsAlarmRelativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmRelativeTime.setStatus("current")
_RcHisNotifsAlarmTableSize_Type = Integer32
_RcHisNotifsAlarmTableSize_Object = MibScalar
rcHisNotifsAlarmTableSize = _RcHisNotifsAlarmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 3),
    _RcHisNotifsAlarmTableSize_Type()
)
rcHisNotifsAlarmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmTableSize.setStatus("current")
_RcHisNotifsAlarmTable_Object = MibTable
rcHisNotifsAlarmTable = _RcHisNotifsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    rcHisNotifsAlarmTable.setStatus("current")
_RcHisNotifsAlarmEntry_Object = MibTableRow
rcHisNotifsAlarmEntry = _RcHisNotifsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1)
)
rcHisNotifsAlarmEntry.setIndexNames(
    (0, "RAISECOM-NOTIFICATION-MIB", "rcHisNotifsAlarmIndex"),
)
if mibBuilder.loadTexts:
    rcHisNotifsAlarmEntry.setStatus("current")
_RcHisNotifsAlarmIndex_Type = Integer32
_RcHisNotifsAlarmIndex_Object = MibTableColumn
rcHisNotifsAlarmIndex = _RcHisNotifsAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 1),
    _RcHisNotifsAlarmIndex_Type()
)
rcHisNotifsAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmIndex.setStatus("current")
_RcHisNotifsAlarmType_Type = ObjectIdentifier
_RcHisNotifsAlarmType_Object = MibTableColumn
rcHisNotifsAlarmType = _RcHisNotifsAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 2),
    _RcHisNotifsAlarmType_Type()
)
rcHisNotifsAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmType.setStatus("current")
_RcHisNotifsAlarmBindVarNum_Type = Integer32
_RcHisNotifsAlarmBindVarNum_Object = MibTableColumn
rcHisNotifsAlarmBindVarNum = _RcHisNotifsAlarmBindVarNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 3),
    _RcHisNotifsAlarmBindVarNum_Type()
)
rcHisNotifsAlarmBindVarNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmBindVarNum.setStatus("current")
_RcHisNotifsAlarmBindVar_Type = OctetString
_RcHisNotifsAlarmBindVar_Object = MibTableColumn
rcHisNotifsAlarmBindVar = _RcHisNotifsAlarmBindVar_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 4),
    _RcHisNotifsAlarmBindVar_Type()
)
rcHisNotifsAlarmBindVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmBindVar.setStatus("current")
_RcHisNotifsAlarmDeclareTime_Type = TimeStamp
_RcHisNotifsAlarmDeclareTime_Object = MibTableColumn
rcHisNotifsAlarmDeclareTime = _RcHisNotifsAlarmDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 5),
    _RcHisNotifsAlarmDeclareTime_Type()
)
rcHisNotifsAlarmDeclareTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmDeclareTime.setStatus("current")
_RcHisNotifsAlarmClearTime_Type = TimeStamp
_RcHisNotifsAlarmClearTime_Object = MibTableColumn
rcHisNotifsAlarmClearTime = _RcHisNotifsAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 6),
    _RcHisNotifsAlarmClearTime_Type()
)
rcHisNotifsAlarmClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmClearTime.setStatus("current")


class _RcHisNotifsAlarmCause_Type(Integer32):
    """Custom type rcHisNotifsAlarmCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_RcHisNotifsAlarmCause_Type.__name__ = "Integer32"
_RcHisNotifsAlarmCause_Object = MibTableColumn
rcHisNotifsAlarmCause = _RcHisNotifsAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 4, 1, 7),
    _RcHisNotifsAlarmCause_Type()
)
rcHisNotifsAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcHisNotifsAlarmCause.setStatus("current")


class _RcCurNotifsAlarmTableCmd_Type(OctetString):
    """Custom type rcCurNotifsAlarmTableCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_RcCurNotifsAlarmTableCmd_Type.__name__ = "OctetString"
_RcCurNotifsAlarmTableCmd_Object = MibScalar
rcCurNotifsAlarmTableCmd = _RcCurNotifsAlarmTableCmd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 10),
    _RcCurNotifsAlarmTableCmd_Type()
)
rcCurNotifsAlarmTableCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmTableCmd.setStatus("current")


class _RcCurNotifsAlarmTableDeleteByAlarmOID_Type(OctetString):
    """Custom type rcCurNotifsAlarmTableDeleteByAlarmOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 1024),
    )


_RcCurNotifsAlarmTableDeleteByAlarmOID_Type.__name__ = "OctetString"
_RcCurNotifsAlarmTableDeleteByAlarmOID_Object = MibScalar
rcCurNotifsAlarmTableDeleteByAlarmOID = _RcCurNotifsAlarmTableDeleteByAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 11),
    _RcCurNotifsAlarmTableDeleteByAlarmOID_Type()
)
rcCurNotifsAlarmTableDeleteByAlarmOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmTableDeleteByAlarmOID.setStatus("current")


class _RcCurNotifsAlarmTableMaxSize_Type(Integer32):
    """Custom type rcCurNotifsAlarmTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_RcCurNotifsAlarmTableMaxSize_Type.__name__ = "Integer32"
_RcCurNotifsAlarmTableMaxSize_Object = MibScalar
rcCurNotifsAlarmTableMaxSize = _RcCurNotifsAlarmTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 20),
    _RcCurNotifsAlarmTableMaxSize_Type()
)
rcCurNotifsAlarmTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmTableMaxSize.setStatus("current")


class _RcCurNotifsAlarmTableStorageMode_Type(Integer32):
    """Custom type rcCurNotifsAlarmTableStorageMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("stop", 2))
    )


_RcCurNotifsAlarmTableStorageMode_Type.__name__ = "Integer32"
_RcCurNotifsAlarmTableStorageMode_Object = MibScalar
rcCurNotifsAlarmTableStorageMode = _RcCurNotifsAlarmTableStorageMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1, 3, 2, 21),
    _RcCurNotifsAlarmTableStorageMode_Type()
)
rcCurNotifsAlarmTableStorageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCurNotifsAlarmTableStorageMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-NOTIFICATION-MIB",
    **{"raisecomNotifisMib": raisecomNotifisMib,
       "rcNotifsConfObjects": rcNotifsConfObjects,
       "rcNotifsTrapVersion": rcNotifsTrapVersion,
       "rcNotifsTrapEnable": rcNotifsTrapEnable,
       "rcNotifsTrapTotalNumber": rcNotifsTrapTotalNumber,
       "rcNotifsTrapLocation": rcNotifsTrapLocation,
       "rcNotifsTrapFilterSwitch": rcNotifsTrapFilterSwitch,
       "rcNotifsAlarmOutputGroup": rcNotifsAlarmOutputGroup,
       "rcNotifsTrapSinkTable": rcNotifsTrapSinkTable,
       "rcNotifsTrapSinkEntry": rcNotifsTrapSinkEntry,
       "rcNotifsTrapIndex": rcNotifsTrapIndex,
       "rcNotifsTrapTarget": rcNotifsTrapTarget,
       "rcNotifsTrapPort": rcNotifsTrapPort,
       "rcNotifsAlarmFilterTable": rcNotifsAlarmFilterTable,
       "rcNotifsAlarmFilterEntry": rcNotifsAlarmFilterEntry,
       "rcNotifsFilterAlarmTrapOID": rcNotifsFilterAlarmTrapOID,
       "rcNotifsAlarmTrapEnable": rcNotifsAlarmTrapEnable,
       "rcNotifsAlarmTrapLogEnable": rcNotifsAlarmTrapLogEnable,
       "rcNotifsAlarmFilterControl": rcNotifsAlarmFilterControl,
       "rcNotifsAlarmOutputEnable": rcNotifsAlarmOutputEnable,
       "rcNotifsAlarmMonitoringDisable": rcNotifsAlarmMonitoringDisable,
       "rcNotifsPortFilterConfig": rcNotifsPortFilterConfig,
       "rcNotifsPortFilterIndexNext": rcNotifsPortFilterIndexNext,
       "rcNotifsPortFilterTable": rcNotifsPortFilterTable,
       "rcNotifsPortFilterEntry": rcNotifsPortFilterEntry,
       "rcNotifsPortFilterIndex": rcNotifsPortFilterIndex,
       "rcNotifsPortIfIndex": rcNotifsPortIfIndex,
       "rcNotifsPortFilterRowStatus": rcNotifsPortFilterRowStatus,
       "rcNotifsTrapPhysicalID": rcNotifsTrapPhysicalID,
       "rcNotifsTrapIfIndex": rcNotifsTrapIfIndex,
       "rcNotifsTrapBindVariable1": rcNotifsTrapBindVariable1,
       "rcNotifsTrapBindVariable2": rcNotifsTrapBindVariable2,
       "rcNotifsTrapBindVariable3": rcNotifsTrapBindVariable3,
       "rcNotifsTrapBindIpAddress": rcNotifsTrapBindIpAddress,
       "rcNotifsTrapInhibitEnable": rcNotifsTrapInhibitEnable,
       "rcNotifsTrapDelayEnable": rcNotifsTrapDelayEnable,
       "rcNotifsTrapDelayStartingTime": rcNotifsTrapDelayStartingTime,
       "rcNotifsTrapDelayEndTime": rcNotifsTrapDelayEndTime,
       "rcNotifsTrapAutoSaveEnable": rcNotifsTrapAutoSaveEnable,
       "rcNotifsPortAlarmFilterConfig": rcNotifsPortAlarmFilterConfig,
       "rcNotifsPortAlarmFilterTableSize": rcNotifsPortAlarmFilterTableSize,
       "rcNotifsPortAlarmFilterTable": rcNotifsPortAlarmFilterTable,
       "rcNotifsPortAlarmFilterEntry": rcNotifsPortAlarmFilterEntry,
       "rcNotifsPortAlarmFilterPhysicalID": rcNotifsPortAlarmFilterPhysicalID,
       "rcNotifsPortAlarmFilterIfIndex": rcNotifsPortAlarmFilterIfIndex,
       "rcNotifsPortAlarmFilterTrapEnable": rcNotifsPortAlarmFilterTrapEnable,
       "rcNotifsPortAlarmFilterMonitoringDisable": rcNotifsPortAlarmFilterMonitoringDisable,
       "rcNotifsPortAlarmFilterRowStatus": rcNotifsPortAlarmFilterRowStatus,
       "rcNotifsPortAlarmInverseConfig": rcNotifsPortAlarmInverseConfig,
       "rcNotifsAlarmInverseMode": rcNotifsAlarmInverseMode,
       "rcNotifsPortAlarmInverseTableSize": rcNotifsPortAlarmInverseTableSize,
       "rcNotifsPortAlarmInverseTable": rcNotifsPortAlarmInverseTable,
       "rcNotifsPortAlarmInverseEntry": rcNotifsPortAlarmInverseEntry,
       "rcNotifsPortAlarmInversePhysicalID": rcNotifsPortAlarmInversePhysicalID,
       "rcNotifsPortAlarmInverseIfIndex": rcNotifsPortAlarmInverseIfIndex,
       "rcNotifsPortAlarmInverseEnable": rcNotifsPortAlarmInverseEnable,
       "rcNotifsAlarmInverseBatchEnable": rcNotifsAlarmInverseBatchEnable,
       "rcNotifsTrapRepeatIndex": rcNotifsTrapRepeatIndex,
       "rcNotifsTrapCurrentIndex": rcNotifsTrapCurrentIndex,
       "rcNotifsTrapRelateEnable": rcNotifsTrapRelateEnable,
       "rcNotifsTrapRelateDelayTimes": rcNotifsTrapRelateDelayTimes,
       "rcNotifsObjects": rcNotifsObjects,
       "rcCurNotifsAlarmTableSize": rcCurNotifsAlarmTableSize,
       "rcCurNotifsAlarmTable": rcCurNotifsAlarmTable,
       "rcCurNotifsAlarmEntry": rcCurNotifsAlarmEntry,
       "rcCurNotifsAlarmIndex": rcCurNotifsAlarmIndex,
       "rcCurNotifsAlarmType": rcCurNotifsAlarmType,
       "rcCurNotifsAlarmBindVarNum": rcCurNotifsAlarmBindVarNum,
       "rcCurNotifsAlarmBindVar": rcCurNotifsAlarmBindVar,
       "rcCurNotifsAlarmDeclareTime": rcCurNotifsAlarmDeclareTime,
       "rcCurNotifsAlarmRelativeTime": rcCurNotifsAlarmRelativeTime,
       "rcHisNotifsAlarmTableSize": rcHisNotifsAlarmTableSize,
       "rcHisNotifsAlarmTable": rcHisNotifsAlarmTable,
       "rcHisNotifsAlarmEntry": rcHisNotifsAlarmEntry,
       "rcHisNotifsAlarmIndex": rcHisNotifsAlarmIndex,
       "rcHisNotifsAlarmType": rcHisNotifsAlarmType,
       "rcHisNotifsAlarmBindVarNum": rcHisNotifsAlarmBindVarNum,
       "rcHisNotifsAlarmBindVar": rcHisNotifsAlarmBindVar,
       "rcHisNotifsAlarmDeclareTime": rcHisNotifsAlarmDeclareTime,
       "rcHisNotifsAlarmClearTime": rcHisNotifsAlarmClearTime,
       "rcHisNotifsAlarmCause": rcHisNotifsAlarmCause,
       "rcCurNotifsAlarmTableCmd": rcCurNotifsAlarmTableCmd,
       "rcCurNotifsAlarmTableDeleteByAlarmOID": rcCurNotifsAlarmTableDeleteByAlarmOID,
       "rcCurNotifsAlarmTableMaxSize": rcCurNotifsAlarmTableMaxSize,
       "rcCurNotifsAlarmTableStorageMode": rcCurNotifsAlarmTableStorageMode}
)
