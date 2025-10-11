# SNMP MIB module (QTECH-ANTI-ARPCHEAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:03 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechAntiArpcheatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41)
)
if mibBuilder.loadTexts:
    qtechAntiArpcheatMIB.setRevisions(
        ("2007-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAntiArpcheatMIBObjects_ObjectIdentity = ObjectIdentity
qtechAntiArpcheatMIBObjects = _QtechAntiArpcheatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1)
)
_QtechTrustedArpDelete_Type = Integer32
_QtechTrustedArpDelete_Object = MibScalar
qtechTrustedArpDelete = _QtechTrustedArpDelete_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 1),
    _QtechTrustedArpDelete_Type()
)
qtechTrustedArpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTrustedArpDelete.setStatus("current")
_QtechTrustedArpTable_Object = MibTable
qtechTrustedArpTable = _QtechTrustedArpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    qtechTrustedArpTable.setStatus("current")
_QtechTrustedArpEntry_Object = MibTableRow
qtechTrustedArpEntry = _QtechTrustedArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1)
)
qtechTrustedArpEntry.setIndexNames(
    (0, "QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
    (0, "QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
)
if mibBuilder.loadTexts:
    qtechTrustedArpEntry.setStatus("current")
_TrustedArpIfIndex_Type = IfIndex
_TrustedArpIfIndex_Object = MibTableColumn
trustedArpIfIndex = _TrustedArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 1),
    _TrustedArpIfIndex_Type()
)
trustedArpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpIfIndex.setStatus("current")
_TrustedArpIp_Type = IpAddress
_TrustedArpIp_Object = MibTableColumn
trustedArpIp = _TrustedArpIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 2),
    _TrustedArpIp_Type()
)
trustedArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpIp.setStatus("current")
_TrustedArpMediaPhysAddress_Type = MacAddress
_TrustedArpMediaPhysAddress_Object = MibTableColumn
trustedArpMediaPhysAddress = _TrustedArpMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 3),
    _TrustedArpMediaPhysAddress_Type()
)
trustedArpMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpMediaPhysAddress.setStatus("current")
_TrustedArpVlan_Type = VlanId
_TrustedArpVlan_Object = MibTableColumn
trustedArpVlan = _TrustedArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 4),
    _TrustedArpVlan_Type()
)
trustedArpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpVlan.setStatus("current")
_TrustedArpOperationType_Type = Integer32
_TrustedArpOperationType_Object = MibTableColumn
trustedArpOperationType = _TrustedArpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 5),
    _TrustedArpOperationType_Type()
)
trustedArpOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedArpOperationType.setStatus("current")
_QtechAntiArpcheatMIBConformance_ObjectIdentity = ObjectIdentity
qtechAntiArpcheatMIBConformance = _QtechAntiArpcheatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2)
)
_QtechAntiArpcheatMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAntiArpcheatMIBCompliances = _QtechAntiArpcheatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 1)
)
_QtechAntiArpcheatMIBGroups_ObjectIdentity = ObjectIdentity
qtechAntiArpcheatMIBGroups = _QtechAntiArpcheatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 2)
)

# Managed Objects groups

qtechAntiArpcheatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 2, 1)
)
qtechAntiArpcheatMIBGroup.setObjects(
      *(("QTECH-ANTI-ARPCHEAT-MIB", "qtechTrustedArpDelete"),
        ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"),
        ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIp"),
        ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"),
        ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpVlan"),
        ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
)
if mibBuilder.loadTexts:
    qtechAntiArpcheatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechAntiArpcheatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 1, 1)
)
qtechAntiArpcheatMIBCompliance.setObjects(
    ("QTECH-ANTI-ARPCHEAT-MIB", "qtechAntiArpcheatMIBGroup")
)
if mibBuilder.loadTexts:
    qtechAntiArpcheatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ANTI-ARPCHEAT-MIB",
    **{"qtechAntiArpcheatMIB": qtechAntiArpcheatMIB,
       "qtechAntiArpcheatMIBObjects": qtechAntiArpcheatMIBObjects,
       "qtechTrustedArpDelete": qtechTrustedArpDelete,
       "qtechTrustedArpTable": qtechTrustedArpTable,
       "qtechTrustedArpEntry": qtechTrustedArpEntry,
       "trustedArpIfIndex": trustedArpIfIndex,
       "trustedArpIp": trustedArpIp,
       "trustedArpMediaPhysAddress": trustedArpMediaPhysAddress,
       "trustedArpVlan": trustedArpVlan,
       "trustedArpOperationType": trustedArpOperationType,
       "qtechAntiArpcheatMIBConformance": qtechAntiArpcheatMIBConformance,
       "qtechAntiArpcheatMIBCompliances": qtechAntiArpcheatMIBCompliances,
       "qtechAntiArpcheatMIBCompliance": qtechAntiArpcheatMIBCompliance,
       "qtechAntiArpcheatMIBGroups": qtechAntiArpcheatMIBGroups,
       "qtechAntiArpcheatMIBGroup": qtechAntiArpcheatMIBGroup}
)
