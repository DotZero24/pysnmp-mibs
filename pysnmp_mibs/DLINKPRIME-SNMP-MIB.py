# SNMP MIB module (DLINKPRIME-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:26 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,
 SnmpEngineID,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "SnmpSecurityModel")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15)
)
if mibBuilder.loadTexts:
    dlinkPrimeSnmpMIB.setRevisions(
        ("2014-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpSnmpMIBNotifications_ObjectIdentity = ObjectIdentity
dpSnmpMIBNotifications = _DpSnmpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 0)
)
_DpSnmpMIBObjects_ObjectIdentity = ObjectIdentity
dpSnmpMIBObjects = _DpSnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1)
)
_DpSnmpGeneral_ObjectIdentity = ObjectIdentity
dpSnmpGeneral = _DpSnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 1)
)
_DpSnmpServiceEnabled_Type = TruthValue
_DpSnmpServiceEnabled_Object = MibScalar
dpSnmpServiceEnabled = _DpSnmpServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 1, 1),
    _DpSnmpServiceEnabled_Type()
)
dpSnmpServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpServiceEnabled.setStatus("current")
_DpSnmpMIBTrap_ObjectIdentity = ObjectIdentity
dpSnmpMIBTrap = _DpSnmpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 2)
)
_DpSnmpTrapGlobalEnabled_Type = TruthValue
_DpSnmpTrapGlobalEnabled_Object = MibScalar
dpSnmpTrapGlobalEnabled = _DpSnmpTrapGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 2, 1),
    _DpSnmpTrapGlobalEnabled_Type()
)
dpSnmpTrapGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpTrapGlobalEnabled.setStatus("current")


class _DpSnmpTrapGlobalNotifyEnable_Type(Bits):
    """Custom type dpSnmpTrapGlobalNotifyEnable based on Bits"""
    namedValues = NamedValues(
        *(("linkUp", 0),
          ("linkDown", 1),
          ("coldStart", 2),
          ("warmStart", 3),
          ("authentication", 4))
    )

_DpSnmpTrapGlobalNotifyEnable_Type.__name__ = "Bits"
_DpSnmpTrapGlobalNotifyEnable_Object = MibScalar
dpSnmpTrapGlobalNotifyEnable = _DpSnmpTrapGlobalNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 2, 2),
    _DpSnmpTrapGlobalNotifyEnable_Type()
)
dpSnmpTrapGlobalNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpTrapGlobalNotifyEnable.setStatus("current")
_DpSnmpAccessCfg_ObjectIdentity = ObjectIdentity
dpSnmpAccessCfg = _DpSnmpAccessCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3)
)
_DpSnmpCommunityTable_Object = MibTable
dpSnmpCommunityTable = _DpSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dpSnmpCommunityTable.setStatus("current")
_DpSnmpCommunityEntry_Object = MibTableRow
dpSnmpCommunityEntry = _DpSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 1, 1)
)
dpSnmpCommunityEntry.setIndexNames(
    (0, "DLINKPRIME-SNMP-MIB", "dpSnmpCommunityName"),
)
if mibBuilder.loadTexts:
    dpSnmpCommunityEntry.setStatus("current")
_DpSnmpCommunityName_Type = SnmpAdminString
_DpSnmpCommunityName_Object = MibTableColumn
dpSnmpCommunityName = _DpSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 1, 1, 1),
    _DpSnmpCommunityName_Type()
)
dpSnmpCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpSnmpCommunityName.setStatus("current")
_DpSnmpCommunityAccessListName_Type = DisplayString
_DpSnmpCommunityAccessListName_Object = MibTableColumn
dpSnmpCommunityAccessListName = _DpSnmpCommunityAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 1, 1, 3),
    _DpSnmpCommunityAccessListName_Type()
)
dpSnmpCommunityAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpCommunityAccessListName.setStatus("current")
_DpSnmpHostTable_Object = MibTable
dpSnmpHostTable = _DpSnmpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dpSnmpHostTable.setStatus("current")
_DpSnmpHostEntry_Object = MibTableRow
dpSnmpHostEntry = _DpSnmpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 2, 1)
)
dpSnmpHostEntry.setIndexNames(
    (0, "DLINKPRIME-SNMP-MIB", "dpSnmpHostIndex"),
)
if mibBuilder.loadTexts:
    dpSnmpHostEntry.setStatus("current")
_DpSnmpHostIndex_Type = Unsigned32
_DpSnmpHostIndex_Object = MibTableColumn
dpSnmpHostIndex = _DpSnmpHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 2, 1, 1),
    _DpSnmpHostIndex_Type()
)
dpSnmpHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpSnmpHostIndex.setStatus("current")
_DpSnmpHostIPv4Addr_Type = IpAddress
_DpSnmpHostIPv4Addr_Object = MibTableColumn
dpSnmpHostIPv4Addr = _DpSnmpHostIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 2, 1, 2),
    _DpSnmpHostIPv4Addr_Type()
)
dpSnmpHostIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpHostIPv4Addr.setStatus("current")


