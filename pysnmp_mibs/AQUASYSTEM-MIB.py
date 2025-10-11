# SNMP MIB module (AQUASYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/AQUASYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:10 2025
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

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(wanflex,) = mibBuilder.importSymbols(
    "INFINET-MIB",
    "wanflex")

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

aquasystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3)
)
if mibBuilder.loadTexts:
    aquasystemMIB.setRevisions(
        ("2018-02-26 10:30",
         "2014-07-29 06:57",
         "2014-06-03 03:50",
         "2014-01-21 07:21",
         "2014-01-15 04:38",
         "2013-07-22 11:04",
         "2013-06-19 16:22",
         "2012-06-13 08:16",
         "2011-02-16 09:34",
         "2008-05-05 09:00",
         "2007-11-08 11:16",
         "2007-08-23 17:32")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysGPSXY_Type = OctetString
_SysGPSXY_Object = MibScalar
sysGPSXY = _SysGPSXY_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 1),
    _SysGPSXY_Type()
)
sysGPSXY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGPSXY.setStatus("current")


class _SysFastRoute_Type(Integer32):
    """Custom type sysFastRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SysFastRoute_Type.__name__ = "Integer32"
_SysFastRoute_Object = MibScalar
sysFastRoute = _SysFastRoute_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 2),
    _SysFastRoute_Type()
)
sysFastRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFastRoute.setStatus("current")


class _SysICMPLimit_Type(Integer32):
    """Custom type sysICMPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SysICMPLimit_Type.__name__ = "Integer32"
_SysICMPLimit_Object = MibScalar
sysICMPLimit = _SysICMPLimit_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 3),
    _SysICMPLimit_Type()
)
sysICMPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysICMPLimit.setStatus("current")


class _SysSendRedirects_Type(Integer32):
    """Custom type sysSendRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SysSendRedirects_Type.__name__ = "Integer32"
_SysSendRedirects_Object = MibScalar
sysSendRedirects = _SysSendRedirects_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 4),
    _SysSendRedirects_Type()
)
sysSendRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSendRedirects.setStatus("current")


class _SysDropRedirects_Type(Integer32):
    """Custom type sysDropRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SysDropRedirects_Type.__name__ = "Integer32"
_SysDropRedirects_Object = MibScalar
sysDropRedirects = _SysDropRedirects_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 5),
    _SysDropRedirects_Type()
)
sysDropRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDropRedirects.setStatus("current")
_SysCpu_Type = Gauge32
_SysCpu_Object = MibScalar
sysCpu = _SysCpu_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 6),
    _SysCpu_Type()
)
sysCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCpu.setStatus("current")
_SysTemperature_Type = Integer32
_SysTemperature_Object = MibScalar
sysTemperature = _SysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 7),
    _SysTemperature_Type()
)
sysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTemperature.setStatus("current")
_SysTrapSequence_Type = Counter32
_SysTrapSequence_Object = MibScalar
sysTrapSequence = _SysTrapSequence_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 8),
    _SysTrapSequence_Type()
)
sysTrapSequence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sysTrapSequence.setStatus("current")
_SysSerialNumber_Type = Integer32
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 9),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")


