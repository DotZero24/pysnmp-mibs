# SNMP MIB module (NEWTEC-ANTENNA-CONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ANTENNA-CONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:51 2025
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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

ntcAntennaController = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700)
)
if mibBuilder.loadTexts:
    ntcAntennaController.setRevisions(
        ("2018-02-02 09:00",
         "2014-02-03 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAntCtrlObjects_ObjectIdentity = ObjectIdentity
ntcAntCtrlObjects = _NtcAntCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1)
)
if mibBuilder.loadTexts:
    ntcAntCtrlObjects.setStatus("current")
_NtcAntCtrlCfg_ObjectIdentity = ObjectIdentity
ntcAntCtrlCfg = _NtcAntCtrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1)
)
if mibBuilder.loadTexts:
    ntcAntCtrlCfg.setStatus("current")
_NtcAntCtrlCfgTable_Object = MibTable
ntcAntCtrlCfgTable = _NtcAntCtrlCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntcAntCtrlCfgTable.setStatus("current")
_NtcAntCtrlCfgEntry_Object = MibTableRow
ntcAntCtrlCfgEntry = _NtcAntCtrlCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1)
)
ntcAntCtrlCfgEntry.setIndexNames(
    (0, "NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgControlId"),
)
if mibBuilder.loadTexts:
    ntcAntCtrlCfgEntry.setStatus("current")


class _NtcAntCtrlCfgControlId_Type(Integer32):
    """Custom type ntcAntCtrlCfgControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("control1", 1),
          ("control2", 2),
          ("control3", 3),
          ("control4", 4))
    )


_NtcAntCtrlCfgControlId_Type.__name__ = "Integer32"
_NtcAntCtrlCfgControlId_Object = MibTableColumn
ntcAntCtrlCfgControlId = _NtcAntCtrlCfgControlId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 1),
    _NtcAntCtrlCfgControlId_Type()
)
ntcAntCtrlCfgControlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgControlId.setStatus("current")


class _NtcAntCtrlCfgEnable_Type(NtcEnable):
    """Custom type ntcAntCtrlCfgEnable based on NtcEnable"""
    defaultValue = 0


_NtcAntCtrlCfgEnable_Type.__name__ = "NtcEnable"
_NtcAntCtrlCfgEnable_Object = MibTableColumn
ntcAntCtrlCfgEnable = _NtcAntCtrlCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 2),
    _NtcAntCtrlCfgEnable_Type()
)
ntcAntCtrlCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgEnable.setStatus("current")
_NtcAntCtrlCfgIpAddress_Type = IpAddress
_NtcAntCtrlCfgIpAddress_Object = MibTableColumn
ntcAntCtrlCfgIpAddress = _NtcAntCtrlCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 3),
    _NtcAntCtrlCfgIpAddress_Type()
)
ntcAntCtrlCfgIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgIpAddress.setStatus("current")


class _NtcAntCtrlCfgPort_Type(Unsigned32):
    """Custom type ntcAntCtrlCfgPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcAntCtrlCfgPort_Type.__name__ = "Unsigned32"
_NtcAntCtrlCfgPort_Object = MibTableColumn
ntcAntCtrlCfgPort = _NtcAntCtrlCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 4),
    _NtcAntCtrlCfgPort_Type()
)
ntcAntCtrlCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgPort.setStatus("current")
_NtcAntCtrlCfgSatLong_Type = Float32TC
_NtcAntCtrlCfgSatLong_Object = MibTableColumn
ntcAntCtrlCfgSatLong = _NtcAntCtrlCfgSatLong_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 5),
    _NtcAntCtrlCfgSatLong_Type()
)
ntcAntCtrlCfgSatLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgSatLong.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgSatLong.setUnits("deg.")
_NtcAntCtrlCfgSatLatVar_Type = Float32TC
_NtcAntCtrlCfgSatLatVar_Object = MibTableColumn
ntcAntCtrlCfgSatLatVar = _NtcAntCtrlCfgSatLatVar_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 6),
    _NtcAntCtrlCfgSatLatVar_Type()
)
ntcAntCtrlCfgSatLatVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgSatLatVar.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgSatLatVar.setUnits("deg.")
_NtcAntCtrlCfgSatSkew_Type = Float32TC
_NtcAntCtrlCfgSatSkew_Object = MibTableColumn
ntcAntCtrlCfgSatSkew = _NtcAntCtrlCfgSatSkew_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 7),
    _NtcAntCtrlCfgSatSkew_Type()
)
ntcAntCtrlCfgSatSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgSatSkew.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgSatSkew.setUnits("deg.")


