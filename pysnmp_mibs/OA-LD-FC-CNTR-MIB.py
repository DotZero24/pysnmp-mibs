# SNMP MIB module (OA-LD-FC-CNTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-LD-FC-CNTR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:12 2025
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

oaLdFcCntrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82)
)
if mibBuilder.loadTexts:
    oaLdFcCntrMib.setRevisions(
        ("2012-07-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaLambdaDriver_ObjectIdentity = ObjectIdentity
oaLambdaDriver = _OaLambdaDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41)
)
_OaLdFcCardPortCounters_ObjectIdentity = ObjectIdentity
oaLdFcCardPortCounters = _OaLdFcCardPortCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1)
)
_OaLdFcCardPortsCntrTable_Object = MibTable
oaLdFcCardPortsCntrTable = _OaLdFcCardPortsCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2)
)
if mibBuilder.loadTexts:
    oaLdFcCardPortsCntrTable.setStatus("current")
_OaLdFcCardPortsCntrEntry_Object = MibTableRow
oaLdFcCardPortsCntrEntry = _OaLdFcCardPortsCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1)
)
oaLdFcCardPortsCntrEntry.setIndexNames(
    (0, "OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrSlotNumber"),
    (0, "OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrPortNumber"),
)
if mibBuilder.loadTexts:
    oaLdFcCardPortsCntrEntry.setStatus("current")


class _OaLdFcCrdPrtsCntrSlotNumber_Type(Integer32):
    """Custom type oaLdFcCrdPrtsCntrSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaLdFcCrdPrtsCntrSlotNumber_Type.__name__ = "Integer32"
_OaLdFcCrdPrtsCntrSlotNumber_Object = MibTableColumn
oaLdFcCrdPrtsCntrSlotNumber = _OaLdFcCrdPrtsCntrSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 1),
    _OaLdFcCrdPrtsCntrSlotNumber_Type()
)
oaLdFcCrdPrtsCntrSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrSlotNumber.setStatus("current")


class _OaLdFcCrdPrtsCntrPortNumber_Type(Integer32):
    """Custom type oaLdFcCrdPrtsCntrPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaLdFcCrdPrtsCntrPortNumber_Type.__name__ = "Integer32"
_OaLdFcCrdPrtsCntrPortNumber_Object = MibTableColumn
oaLdFcCrdPrtsCntrPortNumber = _OaLdFcCrdPrtsCntrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 2),
    _OaLdFcCrdPrtsCntrPortNumber_Type()
)
oaLdFcCrdPrtsCntrPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrPortNumber.setStatus("current")


class _OaLdFcCrdPrtsCntrTxStatus_Type(Bits):
    """Custom type oaLdFcCrdPrtsCntrTxStatus based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("txNoSync", 1),
          ("txDLOL", 2))
    )

_OaLdFcCrdPrtsCntrTxStatus_Type.__name__ = "Bits"
_OaLdFcCrdPrtsCntrTxStatus_Object = MibTableColumn
oaLdFcCrdPrtsCntrTxStatus = _OaLdFcCrdPrtsCntrTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 3),
    _OaLdFcCrdPrtsCntrTxStatus_Type()
)
oaLdFcCrdPrtsCntrTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrTxStatus.setStatus("current")


class _OaLdFcCrdPrtsCntrRxStatus_Type(Bits):
    """Custom type oaLdFcCrdPrtsCntrRxStatus based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("rxNoSync", 1),
          ("rxDLOL", 2),
          ("rxASD", 3))
    )

