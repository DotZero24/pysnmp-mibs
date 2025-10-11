# SNMP MIB module (TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trapeze/TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:19 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(TrpzApSerialNum,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApSerialNum")

(TrpzPhysPortNumber,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzPhysPortNumber")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzApUnconfiguredMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15)
)
if mibBuilder.loadTexts:
    trpzApUnconfiguredMib.setRevisions(
        ("2011-06-15 00:11",
         "2008-11-14 00:04")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzApUnconfiguredOrphanReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("no-configuration", 2),
          ("ap-license-exceeded", 3),
          ("controller-behind-nat", 4),
          ("ap-model-mismatch", 5),
          ("no-macs", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzApUnconfMibObjects_ObjectIdentity = ObjectIdentity
trpzApUnconfMibObjects = _TrpzApUnconfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1)
)
_TrpzApUnconfOrphanTable_Object = MibTable
trpzApUnconfOrphanTable = _TrpzApUnconfOrphanTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2)
)
if mibBuilder.loadTexts:
    trpzApUnconfOrphanTable.setStatus("current")
_TrpzApUnconfOrphanEntry_Object = MibTableRow
trpzApUnconfOrphanEntry = _TrpzApUnconfOrphanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1)
)
trpzApUnconfOrphanEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApSerialNum"),
)
if mibBuilder.loadTexts:
    trpzApUnconfOrphanEntry.setStatus("current")
_TrpzApUnconfOrphanApSerialNum_Type = TrpzApSerialNum
_TrpzApUnconfOrphanApSerialNum_Object = MibTableColumn
trpzApUnconfOrphanApSerialNum = _TrpzApUnconfOrphanApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 1),
    _TrpzApUnconfOrphanApSerialNum_Type()
)
trpzApUnconfOrphanApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanApSerialNum.setStatus("current")


class _TrpzApUnconfOrphanApModelName_Type(DisplayString):
    """Custom type trpzApUnconfOrphanApModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_TrpzApUnconfOrphanApModelName_Type.__name__ = "DisplayString"
_TrpzApUnconfOrphanApModelName_Object = MibTableColumn
trpzApUnconfOrphanApModelName = _TrpzApUnconfOrphanApModelName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 2),
    _TrpzApUnconfOrphanApModelName_Type()
)
trpzApUnconfOrphanApModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanApModelName.setStatus("current")
_TrpzApUnconfOrphanIpAddress_Type = IpAddress
_TrpzApUnconfOrphanIpAddress_Object = MibTableColumn
trpzApUnconfOrphanIpAddress = _TrpzApUnconfOrphanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 5),
    _TrpzApUnconfOrphanIpAddress_Type()
)
trpzApUnconfOrphanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanIpAddress.setStatus("current")
_TrpzApUnconfOrphanPhysPortNum_Type = TrpzPhysPortNumber
_TrpzApUnconfOrphanPhysPortNum_Object = MibTableColumn
trpzApUnconfOrphanPhysPortNum = _TrpzApUnconfOrphanPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 6),
    _TrpzApUnconfOrphanPhysPortNum_Type()
)
trpzApUnconfOrphanPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanPhysPortNum.setStatus("current")


class _TrpzApUnconfOrphanVLANName_Type(DisplayString):
    """Custom type trpzApUnconfOrphanVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApUnconfOrphanVLANName_Type.__name__ = "DisplayString"
_TrpzApUnconfOrphanVLANName_Object = MibTableColumn
trpzApUnconfOrphanVLANName = _TrpzApUnconfOrphanVLANName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 7),
    _TrpzApUnconfOrphanVLANName_Type()
)
trpzApUnconfOrphanVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanVLANName.setStatus("current")
_TrpzApUnconfOrphanReason_Type = TrpzApUnconfiguredOrphanReason
_TrpzApUnconfOrphanReason_Object = MibTableColumn
trpzApUnconfOrphanReason = _TrpzApUnconfOrphanReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 8),
    _TrpzApUnconfOrphanReason_Type()
)
trpzApUnconfOrphanReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanReason.setStatus("current")
_TrpzApUnconfConformance_ObjectIdentity = ObjectIdentity
trpzApUnconfConformance = _TrpzApUnconfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2)
)
_TrpzApUnconfCompliances_ObjectIdentity = ObjectIdentity
trpzApUnconfCompliances = _TrpzApUnconfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1)
)
_TrpzApUnconfGroups_ObjectIdentity = ObjectIdentity
trpzApUnconfGroups = _TrpzApUnconfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2)
)

# Managed Objects groups

trpzApUnconfOrphanBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2, 1)
)
trpzApUnconfOrphanBasicGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApModelName"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanIpAddress"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanPhysPortNum"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanVLANName"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanReason"))
)
if mibBuilder.loadTexts:
    trpzApUnconfOrphanBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzApUnconfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1, 1)
)
trpzApUnconfCompliance.setObjects(
    ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanBasicGroup")
)
if mibBuilder.loadTexts:
    trpzApUnconfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB",
    **{"TrpzApUnconfiguredOrphanReason": TrpzApUnconfiguredOrphanReason,
       "trpzApUnconfiguredMib": trpzApUnconfiguredMib,
       "trpzApUnconfMibObjects": trpzApUnconfMibObjects,
       "trpzApUnconfOrphanTable": trpzApUnconfOrphanTable,
       "trpzApUnconfOrphanEntry": trpzApUnconfOrphanEntry,
       "trpzApUnconfOrphanApSerialNum": trpzApUnconfOrphanApSerialNum,
       "trpzApUnconfOrphanApModelName": trpzApUnconfOrphanApModelName,
       "trpzApUnconfOrphanIpAddress": trpzApUnconfOrphanIpAddress,
       "trpzApUnconfOrphanPhysPortNum": trpzApUnconfOrphanPhysPortNum,
       "trpzApUnconfOrphanVLANName": trpzApUnconfOrphanVLANName,
       "trpzApUnconfOrphanReason": trpzApUnconfOrphanReason,
       "trpzApUnconfConformance": trpzApUnconfConformance,
       "trpzApUnconfCompliances": trpzApUnconfCompliances,
       "trpzApUnconfCompliance": trpzApUnconfCompliance,
       "trpzApUnconfGroups": trpzApUnconfGroups,
       "trpzApUnconfOrphanBasicGroup": trpzApUnconfOrphanBasicGroup}
)
