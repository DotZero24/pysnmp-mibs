# SNMP MIB module (TPLINK-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-ARP-INSPECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:11 2025
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

tplinkArpInspectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28)
)
if mibBuilder.loadTexts:
    tplinkArpInspectionMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkArpInspectionMIBObjects_ObjectIdentity = ObjectIdentity
tplinkArpInspectionMIBObjects = _TplinkArpInspectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1)
)
_ArpInspectionGlobalConfig_ObjectIdentity = ObjectIdentity
arpInspectionGlobalConfig = _ArpInspectionGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1)
)


class _ArpInspectionGlobalEnable_Type(Integer32):
    """Custom type arpInspectionGlobalEnable based on Integer32"""
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


_ArpInspectionGlobalEnable_Type.__name__ = "Integer32"
_ArpInspectionGlobalEnable_Object = MibScalar
arpInspectionGlobalEnable = _ArpInspectionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 1),
    _ArpInspectionGlobalEnable_Type()
)
arpInspectionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionGlobalEnable.setStatus("current")


class _ArpInspectionVerifySmac_Type(Integer32):
    """Custom type arpInspectionVerifySmac based on Integer32"""
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


_ArpInspectionVerifySmac_Type.__name__ = "Integer32"
_ArpInspectionVerifySmac_Object = MibScalar
arpInspectionVerifySmac = _ArpInspectionVerifySmac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 2),
    _ArpInspectionVerifySmac_Type()
)
arpInspectionVerifySmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionVerifySmac.setStatus("current")


class _ArpInspectionVerifyDmac_Type(Integer32):
    """Custom type arpInspectionVerifyDmac based on Integer32"""
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


_ArpInspectionVerifyDmac_Type.__name__ = "Integer32"
_ArpInspectionVerifyDmac_Object = MibScalar
arpInspectionVerifyDmac = _ArpInspectionVerifyDmac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 3),
    _ArpInspectionVerifyDmac_Type()
)
arpInspectionVerifyDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionVerifyDmac.setStatus("current")


class _ArpInspectionVerifyIp_Type(Integer32):
    """Custom type arpInspectionVerifyIp based on Integer32"""
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


_ArpInspectionVerifyIp_Type.__name__ = "Integer32"
_ArpInspectionVerifyIp_Object = MibScalar
arpInspectionVerifyIp = _ArpInspectionVerifyIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 1, 4),
    _ArpInspectionVerifyIp_Type()
)
arpInspectionVerifyIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionVerifyIp.setStatus("current")
_ArpInspectionVlanConfig_ObjectIdentity = ObjectIdentity
arpInspectionVlanConfig = _ArpInspectionVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2)
)
_ArpInspectionVlanConfigTable_Object = MibTable
arpInspectionVlanConfigTable = _ArpInspectionVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arpInspectionVlanConfigTable.setStatus("current")
_ArpInspectionVlanConfigEntry_Object = MibTableRow
arpInspectionVlanConfigEntry = _ArpInspectionVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1)
)
arpInspectionVlanConfigEntry.setIndexNames(
    (0, "TPLINK-ARP-INSPECTION-MIB", "arpInspectionVlanId"),
)
if mibBuilder.loadTexts:
    arpInspectionVlanConfigEntry.setStatus("current")