class _NtcAntCtrlCfgRxPol_Type(Integer32):
    """Custom type ntcAntCtrlCfgRxPol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lefthanded", 0),
          ("righthanded", 1),
          ("horizontal", 3),
          ("vertical", 4))
    )


_NtcAntCtrlCfgRxPol_Type.__name__ = "Integer32"
_NtcAntCtrlCfgRxPol_Object = MibTableColumn
ntcAntCtrlCfgRxPol = _NtcAntCtrlCfgRxPol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 8),
    _NtcAntCtrlCfgRxPol_Type()
)
ntcAntCtrlCfgRxPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgRxPol.setStatus("current")


class _NtcAntCtrlCfgTxPol_Type(Integer32):
    """Custom type ntcAntCtrlCfgTxPol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lefthanded", 0),
          ("righthanded", 1),
          ("horizontal", 3),
          ("vertical", 4))
    )


_NtcAntCtrlCfgTxPol_Type.__name__ = "Integer32"
_NtcAntCtrlCfgTxPol_Object = MibTableColumn
ntcAntCtrlCfgTxPol = _NtcAntCtrlCfgTxPol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 9),
    _NtcAntCtrlCfgTxPol_Type()
)
ntcAntCtrlCfgTxPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgTxPol.setStatus("current")


class _NtcAntCtrlCfgRxLoFreq_Type(Unsigned32):
    """Custom type ntcAntCtrlCfgRxLoFreq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 42000000),
    )


_NtcAntCtrlCfgRxLoFreq_Type.__name__ = "Unsigned32"
_NtcAntCtrlCfgRxLoFreq_Object = MibTableColumn
ntcAntCtrlCfgRxLoFreq = _NtcAntCtrlCfgRxLoFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 10),
    _NtcAntCtrlCfgRxLoFreq_Type()
)
ntcAntCtrlCfgRxLoFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgRxLoFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgRxLoFreq.setUnits("kHz")


class _NtcAntCtrlCfgTxLoFreq_Type(Unsigned32):
    """Custom type ntcAntCtrlCfgTxLoFreq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 42000000),
    )


_NtcAntCtrlCfgTxLoFreq_Type.__name__ = "Unsigned32"
_NtcAntCtrlCfgTxLoFreq_Object = MibTableColumn
ntcAntCtrlCfgTxLoFreq = _NtcAntCtrlCfgTxLoFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 11),
    _NtcAntCtrlCfgTxLoFreq_Type()
)
ntcAntCtrlCfgTxLoFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgTxLoFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgTxLoFreq.setUnits("kHz")
_NtcAntCtrlCfgTxMaxSkew_Type = Float32TC
_NtcAntCtrlCfgTxMaxSkew_Object = MibTableColumn
ntcAntCtrlCfgTxMaxSkew = _NtcAntCtrlCfgTxMaxSkew_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 1, 1, 1, 12),
    _NtcAntCtrlCfgTxMaxSkew_Type()
)
ntcAntCtrlCfgTxMaxSkew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgTxMaxSkew.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlCfgTxMaxSkew.setUnits("deg.")
_NtcAntCtrlMon_ObjectIdentity = ObjectIdentity
ntcAntCtrlMon = _NtcAntCtrlMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2)
)
if mibBuilder.loadTexts:
    ntcAntCtrlMon.setStatus("current")
_NtcAntCtrlMonTable_Object = MibTable
ntcAntCtrlMonTable = _NtcAntCtrlMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAntCtrlMonTable.setStatus("current")
_NtcAntCtrlMonEntry_Object = MibTableRow
ntcAntCtrlMonEntry = _NtcAntCtrlMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1)
)
ntcAntCtrlMonEntry.setIndexNames(
    (0, "NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlMonControlId"),
)
if mibBuilder.loadTexts:
    ntcAntCtrlMonEntry.setStatus("current")


