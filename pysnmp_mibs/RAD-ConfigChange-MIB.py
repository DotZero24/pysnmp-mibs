# SNMP MIB module (RAD-ConfigChange-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-ConfigChange-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:41 2025
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

(systemsEvents,) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "systemsEvents")

(agnt,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "agnt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

agnConfigChange = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConfigChange_ObjectIdentity = ObjectIdentity
configChange = _ConfigChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1)
)
_ConfigurationChangeTable_Object = MibTable
configurationChangeTable = _ConfigurationChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 1)
)
if mibBuilder.loadTexts:
    configurationChangeTable.setStatus("current")
_ConfigurationChangeEntry_Object = MibTableRow
configurationChangeEntry = _ConfigurationChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 1, 1)
)
configurationChangeEntry.setIndexNames(
    (0, "RAD-ConfigChange-MIB", "configurationChangeFamilyOid"),
)
if mibBuilder.loadTexts:
    configurationChangeEntry.setStatus("current")
_ConfigurationChangeFamilyOid_Type = ObjectIdentifier
_ConfigurationChangeFamilyOid_Object = MibTableColumn
configurationChangeFamilyOid = _ConfigurationChangeFamilyOid_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 1, 1, 1),
    _ConfigurationChangeFamilyOid_Type()
)
configurationChangeFamilyOid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configurationChangeFamilyOid.setStatus("current")
_ConfigurationChangeLastChangeId_Type = Unsigned32
_ConfigurationChangeLastChangeId_Object = MibTableColumn
configurationChangeLastChangeId = _ConfigurationChangeLastChangeId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 1, 1, 2),
    _ConfigurationChangeLastChangeId_Type()
)
configurationChangeLastChangeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationChangeLastChangeId.setStatus("current")


class _ConfigurationChangeOIDType_Type(Integer32):
    """Custom type configurationChangeOIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tableOID", 2),
          ("scalarOID", 3))
    )


_ConfigurationChangeOIDType_Type.__name__ = "Integer32"
_ConfigurationChangeOIDType_Object = MibTableColumn
configurationChangeOIDType = _ConfigurationChangeOIDType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 1, 1, 3),
    _ConfigurationChangeOIDType_Type()
)
configurationChangeOIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationChangeOIDType.setStatus("current")
_ConfigurationChangeId_Type = Unsigned32
_ConfigurationChangeId_Object = MibScalar
configurationChangeId = _ConfigurationChangeId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 2),
    _ConfigurationChangeId_Type()
)
configurationChangeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationChangeId.setStatus("current")


class _ConfigurationChangeTrapsEnable_Type(Integer32):
    """Custom type configurationChangeTrapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_ConfigurationChangeTrapsEnable_Type.__name__ = "Integer32"
_ConfigurationChangeTrapsEnable_Object = MibScalar
configurationChangeTrapsEnable = _ConfigurationChangeTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 4),
    _ConfigurationChangeTrapsEnable_Type()
)
configurationChangeTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationChangeTrapsEnable.setStatus("current")