class _DpSnmpHostSecurity_Type(Integer32):
    """Custom type dpSnmpHostSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_DpSnmpHostSecurity_Type.__name__ = "Integer32"
_DpSnmpHostSecurity_Object = MibTableColumn
dpSnmpHostSecurity = _DpSnmpHostSecurity_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 2, 1, 3),
    _DpSnmpHostSecurity_Type()
)
dpSnmpHostSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpHostSecurity.setStatus("current")


class _DpSnmpHostCommunityName_Type(SnmpAdminString):
    """Custom type dpSnmpHostCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DpSnmpHostCommunityName_Type.__name__ = "SnmpAdminString"
_DpSnmpHostCommunityName_Object = MibTableColumn
dpSnmpHostCommunityName = _DpSnmpHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 1, 3, 2, 1, 4),
    _DpSnmpHostCommunityName_Type()
)
dpSnmpHostCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSnmpHostCommunityName.setStatus("current")
_DpSnmpMIBConformance_ObjectIdentity = ObjectIdentity
dpSnmpMIBConformance = _DpSnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 2)
)
_DpSnmpCompliances_ObjectIdentity = ObjectIdentity
dpSnmpCompliances = _DpSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 2, 1)
)
_DpSnmpGroups_ObjectIdentity = ObjectIdentity
dpSnmpGroups = _DpSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 2, 2)
)

# Managed Objects groups

dpSnmpSysCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 2, 2, 1)
)
dpSnmpSysCfgGroup.setObjects(
    ("DLINKPRIME-SNMP-MIB", "dpSnmpServiceEnabled")
)
if mibBuilder.loadTexts:
    dpSnmpSysCfgGroup.setStatus("current")

dpSnmpTrapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 2, 2, 2)
)
dpSnmpTrapCfgGroup.setObjects(
      *(("DLINKPRIME-SNMP-MIB", "dpSnmpTrapGlobalEnabled"),
        ("DLINKPRIME-SNMP-MIB", "dpSnmpTrapGlobalNotifyEnable"))
)
if mibBuilder.loadTexts:
    dpSnmpTrapCfgGroup.setStatus("current")

dpSnmpCommunityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 15, 2, 2, 3)
)
dpSnmpCommunityExtGroup.setObjects(
    ("DLINKPRIME-SNMP-MIB", "dpSnmpCommunityAccessListName")
)
if mibBuilder.loadTexts:
    dpSnmpCommunityExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SNMP-MIB",
    **{"dlinkPrimeSnmpMIB": dlinkPrimeSnmpMIB,
       "dpSnmpMIBNotifications": dpSnmpMIBNotifications,
       "dpSnmpMIBObjects": dpSnmpMIBObjects,
       "dpSnmpGeneral": dpSnmpGeneral,
       "dpSnmpServiceEnabled": dpSnmpServiceEnabled,
       "dpSnmpMIBTrap": dpSnmpMIBTrap,
       "dpSnmpTrapGlobalEnabled": dpSnmpTrapGlobalEnabled,
       "dpSnmpTrapGlobalNotifyEnable": dpSnmpTrapGlobalNotifyEnable,
       "dpSnmpAccessCfg": dpSnmpAccessCfg,
       "dpSnmpCommunityTable": dpSnmpCommunityTable,
       "dpSnmpCommunityEntry": dpSnmpCommunityEntry,
       "dpSnmpCommunityName": dpSnmpCommunityName,
       "dpSnmpCommunityAccessListName": dpSnmpCommunityAccessListName,
       "dpSnmpHostTable": dpSnmpHostTable,
       "dpSnmpHostEntry": dpSnmpHostEntry,
       "dpSnmpHostIndex": dpSnmpHostIndex,
       "dpSnmpHostIPv4Addr": dpSnmpHostIPv4Addr,
       "dpSnmpHostSecurity": dpSnmpHostSecurity,
       "dpSnmpHostCommunityName": dpSnmpHostCommunityName,
       "dpSnmpMIBConformance": dpSnmpMIBConformance,
       "dpSnmpCompliances": dpSnmpCompliances,
       "dpSnmpGroups": dpSnmpGroups,
       "dpSnmpSysCfgGroup": dpSnmpSysCfgGroup,
       "dpSnmpTrapCfgGroup": dpSnmpTrapCfgGroup,
       "dpSnmpCommunityExtGroup": dpSnmpCommunityExtGroup}
)
