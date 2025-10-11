# SNMP MIB module (H3C-WLAN-FLEXAPP-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-WLAN-FLEXAPP-CFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:53 2025
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

(h3cDot11,) = mibBuilder.importSymbols(
    "H3C-DOT11-REF-MIB",
    "h3cDot11")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cWlanFlexAppCFG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19)
)
if mibBuilder.loadTexts:
    h3cWlanFlexAppCFG.setRevisions(
        ("2015-05-26 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cWlanModuleConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanModuleConfigGroup = _H3cWlanModuleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1)
)
_H3cWlanModuleConfigTable_Object = MibTable
h3cWlanModuleConfigTable = _H3cWlanModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1)
)
if mibBuilder.loadTexts:
    h3cWlanModuleConfigTable.setStatus("current")
_H3cWlanModuleConfigEntry_Object = MibTableRow
h3cWlanModuleConfigEntry = _H3cWlanModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1)
)
h3cWlanModuleConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanAPSerialID"),
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanModuleID"),
)
if mibBuilder.loadTexts:
    h3cWlanModuleConfigEntry.setStatus("current")


class _H3cWlanAPSerialID_Type(OctetString):
    """Custom type h3cWlanAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanAPSerialID_Type.__name__ = "OctetString"
_H3cWlanAPSerialID_Object = MibTableColumn
h3cWlanAPSerialID = _H3cWlanAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 1),
    _H3cWlanAPSerialID_Type()
)
h3cWlanAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanAPSerialID.setStatus("current")


class _H3cWlanModuleID_Type(Integer32):
    """Custom type h3cWlanModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanModuleID_Type.__name__ = "Integer32"
_H3cWlanModuleID_Object = MibTableColumn
h3cWlanModuleID = _H3cWlanModuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 2),
    _H3cWlanModuleID_Type()
)
h3cWlanModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanModuleID.setStatus("current")


class _H3cWlanModuleType_Type(Integer32):
    """Custom type h3cWlanModuleType based on Integer32"""
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
          ("ble", 1),
          ("iot", 2))
    )


_H3cWlanModuleType_Type.__name__ = "Integer32"
_H3cWlanModuleType_Object = MibTableColumn
h3cWlanModuleType = _H3cWlanModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 3),
    _H3cWlanModuleType_Type()
)
h3cWlanModuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleType.setStatus("current")
_H3cWlanModuleStatus_Type = TruthValue
_H3cWlanModuleStatus_Object = MibTableColumn
h3cWlanModuleStatus = _H3cWlanModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 4),
    _H3cWlanModuleStatus_Type()
)
h3cWlanModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleStatus.setStatus("current")


class _H3cWlanModuleReset_Type(Integer32):
    """Custom type h3cWlanModuleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reboot", 1))
    )


_H3cWlanModuleReset_Type.__name__ = "Integer32"
_H3cWlanModuleReset_Object = MibTableColumn
h3cWlanModuleReset = _H3cWlanModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 5),
    _H3cWlanModuleReset_Type()
)
h3cWlanModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleReset.setStatus("current")


class _H3cWlanModuleRstFac_Type(Integer32):
    """Custom type h3cWlanModuleRstFac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("restore", 1))
    )


_H3cWlanModuleRstFac_Type.__name__ = "Integer32"
_H3cWlanModuleRstFac_Object = MibTableColumn
h3cWlanModuleRstFac = _H3cWlanModuleRstFac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 6),
    _H3cWlanModuleRstFac_Type()
)
h3cWlanModuleRstFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleRstFac.setStatus("current")
_H3cWlanModuleUpWareStatus_Type = TruthValue
_H3cWlanModuleUpWareStatus_Object = MibTableColumn
h3cWlanModuleUpWareStatus = _H3cWlanModuleUpWareStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 7),
    _H3cWlanModuleUpWareStatus_Type()
)
h3cWlanModuleUpWareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleUpWareStatus.setStatus("current")


class _H3cWlanModuleTxPower_Type(Integer32):
    """Custom type h3cWlanModuleTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_H3cWlanModuleTxPower_Type.__name__ = "Integer32"
_H3cWlanModuleTxPower_Object = MibTableColumn
h3cWlanModuleTxPower = _H3cWlanModuleTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 8),
    _H3cWlanModuleTxPower_Type()
)
h3cWlanModuleTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleTxPower.setStatus("current")
_H3cWlanModuleManualUpdate_Type = OctetString
_H3cWlanModuleManualUpdate_Object = MibTableColumn
h3cWlanModuleManualUpdate = _H3cWlanModuleManualUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 1, 1, 9),
    _H3cWlanModuleManualUpdate_Type()
)
h3cWlanModuleManualUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanModuleManualUpdate.setStatus("current")
_H3cWlanModuleInfoTable_Object = MibTable
h3cWlanModuleInfoTable = _H3cWlanModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2)
)
if mibBuilder.loadTexts:
    h3cWlanModuleInfoTable.setStatus("current")
_H3cWlanModuleInfoEntry_Object = MibTableRow
h3cWlanModuleInfoEntry = _H3cWlanModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1)
)
h3cWlanModuleInfoEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cDot11IOTAPSerialID"),
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cDot11IOTModuleID"),
)
if mibBuilder.loadTexts:
    h3cWlanModuleInfoEntry.setStatus("current")


class _H3cDot11IOTAPSerialID_Type(OctetString):
    """Custom type h3cDot11IOTAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11IOTAPSerialID_Type.__name__ = "OctetString"
_H3cDot11IOTAPSerialID_Object = MibTableColumn
h3cDot11IOTAPSerialID = _H3cDot11IOTAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 1),
    _H3cDot11IOTAPSerialID_Type()
)
h3cDot11IOTAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11IOTAPSerialID.setStatus("current")


class _H3cDot11IOTModuleID_Type(Integer32):
    """Custom type h3cDot11IOTModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cDot11IOTModuleID_Type.__name__ = "Integer32"
_H3cDot11IOTModuleID_Object = MibTableColumn
h3cDot11IOTModuleID = _H3cDot11IOTModuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 2),
    _H3cDot11IOTModuleID_Type()
)
h3cDot11IOTModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11IOTModuleID.setStatus("current")


class _H3cDot11IOTModuleType_Type(Integer32):
    """Custom type h3cDot11IOTModuleType based on Integer32"""
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
          ("h3c", 1),
          ("iot", 2))
    )


_H3cDot11IOTModuleType_Type.__name__ = "Integer32"
_H3cDot11IOTModuleType_Object = MibTableColumn
h3cDot11IOTModuleType = _H3cDot11IOTModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 3),
    _H3cDot11IOTModuleType_Type()
)
h3cDot11IOTModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11IOTModuleType.setStatus("current")
_H3cDot11IOTModuleModel_Type = OctetString
_H3cDot11IOTModuleModel_Object = MibTableColumn
h3cDot11IOTModuleModel = _H3cDot11IOTModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 4),
    _H3cDot11IOTModuleModel_Type()
)
h3cDot11IOTModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11IOTModuleModel.setStatus("current")
_H3cDot11IOTModuleHwVersion_Type = OctetString
_H3cDot11IOTModuleHwVersion_Object = MibTableColumn
h3cDot11IOTModuleHwVersion = _H3cDot11IOTModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 5),
    _H3cDot11IOTModuleHwVersion_Type()
)
h3cDot11IOTModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11IOTModuleHwVersion.setStatus("current")
_H3cDot11IOTModuleSwVersion_Type = OctetString
_H3cDot11IOTModuleSwVersion_Object = MibTableColumn
h3cDot11IOTModuleSwVersion = _H3cDot11IOTModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 6),
    _H3cDot11IOTModuleSwVersion_Type()
)
h3cDot11IOTModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11IOTModuleSwVersion.setStatus("current")
_H3cDot11IOTModuleSerialId_Type = OctetString
_H3cDot11IOTModuleSerialId_Object = MibTableColumn
h3cDot11IOTModuleSerialId = _H3cDot11IOTModuleSerialId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 1, 2, 1, 7),
    _H3cDot11IOTModuleSerialId_Type()
)
h3cDot11IOTModuleSerialId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11IOTModuleSerialId.setStatus("current")
_H3cWlanIOTConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanIOTConfigGroup = _H3cWlanIOTConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 2)
)
_H3cWlanIOTConfigTable_Object = MibTable
h3cWlanIOTConfigTable = _H3cWlanIOTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 2, 1)
)
if mibBuilder.loadTexts:
    h3cWlanIOTConfigTable.setStatus("current")
_H3cWlanIOTConfigEntry_Object = MibTableRow
h3cWlanIOTConfigEntry = _H3cWlanIOTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 2, 1, 1)
)
h3cWlanIOTConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanIOTAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cWlanIOTConfigEntry.setStatus("current")


class _H3cWlanIOTAPSerialID_Type(OctetString):
    """Custom type h3cWlanIOTAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanIOTAPSerialID_Type.__name__ = "OctetString"
