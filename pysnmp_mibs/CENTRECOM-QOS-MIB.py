# SNMP MIB module (CENTRECOM-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/CENTRECOM-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:32 2025
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

(extSwitchMIB,) = mibBuilder.importSymbols(
    "CENTRECOM-MIB",
    "extSwitchMIB")

(atiVlanIfIndex,) = mibBuilder.importSymbols(
    "CENTRECOM-VLAN-MIB",
    "atiVlanIfIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atiQos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtiQosCommon_ObjectIdentity = ObjectIdentity
atiQosCommon = _AtiQosCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1)
)


class _AtiQosMode_Type(Integer32):
    """Custom type atiQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_AtiQosMode_Type.__name__ = "Integer32"
_AtiQosMode_Object = MibScalar
atiQosMode = _AtiQosMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 4),
    _AtiQosMode_Type()
)
atiQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosMode.setStatus("mandatory")
_AtiQosUnconfigure_Type = TruthValue
_AtiQosUnconfigure_Object = MibScalar
atiQosUnconfigure = _AtiQosUnconfigure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 5),
    _AtiQosUnconfigure_Type()
)
atiQosUnconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosUnconfigure.setStatus("mandatory")
_AtiQosProfileTable_Object = MibTable
atiQosProfileTable = _AtiQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6)
)
if mibBuilder.loadTexts:
    atiQosProfileTable.setStatus("mandatory")
_AtiQosProfileEntry_Object = MibTableRow
atiQosProfileEntry = _AtiQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1)
)
atiQosProfileEntry.setIndexNames(
    (0, "CENTRECOM-QOS-MIB", "atiQosProfileIndex"),
)
if mibBuilder.loadTexts:
    atiQosProfileEntry.setStatus("mandatory")


class _AtiQosProfileIndex_Type(Integer32):
    """Custom type atiQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiQosProfileIndex_Type.__name__ = "Integer32"
_AtiQosProfileIndex_Object = MibTableColumn
atiQosProfileIndex = _AtiQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1, 1),
    _AtiQosProfileIndex_Type()
)
atiQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosProfileIndex.setStatus("mandatory")


class _AtiQosProfileName_Type(DisplayString):
    """Custom type atiQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AtiQosProfileName_Type.__name__ = "DisplayString"
_AtiQosProfileName_Object = MibTableColumn
atiQosProfileName = _AtiQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1, 2),
    _AtiQosProfileName_Type()
)
atiQosProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosProfileName.setStatus("mandatory")
_AtiQosProfileMinBw_Type = Integer32
_AtiQosProfileMinBw_Object = MibTableColumn
atiQosProfileMinBw = _AtiQosProfileMinBw_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1, 3),
    _AtiQosProfileMinBw_Type()
)
atiQosProfileMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosProfileMinBw.setStatus("mandatory")
_AtiQosProfileMaxBw_Type = Integer32
_AtiQosProfileMaxBw_Object = MibTableColumn
atiQosProfileMaxBw = _AtiQosProfileMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1, 4),
    _AtiQosProfileMaxBw_Type()
)
atiQosProfileMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosProfileMaxBw.setStatus("mandatory")


class _AtiQosProfilePriority_Type(Integer32):
    """Custom type atiQosProfilePriority based on Integer32"""
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
        *(("low", 1),
          ("normal", 2),
          ("medium", 3),
          ("high", 4))
    )


_AtiQosProfilePriority_Type.__name__ = "Integer32"
_AtiQosProfilePriority_Object = MibTableColumn
atiQosProfilePriority = _AtiQosProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1, 5),
    _AtiQosProfilePriority_Type()
)
atiQosProfilePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosProfilePriority.setStatus("mandatory")
_AtiQosProfileRowStatus_Type = RowStatus
_AtiQosProfileRowStatus_Object = MibTableColumn
atiQosProfileRowStatus = _AtiQosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 6, 1, 6),
    _AtiQosProfileRowStatus_Type()
)
atiQosProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosProfileRowStatus.setStatus("mandatory")
_AtiQosByVlanMappingTable_Object = MibTable
atiQosByVlanMappingTable = _AtiQosByVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 7)
)
if mibBuilder.loadTexts:
    atiQosByVlanMappingTable.setStatus("mandatory")
_AtiQosByVlanMappingEntry_Object = MibTableRow
atiQosByVlanMappingEntry = _AtiQosByVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 7, 1)
)
atiQosByVlanMappingEntry.setIndexNames(
    (0, "CENTRECOM-VLAN-MIB", "atiVlanIfIndex"),
)
if mibBuilder.loadTexts:
    atiQosByVlanMappingEntry.setStatus("mandatory")


class _AtiQosByVlanMappingQosProfileIndex_Type(Integer32):
    """Custom type atiQosByVlanMappingQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtiQosByVlanMappingQosProfileIndex_Type.__name__ = "Integer32"
_AtiQosByVlanMappingQosProfileIndex_Object = MibTableColumn
atiQosByVlanMappingQosProfileIndex = _AtiQosByVlanMappingQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 5, 1, 7, 1, 1),
    _AtiQosByVlanMappingQosProfileIndex_Type()
)
atiQosByVlanMappingQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiQosByVlanMappingQosProfileIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTRECOM-QOS-MIB",
    **{"atiQos": atiQos,
       "atiQosCommon": atiQosCommon,
       "atiQosMode": atiQosMode,
       "atiQosUnconfigure": atiQosUnconfigure,
       "atiQosProfileTable": atiQosProfileTable,
       "atiQosProfileEntry": atiQosProfileEntry,
       "atiQosProfileIndex": atiQosProfileIndex,
       "atiQosProfileName": atiQosProfileName,
       "atiQosProfileMinBw": atiQosProfileMinBw,
       "atiQosProfileMaxBw": atiQosProfileMaxBw,
       "atiQosProfilePriority": atiQosProfilePriority,
       "atiQosProfileRowStatus": atiQosProfileRowStatus,
       "atiQosByVlanMappingTable": atiQosByVlanMappingTable,
       "atiQosByVlanMappingEntry": atiQosByVlanMappingEntry,
       "atiQosByVlanMappingQosProfileIndex": atiQosByVlanMappingQosProfileIndex}
)
