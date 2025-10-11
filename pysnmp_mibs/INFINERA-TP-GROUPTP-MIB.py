# SNMP MIB module (INFINERA-TP-GROUPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-GROUPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:06 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatTenths,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnServiceType")

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


# MODULE-IDENTITY

groupTpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    groupTpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GroupTpTable_Object = MibTable
groupTpTable = _GroupTpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    groupTpTable.setStatus("current")
_GroupTpEntry_Object = MibTableRow
groupTpEntry = _GroupTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1)
)
groupTpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    groupTpEntry.setStatus("current")


class _GroupTpCfgProtSt_Type(Integer32):
    """Custom type groupTpCfgProtSt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("wrk", 2),
          ("prot", 3),
          ("relb", 4),
          ("pu", 5))
    )


_GroupTpCfgProtSt_Type.__name__ = "Integer32"
_GroupTpCfgProtSt_Object = MibTableColumn
groupTpCfgProtSt = _GroupTpCfgProtSt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 1),
    _GroupTpCfgProtSt_Type()
)
groupTpCfgProtSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpCfgProtSt.setStatus("current")


class _GroupTpProtMod_Type(Integer32):
    """Custom type groupTpProtMod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dtDSNCP", 2),
          ("stDSNCP", 3))
    )


_GroupTpProtMod_Type.__name__ = "Integer32"
_GroupTpProtMod_Object = MibTableColumn
groupTpProtMod = _GroupTpProtMod_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 2),
    _GroupTpProtMod_Type()
)
groupTpProtMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpProtMod.setStatus("current")


class _GroupTpSwReason_Type(Integer32):
    """Custom type groupTpSwReason based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("mSwP", 1),
          ("mSwW", 2),
          ("wLck", 3),
          ("pLck", 4),
          ("auto", 5),
          ("none", 6),
          ("revert", 7),
          ("admLck", 8),
          ("unProv", 9),
          ("eqFlt", 10),
          ("liFlt", 11),
          ("liSF", 12),
          ("clRxFlt", 13),
          ("clTxFlt", 14),
          ("sysLof", 15))
    )


_GroupTpSwReason_Type.__name__ = "Integer32"
_GroupTpSwReason_Object = MibTableColumn
groupTpSwReason = _GroupTpSwReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 3),
    _GroupTpSwReason_Type()
)
groupTpSwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpSwReason.setStatus("current")


class _GroupTpGtpType_Type(Integer32):
    """Custom type groupTpGtpType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trib", 1),
          ("line", 2),
          ("hybrid", 3))
    )


_GroupTpGtpType_Type.__name__ = "Integer32"
_GroupTpGtpType_Object = MibTableColumn
groupTpGtpType = _GroupTpGtpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 4),
    _GroupTpGtpType_Type()
)
groupTpGtpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    groupTpGtpType.setStatus("current")
_GroupTpDtpList_Type = DisplayString
_GroupTpDtpList_Object = MibTableColumn
groupTpDtpList = _GroupTpDtpList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 5),
    _GroupTpDtpList_Type()
)
groupTpDtpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    groupTpDtpList.setStatus("current")


class _GroupTpCrossConnectType_Type(Integer32):
    """Custom type groupTpCrossConnectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unidirectionFrom", 2),
          ("unidirectionTo", 3),
          ("unidirectionToAndFrom", 4),
          ("bidirection", 5),
          ("bidirectionUnidirectionFrom", 6),
          ("bidirectionUnidirectionTo", 7),
          ("bidirectionUnidirectionToAndFrom", 8))
    )


_GroupTpCrossConnectType_Type.__name__ = "Integer32"
_GroupTpCrossConnectType_Object = MibTableColumn
groupTpCrossConnectType = _GroupTpCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 6),
    _GroupTpCrossConnectType_Type()
)
groupTpCrossConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpCrossConnectType.setStatus("current")


class _GroupTpPmHistStatsEnable_Type(Integer32):
    """Custom type groupTpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_GroupTpPmHistStatsEnable_Type.__name__ = "Integer32"
