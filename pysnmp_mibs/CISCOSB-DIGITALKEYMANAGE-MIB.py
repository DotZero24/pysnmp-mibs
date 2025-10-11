# SNMP MIB module (CISCOSB-DIGITALKEYMANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ciscosb/CISCOSB-DIGITALKEYMANAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:12 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDigitalKeyManage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86)
)
if mibBuilder.loadTexts:
    rlDigitalKeyManage.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlKeyChainKeyAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simple-password", 1),
          ("md5", 2),
          ("hmac-sha-1", 3),
          ("hmac-sha-256", 4),
          ("hmac-sha-384", 5),
          ("hmac-sha-512", 6))
    )



# MIB Managed Objects in the order of their OIDs

_RlMD5KeyChainTable_Object = MibTable
rlMD5KeyChainTable = _RlMD5KeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1)
)
if mibBuilder.loadTexts:
    rlMD5KeyChainTable.setStatus("current")
_RlMD5KeyChainEntry_Object = MibTableRow
rlMD5KeyChainEntry = _RlMD5KeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1)
)
rlMD5KeyChainEntry.setIndexNames(
    (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlMD5KeyChainName"),
    (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlMD5KeyChainKeyId"),
)
if mibBuilder.loadTexts:
    rlMD5KeyChainEntry.setStatus("current")
_RlMD5KeyChainName_Type = DisplayString
_RlMD5KeyChainName_Object = MibTableColumn
rlMD5KeyChainName = _RlMD5KeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 1),
    _RlMD5KeyChainName_Type()
)
rlMD5KeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainName.setStatus("current")


class _RlMD5KeyChainKeyId_Type(Integer32):
    """Custom type rlMD5KeyChainKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlMD5KeyChainKeyId_Type.__name__ = "Integer32"
_RlMD5KeyChainKeyId_Object = MibTableColumn
rlMD5KeyChainKeyId = _RlMD5KeyChainKeyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 2),
    _RlMD5KeyChainKeyId_Type()
)
rlMD5KeyChainKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyId.setStatus("current")


class _RlMD5KeyChainKey_Type(DisplayString):
    """Custom type rlMD5KeyChainKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlMD5KeyChainKey_Type.__name__ = "DisplayString"
_RlMD5KeyChainKey_Object = MibTableColumn
rlMD5KeyChainKey = _RlMD5KeyChainKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 3),
    _RlMD5KeyChainKey_Type()
)
rlMD5KeyChainKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKey.setStatus("current")
_RlMD5KeyChainKeyStartAccept_Type = DateAndTime
_RlMD5KeyChainKeyStartAccept_Object = MibTableColumn
rlMD5KeyChainKeyStartAccept = _RlMD5KeyChainKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 4),
    _RlMD5KeyChainKeyStartAccept_Type()
)
rlMD5KeyChainKeyStartAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStartAccept.setStatus("current")
_RlMD5KeyChainKeyStartGenerate_Type = DateAndTime
_RlMD5KeyChainKeyStartGenerate_Object = MibTableColumn
rlMD5KeyChainKeyStartGenerate = _RlMD5KeyChainKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 5),
    _RlMD5KeyChainKeyStartGenerate_Type()
)
rlMD5KeyChainKeyStartGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStartGenerate.setStatus("current")
_RlMD5KeyChainKeyStopGenerate_Type = DateAndTime
_RlMD5KeyChainKeyStopGenerate_Object = MibTableColumn
rlMD5KeyChainKeyStopGenerate = _RlMD5KeyChainKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 6),
    _RlMD5KeyChainKeyStopGenerate_Type()
)
rlMD5KeyChainKeyStopGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStopGenerate.setStatus("current")
_RlMD5KeyChainKeyStopAccept_Type = DateAndTime
_RlMD5KeyChainKeyStopAccept_Object = MibTableColumn
rlMD5KeyChainKeyStopAccept = _RlMD5KeyChainKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 7),
    _RlMD5KeyChainKeyStopAccept_Type()
)
rlMD5KeyChainKeyStopAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStopAccept.setStatus("current")


class _RlMD5KeyChainKeyValidForAccept_Type(TruthValue):
    """Custom type rlMD5KeyChainKeyValidForAccept based on TruthValue"""
    defaultValue = 2


_RlMD5KeyChainKeyValidForAccept_Type.__name__ = "TruthValue"
_RlMD5KeyChainKeyValidForAccept_Object = MibTableColumn
rlMD5KeyChainKeyValidForAccept = _RlMD5KeyChainKeyValidForAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 8),
    _RlMD5KeyChainKeyValidForAccept_Type()
)
rlMD5KeyChainKeyValidForAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyValidForAccept.setStatus("current")