class _SysRestartTimer_Type(Unsigned32):
    """Custom type sysRestartTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 107374),
    )


_SysRestartTimer_Type.__name__ = "Unsigned32"
_SysRestartTimer_Object = MibScalar
sysRestartTimer = _SysRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 10),
    _SysRestartTimer_Type()
)
sysRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestartTimer.setStatus("current")
_SysSerialNumberStr_Type = DisplayString
_SysSerialNumberStr_Object = MibScalar
sysSerialNumberStr = _SysSerialNumberStr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 11),
    _SysSerialNumberStr_Type()
)
sysSerialNumberStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumberStr.setStatus("current")
_SysNote_Type = OctetString
_SysNote_Object = MibScalar
sysNote = _SysNote_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 12),
    _SysNote_Type()
)
sysNote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNote.setStatus("current")
_SysLastRebootReason_Type = DisplayString
_SysLastRebootReason_Object = MibScalar
sysLastRebootReason = _SysLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 13),
    _SysLastRebootReason_Type()
)
sysLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastRebootReason.setStatus("current")
_SysSoftwareVersion_Type = DisplayString
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 14),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("current")
_SysModel_Type = DisplayString
_SysModel_Object = MibScalar
sysModel = _SysModel_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 15),
    _SysModel_Type()
)
sysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModel.setStatus("current")
_SysFirmwareID_Type = DisplayString
_SysFirmwareID_Object = MibScalar
sysFirmwareID = _SysFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 16),
    _SysFirmwareID_Type()
)
sysFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareID.setStatus("current")
_SysBuildDate_Type = DisplayString
_SysBuildDate_Object = MibScalar
sysBuildDate = _SysBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 17),
    _SysBuildDate_Type()
)
sysBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBuildDate.setStatus("current")
_SysBuildTime_Type = DisplayString
_SysBuildTime_Object = MibScalar
sysBuildTime = _SysBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 18),
    _SysBuildTime_Type()
)
sysBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBuildTime.setStatus("current")
_SysIf_ObjectIdentity = ObjectIdentity
sysIf = _SysIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20)
)
_SysIfTable_Object = MibTable
sysIfTable = _SysIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20, 1)
)
if mibBuilder.loadTexts:
    sysIfTable.setStatus("current")
_SysIfEntry_Object = MibTableRow
sysIfEntry = _SysIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20, 1, 1)
)
if mibBuilder.loadTexts:
    sysIfEntry.setStatus("current")
_SysIfCurPpsRx_Type = Gauge32
_SysIfCurPpsRx_Object = MibTableColumn
sysIfCurPpsRx = _SysIfCurPpsRx_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20, 1, 1, 1),
    _SysIfCurPpsRx_Type()
)
sysIfCurPpsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfCurPpsRx.setStatus("current")
_SysIfCurPpsTx_Type = Gauge32
_SysIfCurPpsTx_Object = MibTableColumn
sysIfCurPpsTx = _SysIfCurPpsTx_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20, 1, 1, 2),
    _SysIfCurPpsTx_Type()
)
sysIfCurPpsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfCurPpsTx.setStatus("current")
_SysIfCurLoadRx_Type = Gauge32
_SysIfCurLoadRx_Object = MibTableColumn
sysIfCurLoadRx = _SysIfCurLoadRx_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20, 1, 1, 3),
    _SysIfCurLoadRx_Type()
)
sysIfCurLoadRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfCurLoadRx.setStatus("current")
_SysIfCurLoadTx_Type = Gauge32
_SysIfCurLoadTx_Object = MibTableColumn
sysIfCurLoadTx = _SysIfCurLoadTx_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 20, 1, 1, 4),
    _SysIfCurLoadTx_Type()
)
sysIfCurLoadTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfCurLoadTx.setStatus("current")
_SysMem_ObjectIdentity = ObjectIdentity
sysMem = _SysMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 21)
)
_SysMemTotal_Type = Gauge32
_SysMemTotal_Object = MibScalar
sysMemTotal = _SysMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 21, 1),
    _SysMemTotal_Type()
)
sysMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemTotal.setStatus("current")
_SysMemFree_Type = Gauge32
_SysMemFree_Object = MibScalar
sysMemFree = _SysMemFree_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 21, 2),
    _SysMemFree_Type()
)
sysMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemFree.setStatus("current")
_SysNetBufsInUse_Type = Gauge32
_SysNetBufsInUse_Object = MibScalar
sysNetBufsInUse = _SysNetBufsInUse_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 21, 3),
    _SysNetBufsInUse_Type()
)
sysNetBufsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetBufsInUse.setStatus("current")
_SysNetPagesTotal_Type = Gauge32
_SysNetPagesTotal_Object = MibScalar
sysNetPagesTotal = _SysNetPagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 21, 4),
    _SysNetPagesTotal_Type()
)
sysNetPagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetPagesTotal.setStatus("current")
_SysNetPagesInUse_Type = Gauge32
_SysNetPagesInUse_Object = MibScalar
sysNetPagesInUse = _SysNetPagesInUse_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 21, 5),
    _SysNetPagesInUse_Type()
)
sysNetPagesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetPagesInUse.setStatus("current")
_SysQueue_ObjectIdentity = ObjectIdentity
sysQueue = _SysQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22)
)
_SysQueueTable_Object = MibTable
sysQueueTable = _SysQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1)
)
if mibBuilder.loadTexts:
    sysQueueTable.setStatus("current")
_SysQueueEntry_Object = MibTableRow
sysQueueEntry = _SysQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1, 1)
)
sysQueueEntry.setIndexNames(
    (0, "AQUASYSTEM-MIB", "sysQueueIndex"),
)
if mibBuilder.loadTexts:
    sysQueueEntry.setStatus("current")


class _SysQueueIndex_Type(Integer32):
    """Custom type sysQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SysQueueIndex_Type.__name__ = "Integer32"