_H3cWlanIOTAPSerialID_Object = MibTableColumn
h3cWlanIOTAPSerialID = _H3cWlanIOTAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 2, 1, 1, 1),
    _H3cWlanIOTAPSerialID_Type()
)
h3cWlanIOTAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanIOTAPSerialID.setStatus("current")
_H3cWlanIOTEngineAdd_Type = IpAddress
_H3cWlanIOTEngineAdd_Object = MibTableColumn
h3cWlanIOTEngineAdd = _H3cWlanIOTEngineAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 2, 1, 1, 2),
    _H3cWlanIOTEngineAdd_Type()
)
h3cWlanIOTEngineAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanIOTEngineAdd.setStatus("current")


class _H3cWlanIOTEnginePort_Type(Integer32):
    """Custom type h3cWlanIOTEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanIOTEnginePort_Type.__name__ = "Integer32"
_H3cWlanIOTEnginePort_Object = MibTableColumn
h3cWlanIOTEnginePort = _H3cWlanIOTEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 2, 1, 1, 3),
    _H3cWlanIOTEnginePort_Type()
)
h3cWlanIOTEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanIOTEnginePort.setStatus("current")
_H3cWlanModuleNotifyGroup_ObjectIdentity = ObjectIdentity
h3cWlanModuleNotifyGroup = _H3cWlanModuleNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3)
)
_H3cWlanModuleTraps_ObjectIdentity = ObjectIdentity
h3cWlanModuleTraps = _H3cWlanModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 0)
)
_H3cWlanModuleTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cWlanModuleTrapVarObjects = _H3cWlanModuleTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1)
)
_H3cWlanTrapAPMacAddress_Type = MacAddress
_H3cWlanTrapAPMacAddress_Object = MibScalar
h3cWlanTrapAPMacAddress = _H3cWlanTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 1),
    _H3cWlanTrapAPMacAddress_Type()
)
h3cWlanTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapAPMacAddress.setStatus("current")
_H3cWlanTrapModuleID_Type = Integer32
_H3cWlanTrapModuleID_Object = MibScalar
h3cWlanTrapModuleID = _H3cWlanTrapModuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 2),
    _H3cWlanTrapModuleID_Type()
)
h3cWlanTrapModuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModuleID.setStatus("current")


class _H3cWlanTrapModuleCfgType_Type(Integer32):
    """Custom type h3cWlanTrapModuleCfgType based on Integer32"""
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
          ("h3c", 1),
          ("iot", 2))
    )


_H3cWlanTrapModuleCfgType_Type.__name__ = "Integer32"
_H3cWlanTrapModuleCfgType_Object = MibScalar
h3cWlanTrapModuleCfgType = _H3cWlanTrapModuleCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 3),
    _H3cWlanTrapModuleCfgType_Type()
)
h3cWlanTrapModuleCfgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModuleCfgType.setStatus("current")


class _H3cWlanTrapModulePhyType_Type(Integer32):
    """Custom type h3cWlanTrapModulePhyType based on Integer32"""
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
          ("h3c", 1),
          ("iot", 2))
    )


_H3cWlanTrapModulePhyType_Type.__name__ = "Integer32"
_H3cWlanTrapModulePhyType_Object = MibScalar
h3cWlanTrapModulePhyType = _H3cWlanTrapModulePhyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 4),
    _H3cWlanTrapModulePhyType_Type()
)
h3cWlanTrapModulePhyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModulePhyType.setStatus("current")
_H3cWlanTrapModuleModel_Type = OctetString
_H3cWlanTrapModuleModel_Object = MibScalar
h3cWlanTrapModuleModel = _H3cWlanTrapModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 5),
    _H3cWlanTrapModuleModel_Type()
)
h3cWlanTrapModuleModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModuleModel.setStatus("current")
_H3cWlanTrapModuleHwVersion_Type = OctetString
_H3cWlanTrapModuleHwVersion_Object = MibScalar
h3cWlanTrapModuleHwVersion = _H3cWlanTrapModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 6),
    _H3cWlanTrapModuleHwVersion_Type()
)
h3cWlanTrapModuleHwVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModuleHwVersion.setStatus("current")
_H3cWlanTrapModuleSwVersion_Type = OctetString
_H3cWlanTrapModuleSwVersion_Object = MibScalar
h3cWlanTrapModuleSwVersion = _H3cWlanTrapModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 7),
    _H3cWlanTrapModuleSwVersion_Type()
)
h3cWlanTrapModuleSwVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModuleSwVersion.setStatus("current")
_H3cWlanTrapModuleSequenceId_Type = OctetString
_H3cWlanTrapModuleSequenceId_Object = MibScalar
h3cWlanTrapModuleSequenceId = _H3cWlanTrapModuleSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 1, 8),
    _H3cWlanTrapModuleSequenceId_Type()
)
h3cWlanTrapModuleSequenceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWlanTrapModuleSequenceId.setStatus("current")
_H3cWlanBLEConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanBLEConfigGroup = _H3cWlanBLEConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4)
)
_H3cWlanBLEConfigTable_Object = MibTable
h3cWlanBLEConfigTable = _H3cWlanBLEConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1)
)
if mibBuilder.loadTexts:
    h3cWlanBLEConfigTable.setStatus("current")
_H3cWlanBLEConfigEntry_Object = MibTableRow
h3cWlanBLEConfigEntry = _H3cWlanBLEConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1)
)
h3cWlanBLEConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanBLEAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cWlanBLEConfigEntry.setStatus("current")


class _H3cWlanBLEAPSerialID_Type(OctetString):
    """Custom type h3cWlanBLEAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanBLEAPSerialID_Type.__name__ = "OctetString"