class _ConfigurationChangeEnd_Type(Integer32):
    """Custom type configurationChangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("end", 2),
          ("startAndEnd", 3),
          ("continue", 4))
    )


_ConfigurationChangeEnd_Type.__name__ = "Integer32"
_ConfigurationChangeEnd_Object = MibScalar
configurationChangeEnd = _ConfigurationChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 5),
    _ConfigurationChangeEnd_Type()
)
configurationChangeEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configurationChangeEnd.setStatus("current")
_ConfigChangeNotificationTable_Object = MibTable
configChangeNotificationTable = _ConfigChangeNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 6)
)
if mibBuilder.loadTexts:
    configChangeNotificationTable.setStatus("current")
_ConfigChangeNotificationEntry_Object = MibTableRow
configChangeNotificationEntry = _ConfigChangeNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 6, 1)
)
configChangeNotificationEntry.setIndexNames(
    (0, "RAD-ConfigChange-MIB", "configChangeNotificationFamilyOid"),
)
if mibBuilder.loadTexts:
    configChangeNotificationEntry.setStatus("current")
_ConfigChangeNotificationFamilyOid_Type = ObjectIdentifier
_ConfigChangeNotificationFamilyOid_Object = MibTableColumn
configChangeNotificationFamilyOid = _ConfigChangeNotificationFamilyOid_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 6, 1, 1),
    _ConfigChangeNotificationFamilyOid_Type()
)
configChangeNotificationFamilyOid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configChangeNotificationFamilyOid.setStatus("current")
_ConfigChangeNotificationAdd_Type = ObjectIdentifier
_ConfigChangeNotificationAdd_Object = MibTableColumn
configChangeNotificationAdd = _ConfigChangeNotificationAdd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 6, 1, 2),
    _ConfigChangeNotificationAdd_Type()
)
configChangeNotificationAdd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configChangeNotificationAdd.setStatus("current")
_ConfigChangeNotificationChange_Type = ObjectIdentifier
_ConfigChangeNotificationChange_Object = MibTableColumn
configChangeNotificationChange = _ConfigChangeNotificationChange_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 6, 1, 3),
    _ConfigChangeNotificationChange_Type()
)
configChangeNotificationChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configChangeNotificationChange.setStatus("current")
_ConfigChangeNotificationRemove_Type = ObjectIdentifier
_ConfigChangeNotificationRemove_Object = MibTableColumn
configChangeNotificationRemove = _ConfigChangeNotificationRemove_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 6, 1, 4),
    _ConfigChangeNotificationRemove_Type()
)
configChangeNotificationRemove.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    configChangeNotificationRemove.setStatus("current")


class _ConfigChangeTransactionKey_Type(OctetString):
    """Custom type configChangeTransactionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigChangeTransactionKey_Type.__name__ = "OctetString"
_ConfigChangeTransactionKey_Object = MibScalar
configChangeTransactionKey = _ConfigChangeTransactionKey_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 75, 1, 7),
    _ConfigChangeTransactionKey_Type()
)
configChangeTransactionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configChangeTransactionKey.setStatus("current")

# Managed Objects groups


# Notification objects

systemConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 79)
)
systemConfigurationChange.setObjects(
      *(("RAD-ConfigChange-MIB", "configurationChangeId"),
        ("RAD-ConfigChange-MIB", "configChangeTransactionKey"))
)
if mibBuilder.loadTexts:
    systemConfigurationChange.setStatus(
        "current"
    )

systemConfigChangeEnableTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 80)
)
systemConfigChangeEnableTraps.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("RAD-ConfigChange-MIB", "configurationChangeId"),
        ("RAD-ConfigChange-MIB", "configurationChangeTrapsEnable"))
)
if mibBuilder.loadTexts:
    systemConfigChangeEnableTraps.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-ConfigChange-MIB",
    **{"systemConfigurationChange": systemConfigurationChange,
       "systemConfigChangeEnableTraps": systemConfigChangeEnableTraps,
       "agnConfigChange": agnConfigChange,
       "configChange": configChange,
       "configurationChangeTable": configurationChangeTable,
       "configurationChangeEntry": configurationChangeEntry,
       "configurationChangeFamilyOid": configurationChangeFamilyOid,
       "configurationChangeLastChangeId": configurationChangeLastChangeId,
       "configurationChangeOIDType": configurationChangeOIDType,
       "configurationChangeId": configurationChangeId,
       "configurationChangeTrapsEnable": configurationChangeTrapsEnable,
       "configurationChangeEnd": configurationChangeEnd,
       "configChangeNotificationTable": configChangeNotificationTable,
       "configChangeNotificationEntry": configChangeNotificationEntry,
       "configChangeNotificationFamilyOid": configChangeNotificationFamilyOid,
       "configChangeNotificationAdd": configChangeNotificationAdd,
       "configChangeNotificationChange": configChangeNotificationChange,
       "configChangeNotificationRemove": configChangeNotificationRemove,
       "configChangeTransactionKey": configChangeTransactionKey}
)
