# SNMP MIB module (FS-ANTI-ARPCHEAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:27 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

fsAntiArpcheatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41)
)
if mibBuilder.loadTexts:
    fsAntiArpcheatMIB.setRevisions(
        ("2007-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsAntiArpcheatMIBObjects_ObjectIdentity = ObjectIdentity
fsAntiArpcheatMIBObjects = _FsAntiArpcheatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1)
)
_FsTrustedArpDelete_Type = Integer32
_FsTrustedArpDelete_Object = MibScalar
fsTrustedArpDelete = _FsTrustedArpDelete_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 1),
    _FsTrustedArpDelete_Type()
)
fsTrustedArpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTrustedArpDelete.setStatus("current")
_FsTrustedArpTable_Object = MibTable
fsTrustedArpTable = _FsTrustedArpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    fsTrustedArpTable.setStatus("current")
_FsTrustedArpEntry_Object = MibTableRow
fsTrustedArpEntry = _FsTrustedArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1)
)
fsTrustedArpEntry.setIndexNames(
    (0, "FS-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
    (0, "FS-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
)
if mibBuilder.loadTexts:
    fsTrustedArpEntry.setStatus("current")
_TrustedArpIfIndex_Type = IfIndex
_TrustedArpIfIndex_Object = MibTableColumn
trustedArpIfIndex = _TrustedArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 1),
    _TrustedArpIfIndex_Type()
)
trustedArpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpIfIndex.setStatus("current")
_TrustedArpIp_Type = IpAddress
_TrustedArpIp_Object = MibTableColumn
trustedArpIp = _TrustedArpIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 2),
    _TrustedArpIp_Type()
)
trustedArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpIp.setStatus("current")
_TrustedArpMediaPhysAddress_Type = MacAddress
_TrustedArpMediaPhysAddress_Object = MibTableColumn
trustedArpMediaPhysAddress = _TrustedArpMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 3),
    _TrustedArpMediaPhysAddress_Type()
)
trustedArpMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpMediaPhysAddress.setStatus("current")
_TrustedArpVlan_Type = VlanId
_TrustedArpVlan_Object = MibTableColumn
trustedArpVlan = _TrustedArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 4),
    _TrustedArpVlan_Type()
)
trustedArpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpVlan.setStatus("current")
_TrustedArpOperationType_Type = Integer32
_TrustedArpOperationType_Object = MibTableColumn
trustedArpOperationType = _TrustedArpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 1, 2, 1, 5),
    _TrustedArpOperationType_Type()
)
trustedArpOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpOperationType.setStatus("current")
_FsAntiArpcheatMIBConformance_ObjectIdentity = ObjectIdentity
fsAntiArpcheatMIBConformance = _FsAntiArpcheatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2)
)
_FsAntiArpcheatMIBCompliances_ObjectIdentity = ObjectIdentity
fsAntiArpcheatMIBCompliances = _FsAntiArpcheatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 1)
)
_FsAntiArpcheatMIBGroups_ObjectIdentity = ObjectIdentity
fsAntiArpcheatMIBGroups = _FsAntiArpcheatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 2)
)

# Managed Objects groups

fsAntiArpcheatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 2, 1)
)
fsAntiArpcheatMIBGroup.setObjects(
      *(("FS-ANTI-ARPCHEAT-MIB", "fsTrustedArpDelete"),
        ("FS-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
        ("FS-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
        ("FS-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"),
        ("FS-ANTI-ARPCHEAT-MIB", "trustedArpVlan"),
        ("FS-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
)
if mibBuilder.loadTexts:
    fsAntiArpcheatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsAntiArpcheatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 41, 2, 1, 1)
)
fsAntiArpcheatMIBCompliance.setObjects(
    ("FS-ANTI-ARPCHEAT-MIB", "fsAntiArpcheatMIBGroup")
)
if mibBuilder.loadTexts:
    fsAntiArpcheatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ANTI-ARPCHEAT-MIB",
    **{"fsAntiArpcheatMIB": fsAntiArpcheatMIB,
       "fsAntiArpcheatMIBObjects": fsAntiArpcheatMIBObjects,
       "fsTrustedArpDelete": fsTrustedArpDelete,
       "fsTrustedArpTable": fsTrustedArpTable,
       "fsTrustedArpEntry": fsTrustedArpEntry,
       "trustedArpIfIndex": trustedArpIfIndex,
       "trustedArpIp": trustedArpIp,
       "trustedArpMediaPhysAddress": trustedArpMediaPhysAddress,
       "trustedArpVlan": trustedArpVlan,
       "trustedArpOperationType": trustedArpOperationType,
       "fsAntiArpcheatMIBConformance": fsAntiArpcheatMIBConformance,
       "fsAntiArpcheatMIBCompliances": fsAntiArpcheatMIBCompliances,
       "fsAntiArpcheatMIBCompliance": fsAntiArpcheatMIBCompliance,
       "fsAntiArpcheatMIBGroups": fsAntiArpcheatMIBGroups,
       "fsAntiArpcheatMIBGroup": fsAntiArpcheatMIBGroup}
)
