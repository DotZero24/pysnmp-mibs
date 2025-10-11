# SNMP MIB module (SUPERMICRO-PBB-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PBB-TE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:31 2025
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

(IfIndexList,
 ieee8021PbbTeTeSidEntry) = mibBuilder.importSymbols(
    "IEEE8021-PBBTE-MIB",
    "IfIndexList",
    "ieee8021PbbTeTeSidEntry")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(VlanId,) = mibBuilder.importSymbols(
    "SUPERMICROQ-BRIDGE-MIB",
    "VlanId")


# MODULE-IDENTITY

fspbbte = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11)
)
if mibBuilder.loadTexts:
    fspbbte.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPbbTeScalars_ObjectIdentity = ObjectIdentity
fsPbbTeScalars = _FsPbbTeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 1)
)
_FsPbbTeGlobalTraceOption_Type = Unsigned32
_FsPbbTeGlobalTraceOption_Object = MibScalar
fsPbbTeGlobalTraceOption = _FsPbbTeGlobalTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 1, 1),
    _FsPbbTeGlobalTraceOption_Type()
)
fsPbbTeGlobalTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeGlobalTraceOption.setStatus("current")
_FsPbbTeContext_ObjectIdentity = ObjectIdentity
fsPbbTeContext = _FsPbbTeContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2)
)
_FsPbbTeContextTable_Object = MibTable
fsPbbTeContextTable = _FsPbbTeContextTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    fsPbbTeContextTable.setStatus("current")
_FsPbbTeContextEntry_Object = MibTableRow
fsPbbTeContextEntry = _FsPbbTeContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1)
)
fsPbbTeContextEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-TE-MIB", "fsPbbTeContextId"),
)
if mibBuilder.loadTexts:
    fsPbbTeContextEntry.setStatus("current")


class _FsPbbTeContextId_Type(Integer32):
    """Custom type fsPbbTeContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPbbTeContextId_Type.__name__ = "Integer32"
_FsPbbTeContextId_Object = MibTableColumn
fsPbbTeContextId = _FsPbbTeContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1, 1),
    _FsPbbTeContextId_Type()
)
fsPbbTeContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbTeContextId.setStatus("current")


class _FsPbbTeContextSystemControl_Type(Integer32):
    """Custom type fsPbbTeContextSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPbbTeContextSystemControl_Type.__name__ = "Integer32"
_FsPbbTeContextSystemControl_Object = MibTableColumn
fsPbbTeContextSystemControl = _FsPbbTeContextSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1, 2),
    _FsPbbTeContextSystemControl_Type()
)
fsPbbTeContextSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeContextSystemControl.setStatus("current")
_FsPbbTeContextTraceOption_Type = Unsigned32
_FsPbbTeContextTraceOption_Object = MibTableColumn
fsPbbTeContextTraceOption = _FsPbbTeContextTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1, 3),
    _FsPbbTeContextTraceOption_Type()
)
fsPbbTeContextTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeContextTraceOption.setStatus("current")
_FsPbbTeContextNoOfActiveEsps_Type = Counter32
_FsPbbTeContextNoOfActiveEsps_Object = MibTableColumn
fsPbbTeContextNoOfActiveEsps = _FsPbbTeContextNoOfActiveEsps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1, 4),
    _FsPbbTeContextNoOfActiveEsps_Type()
)
fsPbbTeContextNoOfActiveEsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbTeContextNoOfActiveEsps.setStatus("current")
_FsPbbTeContextNoOfCreatedEsps_Type = Counter32
_FsPbbTeContextNoOfCreatedEsps_Object = MibTableColumn
fsPbbTeContextNoOfCreatedEsps = _FsPbbTeContextNoOfCreatedEsps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1, 5),
    _FsPbbTeContextNoOfCreatedEsps_Type()
)
fsPbbTeContextNoOfCreatedEsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbTeContextNoOfCreatedEsps.setStatus("current")
_FsPbbTeContextNoOfDeletedEsps_Type = Counter32
_FsPbbTeContextNoOfDeletedEsps_Object = MibTableColumn
fsPbbTeContextNoOfDeletedEsps = _FsPbbTeContextNoOfDeletedEsps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 2, 1, 1, 6),
    _FsPbbTeContextNoOfDeletedEsps_Type()
)
fsPbbTeContextNoOfDeletedEsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbTeContextNoOfDeletedEsps.setStatus("current")
_FsPbbTeEspVidMapping_ObjectIdentity = ObjectIdentity
fsPbbTeEspVidMapping = _FsPbbTeEspVidMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 3)
)
_FsPbbTeEspVidTable_Object = MibTable
fsPbbTeEspVidTable = _FsPbbTeEspVidTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    fsPbbTeEspVidTable.setStatus("current")
_FsPbbTeEspVidEntry_Object = MibTableRow
fsPbbTeEspVidEntry = _FsPbbTeEspVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 3, 1, 1)
)
fsPbbTeEspVidEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-TE-MIB", "fsPbbTeContextId"),
    (0, "SUPERMICRO-PBB-TE-MIB", "fsPbbTeEspVid"),
)
if mibBuilder.loadTexts:
    fsPbbTeEspVidEntry.setStatus("current")
