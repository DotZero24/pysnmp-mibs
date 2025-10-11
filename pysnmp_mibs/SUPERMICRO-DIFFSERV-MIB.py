# SNMP MIB module (SUPERMICRO-DIFFSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DIFFSERV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:21 2025
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

(InetAddressPrefixLength,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength")

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


# MODULE-IDENTITY

fsDiffServMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83)
)
if mibBuilder.loadTexts:
    fsDiffServMib.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IfDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outbound", 1),
          ("inbound", 2))
    )



class PortList(TextualConvention, OctetString):
    status = "current"


class DscpOrAny(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



# MIB Managed Objects in the order of their OIDs

_FsDiffServMIBObjects_ObjectIdentity = ObjectIdentity
fsDiffServMIBObjects = _FsDiffServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1)
)
_FsDiffServSystem_ObjectIdentity = ObjectIdentity
fsDiffServSystem = _FsDiffServSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 1)
)


class _FsDsSystemControl_Type(Integer32):
    """Custom type fsDsSystemControl based on Integer32"""
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


_FsDsSystemControl_Type.__name__ = "Integer32"
_FsDsSystemControl_Object = MibScalar
fsDsSystemControl = _FsDsSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 1, 1),
    _FsDsSystemControl_Type()
)
fsDsSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDsSystemControl.setStatus("current")


class _FsDsStatus_Type(Integer32):
    """Custom type fsDsStatus based on Integer32"""
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


_FsDsStatus_Type.__name__ = "Integer32"
_FsDsStatus_Object = MibScalar
fsDsStatus = _FsDsStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 1, 2),
    _FsDsStatus_Type()
)
fsDsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDsStatus.setStatus("current")
_FsDiffServMFClassifier_ObjectIdentity = ObjectIdentity
fsDiffServMFClassifier = _FsDiffServMFClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2)
)
_FsDiffServMultiFieldClfrTable_Object = MibTable
fsDiffServMultiFieldClfrTable = _FsDiffServMultiFieldClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsDiffServMultiFieldClfrTable.setStatus("current")
_FsDiffServMultiFieldClfrEntry_Object = MibTableRow
fsDiffServMultiFieldClfrEntry = _FsDiffServMultiFieldClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2, 1, 1)
)
fsDiffServMultiFieldClfrEntry.setIndexNames(
    (0, "SUPERMICRO-DIFFSERV-MIB", "fsDiffServMultiFieldClfrId"),
)
if mibBuilder.loadTexts:
    fsDiffServMultiFieldClfrEntry.setStatus("current")


class _FsDiffServMultiFieldClfrId_Type(Integer32):
    """Custom type fsDiffServMultiFieldClfrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDiffServMultiFieldClfrId_Type.__name__ = "Integer32"
_FsDiffServMultiFieldClfrId_Object = MibTableColumn
fsDiffServMultiFieldClfrId = _FsDiffServMultiFieldClfrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2, 1, 1, 1),
    _FsDiffServMultiFieldClfrId_Type()
)
fsDiffServMultiFieldClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiffServMultiFieldClfrId.setStatus("current")
_FsDiffServMultiFieldClfrFilterId_Type = Unsigned32
_FsDiffServMultiFieldClfrFilterId_Object = MibTableColumn
fsDiffServMultiFieldClfrFilterId = _FsDiffServMultiFieldClfrFilterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2, 1, 1, 2),
    _FsDiffServMultiFieldClfrFilterId_Type()
)
fsDiffServMultiFieldClfrFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServMultiFieldClfrFilterId.setStatus("current")


class _FsDiffServMultiFieldClfrFilterType_Type(Integer32):
    """Custom type fsDiffServMultiFieldClfrFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macfilter", 1),
          ("ipfilter", 2))
    )


