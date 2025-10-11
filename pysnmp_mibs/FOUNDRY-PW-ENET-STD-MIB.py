# SNMP MIB module (FOUNDRY-PW-ENET-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/FOUNDRY-PW-ENET-STD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:37 2025
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

(pwIndex,) = mibBuilder.importSymbols(
    "FOUNDRY-PW-STD-MIB",
    "pwIndex")

(PwVlanCfg,) = mibBuilder.importSymbols(
    "FOUNDRY-PW-TC-STD-MIB",
    "PwVlanCfg")

(pwe3,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "pwe3")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

pwEnetStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4)
)
if mibBuilder.loadTexts:
    pwEnetStdMIB.setRevisions(
        ("2007-05-20 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PwEnetObjects_ObjectIdentity = ObjectIdentity
pwEnetObjects = _PwEnetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1)
)
_PwEnetTable_Object = MibTable
pwEnetTable = _PwEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    pwEnetTable.setStatus("current")
_PwEnetEntry_Object = MibTableRow
pwEnetEntry = _PwEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1)
)
pwEnetEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
    (0, "FOUNDRY-PW-ENET-STD-MIB", "pwEnetPwInstance"),
)
if mibBuilder.loadTexts:
    pwEnetEntry.setStatus("current")
_PwEnetPwInstance_Type = Unsigned32
_PwEnetPwInstance_Object = MibTableColumn
pwEnetPwInstance = _PwEnetPwInstance_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 1),
    _PwEnetPwInstance_Type()
)
pwEnetPwInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwEnetPwInstance.setStatus("current")
_PwEnetPwVlan_Type = PwVlanCfg
_PwEnetPwVlan_Object = MibTableColumn
pwEnetPwVlan = _PwEnetPwVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 2),
    _PwEnetPwVlan_Type()
)
pwEnetPwVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetPwVlan.setStatus("current")