class _ArpInspectionVlanId_Type(Integer32):
    """Custom type arpInspectionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectionVlanId_Type.__name__ = "Integer32"
_ArpInspectionVlanId_Object = MibTableColumn
arpInspectionVlanId = _ArpInspectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1),
    _ArpInspectionVlanId_Type()
)
arpInspectionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionVlanId.setStatus("current")


class _ArpInspectionVlanStatus_Type(Integer32):
    """Custom type arpInspectionVlanStatus based on Integer32"""
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


_ArpInspectionVlanStatus_Type.__name__ = "Integer32"
_ArpInspectionVlanStatus_Object = MibTableColumn
arpInspectionVlanStatus = _ArpInspectionVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 2),
    _ArpInspectionVlanStatus_Type()
)
arpInspectionVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionVlanStatus.setStatus("current")


class _ArpInspectionVlanLogStatus_Type(Integer32):
    """Custom type arpInspectionVlanLogStatus based on Integer32"""
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


_ArpInspectionVlanLogStatus_Type.__name__ = "Integer32"
_ArpInspectionVlanLogStatus_Object = MibTableColumn
arpInspectionVlanLogStatus = _ArpInspectionVlanLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 3),
    _ArpInspectionVlanLogStatus_Type()
)
arpInspectionVlanLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionVlanLogStatus.setStatus("current")
_ArpInspectionPortConfig_ObjectIdentity = ObjectIdentity
arpInspectionPortConfig = _ArpInspectionPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3)
)
_ArpInspectionPortConfigTable_Object = MibTable
arpInspectionPortConfigTable = _ArpInspectionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    arpInspectionPortConfigTable.setStatus("current")
_ArpInspectionPortConfigEntry_Object = MibTableRow
arpInspectionPortConfigEntry = _ArpInspectionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1)
)
arpInspectionPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arpInspectionPortConfigEntry.setStatus("current")
_ArpInspectionPortConfigPort_Type = OctetString
_ArpInspectionPortConfigPort_Object = MibTableColumn
arpInspectionPortConfigPort = _ArpInspectionPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 1),
    _ArpInspectionPortConfigPort_Type()
)
arpInspectionPortConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionPortConfigPort.setStatus("current")


class _ArpInspectionPortConfigTrust_Type(Integer32):
    """Custom type arpInspectionPortConfigTrust based on Integer32"""
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


_ArpInspectionPortConfigTrust_Type.__name__ = "Integer32"
_ArpInspectionPortConfigTrust_Object = MibTableColumn
arpInspectionPortConfigTrust = _ArpInspectionPortConfigTrust_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 2),
    _ArpInspectionPortConfigTrust_Type()
)
arpInspectionPortConfigTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigTrust.setStatus("current")
_ArpInspectionPortConfigLimitRate_Type = Integer32
_ArpInspectionPortConfigLimitRate_Object = MibTableColumn
arpInspectionPortConfigLimitRate = _ArpInspectionPortConfigLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 3),
    _ArpInspectionPortConfigLimitRate_Type()
)
arpInspectionPortConfigLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigLimitRate.setStatus("current")
_ArpInspectionPortConfigCurrentSpeed_Type = Integer32
_ArpInspectionPortConfigCurrentSpeed_Object = MibTableColumn
arpInspectionPortConfigCurrentSpeed = _ArpInspectionPortConfigCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 4),
    _ArpInspectionPortConfigCurrentSpeed_Type()
)
arpInspectionPortConfigCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionPortConfigCurrentSpeed.setStatus("current")
_ArpInspectionPortConfigBurstInterval_Type = Integer32
_ArpInspectionPortConfigBurstInterval_Object = MibTableColumn
arpInspectionPortConfigBurstInterval = _ArpInspectionPortConfigBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 5),
    _ArpInspectionPortConfigBurstInterval_Type()
)
arpInspectionPortConfigBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigBurstInterval.setStatus("current")


class _ArpInspectionPortConfigStatus_Type(Integer32):
    """Custom type arpInspectionPortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("down", 1))
    )


_ArpInspectionPortConfigStatus_Type.__name__ = "Integer32"
_ArpInspectionPortConfigStatus_Object = MibTableColumn
arpInspectionPortConfigStatus = _ArpInspectionPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 6),
    _ArpInspectionPortConfigStatus_Type()
)
arpInspectionPortConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionPortConfigStatus.setStatus("current")


class _ArpInspectionPortConfigRecover_Type(Integer32):
    """Custom type arpInspectionPortConfigRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("recover", 1))
    )


_ArpInspectionPortConfigRecover_Type.__name__ = "Integer32"
_ArpInspectionPortConfigRecover_Object = MibTableColumn
arpInspectionPortConfigRecover = _ArpInspectionPortConfigRecover_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 7),
    _ArpInspectionPortConfigRecover_Type()
)
arpInspectionPortConfigRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigRecover.setStatus("current")
_ArpInspectionPortConfigPortLag_Type = OctetString
_ArpInspectionPortConfigPortLag_Object = MibTableColumn
arpInspectionPortConfigPortLag = _ArpInspectionPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 3, 1, 1, 8),
    _ArpInspectionPortConfigPortLag_Type()
)
arpInspectionPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionPortConfigPortLag.setStatus("current")
_ArpInspectionStatisticConfig_ObjectIdentity = ObjectIdentity
arpInspectionStatisticConfig = _ArpInspectionStatisticConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4)
)


class _ArpInspectionStatReset_Type(Integer32):
    """Custom type arpInspectionStatReset based on Integer32"""
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


_ArpInspectionStatReset_Type.__name__ = "Integer32"
_ArpInspectionStatReset_Object = MibScalar
arpInspectionStatReset = _ArpInspectionStatReset_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4, 1),
    _ArpInspectionStatReset_Type()
)
arpInspectionStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionStatReset.setStatus("current")
_ArpInspectionStatTable_Object = MibTable
arpInspectionStatTable = _ArpInspectionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4, 2)
)
if mibBuilder.loadTexts:
    arpInspectionStatTable.setStatus("current")
_ArpInspectionStatEntry_Object = MibTableRow
arpInspectionStatEntry = _ArpInspectionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4, 2, 1)
)
arpInspectionStatEntry.setIndexNames(
    (0, "TPLINK-ARP-INSPECTION-MIB", "arpInspectionStatVlanId"),
)
if mibBuilder.loadTexts:
    arpInspectionStatEntry.setStatus("current")


class _ArpInspectionStatVlanId_Type(Integer32):
    """Custom type arpInspectionStatVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectionStatVlanId_Type.__name__ = "Integer32"
