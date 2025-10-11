# SNMP MIB module (RUGGEDCOM-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-GPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:35 2025
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

(ruggedcomMgmt,
 ruggedcomTraps) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt",
    "ruggedcomTraps")

(RcTimeSyncStatus,) = mibBuilder.importSymbols(
    "RUGGEDCOM-TIMECONFIG-MIB",
    "RcTimeSyncStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcGps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9)
)
if mibBuilder.loadTexts:
    rcGps.setRevisions(
        ("2015-10-30 17:00",
         "2014-12-01 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcGpsBase_ObjectIdentity = ObjectIdentity
rcGpsBase = _RcGpsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1)
)
_RcGpsStatus_Type = RcTimeSyncStatus
_RcGpsStatus_Object = MibScalar
rcGpsStatus = _RcGpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 1),
    _RcGpsStatus_Type()
)
rcGpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcGpsStatus.setStatus("current")


class _RcGpsLocInt_Type(Integer32):
    """Custom type rcGpsLocInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RcGpsLocInt_Type.__name__ = "Integer32"
_RcGpsLocInt_Object = MibScalar
rcGpsLocInt = _RcGpsLocInt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 2),
    _RcGpsLocInt_Type()
)
rcGpsLocInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGpsLocInt.setStatus("current")


class _RcGpsCableCompensate_Type(Integer32):
    """Custom type rcGpsCableCompensate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_RcGpsCableCompensate_Type.__name__ = "Integer32"
_RcGpsCableCompensate_Object = MibScalar
rcGpsCableCompensate = _RcGpsCableCompensate_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 3),
    _RcGpsCableCompensate_Type()
)
rcGpsCableCompensate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGpsCableCompensate.setStatus("current")
_RcGpsAntPower_Type = TruthValue
_RcGpsAntPower_Object = MibScalar
rcGpsAntPower = _RcGpsAntPower_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 4),
    _RcGpsAntPower_Type()
)
rcGpsAntPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGpsAntPower.setStatus("current")


class _RcSatelliteInView_Type(Integer32):
    """Custom type rcSatelliteInView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_RcSatelliteInView_Type.__name__ = "Integer32"
_RcSatelliteInView_Object = MibScalar
rcSatelliteInView = _RcSatelliteInView_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 5),
    _RcSatelliteInView_Type()
)
rcSatelliteInView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSatelliteInView.setStatus("current")
_RcGpsLatitude_Type = DisplayString
_RcGpsLatitude_Object = MibScalar
rcGpsLatitude = _RcGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 6),
    _RcGpsLatitude_Type()
)
rcGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcGpsLatitude.setStatus("current")
_RcGpsLongtitude_Type = DisplayString
_RcGpsLongtitude_Object = MibScalar
rcGpsLongtitude = _RcGpsLongtitude_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 7),
    _RcGpsLongtitude_Type()
)
rcGpsLongtitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcGpsLongtitude.setStatus("current")


class _RcOFM_Type(Integer32):
    """Custom type rcOFM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_RcOFM_Type.__name__ = "Integer32"
_RcOFM_Object = MibScalar
rcOFM = _RcOFM_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 8),
    _RcOFM_Type()
)
rcOFM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcOFM.setStatus("current")


class _RcFreqAdj_Type(Integer32):
    """Custom type rcFreqAdj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_RcFreqAdj_Type.__name__ = "Integer32"
_RcFreqAdj_Object = MibScalar
rcFreqAdj = _RcFreqAdj_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 1, 9),
    _RcFreqAdj_Type()
)
rcFreqAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcFreqAdj.setStatus("current")
_RcGpsConformance_ObjectIdentity = ObjectIdentity
rcGpsConformance = _RcGpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 3)
)
_RcGpsGroups_ObjectIdentity = ObjectIdentity
rcGpsGroups = _RcGpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 3, 2)
)

# Managed Objects groups

rcGpsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 3, 2, 1)
)
rcGpsBaseGroup.setObjects(
    ("RUGGEDCOM-GPS-MIB", "rcGpsStatus")
)
if mibBuilder.loadTexts:
    rcGpsBaseGroup.setStatus("current")

rcGpsNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 3, 2, 2)
)
rcGpsNotifyGroup.setObjects(
    ("RUGGEDCOM-GPS-MIB", "rcGpsStatusChange")
)
if mibBuilder.loadTexts:
    rcGpsNotifyGroup.setStatus("current")

rcGpsBaseGroup01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 9, 3, 2, 3)
)
rcGpsBaseGroup01.setObjects(
      *(("RUGGEDCOM-GPS-MIB", "rcGpsStatus"),
        ("RUGGEDCOM-GPS-MIB", "rcGpsLocInt"),
        ("RUGGEDCOM-GPS-MIB", "rcGpsCableCompensate"),
        ("RUGGEDCOM-GPS-MIB", "rcGpsAntPower"),
        ("RUGGEDCOM-GPS-MIB", "rcSatelliteInView"),
        ("RUGGEDCOM-GPS-MIB", "rcGpsLatitude"),
        ("RUGGEDCOM-GPS-MIB", "rcGpsLongtitude"),
        ("RUGGEDCOM-GPS-MIB", "rcOFM"),
        ("RUGGEDCOM-GPS-MIB", "rcFreqAdj"))
)
if mibBuilder.loadTexts:
    rcGpsBaseGroup01.setStatus("current")


# Notification objects

rcGpsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 19)
)
rcGpsStatusChange.setObjects(
    ("RUGGEDCOM-GPS-MIB", "rcGpsStatus")
)
if mibBuilder.loadTexts:
    rcGpsStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-GPS-MIB",
    **{"rcGps": rcGps,
       "rcGpsBase": rcGpsBase,
       "rcGpsStatus": rcGpsStatus,
       "rcGpsLocInt": rcGpsLocInt,
       "rcGpsCableCompensate": rcGpsCableCompensate,
       "rcGpsAntPower": rcGpsAntPower,
       "rcSatelliteInView": rcSatelliteInView,
       "rcGpsLatitude": rcGpsLatitude,
       "rcGpsLongtitude": rcGpsLongtitude,
       "rcOFM": rcOFM,
       "rcFreqAdj": rcFreqAdj,
       "rcGpsConformance": rcGpsConformance,
       "rcGpsGroups": rcGpsGroups,
       "rcGpsBaseGroup": rcGpsBaseGroup,
       "rcGpsNotifyGroup": rcGpsNotifyGroup,
       "rcGpsBaseGroup01": rcGpsBaseGroup01,
       "rcGpsStatusChange": rcGpsStatusChange}
)
