# SNMP MIB module (ARICENT-SNMPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-SNMPv2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:27 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

futuresnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 50)
)
if mibBuilder.loadTexts:
    futuresnmp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EntryStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )



# MIB Managed Objects in the order of their OIDs



class _SnmpListenPort_Type(Integer32):
    """Custom type snmpListenPort based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpListenPort_Type.__name__ = "Integer32"
_SnmpListenPort_Object = MibScalar
snmpListenPort = _SnmpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 1),
    _SnmpListenPort_Type()
)
snmpListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpListenPort.setStatus("current")


class _SnmpListenTrapPort_Type(Integer32):
    """Custom type snmpListenTrapPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpListenTrapPort_Type.__name__ = "Integer32"
_SnmpListenTrapPort_Object = MibScalar
snmpListenTrapPort = _SnmpListenTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 2),
    _SnmpListenTrapPort_Type()
)
snmpListenTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpListenTrapPort.setStatus("current")
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "ARICENT-SNMPv2-MIB", "snmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")


class _SnmpCommunityIndex_Type(Integer32):
    """Custom type snmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SnmpCommunityIndex_Type.__name__ = "Integer32"
_SnmpCommunityIndex_Object = MibTableColumn
snmpCommunityIndex = _SnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3, 1, 1),
    _SnmpCommunityIndex_Type()
)
snmpCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpCommunityIndex.setStatus("current")
_SnmpCommunityName_Type = DisplayString
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3, 1, 2),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")


class _SnmpCommunityPrivilege_Type(Integer32):
    """Custom type snmpCommunityPrivilege based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_SnmpCommunityPrivilege_Type.__name__ = "Integer32"
_SnmpCommunityPrivilege_Object = MibTableColumn
snmpCommunityPrivilege = _SnmpCommunityPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3, 1, 3),
    _SnmpCommunityPrivilege_Type()
)
snmpCommunityPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityPrivilege.setStatus("current")


class _SnmpCommunityIpAddr_Type(IpAddress):
    """Custom type snmpCommunityIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_SnmpCommunityIpAddr_Type.__name__ = "IpAddress"
_SnmpCommunityIpAddr_Object = MibTableColumn
snmpCommunityIpAddr = _SnmpCommunityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3, 1, 4),
    _SnmpCommunityIpAddr_Type()
)
snmpCommunityIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityIpAddr.setStatus("current")
_SnmpStatus_Type = EntryStatus
_SnmpStatus_Object = MibTableColumn
snmpStatus = _SnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 3, 1, 5),
    _SnmpStatus_Type()
)
snmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpStatus.setStatus("current")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("current")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "ARICENT-SNMPv2-MIB", "snmpTrapIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("current")


class _SnmpTrapIndex_Type(Integer32):
    """Custom type snmpTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SnmpTrapIndex_Type.__name__ = "Integer32"
_SnmpTrapIndex_Object = MibTableColumn
snmpTrapIndex = _SnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4, 1, 1),
    _SnmpTrapIndex_Type()
)
snmpTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapIndex.setStatus("current")


class _SnmpTrapCommunityName_Type(DisplayString):
    """Custom type snmpTrapCommunityName based on DisplayString"""
    defaultValue = OctetString("PUBLIC")


_SnmpTrapCommunityName_Type.__name__ = "DisplayString"
_SnmpTrapCommunityName_Object = MibTableColumn
snmpTrapCommunityName = _SnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4, 1, 2),
    _SnmpTrapCommunityName_Type()
)
snmpTrapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunityName.setStatus("current")
_SnmpTrapIpAddr_Type = IpAddress
_SnmpTrapIpAddr_Object = MibTableColumn
snmpTrapIpAddr = _SnmpTrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4, 1, 3),
    _SnmpTrapIpAddr_Type()
)
snmpTrapIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapIpAddr.setStatus("current")


class _SnmpTrapMgrType_Type(Integer32):
    """Custom type snmpTrapMgrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2", 1),
          ("v1v2", 2))
    )


_SnmpTrapMgrType_Type.__name__ = "Integer32"
_SnmpTrapMgrType_Object = MibTableColumn
snmpTrapMgrType = _SnmpTrapMgrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4, 1, 4),
    _SnmpTrapMgrType_Type()
)
snmpTrapMgrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapMgrType.setStatus("current")
_SnmpTrapStatus_Type = EntryStatus
_SnmpTrapStatus_Object = MibTableColumn
snmpTrapStatus = _SnmpTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 50, 4, 1, 5),
    _SnmpTrapStatus_Type()
)
snmpTrapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-SNMPv2-MIB",
    **{"EntryStatus": EntryStatus,
       "futuresnmp": futuresnmp,
       "snmpListenPort": snmpListenPort,
       "snmpListenTrapPort": snmpListenTrapPort,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityIndex": snmpCommunityIndex,
       "snmpCommunityName": snmpCommunityName,
       "snmpCommunityPrivilege": snmpCommunityPrivilege,
       "snmpCommunityIpAddr": snmpCommunityIpAddr,
       "snmpStatus": snmpStatus,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapIndex": snmpTrapIndex,
       "snmpTrapCommunityName": snmpTrapCommunityName,
       "snmpTrapIpAddr": snmpTrapIpAddr,
       "snmpTrapMgrType": snmpTrapMgrType,
       "snmpTrapStatus": snmpTrapStatus}
)
