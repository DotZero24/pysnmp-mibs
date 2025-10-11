# SNMP MIB module (RFC1354-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/RFC1354-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:20:41 2025
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

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpForward_ObjectIdentity = ObjectIdentity
ipForward = _IpForward_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24)
)
_IpForwardNumber_Type = Gauge32
_IpForwardNumber_Object = MibScalar
ipForwardNumber = _IpForwardNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 1),
    _IpForwardNumber_Type()
)
ipForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardNumber.setStatus("mandatory")
_IpForwardTable_Object = MibTable
ipForwardTable = _IpForwardTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2)
)
if mibBuilder.loadTexts:
    ipForwardTable.setStatus("mandatory")
_IpForwardEntry_Object = MibTableRow
ipForwardEntry = _IpForwardEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1)
)
ipForwardEntry.setIndexNames(
    (0, "RFC1354-MIB", "ipForwardDest"),
    (0, "RFC1354-MIB", "ipForwardProto"),
    (0, "RFC1354-MIB", "ipForwardPolicy"),
    (0, "RFC1354-MIB", "ipForwardNextHop"),
)
if mibBuilder.loadTexts:
    ipForwardEntry.setStatus("mandatory")
_IpForwardDest_Type = IpAddress
_IpForwardDest_Object = MibTableColumn
ipForwardDest = _IpForwardDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 1),
    _IpForwardDest_Type()
)
ipForwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardDest.setStatus("mandatory")


class _IpForwardMask_Type(IpAddress):
    """Custom type ipForwardMask based on IpAddress"""
    defaultHexValue = "00000000"


_IpForwardMask_Type.__name__ = "IpAddress"
_IpForwardMask_Object = MibTableColumn
ipForwardMask = _IpForwardMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 2),
    _IpForwardMask_Type()
)
ipForwardMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardMask.setStatus("mandatory")
_IpForwardPolicy_Type = Integer32
_IpForwardPolicy_Object = MibTableColumn
ipForwardPolicy = _IpForwardPolicy_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 3),
    _IpForwardPolicy_Type()
)
ipForwardPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardPolicy.setStatus("mandatory")
_IpForwardNextHop_Type = IpAddress
_IpForwardNextHop_Object = MibTableColumn
ipForwardNextHop = _IpForwardNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 4),
    _IpForwardNextHop_Type()
)
ipForwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardNextHop.setStatus("mandatory")


class _IpForwardIfIndex_Type(Integer32):
    """Custom type ipForwardIfIndex based on Integer32"""
    defaultValue = 0


_IpForwardIfIndex_Type.__name__ = "Integer32"
_IpForwardIfIndex_Object = MibTableColumn
ipForwardIfIndex = _IpForwardIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 5),
    _IpForwardIfIndex_Type()
)
ipForwardIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardIfIndex.setStatus("mandatory")


class _IpForwardType_Type(Integer32):
    """Custom type ipForwardType based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("invalid", 2),
          ("local", 3),
          ("remote", 4))
    )


_IpForwardType_Type.__name__ = "Integer32"
_IpForwardType_Object = MibTableColumn
ipForwardType = _IpForwardType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 6),
    _IpForwardType_Type()
)
ipForwardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardType.setStatus("mandatory")


class _IpForwardProto_Type(Integer32):
    """Custom type ipForwardProto based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("is-is", 9),
          ("es-is", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15))
    )


_IpForwardProto_Type.__name__ = "Integer32"
_IpForwardProto_Object = MibTableColumn
ipForwardProto = _IpForwardProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 7),
    _IpForwardProto_Type()
)
ipForwardProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardProto.setStatus("mandatory")


class _IpForwardAge_Type(Integer32):
    """Custom type ipForwardAge based on Integer32"""
    defaultValue = 0