_H3cWlanBLEAPSerialID_Object = MibTableColumn
h3cWlanBLEAPSerialID = _H3cWlanBLEAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 1),
    _H3cWlanBLEAPSerialID_Type()
)
h3cWlanBLEAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanBLEAPSerialID.setStatus("current")
_H3cWlanBLEStatus_Type = TruthValue
_H3cWlanBLEStatus_Object = MibTableColumn
h3cWlanBLEStatus = _H3cWlanBLEStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 2),
    _H3cWlanBLEStatus_Type()
)
h3cWlanBLEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEStatus.setStatus("current")
_H3cWlanBLEEngineAdd_Type = IpAddress
_H3cWlanBLEEngineAdd_Object = MibTableColumn
h3cWlanBLEEngineAdd = _H3cWlanBLEEngineAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 3),
    _H3cWlanBLEEngineAdd_Type()
)
h3cWlanBLEEngineAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEEngineAdd.setStatus("current")


class _H3cWlanBLEEnginePort_Type(Integer32):
    """Custom type h3cWlanBLEEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanBLEEnginePort_Type.__name__ = "Integer32"
_H3cWlanBLEEnginePort_Object = MibTableColumn
h3cWlanBLEEnginePort = _H3cWlanBLEEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 4),
    _H3cWlanBLEEnginePort_Type()
)
h3cWlanBLEEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEEnginePort.setStatus("current")


class _H3cWlanBLEVendorPort_Type(Integer32):
    """Custom type h3cWlanBLEVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanBLEVendorPort_Type.__name__ = "Integer32"
_H3cWlanBLEVendorPort_Object = MibTableColumn
h3cWlanBLEVendorPort = _H3cWlanBLEVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 5),
    _H3cWlanBLEVendorPort_Type()
)
h3cWlanBLEVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEVendorPort.setStatus("current")
_H3cWlanBLERssiStatus_Type = TruthValue
_H3cWlanBLERssiStatus_Object = MibTableColumn
h3cWlanBLERssiStatus = _H3cWlanBLERssiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 6),
    _H3cWlanBLERssiStatus_Type()
)
h3cWlanBLERssiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLERssiStatus.setStatus("current")


class _H3cWlanBLERssiThreshold_Type(Integer32):
    """Custom type h3cWlanBLERssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_H3cWlanBLERssiThreshold_Type.__name__ = "Integer32"
_H3cWlanBLERssiThreshold_Object = MibTableColumn
h3cWlanBLERssiThreshold = _H3cWlanBLERssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 7),
    _H3cWlanBLERssiThreshold_Type()
)
h3cWlanBLERssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLERssiThreshold.setStatus("current")


class _H3cWlanBLEConnectPassword_Type(OctetString):
    """Custom type h3cWlanBLEConnectPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_H3cWlanBLEConnectPassword_Type.__name__ = "OctetString"
_H3cWlanBLEConnectPassword_Object = MibTableColumn
h3cWlanBLEConnectPassword = _H3cWlanBLEConnectPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 8),
    _H3cWlanBLEConnectPassword_Type()
)
h3cWlanBLEConnectPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEConnectPassword.setStatus("current")


class _H3cWlanBLECommandPassword_Type(OctetString):
    """Custom type h3cWlanBLECommandPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
    )


_H3cWlanBLECommandPassword_Type.__name__ = "OctetString"
_H3cWlanBLECommandPassword_Object = MibTableColumn
h3cWlanBLECommandPassword = _H3cWlanBLECommandPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 9),
    _H3cWlanBLECommandPassword_Type()
)
h3cWlanBLECommandPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLECommandPassword.setStatus("current")
_H3cWlanBLEReportStatus_Type = TruthValue
_H3cWlanBLEReportStatus_Object = MibTableColumn
h3cWlanBLEReportStatus = _H3cWlanBLEReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 10),
    _H3cWlanBLEReportStatus_Type()
)
h3cWlanBLEReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEReportStatus.setStatus("current")


class _H3cWlanBLEReportInterval_Type(Integer32):
    """Custom type h3cWlanBLEReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_H3cWlanBLEReportInterval_Type.__name__ = "Integer32"
_H3cWlanBLEReportInterval_Object = MibTableColumn
h3cWlanBLEReportInterval = _H3cWlanBLEReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 11),
    _H3cWlanBLEReportInterval_Type()
)
h3cWlanBLEReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanBLEReportInterval.setUnits("Second")


class _H3cWlanBLEAgingTime_Type(Integer32):
    """Custom type h3cWlanBLEAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_H3cWlanBLEAgingTime_Type.__name__ = "Integer32"
_H3cWlanBLEAgingTime_Object = MibTableColumn
h3cWlanBLEAgingTime = _H3cWlanBLEAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 12),
    _H3cWlanBLEAgingTime_Type()
)
h3cWlanBLEAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanBLEAgingTime.setUnits("Second")
_H3cWlanBLERealTimeReportStatus_Type = TruthValue
_H3cWlanBLERealTimeReportStatus_Object = MibTableColumn
h3cWlanBLERealTimeReportStatus = _H3cWlanBLERealTimeReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 13),
    _H3cWlanBLERealTimeReportStatus_Type()
)
h3cWlanBLERealTimeReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLERealTimeReportStatus.setStatus("current")


class _H3cWlanBLERealTimePrefix_Type(OctetString):
    """Custom type h3cWlanBLERealTimePrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 18),
    )


_H3cWlanBLERealTimePrefix_Type.__name__ = "OctetString"
_H3cWlanBLERealTimePrefix_Object = MibTableColumn
h3cWlanBLERealTimePrefix = _H3cWlanBLERealTimePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 1, 1, 14),
    _H3cWlanBLERealTimePrefix_Type()
)
h3cWlanBLERealTimePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLERealTimePrefix.setStatus("current")
_H3cWlanBLEModuleConfigTable_Object = MibTable
h3cWlanBLEModuleConfigTable = _H3cWlanBLEModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2)
)
if mibBuilder.loadTexts:
    h3cWlanBLEModuleConfigTable.setStatus("current")
_H3cWlanBLEModuleConfigEntry_Object = MibTableRow
h3cWlanBLEModuleConfigEntry = _H3cWlanBLEModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1)
)
h3cWlanBLEModuleConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanBLEModuleAPSerialID"),
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanBLEModuleID"),
)
if mibBuilder.loadTexts:
    h3cWlanBLEModuleConfigEntry.setStatus("current")


class _H3cWlanBLEModuleAPSerialID_Type(OctetString):
    """Custom type h3cWlanBLEModuleAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanBLEModuleAPSerialID_Type.__name__ = "OctetString"
_H3cWlanBLEModuleAPSerialID_Object = MibTableColumn
h3cWlanBLEModuleAPSerialID = _H3cWlanBLEModuleAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 1),
    _H3cWlanBLEModuleAPSerialID_Type()
)
h3cWlanBLEModuleAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanBLEModuleAPSerialID.setStatus("current")


class _H3cWlanBLEModuleID_Type(Integer32):
    """Custom type h3cWlanBLEModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanBLEModuleID_Type.__name__ = "Integer32"
_H3cWlanBLEModuleID_Object = MibTableColumn
h3cWlanBLEModuleID = _H3cWlanBLEModuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 2),
    _H3cWlanBLEModuleID_Type()
)
h3cWlanBLEModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanBLEModuleID.setStatus("current")
_H3cWlanBLEAdvReportStatus_Type = TruthValue
_H3cWlanBLEAdvReportStatus_Object = MibTableColumn
h3cWlanBLEAdvReportStatus = _H3cWlanBLEAdvReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 3),
    _H3cWlanBLEAdvReportStatus_Type()
)
h3cWlanBLEAdvReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEAdvReportStatus.setStatus("current")


