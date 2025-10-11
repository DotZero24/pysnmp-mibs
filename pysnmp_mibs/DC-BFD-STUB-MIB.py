# SNMP MIB module (DC-BFD-STUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-BFD-STUB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:49 2025
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

(AdminStatus,
 EntityProcType,
 InterfaceScope,
 NpgOperStatus,
 NumericIndex) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AdminStatus",
    "EntityProcType",
    "InterfaceScope",
    "NpgOperStatus",
    "NumericIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

bfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 11)
)
if mibBuilder.loadTexts:
    bfdMIB.setRevisions(
        ("2015-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BfdInterval(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BfdDiag(TextualConvention, Integer32):
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
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noDiagnostic", 1),
          ("controlDetectionTimeExpired", 2),
          ("echoFunctionFailed", 3),
          ("neighborSignaledSessionDown", 4),
          ("forwardingPlaneReset", 5),
          ("pathDown", 6),
          ("concatenatedPathDown", 7),
          ("administrativelyDown", 8),
          ("reverseConcatenatedPathDown", 9),
          ("misconnectivity", 16),
          ("noContact", 255))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_BfdNotifications_ObjectIdentity = ObjectIdentity
bfdNotifications = _BfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 0)
)
_BfdObjects_ObjectIdentity = ObjectIdentity
bfdObjects = _BfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1)
)
_BfdEntityTable_Object = MibTable
bfdEntityTable = _BfdEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1)
)
if mibBuilder.loadTexts:
    bfdEntityTable.setStatus("current")
_BfdEntityEntry_Object = MibTableRow
bfdEntityEntry = _BfdEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1)
)
bfdEntityEntry.setIndexNames(
    (0, "DC-BFD-STUB-MIB", "bfdEntityIndex"),
)
if mibBuilder.loadTexts:
    bfdEntityEntry.setStatus("current")
_BfdEntityIndex_Type = NumericIndex
_BfdEntityIndex_Object = MibTableColumn
bfdEntityIndex = _BfdEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 1),
    _BfdEntityIndex_Type()
)
bfdEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdEntityIndex.setStatus("current")


class _BfdAdminStatus_Type(AdminStatus):
    """Custom type bfdAdminStatus based on AdminStatus"""
    defaultValue = 1


_BfdAdminStatus_Type.__name__ = "AdminStatus"
_BfdAdminStatus_Object = MibTableColumn
bfdAdminStatus = _BfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 2),
    _BfdAdminStatus_Type()
)
bfdAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdAdminStatus.setStatus("current")
_BfdOperStatus_Type = NpgOperStatus
_BfdOperStatus_Object = MibTableColumn
bfdOperStatus = _BfdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 3),
    _BfdOperStatus_Type()
)
bfdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdOperStatus.setStatus("current")
_BfdRowStatus_Type = RowStatus
_BfdRowStatus_Object = MibTableColumn
bfdRowStatus = _BfdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 4),
    _BfdRowStatus_Type()
)
bfdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdRowStatus.setStatus("current")


class _BfdVersionNumber_Type(Unsigned32):
    """Custom type bfdVersionNumber based on Unsigned32"""
    defaultValue = 1


_BfdVersionNumber_Type.__name__ = "Unsigned32"
_BfdVersionNumber_Object = MibTableColumn
bfdVersionNumber = _BfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 5),
    _BfdVersionNumber_Type()
)
bfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdVersionNumber.setStatus("current")


class _BfdDesiredMinTxInterval_Type(BfdInterval):
    """Custom type bfdDesiredMinTxInterval based on BfdInterval"""
    defaultValue = 150000


_BfdDesiredMinTxInterval_Type.__name__ = "BfdInterval"
_BfdDesiredMinTxInterval_Object = MibTableColumn
bfdDesiredMinTxInterval = _BfdDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 6),
    _BfdDesiredMinTxInterval_Type()
)
bfdDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdDesiredMinTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    bfdDesiredMinTxInterval.setUnits("microseconds")


class _BfdReqMinRxInterval_Type(BfdInterval):
    """Custom type bfdReqMinRxInterval based on BfdInterval"""
    defaultValue = 150000