_SysQueueIndex_Object = MibTableColumn
sysQueueIndex = _SysQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1, 1, 1),
    _SysQueueIndex_Type()
)
sysQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysQueueIndex.setStatus("current")
_SysQueueName_Type = OctetString
_SysQueueName_Object = MibTableColumn
sysQueueName = _SysQueueName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1, 1, 2),
    _SysQueueName_Type()
)
sysQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysQueueName.setStatus("current")
_SysQueueLen_Type = Unsigned32
_SysQueueLen_Object = MibTableColumn
sysQueueLen = _SysQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1, 1, 3),
    _SysQueueLen_Type()
)
sysQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysQueueLen.setStatus("current")
_SysQueueMaxLen_Type = Unsigned32
_SysQueueMaxLen_Object = MibTableColumn
sysQueueMaxLen = _SysQueueMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1, 1, 4),
    _SysQueueMaxLen_Type()
)
sysQueueMaxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysQueueMaxLen.setStatus("current")
_SysQueueDrops_Type = Unsigned32
_SysQueueDrops_Object = MibTableColumn
sysQueueDrops = _SysQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 22, 1, 1, 5),
    _SysQueueDrops_Type()
)
sysQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysQueueDrops.setStatus("current")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23)
)
_SysMgmtGlobals_ObjectIdentity = ObjectIdentity
sysMgmtGlobals = _SysMgmtGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1)
)
_SysMgmtAccess_Type = DisplayString
_SysMgmtAccess_Object = MibScalar
sysMgmtAccess = _SysMgmtAccess_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1, 1),
    _SysMgmtAccess_Type()
)
sysMgmtAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtAccess.setStatus("current")
_SysMgmtSrcIp_Type = IpAddress
_SysMgmtSrcIp_Object = MibScalar
sysMgmtSrcIp = _SysMgmtSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1, 2),
    _SysMgmtSrcIp_Type()
)
sysMgmtSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtSrcIp.setStatus("current")


class _SysMgmtCurrentState_Type(Integer32):
    """Custom type sysMgmtCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("busy", 1),
          ("hold", 2))
    )


_SysMgmtCurrentState_Type.__name__ = "Integer32"
_SysMgmtCurrentState_Object = MibScalar
sysMgmtCurrentState = _SysMgmtCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1, 3),
    _SysMgmtCurrentState_Type()
)
sysMgmtCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCurrentState.setStatus("current")


class _SysMgmtOperProgress_Type(Integer32):
    """Custom type sysMgmtOperProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtOperProgress_Type.__name__ = "Integer32"