class _H3cWlanBLEAdvReportInterval_Type(Integer32):
    """Custom type h3cWlanBLEAdvReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_H3cWlanBLEAdvReportInterval_Type.__name__ = "Integer32"
_H3cWlanBLEAdvReportInterval_Object = MibTableColumn
h3cWlanBLEAdvReportInterval = _H3cWlanBLEAdvReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 4),
    _H3cWlanBLEAdvReportInterval_Type()
)
h3cWlanBLEAdvReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEAdvReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanBLEAdvReportInterval.setUnits("Second")


class _H3cWlanBLEAdvUUID_Type(OctetString):
    """Custom type h3cWlanBLEAdvUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_H3cWlanBLEAdvUUID_Type.__name__ = "OctetString"
_H3cWlanBLEAdvUUID_Object = MibTableColumn
h3cWlanBLEAdvUUID = _H3cWlanBLEAdvUUID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 5),
    _H3cWlanBLEAdvUUID_Type()
)
h3cWlanBLEAdvUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEAdvUUID.setStatus("current")


class _H3cWlanBLEAdvMajorID_Type(Integer32):
    """Custom type h3cWlanBLEAdvMajorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanBLEAdvMajorID_Type.__name__ = "Integer32"
_H3cWlanBLEAdvMajorID_Object = MibTableColumn
h3cWlanBLEAdvMajorID = _H3cWlanBLEAdvMajorID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 6),
    _H3cWlanBLEAdvMajorID_Type()
)
h3cWlanBLEAdvMajorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEAdvMajorID.setStatus("current")


class _H3cWlanBLEAdvMinorID_Type(Integer32):
    """Custom type h3cWlanBLEAdvMinorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanBLEAdvMinorID_Type.__name__ = "Integer32"
_H3cWlanBLEAdvMinorID_Object = MibTableColumn
h3cWlanBLEAdvMinorID = _H3cWlanBLEAdvMinorID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 4, 2, 1, 7),
    _H3cWlanBLEAdvMinorID_Type()
)
h3cWlanBLEAdvMinorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanBLEAdvMinorID.setStatus("current")
_H3cWlanAEConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanAEConfigGroup = _H3cWlanAEConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5)
)
_H3cWlanAEConfigTable_Object = MibTable
h3cWlanAEConfigTable = _H3cWlanAEConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1)
)
if mibBuilder.loadTexts:
    h3cWlanAEConfigTable.setStatus("current")
_H3cWlanAEConfigEntry_Object = MibTableRow
h3cWlanAEConfigEntry = _H3cWlanAEConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1)
)
h3cWlanAEConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanAEAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cWlanAEConfigEntry.setStatus("current")


class _H3cWlanAEAPSerialID_Type(OctetString):
    """Custom type h3cWlanAEAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanAEAPSerialID_Type.__name__ = "OctetString"
_H3cWlanAEAPSerialID_Object = MibTableColumn
h3cWlanAEAPSerialID = _H3cWlanAEAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 1),
    _H3cWlanAEAPSerialID_Type()
)
h3cWlanAEAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanAEAPSerialID.setStatus("current")
_H3cWlanAEStatus_Type = TruthValue
_H3cWlanAEStatus_Object = MibTableColumn
h3cWlanAEStatus = _H3cWlanAEStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 2),
    _H3cWlanAEStatus_Type()
)
h3cWlanAEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEStatus.setStatus("current")
_H3cWlanAEEngineAddr_Type = IpAddress
_H3cWlanAEEngineAddr_Object = MibTableColumn
h3cWlanAEEngineAddr = _H3cWlanAEEngineAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 3),
    _H3cWlanAEEngineAddr_Type()
)
h3cWlanAEEngineAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEEngineAddr.setStatus("current")


class _H3cWlanAEEnginePort_Type(Integer32):
    """Custom type h3cWlanAEEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanAEEnginePort_Type.__name__ = "Integer32"
_H3cWlanAEEnginePort_Object = MibTableColumn
h3cWlanAEEnginePort = _H3cWlanAEEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 4),
    _H3cWlanAEEnginePort_Type()
)
h3cWlanAEEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEEnginePort.setStatus("current")


class _H3cWlanAEVendorPort_Type(Integer32):
    """Custom type h3cWlanAEVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanAEVendorPort_Type.__name__ = "Integer32"
_H3cWlanAEVendorPort_Object = MibTableColumn
h3cWlanAEVendorPort = _H3cWlanAEVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 5),
    _H3cWlanAEVendorPort_Type()
)
h3cWlanAEVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEVendorPort.setStatus("current")


class _H3cWlanAETimeStamp_Type(Integer32):
    """Custom type h3cWlanAETimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("relative", 2))
    )


_H3cWlanAETimeStamp_Type.__name__ = "Integer32"
_H3cWlanAETimeStamp_Object = MibTableColumn
h3cWlanAETimeStamp = _H3cWlanAETimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 6),
    _H3cWlanAETimeStamp_Type()
)
h3cWlanAETimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAETimeStamp.setStatus("current")


class _H3cWlanAEVersion_Type(Integer32):
    """Custom type h3cWlanAEVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_H3cWlanAEVersion_Type.__name__ = "Integer32"
_H3cWlanAEVersion_Object = MibTableColumn
h3cWlanAEVersion = _H3cWlanAEVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 7),
    _H3cWlanAEVersion_Type()
)
h3cWlanAEVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEVersion.setStatus("current")
_H3cWlanAETagMultiAddr_Type = MacAddress
_H3cWlanAETagMultiAddr_Object = MibTableColumn
h3cWlanAETagMultiAddr = _H3cWlanAETagMultiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 8),
    _H3cWlanAETagMultiAddr_Type()
)
h3cWlanAETagMultiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAETagMultiAddr.setStatus("current")


class _H3cWlanAEEngineDetection_Type(Integer32):
    """Custom type h3cWlanAEEngineDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_H3cWlanAEEngineDetection_Type.__name__ = "Integer32"
_H3cWlanAEEngineDetection_Object = MibTableColumn
h3cWlanAEEngineDetection = _H3cWlanAEEngineDetection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 9),
    _H3cWlanAEEngineDetection_Type()
)
h3cWlanAEEngineDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEEngineDetection.setStatus("current")


class _H3cWlanAEReportMode_Type(Integer32):
    """Custom type h3cWlanAEReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("central", 2))
    )


_H3cWlanAEReportMode_Type.__name__ = "Integer32"
_H3cWlanAEReportMode_Object = MibTableColumn
h3cWlanAEReportMode = _H3cWlanAEReportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 1, 1, 10),
    _H3cWlanAEReportMode_Type()
)
h3cWlanAEReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEReportMode.setStatus("current")
_H3cWlanAERadioConfigTable_Object = MibTable
h3cWlanAERadioConfigTable = _H3cWlanAERadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2)
)
if mibBuilder.loadTexts:
    h3cWlanAERadioConfigTable.setStatus("current")
_H3cWlanAERadioConfigEntry_Object = MibTableRow
h3cWlanAERadioConfigEntry = _H3cWlanAERadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2, 1)
)
h3cWlanAERadioConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanAERadioAPSerialID"),
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanAEAPRadioID"),
)
if mibBuilder.loadTexts:
    h3cWlanAERadioConfigEntry.setStatus("current")


class _H3cWlanAERadioAPSerialID_Type(OctetString):
    """Custom type h3cWlanAERadioAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanAERadioAPSerialID_Type.__name__ = "OctetString"
_H3cWlanAERadioAPSerialID_Object = MibTableColumn
h3cWlanAERadioAPSerialID = _H3cWlanAERadioAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2, 1, 1),
    _H3cWlanAERadioAPSerialID_Type()
)
h3cWlanAERadioAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanAERadioAPSerialID.setStatus("current")