class _RlMD5KeyChainKeyValidForGenerate_Type(TruthValue):
    """Custom type rlMD5KeyChainKeyValidForGenerate based on TruthValue"""
    defaultValue = 2


_RlMD5KeyChainKeyValidForGenerate_Type.__name__ = "TruthValue"
_RlMD5KeyChainKeyValidForGenerate_Object = MibTableColumn
rlMD5KeyChainKeyValidForGenerate = _RlMD5KeyChainKeyValidForGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 9),
    _RlMD5KeyChainKeyValidForGenerate_Type()
)
rlMD5KeyChainKeyValidForGenerate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyValidForGenerate.setStatus("current")
_RlMD5KeyChainRowStatus_Type = RowStatus
_RlMD5KeyChainRowStatus_Object = MibTableColumn
rlMD5KeyChainRowStatus = _RlMD5KeyChainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 10),
    _RlMD5KeyChainRowStatus_Type()
)
rlMD5KeyChainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainRowStatus.setStatus("current")
_RlKeyChainMngTable_Object = MibTable
rlKeyChainMngTable = _RlKeyChainMngTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2)
)
if mibBuilder.loadTexts:
    rlKeyChainMngTable.setStatus("current")
_RlKeyChainMngEntry_Object = MibTableRow
rlKeyChainMngEntry = _RlKeyChainMngEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1)
)
rlKeyChainMngEntry.setIndexNames(
    (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlKeyChainMngName"),
    (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlKeyChainMngKeyId"),
)
if mibBuilder.loadTexts:
    rlKeyChainMngEntry.setStatus("current")
_RlKeyChainMngName_Type = DisplayString
_RlKeyChainMngName_Object = MibTableColumn
rlKeyChainMngName = _RlKeyChainMngName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 1),
    _RlKeyChainMngName_Type()
)
rlKeyChainMngName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlKeyChainMngName.setStatus("current")


class _RlKeyChainMngKeyId_Type(Integer32):
    """Custom type rlKeyChainMngKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlKeyChainMngKeyId_Type.__name__ = "Integer32"
_RlKeyChainMngKeyId_Object = MibTableColumn
rlKeyChainMngKeyId = _RlKeyChainMngKeyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 2),
    _RlKeyChainMngKeyId_Type()
)
rlKeyChainMngKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyId.setStatus("current")


class _RlKeyChainMngKeyAuthType_Type(RlKeyChainKeyAuthType):
    """Custom type rlKeyChainMngKeyAuthType based on RlKeyChainKeyAuthType"""
    defaultValue = 0


_RlKeyChainMngKeyAuthType_Type.__name__ = "RlKeyChainKeyAuthType"
_RlKeyChainMngKeyAuthType_Object = MibTableColumn
rlKeyChainMngKeyAuthType = _RlKeyChainMngKeyAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 3),
    _RlKeyChainMngKeyAuthType_Type()
)
rlKeyChainMngKeyAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyAuthType.setStatus("current")


class _RlKeyChainMngKey_Type(DisplayString):
    """Custom type rlKeyChainMngKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlKeyChainMngKey_Type.__name__ = "DisplayString"
_RlKeyChainMngKey_Object = MibTableColumn
rlKeyChainMngKey = _RlKeyChainMngKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 4),
    _RlKeyChainMngKey_Type()
)
rlKeyChainMngKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlKeyChainMngKey.setStatus("current")
_RlKeyChainMngKeyStartAccept_Type = DateAndTime
_RlKeyChainMngKeyStartAccept_Object = MibTableColumn
rlKeyChainMngKeyStartAccept = _RlKeyChainMngKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 5),
    _RlKeyChainMngKeyStartAccept_Type()
)
rlKeyChainMngKeyStartAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyStartAccept.setStatus("current")
_RlKeyChainMngKeyStartGenerate_Type = DateAndTime
_RlKeyChainMngKeyStartGenerate_Object = MibTableColumn
rlKeyChainMngKeyStartGenerate = _RlKeyChainMngKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 6),
    _RlKeyChainMngKeyStartGenerate_Type()
)
rlKeyChainMngKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyStartGenerate.setStatus("current")
_RlKeyChainMngKeyStopGenerate_Type = DateAndTime
_RlKeyChainMngKeyStopGenerate_Object = MibTableColumn
rlKeyChainMngKeyStopGenerate = _RlKeyChainMngKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 7),
    _RlKeyChainMngKeyStopGenerate_Type()
)
rlKeyChainMngKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyStopGenerate.setStatus("current")
_RlKeyChainMngKeyStopAccept_Type = DateAndTime
_RlKeyChainMngKeyStopAccept_Object = MibTableColumn
rlKeyChainMngKeyStopAccept = _RlKeyChainMngKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 8),
    _RlKeyChainMngKeyStopAccept_Type()
)
rlKeyChainMngKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyStopAccept.setStatus("current")