_SysMgmtOperProgress_Object = MibScalar
sysMgmtOperProgress = _SysMgmtOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1, 4),
    _SysMgmtOperProgress_Type()
)
sysMgmtOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtOperProgress.setStatus("current")
_SysMgmtErrorString_Type = DisplayString
_SysMgmtErrorString_Object = MibScalar
sysMgmtErrorString = _SysMgmtErrorString_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1, 5),
    _SysMgmtErrorString_Type()
)
sysMgmtErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtErrorString.setStatus("current")


class _SysMgmtHoldTimer_Type(Gauge32):
    """Custom type sysMgmtHoldTimer based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SysMgmtHoldTimer_Type.__name__ = "Gauge32"
_SysMgmtHoldTimer_Object = MibScalar
sysMgmtHoldTimer = _SysMgmtHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 1, 6),
    _SysMgmtHoldTimer_Type()
)
sysMgmtHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtHoldTimer.setStatus("current")
_SysMgmtFrmw_ObjectIdentity = ObjectIdentity
sysMgmtFrmw = _SysMgmtFrmw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 2)
)


class _SysMgmtFrmwDlPath_Type(DisplayString):
    """Custom type sysMgmtFrmwDlPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SysMgmtFrmwDlPath_Type.__name__ = "DisplayString"
_SysMgmtFrmwDlPath_Object = MibScalar
sysMgmtFrmwDlPath = _SysMgmtFrmwDlPath_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 2, 1),
    _SysMgmtFrmwDlPath_Type()
)
sysMgmtFrmwDlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtFrmwDlPath.setStatus("current")


class _SysMgmtFrmwDlResult_Type(Integer32):
    """Custom type sysMgmtFrmwDlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("system-error", 1),
          ("ftp-error", 2),
          ("firmware-error", 3),
          ("blocked", 4))
    )


_SysMgmtFrmwDlResult_Type.__name__ = "Integer32"
_SysMgmtFrmwDlResult_Object = MibScalar
sysMgmtFrmwDlResult = _SysMgmtFrmwDlResult_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 2, 2),
    _SysMgmtFrmwDlResult_Type()
)
sysMgmtFrmwDlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtFrmwDlResult.setStatus("current")
_SysMgmtFrmwUlPath_Type = DisplayString
_SysMgmtFrmwUlPath_Object = MibScalar
sysMgmtFrmwUlPath = _SysMgmtFrmwUlPath_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 2, 3),
    _SysMgmtFrmwUlPath_Type()
)
sysMgmtFrmwUlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtFrmwUlPath.setStatus("current")


class _SysMgmtFrmwUlResult_Type(Integer32):
    """Custom type sysMgmtFrmwUlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("system-error", 1),
          ("ftp-error", 2),
          ("blocked", 3))
    )


_SysMgmtFrmwUlResult_Type.__name__ = "Integer32"
_SysMgmtFrmwUlResult_Object = MibScalar
sysMgmtFrmwUlResult = _SysMgmtFrmwUlResult_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 2, 4),
    _SysMgmtFrmwUlResult_Type()
)
sysMgmtFrmwUlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtFrmwUlResult.setStatus("current")
_SysMgmtLic_ObjectIdentity = ObjectIdentity
sysMgmtLic = _SysMgmtLic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 3)
)
_SysMgmtLicDlPath_Type = DisplayString
_SysMgmtLicDlPath_Object = MibScalar
sysMgmtLicDlPath = _SysMgmtLicDlPath_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 3, 1),
    _SysMgmtLicDlPath_Type()
)
sysMgmtLicDlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtLicDlPath.setStatus("current")


