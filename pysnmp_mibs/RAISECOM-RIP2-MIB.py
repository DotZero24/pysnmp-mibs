# SNMP MIB module (RAISECOM-RIP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RIP2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:54 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

(rip2IfStatAddress,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfStatAddress")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomRip2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32)
)
if mibBuilder.loadTexts:
    raisecomRip2.setRevisions(
        ("2011-01-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomRip2Notifications_ObjectIdentity = ObjectIdentity
raisecomRip2Notifications = _RaisecomRip2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 1)
)
_RaisecomRip2Objects_ObjectIdentity = ObjectIdentity
raisecomRip2Objects = _RaisecomRip2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2)
)
_RaisecomRip2ScalarGroup_ObjectIdentity = ObjectIdentity
raisecomRip2ScalarGroup = _RaisecomRip2ScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1)
)


class _RaisecomRip2Enabled_Type(EnableVar):
    """Custom type raisecomRip2Enabled based on EnableVar"""
    defaultValue = 2


_RaisecomRip2Enabled_Type.__name__ = "EnableVar"
_RaisecomRip2Enabled_Object = MibScalar
raisecomRip2Enabled = _RaisecomRip2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 1),
    _RaisecomRip2Enabled_Type()
)
raisecomRip2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2Enabled.setStatus("current")


class _RaisecomRip2Version_Type(Integer32):
    """Custom type raisecomRip2Version based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rip1", 1),
          ("rip2", 2))
    )


_RaisecomRip2Version_Type.__name__ = "Integer32"
_RaisecomRip2Version_Object = MibScalar
raisecomRip2Version = _RaisecomRip2Version_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 2),
    _RaisecomRip2Version_Type()
)
raisecomRip2Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2Version.setStatus("current")


class _RaisecomRip2SourceAddressValidated_Type(EnableVar):
    """Custom type raisecomRip2SourceAddressValidated based on EnableVar"""
    defaultValue = 1


_RaisecomRip2SourceAddressValidated_Type.__name__ = "EnableVar"
_RaisecomRip2SourceAddressValidated_Object = MibScalar
raisecomRip2SourceAddressValidated = _RaisecomRip2SourceAddressValidated_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 3),
    _RaisecomRip2SourceAddressValidated_Type()
)
raisecomRip2SourceAddressValidated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2SourceAddressValidated.setStatus("current")


class _RaisecomRip2HostRouteAccepted_Type(EnableVar):
    """Custom type raisecomRip2HostRouteAccepted based on EnableVar"""
    defaultValue = 1


_RaisecomRip2HostRouteAccepted_Type.__name__ = "EnableVar"
_RaisecomRip2HostRouteAccepted_Object = MibScalar
raisecomRip2HostRouteAccepted = _RaisecomRip2HostRouteAccepted_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 4),
    _RaisecomRip2HostRouteAccepted_Type()
)
raisecomRip2HostRouteAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2HostRouteAccepted.setStatus("current")


class _RaisecomRip2AdminDistance_Type(Integer32):
    """Custom type raisecomRip2AdminDistance based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RaisecomRip2AdminDistance_Type.__name__ = "Integer32"
_RaisecomRip2AdminDistance_Object = MibScalar
raisecomRip2AdminDistance = _RaisecomRip2AdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 5),
    _RaisecomRip2AdminDistance_Type()
)
raisecomRip2AdminDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2AdminDistance.setStatus("current")


class _RaisecomRip2TimerUpdate_Type(Integer32):
    """Custom type raisecomRip2TimerUpdate based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RaisecomRip2TimerUpdate_Type.__name__ = "Integer32"
_RaisecomRip2TimerUpdate_Object = MibScalar
raisecomRip2TimerUpdate = _RaisecomRip2TimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 6),
    _RaisecomRip2TimerUpdate_Type()
)
raisecomRip2TimerUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2TimerUpdate.setStatus("current")


class _RaisecomRip2TimerInvalid_Type(Integer32):
    """Custom type raisecomRip2TimerInvalid based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RaisecomRip2TimerInvalid_Type.__name__ = "Integer32"
_RaisecomRip2TimerInvalid_Object = MibScalar
raisecomRip2TimerInvalid = _RaisecomRip2TimerInvalid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 7),
    _RaisecomRip2TimerInvalid_Type()
)
raisecomRip2TimerInvalid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2TimerInvalid.setStatus("current")


class _RaisecomRip2TimerFlush_Type(Integer32):
    """Custom type raisecomRip2TimerFlush based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RaisecomRip2TimerFlush_Type.__name__ = "Integer32"
_RaisecomRip2TimerFlush_Object = MibScalar
raisecomRip2TimerFlush = _RaisecomRip2TimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 8),
    _RaisecomRip2TimerFlush_Type()
)
raisecomRip2TimerFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2TimerFlush.setStatus("current")


class _RaisecomRip2TimerSuppress_Type(Integer32):
    """Custom type raisecomRip2TimerSuppress based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RaisecomRip2TimerSuppress_Type.__name__ = "Integer32"
_RaisecomRip2TimerSuppress_Object = MibScalar
raisecomRip2TimerSuppress = _RaisecomRip2TimerSuppress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 9),
    _RaisecomRip2TimerSuppress_Type()
)
raisecomRip2TimerSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2TimerSuppress.setStatus("current")


class _RaisecomRip2DatabaseClear_Type(TruthValue):
    """Custom type raisecomRip2DatabaseClear based on TruthValue"""
    defaultValue = 2