_FsDiffServMultiFieldClfrFilterType_Type.__name__ = "Integer32"
_FsDiffServMultiFieldClfrFilterType_Object = MibTableColumn
fsDiffServMultiFieldClfrFilterType = _FsDiffServMultiFieldClfrFilterType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2, 1, 1, 3),
    _FsDiffServMultiFieldClfrFilterType_Type()
)
fsDiffServMultiFieldClfrFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServMultiFieldClfrFilterType.setStatus("current")
_FsDiffServMultiFieldClfrStatus_Type = RowStatus
_FsDiffServMultiFieldClfrStatus_Object = MibTableColumn
fsDiffServMultiFieldClfrStatus = _FsDiffServMultiFieldClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 2, 1, 1, 4),
    _FsDiffServMultiFieldClfrStatus_Type()
)
fsDiffServMultiFieldClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDiffServMultiFieldClfrStatus.setStatus("current")
_FsDiffServClassifier_ObjectIdentity = ObjectIdentity
fsDiffServClassifier = _FsDiffServClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3)
)
_FsDiffServClfrTable_Object = MibTable
fsDiffServClfrTable = _FsDiffServClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsDiffServClfrTable.setStatus("current")
_FsDiffServClfrEntry_Object = MibTableRow
fsDiffServClfrEntry = _FsDiffServClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1, 1)
)
fsDiffServClfrEntry.setIndexNames(
    (0, "SUPERMICRO-DIFFSERV-MIB", "fsDiffServClfrId"),
)
if mibBuilder.loadTexts:
    fsDiffServClfrEntry.setStatus("current")


class _FsDiffServClfrId_Type(Integer32):
    """Custom type fsDiffServClfrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDiffServClfrId_Type.__name__ = "Integer32"
_FsDiffServClfrId_Object = MibTableColumn
fsDiffServClfrId = _FsDiffServClfrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1, 1, 1),
    _FsDiffServClfrId_Type()
)
fsDiffServClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiffServClfrId.setStatus("current")


class _FsDiffServClfrMFClfrId_Type(Integer32):
    """Custom type fsDiffServClfrMFClfrId based on Integer32"""
    defaultValue = 0


_FsDiffServClfrMFClfrId_Type.__name__ = "Integer32"
_FsDiffServClfrMFClfrId_Object = MibTableColumn
fsDiffServClfrMFClfrId = _FsDiffServClfrMFClfrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1, 1, 2),
    _FsDiffServClfrMFClfrId_Type()
)
fsDiffServClfrMFClfrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServClfrMFClfrId.setStatus("current")


class _FsDiffServClfrInProActionId_Type(Integer32):
    """Custom type fsDiffServClfrInProActionId based on Integer32"""
    defaultValue = 0


_FsDiffServClfrInProActionId_Type.__name__ = "Integer32"
_FsDiffServClfrInProActionId_Object = MibTableColumn
fsDiffServClfrInProActionId = _FsDiffServClfrInProActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1, 1, 3),
    _FsDiffServClfrInProActionId_Type()
)
fsDiffServClfrInProActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServClfrInProActionId.setStatus("current")


class _FsDiffServClfrOutProActionId_Type(Integer32):
    """Custom type fsDiffServClfrOutProActionId based on Integer32"""
    defaultValue = 0


_FsDiffServClfrOutProActionId_Type.__name__ = "Integer32"
_FsDiffServClfrOutProActionId_Object = MibTableColumn
fsDiffServClfrOutProActionId = _FsDiffServClfrOutProActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1, 1, 4),
    _FsDiffServClfrOutProActionId_Type()
)
fsDiffServClfrOutProActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServClfrOutProActionId.setStatus("current")
_FsDiffServClfrStatus_Type = RowStatus
_FsDiffServClfrStatus_Object = MibTableColumn
fsDiffServClfrStatus = _FsDiffServClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 3, 1, 1, 5),
    _FsDiffServClfrStatus_Type()
)
fsDiffServClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDiffServClfrStatus.setStatus("current")
_FsDiffServInProfileAction_ObjectIdentity = ObjectIdentity
fsDiffServInProfileAction = _FsDiffServInProfileAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4)
)
_FsDiffServInProfileActionTable_Object = MibTable
fsDiffServInProfileActionTable = _FsDiffServInProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsDiffServInProfileActionTable.setStatus("current")
_FsDiffServInProfileActionEntry_Object = MibTableRow
fsDiffServInProfileActionEntry = _FsDiffServInProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1)
)
fsDiffServInProfileActionEntry.setIndexNames(
    (0, "SUPERMICRO-DIFFSERV-MIB", "fsDiffServInProfileActionId"),
)
if mibBuilder.loadTexts:
    fsDiffServInProfileActionEntry.setStatus("current")


class _FsDiffServInProfileActionId_Type(Integer32):
    """Custom type fsDiffServInProfileActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDiffServInProfileActionId_Type.__name__ = "Integer32"
