# SNMP MIB module (ELTEX-MES-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-GVRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:05 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

eltMesGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256)
)
if mibBuilder.loadTexts:
    eltMesGvrpMIB.setRevisions(
        ("2018-01-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesGvrpObjects_ObjectIdentity = ObjectIdentity
eltMesGvrpObjects = _EltMesGvrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1)
)
_EltMesGvrpConfigs_ObjectIdentity = ObjectIdentity
eltMesGvrpConfigs = _EltMesGvrpConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1)
)
_EltGvrpAdvertisementForbidVlanTable_Object = MibTable
eltGvrpAdvertisementForbidVlanTable = _EltGvrpAdvertisementForbidVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanTable.setStatus("current")
_EltGvrpAdvertisementForbidVlanEntry_Object = MibTableRow
eltGvrpAdvertisementForbidVlanEntry = _EltGvrpAdvertisementForbidVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1, 1)
)
eltGvrpAdvertisementForbidVlanEntry.setIndexNames(
    (0, "ELTEX-MES-GVRP-MIB", "eltGvrpAdvertisementForbidVlanIndex"),
)
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanEntry.setStatus("current")


class _EltGvrpAdvertisementForbidVlanIndex_Type(Integer32):
    """Custom type eltGvrpAdvertisementForbidVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_EltGvrpAdvertisementForbidVlanIndex_Type.__name__ = "Integer32"
_EltGvrpAdvertisementForbidVlanIndex_Object = MibTableColumn
eltGvrpAdvertisementForbidVlanIndex = _EltGvrpAdvertisementForbidVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1, 1, 1),
    _EltGvrpAdvertisementForbidVlanIndex_Type()
)
eltGvrpAdvertisementForbidVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanIndex.setStatus("current")


class _EltGvrpAdvertisementForbidVlanId1To1024_Type(OctetString):
    """Custom type eltGvrpAdvertisementForbidVlanId1To1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltGvrpAdvertisementForbidVlanId1To1024_Type.__name__ = "OctetString"
_EltGvrpAdvertisementForbidVlanId1To1024_Object = MibTableColumn
eltGvrpAdvertisementForbidVlanId1To1024 = _EltGvrpAdvertisementForbidVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1, 1, 2),
    _EltGvrpAdvertisementForbidVlanId1To1024_Type()
)
eltGvrpAdvertisementForbidVlanId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanId1To1024.setStatus("current")


class _EltGvrpAdvertisementForbidVlanId1025To2048_Type(OctetString):
    """Custom type eltGvrpAdvertisementForbidVlanId1025To2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltGvrpAdvertisementForbidVlanId1025To2048_Type.__name__ = "OctetString"
_EltGvrpAdvertisementForbidVlanId1025To2048_Object = MibTableColumn
eltGvrpAdvertisementForbidVlanId1025To2048 = _EltGvrpAdvertisementForbidVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1, 1, 3),
    _EltGvrpAdvertisementForbidVlanId1025To2048_Type()
)
eltGvrpAdvertisementForbidVlanId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanId1025To2048.setStatus("current")


class _EltGvrpAdvertisementForbidVlanId2049To3072_Type(OctetString):
    """Custom type eltGvrpAdvertisementForbidVlanId2049To3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltGvrpAdvertisementForbidVlanId2049To3072_Type.__name__ = "OctetString"
_EltGvrpAdvertisementForbidVlanId2049To3072_Object = MibTableColumn
eltGvrpAdvertisementForbidVlanId2049To3072 = _EltGvrpAdvertisementForbidVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1, 1, 4),
    _EltGvrpAdvertisementForbidVlanId2049To3072_Type()
)
eltGvrpAdvertisementForbidVlanId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanId2049To3072.setStatus("current")


class _EltGvrpAdvertisementForbidVlanId3073To4094_Type(OctetString):
    """Custom type eltGvrpAdvertisementForbidVlanId3073To4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltGvrpAdvertisementForbidVlanId3073To4094_Type.__name__ = "OctetString"
_EltGvrpAdvertisementForbidVlanId3073To4094_Object = MibTableColumn
eltGvrpAdvertisementForbidVlanId3073To4094 = _EltGvrpAdvertisementForbidVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 1, 1, 5),
    _EltGvrpAdvertisementForbidVlanId3073To4094_Type()
)
eltGvrpAdvertisementForbidVlanId3073To4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltGvrpAdvertisementForbidVlanId3073To4094.setStatus("current")


class _EltGvrpStaticVlanEnable_Type(TruthValue):
    """Custom type eltGvrpStaticVlanEnable based on TruthValue"""
    defaultValue = 2


_EltGvrpStaticVlanEnable_Type.__name__ = "TruthValue"
_EltGvrpStaticVlanEnable_Object = MibScalar
eltGvrpStaticVlanEnable = _EltGvrpStaticVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 256, 1, 1, 2),
    _EltGvrpStaticVlanEnable_Type()
)
eltGvrpStaticVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltGvrpStaticVlanEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-GVRP-MIB",
    **{"eltMesGvrpMIB": eltMesGvrpMIB,
       "eltMesGvrpObjects": eltMesGvrpObjects,
       "eltMesGvrpConfigs": eltMesGvrpConfigs,
       "eltGvrpAdvertisementForbidVlanTable": eltGvrpAdvertisementForbidVlanTable,
       "eltGvrpAdvertisementForbidVlanEntry": eltGvrpAdvertisementForbidVlanEntry,
       "eltGvrpAdvertisementForbidVlanIndex": eltGvrpAdvertisementForbidVlanIndex,
       "eltGvrpAdvertisementForbidVlanId1To1024": eltGvrpAdvertisementForbidVlanId1To1024,
       "eltGvrpAdvertisementForbidVlanId1025To2048": eltGvrpAdvertisementForbidVlanId1025To2048,
       "eltGvrpAdvertisementForbidVlanId2049To3072": eltGvrpAdvertisementForbidVlanId2049To3072,
       "eltGvrpAdvertisementForbidVlanId3073To4094": eltGvrpAdvertisementForbidVlanId3073To4094,
       "eltGvrpStaticVlanEnable": eltGvrpStaticVlanEnable}
)
