# SNMP MIB module (TPLINK-NDDETECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-NDDETECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:12 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkNdDetectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93)
)
if mibBuilder.loadTexts:
    tplinkNdDetectionMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkNdDetectionMIBObjects_ObjectIdentity = ObjectIdentity
tplinkNdDetectionMIBObjects = _TplinkNdDetectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1)
)
_NdDetectionGlobalConfig_ObjectIdentity = ObjectIdentity
ndDetectionGlobalConfig = _NdDetectionGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1)
)


class _NdDetectionEnable_Type(Integer32):
    """Custom type ndDetectionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NdDetectionEnable_Type.__name__ = "Integer32"
_NdDetectionEnable_Object = MibScalar
ndDetectionEnable = _NdDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 1, 1),
    _NdDetectionEnable_Type()
)
ndDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionEnable.setStatus("current")
_NdDetectionVlanConfig_ObjectIdentity = ObjectIdentity
ndDetectionVlanConfig = _NdDetectionVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 2)
)
_NdDetectionVlanConfigTable_Object = MibTable
ndDetectionVlanConfigTable = _NdDetectionVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ndDetectionVlanConfigTable.setStatus("current")
_NdDetectionVlanConfigEntry_Object = MibTableRow
ndDetectionVlanConfigEntry = _NdDetectionVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 2, 1, 1)
)
ndDetectionVlanConfigEntry.setIndexNames(
    (0, "TPLINK-NDDETECTION-MIB", "ndDetectionVlanId"),
)
if mibBuilder.loadTexts:
    ndDetectionVlanConfigEntry.setStatus("current")


class _NdDetectionVlanId_Type(Integer32):
    """Custom type ndDetectionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NdDetectionVlanId_Type.__name__ = "Integer32"
_NdDetectionVlanId_Object = MibTableColumn
ndDetectionVlanId = _NdDetectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 2, 1, 1, 1),
    _NdDetectionVlanId_Type()
)
ndDetectionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionVlanId.setStatus("current")


class _NdDetectionVlanStatus_Type(Integer32):
    """Custom type ndDetectionVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NdDetectionVlanStatus_Type.__name__ = "Integer32"
_NdDetectionVlanStatus_Object = MibTableColumn
ndDetectionVlanStatus = _NdDetectionVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 2, 1, 1, 2),
    _NdDetectionVlanStatus_Type()
)
ndDetectionVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionVlanStatus.setStatus("current")


class _NdDetectionVlanLogStatus_Type(Integer32):
    """Custom type ndDetectionVlanLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NdDetectionVlanLogStatus_Type.__name__ = "Integer32"
_NdDetectionVlanLogStatus_Object = MibTableColumn
ndDetectionVlanLogStatus = _NdDetectionVlanLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 2, 1, 1, 3),
    _NdDetectionVlanLogStatus_Type()
)
ndDetectionVlanLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionVlanLogStatus.setStatus("current")
_NdDetectionPortConfig_ObjectIdentity = ObjectIdentity
ndDetectionPortConfig = _NdDetectionPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3)
)
_NdDetectionPortConfigTable_Object = MibTable
ndDetectionPortConfigTable = _NdDetectionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ndDetectionPortConfigTable.setStatus("current")
_NdDetectionPortConfigEntry_Object = MibTableRow
ndDetectionPortConfigEntry = _NdDetectionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1)
)
ndDetectionPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ndDetectionPortConfigEntry.setStatus("current")


class _NdDetectionPort_Type(OctetString):
    """Custom type ndDetectionPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NdDetectionPort_Type.__name__ = "OctetString"
_NdDetectionPort_Object = MibTableColumn
ndDetectionPort = _NdDetectionPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1, 1),
    _NdDetectionPort_Type()
)
ndDetectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionPort.setStatus("current")


class _NdDetectionPortConfigTrustedPort_Type(Integer32):
    """Custom type ndDetectionPortConfigTrustedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NdDetectionPortConfigTrustedPort_Type.__name__ = "Integer32"
_NdDetectionPortConfigTrustedPort_Object = MibTableColumn
ndDetectionPortConfigTrustedPort = _NdDetectionPortConfigTrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1, 2),
    _NdDetectionPortConfigTrustedPort_Type()
)
ndDetectionPortConfigTrustedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionPortConfigTrustedPort.setStatus("current")