class _H3cWlanAEAPRadioID_Type(Integer32):
    """Custom type h3cWlanAEAPRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanAEAPRadioID_Type.__name__ = "Integer32"
_H3cWlanAEAPRadioID_Object = MibTableColumn
h3cWlanAEAPRadioID = _H3cWlanAEAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2, 1, 2),
    _H3cWlanAEAPRadioID_Type()
)
h3cWlanAEAPRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanAEAPRadioID.setStatus("current")
_H3cWlanAERadioStatus_Type = TruthValue
_H3cWlanAERadioStatus_Object = MibTableColumn
h3cWlanAERadioStatus = _H3cWlanAERadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2, 1, 3),
    _H3cWlanAERadioStatus_Type()
)
h3cWlanAERadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAERadioStatus.setStatus("current")
_H3cWlanAEMUStatus_Type = TruthValue
_H3cWlanAEMUStatus_Object = MibTableColumn
h3cWlanAEMUStatus = _H3cWlanAEMUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2, 1, 4),
    _H3cWlanAEMUStatus_Type()
)
h3cWlanAEMUStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAEMUStatus.setStatus("current")
_H3cWlanAETagStatus_Type = TruthValue
_H3cWlanAETagStatus_Object = MibTableColumn
h3cWlanAETagStatus = _H3cWlanAETagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 5, 2, 1, 5),
    _H3cWlanAETagStatus_Type()
)
h3cWlanAETagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanAETagStatus.setStatus("current")
_H3cWlanCommonConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanCommonConfigGroup = _H3cWlanCommonConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6)
)
_H3cWlanCommonConfigTable_Object = MibTable
h3cWlanCommonConfigTable = _H3cWlanCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1)
)
if mibBuilder.loadTexts:
    h3cWlanCommonConfigTable.setStatus("current")
_H3cWlanCommonConfigEntry_Object = MibTableRow
h3cWlanCommonConfigEntry = _H3cWlanCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1)
)
h3cWlanCommonConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanCommonAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cWlanCommonConfigEntry.setStatus("current")


class _H3cWlanCommonAPSerialID_Type(OctetString):
    """Custom type h3cWlanCommonAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanCommonAPSerialID_Type.__name__ = "OctetString"
_H3cWlanCommonAPSerialID_Object = MibTableColumn
h3cWlanCommonAPSerialID = _H3cWlanCommonAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 1),
    _H3cWlanCommonAPSerialID_Type()
)
h3cWlanCommonAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanCommonAPSerialID.setStatus("current")
_H3cWlanDilutionStatus_Type = TruthValue
_H3cWlanDilutionStatus_Object = MibTableColumn
h3cWlanDilutionStatus = _H3cWlanDilutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 2),
    _H3cWlanDilutionStatus_Type()
)
h3cWlanDilutionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanDilutionStatus.setStatus("current")


class _H3cWlanDilutionFactor_Type(Integer32):
    """Custom type h3cWlanDilutionFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_H3cWlanDilutionFactor_Type.__name__ = "Integer32"
_H3cWlanDilutionFactor_Object = MibTableColumn
h3cWlanDilutionFactor = _H3cWlanDilutionFactor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 3),
    _H3cWlanDilutionFactor_Type()
)
h3cWlanDilutionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanDilutionFactor.setStatus("current")


class _H3cWlanDilutionTimeout_Type(Integer32):
    """Custom type h3cWlanDilutionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_H3cWlanDilutionTimeout_Type.__name__ = "Integer32"
_H3cWlanDilutionTimeout_Object = MibTableColumn
h3cWlanDilutionTimeout = _H3cWlanDilutionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 4),
    _H3cWlanDilutionTimeout_Type()
)
h3cWlanDilutionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanDilutionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanDilutionTimeout.setUnits("Second")
_H3cWlanIgnoreBeacon_Type = TruthValue
_H3cWlanIgnoreBeacon_Object = MibTableColumn
h3cWlanIgnoreBeacon = _H3cWlanIgnoreBeacon_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 5),
    _H3cWlanIgnoreBeacon_Type()
)
h3cWlanIgnoreBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanIgnoreBeacon.setStatus("current")
_H3cWlanRateLimitStatus_Type = TruthValue
_H3cWlanRateLimitStatus_Object = MibTableColumn
h3cWlanRateLimitStatus = _H3cWlanRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 6),
    _H3cWlanRateLimitStatus_Type()
)
h3cWlanRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanRateLimitStatus.setStatus("current")


class _H3cWlanRateLimitCir_Type(Integer32):
    """Custom type h3cWlanRateLimitCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 1300000),
    )


_H3cWlanRateLimitCir_Type.__name__ = "Integer32"
_H3cWlanRateLimitCir_Object = MibTableColumn
h3cWlanRateLimitCir = _H3cWlanRateLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 7),
    _H3cWlanRateLimitCir_Type()
)
h3cWlanRateLimitCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanRateLimitCir.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanRateLimitCir.setUnits("Kbps")


class _H3cWlanRateLimitCbs_Type(Integer32):
    """Custom type h3cWlanRateLimitCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 130000000),
    )


_H3cWlanRateLimitCbs_Type.__name__ = "Integer32"
_H3cWlanRateLimitCbs_Object = MibTableColumn
h3cWlanRateLimitCbs = _H3cWlanRateLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 8),
    _H3cWlanRateLimitCbs_Type()
)
h3cWlanRateLimitCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanRateLimitCbs.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanRateLimitCbs.setUnits("Bytes")
_H3cWlanClientRateLimitStatus_Type = TruthValue
_H3cWlanClientRateLimitStatus_Object = MibTableColumn
h3cWlanClientRateLimitStatus = _H3cWlanClientRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 9),
    _H3cWlanClientRateLimitStatus_Type()
)
h3cWlanClientRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanClientRateLimitStatus.setStatus("current")


class _H3cWlanClientRateLimitCir_Type(Integer32):
    """Custom type h3cWlanClientRateLimitCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1300000),
    )


_H3cWlanClientRateLimitCir_Type.__name__ = "Integer32"
_H3cWlanClientRateLimitCir_Object = MibTableColumn
h3cWlanClientRateLimitCir = _H3cWlanClientRateLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 10),
    _H3cWlanClientRateLimitCir_Type()
)
h3cWlanClientRateLimitCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanClientRateLimitCir.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanClientRateLimitCir.setUnits("Kbps")


class _H3cWlanClientRateLimitCbs_Type(Integer32):
    """Custom type h3cWlanClientRateLimitCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(80, 130000000),
    )


_H3cWlanClientRateLimitCbs_Type.__name__ = "Integer32"
_H3cWlanClientRateLimitCbs_Object = MibTableColumn
h3cWlanClientRateLimitCbs = _H3cWlanClientRateLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 11),
    _H3cWlanClientRateLimitCbs_Type()
)
h3cWlanClientRateLimitCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanClientRateLimitCbs.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanClientRateLimitCbs.setUnits("Bytes")
_H3cWlanRssiStatus_Type = TruthValue
_H3cWlanRssiStatus_Object = MibTableColumn
h3cWlanRssiStatus = _H3cWlanRssiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 12),
    _H3cWlanRssiStatus_Type()
)
h3cWlanRssiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanRssiStatus.setStatus("current")


