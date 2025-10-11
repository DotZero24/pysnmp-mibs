# SNMP MIB module (TPLINK-AUTOVOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-AUTOVOIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:02 2025
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

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkAutoVoipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98)
)
if mibBuilder.loadTexts:
    tplinkAutoVoipMIB.setRevisions(
        ("2012-12-13 16:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkAutoVoipMIBObjects_ObjectIdentity = ObjectIdentity
tplinkAutoVoipMIBObjects = _TplinkAutoVoipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1)
)
_AutoVoipGlobalConfig_ObjectIdentity = ObjectIdentity
autoVoipGlobalConfig = _AutoVoipGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 1)
)


class _AutoVoipGlobalEnable_Type(Integer32):
    """Custom type autoVoipGlobalEnable based on Integer32"""
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


_AutoVoipGlobalEnable_Type.__name__ = "Integer32"
_AutoVoipGlobalEnable_Object = MibScalar
autoVoipGlobalEnable = _AutoVoipGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 1, 1),
    _AutoVoipGlobalEnable_Type()
)
autoVoipGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoVoipGlobalEnable.setStatus("current")
_AutoVoipPortConfig_ObjectIdentity = ObjectIdentity
autoVoipPortConfig = _AutoVoipPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2)
)
_AutoVoipPortTable_Object = MibTable
autoVoipPortTable = _AutoVoipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    autoVoipPortTable.setStatus("current")
_AutoVoipPortEntry_Object = MibTableRow
autoVoipPortEntry = _AutoVoipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1)
)
autoVoipPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    autoVoipPortEntry.setStatus("current")


class _AutoVoipPortNumber_Type(OctetString):
    """Custom type autoVoipPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AutoVoipPortNumber_Type.__name__ = "OctetString"
_AutoVoipPortNumber_Object = MibTableColumn
autoVoipPortNumber = _AutoVoipPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1, 1),
    _AutoVoipPortNumber_Type()
)
autoVoipPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoVoipPortNumber.setStatus("current")


class _AutoVoipPortMode_Type(Integer32):
    """Custom type autoVoipPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("vlan", 1),
          ("dot1p", 2),
          ("none", 3),
          ("untagged", 4))
    )


_AutoVoipPortMode_Type.__name__ = "Integer32"
_AutoVoipPortMode_Object = MibTableColumn
autoVoipPortMode = _AutoVoipPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1, 2),
    _AutoVoipPortMode_Type()
)
autoVoipPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoVoipPortMode.setStatus("current")


class _AutoVoipPortValue_Type(Integer32):
    """Custom type autoVoipPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AutoVoipPortValue_Type.__name__ = "Integer32"
_AutoVoipPortValue_Object = MibTableColumn
autoVoipPortValue = _AutoVoipPortValue_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1, 3),
    _AutoVoipPortValue_Type()
)
autoVoipPortValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoVoipPortValue.setStatus("current")


class _AutoVoipCosOverrideMode_Type(Integer32):
    """Custom type autoVoipCosOverrideMode based on Integer32"""
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


_AutoVoipCosOverrideMode_Type.__name__ = "Integer32"
_AutoVoipCosOverrideMode_Object = MibTableColumn
autoVoipCosOverrideMode = _AutoVoipCosOverrideMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1, 4),
    _AutoVoipCosOverrideMode_Type()
)
autoVoipCosOverrideMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoVoipCosOverrideMode.setStatus("current")


class _AutoVoipOperaState_Type(Integer32):
    """Custom type autoVoipOperaState based on Integer32"""
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


_AutoVoipOperaState_Type.__name__ = "Integer32"
_AutoVoipOperaState_Object = MibTableColumn
autoVoipOperaState = _AutoVoipOperaState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1, 5),
    _AutoVoipOperaState_Type()
)
autoVoipOperaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoVoipOperaState.setStatus("current")


class _AutoVoipDscpValue_Type(Integer32):
    """Custom type autoVoipDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AutoVoipDscpValue_Type.__name__ = "Integer32"
_AutoVoipDscpValue_Object = MibTableColumn
autoVoipDscpValue = _AutoVoipDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 1, 2, 1, 1, 6),
    _AutoVoipDscpValue_Type()
)
autoVoipDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoVoipDscpValue.setStatus("current")
_TplinkAutoVoipMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkAutoVoipMIBNotifications = _TplinkAutoVoipMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 98, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-AUTOVOIP-MIB",
    **{"tplinkAutoVoipMIB": tplinkAutoVoipMIB,
       "tplinkAutoVoipMIBObjects": tplinkAutoVoipMIBObjects,
       "autoVoipGlobalConfig": autoVoipGlobalConfig,
       "autoVoipGlobalEnable": autoVoipGlobalEnable,
       "autoVoipPortConfig": autoVoipPortConfig,
       "autoVoipPortTable": autoVoipPortTable,
       "autoVoipPortEntry": autoVoipPortEntry,
       "autoVoipPortNumber": autoVoipPortNumber,
       "autoVoipPortMode": autoVoipPortMode,
       "autoVoipPortValue": autoVoipPortValue,
       "autoVoipCosOverrideMode": autoVoipCosOverrideMode,
       "autoVoipOperaState": autoVoipOperaState,
       "autoVoipDscpValue": autoVoipDscpValue,
       "tplinkAutoVoipMIBNotifications": tplinkAutoVoipMIBNotifications}
)
