# SNMP MIB module (H3C-FC-FLOGIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FC-FLOGIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:18 2025
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

(H3cFcAddressId,
 H3cFcBbCredit,
 H3cFcClassOfServices,
 H3cFcNameId,
 H3cFcRxMTU) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcAddressId",
    "H3cFcBbCredit",
    "H3cFcClassOfServices",
    "H3cFcNameId",
    "H3cFcRxMTU")

(h3cSan,
 h3cVsanIndex) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan",
    "h3cVsanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cFcFLogin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3)
)
if mibBuilder.loadTexts:
    h3cFcFLogin.setRevisions(
        ("2013-02-27 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFcFLoginMibObjects_ObjectIdentity = ObjectIdentity
h3cFcFLoginMibObjects = _H3cFcFLoginMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1)
)
_H3cFcFLoginTable_Object = MibTable
h3cFcFLoginTable = _H3cFcFLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFcFLoginTable.setStatus("current")
_H3cFcFLoginEntry_Object = MibTableRow
h3cFcFLoginEntry = _H3cFcFLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1)
)
h3cFcFLoginEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-FC-FLOGIN-MIB", "h3cFcFLoginIndex"),
)
if mibBuilder.loadTexts:
    h3cFcFLoginEntry.setStatus("current")
_H3cFcFLoginIndex_Type = H3cFcAddressId
_H3cFcFLoginIndex_Object = MibTableColumn
h3cFcFLoginIndex = _H3cFcFLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 1),
    _H3cFcFLoginIndex_Type()
)
h3cFcFLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcFLoginIndex.setStatus("current")
_H3cFcFLoginPortNodeWWN_Type = H3cFcNameId
_H3cFcFLoginPortNodeWWN_Object = MibTableColumn
h3cFcFLoginPortNodeWWN = _H3cFcFLoginPortNodeWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 2),
    _H3cFcFLoginPortNodeWWN_Type()
)
h3cFcFLoginPortNodeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginPortNodeWWN.setStatus("current")
_H3cFcFLoginPortWWN_Type = H3cFcNameId
_H3cFcFLoginPortWWN_Object = MibTableColumn
h3cFcFLoginPortWWN = _H3cFcFLoginPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 3),
    _H3cFcFLoginPortWWN_Type()
)
h3cFcFLoginPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginPortWWN.setStatus("current")
_H3cFcFLoginPortFcId_Type = H3cFcAddressId
_H3cFcFLoginPortFcId_Object = MibTableColumn
h3cFcFLoginPortFcId = _H3cFcFLoginPortFcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 4),
    _H3cFcFLoginPortFcId_Type()
)
h3cFcFLoginPortFcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginPortFcId.setStatus("current")
_H3cFcFLoginRxBbCredit_Type = H3cFcBbCredit
_H3cFcFLoginRxBbCredit_Object = MibTableColumn
h3cFcFLoginRxBbCredit = _H3cFcFLoginRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 5),
    _H3cFcFLoginRxBbCredit_Type()
)
h3cFcFLoginRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginRxBbCredit.setStatus("current")
_H3cFcFLoginTxBbCredit_Type = H3cFcBbCredit
_H3cFcFLoginTxBbCredit_Object = MibTableColumn
h3cFcFLoginTxBbCredit = _H3cFcFLoginTxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 6),
    _H3cFcFLoginTxBbCredit_Type()
)
h3cFcFLoginTxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginTxBbCredit.setStatus("current")
_H3cFcFLoginClass2RxMTU_Type = H3cFcRxMTU
_H3cFcFLoginClass2RxMTU_Object = MibTableColumn
h3cFcFLoginClass2RxMTU = _H3cFcFLoginClass2RxMTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 7),
    _H3cFcFLoginClass2RxMTU_Type()
)
h3cFcFLoginClass2RxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginClass2RxMTU.setStatus("current")
_H3cFcFLoginClass3RxMTU_Type = H3cFcRxMTU
_H3cFcFLoginClass3RxMTU_Object = MibTableColumn
h3cFcFLoginClass3RxMTU = _H3cFcFLoginClass3RxMTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 8),
    _H3cFcFLoginClass3RxMTU_Type()
)
h3cFcFLoginClass3RxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginClass3RxMTU.setStatus("current")
_H3cFcFLoginSuppClassRequested_Type = H3cFcClassOfServices
_H3cFcFLoginSuppClassRequested_Object = MibTableColumn
h3cFcFLoginSuppClassRequested = _H3cFcFLoginSuppClassRequested_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 9),
    _H3cFcFLoginSuppClassRequested_Type()
)
h3cFcFLoginSuppClassRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginSuppClassRequested.setStatus("current")
_H3cFcFLoginClass2ReqAgreed_Type = TruthValue
_H3cFcFLoginClass2ReqAgreed_Object = MibTableColumn
h3cFcFLoginClass2ReqAgreed = _H3cFcFLoginClass2ReqAgreed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 10),
    _H3cFcFLoginClass2ReqAgreed_Type()
)
h3cFcFLoginClass2ReqAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginClass2ReqAgreed.setStatus("current")
_H3cFcFLoginClass3ReqAgreed_Type = TruthValue
_H3cFcFLoginClass3ReqAgreed_Object = MibTableColumn
h3cFcFLoginClass3ReqAgreed = _H3cFcFLoginClass3ReqAgreed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 3, 1, 1, 1, 11),
    _H3cFcFLoginClass3ReqAgreed_Type()
)
h3cFcFLoginClass3ReqAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcFLoginClass3ReqAgreed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FC-FLOGIN-MIB",
    **{"h3cFcFLogin": h3cFcFLogin,
       "h3cFcFLoginMibObjects": h3cFcFLoginMibObjects,
       "h3cFcFLoginTable": h3cFcFLoginTable,
       "h3cFcFLoginEntry": h3cFcFLoginEntry,
       "h3cFcFLoginIndex": h3cFcFLoginIndex,
       "h3cFcFLoginPortNodeWWN": h3cFcFLoginPortNodeWWN,
       "h3cFcFLoginPortWWN": h3cFcFLoginPortWWN,
       "h3cFcFLoginPortFcId": h3cFcFLoginPortFcId,
       "h3cFcFLoginRxBbCredit": h3cFcFLoginRxBbCredit,
       "h3cFcFLoginTxBbCredit": h3cFcFLoginTxBbCredit,
       "h3cFcFLoginClass2RxMTU": h3cFcFLoginClass2RxMTU,
       "h3cFcFLoginClass3RxMTU": h3cFcFLoginClass3RxMTU,
       "h3cFcFLoginSuppClassRequested": h3cFcFLoginSuppClassRequested,
       "h3cFcFLoginClass2ReqAgreed": h3cFcFLoginClass2ReqAgreed,
       "h3cFcFLoginClass3ReqAgreed": h3cFcFLoginClass3ReqAgreed}
)