class _PwEnetVlanMode_Type(Integer32):
    """Custom type pwEnetVlanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("portBased", 1),
          ("noChange", 2),
          ("changeVlan", 3),
          ("addVlan", 4),
          ("removeVlan", 5))
    )


_PwEnetVlanMode_Type.__name__ = "Integer32"
_PwEnetVlanMode_Object = MibTableColumn
pwEnetVlanMode = _PwEnetVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 3),
    _PwEnetVlanMode_Type()
)
pwEnetVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetVlanMode.setStatus("current")


class _PwEnetPortVlan_Type(PwVlanCfg):
    """Custom type pwEnetPortVlan based on PwVlanCfg"""
    defaultValue = 4097


_PwEnetPortVlan_Type.__name__ = "PwVlanCfg"
_PwEnetPortVlan_Object = MibTableColumn
pwEnetPortVlan = _PwEnetPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 4),
    _PwEnetPortVlan_Type()
)
pwEnetPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetPortVlan.setStatus("current")
_PwEnetPortIfIndex_Type = InterfaceIndexOrZero
_PwEnetPortIfIndex_Object = MibTableColumn
pwEnetPortIfIndex = _PwEnetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 5),
    _PwEnetPortIfIndex_Type()
)
pwEnetPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetPortIfIndex.setStatus("current")


class _PwEnetPwIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pwEnetPwIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PwEnetPwIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_PwEnetPwIfIndex_Object = MibTableColumn
pwEnetPwIfIndex = _PwEnetPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 6),
    _PwEnetPwIfIndex_Type()
)
pwEnetPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetPwIfIndex.setStatus("current")
_PwEnetRowStatus_Type = RowStatus
_PwEnetRowStatus_Object = MibTableColumn
pwEnetRowStatus = _PwEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 7),
    _PwEnetRowStatus_Type()
)
pwEnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetRowStatus.setStatus("current")


class _PwEnetStorageType_Type(StorageType):
    """Custom type pwEnetStorageType based on StorageType"""
    defaultValue = 3


_PwEnetStorageType_Type.__name__ = "StorageType"
_PwEnetStorageType_Object = MibTableColumn
pwEnetStorageType = _PwEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 1, 1, 8),
    _PwEnetStorageType_Type()
)
pwEnetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwEnetStorageType.setStatus("current")
_PwEnetStatsTable_Object = MibTable
pwEnetStatsTable = _PwEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    pwEnetStatsTable.setStatus("current")
_PwEnetStatsEntry_Object = MibTableRow
pwEnetStatsEntry = _PwEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 2, 1)
)
pwEnetStatsEntry.setIndexNames(
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwEnetStatsEntry.setStatus("current")
_PwEnetStatsIllegalVlan_Type = ZeroBasedCounter32
_PwEnetStatsIllegalVlan_Object = MibTableColumn
pwEnetStatsIllegalVlan = _PwEnetStatsIllegalVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 2, 1, 1),
    _PwEnetStatsIllegalVlan_Type()
)
pwEnetStatsIllegalVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwEnetStatsIllegalVlan.setStatus("current")
_PwEnetStatsIllegalLength_Type = ZeroBasedCounter32
_PwEnetStatsIllegalLength_Object = MibTableColumn
pwEnetStatsIllegalLength = _PwEnetStatsIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 1, 2, 1, 2),
    _PwEnetStatsIllegalLength_Type()
)
pwEnetStatsIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwEnetStatsIllegalLength.setStatus("current")
_PwEnetConformance_ObjectIdentity = ObjectIdentity
pwEnetConformance = _PwEnetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2)
)
_PwEnetGroups_ObjectIdentity = ObjectIdentity
pwEnetGroups = _PwEnetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2, 1)
)
_PwEnetCompliances_ObjectIdentity = ObjectIdentity
pwEnetCompliances = _PwEnetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2, 2)
)

# Managed Objects groups

pwEnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2, 1, 1)
)
pwEnetGroup.setObjects(
      *(("FOUNDRY-PW-ENET-STD-MIB", "pwEnetPwVlan"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetVlanMode"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetPortVlan"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetPortIfIndex"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetPwIfIndex"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetRowStatus"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetStorageType"))
)
if mibBuilder.loadTexts:
    pwEnetGroup.setStatus("current")

pwEnetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2, 1, 2)
)
pwEnetStatsGroup.setObjects(
      *(("FOUNDRY-PW-ENET-STD-MIB", "pwEnetStatsIllegalVlan"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetStatsIllegalLength"))
)
if mibBuilder.loadTexts:
    pwEnetStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pwEnetModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2, 2, 1)
)
pwEnetModuleFullCompliance.setObjects(
      *(("FOUNDRY-PW-ENET-STD-MIB", "pwEnetGroup"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetStatsGroup"))
)
if mibBuilder.loadTexts:
    pwEnetModuleFullCompliance.setStatus(
        "current"
    )

pwEnetModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1, 4, 2, 2, 2)
)
pwEnetModuleReadOnlyCompliance.setObjects(
      *(("FOUNDRY-PW-ENET-STD-MIB", "pwEnetGroup"),
        ("FOUNDRY-PW-ENET-STD-MIB", "pwEnetStatsGroup"))
)
if mibBuilder.loadTexts:
    pwEnetModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-PW-ENET-STD-MIB",
    **{"pwEnetStdMIB": pwEnetStdMIB,
       "pwEnetObjects": pwEnetObjects,
       "pwEnetTable": pwEnetTable,
       "pwEnetEntry": pwEnetEntry,
       "pwEnetPwInstance": pwEnetPwInstance,
       "pwEnetPwVlan": pwEnetPwVlan,
       "pwEnetVlanMode": pwEnetVlanMode,
       "pwEnetPortVlan": pwEnetPortVlan,
       "pwEnetPortIfIndex": pwEnetPortIfIndex,
       "pwEnetPwIfIndex": pwEnetPwIfIndex,
       "pwEnetRowStatus": pwEnetRowStatus,
       "pwEnetStorageType": pwEnetStorageType,
       "pwEnetStatsTable": pwEnetStatsTable,
       "pwEnetStatsEntry": pwEnetStatsEntry,
       "pwEnetStatsIllegalVlan": pwEnetStatsIllegalVlan,
       "pwEnetStatsIllegalLength": pwEnetStatsIllegalLength,
       "pwEnetConformance": pwEnetConformance,
       "pwEnetGroups": pwEnetGroups,
       "pwEnetGroup": pwEnetGroup,
       "pwEnetStatsGroup": pwEnetStatsGroup,
       "pwEnetCompliances": pwEnetCompliances,
       "pwEnetModuleFullCompliance": pwEnetModuleFullCompliance,
       "pwEnetModuleReadOnlyCompliance": pwEnetModuleReadOnlyCompliance}
)