_RaisecomRip2DatabaseClear_Type.__name__ = "TruthValue"
_RaisecomRip2DatabaseClear_Object = MibScalar
raisecomRip2DatabaseClear = _RaisecomRip2DatabaseClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 10),
    _RaisecomRip2DatabaseClear_Type()
)
raisecomRip2DatabaseClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DatabaseClear.setStatus("current")


class _RaisecomRip2StatisticsClear_Type(TruthValue):
    """Custom type raisecomRip2StatisticsClear based on TruthValue"""
    defaultValue = 2


_RaisecomRip2StatisticsClear_Type.__name__ = "TruthValue"
_RaisecomRip2StatisticsClear_Object = MibScalar
raisecomRip2StatisticsClear = _RaisecomRip2StatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 11),
    _RaisecomRip2StatisticsClear_Type()
)
raisecomRip2StatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2StatisticsClear.setStatus("current")


class _RaisecomRip2TrapEnable_Type(EnableVar):
    """Custom type raisecomRip2TrapEnable based on EnableVar"""
    defaultValue = 2


_RaisecomRip2TrapEnable_Type.__name__ = "EnableVar"
_RaisecomRip2TrapEnable_Object = MibScalar
raisecomRip2TrapEnable = _RaisecomRip2TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 12),
    _RaisecomRip2TrapEnable_Type()
)
raisecomRip2TrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2TrapEnable.setStatus("current")


class _RaisecomRip2DefaultMetric_Type(Integer32):
    """Custom type raisecomRip2DefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RaisecomRip2DefaultMetric_Type.__name__ = "Integer32"
_RaisecomRip2DefaultMetric_Object = MibScalar
raisecomRip2DefaultMetric = _RaisecomRip2DefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 1, 13),
    _RaisecomRip2DefaultMetric_Type()
)
raisecomRip2DefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DefaultMetric.setStatus("current")
_RaisecomRip2InterfaceConfigGroup_ObjectIdentity = ObjectIdentity
raisecomRip2InterfaceConfigGroup = _RaisecomRip2InterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2)
)
_RaisecomRip2IfConfTable_Object = MibTable
raisecomRip2IfConfTable = _RaisecomRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomRip2IfConfTable.setStatus("current")
_RaisecomRip2IfConfEntry_Object = MibTableRow
raisecomRip2IfConfEntry = _RaisecomRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1)
)
raisecomRip2IfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRip2IfConfEntry.setStatus("current")


class _RaisecomRip2IfConfPassiveInterface_Type(EnableVar):
    """Custom type raisecomRip2IfConfPassiveInterface based on EnableVar"""
    defaultValue = 2


_RaisecomRip2IfConfPassiveInterface_Type.__name__ = "EnableVar"
_RaisecomRip2IfConfPassiveInterface_Object = MibTableColumn
raisecomRip2IfConfPassiveInterface = _RaisecomRip2IfConfPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 1),
    _RaisecomRip2IfConfPassiveInterface_Type()
)
raisecomRip2IfConfPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfPassiveInterface.setStatus("current")


class _RaisecomRip2IfConfSendVersion_Type(Integer32):
    """Custom type raisecomRip2IfConfSendVersion based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("rip1", 1),
          ("rip1Compatible", 2),
          ("rip2", 3))
    )


_RaisecomRip2IfConfSendVersion_Type.__name__ = "Integer32"
_RaisecomRip2IfConfSendVersion_Object = MibTableColumn
raisecomRip2IfConfSendVersion = _RaisecomRip2IfConfSendVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 2),
    _RaisecomRip2IfConfSendVersion_Type()
)
raisecomRip2IfConfSendVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfSendVersion.setStatus("current")


class _RaisecomRip2IfConfReceiveVersion_Type(Integer32):
    """Custom type raisecomRip2IfConfReceiveVersion based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3))
    )


_RaisecomRip2IfConfReceiveVersion_Type.__name__ = "Integer32"
_RaisecomRip2IfConfReceiveVersion_Object = MibTableColumn
raisecomRip2IfConfReceiveVersion = _RaisecomRip2IfConfReceiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 3),
    _RaisecomRip2IfConfReceiveVersion_Type()
)
raisecomRip2IfConfReceiveVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfReceiveVersion.setStatus("current")


class _RaisecomRip2IfConfAuthMode_Type(Integer32):
    """Custom type raisecomRip2IfConfAuthMode based on Integer32"""
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
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3))
    )


_RaisecomRip2IfConfAuthMode_Type.__name__ = "Integer32"
_RaisecomRip2IfConfAuthMode_Object = MibTableColumn
raisecomRip2IfConfAuthMode = _RaisecomRip2IfConfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 4),
    _RaisecomRip2IfConfAuthMode_Type()
)
raisecomRip2IfConfAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfAuthMode.setStatus("current")


class _RaisecomRip2IfConfInputMetricOffset_Type(Integer32):
    """Custom type raisecomRip2IfConfInputMetricOffset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RaisecomRip2IfConfInputMetricOffset_Type.__name__ = "Integer32"
_RaisecomRip2IfConfInputMetricOffset_Object = MibTableColumn
raisecomRip2IfConfInputMetricOffset = _RaisecomRip2IfConfInputMetricOffset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 5),
    _RaisecomRip2IfConfInputMetricOffset_Type()
)
raisecomRip2IfConfInputMetricOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfInputMetricOffset.setStatus("current")


