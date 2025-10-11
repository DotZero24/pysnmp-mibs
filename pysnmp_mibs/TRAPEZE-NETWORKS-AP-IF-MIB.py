# SNMP MIB module (TRAPEZE-NETWORKS-AP-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trapeze/TRAPEZE-NETWORKS-AP-IF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:20 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

(TrpzApSerialNum,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApSerialNum")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzApIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16)
)
if mibBuilder.loadTexts:
    trpzApIfMib.setRevisions(
        ("2008-11-20 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzApInterfaceIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_TrpzApIfMibObjects_ObjectIdentity = ObjectIdentity
trpzApIfMibObjects = _TrpzApIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1)
)
_TrpzApIfTable_Object = MibTable
trpzApIfTable = _TrpzApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1)
)
if mibBuilder.loadTexts:
    trpzApIfTable.setStatus("current")
_TrpzApIfEntry_Object = MibTableRow
trpzApIfEntry = _TrpzApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1)
)
trpzApIfEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfApSerialNum"),
    (0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfIndex"),
)
if mibBuilder.loadTexts:
    trpzApIfEntry.setStatus("current")
_TrpzApIfApSerialNum_Type = TrpzApSerialNum
_TrpzApIfApSerialNum_Object = MibTableColumn
trpzApIfApSerialNum = _TrpzApIfApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 1),
    _TrpzApIfApSerialNum_Type()
)
trpzApIfApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApIfApSerialNum.setStatus("current")
_TrpzApIfIndex_Type = TrpzApInterfaceIndex
_TrpzApIfIndex_Object = MibTableColumn
trpzApIfIndex = _TrpzApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 2),
    _TrpzApIfIndex_Type()
)
trpzApIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApIfIndex.setStatus("current")
_TrpzApIfName_Type = DisplayString
_TrpzApIfName_Object = MibTableColumn
trpzApIfName = _TrpzApIfName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 3),
    _TrpzApIfName_Type()
)
trpzApIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApIfName.setStatus("current")
_TrpzApIfType_Type = IANAifType
_TrpzApIfType_Object = MibTableColumn
trpzApIfType = _TrpzApIfType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 4),
    _TrpzApIfType_Type()
)
trpzApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApIfType.setStatus("current")
_TrpzApIfMtu_Type = Unsigned32
_TrpzApIfMtu_Object = MibTableColumn
trpzApIfMtu = _TrpzApIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 5),
    _TrpzApIfMtu_Type()
)
trpzApIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApIfMtu.setStatus("current")
_TrpzApIfHighSpeed_Type = Gauge32
_TrpzApIfHighSpeed_Object = MibTableColumn
trpzApIfHighSpeed = _TrpzApIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 6),
    _TrpzApIfHighSpeed_Type()
)
trpzApIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApIfHighSpeed.setStatus("current")
_TrpzApIfMac_Type = MacAddress
_TrpzApIfMac_Object = MibTableColumn
trpzApIfMac = _TrpzApIfMac_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 7),
    _TrpzApIfMac_Type()
)
trpzApIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApIfMac.setStatus("current")
_TrpzApIfConformance_ObjectIdentity = ObjectIdentity
trpzApIfConformance = _TrpzApIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 2)
)
_TrpzApIfCompliances_ObjectIdentity = ObjectIdentity
trpzApIfCompliances = _TrpzApIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1)
)
_TrpzApIfGroups_ObjectIdentity = ObjectIdentity
trpzApIfGroups = _TrpzApIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2)
)

# Managed Objects groups

trpzApIfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2, 1)
)
trpzApIfBasicGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfName"),
        ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfType"),
        ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMtu"),
        ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfHighSpeed"),
        ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMac"))
)
if mibBuilder.loadTexts:
    trpzApIfBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzApIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1, 1)
)
trpzApIfCompliance.setObjects(
    ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfBasicGroup")
)
if mibBuilder.loadTexts:
    trpzApIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-AP-IF-MIB",
    **{"TrpzApInterfaceIndex": TrpzApInterfaceIndex,
       "trpzApIfMib": trpzApIfMib,
       "trpzApIfMibObjects": trpzApIfMibObjects,
       "trpzApIfTable": trpzApIfTable,
       "trpzApIfEntry": trpzApIfEntry,
       "trpzApIfApSerialNum": trpzApIfApSerialNum,
       "trpzApIfIndex": trpzApIfIndex,
       "trpzApIfName": trpzApIfName,
       "trpzApIfType": trpzApIfType,
       "trpzApIfMtu": trpzApIfMtu,
       "trpzApIfHighSpeed": trpzApIfHighSpeed,
       "trpzApIfMac": trpzApIfMac,
       "trpzApIfConformance": trpzApIfConformance,
       "trpzApIfCompliances": trpzApIfCompliances,
       "trpzApIfCompliance": trpzApIfCompliance,
       "trpzApIfGroups": trpzApIfGroups,
       "trpzApIfBasicGroup": trpzApIfBasicGroup}
)
