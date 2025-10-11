# SNMP MIB module (FS-EG-BSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-EG-BSP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:18 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsEgBspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147)
)
if mibBuilder.loadTexts:
    fsEgBspMIB.setRevisions(
        ("2016-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsEgBspMIBObjects_ObjectIdentity = ObjectIdentity
fsEgBspMIBObjects = _FsEgBspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1)
)
_FsEgBspMaxNumber_Type = Integer32
_FsEgBspMaxNumber_Object = MibScalar
fsEgBspMaxNumber = _FsEgBspMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 1),
    _FsEgBspMaxNumber_Type()
)
fsEgBspMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEgBspMaxNumber.setStatus("current")
_FsEgBspInfoTable_Object = MibTable
fsEgBspInfoTable = _FsEgBspInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2)
)
if mibBuilder.loadTexts:
    fsEgBspInfoTable.setStatus("current")
_FsEgBspInfoEntry_Object = MibTableRow
fsEgBspInfoEntry = _FsEgBspInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1)
)
fsEgBspInfoEntry.setIndexNames(
    (0, "FS-EG-BSP-MIB", "fsEgBspInfoMacAddress"),
    (0, "FS-EG-BSP-MIB", "fsEgBspInfoVlanID"),
    (0, "FS-EG-BSP-MIB", "fsEgBspInfoPort"),
)
if mibBuilder.loadTexts:
    fsEgBspInfoEntry.setStatus("current")
_FsEgBspInfoMacAddress_Type = MacAddress
_FsEgBspInfoMacAddress_Object = MibTableColumn
fsEgBspInfoMacAddress = _FsEgBspInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 1),
    _FsEgBspInfoMacAddress_Type()
)
fsEgBspInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEgBspInfoMacAddress.setStatus("current")
_FsEgBspInfoVlanID_Type = Integer32
_FsEgBspInfoVlanID_Object = MibTableColumn
fsEgBspInfoVlanID = _FsEgBspInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 2),
    _FsEgBspInfoVlanID_Type()
)
fsEgBspInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEgBspInfoVlanID.setStatus("current")
_FsEgBspInfoPort_Type = Integer32
_FsEgBspInfoPort_Object = MibTableColumn
fsEgBspInfoPort = _FsEgBspInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 3),
    _FsEgBspInfoPort_Type()
)
fsEgBspInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEgBspInfoPort.setStatus("current")
_FsEgBspInfoAge_Type = Integer32
_FsEgBspInfoAge_Object = MibTableColumn
fsEgBspInfoAge = _FsEgBspInfoAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 4),
    _FsEgBspInfoAge_Type()
)
fsEgBspInfoAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEgBspInfoAge.setStatus("current")
_FsEgBspMIBConformance_ObjectIdentity = ObjectIdentity
fsEgBspMIBConformance = _FsEgBspMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2)
)
_FsEgBspMIBCompliances_ObjectIdentity = ObjectIdentity
fsEgBspMIBCompliances = _FsEgBspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 1)
)
_FsEgBspMIBGroups_ObjectIdentity = ObjectIdentity
fsEgBspMIBGroups = _FsEgBspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 2)
)

# Managed Objects groups

fsEgBspMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 2, 1)
)
fsEgBspMIBGroup.setObjects(
      *(("FS-EG-BSP-MIB", "fsEgBspMaxNumber"),
        ("FS-EG-BSP-MIB", "fsEgBspInfoMacAddress"),
        ("FS-EG-BSP-MIB", "fsEgBspInfoVlanID"),
        ("FS-EG-BSP-MIB", "fsEgBspInfoPort"),
        ("FS-EG-BSP-MIB", "fsEgBspInfoAge"))
)
if mibBuilder.loadTexts:
    fsEgBspMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsEgBspMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 1, 1)
)
fsEgBspMIBCompliance.setObjects(
    ("FS-EG-BSP-MIB", "fsEgBspMIBGroup")
)
if mibBuilder.loadTexts:
    fsEgBspMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-EG-BSP-MIB",
    **{"fsEgBspMIB": fsEgBspMIB,
       "fsEgBspMIBObjects": fsEgBspMIBObjects,
       "fsEgBspMaxNumber": fsEgBspMaxNumber,
       "fsEgBspInfoTable": fsEgBspInfoTable,
       "fsEgBspInfoEntry": fsEgBspInfoEntry,
       "fsEgBspInfoMacAddress": fsEgBspInfoMacAddress,
       "fsEgBspInfoVlanID": fsEgBspInfoVlanID,
       "fsEgBspInfoPort": fsEgBspInfoPort,
       "fsEgBspInfoAge": fsEgBspInfoAge,
       "fsEgBspMIBConformance": fsEgBspMIBConformance,
       "fsEgBspMIBCompliances": fsEgBspMIBCompliances,
       "fsEgBspMIBCompliance": fsEgBspMIBCompliance,
       "fsEgBspMIBGroups": fsEgBspMIBGroups,
       "fsEgBspMIBGroup": fsEgBspMIBGroup}
)