class _RaisecomRip2IfConfOutputMetricOffset_Type(Integer32):
    """Custom type raisecomRip2IfConfOutputMetricOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RaisecomRip2IfConfOutputMetricOffset_Type.__name__ = "Integer32"
_RaisecomRip2IfConfOutputMetricOffset_Object = MibTableColumn
raisecomRip2IfConfOutputMetricOffset = _RaisecomRip2IfConfOutputMetricOffset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 6),
    _RaisecomRip2IfConfOutputMetricOffset_Type()
)
raisecomRip2IfConfOutputMetricOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfOutputMetricOffset.setStatus("current")


class _RaisecomRip2IfConfSplitHorizon_Type(EnableVar):
    """Custom type raisecomRip2IfConfSplitHorizon based on EnableVar"""
    defaultValue = 1


_RaisecomRip2IfConfSplitHorizon_Type.__name__ = "EnableVar"
_RaisecomRip2IfConfSplitHorizon_Object = MibTableColumn
raisecomRip2IfConfSplitHorizon = _RaisecomRip2IfConfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 7),
    _RaisecomRip2IfConfSplitHorizon_Type()
)
raisecomRip2IfConfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfSplitHorizon.setStatus("current")


class _RaisecomRip2IfConfPoisonReverse_Type(EnableVar):
    """Custom type raisecomRip2IfConfPoisonReverse based on EnableVar"""
    defaultValue = 2


_RaisecomRip2IfConfPoisonReverse_Type.__name__ = "EnableVar"
_RaisecomRip2IfConfPoisonReverse_Object = MibTableColumn
raisecomRip2IfConfPoisonReverse = _RaisecomRip2IfConfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 8),
    _RaisecomRip2IfConfPoisonReverse_Type()
)
raisecomRip2IfConfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfPoisonReverse.setStatus("current")


class _RaisecomRip2IfConfDatabaseClear_Type(TruthValue):
    """Custom type raisecomRip2IfConfDatabaseClear based on TruthValue"""
    defaultValue = 2


_RaisecomRip2IfConfDatabaseClear_Type.__name__ = "TruthValue"
_RaisecomRip2IfConfDatabaseClear_Object = MibTableColumn
raisecomRip2IfConfDatabaseClear = _RaisecomRip2IfConfDatabaseClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 9),
    _RaisecomRip2IfConfDatabaseClear_Type()
)
raisecomRip2IfConfDatabaseClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfDatabaseClear.setStatus("current")


class _RaisecomRip2IfConfStatisticClear_Type(TruthValue):
    """Custom type raisecomRip2IfConfStatisticClear based on TruthValue"""
    defaultValue = 2


_RaisecomRip2IfConfStatisticClear_Type.__name__ = "TruthValue"
_RaisecomRip2IfConfStatisticClear_Object = MibTableColumn
raisecomRip2IfConfStatisticClear = _RaisecomRip2IfConfStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 10),
    _RaisecomRip2IfConfStatisticClear_Type()
)
raisecomRip2IfConfStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfStatisticClear.setStatus("current")


class _RaisecomRip2IfConfAuthKeyChain_Type(OctetString):
    """Custom type raisecomRip2IfConfAuthKeyChain based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RaisecomRip2IfConfAuthKeyChain_Type.__name__ = "OctetString"
_RaisecomRip2IfConfAuthKeyChain_Object = MibTableColumn
raisecomRip2IfConfAuthKeyChain = _RaisecomRip2IfConfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 2, 1, 1, 11),
    _RaisecomRip2IfConfAuthKeyChain_Type()
)
raisecomRip2IfConfAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2IfConfAuthKeyChain.setStatus("current")
_RaisecomRip2InterfaceStatisticGroup_ObjectIdentity = ObjectIdentity
raisecomRip2InterfaceStatisticGroup = _RaisecomRip2InterfaceStatisticGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 3)
)
_RaisecomRip2IfStatsTable_Object = MibTable
raisecomRip2IfStatsTable = _RaisecomRip2IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 3, 1)
)
if mibBuilder.loadTexts:
    raisecomRip2IfStatsTable.setStatus("current")
_RaisecomRip2IfStatsEntry_Object = MibTableRow
raisecomRip2IfStatsEntry = _RaisecomRip2IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 3, 1, 1)
)
raisecomRip2IfStatsEntry.setIndexNames(
    (0, "RIPv2-MIB", "rip2IfStatAddress"),
)
if mibBuilder.loadTexts:
    raisecomRip2IfStatsEntry.setStatus("current")
_RaisecomRip2IfStatsRecvValid_Type = Counter32
_RaisecomRip2IfStatsRecvValid_Object = MibTableColumn
raisecomRip2IfStatsRecvValid = _RaisecomRip2IfStatsRecvValid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 3, 1, 1, 1),
    _RaisecomRip2IfStatsRecvValid_Type()
)
raisecomRip2IfStatsRecvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2IfStatsRecvValid.setStatus("current")
_RaisecomRip2NetConfigGroup_ObjectIdentity = ObjectIdentity
raisecomRip2NetConfigGroup = _RaisecomRip2NetConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 4)
)
_RaisecomRip2NetConfTable_Object = MibTable
raisecomRip2NetConfTable = _RaisecomRip2NetConfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 4, 1)
)
if mibBuilder.loadTexts:
    raisecomRip2NetConfTable.setStatus("current")