_ArpInspectionStatVlanId_Object = MibTableColumn
arpInspectionStatVlanId = _ArpInspectionStatVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4, 2, 1, 1),
    _ArpInspectionStatVlanId_Type()
)
arpInspectionStatVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionStatVlanId.setStatus("current")
_ArpInspectionStatForward_Type = Counter64
_ArpInspectionStatForward_Object = MibTableColumn
arpInspectionStatForward = _ArpInspectionStatForward_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4, 2, 1, 2),
    _ArpInspectionStatForward_Type()
)
arpInspectionStatForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionStatForward.setStatus("current")
_ArpInspectionStatDrop_Type = Counter64
_ArpInspectionStatDrop_Object = MibTableColumn
arpInspectionStatDrop = _ArpInspectionStatDrop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 4, 2, 1, 3),
    _ArpInspectionStatDrop_Type()
)
arpInspectionStatDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectionStatDrop.setStatus("current")
_TplinkArpInspectionNotifications_ObjectIdentity = ObjectIdentity
tplinkArpInspectionNotifications = _TplinkArpInspectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 2)
)

# Managed Objects groups


# Notification objects

arpInspectionRxIllegalArpPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 2, 1)
)
if mibBuilder.loadTexts:
    arpInspectionRxIllegalArpPacket.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ARP-INSPECTION-MIB",
    **{"tplinkArpInspectionMIB": tplinkArpInspectionMIB,
       "tplinkArpInspectionMIBObjects": tplinkArpInspectionMIBObjects,
       "arpInspectionGlobalConfig": arpInspectionGlobalConfig,
       "arpInspectionGlobalEnable": arpInspectionGlobalEnable,
       "arpInspectionVerifySmac": arpInspectionVerifySmac,
       "arpInspectionVerifyDmac": arpInspectionVerifyDmac,
       "arpInspectionVerifyIp": arpInspectionVerifyIp,
       "arpInspectionVlanConfig": arpInspectionVlanConfig,
       "arpInspectionVlanConfigTable": arpInspectionVlanConfigTable,
       "arpInspectionVlanConfigEntry": arpInspectionVlanConfigEntry,
       "arpInspectionVlanId": arpInspectionVlanId,
       "arpInspectionVlanStatus": arpInspectionVlanStatus,
       "arpInspectionVlanLogStatus": arpInspectionVlanLogStatus,
       "arpInspectionPortConfig": arpInspectionPortConfig,
       "arpInspectionPortConfigTable": arpInspectionPortConfigTable,
       "arpInspectionPortConfigEntry": arpInspectionPortConfigEntry,
       "arpInspectionPortConfigPort": arpInspectionPortConfigPort,
       "arpInspectionPortConfigTrust": arpInspectionPortConfigTrust,
       "arpInspectionPortConfigLimitRate": arpInspectionPortConfigLimitRate,
       "arpInspectionPortConfigCurrentSpeed": arpInspectionPortConfigCurrentSpeed,
       "arpInspectionPortConfigBurstInterval": arpInspectionPortConfigBurstInterval,
       "arpInspectionPortConfigStatus": arpInspectionPortConfigStatus,
       "arpInspectionPortConfigRecover": arpInspectionPortConfigRecover,
       "arpInspectionPortConfigPortLag": arpInspectionPortConfigPortLag,
       "arpInspectionStatisticConfig": arpInspectionStatisticConfig,
       "arpInspectionStatReset": arpInspectionStatReset,
       "arpInspectionStatTable": arpInspectionStatTable,
       "arpInspectionStatEntry": arpInspectionStatEntry,
       "arpInspectionStatVlanId": arpInspectionStatVlanId,
       "arpInspectionStatForward": arpInspectionStatForward,
       "arpInspectionStatDrop": arpInspectionStatDrop,
       "tplinkArpInspectionNotifications": tplinkArpInspectionNotifications,
       "arpInspectionRxIllegalArpPacket": arpInspectionRxIllegalArpPacket}
)