_FsPbbTeEspVid_Type = VlanId
_FsPbbTeEspVid_Object = MibTableColumn
fsPbbTeEspVid = _FsPbbTeEspVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 3, 1, 1, 1),
    _FsPbbTeEspVid_Type()
)
fsPbbTeEspVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbTeEspVid.setStatus("current")


class _FsPbbTeEspVidRowStatus_Type(RowStatus):
    """Custom type fsPbbTeEspVidRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )


_FsPbbTeEspVidRowStatus_Type.__name__ = "RowStatus"
_FsPbbTeEspVidRowStatus_Object = MibTableColumn
fsPbbTeEspVidRowStatus = _FsPbbTeEspVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 3, 1, 1, 2),
    _FsPbbTeEspVidRowStatus_Type()
)
fsPbbTeEspVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbTeEspVidRowStatus.setStatus("current")
_FsPbbTeTeSidExtension_ObjectIdentity = ObjectIdentity
fsPbbTeTeSidExtension = _FsPbbTeTeSidExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 4)
)
_FsPbbTeTeSidExtTable_Object = MibTable
fsPbbTeTeSidExtTable = _FsPbbTeTeSidExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    fsPbbTeTeSidExtTable.setStatus("current")
_FsPbbTeTeSidExtEntry_Object = MibTableRow
fsPbbTeTeSidExtEntry = _FsPbbTeTeSidExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fsPbbTeTeSidExtEntry.setStatus("current")


class _FsPbbTeTeSidExtContextId_Type(Integer32):
    """Custom type fsPbbTeTeSidExtContextId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_FsPbbTeTeSidExtContextId_Type.__name__ = "Integer32"
_FsPbbTeTeSidExtContextId_Object = MibTableColumn
fsPbbTeTeSidExtContextId = _FsPbbTeTeSidExtContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 4, 1, 1, 1),
    _FsPbbTeTeSidExtContextId_Type()
)
fsPbbTeTeSidExtContextId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTeSidExtContextId.setStatus("current")
_FsPbbTeTest_ObjectIdentity = ObjectIdentity
fsPbbTeTest = _FsPbbTeTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5)
)


class _FsPbbTeTestApiContextId_Type(Integer32):
    """Custom type fsPbbTeTestApiContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPbbTeTestApiContextId_Type.__name__ = "Integer32"
_FsPbbTeTestApiContextId_Object = MibScalar
fsPbbTeTestApiContextId = _FsPbbTeTestApiContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 1),
    _FsPbbTeTestApiContextId_Type()
)
fsPbbTeTestApiContextId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiContextId.setStatus("current")
_FsPbbTeTestApiTeSid_Type = Integer32
_FsPbbTeTestApiTeSid_Object = MibScalar
fsPbbTeTestApiTeSid = _FsPbbTeTestApiTeSid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 2),
    _FsPbbTeTestApiTeSid_Type()
)
fsPbbTeTestApiTeSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiTeSid.setStatus("current")
_FsPbbTeTestApiDestMacAddr_Type = MacAddress
_FsPbbTeTestApiDestMacAddr_Object = MibScalar
fsPbbTeTestApiDestMacAddr = _FsPbbTeTestApiDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 3),
    _FsPbbTeTestApiDestMacAddr_Type()
)
fsPbbTeTestApiDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiDestMacAddr.setStatus("current")
_FsPbbTeTestApiSourceMacAddr_Type = MacAddress
_FsPbbTeTestApiSourceMacAddr_Object = MibScalar
fsPbbTeTestApiSourceMacAddr = _FsPbbTeTestApiSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 4),
    _FsPbbTeTestApiSourceMacAddr_Type()
)
fsPbbTeTestApiSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiSourceMacAddr.setStatus("current")
_FsPbbTeTestApiEspVlanId_Type = VlanId
_FsPbbTeTestApiEspVlanId_Object = MibScalar
fsPbbTeTestApiEspVlanId = _FsPbbTeTestApiEspVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 5),
    _FsPbbTeTestApiEspVlanId_Type()
)
fsPbbTeTestApiEspVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiEspVlanId.setStatus("current")


class _FsPbbTeTestApiEgressPort_Type(Integer32):
    """Custom type fsPbbTeTestApiEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPbbTeTestApiEgressPort_Type.__name__ = "Integer32"
