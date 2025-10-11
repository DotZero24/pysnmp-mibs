# SNMP MIB module (MX-EMERGENCY-CALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-EMERGENCY-CALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:43 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

emergencyCallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75)
)
if mibBuilder.loadTexts:
    emergencyCallMIB.setRevisions(
        ("1903-03-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmergencyCallMIBObjects_ObjectIdentity = ObjectIdentity
emergencyCallMIBObjects = _EmergencyCallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 1)
)
_EmergencyCallUrgentGatewayCustomization_ObjectIdentity = ObjectIdentity
emergencyCallUrgentGatewayCustomization = _EmergencyCallUrgentGatewayCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5)
)


class _EmergencyCallUrgentGatewayEnable_Type(MxEnableState):
    """Custom type emergencyCallUrgentGatewayEnable based on MxEnableState"""
    defaultValue = 0


_EmergencyCallUrgentGatewayEnable_Type.__name__ = "MxEnableState"
_EmergencyCallUrgentGatewayEnable_Object = MibScalar
emergencyCallUrgentGatewayEnable = _EmergencyCallUrgentGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5, 5),
    _EmergencyCallUrgentGatewayEnable_Type()
)
emergencyCallUrgentGatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emergencyCallUrgentGatewayEnable.setStatus("current")


class _EmergencyCallUrgentGatewayDigitMap_Type(OctetString):
    """Custom type emergencyCallUrgentGatewayDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EmergencyCallUrgentGatewayDigitMap_Type.__name__ = "OctetString"
_EmergencyCallUrgentGatewayDigitMap_Object = MibScalar
emergencyCallUrgentGatewayDigitMap = _EmergencyCallUrgentGatewayDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5, 10),
    _EmergencyCallUrgentGatewayDigitMap_Type()
)
emergencyCallUrgentGatewayDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emergencyCallUrgentGatewayDigitMap.setStatus("current")


class _EmergencyCallUrgentGatewayTargetAddress_Type(OctetString):
    """Custom type emergencyCallUrgentGatewayTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EmergencyCallUrgentGatewayTargetAddress_Type.__name__ = "OctetString"
_EmergencyCallUrgentGatewayTargetAddress_Object = MibScalar
emergencyCallUrgentGatewayTargetAddress = _EmergencyCallUrgentGatewayTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5, 15),
    _EmergencyCallUrgentGatewayTargetAddress_Type()
)
emergencyCallUrgentGatewayTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emergencyCallUrgentGatewayTargetAddress.setStatus("current")
_EmergencyCallConformance_ObjectIdentity = ObjectIdentity
emergencyCallConformance = _EmergencyCallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 2)
)
_EmergencyCallCompliances_ObjectIdentity = ObjectIdentity
emergencyCallCompliances = _EmergencyCallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 1)
)
_EmergencyCallGroups_ObjectIdentity = ObjectIdentity
emergencyCallGroups = _EmergencyCallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 5)
)

# Managed Objects groups

emergencyCallUrgentGatewayVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 5, 5)
)
emergencyCallUrgentGatewayVer1.setObjects(
      *(("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayEnable"),
        ("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayDigitMap"),
        ("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayTargetAddress"))
)
if mibBuilder.loadTexts:
    emergencyCallUrgentGatewayVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

emergencyCallComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 1, 1)
)
emergencyCallComplVer1.setObjects(
    ("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayVer1")
)
if mibBuilder.loadTexts:
    emergencyCallComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-EMERGENCY-CALL-MIB",
    **{"emergencyCallMIB": emergencyCallMIB,
       "emergencyCallMIBObjects": emergencyCallMIBObjects,
       "emergencyCallUrgentGatewayCustomization": emergencyCallUrgentGatewayCustomization,
       "emergencyCallUrgentGatewayEnable": emergencyCallUrgentGatewayEnable,
       "emergencyCallUrgentGatewayDigitMap": emergencyCallUrgentGatewayDigitMap,
       "emergencyCallUrgentGatewayTargetAddress": emergencyCallUrgentGatewayTargetAddress,
       "emergencyCallConformance": emergencyCallConformance,
       "emergencyCallCompliances": emergencyCallCompliances,
       "emergencyCallComplVer1": emergencyCallComplVer1,
       "emergencyCallGroups": emergencyCallGroups,
       "emergencyCallUrgentGatewayVer1": emergencyCallUrgentGatewayVer1}
)