_FsDiffServInProfileActionId_Object = MibTableColumn
fsDiffServInProfileActionId = _FsDiffServInProfileActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 1),
    _FsDiffServInProfileActionId_Type()
)
fsDiffServInProfileActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionId.setStatus("current")
_FsDiffServInProfileActionFlag_Type = Unsigned32
_FsDiffServInProfileActionFlag_Object = MibTableColumn
fsDiffServInProfileActionFlag = _FsDiffServInProfileActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 2),
    _FsDiffServInProfileActionFlag_Type()
)
fsDiffServInProfileActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionFlag.setStatus("current")
_FsDiffServInProfileActionNewPrio_Type = Unsigned32
_FsDiffServInProfileActionNewPrio_Object = MibTableColumn
fsDiffServInProfileActionNewPrio = _FsDiffServInProfileActionNewPrio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 3),
    _FsDiffServInProfileActionNewPrio_Type()
)
fsDiffServInProfileActionNewPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionNewPrio.setStatus("current")
_FsDiffServInProfileActionIpTOS_Type = Unsigned32
_FsDiffServInProfileActionIpTOS_Object = MibTableColumn
fsDiffServInProfileActionIpTOS = _FsDiffServInProfileActionIpTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 4),
    _FsDiffServInProfileActionIpTOS_Type()
)
fsDiffServInProfileActionIpTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionIpTOS.setStatus("current")
_FsDiffServInProfileActionPort_Type = Unsigned32
_FsDiffServInProfileActionPort_Object = MibTableColumn
fsDiffServInProfileActionPort = _FsDiffServInProfileActionPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 5),
    _FsDiffServInProfileActionPort_Type()
)
fsDiffServInProfileActionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionPort.setStatus("current")
_FsDiffServInProfileActionDscp_Type = DscpOrAny
_FsDiffServInProfileActionDscp_Object = MibTableColumn
fsDiffServInProfileActionDscp = _FsDiffServInProfileActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 6),
    _FsDiffServInProfileActionDscp_Type()
)
fsDiffServInProfileActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionDscp.setStatus("current")
_FsDiffServInProfileActionStatus_Type = RowStatus
_FsDiffServInProfileActionStatus_Object = MibTableColumn
fsDiffServInProfileActionStatus = _FsDiffServInProfileActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 4, 1, 1, 7),
    _FsDiffServInProfileActionStatus_Type()
)
fsDiffServInProfileActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDiffServInProfileActionStatus.setStatus("current")
_FsDiffServOutProfileAction_ObjectIdentity = ObjectIdentity
fsDiffServOutProfileAction = _FsDiffServOutProfileAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5)
)
_FsDiffServOutProfileActionTable_Object = MibTable
fsDiffServOutProfileActionTable = _FsDiffServOutProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionTable.setStatus("current")
_FsDiffServOutProfileActionEntry_Object = MibTableRow
fsDiffServOutProfileActionEntry = _FsDiffServOutProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1, 1)
)
fsDiffServOutProfileActionEntry.setIndexNames(
    (0, "SUPERMICRO-DIFFSERV-MIB", "fsDiffServOutProfileActionId"),
)
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionEntry.setStatus("current")