class _H3cWlanRssiThreshold_Type(Integer32):
    """Custom type h3cWlanRssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_H3cWlanRssiThreshold_Type.__name__ = "Integer32"
_H3cWlanRssiThreshold_Object = MibTableColumn
h3cWlanRssiThreshold = _H3cWlanRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 13),
    _H3cWlanRssiThreshold_Type()
)
h3cWlanRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanRssiThreshold.setStatus("current")
_H3cWlanIgnoreApFrame_Type = TruthValue
_H3cWlanIgnoreApFrame_Object = MibTableColumn
h3cWlanIgnoreApFrame = _H3cWlanIgnoreApFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 6, 1, 1, 14),
    _H3cWlanIgnoreApFrame_Type()
)
h3cWlanIgnoreApFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanIgnoreApFrame.setStatus("current")
_H3cWlanCUPIDConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanCUPIDConfigGroup = _H3cWlanCUPIDConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7)
)
_H3cWlanCUPIDConfigTable_Object = MibTable
h3cWlanCUPIDConfigTable = _H3cWlanCUPIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1)
)
if mibBuilder.loadTexts:
    h3cWlanCUPIDConfigTable.setStatus("current")
_H3cWlanCUPIDConfigEntry_Object = MibTableRow
h3cWlanCUPIDConfigEntry = _H3cWlanCUPIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1)
)
h3cWlanCUPIDConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanCupidAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cWlanCUPIDConfigEntry.setStatus("current")


class _H3cWlanCupidAPSerialID_Type(OctetString):
    """Custom type h3cWlanCupidAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanCupidAPSerialID_Type.__name__ = "OctetString"
_H3cWlanCupidAPSerialID_Object = MibTableColumn
h3cWlanCupidAPSerialID = _H3cWlanCupidAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 1),
    _H3cWlanCupidAPSerialID_Type()
)
h3cWlanCupidAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanCupidAPSerialID.setStatus("current")
_H3cWlanCupidStatus_Type = TruthValue
_H3cWlanCupidStatus_Object = MibTableColumn
h3cWlanCupidStatus = _H3cWlanCupidStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 2),
    _H3cWlanCupidStatus_Type()
)
h3cWlanCupidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidStatus.setStatus("current")
_H3cWlanCupidEngineAddr_Type = IpAddress
_H3cWlanCupidEngineAddr_Object = MibTableColumn
h3cWlanCupidEngineAddr = _H3cWlanCupidEngineAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 3),
    _H3cWlanCupidEngineAddr_Type()
)
h3cWlanCupidEngineAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidEngineAddr.setStatus("current")


class _H3cWlanCupidEnginePort_Type(Integer32):
    """Custom type h3cWlanCupidEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanCupidEnginePort_Type.__name__ = "Integer32"
_H3cWlanCupidEnginePort_Object = MibTableColumn
h3cWlanCupidEnginePort = _H3cWlanCupidEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 4),
    _H3cWlanCupidEnginePort_Type()
)
h3cWlanCupidEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidEnginePort.setStatus("current")


class _H3cWlanCupidVendorPort_Type(Integer32):
    """Custom type h3cWlanCupidVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanCupidVendorPort_Type.__name__ = "Integer32"
_H3cWlanCupidVendorPort_Object = MibTableColumn
h3cWlanCupidVendorPort = _H3cWlanCupidVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 5),
    _H3cWlanCupidVendorPort_Type()
)
h3cWlanCupidVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidVendorPort.setStatus("current")
_H3cWlanCupidReportStatus_Type = TruthValue
_H3cWlanCupidReportStatus_Object = MibTableColumn
h3cWlanCupidReportStatus = _H3cWlanCupidReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 6),
    _H3cWlanCupidReportStatus_Type()
)
h3cWlanCupidReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidReportStatus.setStatus("current")


class _H3cWlanCupidReportInterval_Type(Integer32):
    """Custom type h3cWlanCupidReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cWlanCupidReportInterval_Type.__name__ = "Integer32"
_H3cWlanCupidReportInterval_Object = MibTableColumn
h3cWlanCupidReportInterval = _H3cWlanCupidReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 7),
    _H3cWlanCupidReportInterval_Type()
)
h3cWlanCupidReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cWlanCupidReportInterval.setUnits("Second")
_H3cWlanCupidUnassSta_Type = TruthValue
_H3cWlanCupidUnassSta_Object = MibTableColumn
h3cWlanCupidUnassSta = _H3cWlanCupidUnassSta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 8),
    _H3cWlanCupidUnassSta_Type()
)
h3cWlanCupidUnassSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidUnassSta.setStatus("current")
_H3cWlanCupidUnassMeasureSta_Type = TruthValue
_H3cWlanCupidUnassMeasureSta_Object = MibTableColumn
h3cWlanCupidUnassMeasureSta = _H3cWlanCupidUnassMeasureSta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 9),
    _H3cWlanCupidUnassMeasureSta_Type()
)
h3cWlanCupidUnassMeasureSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidUnassMeasureSta.setStatus("current")


class _H3cWlanCupidReportMode_Type(Integer32):
    """Custom type h3cWlanCupidReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("central", 2))
    )


_H3cWlanCupidReportMode_Type.__name__ = "Integer32"
_H3cWlanCupidReportMode_Object = MibTableColumn
h3cWlanCupidReportMode = _H3cWlanCupidReportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 10),
    _H3cWlanCupidReportMode_Type()
)
h3cWlanCupidReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCupidReportMode.setStatus("current")


class _H3cWlanCUPIDReportFormat_Type(Integer32):
    """Custom type h3cWlanCUPIDReportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("lightweight", 2))
    )


_H3cWlanCUPIDReportFormat_Type.__name__ = "Integer32"
_H3cWlanCUPIDReportFormat_Object = MibTableColumn
h3cWlanCUPIDReportFormat = _H3cWlanCUPIDReportFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 7, 1, 1, 11),
    _H3cWlanCUPIDReportFormat_Type()
)
h3cWlanCUPIDReportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanCUPIDReportFormat.setStatus("current")
_H3cWlanFPConfigGroup_ObjectIdentity = ObjectIdentity
h3cWlanFPConfigGroup = _H3cWlanFPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8)
)
_H3cWlanFPConfigTable_Object = MibTable
h3cWlanFPConfigTable = _H3cWlanFPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1)
)
if mibBuilder.loadTexts:
    h3cWlanFPConfigTable.setStatus("current")
_H3cWlanFPConfigEntry_Object = MibTableRow
h3cWlanFPConfigEntry = _H3cWlanFPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1)
)
h3cWlanFPConfigEntry.setIndexNames(
    (0, "H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanFPAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cWlanFPConfigEntry.setStatus("current")


class _H3cWlanFPAPSerialID_Type(OctetString):
    """Custom type h3cWlanFPAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cWlanFPAPSerialID_Type.__name__ = "OctetString"
_H3cWlanFPAPSerialID_Object = MibTableColumn
h3cWlanFPAPSerialID = _H3cWlanFPAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 1),
    _H3cWlanFPAPSerialID_Type()
)
h3cWlanFPAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cWlanFPAPSerialID.setStatus("current")
_H3cWlanFPStatus_Type = TruthValue
_H3cWlanFPStatus_Object = MibTableColumn
h3cWlanFPStatus = _H3cWlanFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 2),
    _H3cWlanFPStatus_Type()
)
h3cWlanFPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPStatus.setStatus("current")
_H3cWlanFPEngineAddr_Type = IpAddress
_H3cWlanFPEngineAddr_Object = MibTableColumn
h3cWlanFPEngineAddr = _H3cWlanFPEngineAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 3),
    _H3cWlanFPEngineAddr_Type()
)
h3cWlanFPEngineAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPEngineAddr.setStatus("current")