class _RlKeyChainMngKeyValidForAccept_Type(TruthValue):
    """Custom type rlKeyChainMngKeyValidForAccept based on TruthValue"""
    defaultValue = 2


_RlKeyChainMngKeyValidForAccept_Type.__name__ = "TruthValue"
_RlKeyChainMngKeyValidForAccept_Object = MibTableColumn
rlKeyChainMngKeyValidForAccept = _RlKeyChainMngKeyValidForAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 9),
    _RlKeyChainMngKeyValidForAccept_Type()
)
rlKeyChainMngKeyValidForAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyValidForAccept.setStatus("current")


class _RlKeyChainMngKeyValidForGenerate_Type(TruthValue):
    """Custom type rlKeyChainMngKeyValidForGenerate based on TruthValue"""
    defaultValue = 2


_RlKeyChainMngKeyValidForGenerate_Type.__name__ = "TruthValue"
_RlKeyChainMngKeyValidForGenerate_Object = MibTableColumn
rlKeyChainMngKeyValidForGenerate = _RlKeyChainMngKeyValidForGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 10),
    _RlKeyChainMngKeyValidForGenerate_Type()
)
rlKeyChainMngKeyValidForGenerate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlKeyChainMngKeyValidForGenerate.setStatus("current")
_RlKeyChainMngRowStatus_Type = RowStatus
_RlKeyChainMngRowStatus_Object = MibTableColumn
rlKeyChainMngRowStatus = _RlKeyChainMngRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 2, 1, 11),
    _RlKeyChainMngRowStatus_Type()
)
rlKeyChainMngRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlKeyChainMngRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DIGITALKEYMANAGE-MIB",
    **{"RlKeyChainKeyAuthType": RlKeyChainKeyAuthType,
       "rlDigitalKeyManage": rlDigitalKeyManage,
       "rlMD5KeyChainTable": rlMD5KeyChainTable,
       "rlMD5KeyChainEntry": rlMD5KeyChainEntry,
       "rlMD5KeyChainName": rlMD5KeyChainName,
       "rlMD5KeyChainKeyId": rlMD5KeyChainKeyId,
       "rlMD5KeyChainKey": rlMD5KeyChainKey,
       "rlMD5KeyChainKeyStartAccept": rlMD5KeyChainKeyStartAccept,
       "rlMD5KeyChainKeyStartGenerate": rlMD5KeyChainKeyStartGenerate,
       "rlMD5KeyChainKeyStopGenerate": rlMD5KeyChainKeyStopGenerate,
       "rlMD5KeyChainKeyStopAccept": rlMD5KeyChainKeyStopAccept,
       "rlMD5KeyChainKeyValidForAccept": rlMD5KeyChainKeyValidForAccept,
       "rlMD5KeyChainKeyValidForGenerate": rlMD5KeyChainKeyValidForGenerate,
       "rlMD5KeyChainRowStatus": rlMD5KeyChainRowStatus,
       "rlKeyChainMngTable": rlKeyChainMngTable,
       "rlKeyChainMngEntry": rlKeyChainMngEntry,
       "rlKeyChainMngName": rlKeyChainMngName,
       "rlKeyChainMngKeyId": rlKeyChainMngKeyId,
       "rlKeyChainMngKeyAuthType": rlKeyChainMngKeyAuthType,
       "rlKeyChainMngKey": rlKeyChainMngKey,
       "rlKeyChainMngKeyStartAccept": rlKeyChainMngKeyStartAccept,
       "rlKeyChainMngKeyStartGenerate": rlKeyChainMngKeyStartGenerate,
       "rlKeyChainMngKeyStopGenerate": rlKeyChainMngKeyStopGenerate,
       "rlKeyChainMngKeyStopAccept": rlKeyChainMngKeyStopAccept,
       "rlKeyChainMngKeyValidForAccept": rlKeyChainMngKeyValidForAccept,
       "rlKeyChainMngKeyValidForGenerate": rlKeyChainMngKeyValidForGenerate,
       "rlKeyChainMngRowStatus": rlKeyChainMngRowStatus}
)
