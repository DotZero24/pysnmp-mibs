# SNMP MIB module (RADLAN-Redistribute) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/RADLAN-Redistribute
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:55 2025
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

(ipSpec,) = mibBuilder.importSymbols(
    "RADLAN-IP",
    "ipSpec")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class RlRedistSrcProtocol(TextualConvention, Integer32):
    status = "current"
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
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("rlRedistProtocolConnected", 1),
          ("rlRedistProtocolStatic", 2),
          ("rlRedistProtocolRip", 3),
          ("rlRedistProtocolOspfv2", 4),
          ("rlRedistProtocolOspfv3", 5),
          ("rlRedistProtocolBgp", 6),
          ("rlRedistProtocolEigrp", 7),
          ("rlRedistProtocolIsIs", 8),
          ("rlRedistProtocolMobile", 9),
          ("rlRedistProtocolAll", 10),
          ("rlRedistProtocolIsIsL1", 101),
          ("rlRedistProtocolIsIsL2", 102))
    )



class RlRedistDstProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("rlRedistProtocolRip", 3),
          ("rlRedistProtocolOspfv2", 4),
          ("rlRedistProtocolOspfv3", 5),
          ("rlRedistProtocolBgp", 6),
          ("rlRedistProtocolEigrp", 7),
          ("rlRedistProtocolIsIs", 8),
          ("rlRedistProtocolMobile", 9),
          ("rlRedistProtocolBgpMulticast", 100),
          ("rlRedistProtocolIsIsL1", 101),
          ("rlRedistProtocolIsIsL2", 102))
    )



class RlRedistMatchType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("rlRedistMatchTypeNone", 0),
          ("rlRedistMatchTypeInternal", 1),
          ("rlRedistMatchTypeExternalOne", 2),
          ("rlRedistMatchTypeExternalTwo", 3),
          ("rlRedistMatchTypeIsIsInternal", 100),
          ("rlRedistMatchTypeIsIsExternal", 101))
    )



class RlRedistMetricType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("rlRedistMetricTypeNone", 0),
          ("rlRedistMetricTypeExternalOne", 1),
          ("rlRedistMetricTypeExternalTwo", 2),
          ("rlRedistMetricTypeIsIsInternal", 100),
          ("rlRedistMetricTypeIsIsExternal", 101))
    )



# MIB Managed Objects in the order of their OIDs

_RlRedistribute_ObjectIdentity = ObjectIdentity
rlRedistribute = _RlRedistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 27)
)
_RlRedistTable_Object = MibTable
rlRedistTable = _RlRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1)
)
if mibBuilder.loadTexts:
    rlRedistTable.setStatus("current")
_RlRedistEntry_Object = MibTableRow
rlRedistEntry = _RlRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1)
)
rlRedistEntry.setIndexNames(
    (0, "RADLAN-Redistribute", "rlRedistDstProtocol"),
    (0, "RADLAN-Redistribute", "rlRedistSrcProtocol"),
    (0, "RADLAN-Redistribute", "rlRedistDstProcessId"),
    (0, "RADLAN-Redistribute", "rlRedistSrcProcessId"),
    (0, "RADLAN-Redistribute", "rlRedistMatchType"),
    (0, "RADLAN-Redistribute", "rlRedistRoutMapName"),
)
if mibBuilder.loadTexts:
    rlRedistEntry.setStatus("current")
_RlRedistDstProtocol_Type = RlRedistDstProtocol
_RlRedistDstProtocol_Object = MibTableColumn
rlRedistDstProtocol = _RlRedistDstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 1),
    _RlRedistDstProtocol_Type()
)
rlRedistDstProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRedistDstProtocol.setStatus("current")
_RlRedistSrcProtocol_Type = RlRedistSrcProtocol
_RlRedistSrcProtocol_Object = MibTableColumn
rlRedistSrcProtocol = _RlRedistSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 2),
    _RlRedistSrcProtocol_Type()
)
rlRedistSrcProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRedistSrcProtocol.setStatus("current")


class _RlRedistDstProcessId_Type(Integer32):
    """Custom type rlRedistDstProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRedistDstProcessId_Type.__name__ = "Integer32"
_RlRedistDstProcessId_Object = MibTableColumn
rlRedistDstProcessId = _RlRedistDstProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 3),
    _RlRedistDstProcessId_Type()
)
rlRedistDstProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRedistDstProcessId.setStatus("current")


class _RlRedistSrcProcessId_Type(Integer32):
    """Custom type rlRedistSrcProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRedistSrcProcessId_Type.__name__ = "Integer32"
_RlRedistSrcProcessId_Object = MibTableColumn
rlRedistSrcProcessId = _RlRedistSrcProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 4),
    _RlRedistSrcProcessId_Type()
)
rlRedistSrcProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRedistSrcProcessId.setStatus("current")
_RlRedistMatchType_Type = RlRedistMatchType
_RlRedistMatchType_Object = MibTableColumn
rlRedistMatchType = _RlRedistMatchType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 5),
    _RlRedistMatchType_Type()
)
rlRedistMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRedistMatchType.setStatus("current")