_OaLdFcCrdPrtsCntrRxStatus_Type.__name__ = "Bits"
_OaLdFcCrdPrtsCntrRxStatus_Object = MibTableColumn
oaLdFcCrdPrtsCntrRxStatus = _OaLdFcCrdPrtsCntrRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 4),
    _OaLdFcCrdPrtsCntrRxStatus_Type()
)
oaLdFcCrdPrtsCntrRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrRxStatus.setStatus("current")
_OaLdFcCrdPrtsCntrTxTotalPckts_Type = Counter32
_OaLdFcCrdPrtsCntrTxTotalPckts_Object = MibTableColumn
oaLdFcCrdPrtsCntrTxTotalPckts = _OaLdFcCrdPrtsCntrTxTotalPckts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 5),
    _OaLdFcCrdPrtsCntrTxTotalPckts_Type()
)
oaLdFcCrdPrtsCntrTxTotalPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrTxTotalPckts.setStatus("current")
_OaLdFcCrdPrtsCntrRxTotalPckts_Type = Counter32
_OaLdFcCrdPrtsCntrRxTotalPckts_Object = MibTableColumn
oaLdFcCrdPrtsCntrRxTotalPckts = _OaLdFcCrdPrtsCntrRxTotalPckts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 6),
    _OaLdFcCrdPrtsCntrRxTotalPckts_Type()
)
oaLdFcCrdPrtsCntrRxTotalPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrRxTotalPckts.setStatus("current")
_OaLdFcCrdPrtsCntrTxLcvErrors_Type = Counter32
_OaLdFcCrdPrtsCntrTxLcvErrors_Object = MibTableColumn
oaLdFcCrdPrtsCntrTxLcvErrors = _OaLdFcCrdPrtsCntrTxLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 7),
    _OaLdFcCrdPrtsCntrTxLcvErrors_Type()
)
oaLdFcCrdPrtsCntrTxLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrTxLcvErrors.setStatus("current")
_OaLdFcCrdPrtsCntrRxLcvErrors_Type = Counter32
_OaLdFcCrdPrtsCntrRxLcvErrors_Object = MibTableColumn
oaLdFcCrdPrtsCntrRxLcvErrors = _OaLdFcCrdPrtsCntrRxLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 8),
    _OaLdFcCrdPrtsCntrRxLcvErrors_Type()
)
oaLdFcCrdPrtsCntrRxLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrRxLcvErrors.setStatus("current")
_OaLdFcCrdPrtsCntrTxBadCrcErrors_Type = Counter32
_OaLdFcCrdPrtsCntrTxBadCrcErrors_Object = MibTableColumn
oaLdFcCrdPrtsCntrTxBadCrcErrors = _OaLdFcCrdPrtsCntrTxBadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 9),
    _OaLdFcCrdPrtsCntrTxBadCrcErrors_Type()
)
oaLdFcCrdPrtsCntrTxBadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrTxBadCrcErrors.setStatus("current")
_OaLdFcCrdPrtsCntrRxBadCrcErrors_Type = Counter32
_OaLdFcCrdPrtsCntrRxBadCrcErrors_Object = MibTableColumn
oaLdFcCrdPrtsCntrRxBadCrcErrors = _OaLdFcCrdPrtsCntrRxBadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 1, 2, 1, 10),
    _OaLdFcCrdPrtsCntrRxBadCrcErrors_Type()
)
oaLdFcCrdPrtsCntrRxBadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdFcCrdPrtsCntrRxBadCrcErrors.setStatus("current")
_OaLdFcConformance_ObjectIdentity = ObjectIdentity
oaLdFcConformance = _OaLdFcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 2)
)
_OaLdFcGroups_ObjectIdentity = ObjectIdentity
oaLdFcGroups = _OaLdFcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 2, 1)
)
_OaLdFcCompliances_ObjectIdentity = ObjectIdentity
oaLdFcCompliances = _OaLdFcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 2, 2)
)

# Managed Objects groups

oaLdFcCardPortCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 2, 1, 1)
)
oaLdFcCardPortCountersGroup.setObjects(
      *(("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrTxStatus"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrRxStatus"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrTxTotalPckts"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrRxTotalPckts"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrTxLcvErrors"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrRxLcvErrors"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrTxBadCrcErrors"),
        ("OA-LD-FC-CNTR-MIB", "oaLdFcCrdPrtsCntrRxBadCrcErrors"))
)
if mibBuilder.loadTexts:
    oaLdFcCardPortCountersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaLdFcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 82, 2, 2, 1)
)
oaLdFcCompliance.setObjects(
    ("OA-LD-FC-CNTR-MIB", "oaLdFcCardPortCountersGroup")
)
if mibBuilder.loadTexts:
    oaLdFcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-LD-FC-CNTR-MIB",
    **{"oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaLambdaDriver": oaLambdaDriver,
       "oaLdFcCntrMib": oaLdFcCntrMib,
       "oaLdFcCardPortCounters": oaLdFcCardPortCounters,
       "oaLdFcCardPortsCntrTable": oaLdFcCardPortsCntrTable,
       "oaLdFcCardPortsCntrEntry": oaLdFcCardPortsCntrEntry,
       "oaLdFcCrdPrtsCntrSlotNumber": oaLdFcCrdPrtsCntrSlotNumber,
       "oaLdFcCrdPrtsCntrPortNumber": oaLdFcCrdPrtsCntrPortNumber,
       "oaLdFcCrdPrtsCntrTxStatus": oaLdFcCrdPrtsCntrTxStatus,
       "oaLdFcCrdPrtsCntrRxStatus": oaLdFcCrdPrtsCntrRxStatus,
       "oaLdFcCrdPrtsCntrTxTotalPckts": oaLdFcCrdPrtsCntrTxTotalPckts,
       "oaLdFcCrdPrtsCntrRxTotalPckts": oaLdFcCrdPrtsCntrRxTotalPckts,
       "oaLdFcCrdPrtsCntrTxLcvErrors": oaLdFcCrdPrtsCntrTxLcvErrors,
       "oaLdFcCrdPrtsCntrRxLcvErrors": oaLdFcCrdPrtsCntrRxLcvErrors,
       "oaLdFcCrdPrtsCntrTxBadCrcErrors": oaLdFcCrdPrtsCntrTxBadCrcErrors,
       "oaLdFcCrdPrtsCntrRxBadCrcErrors": oaLdFcCrdPrtsCntrRxBadCrcErrors,
       "oaLdFcConformance": oaLdFcConformance,
       "oaLdFcGroups": oaLdFcGroups,
       "oaLdFcCardPortCountersGroup": oaLdFcCardPortCountersGroup,
       "oaLdFcCompliances": oaLdFcCompliances,
       "oaLdFcCompliance": oaLdFcCompliance}
)