class _H3cWlanFPEnginePort_Type(Integer32):
    """Custom type h3cWlanFPEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cWlanFPEnginePort_Type.__name__ = "Integer32"
_H3cWlanFPEnginePort_Object = MibTableColumn
h3cWlanFPEnginePort = _H3cWlanFPEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 4),
    _H3cWlanFPEnginePort_Type()
)
h3cWlanFPEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPEnginePort.setStatus("current")


class _H3cWlanFPVendorPort_Type(Integer32):
    """Custom type h3cWlanFPVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cWlanFPVendorPort_Type.__name__ = "Integer32"
_H3cWlanFPVendorPort_Object = MibTableColumn
h3cWlanFPVendorPort = _H3cWlanFPVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 5),
    _H3cWlanFPVendorPort_Type()
)
h3cWlanFPVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPVendorPort.setStatus("current")
_H3cWlanFPRawFrameReport_Type = TruthValue
_H3cWlanFPRawFrameReport_Object = MibTableColumn
h3cWlanFPRawFrameReport = _H3cWlanFPRawFrameReport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 6),
    _H3cWlanFPRawFrameReport_Type()
)
h3cWlanFPRawFrameReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPRawFrameReport.setStatus("current")
_H3cWlanFPMUReport_Type = TruthValue
_H3cWlanFPMUReport_Object = MibTableColumn
h3cWlanFPMUReport = _H3cWlanFPMUReport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 7),
    _H3cWlanFPMUReport_Type()
)
h3cWlanFPMUReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPMUReport.setStatus("current")


class _H3cWlanFPReportMode_Type(Integer32):
    """Custom type h3cWlanFPReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("central", 2))
    )


_H3cWlanFPReportMode_Type.__name__ = "Integer32"
_H3cWlanFPReportMode_Object = MibTableColumn
h3cWlanFPReportMode = _H3cWlanFPReportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 8),
    _H3cWlanFPReportMode_Type()
)
h3cWlanFPReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPReportMode.setStatus("current")


class _H3cWlanFPReportFormat_Type(Integer32):
    """Custom type h3cWlanFPReportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("lightweight", 2),
          ("cupidhybrid", 3))
    )


_H3cWlanFPReportFormat_Type.__name__ = "Integer32"
_H3cWlanFPReportFormat_Object = MibTableColumn
h3cWlanFPReportFormat = _H3cWlanFPReportFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 9),
    _H3cWlanFPReportFormat_Type()
)
h3cWlanFPReportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPReportFormat.setStatus("current")
_H3cWlanFPTagMultiAddr_Type = MacAddress
_H3cWlanFPTagMultiAddr_Object = MibTableColumn
h3cWlanFPTagMultiAddr = _H3cWlanFPTagMultiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 8, 1, 1, 10),
    _H3cWlanFPTagMultiAddr_Type()
)
h3cWlanFPTagMultiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cWlanFPTagMultiAddr.setStatus("current")

# Managed Objects groups


# Notification objects

h3cWlanModuleInsertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 0, 1)
)
h3cWlanModuleInsertTrap.setObjects(
      *(("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapAPMacAddress"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleID"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModulePhyType"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleModel"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleHwVersion"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleSwVersion"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleSequenceId"))
)
if mibBuilder.loadTexts:
    h3cWlanModuleInsertTrap.setStatus(
        "current"
    )

h3cWlanModuleRomveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 0, 2)
)
h3cWlanModuleRomveTrap.setObjects(
      *(("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapAPMacAddress"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleID"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModulePhyType"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleModel"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleHwVersion"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleSwVersion"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleSequenceId"))
)
if mibBuilder.loadTexts:
    h3cWlanModuleRomveTrap.setStatus(
        "current"
    )

