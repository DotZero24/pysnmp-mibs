# SNMP MIB module (BRCM-THERMAL-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-THERMAL-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:45 2025
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

(cableDataMgmtMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtMIBObjects")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

thermalMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    thermalMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2006-10-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ThermalMgmtBase_ObjectIdentity = ObjectIdentity
thermalMgmtBase = _ThermalMgmtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1)
)
_ThermalCurrentTemperature_Type = Integer32
_ThermalCurrentTemperature_Object = MibScalar
thermalCurrentTemperature = _ThermalCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 1),
    _ThermalCurrentTemperature_Type()
)
thermalCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thermalCurrentTemperature.setStatus("current")
if mibBuilder.loadTexts:
    thermalCurrentTemperature.setUnits("degrees C")


class _ThermalPowerOffThreshold_Type(Integer32):
    """Custom type thermalPowerOffThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 120),
    )


_ThermalPowerOffThreshold_Type.__name__ = "Integer32"
_ThermalPowerOffThreshold_Object = MibScalar
thermalPowerOffThreshold = _ThermalPowerOffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 2),
    _ThermalPowerOffThreshold_Type()
)
thermalPowerOffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalPowerOffThreshold.setStatus("current")
if mibBuilder.loadTexts:
    thermalPowerOffThreshold.setUnits("degrees C")


class _ThermalPowerOnThreshold_Type(Integer32):
    """Custom type thermalPowerOnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 120),
    )


_ThermalPowerOnThreshold_Type.__name__ = "Integer32"
_ThermalPowerOnThreshold_Object = MibScalar
thermalPowerOnThreshold = _ThermalPowerOnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 3),
    _ThermalPowerOnThreshold_Type()
)
thermalPowerOnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalPowerOnThreshold.setStatus("current")
if mibBuilder.loadTexts:
    thermalPowerOnThreshold.setUnits("degrees C")


class _ThermalPowerOnDelay_Type(Unsigned32):
    """Custom type thermalPowerOnDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_ThermalPowerOnDelay_Type.__name__ = "Unsigned32"
_ThermalPowerOnDelay_Object = MibScalar
thermalPowerOnDelay = _ThermalPowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 4),
    _ThermalPowerOnDelay_Type()
)
thermalPowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalPowerOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    thermalPowerOnDelay.setUnits("250 Milliseconds")


class _ThermalPowerOffDelay_Type(Unsigned32):
    """Custom type thermalPowerOffDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_ThermalPowerOffDelay_Type.__name__ = "Unsigned32"
_ThermalPowerOffDelay_Object = MibScalar
thermalPowerOffDelay = _ThermalPowerOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 5),
    _ThermalPowerOffDelay_Type()
)
thermalPowerOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalPowerOffDelay.setStatus("current")
if mibBuilder.loadTexts:
    thermalPowerOffDelay.setUnits("Seconds")


class _ThermalNotificationDelay_Type(Unsigned32):
    """Custom type thermalNotificationDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_ThermalNotificationDelay_Type.__name__ = "Unsigned32"
_ThermalNotificationDelay_Object = MibScalar
thermalNotificationDelay = _ThermalNotificationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 6),
    _ThermalNotificationDelay_Type()
)
thermalNotificationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalNotificationDelay.setStatus("current")
if mibBuilder.loadTexts:
    thermalNotificationDelay.setUnits("Seconds")


class _ThermalMonitorInitialized_Type(TruthValue):
    """Custom type thermalMonitorInitialized based on TruthValue"""
    defaultValue = 2


_ThermalMonitorInitialized_Type.__name__ = "TruthValue"
_ThermalMonitorInitialized_Object = MibScalar
thermalMonitorInitialized = _ThermalMonitorInitialized_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 11, 1, 7),
    _ThermalMonitorInitialized_Type()
)
thermalMonitorInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thermalMonitorInitialized.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-THERMAL-MGMT-MIB",
    **{"thermalMgmt": thermalMgmt,
       "thermalMgmtBase": thermalMgmtBase,
       "thermalCurrentTemperature": thermalCurrentTemperature,
       "thermalPowerOffThreshold": thermalPowerOffThreshold,
       "thermalPowerOnThreshold": thermalPowerOnThreshold,
       "thermalPowerOnDelay": thermalPowerOnDelay,
       "thermalPowerOffDelay": thermalPowerOffDelay,
       "thermalNotificationDelay": thermalNotificationDelay,
       "thermalMonitorInitialized": thermalMonitorInitialized}
)