_BfdReqMinRxInterval_Type.__name__ = "BfdInterval"
_BfdReqMinRxInterval_Object = MibTableColumn
bfdReqMinRxInterval = _BfdReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 7),
    _BfdReqMinRxInterval_Type()
)
bfdReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdReqMinRxInterval.setStatus("current")
if mibBuilder.loadTexts:
    bfdReqMinRxInterval.setUnits("microseconds")


class _BfdInterfaceScope_Type(InterfaceScope):
    """Custom type bfdInterfaceScope based on InterfaceScope"""
    defaultHexValue = ""


_BfdInterfaceScope_Type.__name__ = "InterfaceScope"
_BfdInterfaceScope_Object = MibTableColumn
bfdInterfaceScope = _BfdInterfaceScope_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 1, 1, 8),
    _BfdInterfaceScope_Type()
)
bfdInterfaceScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdInterfaceScope.setStatus("current")
_BfdSessionTable_Object = MibTable
bfdSessionTable = _BfdSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2)
)
if mibBuilder.loadTexts:
    bfdSessionTable.setStatus("current")
_BfdSessionEntry_Object = MibTableRow
bfdSessionEntry = _BfdSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1)
)
bfdSessionEntry.setIndexNames(
    (0, "DC-BFD-STUB-MIB", "bfdEntityIndex"),
    (0, "DC-BFD-STUB-MIB", "bfdSessIndex"),
)
if mibBuilder.loadTexts:
    bfdSessionEntry.setStatus("current")
_BfdSessIndex_Type = BfdSessIndexTC
_BfdSessIndex_Object = MibTableColumn
bfdSessIndex = _BfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 1),
    _BfdSessIndex_Type()
)
bfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessIndex.setStatus("current")


class _BfdSessDiscriminator_Type(Unsigned32):
    """Custom type bfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BfdSessDiscriminator_Type.__name__ = "Unsigned32"
_BfdSessDiscriminator_Object = MibTableColumn
bfdSessDiscriminator = _BfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 4),
    _BfdSessDiscriminator_Type()
)
bfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessDiscriminator.setStatus("current")


class _BfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type bfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_BfdSessRemoteDiscr_Object = MibTableColumn
bfdSessRemoteDiscr = _BfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 5),
    _BfdSessRemoteDiscr_Type()
)
bfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessRemoteDiscr.setStatus("current")


class _BfdSessState_Type(Integer32):
    """Custom type bfdSessState based on Integer32"""
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4))
    )


_BfdSessState_Type.__name__ = "Integer32"
_BfdSessState_Object = MibTableColumn
bfdSessState = _BfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 7),
    _BfdSessState_Type()
)
bfdSessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessState.setStatus("current")
_BfdSessDiag_Type = BfdDiag
_BfdSessDiag_Object = MibTableColumn
bfdSessDiag = _BfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 9),
    _BfdSessDiag_Type()
)
bfdSessDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessDiag.setStatus("current")


class _BfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type bfdSessControlPlanIndepFlag based on TruthValue"""
    defaultValue = 2


_BfdSessControlPlanIndepFlag_Type.__name__ = "TruthValue"
_BfdSessControlPlanIndepFlag_Object = MibTableColumn
bfdSessControlPlanIndepFlag = _BfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 13),
    _BfdSessControlPlanIndepFlag_Type()
)
bfdSessControlPlanIndepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessControlPlanIndepFlag.setStatus("current")
_BfdSessIntface_Type = InterfaceIndexOrZero
_BfdSessIntface_Object = MibTableColumn
bfdSessIntface = _BfdSessIntface_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 14),
    _BfdSessIntface_Type()
)
bfdSessIntface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessIntface.setStatus("current")
_BfdSessAddrType_Type = InetAddressType
_BfdSessAddrType_Object = MibTableColumn
bfdSessAddrType = _BfdSessAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 15),
    _BfdSessAddrType_Type()
)
bfdSessAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessAddrType.setStatus("current")