_FsPbbTeTestApiEgressPort_Object = MibScalar
fsPbbTeTestApiEgressPort = _FsPbbTeTestApiEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 6),
    _FsPbbTeTestApiEgressPort_Type()
)
fsPbbTeTestApiEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiEgressPort.setStatus("current")
_FsPbbTeTestApiEgressPortList_Type = IfIndexList
_FsPbbTeTestApiEgressPortList_Object = MibScalar
fsPbbTeTestApiEgressPortList = _FsPbbTeTestApiEgressPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 7),
    _FsPbbTeTestApiEgressPortList_Type()
)
fsPbbTeTestApiEgressPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiEgressPortList.setStatus("current")


class _FsPbbTeTestApiAction_Type(Integer32):
    """Custom type fsPbbTeTestApiAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destroy", 2))
    )


_FsPbbTeTestApiAction_Type.__name__ = "Integer32"
_FsPbbTeTestApiAction_Object = MibScalar
fsPbbTeTestApiAction = _FsPbbTeTestApiAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 11, 5, 8),
    _FsPbbTeTestApiAction_Type()
)
fsPbbTeTestApiAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbTeTestApiAction.setStatus("current")
ieee8021PbbTeTeSidEntry.registerAugmentions(
    ("SUPERMICRO-PBB-TE-MIB",
     "fsPbbTeTeSidExtEntry")
)
fsPbbTeTeSidExtEntry.setIndexNames(*ieee8021PbbTeTeSidEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PBB-TE-MIB",
    **{"fspbbte": fspbbte,
       "fsPbbTeScalars": fsPbbTeScalars,
       "fsPbbTeGlobalTraceOption": fsPbbTeGlobalTraceOption,
       "fsPbbTeContext": fsPbbTeContext,
       "fsPbbTeContextTable": fsPbbTeContextTable,
       "fsPbbTeContextEntry": fsPbbTeContextEntry,
       "fsPbbTeContextId": fsPbbTeContextId,
       "fsPbbTeContextSystemControl": fsPbbTeContextSystemControl,
       "fsPbbTeContextTraceOption": fsPbbTeContextTraceOption,
       "fsPbbTeContextNoOfActiveEsps": fsPbbTeContextNoOfActiveEsps,
       "fsPbbTeContextNoOfCreatedEsps": fsPbbTeContextNoOfCreatedEsps,
       "fsPbbTeContextNoOfDeletedEsps": fsPbbTeContextNoOfDeletedEsps,
       "fsPbbTeEspVidMapping": fsPbbTeEspVidMapping,
       "fsPbbTeEspVidTable": fsPbbTeEspVidTable,
       "fsPbbTeEspVidEntry": fsPbbTeEspVidEntry,
       "fsPbbTeEspVid": fsPbbTeEspVid,
       "fsPbbTeEspVidRowStatus": fsPbbTeEspVidRowStatus,
       "fsPbbTeTeSidExtension": fsPbbTeTeSidExtension,
       "fsPbbTeTeSidExtTable": fsPbbTeTeSidExtTable,
       "fsPbbTeTeSidExtEntry": fsPbbTeTeSidExtEntry,
       "fsPbbTeTeSidExtContextId": fsPbbTeTeSidExtContextId,
       "fsPbbTeTest": fsPbbTeTest,
       "fsPbbTeTestApiContextId": fsPbbTeTestApiContextId,
       "fsPbbTeTestApiTeSid": fsPbbTeTestApiTeSid,
       "fsPbbTeTestApiDestMacAddr": fsPbbTeTestApiDestMacAddr,
       "fsPbbTeTestApiSourceMacAddr": fsPbbTeTestApiSourceMacAddr,
       "fsPbbTeTestApiEspVlanId": fsPbbTeTestApiEspVlanId,
       "fsPbbTeTestApiEgressPort": fsPbbTeTestApiEgressPort,
       "fsPbbTeTestApiEgressPortList": fsPbbTeTestApiEgressPortList,
       "fsPbbTeTestApiAction": fsPbbTeTestApiAction}
)