_IpForwardAge_Type.__name__ = "Integer32"
_IpForwardAge_Object = MibTableColumn
ipForwardAge = _IpForwardAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 8),
    _IpForwardAge_Type()
)
ipForwardAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardAge.setStatus("mandatory")
_IpForwardInfo_Type = ObjectIdentifier
_IpForwardInfo_Object = MibTableColumn
ipForwardInfo = _IpForwardInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 9),
    _IpForwardInfo_Type()
)
ipForwardInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardInfo.setStatus("mandatory")


class _IpForwardNextHopAS_Type(Integer32):
    """Custom type ipForwardNextHopAS based on Integer32"""
    defaultValue = 0


_IpForwardNextHopAS_Type.__name__ = "Integer32"
_IpForwardNextHopAS_Object = MibTableColumn
ipForwardNextHopAS = _IpForwardNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 10),
    _IpForwardNextHopAS_Type()
)
ipForwardNextHopAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardNextHopAS.setStatus("mandatory")


class _IpForwardMetric1_Type(Integer32):
    """Custom type ipForwardMetric1 based on Integer32"""
    defaultValue = -1


_IpForwardMetric1_Type.__name__ = "Integer32"
_IpForwardMetric1_Object = MibTableColumn
ipForwardMetric1 = _IpForwardMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 11),
    _IpForwardMetric1_Type()
)
ipForwardMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardMetric1.setStatus("mandatory")


class _IpForwardMetric2_Type(Integer32):
    """Custom type ipForwardMetric2 based on Integer32"""
    defaultValue = -1


_IpForwardMetric2_Type.__name__ = "Integer32"
_IpForwardMetric2_Object = MibTableColumn
ipForwardMetric2 = _IpForwardMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 12),
    _IpForwardMetric2_Type()
)
ipForwardMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardMetric2.setStatus("mandatory")


class _IpForwardMetric3_Type(Integer32):
    """Custom type ipForwardMetric3 based on Integer32"""
    defaultValue = -1


_IpForwardMetric3_Type.__name__ = "Integer32"
_IpForwardMetric3_Object = MibTableColumn
ipForwardMetric3 = _IpForwardMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 13),
    _IpForwardMetric3_Type()
)
ipForwardMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardMetric3.setStatus("mandatory")


class _IpForwardMetric4_Type(Integer32):
    """Custom type ipForwardMetric4 based on Integer32"""
    defaultValue = -1


_IpForwardMetric4_Type.__name__ = "Integer32"
_IpForwardMetric4_Object = MibTableColumn
ipForwardMetric4 = _IpForwardMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 14),
    _IpForwardMetric4_Type()
)
ipForwardMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardMetric4.setStatus("mandatory")


class _IpForwardMetric5_Type(Integer32):
    """Custom type ipForwardMetric5 based on Integer32"""
    defaultValue = -1


_IpForwardMetric5_Type.__name__ = "Integer32"
_IpForwardMetric5_Object = MibTableColumn
ipForwardMetric5 = _IpForwardMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 15),
    _IpForwardMetric5_Type()
)
ipForwardMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardMetric5.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1354-MIB",
    **{"ipForward": ipForward,
       "ipForwardNumber": ipForwardNumber,
       "ipForwardTable": ipForwardTable,
       "ipForwardEntry": ipForwardEntry,
       "ipForwardDest": ipForwardDest,
       "ipForwardMask": ipForwardMask,
       "ipForwardPolicy": ipForwardPolicy,
       "ipForwardNextHop": ipForwardNextHop,
       "ipForwardIfIndex": ipForwardIfIndex,
       "ipForwardType": ipForwardType,
       "ipForwardProto": ipForwardProto,
       "ipForwardAge": ipForwardAge,
       "ipForwardInfo": ipForwardInfo,
       "ipForwardNextHopAS": ipForwardNextHopAS,
       "ipForwardMetric1": ipForwardMetric1,
       "ipForwardMetric2": ipForwardMetric2,
       "ipForwardMetric3": ipForwardMetric3,
       "ipForwardMetric4": ipForwardMetric4,
       "ipForwardMetric5": ipForwardMetric5}
)