class _NtcAntCtrlMonControlId_Type(Integer32):
    """Custom type ntcAntCtrlMonControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("control1", 1),
          ("control2", 2),
          ("control3", 3),
          ("control4", 4))
    )


_NtcAntCtrlMonControlId_Type.__name__ = "Integer32"
_NtcAntCtrlMonControlId_Object = MibTableColumn
ntcAntCtrlMonControlId = _NtcAntCtrlMonControlId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 1),
    _NtcAntCtrlMonControlId_Type()
)
ntcAntCtrlMonControlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAntCtrlMonControlId.setStatus("current")


class _NtcAntCtrlInterval_Type(Unsigned32):
    """Custom type ntcAntCtrlInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_NtcAntCtrlInterval_Type.__name__ = "Unsigned32"
_NtcAntCtrlInterval_Object = MibTableColumn
ntcAntCtrlInterval = _NtcAntCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 2),
    _NtcAntCtrlInterval_Type()
)
ntcAntCtrlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlInterval.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlInterval.setUnits("s")


class _NtcAntCtrlAntStatus_Type(Integer32):
    """Custom type ntcAntCtrlAntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("failed", 2))
    )


_NtcAntCtrlAntStatus_Type.__name__ = "Integer32"
_NtcAntCtrlAntStatus_Object = MibTableColumn
ntcAntCtrlAntStatus = _NtcAntCtrlAntStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 3),
    _NtcAntCtrlAntStatus_Type()
)
ntcAntCtrlAntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlAntStatus.setStatus("current")


class _NtcAntCtrlTxAllowed_Type(Integer32):
    """Custom type ntcAntCtrlTxAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("on", 1),
          ("off", 2))
    )


_NtcAntCtrlTxAllowed_Type.__name__ = "Integer32"
_NtcAntCtrlTxAllowed_Object = MibTableColumn
ntcAntCtrlTxAllowed = _NtcAntCtrlTxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 4),
    _NtcAntCtrlTxAllowed_Type()
)
ntcAntCtrlTxAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlTxAllowed.setStatus("current")
_NtcAntCtrlLatitude_Type = Float32TC
_NtcAntCtrlLatitude_Object = MibTableColumn
ntcAntCtrlLatitude = _NtcAntCtrlLatitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 5),
    _NtcAntCtrlLatitude_Type()
)
ntcAntCtrlLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlLatitude.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlLatitude.setUnits("deg.")
_NtcAntCtrlLongitude_Type = Float32TC
_NtcAntCtrlLongitude_Object = MibTableColumn
ntcAntCtrlLongitude = _NtcAntCtrlLongitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 6),
    _NtcAntCtrlLongitude_Type()
)
ntcAntCtrlLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlLongitude.setStatus("current")
if mibBuilder.loadTexts:
    ntcAntCtrlLongitude.setUnits("deg.")
_NtcAntCtrlTxMsg_Type = Unsigned32
_NtcAntCtrlTxMsg_Object = MibTableColumn
ntcAntCtrlTxMsg = _NtcAntCtrlTxMsg_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 7),
    _NtcAntCtrlTxMsg_Type()
)
ntcAntCtrlTxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlTxMsg.setStatus("current")
_NtcAntCtrlRxMsg_Type = Unsigned32
_NtcAntCtrlRxMsg_Object = MibTableColumn
ntcAntCtrlRxMsg = _NtcAntCtrlRxMsg_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 2, 1, 1, 8),
    _NtcAntCtrlRxMsg_Type()
)
ntcAntCtrlRxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlRxMsg.setStatus("current")
_NtcAntCtrlAlarm_ObjectIdentity = ObjectIdentity
ntcAntCtrlAlarm = _NtcAntCtrlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3)
)
if mibBuilder.loadTexts:
    ntcAntCtrlAlarm.setStatus("current")