class _BfdSessAddr_Type(InetAddress):
    """Custom type bfdSessAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_BfdSessAddr_Type.__name__ = "InetAddress"
_BfdSessAddr_Object = MibTableColumn
bfdSessAddr = _BfdSessAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 16),
    _BfdSessAddr_Type()
)
bfdSessAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessAddr.setStatus("current")
_BfdSessApplicationSessions_Type = Gauge32
_BfdSessApplicationSessions_Object = MibTableColumn
bfdSessApplicationSessions = _BfdSessApplicationSessions_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 27),
    _BfdSessApplicationSessions_Type()
)
bfdSessApplicationSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessApplicationSessions.setStatus("current")
_BfdSessLocalAddrType_Type = InetAddressType
_BfdSessLocalAddrType_Object = MibTableColumn
bfdSessLocalAddrType = _BfdSessLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 28),
    _BfdSessLocalAddrType_Type()
)
bfdSessLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessLocalAddrType.setStatus("current")
_BfdSessLocalAddr_Type = InetAddress
_BfdSessLocalAddr_Object = MibTableColumn
bfdSessLocalAddr = _BfdSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 2, 1, 29),
    _BfdSessLocalAddr_Type()
)
bfdSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessLocalAddr.setStatus("current")
_DcBfdSessMapTable_Object = MibTable
dcBfdSessMapTable = _DcBfdSessMapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 5)
)
if mibBuilder.loadTexts:
    dcBfdSessMapTable.setStatus("current")
_DcBfdSessMapEntry_Object = MibTableRow
dcBfdSessMapEntry = _DcBfdSessMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 5, 1)
)
dcBfdSessMapEntry.setIndexNames(
    (0, "DC-BFD-STUB-MIB", "bfdEntityIndex"),
    (0, "DC-BFD-STUB-MIB", "bfdSessIntface"),
    (0, "DC-BFD-STUB-MIB", "bfdSessAddrType"),
    (0, "DC-BFD-STUB-MIB", "bfdSessAddr"),
    (0, "DC-BFD-STUB-MIB", "bfdSessRemoteDiscr"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessMapEntityType"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessMapEntityIndex"),
    (0, "DC-BFD-STUB-MIB", "bfdSessLocalAddrType"),
    (0, "DC-BFD-STUB-MIB", "bfdSessLocalAddr"),
)
if mibBuilder.loadTexts:
    dcBfdSessMapEntry.setStatus("current")
_DcBfdSessMapEntityType_Type = EntityProcType
_DcBfdSessMapEntityType_Object = MibTableColumn
dcBfdSessMapEntityType = _DcBfdSessMapEntityType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 5, 1, 1),
    _DcBfdSessMapEntityType_Type()
)
dcBfdSessMapEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessMapEntityType.setStatus("current")
_DcBfdSessMapEntityIndex_Type = Unsigned32
_DcBfdSessMapEntityIndex_Object = MibTableColumn
dcBfdSessMapEntityIndex = _DcBfdSessMapEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 5, 1, 2),
    _DcBfdSessMapEntityIndex_Type()
)
dcBfdSessMapEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessMapEntityIndex.setStatus("current")
_DcBfdSessMapBfdIndex_Type = BfdSessIndexTC
_DcBfdSessMapBfdIndex_Object = MibTableColumn
dcBfdSessMapBfdIndex = _DcBfdSessMapBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 5, 1, 3),
    _DcBfdSessMapBfdIndex_Type()
)
dcBfdSessMapBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBfdSessMapBfdIndex.setStatus("current")
_DcBfdSessConfigTable_Object = MibTable
dcBfdSessConfigTable = _DcBfdSessConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6)
)
if mibBuilder.loadTexts:
    dcBfdSessConfigTable.setStatus("current")
_DcBfdSessConfigEntry_Object = MibTableRow
dcBfdSessConfigEntry = _DcBfdSessConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1)
)
dcBfdSessConfigEntry.setIndexNames(
    (0, "DC-BFD-STUB-MIB", "bfdEntityIndex"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessConfigProtocol"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessConfigIfIndex"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessConfigAddrType"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessConfigAddr"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessConfigLocalAddrType"),
    (0, "DC-BFD-STUB-MIB", "dcBfdSessConfigLocalAddr"),
)
if mibBuilder.loadTexts:
    dcBfdSessConfigEntry.setStatus("current")


class _DcBfdSessConfigProtocol_Type(Bits):
    """Custom type dcBfdSessConfigProtocol based on Bits"""
    namedValues = NamedValues(
        *(("ospf", 0),
          ("isis", 1),
          ("bgp", 2),
          ("rip", 3),
          ("pim", 4),
          ("rsvp", 5),
          ("ldp", 6),
          ("lmp", 7),
          ("static", 8))
    )

_DcBfdSessConfigProtocol_Type.__name__ = "Bits"
_DcBfdSessConfigProtocol_Object = MibTableColumn
dcBfdSessConfigProtocol = _DcBfdSessConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 2),
    _DcBfdSessConfigProtocol_Type()
)
dcBfdSessConfigProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessConfigProtocol.setStatus("current")
_DcBfdSessConfigIfIndex_Type = InterfaceIndexOrZero
_DcBfdSessConfigIfIndex_Object = MibTableColumn
dcBfdSessConfigIfIndex = _DcBfdSessConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 3),
    _DcBfdSessConfigIfIndex_Type()
)
dcBfdSessConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessConfigIfIndex.setStatus("current")
_DcBfdSessConfigAddrType_Type = InetAddressType
_DcBfdSessConfigAddrType_Object = MibTableColumn
dcBfdSessConfigAddrType = _DcBfdSessConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 4),
    _DcBfdSessConfigAddrType_Type()
)
dcBfdSessConfigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessConfigAddrType.setStatus("current")


class _DcBfdSessConfigAddr_Type(InetAddress):
    """Custom type dcBfdSessConfigAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_DcBfdSessConfigAddr_Type.__name__ = "InetAddress"