_RaisecomRip2NetConfEntry_Object = MibTableRow
raisecomRip2NetConfEntry = _RaisecomRip2NetConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 4, 1, 1)
)
raisecomRip2NetConfEntry.setIndexNames(
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2NetConfNetwork"),
)
if mibBuilder.loadTexts:
    raisecomRip2NetConfEntry.setStatus("current")
_RaisecomRip2NetConfNetwork_Type = IpAddress
_RaisecomRip2NetConfNetwork_Object = MibTableColumn
raisecomRip2NetConfNetwork = _RaisecomRip2NetConfNetwork_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 4, 1, 1, 1),
    _RaisecomRip2NetConfNetwork_Type()
)
raisecomRip2NetConfNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRip2NetConfNetwork.setStatus("current")
_RaisecomRip2NetConfRowStatus_Type = RowStatus
_RaisecomRip2NetConfRowStatus_Object = MibTableColumn
raisecomRip2NetConfRowStatus = _RaisecomRip2NetConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 4, 1, 1, 2),
    _RaisecomRip2NetConfRowStatus_Type()
)
raisecomRip2NetConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2NetConfRowStatus.setStatus("current")
_RaisecomRip2RouteGroup_ObjectIdentity = ObjectIdentity
raisecomRip2RouteGroup = _RaisecomRip2RouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5)
)
_RaisecomRip2RouteTable_Object = MibTable
raisecomRip2RouteTable = _RaisecomRip2RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1)
)
if mibBuilder.loadTexts:
    raisecomRip2RouteTable.setStatus("current")
_RaisecomRip2RouteEntry_Object = MibTableRow
raisecomRip2RouteEntry = _RaisecomRip2RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1)
)
raisecomRip2RouteEntry.setIndexNames(
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2RouteDest"),
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2RouteMask"),
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2RouteNextHop"),
)
if mibBuilder.loadTexts:
    raisecomRip2RouteEntry.setStatus("current")
_RaisecomRip2RouteDest_Type = IpAddress
_RaisecomRip2RouteDest_Object = MibTableColumn
raisecomRip2RouteDest = _RaisecomRip2RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 1),
    _RaisecomRip2RouteDest_Type()
)
raisecomRip2RouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteDest.setStatus("current")
_RaisecomRip2RouteMask_Type = IpAddress
_RaisecomRip2RouteMask_Object = MibTableColumn
raisecomRip2RouteMask = _RaisecomRip2RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 2),
    _RaisecomRip2RouteMask_Type()
)
raisecomRip2RouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteMask.setStatus("current")
_RaisecomRip2RouteNextHop_Type = IpAddress
_RaisecomRip2RouteNextHop_Object = MibTableColumn
raisecomRip2RouteNextHop = _RaisecomRip2RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 3),
    _RaisecomRip2RouteNextHop_Type()
)
raisecomRip2RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteNextHop.setStatus("current")
_RaisecomRip2RouteLearnFrom_Type = IpAddress
_RaisecomRip2RouteLearnFrom_Object = MibTableColumn
raisecomRip2RouteLearnFrom = _RaisecomRip2RouteLearnFrom_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 4),
    _RaisecomRip2RouteLearnFrom_Type()
)
raisecomRip2RouteLearnFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteLearnFrom.setStatus("current")
_RaisecomRip2RouteIfIndex_Type = Integer32
_RaisecomRip2RouteIfIndex_Object = MibTableColumn
raisecomRip2RouteIfIndex = _RaisecomRip2RouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 5),
    _RaisecomRip2RouteIfIndex_Type()
)
raisecomRip2RouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteIfIndex.setStatus("current")


class _RaisecomRip2RouteMetric_Type(Integer32):
    """Custom type raisecomRip2RouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RaisecomRip2RouteMetric_Type.__name__ = "Integer32"
_RaisecomRip2RouteMetric_Object = MibTableColumn
raisecomRip2RouteMetric = _RaisecomRip2RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 6),
    _RaisecomRip2RouteMetric_Type()
)
raisecomRip2RouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteMetric.setStatus("current")


class _RaisecomRip2RouteProtoType_Type(Integer32):
    """Custom type raisecomRip2RouteProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("is-is", 9),
          ("es-is", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14))
    )


_RaisecomRip2RouteProtoType_Type.__name__ = "Integer32"
_RaisecomRip2RouteProtoType_Object = MibTableColumn
raisecomRip2RouteProtoType = _RaisecomRip2RouteProtoType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 7),
    _RaisecomRip2RouteProtoType_Type()
)
raisecomRip2RouteProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteProtoType.setStatus("current")


class _RaisecomRip2RouteStatus_Type(Bits):
    """Custom type raisecomRip2RouteStatus based on Bits"""
    namedValues = NamedValues(
        *(("permenant", 1),
          ("aging", 2),
          ("suppress", 3),
          ("flush", 4))
    )

_RaisecomRip2RouteStatus_Type.__name__ = "Bits"
_RaisecomRip2RouteStatus_Object = MibTableColumn
raisecomRip2RouteStatus = _RaisecomRip2RouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 8),
    _RaisecomRip2RouteStatus_Type()
)
raisecomRip2RouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteStatus.setStatus("current")