class _RlRedistRoutMapName_Type(DisplayString):
    """Custom type rlRedistRoutMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRedistRoutMapName_Type.__name__ = "DisplayString"
_RlRedistRoutMapName_Object = MibTableColumn
rlRedistRoutMapName = _RlRedistRoutMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 6),
    _RlRedistRoutMapName_Type()
)
rlRedistRoutMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRedistRoutMapName.setStatus("current")


class _RlRedistAsNumber_Type(Integer32):
    """Custom type rlRedistAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRedistAsNumber_Type.__name__ = "Integer32"
_RlRedistAsNumber_Object = MibTableColumn
rlRedistAsNumber = _RlRedistAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 7),
    _RlRedistAsNumber_Type()
)
rlRedistAsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistAsNumber.setStatus("current")


class _RlRedistMetricTransparent_Type(TruthValue):
    """Custom type rlRedistMetricTransparent based on TruthValue"""
    defaultValue = 1


_RlRedistMetricTransparent_Type.__name__ = "TruthValue"
_RlRedistMetricTransparent_Object = MibTableColumn
rlRedistMetricTransparent = _RlRedistMetricTransparent_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 8),
    _RlRedistMetricTransparent_Type()
)
rlRedistMetricTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistMetricTransparent.setStatus("current")


class _RlRedistMetricValue_Type(Integer32):
    """Custom type rlRedistMetricValue based on Integer32"""
    defaultValue = 0


_RlRedistMetricValue_Type.__name__ = "Integer32"
_RlRedistMetricValue_Object = MibTableColumn
rlRedistMetricValue = _RlRedistMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 9),
    _RlRedistMetricValue_Type()
)
rlRedistMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistMetricValue.setStatus("current")
_RlRedistMetricType_Type = RlRedistMetricType
_RlRedistMetricType_Object = MibTableColumn
rlRedistMetricType = _RlRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 10),
    _RlRedistMetricType_Type()
)
rlRedistMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistMetricType.setStatus("current")


class _RlRedistSubnets_Type(TruthValue):
    """Custom type rlRedistSubnets based on TruthValue"""
    defaultValue = 2


_RlRedistSubnets_Type.__name__ = "TruthValue"
_RlRedistSubnets_Object = MibTableColumn
rlRedistSubnets = _RlRedistSubnets_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 11),
    _RlRedistSubnets_Type()
)
rlRedistSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistSubnets.setStatus("current")


class _RlRedistOnlyNSSA_Type(TruthValue):
    """Custom type rlRedistOnlyNSSA based on TruthValue"""
    defaultValue = 2


_RlRedistOnlyNSSA_Type.__name__ = "TruthValue"
_RlRedistOnlyNSSA_Object = MibTableColumn
rlRedistOnlyNSSA = _RlRedistOnlyNSSA_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 12),
    _RlRedistOnlyNSSA_Type()
)
rlRedistOnlyNSSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistOnlyNSSA.setStatus("current")
_RlRedistRowStatus_Type = RowStatus
_RlRedistRowStatus_Object = MibTableColumn
rlRedistRowStatus = _RlRedistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 13),
    _RlRedistRowStatus_Type()
)
rlRedistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlRedistRowStatus.setStatus("current")
_RlRedistFilterListName_Type = DisplayString
_RlRedistFilterListName_Object = MibTableColumn
rlRedistFilterListName = _RlRedistFilterListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 14),
    _RlRedistFilterListName_Type()
)
rlRedistFilterListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRedistFilterListName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-Redistribute",
    **{"RlRedistSrcProtocol": RlRedistSrcProtocol,
       "RlRedistDstProtocol": RlRedistDstProtocol,
       "RlRedistMatchType": RlRedistMatchType,
       "RlRedistMetricType": RlRedistMetricType,
       "rlRedistribute": rlRedistribute,
       "rlRedistTable": rlRedistTable,
       "rlRedistEntry": rlRedistEntry,
       "rlRedistDstProtocol": rlRedistDstProtocol,
       "rlRedistSrcProtocol": rlRedistSrcProtocol,
       "rlRedistDstProcessId": rlRedistDstProcessId,
       "rlRedistSrcProcessId": rlRedistSrcProcessId,
       "rlRedistMatchType": rlRedistMatchType,
       "rlRedistRoutMapName": rlRedistRoutMapName,
       "rlRedistAsNumber": rlRedistAsNumber,
       "rlRedistMetricTransparent": rlRedistMetricTransparent,
       "rlRedistMetricValue": rlRedistMetricValue,
       "rlRedistMetricType": rlRedistMetricType,
       "rlRedistSubnets": rlRedistSubnets,
       "rlRedistOnlyNSSA": rlRedistOnlyNSSA,
       "rlRedistRowStatus": rlRedistRowStatus,
       "rlRedistFilterListName": rlRedistFilterListName}
)
