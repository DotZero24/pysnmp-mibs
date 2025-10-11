# SNMP MIB module (NORTEL-ENTITY-VENDORTYPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-ENTITY-VENDORTYPE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:15 2025
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

(nortelGenericMIBs,) = mibBuilder.importSymbols(
    "NORTEL-GENERIC-MIB",
    "nortelGenericMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nnEntityVendorType = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5)
)
if mibBuilder.loadTexts:
    nnEntityVendorType.setRevisions(
        ("2008-12-02 00:00",
         "2000-06-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnEntityVendorTypeOther_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeOther = _NnEntityVendorTypeOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 1)
)
_NnEntityVendorTypeUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeUnknown = _NnEntityVendorTypeUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 2)
)
_NnEntityVendorTypeChassis_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeChassis = _NnEntityVendorTypeChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 3)
)
_NnEntityVendorTypeChassisUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeChassisUnknown = _NnEntityVendorTypeChassisUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 3, 1)
)
_NnEntityVendorTypeBackplane_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeBackplane = _NnEntityVendorTypeBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 4)
)
_NnEntityVendorTypeBackplaneUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeBackplaneUnknown = _NnEntityVendorTypeBackplaneUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 4, 1)
)
_NnEntityVendorTypeContainer_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeContainer = _NnEntityVendorTypeContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 5)
)
_NnEntityVendorTypeContainerUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeContainerUnknown = _NnEntityVendorTypeContainerUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 5, 1)
)
_NnEntityVendorTypePowerSupply_ObjectIdentity = ObjectIdentity
nnEntityVendorTypePowerSupply = _NnEntityVendorTypePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 6)
)
_NnEntityVendorTypePowerSupplyUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypePowerSupplyUnknown = _NnEntityVendorTypePowerSupplyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 6, 1)
)
_NnEntityVendorTypeFan_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeFan = _NnEntityVendorTypeFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 7)
)
_NnEntityVendorTypeFanUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeFanUnknown = _NnEntityVendorTypeFanUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 7, 1)
)
_NnEntityVendorTypeSensor_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeSensor = _NnEntityVendorTypeSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 8)
)
_NnEntityVendorTypeSensorUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeSensorUnknown = _NnEntityVendorTypeSensorUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 8, 1)
)
_NnEntityVendorTypeModule_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeModule = _NnEntityVendorTypeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 9)
)
_NnEntityVendorTypeModuleUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeModuleUnknown = _NnEntityVendorTypeModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 9, 1)
)
_NnEntityVendorTypePort_ObjectIdentity = ObjectIdentity
nnEntityVendorTypePort = _NnEntityVendorTypePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 10)
)
_NnEntityVendorTypePortUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypePortUnknown = _NnEntityVendorTypePortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 10, 1)
)
_NnEntityVendorTypeStack_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeStack = _NnEntityVendorTypeStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 11)
)
_NnEntityVendorTypeStackUnknown_ObjectIdentity = ObjectIdentity
nnEntityVendorTypeStackUnknown = _NnEntityVendorTypeStackUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 11, 1)
)
_NnEntityVendorTypePecCodes_ObjectIdentity = ObjectIdentity
nnEntityVendorTypePecCodes = _NnEntityVendorTypePecCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 5, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-ENTITY-VENDORTYPE-MIB",
    **{"nnEntityVendorType": nnEntityVendorType,
       "nnEntityVendorTypeOther": nnEntityVendorTypeOther,
       "nnEntityVendorTypeUnknown": nnEntityVendorTypeUnknown,
       "nnEntityVendorTypeChassis": nnEntityVendorTypeChassis,
       "nnEntityVendorTypeChassisUnknown": nnEntityVendorTypeChassisUnknown,
       "nnEntityVendorTypeBackplane": nnEntityVendorTypeBackplane,
       "nnEntityVendorTypeBackplaneUnknown": nnEntityVendorTypeBackplaneUnknown,
       "nnEntityVendorTypeContainer": nnEntityVendorTypeContainer,
       "nnEntityVendorTypeContainerUnknown": nnEntityVendorTypeContainerUnknown,
       "nnEntityVendorTypePowerSupply": nnEntityVendorTypePowerSupply,
       "nnEntityVendorTypePowerSupplyUnknown": nnEntityVendorTypePowerSupplyUnknown,
       "nnEntityVendorTypeFan": nnEntityVendorTypeFan,
       "nnEntityVendorTypeFanUnknown": nnEntityVendorTypeFanUnknown,
       "nnEntityVendorTypeSensor": nnEntityVendorTypeSensor,
       "nnEntityVendorTypeSensorUnknown": nnEntityVendorTypeSensorUnknown,
       "nnEntityVendorTypeModule": nnEntityVendorTypeModule,
       "nnEntityVendorTypeModuleUnknown": nnEntityVendorTypeModuleUnknown,
       "nnEntityVendorTypePort": nnEntityVendorTypePort,
       "nnEntityVendorTypePortUnknown": nnEntityVendorTypePortUnknown,
       "nnEntityVendorTypeStack": nnEntityVendorTypeStack,
       "nnEntityVendorTypeStackUnknown": nnEntityVendorTypeStackUnknown,
       "nnEntityVendorTypePecCodes": nnEntityVendorTypePecCodes}
)