_DcBfdSessConfigAddr_Object = MibTableColumn
dcBfdSessConfigAddr = _DcBfdSessConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 5),
    _DcBfdSessConfigAddr_Type()
)
dcBfdSessConfigAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessConfigAddr.setStatus("current")
_DcBfdSessConfigRowStatus_Type = RowStatus
_DcBfdSessConfigRowStatus_Object = MibTableColumn
dcBfdSessConfigRowStatus = _DcBfdSessConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 6),
    _DcBfdSessConfigRowStatus_Type()
)
dcBfdSessConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigRowStatus.setStatus("current")


class _DcBfdSessConfigDemandModeDsrd_Type(TruthValue):
    """Custom type dcBfdSessConfigDemandModeDsrd based on TruthValue"""
    defaultValue = 2


_DcBfdSessConfigDemandModeDsrd_Type.__name__ = "TruthValue"
_DcBfdSessConfigDemandModeDsrd_Object = MibTableColumn
dcBfdSessConfigDemandModeDsrd = _DcBfdSessConfigDemandModeDsrd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 7),
    _DcBfdSessConfigDemandModeDsrd_Type()
)
dcBfdSessConfigDemandModeDsrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigDemandModeDsrd.setStatus("current")


class _DcBfdSessConfigEchoFuncModeDsrd_Type(TruthValue):
    """Custom type dcBfdSessConfigEchoFuncModeDsrd based on TruthValue"""
    defaultValue = 2


_DcBfdSessConfigEchoFuncModeDsrd_Type.__name__ = "TruthValue"
_DcBfdSessConfigEchoFuncModeDsrd_Object = MibTableColumn
dcBfdSessConfigEchoFuncModeDsrd = _DcBfdSessConfigEchoFuncModeDsrd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 8),
    _DcBfdSessConfigEchoFuncModeDsrd_Type()
)
dcBfdSessConfigEchoFuncModeDsrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigEchoFuncModeDsrd.setStatus("current")


class _DcBfdSessConfigDesiredMinTxIntvl_Type(BfdInterval):
    """Custom type dcBfdSessConfigDesiredMinTxIntvl based on BfdInterval"""
    defaultValue = 150000


_DcBfdSessConfigDesiredMinTxIntvl_Type.__name__ = "BfdInterval"
_DcBfdSessConfigDesiredMinTxIntvl_Object = MibTableColumn
dcBfdSessConfigDesiredMinTxIntvl = _DcBfdSessConfigDesiredMinTxIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 9),
    _DcBfdSessConfigDesiredMinTxIntvl_Type()
)
dcBfdSessConfigDesiredMinTxIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigDesiredMinTxIntvl.setStatus("current")


class _DcBfdSessConfigReqMinRxInterval_Type(BfdInterval):
    """Custom type dcBfdSessConfigReqMinRxInterval based on BfdInterval"""
    defaultValue = 150000


_DcBfdSessConfigReqMinRxInterval_Type.__name__ = "BfdInterval"
_DcBfdSessConfigReqMinRxInterval_Object = MibTableColumn
dcBfdSessConfigReqMinRxInterval = _DcBfdSessConfigReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 10),
    _DcBfdSessConfigReqMinRxInterval_Type()
)
dcBfdSessConfigReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigReqMinRxInterval.setStatus("current")