class _FsDiffServOutProfileActionId_Type(Integer32):
    """Custom type fsDiffServOutProfileActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDiffServOutProfileActionId_Type.__name__ = "Integer32"
_FsDiffServOutProfileActionId_Object = MibTableColumn
fsDiffServOutProfileActionId = _FsDiffServOutProfileActionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1, 1, 1),
    _FsDiffServOutProfileActionId_Type()
)
fsDiffServOutProfileActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionId.setStatus("current")
_FsDiffServOutProfileActionFlag_Type = Unsigned32
_FsDiffServOutProfileActionFlag_Object = MibTableColumn
fsDiffServOutProfileActionFlag = _FsDiffServOutProfileActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1, 1, 2),
    _FsDiffServOutProfileActionFlag_Type()
)
fsDiffServOutProfileActionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionFlag.setStatus("current")
_FsDiffServOutProfileActionDscp_Type = DscpOrAny
_FsDiffServOutProfileActionDscp_Object = MibTableColumn
fsDiffServOutProfileActionDscp = _FsDiffServOutProfileActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1, 1, 3),
    _FsDiffServOutProfileActionDscp_Type()
)
fsDiffServOutProfileActionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionDscp.setStatus("current")
_FsDiffServOutProfileActionMID_Type = Integer32
_FsDiffServOutProfileActionMID_Object = MibTableColumn
fsDiffServOutProfileActionMID = _FsDiffServOutProfileActionMID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1, 1, 4),
    _FsDiffServOutProfileActionMID_Type()
)
fsDiffServOutProfileActionMID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionMID.setStatus("current")
_FsDiffServOutProfileActionStatus_Type = RowStatus
_FsDiffServOutProfileActionStatus_Object = MibTableColumn
fsDiffServOutProfileActionStatus = _FsDiffServOutProfileActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 5, 1, 1, 5),
    _FsDiffServOutProfileActionStatus_Type()
)
fsDiffServOutProfileActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDiffServOutProfileActionStatus.setStatus("current")
_FsDiffServMeter_ObjectIdentity = ObjectIdentity
fsDiffServMeter = _FsDiffServMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6)
)
_FsDiffServMeterTable_Object = MibTable
fsDiffServMeterTable = _FsDiffServMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsDiffServMeterTable.setStatus("current")
_FsDiffServMeterEntry_Object = MibTableRow
fsDiffServMeterEntry = _FsDiffServMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6, 1, 1)
)
fsDiffServMeterEntry.setIndexNames(
    (0, "SUPERMICRO-DIFFSERV-MIB", "fsDiffServMeterId"),
)
if mibBuilder.loadTexts:
    fsDiffServMeterEntry.setStatus("current")


class _FsDiffServMeterId_Type(Integer32):
    """Custom type fsDiffServMeterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDiffServMeterId_Type.__name__ = "Integer32"