_NtcAntCtrlAlarmStatsTable_Object = MibTable
ntcAntCtrlAlarmStatsTable = _NtcAntCtrlAlarmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntcAntCtrlAlarmStatsTable.setStatus("current")
_NtcAntCtrlAlarmStatsEntry_Object = MibTableRow
ntcAntCtrlAlarmStatsEntry = _NtcAntCtrlAlarmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 1, 1)
)
ntcAntCtrlAlarmStatsEntry.setIndexNames(
    (0, "NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlAlarmStatsControlId"),
)
if mibBuilder.loadTexts:
    ntcAntCtrlAlarmStatsEntry.setStatus("current")


class _NtcAntCtrlAlarmStatsControlId_Type(Integer32):
    """Custom type ntcAntCtrlAlarmStatsControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("control1", 1),
          ("control2", 2),
          ("control3", 3),
          ("control4", 4))
    )


_NtcAntCtrlAlarmStatsControlId_Type.__name__ = "Integer32"
_NtcAntCtrlAlarmStatsControlId_Object = MibTableColumn
ntcAntCtrlAlarmStatsControlId = _NtcAntCtrlAlarmStatsControlId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 1, 1, 1),
    _NtcAntCtrlAlarmStatsControlId_Type()
)
ntcAntCtrlAlarmStatsControlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAntCtrlAlarmStatsControlId.setStatus("current")
_NtcAntCtrlCommErrorStat_Type = NtcAlarmState
_NtcAntCtrlCommErrorStat_Object = MibTableColumn
ntcAntCtrlCommErrorStat = _NtcAntCtrlCommErrorStat_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 1, 1, 2),
    _NtcAntCtrlCommErrorStat_Type()
)
ntcAntCtrlCommErrorStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlCommErrorStat.setStatus("current")
_NtcAntCtrlAntFailureStat_Type = NtcAlarmState
_NtcAntCtrlAntFailureStat_Object = MibTableColumn
ntcAntCtrlAntFailureStat = _NtcAntCtrlAntFailureStat_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 1, 1, 3),
    _NtcAntCtrlAntFailureStat_Type()
)
ntcAntCtrlAntFailureStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlAntFailureStat.setStatus("current")
_NtcAntCtrlCommError_Type = NtcAlarmState
_NtcAntCtrlCommError_Object = MibScalar
ntcAntCtrlCommError = _NtcAntCtrlCommError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 2),
    _NtcAntCtrlCommError_Type()
)
ntcAntCtrlCommError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlCommError.setStatus("current")
_NtcAntCtrlAntFailure_Type = NtcAlarmState
_NtcAntCtrlAntFailure_Object = MibScalar
ntcAntCtrlAntFailure = _NtcAntCtrlAntFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 1, 3, 3),
    _NtcAntCtrlAntFailure_Type()
)
ntcAntCtrlAntFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAntCtrlAntFailure.setStatus("current")
_NtcAntCtrlConformance_ObjectIdentity = ObjectIdentity
ntcAntCtrlConformance = _NtcAntCtrlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 2)
)
if mibBuilder.loadTexts:
    ntcAntCtrlConformance.setStatus("current")
_NtcAntCtrlConfCompliance_ObjectIdentity = ObjectIdentity
ntcAntCtrlConfCompliance = _NtcAntCtrlConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAntCtrlConfCompliance.setStatus("current")
_NtcAntCtrlConfGroup_ObjectIdentity = ObjectIdentity
ntcAntCtrlConfGroup = _NtcAntCtrlConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAntCtrlConfGroup.setStatus("current")

# Managed Objects groups

ntcAntCtrlConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 2, 2, 1)
)
ntcAntCtrlConfGrpV1Standard.setObjects(
      *(("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgEnable"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgIpAddress"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgPort"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgSatLong"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgSatLatVar"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgSatSkew"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgRxPol"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgTxPol"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgRxLoFreq"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgTxLoFreq"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCfgTxMaxSkew"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlInterval"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlAntStatus"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlTxAllowed"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlLatitude"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlLongitude"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlTxMsg"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlRxMsg"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCommErrorStat"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlAntFailureStat"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlCommError"),
        ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlAntFailure"))
)
if mibBuilder.loadTexts:
    ntcAntCtrlConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAntCtrlConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 5700, 2, 1, 1)
)
ntcAntCtrlConfCompV1Standard.setObjects(
    ("NEWTEC-ANTENNA-CONTROLLER-MIB", "ntcAntCtrlConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAntCtrlConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ANTENNA-CONTROLLER-MIB",
    **{"ntcAntennaController": ntcAntennaController,
       "ntcAntCtrlObjects": ntcAntCtrlObjects,
       "ntcAntCtrlCfg": ntcAntCtrlCfg,
       "ntcAntCtrlCfgTable": ntcAntCtrlCfgTable,
       "ntcAntCtrlCfgEntry": ntcAntCtrlCfgEntry,
       "ntcAntCtrlCfgControlId": ntcAntCtrlCfgControlId,
       "ntcAntCtrlCfgEnable": ntcAntCtrlCfgEnable,
       "ntcAntCtrlCfgIpAddress": ntcAntCtrlCfgIpAddress,
       "ntcAntCtrlCfgPort": ntcAntCtrlCfgPort,
       "ntcAntCtrlCfgSatLong": ntcAntCtrlCfgSatLong,
       "ntcAntCtrlCfgSatLatVar": ntcAntCtrlCfgSatLatVar,
       "ntcAntCtrlCfgSatSkew": ntcAntCtrlCfgSatSkew,
       "ntcAntCtrlCfgRxPol": ntcAntCtrlCfgRxPol,
       "ntcAntCtrlCfgTxPol": ntcAntCtrlCfgTxPol,
       "ntcAntCtrlCfgRxLoFreq": ntcAntCtrlCfgRxLoFreq,
       "ntcAntCtrlCfgTxLoFreq": ntcAntCtrlCfgTxLoFreq,
       "ntcAntCtrlCfgTxMaxSkew": ntcAntCtrlCfgTxMaxSkew,
       "ntcAntCtrlMon": ntcAntCtrlMon,
       "ntcAntCtrlMonTable": ntcAntCtrlMonTable,
       "ntcAntCtrlMonEntry": ntcAntCtrlMonEntry,
       "ntcAntCtrlMonControlId": ntcAntCtrlMonControlId,
       "ntcAntCtrlInterval": ntcAntCtrlInterval,
       "ntcAntCtrlAntStatus": ntcAntCtrlAntStatus,
       "ntcAntCtrlTxAllowed": ntcAntCtrlTxAllowed,
       "ntcAntCtrlLatitude": ntcAntCtrlLatitude,
       "ntcAntCtrlLongitude": ntcAntCtrlLongitude,
       "ntcAntCtrlTxMsg": ntcAntCtrlTxMsg,
       "ntcAntCtrlRxMsg": ntcAntCtrlRxMsg,
       "ntcAntCtrlAlarm": ntcAntCtrlAlarm,
       "ntcAntCtrlAlarmStatsTable": ntcAntCtrlAlarmStatsTable,
       "ntcAntCtrlAlarmStatsEntry": ntcAntCtrlAlarmStatsEntry,
       "ntcAntCtrlAlarmStatsControlId": ntcAntCtrlAlarmStatsControlId,
       "ntcAntCtrlCommErrorStat": ntcAntCtrlCommErrorStat,
       "ntcAntCtrlAntFailureStat": ntcAntCtrlAntFailureStat,
       "ntcAntCtrlCommError": ntcAntCtrlCommError,
       "ntcAntCtrlAntFailure": ntcAntCtrlAntFailure,
       "ntcAntCtrlConformance": ntcAntCtrlConformance,
       "ntcAntCtrlConfCompliance": ntcAntCtrlConfCompliance,
       "ntcAntCtrlConfCompV1Standard": ntcAntCtrlConfCompV1Standard,
       "ntcAntCtrlConfGroup": ntcAntCtrlConfGroup,
       "ntcAntCtrlConfGrpV1Standard": ntcAntCtrlConfGrpV1Standard}
)
