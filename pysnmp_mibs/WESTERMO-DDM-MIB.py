# SNMP MIB module (WESTERMO-DDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-DDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:22 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(common,) = mibBuilder.importSymbols(
    "WESTERMO-OID-MIB",
    "common")


# MODULE-IDENTITY

ddmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2)
)
if mibBuilder.loadTexts:
    ddmMIB.setRevisions(
        ("2017-12-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DdmObjects_ObjectIdentity = ObjectIdentity
ddmObjects = _DdmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1)
)
_DdmPortTable_Object = MibTable
ddmPortTable = _DdmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ddmPortTable.setStatus("current")
_DdmPortEntry_Object = MibTableRow
ddmPortEntry = _DdmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1)
)
ddmPortEntry.setIndexNames(
    (0, "WESTERMO-DDM-MIB", "ddmPortIfIndex"),
)
if mibBuilder.loadTexts:
    ddmPortEntry.setStatus("current")
_DdmPortIfIndex_Type = InterfaceIndex
_DdmPortIfIndex_Object = MibTableColumn
ddmPortIfIndex = _DdmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 1),
    _DdmPortIfIndex_Type()
)
ddmPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddmPortIfIndex.setStatus("current")
_DdmPortIfName_Type = DisplayString
_DdmPortIfName_Object = MibTableColumn
ddmPortIfName = _DdmPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 2),
    _DdmPortIfName_Type()
)
ddmPortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortIfName.setStatus("current")


class _DdmPortVoltage_Type(Integer32):
    """Custom type ddmPortVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6550),
    )


_DdmPortVoltage_Type.__name__ = "Integer32"
_DdmPortVoltage_Object = MibTableColumn
ddmPortVoltage = _DdmPortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 3),
    _DdmPortVoltage_Type()
)
ddmPortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortVoltage.setStatus("current")


class _DdmPortTemperature_Type(Integer32):
    """Custom type ddmPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_DdmPortTemperature_Type.__name__ = "Integer32"
_DdmPortTemperature_Object = MibTableColumn
ddmPortTemperature = _DdmPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 4),
    _DdmPortTemperature_Type()
)
ddmPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTemperature.setStatus("current")


class _DdmPortBiasCurrent_Type(Integer32):
    """Custom type ddmPortBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131),
    )


_DdmPortBiasCurrent_Type.__name__ = "Integer32"
_DdmPortBiasCurrent_Object = MibTableColumn
ddmPortBiasCurrent = _DdmPortBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 5),
    _DdmPortBiasCurrent_Type()
)
ddmPortBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortBiasCurrent.setStatus("current")


class _DdmPortTxPower_Type(Integer32):
    """Custom type ddmPortTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 820),
    )


_DdmPortTxPower_Type.__name__ = "Integer32"
_DdmPortTxPower_Object = MibTableColumn
ddmPortTxPower = _DdmPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 6),
    _DdmPortTxPower_Type()
)
ddmPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortTxPower.setStatus("current")


class _DdmPortRxPower_Type(Integer32):
    """Custom type ddmPortRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 820),
    )


_DdmPortRxPower_Type.__name__ = "Integer32"
_DdmPortRxPower_Object = MibTableColumn
ddmPortRxPower = _DdmPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 7),
    _DdmPortRxPower_Type()
)
ddmPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmPortRxPower.setStatus("current")
_DdmConformance_ObjectIdentity = ObjectIdentity
ddmConformance = _DdmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 2)
)
_DdmGroups_ObjectIdentity = ObjectIdentity
ddmGroups = _DdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 1)
)
_DdmCompliances_ObjectIdentity = ObjectIdentity
ddmCompliances = _DdmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 2)
)

# Managed Objects groups

ddmPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 1, 1)
)
ddmPortGroup.setObjects(
      *(("WESTERMO-DDM-MIB", "ddmPortIfName"),
        ("WESTERMO-DDM-MIB", "ddmPortVoltage"),
        ("WESTERMO-DDM-MIB", "ddmPortTemperature"),
        ("WESTERMO-DDM-MIB", "ddmPortBiasCurrent"),
        ("WESTERMO-DDM-MIB", "ddmPortTxPower"),
        ("WESTERMO-DDM-MIB", "ddmPortRxPower"))
)
if mibBuilder.loadTexts:
    ddmPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ddmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 2, 1)
)
ddmCompliance.setObjects(
    ("WESTERMO-DDM-MIB", "ddmPortGroup")
)
if mibBuilder.loadTexts:
    ddmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-DDM-MIB",
    **{"ddmMIB": ddmMIB,
       "ddmObjects": ddmObjects,
       "ddmPortTable": ddmPortTable,
       "ddmPortEntry": ddmPortEntry,
       "ddmPortIfIndex": ddmPortIfIndex,
       "ddmPortIfName": ddmPortIfName,
       "ddmPortVoltage": ddmPortVoltage,
       "ddmPortTemperature": ddmPortTemperature,
       "ddmPortBiasCurrent": ddmPortBiasCurrent,
       "ddmPortTxPower": ddmPortTxPower,
       "ddmPortRxPower": ddmPortRxPower,
       "ddmConformance": ddmConformance,
       "ddmGroups": ddmGroups,
       "ddmPortGroup": ddmPortGroup,
       "ddmCompliances": ddmCompliances,
       "ddmCompliance": ddmCompliance}
)