_FsDiffServMeterId_Object = MibTableColumn
fsDiffServMeterId = _FsDiffServMeterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6, 1, 1, 1),
    _FsDiffServMeterId_Type()
)
fsDiffServMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiffServMeterId.setStatus("current")
_FsDiffServMetertokenSize_Type = Unsigned32
_FsDiffServMetertokenSize_Object = MibTableColumn
fsDiffServMetertokenSize = _FsDiffServMetertokenSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6, 1, 1, 2),
    _FsDiffServMetertokenSize_Type()
)
fsDiffServMetertokenSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServMetertokenSize.setStatus("current")
_FsDiffServMeterRefreshCount_Type = Unsigned32
_FsDiffServMeterRefreshCount_Object = MibTableColumn
fsDiffServMeterRefreshCount = _FsDiffServMeterRefreshCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6, 1, 1, 3),
    _FsDiffServMeterRefreshCount_Type()
)
fsDiffServMeterRefreshCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServMeterRefreshCount.setStatus("current")
_FsDiffServMeterStatus_Type = RowStatus
_FsDiffServMeterStatus_Object = MibTableColumn
fsDiffServMeterStatus = _FsDiffServMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 6, 1, 1, 4),
    _FsDiffServMeterStatus_Type()
)
fsDiffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDiffServMeterStatus.setStatus("current")
_FsDiffServScheduler_ObjectIdentity = ObjectIdentity
fsDiffServScheduler = _FsDiffServScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7)
)
_FsDiffServSchedulerTable_Object = MibTable
fsDiffServSchedulerTable = _FsDiffServSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fsDiffServSchedulerTable.setStatus("current")
_FsDiffServSchedulerEntry_Object = MibTableRow
fsDiffServSchedulerEntry = _FsDiffServSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1, 1)
)
fsDiffServSchedulerEntry.setIndexNames(
    (0, "SUPERMICRO-DIFFSERV-MIB", "fsDiffServSchedulerId"),
)
if mibBuilder.loadTexts:
    fsDiffServSchedulerEntry.setStatus("current")


class _FsDiffServSchedulerId_Type(Integer32):
    """Custom type fsDiffServSchedulerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDiffServSchedulerId_Type.__name__ = "Integer32"
_FsDiffServSchedulerId_Object = MibTableColumn
fsDiffServSchedulerId = _FsDiffServSchedulerId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1, 1, 1),
    _FsDiffServSchedulerId_Type()
)
fsDiffServSchedulerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiffServSchedulerId.setStatus("current")
_FsDiffServSchedulerDPId_Type = Integer32
_FsDiffServSchedulerDPId_Object = MibTableColumn
fsDiffServSchedulerDPId = _FsDiffServSchedulerDPId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1, 1, 2),
    _FsDiffServSchedulerDPId_Type()
)
fsDiffServSchedulerDPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServSchedulerDPId.setStatus("current")


class _FsDiffServSchedulerQueueCount_Type(Unsigned32):
    """Custom type fsDiffServSchedulerQueueCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsDiffServSchedulerQueueCount_Type.__name__ = "Unsigned32"
_FsDiffServSchedulerQueueCount_Object = MibTableColumn
fsDiffServSchedulerQueueCount = _FsDiffServSchedulerQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1, 1, 3),
    _FsDiffServSchedulerQueueCount_Type()
)
fsDiffServSchedulerQueueCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServSchedulerQueueCount.setStatus("current")