class _SysMgmtLicDlResult_Type(Integer32):
    """Custom type sysMgmtLicDlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("system-error", 1),
          ("ftp-error", 2),
          ("license-error", 3),
          ("blocked", 4))
    )


_SysMgmtLicDlResult_Type.__name__ = "Integer32"
_SysMgmtLicDlResult_Object = MibScalar
sysMgmtLicDlResult = _SysMgmtLicDlResult_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 3, 2),
    _SysMgmtLicDlResult_Type()
)
sysMgmtLicDlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLicDlResult.setStatus("current")
_SysMgmtLicUlPath_Type = DisplayString
_SysMgmtLicUlPath_Object = MibScalar
sysMgmtLicUlPath = _SysMgmtLicUlPath_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 3, 3),
    _SysMgmtLicUlPath_Type()
)
sysMgmtLicUlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtLicUlPath.setStatus("current")


class _SysMgmtLicUlResult_Type(Integer32):
    """Custom type sysMgmtLicUlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("system-error", 1),
          ("ftp-error", 2),
          ("blocked", 3))
    )


_SysMgmtLicUlResult_Type.__name__ = "Integer32"
_SysMgmtLicUlResult_Object = MibScalar
sysMgmtLicUlResult = _SysMgmtLicUlResult_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 3, 4),
    _SysMgmtLicUlResult_Type()
)
sysMgmtLicUlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLicUlResult.setStatus("current")
_SysMgmtCfg_ObjectIdentity = ObjectIdentity
sysMgmtCfg = _SysMgmtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 4)
)
_SysMgmtCfgDlPath_Type = DisplayString
_SysMgmtCfgDlPath_Object = MibScalar
sysMgmtCfgDlPath = _SysMgmtCfgDlPath_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 4, 1),
    _SysMgmtCfgDlPath_Type()
)
sysMgmtCfgDlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCfgDlPath.setStatus("current")


class _SysMgmtCfgDlResult_Type(Integer32):
    """Custom type sysMgmtCfgDlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("system-error", 1),
          ("ftp-error", 2),
          ("config-error", 3),
          ("blocked", 4))
    )


_SysMgmtCfgDlResult_Type.__name__ = "Integer32"
_SysMgmtCfgDlResult_Object = MibScalar
sysMgmtCfgDlResult = _SysMgmtCfgDlResult_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 4, 2),
    _SysMgmtCfgDlResult_Type()
)
sysMgmtCfgDlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCfgDlResult.setStatus("current")
_SysMgmtCfgUlPath_Type = DisplayString
_SysMgmtCfgUlPath_Object = MibScalar
sysMgmtCfgUlPath = _SysMgmtCfgUlPath_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 4, 3),
    _SysMgmtCfgUlPath_Type()
)
sysMgmtCfgUlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCfgUlPath.setStatus("current")


class _SysMgmtCfgUlResult_Type(Integer32):
    """Custom type sysMgmtCfgUlResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("system-error", 1),
          ("ftp-error", 2),
          ("blocked", 3))
    )


_SysMgmtCfgUlResult_Type.__name__ = "Integer32"
_SysMgmtCfgUlResult_Object = MibScalar
sysMgmtCfgUlResult = _SysMgmtCfgUlResult_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 23, 4, 4),
    _SysMgmtCfgUlResult_Type()
)
sysMgmtCfgUlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCfgUlResult.setStatus("current")
_AquasystemMIBConformance_ObjectIdentity = ObjectIdentity
aquasystemMIBConformance = _AquasystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 100)
)
_AquasystemMIBCompliances_ObjectIdentity = ObjectIdentity
aquasystemMIBCompliances = _AquasystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 100, 1)
)
_AquasystemMIBGroups_ObjectIdentity = ObjectIdentity
aquasystemMIBGroups = _AquasystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 100, 2)
)
ifEntry.registerAugmentions(
    ("AQUASYSTEM-MIB",
     "sysIfEntry")
)
sysIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

systemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 100, 2, 1)
)
systemGroup.setObjects(
      *(("AQUASYSTEM-MIB", "sysGPSXY"),
        ("AQUASYSTEM-MIB", "sysFastRoute"),
        ("AQUASYSTEM-MIB", "sysICMPLimit"),
        ("AQUASYSTEM-MIB", "sysSendRedirects"),
        ("AQUASYSTEM-MIB", "sysDropRedirects"),
        ("AQUASYSTEM-MIB", "sysCpu"),
        ("AQUASYSTEM-MIB", "sysTemperature"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysRestartTimer"),
        ("AQUASYSTEM-MIB", "sysSerialNumberStr"),
        ("AQUASYSTEM-MIB", "sysNote"),
        ("AQUASYSTEM-MIB", "sysLastRebootReason"),
        ("AQUASYSTEM-MIB", "sysSoftwareVersion"),
        ("AQUASYSTEM-MIB", "sysModel"),
        ("AQUASYSTEM-MIB", "sysFirmwareID"),
        ("AQUASYSTEM-MIB", "sysBuildDate"),
        ("AQUASYSTEM-MIB", "sysBuildTime"),
        ("AQUASYSTEM-MIB", "sysIfCurPpsRx"),
        ("AQUASYSTEM-MIB", "sysIfCurPpsTx"),
        ("AQUASYSTEM-MIB", "sysIfCurLoadRx"),
        ("AQUASYSTEM-MIB", "sysIfCurLoadTx"),
        ("AQUASYSTEM-MIB", "sysMemFree"),
        ("AQUASYSTEM-MIB", "sysMemTotal"),
        ("AQUASYSTEM-MIB", "sysNetBufsInUse"),
        ("AQUASYSTEM-MIB", "sysNetPagesTotal"),
        ("AQUASYSTEM-MIB", "sysNetPagesInUse"),
        ("AQUASYSTEM-MIB", "sysQueueIndex"),
        ("AQUASYSTEM-MIB", "sysQueueName"),
        ("AQUASYSTEM-MIB", "sysQueueLen"),
        ("AQUASYSTEM-MIB", "sysQueueMaxLen"),
        ("AQUASYSTEM-MIB", "sysQueueDrops"),
        ("AQUASYSTEM-MIB", "sysMgmtAccess"),
        ("AQUASYSTEM-MIB", "sysMgmtSrcIp"),
        ("AQUASYSTEM-MIB", "sysMgmtCurrentState"),
        ("AQUASYSTEM-MIB", "sysMgmtOperProgress"),
        ("AQUASYSTEM-MIB", "sysMgmtErrorString"),
        ("AQUASYSTEM-MIB", "sysMgmtHoldTimer"),
        ("AQUASYSTEM-MIB", "sysMgmtFrmwDlPath"),
        ("AQUASYSTEM-MIB", "sysMgmtFrmwDlResult"),
        ("AQUASYSTEM-MIB", "sysMgmtFrmwUlPath"),
        ("AQUASYSTEM-MIB", "sysMgmtFrmwUlResult"),
        ("AQUASYSTEM-MIB", "sysMgmtLicDlPath"),
        ("AQUASYSTEM-MIB", "sysMgmtLicDlResult"),
        ("AQUASYSTEM-MIB", "sysMgmtLicUlPath"),
        ("AQUASYSTEM-MIB", "sysMgmtLicUlResult"),
        ("AQUASYSTEM-MIB", "sysMgmtCfgDlPath"),
        ("AQUASYSTEM-MIB", "sysMgmtCfgDlResult"),
        ("AQUASYSTEM-MIB", "sysMgmtCfgUlPath"),
        ("AQUASYSTEM-MIB", "sysMgmtCfgUlResult"))
)
if mibBuilder.loadTexts:
    systemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aquasystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 3, 100, 1, 1)
)
aquasystemMIBCompliance.setObjects(
    ("AQUASYSTEM-MIB", "systemGroup")
)
if mibBuilder.loadTexts:
    aquasystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AQUASYSTEM-MIB",
    **{"aquasystemMIB": aquasystemMIB,
       "sysGPSXY": sysGPSXY,
       "sysFastRoute": sysFastRoute,
       "sysICMPLimit": sysICMPLimit,
       "sysSendRedirects": sysSendRedirects,
       "sysDropRedirects": sysDropRedirects,
       "sysCpu": sysCpu,
       "sysTemperature": sysTemperature,
       "sysTrapSequence": sysTrapSequence,
       "sysSerialNumber": sysSerialNumber,
       "sysRestartTimer": sysRestartTimer,
       "sysSerialNumberStr": sysSerialNumberStr,
       "sysNote": sysNote,
       "sysLastRebootReason": sysLastRebootReason,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysModel": sysModel,
       "sysFirmwareID": sysFirmwareID,
       "sysBuildDate": sysBuildDate,
       "sysBuildTime": sysBuildTime,
       "sysIf": sysIf,
       "sysIfTable": sysIfTable,
       "sysIfEntry": sysIfEntry,
       "sysIfCurPpsRx": sysIfCurPpsRx,
       "sysIfCurPpsTx": sysIfCurPpsTx,
       "sysIfCurLoadRx": sysIfCurLoadRx,
       "sysIfCurLoadTx": sysIfCurLoadTx,
       "sysMem": sysMem,
       "sysMemTotal": sysMemTotal,
       "sysMemFree": sysMemFree,
       "sysNetBufsInUse": sysNetBufsInUse,
       "sysNetPagesTotal": sysNetPagesTotal,
       "sysNetPagesInUse": sysNetPagesInUse,
       "sysQueue": sysQueue,
       "sysQueueTable": sysQueueTable,
       "sysQueueEntry": sysQueueEntry,
       "sysQueueIndex": sysQueueIndex,
       "sysQueueName": sysQueueName,
       "sysQueueLen": sysQueueLen,
       "sysQueueMaxLen": sysQueueMaxLen,
       "sysQueueDrops": sysQueueDrops,
       "sysMgmt": sysMgmt,
       "sysMgmtGlobals": sysMgmtGlobals,
       "sysMgmtAccess": sysMgmtAccess,
       "sysMgmtSrcIp": sysMgmtSrcIp,
       "sysMgmtCurrentState": sysMgmtCurrentState,
       "sysMgmtOperProgress": sysMgmtOperProgress,
       "sysMgmtErrorString": sysMgmtErrorString,
       "sysMgmtHoldTimer": sysMgmtHoldTimer,
       "sysMgmtFrmw": sysMgmtFrmw,
       "sysMgmtFrmwDlPath": sysMgmtFrmwDlPath,
       "sysMgmtFrmwDlResult": sysMgmtFrmwDlResult,
       "sysMgmtFrmwUlPath": sysMgmtFrmwUlPath,
       "sysMgmtFrmwUlResult": sysMgmtFrmwUlResult,
       "sysMgmtLic": sysMgmtLic,
       "sysMgmtLicDlPath": sysMgmtLicDlPath,
       "sysMgmtLicDlResult": sysMgmtLicDlResult,
       "sysMgmtLicUlPath": sysMgmtLicUlPath,
       "sysMgmtLicUlResult": sysMgmtLicUlResult,
       "sysMgmtCfg": sysMgmtCfg,
       "sysMgmtCfgDlPath": sysMgmtCfgDlPath,
       "sysMgmtCfgDlResult": sysMgmtCfgDlResult,
       "sysMgmtCfgUlPath": sysMgmtCfgUlPath,
       "sysMgmtCfgUlResult": sysMgmtCfgUlResult,
       "aquasystemMIBConformance": aquasystemMIBConformance,
       "aquasystemMIBCompliances": aquasystemMIBCompliances,
       "aquasystemMIBCompliance": aquasystemMIBCompliance,
       "aquasystemMIBGroups": aquasystemMIBGroups,
       "systemGroup": systemGroup}
)
