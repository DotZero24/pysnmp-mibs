# SNMP MIB module (DES7200-ANTI-ARPCHEAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:11 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "DES7200-TC",
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

myAntiArpcheatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41)
)
if mibBuilder.loadTexts:
    myAntiArpcheatMIB.setRevisions(
        ("2007-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyAntiArpcheatMIBObjects_ObjectIdentity = ObjectIdentity
myAntiArpcheatMIBObjects = _MyAntiArpcheatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1)
)
_MyTrustedArpDelete_Type = Integer32
_MyTrustedArpDelete_Object = MibScalar
myTrustedArpDelete = _MyTrustedArpDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 1),
    _MyTrustedArpDelete_Type()
)
myTrustedArpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTrustedArpDelete.setStatus("current")
_MyTrustedArpTable_Object = MibTable
myTrustedArpTable = _MyTrustedArpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    myTrustedArpTable.setStatus("current")
_MyTrustedArpEntry_Object = MibTableRow
myTrustedArpEntry = _MyTrustedArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1)
)
myTrustedArpEntry.setIndexNames(
    (0, "DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
    (0, "DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
)
if mibBuilder.loadTexts:
    myTrustedArpEntry.setStatus("current")
_TrustedArpIfIndex_Type = IfIndex
_TrustedArpIfIndex_Object = MibTableColumn
trustedArpIfIndex = _TrustedArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 1),
    _TrustedArpIfIndex_Type()
)
trustedArpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedArpIfIndex.setStatus("current")
_TrustedArpIp_Type = IpAddress
_TrustedArpIp_Object = MibTableColumn
trustedArpIp = _TrustedArpIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 2),
    _TrustedArpIp_Type()
)
trustedArpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedArpIp.setStatus("current")
_TrustedArpMediaPhysAddress_Type = MacAddress
_TrustedArpMediaPhysAddress_Object = MibTableColumn
trustedArpMediaPhysAddress = _TrustedArpMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 3),
    _TrustedArpMediaPhysAddress_Type()
)
trustedArpMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpMediaPhysAddress.setStatus("current")
_TrustedArpVlan_Type = VlanId
_TrustedArpVlan_Object = MibTableColumn
trustedArpVlan = _TrustedArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 4),
    _TrustedArpVlan_Type()
)
trustedArpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpVlan.setStatus("current")
_TrustedArpOperationType_Type = Integer32
_TrustedArpOperationType_Object = MibTableColumn
trustedArpOperationType = _TrustedArpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 1, 2, 1, 5),
    _TrustedArpOperationType_Type()
)
trustedArpOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpOperationType.setStatus("current")
_MyAntiArpcheatMIBConformance_ObjectIdentity = ObjectIdentity
myAntiArpcheatMIBConformance = _MyAntiArpcheatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2)
)
_MyAntiArpcheatMIBCompliances_ObjectIdentity = ObjectIdentity
myAntiArpcheatMIBCompliances = _MyAntiArpcheatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 1)
)
_MyAntiArpcheatMIBGroups_ObjectIdentity = ObjectIdentity
myAntiArpcheatMIBGroups = _MyAntiArpcheatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 2)
)

# Managed Objects groups

myAntiArpcheatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 2, 1)
)
myAntiArpcheatMIBGroup.setObjects(
      *(("DES7200-ANTI-ARPCHEAT-MIB", "myTrustedArpDelete"),
        ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
        ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
        ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"),
        ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpVlan"),
        ("DES7200-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
)
if mibBuilder.loadTexts:
    myAntiArpcheatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myAntiArpcheatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 41, 2, 1, 1)
)
myAntiArpcheatMIBCompliance.setObjects(
    ("DES7200-ANTI-ARPCHEAT-MIB", "myAntiArpcheatMIBGroup")
)
if mibBuilder.loadTexts:
    myAntiArpcheatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-ANTI-ARPCHEAT-MIB",
    **{"myAntiArpcheatMIB": myAntiArpcheatMIB,
       "myAntiArpcheatMIBObjects": myAntiArpcheatMIBObjects,
       "myTrustedArpDelete": myTrustedArpDelete,
       "myTrustedArpTable": myTrustedArpTable,
       "myTrustedArpEntry": myTrustedArpEntry,
       "trustedArpIfIndex": trustedArpIfIndex,
       "trustedArpIp": trustedArpIp,
       "trustedArpMediaPhysAddress": trustedArpMediaPhysAddress,
       "trustedArpVlan": trustedArpVlan,
       "trustedArpOperationType": trustedArpOperationType,
       "myAntiArpcheatMIBConformance": myAntiArpcheatMIBConformance,
       "myAntiArpcheatMIBCompliances": myAntiArpcheatMIBCompliances,
       "myAntiArpcheatMIBCompliance": myAntiArpcheatMIBCompliance,
       "myAntiArpcheatMIBGroups": myAntiArpcheatMIBGroups,
       "myAntiArpcheatMIBGroup": myAntiArpcheatMIBGroup}
)