class _FsDiffServSchedulerWeight_Type(OctetString):
    """Custom type fsDiffServSchedulerWeight based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_FsDiffServSchedulerWeight_Type.__name__ = "OctetString"
_FsDiffServSchedulerWeight_Object = MibTableColumn
fsDiffServSchedulerWeight = _FsDiffServSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1, 1, 4),
    _FsDiffServSchedulerWeight_Type()
)
fsDiffServSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServSchedulerWeight.setStatus("current")
_FsDiffServSchedulerStatus_Type = RowStatus
_FsDiffServSchedulerStatus_Object = MibTableColumn
fsDiffServSchedulerStatus = _FsDiffServSchedulerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 83, 1, 7, 1, 1, 5),
    _FsDiffServSchedulerStatus_Type()
)
fsDiffServSchedulerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiffServSchedulerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DIFFSERV-MIB",
    **{"IfDirection": IfDirection,
       "PortList": PortList,
       "DscpOrAny": DscpOrAny,
       "fsDiffServMib": fsDiffServMib,
       "fsDiffServMIBObjects": fsDiffServMIBObjects,
       "fsDiffServSystem": fsDiffServSystem,
       "fsDsSystemControl": fsDsSystemControl,
       "fsDsStatus": fsDsStatus,
       "fsDiffServMFClassifier": fsDiffServMFClassifier,
       "fsDiffServMultiFieldClfrTable": fsDiffServMultiFieldClfrTable,
       "fsDiffServMultiFieldClfrEntry": fsDiffServMultiFieldClfrEntry,
       "fsDiffServMultiFieldClfrId": fsDiffServMultiFieldClfrId,
       "fsDiffServMultiFieldClfrFilterId": fsDiffServMultiFieldClfrFilterId,
       "fsDiffServMultiFieldClfrFilterType": fsDiffServMultiFieldClfrFilterType,
       "fsDiffServMultiFieldClfrStatus": fsDiffServMultiFieldClfrStatus,
       "fsDiffServClassifier": fsDiffServClassifier,
       "fsDiffServClfrTable": fsDiffServClfrTable,
       "fsDiffServClfrEntry": fsDiffServClfrEntry,
       "fsDiffServClfrId": fsDiffServClfrId,
       "fsDiffServClfrMFClfrId": fsDiffServClfrMFClfrId,
       "fsDiffServClfrInProActionId": fsDiffServClfrInProActionId,
       "fsDiffServClfrOutProActionId": fsDiffServClfrOutProActionId,
       "fsDiffServClfrStatus": fsDiffServClfrStatus,
       "fsDiffServInProfileAction": fsDiffServInProfileAction,
       "fsDiffServInProfileActionTable": fsDiffServInProfileActionTable,
       "fsDiffServInProfileActionEntry": fsDiffServInProfileActionEntry,
       "fsDiffServInProfileActionId": fsDiffServInProfileActionId,
       "fsDiffServInProfileActionFlag": fsDiffServInProfileActionFlag,
       "fsDiffServInProfileActionNewPrio": fsDiffServInProfileActionNewPrio,
       "fsDiffServInProfileActionIpTOS": fsDiffServInProfileActionIpTOS,
       "fsDiffServInProfileActionPort": fsDiffServInProfileActionPort,
       "fsDiffServInProfileActionDscp": fsDiffServInProfileActionDscp,
       "fsDiffServInProfileActionStatus": fsDiffServInProfileActionStatus,
       "fsDiffServOutProfileAction": fsDiffServOutProfileAction,
       "fsDiffServOutProfileActionTable": fsDiffServOutProfileActionTable,
       "fsDiffServOutProfileActionEntry": fsDiffServOutProfileActionEntry,
       "fsDiffServOutProfileActionId": fsDiffServOutProfileActionId,
       "fsDiffServOutProfileActionFlag": fsDiffServOutProfileActionFlag,
       "fsDiffServOutProfileActionDscp": fsDiffServOutProfileActionDscp,
       "fsDiffServOutProfileActionMID": fsDiffServOutProfileActionMID,
       "fsDiffServOutProfileActionStatus": fsDiffServOutProfileActionStatus,
       "fsDiffServMeter": fsDiffServMeter,
       "fsDiffServMeterTable": fsDiffServMeterTable,
       "fsDiffServMeterEntry": fsDiffServMeterEntry,
       "fsDiffServMeterId": fsDiffServMeterId,
       "fsDiffServMetertokenSize": fsDiffServMetertokenSize,
       "fsDiffServMeterRefreshCount": fsDiffServMeterRefreshCount,
       "fsDiffServMeterStatus": fsDiffServMeterStatus,
       "fsDiffServScheduler": fsDiffServScheduler,
       "fsDiffServSchedulerTable": fsDiffServSchedulerTable,
       "fsDiffServSchedulerEntry": fsDiffServSchedulerEntry,
       "fsDiffServSchedulerId": fsDiffServSchedulerId,
       "fsDiffServSchedulerDPId": fsDiffServSchedulerDPId,
       "fsDiffServSchedulerQueueCount": fsDiffServSchedulerQueueCount,
       "fsDiffServSchedulerWeight": fsDiffServSchedulerWeight,
       "fsDiffServSchedulerStatus": fsDiffServSchedulerStatus}
)