class _RaisecomRip2RouteTimer_Type(Integer32):
    """Custom type raisecomRip2RouteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RaisecomRip2RouteTimer_Type.__name__ = "Integer32"
_RaisecomRip2RouteTimer_Object = MibTableColumn
raisecomRip2RouteTimer = _RaisecomRip2RouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 5, 1, 1, 9),
    _RaisecomRip2RouteTimer_Type()
)
raisecomRip2RouteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RouteTimer.setStatus("current")
_RaisecomRip2RedistributeListGroup_ObjectIdentity = ObjectIdentity
raisecomRip2RedistributeListGroup = _RaisecomRip2RedistributeListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6)
)
_RaisecomRip2RedistributeTable_Object = MibTable
raisecomRip2RedistributeTable = _RaisecomRip2RedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1)
)
if mibBuilder.loadTexts:
    raisecomRip2RedistributeTable.setStatus("current")
_RaisecomRip2RedistributeEntry_Object = MibTableRow
raisecomRip2RedistributeEntry = _RaisecomRip2RedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1, 1)
)
raisecomRip2RedistributeEntry.setIndexNames(
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2RedistributeProtocol"),
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2RedistributeProcessId"),
)
if mibBuilder.loadTexts:
    raisecomRip2RedistributeEntry.setStatus("current")


class _RaisecomRip2RedistributeProtocol_Type(Integer32):
    """Custom type raisecomRip2RedistributeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              13)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("netmgmt", 3),
          ("ospf", 13))
    )


_RaisecomRip2RedistributeProtocol_Type.__name__ = "Integer32"
_RaisecomRip2RedistributeProtocol_Object = MibTableColumn
raisecomRip2RedistributeProtocol = _RaisecomRip2RedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1, 1, 1),
    _RaisecomRip2RedistributeProtocol_Type()
)
raisecomRip2RedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RedistributeProtocol.setStatus("current")


class _RaisecomRip2RedistributeProcessId_Type(Unsigned32):
    """Custom type raisecomRip2RedistributeProcessId based on Unsigned32"""
    defaultValue = 5


_RaisecomRip2RedistributeProcessId_Type.__name__ = "Unsigned32"
_RaisecomRip2RedistributeProcessId_Object = MibTableColumn
raisecomRip2RedistributeProcessId = _RaisecomRip2RedistributeProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1, 1, 2),
    _RaisecomRip2RedistributeProcessId_Type()
)
raisecomRip2RedistributeProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2RedistributeProcessId.setStatus("current")
_RaisecomRip2RedistributeMetric_Type = Integer32
_RaisecomRip2RedistributeMetric_Object = MibTableColumn
raisecomRip2RedistributeMetric = _RaisecomRip2RedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1, 1, 3),
    _RaisecomRip2RedistributeMetric_Type()
)
raisecomRip2RedistributeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2RedistributeMetric.setStatus("current")