h3cWlanModuleMissMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 19, 3, 0, 3)
)
h3cWlanModuleMissMatch.setObjects(
      *(("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapAPMacAddress"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleID"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleCfgType"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModulePhyType"),
        ("H3C-WLAN-FLEXAPP-CFG-MIB", "h3cWlanTrapModuleModel"))
)
if mibBuilder.loadTexts:
    h3cWlanModuleMissMatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-WLAN-FLEXAPP-CFG-MIB",
    **{"h3cWlanFlexAppCFG": h3cWlanFlexAppCFG,
       "h3cWlanModuleConfigGroup": h3cWlanModuleConfigGroup,
       "h3cWlanModuleConfigTable": h3cWlanModuleConfigTable,
       "h3cWlanModuleConfigEntry": h3cWlanModuleConfigEntry,
       "h3cWlanAPSerialID": h3cWlanAPSerialID,
       "h3cWlanModuleID": h3cWlanModuleID,
       "h3cWlanModuleType": h3cWlanModuleType,
       "h3cWlanModuleStatus": h3cWlanModuleStatus,
       "h3cWlanModuleReset": h3cWlanModuleReset,
       "h3cWlanModuleRstFac": h3cWlanModuleRstFac,
       "h3cWlanModuleUpWareStatus": h3cWlanModuleUpWareStatus,
       "h3cWlanModuleTxPower": h3cWlanModuleTxPower,
       "h3cWlanModuleManualUpdate": h3cWlanModuleManualUpdate,
       "h3cWlanModuleInfoTable": h3cWlanModuleInfoTable,
       "h3cWlanModuleInfoEntry": h3cWlanModuleInfoEntry,
       "h3cDot11IOTAPSerialID": h3cDot11IOTAPSerialID,
       "h3cDot11IOTModuleID": h3cDot11IOTModuleID,
       "h3cDot11IOTModuleType": h3cDot11IOTModuleType,
       "h3cDot11IOTModuleModel": h3cDot11IOTModuleModel,
       "h3cDot11IOTModuleHwVersion": h3cDot11IOTModuleHwVersion,
       "h3cDot11IOTModuleSwVersion": h3cDot11IOTModuleSwVersion,
       "h3cDot11IOTModuleSerialId": h3cDot11IOTModuleSerialId,
       "h3cWlanIOTConfigGroup": h3cWlanIOTConfigGroup,
       "h3cWlanIOTConfigTable": h3cWlanIOTConfigTable,
       "h3cWlanIOTConfigEntry": h3cWlanIOTConfigEntry,
       "h3cWlanIOTAPSerialID": h3cWlanIOTAPSerialID,
       "h3cWlanIOTEngineAdd": h3cWlanIOTEngineAdd,
       "h3cWlanIOTEnginePort": h3cWlanIOTEnginePort,
       "h3cWlanModuleNotifyGroup": h3cWlanModuleNotifyGroup,
       "h3cWlanModuleTraps": h3cWlanModuleTraps,
       "h3cWlanModuleInsertTrap": h3cWlanModuleInsertTrap,
       "h3cWlanModuleRomveTrap": h3cWlanModuleRomveTrap,
       "h3cWlanModuleMissMatch": h3cWlanModuleMissMatch,
       "h3cWlanModuleTrapVarObjects": h3cWlanModuleTrapVarObjects,
       "h3cWlanTrapAPMacAddress": h3cWlanTrapAPMacAddress,
       "h3cWlanTrapModuleID": h3cWlanTrapModuleID,
       "h3cWlanTrapModuleCfgType": h3cWlanTrapModuleCfgType,
       "h3cWlanTrapModulePhyType": h3cWlanTrapModulePhyType,
       "h3cWlanTrapModuleModel": h3cWlanTrapModuleModel,
       "h3cWlanTrapModuleHwVersion": h3cWlanTrapModuleHwVersion,
       "h3cWlanTrapModuleSwVersion": h3cWlanTrapModuleSwVersion,
       "h3cWlanTrapModuleSequenceId": h3cWlanTrapModuleSequenceId,
       "h3cWlanBLEConfigGroup": h3cWlanBLEConfigGroup,
       "h3cWlanBLEConfigTable": h3cWlanBLEConfigTable,
       "h3cWlanBLEConfigEntry": h3cWlanBLEConfigEntry,
       "h3cWlanBLEAPSerialID": h3cWlanBLEAPSerialID,
       "h3cWlanBLEStatus": h3cWlanBLEStatus,
       "h3cWlanBLEEngineAdd": h3cWlanBLEEngineAdd,
       "h3cWlanBLEEnginePort": h3cWlanBLEEnginePort,
       "h3cWlanBLEVendorPort": h3cWlanBLEVendorPort,
       "h3cWlanBLERssiStatus": h3cWlanBLERssiStatus,
       "h3cWlanBLERssiThreshold": h3cWlanBLERssiThreshold,
       "h3cWlanBLEConnectPassword": h3cWlanBLEConnectPassword,
       "h3cWlanBLECommandPassword": h3cWlanBLECommandPassword,
       "h3cWlanBLEReportStatus": h3cWlanBLEReportStatus,
       "h3cWlanBLEReportInterval": h3cWlanBLEReportInterval,
       "h3cWlanBLEAgingTime": h3cWlanBLEAgingTime,
       "h3cWlanBLERealTimeReportStatus": h3cWlanBLERealTimeReportStatus,
       "h3cWlanBLERealTimePrefix": h3cWlanBLERealTimePrefix,
       "h3cWlanBLEModuleConfigTable": h3cWlanBLEModuleConfigTable,
       "h3cWlanBLEModuleConfigEntry": h3cWlanBLEModuleConfigEntry,
       "h3cWlanBLEModuleAPSerialID": h3cWlanBLEModuleAPSerialID,
       "h3cWlanBLEModuleID": h3cWlanBLEModuleID,
       "h3cWlanBLEAdvReportStatus": h3cWlanBLEAdvReportStatus,
       "h3cWlanBLEAdvReportInterval": h3cWlanBLEAdvReportInterval,
       "h3cWlanBLEAdvUUID": h3cWlanBLEAdvUUID,
       "h3cWlanBLEAdvMajorID": h3cWlanBLEAdvMajorID,
       "h3cWlanBLEAdvMinorID": h3cWlanBLEAdvMinorID,
       "h3cWlanAEConfigGroup": h3cWlanAEConfigGroup,
       "h3cWlanAEConfigTable": h3cWlanAEConfigTable,
       "h3cWlanAEConfigEntry": h3cWlanAEConfigEntry,
       "h3cWlanAEAPSerialID": h3cWlanAEAPSerialID,
       "h3cWlanAEStatus": h3cWlanAEStatus,
       "h3cWlanAEEngineAddr": h3cWlanAEEngineAddr,
       "h3cWlanAEEnginePort": h3cWlanAEEnginePort,
       "h3cWlanAEVendorPort": h3cWlanAEVendorPort,
       "h3cWlanAETimeStamp": h3cWlanAETimeStamp,
       "h3cWlanAEVersion": h3cWlanAEVersion,
       "h3cWlanAETagMultiAddr": h3cWlanAETagMultiAddr,
       "h3cWlanAEEngineDetection": h3cWlanAEEngineDetection,
       "h3cWlanAEReportMode": h3cWlanAEReportMode,
       "h3cWlanAERadioConfigTable": h3cWlanAERadioConfigTable,
       "h3cWlanAERadioConfigEntry": h3cWlanAERadioConfigEntry,
       "h3cWlanAERadioAPSerialID": h3cWlanAERadioAPSerialID,
       "h3cWlanAEAPRadioID": h3cWlanAEAPRadioID,
       "h3cWlanAERadioStatus": h3cWlanAERadioStatus,
       "h3cWlanAEMUStatus": h3cWlanAEMUStatus,
       "h3cWlanAETagStatus": h3cWlanAETagStatus,
       "h3cWlanCommonConfigGroup": h3cWlanCommonConfigGroup,
       "h3cWlanCommonConfigTable": h3cWlanCommonConfigTable,
       "h3cWlanCommonConfigEntry": h3cWlanCommonConfigEntry,
       "h3cWlanCommonAPSerialID": h3cWlanCommonAPSerialID,
       "h3cWlanDilutionStatus": h3cWlanDilutionStatus,
       "h3cWlanDilutionFactor": h3cWlanDilutionFactor,
       "h3cWlanDilutionTimeout": h3cWlanDilutionTimeout,
       "h3cWlanIgnoreBeacon": h3cWlanIgnoreBeacon,
       "h3cWlanRateLimitStatus": h3cWlanRateLimitStatus,
       "h3cWlanRateLimitCir": h3cWlanRateLimitCir,
       "h3cWlanRateLimitCbs": h3cWlanRateLimitCbs,
       "h3cWlanClientRateLimitStatus": h3cWlanClientRateLimitStatus,
       "h3cWlanClientRateLimitCir": h3cWlanClientRateLimitCir,
       "h3cWlanClientRateLimitCbs": h3cWlanClientRateLimitCbs,
       "h3cWlanRssiStatus": h3cWlanRssiStatus,
       "h3cWlanRssiThreshold": h3cWlanRssiThreshold,
       "h3cWlanIgnoreApFrame": h3cWlanIgnoreApFrame,
       "h3cWlanCUPIDConfigGroup": h3cWlanCUPIDConfigGroup,
       "h3cWlanCUPIDConfigTable": h3cWlanCUPIDConfigTable,
       "h3cWlanCUPIDConfigEntry": h3cWlanCUPIDConfigEntry,
       "h3cWlanCupidAPSerialID": h3cWlanCupidAPSerialID,
       "h3cWlanCupidStatus": h3cWlanCupidStatus,
       "h3cWlanCupidEngineAddr": h3cWlanCupidEngineAddr,
       "h3cWlanCupidEnginePort": h3cWlanCupidEnginePort,
       "h3cWlanCupidVendorPort": h3cWlanCupidVendorPort,
       "h3cWlanCupidReportStatus": h3cWlanCupidReportStatus,
       "h3cWlanCupidReportInterval": h3cWlanCupidReportInterval,
       "h3cWlanCupidUnassSta": h3cWlanCupidUnassSta,
       "h3cWlanCupidUnassMeasureSta": h3cWlanCupidUnassMeasureSta,
       "h3cWlanCupidReportMode": h3cWlanCupidReportMode,
       "h3cWlanCUPIDReportFormat": h3cWlanCUPIDReportFormat,
       "h3cWlanFPConfigGroup": h3cWlanFPConfigGroup,
       "h3cWlanFPConfigTable": h3cWlanFPConfigTable,
       "h3cWlanFPConfigEntry": h3cWlanFPConfigEntry,
       "h3cWlanFPAPSerialID": h3cWlanFPAPSerialID,
       "h3cWlanFPStatus": h3cWlanFPStatus,
       "h3cWlanFPEngineAddr": h3cWlanFPEngineAddr,
       "h3cWlanFPEnginePort": h3cWlanFPEnginePort,
       "h3cWlanFPVendorPort": h3cWlanFPVendorPort,
       "h3cWlanFPRawFrameReport": h3cWlanFPRawFrameReport,
       "h3cWlanFPMUReport": h3cWlanFPMUReport,
       "h3cWlanFPReportMode": h3cWlanFPReportMode,
       "h3cWlanFPReportFormat": h3cWlanFPReportFormat,
       "h3cWlanFPTagMultiAddr": h3cWlanFPTagMultiAddr}
)