_GroupTpPmHistStatsEnable_Object = MibTableColumn
groupTpPmHistStatsEnable = _GroupTpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 7),
    _GroupTpPmHistStatsEnable_Type()
)
groupTpPmHistStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    groupTpPmHistStatsEnable.setStatus("current")


class _GroupTpConfigPayload_Type(InfnServiceType):
    """Custom type groupTpConfigPayload based on InfnServiceType"""
    defaultValue = 1


_GroupTpConfigPayload_Type.__name__ = "InfnServiceType"
_GroupTpConfigPayload_Object = MibTableColumn
groupTpConfigPayload = _GroupTpConfigPayload_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 8),
    _GroupTpConfigPayload_Type()
)
groupTpConfigPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpConfigPayload.setStatus("current")
_GroupTpSupportingCircuitIdList_Type = DisplayString
_GroupTpSupportingCircuitIdList_Object = MibTableColumn
groupTpSupportingCircuitIdList = _GroupTpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 9),
    _GroupTpSupportingCircuitIdList_Type()
)
groupTpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpSupportingCircuitIdList.setStatus("current")


class _GroupTpServiceAvailability_Type(Integer32):
    """Custom type groupTpServiceAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_GroupTpServiceAvailability_Type.__name__ = "Integer32"
_GroupTpServiceAvailability_Object = MibTableColumn
groupTpServiceAvailability = _GroupTpServiceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 1, 1, 10),
    _GroupTpServiceAvailability_Type()
)
groupTpServiceAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupTpServiceAvailability.setStatus("current")
_GroupTpConformance_ObjectIdentity = ObjectIdentity
groupTpConformance = _GroupTpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 3)
)
_GroupTpCompliances_ObjectIdentity = ObjectIdentity
groupTpCompliances = _GroupTpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 3, 1)
)
_GroupTpGroups_ObjectIdentity = ObjectIdentity
groupTpGroups = _GroupTpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 3, 2)
)

# Managed Objects groups

groupTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 3, 2, 1)
)
groupTpGroup.setObjects(
      *(("INFINERA-TP-GROUPTP-MIB", "groupTpCfgProtSt"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpProtMod"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpSwReason"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpGtpType"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpDtpList"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpCrossConnectType"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpPmHistStatsEnable"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpConfigPayload"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpSupportingCircuitIdList"),
        ("INFINERA-TP-GROUPTP-MIB", "groupTpServiceAvailability"))
)
if mibBuilder.loadTexts:
    groupTpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

groupTpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 10, 3, 1, 1)
)
groupTpCompliance.setObjects(
    ("INFINERA-TP-GROUPTP-MIB", "groupTpGroup")
)
if mibBuilder.loadTexts:
    groupTpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-GROUPTP-MIB",
    **{"groupTpMIB": groupTpMIB,
       "groupTpTable": groupTpTable,
       "groupTpEntry": groupTpEntry,
       "groupTpCfgProtSt": groupTpCfgProtSt,
       "groupTpProtMod": groupTpProtMod,
       "groupTpSwReason": groupTpSwReason,
       "groupTpGtpType": groupTpGtpType,
       "groupTpDtpList": groupTpDtpList,
       "groupTpCrossConnectType": groupTpCrossConnectType,
       "groupTpPmHistStatsEnable": groupTpPmHistStatsEnable,
       "groupTpConfigPayload": groupTpConfigPayload,
       "groupTpSupportingCircuitIdList": groupTpSupportingCircuitIdList,
       "groupTpServiceAvailability": groupTpServiceAvailability,
       "groupTpConformance": groupTpConformance,
       "groupTpCompliances": groupTpCompliances,
       "groupTpCompliance": groupTpCompliance,
       "groupTpGroups": groupTpGroups,
       "groupTpGroup": groupTpGroup}
)