class _NdDetectionPortConfigPortLag_Type(OctetString):
    """Custom type ndDetectionPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NdDetectionPortConfigPortLag_Type.__name__ = "OctetString"
_NdDetectionPortConfigPortLag_Object = MibTableColumn
ndDetectionPortConfigPortLag = _NdDetectionPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 3, 1, 1, 3),
    _NdDetectionPortConfigPortLag_Type()
)
ndDetectionPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionPortConfigPortLag.setStatus("current")
_NdDetectionStatisticConfig_ObjectIdentity = ObjectIdentity
ndDetectionStatisticConfig = _NdDetectionStatisticConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4)
)


class _NdDetectionStatReset_Type(Integer32):
    """Custom type ndDetectionStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReset", 0),
          ("reset", 1))
    )


_NdDetectionStatReset_Type.__name__ = "Integer32"
_NdDetectionStatReset_Object = MibScalar
ndDetectionStatReset = _NdDetectionStatReset_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4, 1),
    _NdDetectionStatReset_Type()
)
ndDetectionStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndDetectionStatReset.setStatus("current")
_NdDetectionStatTable_Object = MibTable
ndDetectionStatTable = _NdDetectionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ndDetectionStatTable.setStatus("current")
_NdDetectionStatEntry_Object = MibTableRow
ndDetectionStatEntry = _NdDetectionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4, 2, 1)
)
ndDetectionStatEntry.setIndexNames(
    (0, "TPLINK-NDDETECTION-MIB", "ndDetectionStatVlanId"),
)
if mibBuilder.loadTexts:
    ndDetectionStatEntry.setStatus("current")


class _NdDetectionStatVlanId_Type(Integer32):
    """Custom type ndDetectionStatVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NdDetectionStatVlanId_Type.__name__ = "Integer32"
_NdDetectionStatVlanId_Object = MibTableColumn
ndDetectionStatVlanId = _NdDetectionStatVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4, 2, 1, 1),
    _NdDetectionStatVlanId_Type()
)
ndDetectionStatVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionStatVlanId.setStatus("current")
_NdDetectionStatForward_Type = Counter64
_NdDetectionStatForward_Object = MibTableColumn
ndDetectionStatForward = _NdDetectionStatForward_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4, 2, 1, 2),
    _NdDetectionStatForward_Type()
)
ndDetectionStatForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionStatForward.setStatus("current")
_NdDetectionStatDrop_Type = Counter64
_NdDetectionStatDrop_Object = MibTableColumn
ndDetectionStatDrop = _NdDetectionStatDrop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 1, 4, 2, 1, 3),
    _NdDetectionStatDrop_Type()
)
ndDetectionStatDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndDetectionStatDrop.setStatus("current")
_TplinkNdDetectionNotifications_ObjectIdentity = ObjectIdentity
tplinkNdDetectionNotifications = _TplinkNdDetectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 93, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-NDDETECTION-MIB",
    **{"tplinkNdDetectionMIB": tplinkNdDetectionMIB,
       "tplinkNdDetectionMIBObjects": tplinkNdDetectionMIBObjects,
       "ndDetectionGlobalConfig": ndDetectionGlobalConfig,
       "ndDetectionEnable": ndDetectionEnable,
       "ndDetectionVlanConfig": ndDetectionVlanConfig,
       "ndDetectionVlanConfigTable": ndDetectionVlanConfigTable,
       "ndDetectionVlanConfigEntry": ndDetectionVlanConfigEntry,
       "ndDetectionVlanId": ndDetectionVlanId,
       "ndDetectionVlanStatus": ndDetectionVlanStatus,
       "ndDetectionVlanLogStatus": ndDetectionVlanLogStatus,
       "ndDetectionPortConfig": ndDetectionPortConfig,
       "ndDetectionPortConfigTable": ndDetectionPortConfigTable,
       "ndDetectionPortConfigEntry": ndDetectionPortConfigEntry,
       "ndDetectionPort": ndDetectionPort,
       "ndDetectionPortConfigTrustedPort": ndDetectionPortConfigTrustedPort,
       "ndDetectionPortConfigPortLag": ndDetectionPortConfigPortLag,
       "ndDetectionStatisticConfig": ndDetectionStatisticConfig,
       "ndDetectionStatReset": ndDetectionStatReset,
       "ndDetectionStatTable": ndDetectionStatTable,
       "ndDetectionStatEntry": ndDetectionStatEntry,
       "ndDetectionStatVlanId": ndDetectionStatVlanId,
       "ndDetectionStatForward": ndDetectionStatForward,
       "ndDetectionStatDrop": ndDetectionStatDrop,
       "tplinkNdDetectionNotifications": tplinkNdDetectionNotifications}
)