class _RaisecomRip2RedistributeRouteMapName_Type(OctetString):
    """Custom type raisecomRip2RedistributeRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2RedistributeRouteMapName_Type.__name__ = "OctetString"
_RaisecomRip2RedistributeRouteMapName_Object = MibTableColumn
raisecomRip2RedistributeRouteMapName = _RaisecomRip2RedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1, 1, 4),
    _RaisecomRip2RedistributeRouteMapName_Type()
)
raisecomRip2RedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2RedistributeRouteMapName.setStatus("current")
_RaisecomRip2RedistributeRowStatus_Type = RowStatus
_RaisecomRip2RedistributeRowStatus_Object = MibTableColumn
raisecomRip2RedistributeRowStatus = _RaisecomRip2RedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 6, 1, 1, 5),
    _RaisecomRip2RedistributeRowStatus_Type()
)
raisecomRip2RedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2RedistributeRowStatus.setStatus("current")
_RaisecomRip2DistributeListGroup_ObjectIdentity = ObjectIdentity
raisecomRip2DistributeListGroup = _RaisecomRip2DistributeListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7)
)
_RaisecomRip2DistributeListTable_Object = MibTable
raisecomRip2DistributeListTable = _RaisecomRip2DistributeListTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1)
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListTable.setStatus("current")
_RaisecomRip2DistributeListEntry_Object = MibTableRow
raisecomRip2DistributeListEntry = _RaisecomRip2DistributeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1)
)
raisecomRip2DistributeListEntry.setIndexNames(
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2DistrIndex"),
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListEntry.setStatus("current")
_RaisecomRip2DistrIndex_Type = Integer32
_RaisecomRip2DistrIndex_Object = MibTableColumn
raisecomRip2DistrIndex = _RaisecomRip2DistrIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1, 1),
    _RaisecomRip2DistrIndex_Type()
)
raisecomRip2DistrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2DistrIndex.setStatus("current")
_RaisecomRip2DistrInAclNum_Type = Integer32
_RaisecomRip2DistrInAclNum_Object = MibTableColumn
raisecomRip2DistrInAclNum = _RaisecomRip2DistrInAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1, 2),
    _RaisecomRip2DistrInAclNum_Type()
)
raisecomRip2DistrInAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrInAclNum.setStatus("current")


class _RaisecomRip2DistrInIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrInIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrInIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrInIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrInIpPrefixListName = _RaisecomRip2DistrInIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1, 3),
    _RaisecomRip2DistrInIpPrefixListName_Type()
)
raisecomRip2DistrInIpPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrInIpPrefixListName.setStatus("current")


class _RaisecomRip2DistrInGatewayIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrInGatewayIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrInGatewayIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrInGatewayIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrInGatewayIpPrefixListName = _RaisecomRip2DistrInGatewayIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1, 4),
    _RaisecomRip2DistrInGatewayIpPrefixListName_Type()
)
raisecomRip2DistrInGatewayIpPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrInGatewayIpPrefixListName.setStatus("current")
_RaisecomRip2DistrOutAclNum_Type = Integer32
_RaisecomRip2DistrOutAclNum_Object = MibTableColumn
raisecomRip2DistrOutAclNum = _RaisecomRip2DistrOutAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1, 5),
    _RaisecomRip2DistrOutAclNum_Type()
)
raisecomRip2DistrOutAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutAclNum.setStatus("current")


class _RaisecomRip2DistrOutIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrOutIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrOutIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrOutIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrOutIpPrefixListName = _RaisecomRip2DistrOutIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 1, 1, 6),
    _RaisecomRip2DistrOutIpPrefixListName_Type()
)
raisecomRip2DistrOutIpPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutIpPrefixListName.setStatus("current")
_RaisecomRip2DistributeListInInterfaceTable_Object = MibTable
raisecomRip2DistributeListInInterfaceTable = _RaisecomRip2DistributeListInInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 2)
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListInInterfaceTable.setStatus("current")
_RaisecomRip2DistributeListInInterfaceEntry_Object = MibTableRow
raisecomRip2DistributeListInInterfaceEntry = _RaisecomRip2DistributeListInInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 2, 1)
)
raisecomRip2DistributeListInInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListInInterfaceEntry.setStatus("current")


class _RaisecomRip2DistrInIfIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrInIfIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrInIfIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrInIfIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrInIfIpPrefixListName = _RaisecomRip2DistrInIfIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 2, 1, 1),
    _RaisecomRip2DistrInIfIpPrefixListName_Type()
)
raisecomRip2DistrInIfIpPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrInIfIpPrefixListName.setStatus("current")


class _RaisecomRip2DistrInIfGatewayIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrInIfGatewayIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrInIfGatewayIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrInIfGatewayIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrInIfGatewayIpPrefixListName = _RaisecomRip2DistrInIfGatewayIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 2, 1, 2),
    _RaisecomRip2DistrInIfGatewayIpPrefixListName_Type()
)
raisecomRip2DistrInIfGatewayIpPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrInIfGatewayIpPrefixListName.setStatus("current")
_RaisecomRip2DistrInIfAclNum_Type = Integer32
_RaisecomRip2DistrInIfAclNum_Object = MibTableColumn
raisecomRip2DistrInIfAclNum = _RaisecomRip2DistrInIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 2, 1, 3),
    _RaisecomRip2DistrInIfAclNum_Type()
)
raisecomRip2DistrInIfAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrInIfAclNum.setStatus("current")
_RaisecomRip2DistributeListOutInterfaceTable_Object = MibTable
raisecomRip2DistributeListOutInterfaceTable = _RaisecomRip2DistributeListOutInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 3)
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListOutInterfaceTable.setStatus("current")
_RaisecomRip2DistributeListOutInterfaceEntry_Object = MibTableRow
raisecomRip2DistributeListOutInterfaceEntry = _RaisecomRip2DistributeListOutInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 3, 1)
)
raisecomRip2DistributeListOutInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListOutInterfaceEntry.setStatus("current")


class _RaisecomRip2DistrOutIfIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrOutIfIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrOutIfIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrOutIfIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrOutIfIpPrefixListName = _RaisecomRip2DistrOutIfIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 3, 1, 1),
    _RaisecomRip2DistrOutIfIpPrefixListName_Type()
)
raisecomRip2DistrOutIfIpPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutIfIpPrefixListName.setStatus("current")
_RaisecomRip2DistrOutIfAclNum_Type = Integer32
_RaisecomRip2DistrOutIfAclNum_Object = MibTableColumn
raisecomRip2DistrOutIfAclNum = _RaisecomRip2DistrOutIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 3, 1, 2),
    _RaisecomRip2DistrOutIfAclNum_Type()
)
raisecomRip2DistrOutIfAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutIfAclNum.setStatus("current")
_RaisecomRip2DistributeListOutProtocolTable_Object = MibTable
raisecomRip2DistributeListOutProtocolTable = _RaisecomRip2DistributeListOutProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4)
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListOutProtocolTable.setStatus("current")
_RaisecomRip2DistributeListOutProtocolEntry_Object = MibTableRow
raisecomRip2DistributeListOutProtocolEntry = _RaisecomRip2DistributeListOutProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4, 1)
)
raisecomRip2DistributeListOutProtocolEntry.setIndexNames(
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2DistrOutProtocol"),
    (0, "RAISECOM-RIP2-MIB", "raisecomRip2DistrOutProcessId"),
)
if mibBuilder.loadTexts:
    raisecomRip2DistributeListOutProtocolEntry.setStatus("current")


class _RaisecomRip2DistrOutProtocol_Type(Integer32):
    """Custom type raisecomRip2DistrOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              13)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("netmgmt", 3),
          ("ospf", 13))
    )


_RaisecomRip2DistrOutProtocol_Type.__name__ = "Integer32"
_RaisecomRip2DistrOutProtocol_Object = MibTableColumn
raisecomRip2DistrOutProtocol = _RaisecomRip2DistrOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4, 1, 1),
    _RaisecomRip2DistrOutProtocol_Type()
)
raisecomRip2DistrOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutProtocol.setStatus("current")


