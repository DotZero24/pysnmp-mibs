# SNMP MIB module (BEGEMOT-LM75-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bsd/BEGEMOT-LM75-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:21:21 2025
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

begemotLm75 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400)
)
if mibBuilder.loadTexts:
    begemotLm75.setRevisions(
        ("2018-10-24 00:00",
         "2014-02-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotLm75Objects_ObjectIdentity = ObjectIdentity
begemotLm75Objects = _BegemotLm75Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1)
)
_Lm75Sensor_ObjectIdentity = ObjectIdentity
lm75Sensor = _Lm75Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 1)
)
_Lm75Sensors_Type = Integer32
_Lm75Sensors_Object = MibScalar
lm75Sensors = _Lm75Sensors_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 1, 1),
    _Lm75Sensors_Type()
)
lm75Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75Sensors.setStatus("current")
_Lm75SensorTable_Object = MibTable
lm75SensorTable = _Lm75SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2)
)
if mibBuilder.loadTexts:
    lm75SensorTable.setStatus("current")
_Lm75SensorEntry_Object = MibTableRow
lm75SensorEntry = _Lm75SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1)
)
lm75SensorEntry.setIndexNames(
    (0, "BEGEMOT-LM75-MIB", "lm75SensorIndex"),
)
if mibBuilder.loadTexts:
    lm75SensorEntry.setStatus("current")
_Lm75SensorIndex_Type = Integer32
_Lm75SensorIndex_Object = MibTableColumn
lm75SensorIndex = _Lm75SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 1),
    _Lm75SensorIndex_Type()
)
lm75SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorIndex.setStatus("current")
_Lm75SensorSysctlIndex_Type = Integer32
_Lm75SensorSysctlIndex_Object = MibTableColumn
lm75SensorSysctlIndex = _Lm75SensorSysctlIndex_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 2),
    _Lm75SensorSysctlIndex_Type()
)
lm75SensorSysctlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorSysctlIndex.setStatus("current")
_Lm75SensorDesc_Type = OctetString
_Lm75SensorDesc_Object = MibTableColumn
lm75SensorDesc = _Lm75SensorDesc_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 3),
    _Lm75SensorDesc_Type()
)
lm75SensorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorDesc.setStatus("current")
_Lm75SensorLocation_Type = OctetString
_Lm75SensorLocation_Object = MibTableColumn
lm75SensorLocation = _Lm75SensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 4),
    _Lm75SensorLocation_Type()
)
lm75SensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorLocation.setStatus("current")
_Lm75SensorPnpInfo_Type = OctetString
_Lm75SensorPnpInfo_Object = MibTableColumn
lm75SensorPnpInfo = _Lm75SensorPnpInfo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 5),
    _Lm75SensorPnpInfo_Type()
)
lm75SensorPnpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorPnpInfo.setStatus("current")
_Lm75SensorParent_Type = OctetString
_Lm75SensorParent_Object = MibTableColumn
lm75SensorParent = _Lm75SensorParent_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 6),
    _Lm75SensorParent_Type()
)
lm75SensorParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorParent.setStatus("current")
_Lm75SensorTemperature_Type = Integer32
_Lm75SensorTemperature_Object = MibTableColumn
lm75SensorTemperature = _Lm75SensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 400, 1, 2, 1, 7),
    _Lm75SensorTemperature_Type()
)
lm75SensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm75SensorTemperature.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-LM75-MIB",
    **{"begemotLm75": begemotLm75,
       "begemotLm75Objects": begemotLm75Objects,
       "lm75Sensor": lm75Sensor,
       "lm75Sensors": lm75Sensors,
       "lm75SensorTable": lm75SensorTable,
       "lm75SensorEntry": lm75SensorEntry,
       "lm75SensorIndex": lm75SensorIndex,
       "lm75SensorSysctlIndex": lm75SensorSysctlIndex,
       "lm75SensorDesc": lm75SensorDesc,
       "lm75SensorLocation": lm75SensorLocation,
       "lm75SensorPnpInfo": lm75SensorPnpInfo,
       "lm75SensorParent": lm75SensorParent,
       "lm75SensorTemperature": lm75SensorTemperature}
)