class _DcBfdSessConfigReqMinEchoRxIntvl_Type(BfdInterval):
    """Custom type dcBfdSessConfigReqMinEchoRxIntvl based on BfdInterval"""
    defaultValue = 150000


_DcBfdSessConfigReqMinEchoRxIntvl_Type.__name__ = "BfdInterval"
_DcBfdSessConfigReqMinEchoRxIntvl_Object = MibTableColumn
dcBfdSessConfigReqMinEchoRxIntvl = _DcBfdSessConfigReqMinEchoRxIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 11),
    _DcBfdSessConfigReqMinEchoRxIntvl_Type()
)
dcBfdSessConfigReqMinEchoRxIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigReqMinEchoRxIntvl.setStatus("current")


class _DcBfdSessConfigDetectMult_Type(Unsigned32):
    """Custom type dcBfdSessConfigDetectMult based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DcBfdSessConfigDetectMult_Type.__name__ = "Unsigned32"
_DcBfdSessConfigDetectMult_Object = MibTableColumn
dcBfdSessConfigDetectMult = _DcBfdSessConfigDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 12),
    _DcBfdSessConfigDetectMult_Type()
)
dcBfdSessConfigDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcBfdSessConfigDetectMult.setStatus("current")
_DcBfdSessConfigLocalAddrType_Type = InetAddressType
_DcBfdSessConfigLocalAddrType_Object = MibTableColumn
dcBfdSessConfigLocalAddrType = _DcBfdSessConfigLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 13),
    _DcBfdSessConfigLocalAddrType_Type()
)
dcBfdSessConfigLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessConfigLocalAddrType.setStatus("current")
_DcBfdSessConfigLocalAddr_Type = InetAddress
_DcBfdSessConfigLocalAddr_Object = MibTableColumn
dcBfdSessConfigLocalAddr = _DcBfdSessConfigLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 1, 6, 1, 14),
    _DcBfdSessConfigLocalAddr_Type()
)
dcBfdSessConfigLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBfdSessConfigLocalAddr.setStatus("current")
_BfdConformance_ObjectIdentity = ObjectIdentity
bfdConformance = _BfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 3)
)
_BfdGroups_ObjectIdentity = ObjectIdentity
bfdGroups = _BfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 3, 1)
)
_BfdCompliances_ObjectIdentity = ObjectIdentity
bfdCompliances = _BfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 3, 2)
)

# Managed Objects groups

bfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 3, 1, 1)
)
bfdSessionGroup.setObjects(
      *(("DC-BFD-STUB-MIB", "bfdAdminStatus"),
        ("DC-BFD-STUB-MIB", "bfdOperStatus"),
        ("DC-BFD-STUB-MIB", "bfdRowStatus"),
        ("DC-BFD-STUB-MIB", "bfdDesiredMinTxInterval"),
        ("DC-BFD-STUB-MIB", "bfdReqMinRxInterval"),
        ("DC-BFD-STUB-MIB", "bfdInterfaceScope"),
        ("DC-BFD-STUB-MIB", "bfdVersionNumber"),
        ("DC-BFD-STUB-MIB", "bfdSessDiscriminator"),
        ("DC-BFD-STUB-MIB", "bfdSessIntface"),
        ("DC-BFD-STUB-MIB", "bfdSessAddrType"),
        ("DC-BFD-STUB-MIB", "bfdSessAddr"),
        ("DC-BFD-STUB-MIB", "bfdSessApplicationSessions"),
        ("DC-BFD-STUB-MIB", "bfdSessRemoteDiscr"),
        ("DC-BFD-STUB-MIB", "bfdSessLocalAddrType"),
        ("DC-BFD-STUB-MIB", "bfdSessLocalAddr"),
        ("DC-BFD-STUB-MIB", "bfdSessState"),
        ("DC-BFD-STUB-MIB", "bfdSessDiag"),
        ("DC-BFD-STUB-MIB", "bfdSessControlPlanIndepFlag"),
        ("DC-BFD-STUB-MIB", "dcBfdSessMapBfdIndex"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigRowStatus"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigDemandModeDsrd"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigEchoFuncModeDsrd"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigDesiredMinTxIntvl"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigReqMinRxInterval"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigReqMinEchoRxIntvl"),
        ("DC-BFD-STUB-MIB", "dcBfdSessConfigDetectMult"))
)
if mibBuilder.loadTexts:
    bfdSessionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 11, 3, 2, 1)
)
bfdModuleFullCompliance.setObjects(
    ("DC-BFD-STUB-MIB", "bfdSessionGroup")
)
if mibBuilder.loadTexts:
    bfdModuleFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-BFD-STUB-MIB",
    **{"BfdSessIndexTC": BfdSessIndexTC,
       "BfdInterval": BfdInterval,
       "BfdDiag": BfdDiag,
       "nbase": nbase,
       "opx": opx,
       "bfdMIB": bfdMIB,
       "bfdNotifications": bfdNotifications,
       "bfdObjects": bfdObjects,
       "bfdEntityTable": bfdEntityTable,
       "bfdEntityEntry": bfdEntityEntry,
       "bfdEntityIndex": bfdEntityIndex,
       "bfdAdminStatus": bfdAdminStatus,
       "bfdOperStatus": bfdOperStatus,
       "bfdRowStatus": bfdRowStatus,
       "bfdVersionNumber": bfdVersionNumber,
       "bfdDesiredMinTxInterval": bfdDesiredMinTxInterval,
       "bfdReqMinRxInterval": bfdReqMinRxInterval,
       "bfdInterfaceScope": bfdInterfaceScope,
       "bfdSessionTable": bfdSessionTable,
       "bfdSessionEntry": bfdSessionEntry,
       "bfdSessIndex": bfdSessIndex,
       "bfdSessDiscriminator": bfdSessDiscriminator,
       "bfdSessRemoteDiscr": bfdSessRemoteDiscr,
       "bfdSessState": bfdSessState,
       "bfdSessDiag": bfdSessDiag,
       "bfdSessControlPlanIndepFlag": bfdSessControlPlanIndepFlag,
       "bfdSessIntface": bfdSessIntface,
       "bfdSessAddrType": bfdSessAddrType,
       "bfdSessAddr": bfdSessAddr,
       "bfdSessApplicationSessions": bfdSessApplicationSessions,
       "bfdSessLocalAddrType": bfdSessLocalAddrType,
       "bfdSessLocalAddr": bfdSessLocalAddr,
       "dcBfdSessMapTable": dcBfdSessMapTable,
       "dcBfdSessMapEntry": dcBfdSessMapEntry,
       "dcBfdSessMapEntityType": dcBfdSessMapEntityType,
       "dcBfdSessMapEntityIndex": dcBfdSessMapEntityIndex,
       "dcBfdSessMapBfdIndex": dcBfdSessMapBfdIndex,
       "dcBfdSessConfigTable": dcBfdSessConfigTable,
       "dcBfdSessConfigEntry": dcBfdSessConfigEntry,
       "dcBfdSessConfigProtocol": dcBfdSessConfigProtocol,
       "dcBfdSessConfigIfIndex": dcBfdSessConfigIfIndex,
       "dcBfdSessConfigAddrType": dcBfdSessConfigAddrType,
       "dcBfdSessConfigAddr": dcBfdSessConfigAddr,
       "dcBfdSessConfigRowStatus": dcBfdSessConfigRowStatus,
       "dcBfdSessConfigDemandModeDsrd": dcBfdSessConfigDemandModeDsrd,
       "dcBfdSessConfigEchoFuncModeDsrd": dcBfdSessConfigEchoFuncModeDsrd,
       "dcBfdSessConfigDesiredMinTxIntvl": dcBfdSessConfigDesiredMinTxIntvl,
       "dcBfdSessConfigReqMinRxInterval": dcBfdSessConfigReqMinRxInterval,
       "dcBfdSessConfigReqMinEchoRxIntvl": dcBfdSessConfigReqMinEchoRxIntvl,
       "dcBfdSessConfigDetectMult": dcBfdSessConfigDetectMult,
       "dcBfdSessConfigLocalAddrType": dcBfdSessConfigLocalAddrType,
       "dcBfdSessConfigLocalAddr": dcBfdSessConfigLocalAddr,
       "bfdConformance": bfdConformance,
       "bfdGroups": bfdGroups,
       "bfdSessionGroup": bfdSessionGroup,
       "bfdCompliances": bfdCompliances,
       "bfdModuleFullCompliance": bfdModuleFullCompliance}
)