class _RaisecomRip2DistrOutProcessId_Type(Unsigned32):
    """Custom type raisecomRip2DistrOutProcessId based on Unsigned32"""
    defaultValue = 5


_RaisecomRip2DistrOutProcessId_Type.__name__ = "Unsigned32"
_RaisecomRip2DistrOutProcessId_Object = MibTableColumn
raisecomRip2DistrOutProcessId = _RaisecomRip2DistrOutProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4, 1, 2),
    _RaisecomRip2DistrOutProcessId_Type()
)
raisecomRip2DistrOutProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutProcessId.setStatus("current")


class _RaisecomRip2DistrOutProIpPrefixListName_Type(OctetString):
    """Custom type raisecomRip2DistrOutProIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RaisecomRip2DistrOutProIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomRip2DistrOutProIpPrefixListName_Object = MibTableColumn
raisecomRip2DistrOutProIpPrefixListName = _RaisecomRip2DistrOutProIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4, 1, 3),
    _RaisecomRip2DistrOutProIpPrefixListName_Type()
)
raisecomRip2DistrOutProIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutProIpPrefixListName.setStatus("current")
_RaisecomRip2DistrOutProAclNum_Type = Integer32
_RaisecomRip2DistrOutProAclNum_Object = MibTableColumn
raisecomRip2DistrOutProAclNum = _RaisecomRip2DistrOutProAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4, 1, 4),
    _RaisecomRip2DistrOutProAclNum_Type()
)
raisecomRip2DistrOutProAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutProAclNum.setStatus("current")
_RaisecomRip2DistrOutProRowStatus_Type = RowStatus
_RaisecomRip2DistrOutProRowStatus_Object = MibTableColumn
raisecomRip2DistrOutProRowStatus = _RaisecomRip2DistrOutProRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 2, 7, 4, 1, 5),
    _RaisecomRip2DistrOutProRowStatus_Type()
)
raisecomRip2DistrOutProRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRip2DistrOutProRowStatus.setStatus("current")
_RaisecomRip2Conformance_ObjectIdentity = ObjectIdentity
raisecomRip2Conformance = _RaisecomRip2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 3)
)

# Managed Objects groups


# Notification objects

raisecomRip2LastKeyExpirationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 1, 1)
)
raisecomRip2LastKeyExpirationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RAISECOM-RIP2-MIB", "raisecomRip2IfConfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    raisecomRip2LastKeyExpirationTrap.setStatus(
        "current"
    )

raisecomRip2KeyValidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 32, 1, 2)
)
raisecomRip2KeyValidTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RAISECOM-RIP2-MIB", "raisecomRip2IfConfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    raisecomRip2KeyValidTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RIP2-MIB",
    **{"raisecomRip2": raisecomRip2,
       "raisecomRip2Notifications": raisecomRip2Notifications,
       "raisecomRip2LastKeyExpirationTrap": raisecomRip2LastKeyExpirationTrap,
       "raisecomRip2KeyValidTrap": raisecomRip2KeyValidTrap,
       "raisecomRip2Objects": raisecomRip2Objects,
       "raisecomRip2ScalarGroup": raisecomRip2ScalarGroup,
       "raisecomRip2Enabled": raisecomRip2Enabled,
       "raisecomRip2Version": raisecomRip2Version,
       "raisecomRip2SourceAddressValidated": raisecomRip2SourceAddressValidated,
       "raisecomRip2HostRouteAccepted": raisecomRip2HostRouteAccepted,
       "raisecomRip2AdminDistance": raisecomRip2AdminDistance,
       "raisecomRip2TimerUpdate": raisecomRip2TimerUpdate,
       "raisecomRip2TimerInvalid": raisecomRip2TimerInvalid,
       "raisecomRip2TimerFlush": raisecomRip2TimerFlush,
       "raisecomRip2TimerSuppress": raisecomRip2TimerSuppress,
       "raisecomRip2DatabaseClear": raisecomRip2DatabaseClear,
       "raisecomRip2StatisticsClear": raisecomRip2StatisticsClear,
       "raisecomRip2TrapEnable": raisecomRip2TrapEnable,
       "raisecomRip2DefaultMetric": raisecomRip2DefaultMetric,
       "raisecomRip2InterfaceConfigGroup": raisecomRip2InterfaceConfigGroup,
       "raisecomRip2IfConfTable": raisecomRip2IfConfTable,
       "raisecomRip2IfConfEntry": raisecomRip2IfConfEntry,
       "raisecomRip2IfConfPassiveInterface": raisecomRip2IfConfPassiveInterface,
       "raisecomRip2IfConfSendVersion": raisecomRip2IfConfSendVersion,
       "raisecomRip2IfConfReceiveVersion": raisecomRip2IfConfReceiveVersion,
       "raisecomRip2IfConfAuthMode": raisecomRip2IfConfAuthMode,
       "raisecomRip2IfConfInputMetricOffset": raisecomRip2IfConfInputMetricOffset,
       "raisecomRip2IfConfOutputMetricOffset": raisecomRip2IfConfOutputMetricOffset,
       "raisecomRip2IfConfSplitHorizon": raisecomRip2IfConfSplitHorizon,
       "raisecomRip2IfConfPoisonReverse": raisecomRip2IfConfPoisonReverse,
       "raisecomRip2IfConfDatabaseClear": raisecomRip2IfConfDatabaseClear,
       "raisecomRip2IfConfStatisticClear": raisecomRip2IfConfStatisticClear,
       "raisecomRip2IfConfAuthKeyChain": raisecomRip2IfConfAuthKeyChain,
       "raisecomRip2InterfaceStatisticGroup": raisecomRip2InterfaceStatisticGroup,
       "raisecomRip2IfStatsTable": raisecomRip2IfStatsTable,
       "raisecomRip2IfStatsEntry": raisecomRip2IfStatsEntry,
       "raisecomRip2IfStatsRecvValid": raisecomRip2IfStatsRecvValid,
       "raisecomRip2NetConfigGroup": raisecomRip2NetConfigGroup,
       "raisecomRip2NetConfTable": raisecomRip2NetConfTable,
       "raisecomRip2NetConfEntry": raisecomRip2NetConfEntry,
       "raisecomRip2NetConfNetwork": raisecomRip2NetConfNetwork,
       "raisecomRip2NetConfRowStatus": raisecomRip2NetConfRowStatus,
       "raisecomRip2RouteGroup": raisecomRip2RouteGroup,
       "raisecomRip2RouteTable": raisecomRip2RouteTable,
       "raisecomRip2RouteEntry": raisecomRip2RouteEntry,
       "raisecomRip2RouteDest": raisecomRip2RouteDest,
       "raisecomRip2RouteMask": raisecomRip2RouteMask,
       "raisecomRip2RouteNextHop": raisecomRip2RouteNextHop,
       "raisecomRip2RouteLearnFrom": raisecomRip2RouteLearnFrom,
       "raisecomRip2RouteIfIndex": raisecomRip2RouteIfIndex,
       "raisecomRip2RouteMetric": raisecomRip2RouteMetric,
       "raisecomRip2RouteProtoType": raisecomRip2RouteProtoType,
       "raisecomRip2RouteStatus": raisecomRip2RouteStatus,
       "raisecomRip2RouteTimer": raisecomRip2RouteTimer,
       "raisecomRip2RedistributeListGroup": raisecomRip2RedistributeListGroup,
       "raisecomRip2RedistributeTable": raisecomRip2RedistributeTable,
       "raisecomRip2RedistributeEntry": raisecomRip2RedistributeEntry,
       "raisecomRip2RedistributeProtocol": raisecomRip2RedistributeProtocol,
       "raisecomRip2RedistributeProcessId": raisecomRip2RedistributeProcessId,
       "raisecomRip2RedistributeMetric": raisecomRip2RedistributeMetric,
       "raisecomRip2RedistributeRouteMapName": raisecomRip2RedistributeRouteMapName,
       "raisecomRip2RedistributeRowStatus": raisecomRip2RedistributeRowStatus,
       "raisecomRip2DistributeListGroup": raisecomRip2DistributeListGroup,
       "raisecomRip2DistributeListTable": raisecomRip2DistributeListTable,
       "raisecomRip2DistributeListEntry": raisecomRip2DistributeListEntry,
       "raisecomRip2DistrIndex": raisecomRip2DistrIndex,
       "raisecomRip2DistrInAclNum": raisecomRip2DistrInAclNum,
       "raisecomRip2DistrInIpPrefixListName": raisecomRip2DistrInIpPrefixListName,
       "raisecomRip2DistrInGatewayIpPrefixListName": raisecomRip2DistrInGatewayIpPrefixListName,
       "raisecomRip2DistrOutAclNum": raisecomRip2DistrOutAclNum,
       "raisecomRip2DistrOutIpPrefixListName": raisecomRip2DistrOutIpPrefixListName,
       "raisecomRip2DistributeListInInterfaceTable": raisecomRip2DistributeListInInterfaceTable,
       "raisecomRip2DistributeListInInterfaceEntry": raisecomRip2DistributeListInInterfaceEntry,
       "raisecomRip2DistrInIfIpPrefixListName": raisecomRip2DistrInIfIpPrefixListName,
       "raisecomRip2DistrInIfGatewayIpPrefixListName": raisecomRip2DistrInIfGatewayIpPrefixListName,
       "raisecomRip2DistrInIfAclNum": raisecomRip2DistrInIfAclNum,
       "raisecomRip2DistributeListOutInterfaceTable": raisecomRip2DistributeListOutInterfaceTable,
       "raisecomRip2DistributeListOutInterfaceEntry": raisecomRip2DistributeListOutInterfaceEntry,
       "raisecomRip2DistrOutIfIpPrefixListName": raisecomRip2DistrOutIfIpPrefixListName,
       "raisecomRip2DistrOutIfAclNum": raisecomRip2DistrOutIfAclNum,
       "raisecomRip2DistributeListOutProtocolTable": raisecomRip2DistributeListOutProtocolTable,
       "raisecomRip2DistributeListOutProtocolEntry": raisecomRip2DistributeListOutProtocolEntry,
       "raisecomRip2DistrOutProtocol": raisecomRip2DistrOutProtocol,
       "raisecomRip2DistrOutProcessId": raisecomRip2DistrOutProcessId,
       "raisecomRip2DistrOutProIpPrefixListName": raisecomRip2DistrOutProIpPrefixListName,
       "raisecomRip2DistrOutProAclNum": raisecomRip2DistrOutProAclNum,
       "raisecomRip2DistrOutProRowStatus": raisecomRip2DistrOutProRowStatus,
       "raisecomRip2Conformance": raisecomRip2Conformance}
)
