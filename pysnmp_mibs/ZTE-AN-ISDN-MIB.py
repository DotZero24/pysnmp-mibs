# SNMP MIB module (ZTE-AN-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ISDN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:27 2025
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

zxAnISDNMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_MsagmajorVersion_ObjectIdentity = ObjectIdentity
msagmajorVersion = _MsagmajorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_MsagISDNService_ObjectIdentity = ObjectIdentity
msagISDNService = _MsagISDNService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4)
)
_IsdnAppServerTable_Object = MibTable
isdnAppServerTable = _IsdnAppServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1)
)
if mibBuilder.loadTexts:
    isdnAppServerTable.setStatus("current")
_IsdnAppServerEntry_Object = MibTableRow
isdnAppServerEntry = _IsdnAppServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1)
)
isdnAppServerEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "isdnAppServerID"),
)
if mibBuilder.loadTexts:
    isdnAppServerEntry.setStatus("current")


class _IsdnAppServerID_Type(Integer32):
    """Custom type isdnAppServerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IsdnAppServerID_Type.__name__ = "Integer32"
_IsdnAppServerID_Object = MibTableColumn
isdnAppServerID = _IsdnAppServerID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1, 1),
    _IsdnAppServerID_Type()
)
isdnAppServerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnAppServerID.setStatus("current")


class _IsdnAppServerProtocol_Type(Integer32):
    """Custom type isdnAppServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tpM3UA", 1),
          ("tpM2UA", 2),
          ("tpM2PA", 3),
          ("tpSUA", 4),
          ("tpIUA", 5),
          ("tpV5UA", 6))
    )


_IsdnAppServerProtocol_Type.__name__ = "Integer32"
_IsdnAppServerProtocol_Object = MibTableColumn
isdnAppServerProtocol = _IsdnAppServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1, 2),
    _IsdnAppServerProtocol_Type()
)
isdnAppServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnAppServerProtocol.setStatus("current")


class _IsdnAppServerMode_Type(Integer32):
    """Custom type isdnAppServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("masterSlave", 1),
          ("share", 2),
          ("broadcast", 3))
    )


_IsdnAppServerMode_Type.__name__ = "Integer32"
_IsdnAppServerMode_Object = MibTableColumn
isdnAppServerMode = _IsdnAppServerMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1, 3),
    _IsdnAppServerMode_Type()
)
isdnAppServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnAppServerMode.setStatus("current")


class _IsdnAppServerModeEval_Type(Integer32):
    """Custom type isdnAppServerModeEval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnAppServerModeEval_Type.__name__ = "Integer32"
_IsdnAppServerModeEval_Object = MibTableColumn
isdnAppServerModeEval = _IsdnAppServerModeEval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1, 4),
    _IsdnAppServerModeEval_Type()
)
isdnAppServerModeEval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnAppServerModeEval.setStatus("current")


class _IsdnAppServerStatus_Type(Integer32):
    """Custom type isdnAppServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("inactive", 1),
          ("active", 2),
          ("pending", 4))
    )


_IsdnAppServerStatus_Type.__name__ = "Integer32"
_IsdnAppServerStatus_Object = MibTableColumn
isdnAppServerStatus = _IsdnAppServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1, 5),
    _IsdnAppServerStatus_Type()
)
isdnAppServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnAppServerStatus.setStatus("current")
_IsdnAppServerRowStatus_Type = RowStatus
_IsdnAppServerRowStatus_Object = MibTableColumn
isdnAppServerRowStatus = _IsdnAppServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 1, 1, 6),
    _IsdnAppServerRowStatus_Type()
)
isdnAppServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnAppServerRowStatus.setStatus("current")
_IsdnAppServerProcTable_Object = MibTable
isdnAppServerProcTable = _IsdnAppServerProcTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2)
)
if mibBuilder.loadTexts:
    isdnAppServerProcTable.setStatus("current")
_IsdnAppServerProcEntry_Object = MibTableRow
isdnAppServerProcEntry = _IsdnAppServerProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1)
)
isdnAppServerProcEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "isdnASPID"),
)
if mibBuilder.loadTexts:
    isdnAppServerProcEntry.setStatus("current")


class _IsdnASPID_Type(Integer32):
    """Custom type isdnASPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IsdnASPID_Type.__name__ = "Integer32"
_IsdnASPID_Object = MibTableColumn
isdnASPID = _IsdnASPID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 1),
    _IsdnASPID_Type()
)
isdnASPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnASPID.setStatus("current")


class _IsdnASPDestPort_Type(Integer32):
    """Custom type isdnASPDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnASPDestPort_Type.__name__ = "Integer32"
_IsdnASPDestPort_Object = MibTableColumn
isdnASPDestPort = _IsdnASPDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 2),
    _IsdnASPDestPort_Type()
)
isdnASPDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPDestPort.setStatus("current")


class _IsdnASPLoclPort_Type(Integer32):
    """Custom type isdnASPLoclPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnASPLoclPort_Type.__name__ = "Integer32"
_IsdnASPLoclPort_Object = MibTableColumn
isdnASPLoclPort = _IsdnASPLoclPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 3),
    _IsdnASPLoclPort_Type()
)
isdnASPLoclPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPLoclPort.setStatus("current")
_IsdnASPSctpID_Type = Integer32
_IsdnASPSctpID_Object = MibTableColumn
isdnASPSctpID = _IsdnASPSctpID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 4),
    _IsdnASPSctpID_Type()
)
isdnASPSctpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnASPSctpID.setStatus("current")


class _IsdnASPUpProto_Type(Integer32):
    """Custom type isdnASPUpProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("iua", 5)
    )


_IsdnASPUpProto_Type.__name__ = "Integer32"
_IsdnASPUpProto_Object = MibTableColumn
isdnASPUpProto = _IsdnASPUpProto_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 5),
    _IsdnASPUpProto_Type()
)
isdnASPUpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnASPUpProto.setStatus("current")


class _IsdnASPDownProto_Type(Integer32):
    """Custom type isdnASPDownProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("ip", 2))
    )


_IsdnASPDownProto_Type.__name__ = "Integer32"
_IsdnASPDownProto_Object = MibTableColumn
isdnASPDownProto = _IsdnASPDownProto_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 6),
    _IsdnASPDownProto_Type()
)
isdnASPDownProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPDownProto.setStatus("current")
_IsdnASPDestIP_Type = IpAddress
_IsdnASPDestIP_Object = MibTableColumn
isdnASPDestIP = _IsdnASPDestIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 7),
    _IsdnASPDestIP_Type()
)
isdnASPDestIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPDestIP.setStatus("current")


class _IsdnASPInStream_Type(Integer32):
    """Custom type isdnASPInStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IsdnASPInStream_Type.__name__ = "Integer32"
_IsdnASPInStream_Object = MibTableColumn
isdnASPInStream = _IsdnASPInStream_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 8),
    _IsdnASPInStream_Type()
)
isdnASPInStream.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPInStream.setStatus("current")


class _IsdnASPOutStream_Type(Integer32):
    """Custom type isdnASPOutStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IsdnASPOutStream_Type.__name__ = "Integer32"
_IsdnASPOutStream_Object = MibTableColumn
isdnASPOutStream = _IsdnASPOutStream_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 9),
    _IsdnASPOutStream_Type()
)
isdnASPOutStream.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPOutStream.setStatus("current")


class _IsdnASPStat_Type(Integer32):
    """Custom type isdnASPStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("aspLost", 0),
          ("aspDown", 1),
          ("aspInactive", 2),
          ("aspActive", 4),
          ("aspStandby", 8),
          ("aspManual", 64),
          ("aspCongest", 128))
    )


_IsdnASPStat_Type.__name__ = "Integer32"
_IsdnASPStat_Object = MibTableColumn
isdnASPStat = _IsdnASPStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 10),
    _IsdnASPStat_Type()
)
isdnASPStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnASPStat.setStatus("current")
_IsdnASPModule_Type = Integer32
_IsdnASPModule_Object = MibTableColumn
isdnASPModule = _IsdnASPModule_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 11),
    _IsdnASPModule_Type()
)
isdnASPModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnASPModule.setStatus("current")


class _IsdnASPClieOrServ_Type(Integer32):
    """Custom type isdnASPClieOrServ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_IsdnASPClieOrServ_Type.__name__ = "Integer32"
_IsdnASPClieOrServ_Object = MibTableColumn
isdnASPClieOrServ = _IsdnASPClieOrServ_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 12),
    _IsdnASPClieOrServ_Type()
)
isdnASPClieOrServ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnASPClieOrServ.setStatus("current")
_IsdnASPRowStatus_Type = RowStatus
_IsdnASPRowStatus_Object = MibTableColumn
isdnASPRowStatus = _IsdnASPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 2, 1, 14),
    _IsdnASPRowStatus_Type()
)
isdnASPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnASPRowStatus.setStatus("current")
_IsdnASASPRelationTable_Object = MibTable
isdnASASPRelationTable = _IsdnASASPRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 3)
)
if mibBuilder.loadTexts:
    isdnASASPRelationTable.setStatus("current")
_IsdnASASPRelationEntry_Object = MibTableRow
isdnASASPRelationEntry = _IsdnASASPRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 3, 1)
)
isdnASASPRelationEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "isdnAARASPID"),
    (0, "ZTE-AN-ISDN-MIB", "isdnAARASID"),
)
if mibBuilder.loadTexts:
    isdnASASPRelationEntry.setStatus("current")


class _IsdnAARASPID_Type(Integer32):
    """Custom type isdnAARASPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IsdnAARASPID_Type.__name__ = "Integer32"
_IsdnAARASPID_Object = MibTableColumn
isdnAARASPID = _IsdnAARASPID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 3, 1, 1),
    _IsdnAARASPID_Type()
)
isdnAARASPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnAARASPID.setStatus("current")


class _IsdnAARASID_Type(Integer32):
    """Custom type isdnAARASID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IsdnAARASID_Type.__name__ = "Integer32"
_IsdnAARASID_Object = MibTableColumn
isdnAARASID = _IsdnAARASID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 3, 1, 2),
    _IsdnAARASID_Type()
)
isdnAARASID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnAARASID.setStatus("current")


class _IsdnAARQueue_Type(Integer32):
    """Custom type isdnAARQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aspInit", 0),
          ("aspDown", 1),
          ("aspUp", 2),
          ("aspActive", 4))
    )


_IsdnAARQueue_Type.__name__ = "Integer32"
_IsdnAARQueue_Object = MibTableColumn
isdnAARQueue = _IsdnAARQueue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 3, 1, 3),
    _IsdnAARQueue_Type()
)
isdnAARQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnAARQueue.setStatus("current")
_IsdnAARRowStatus_Type = RowStatus
_IsdnAARRowStatus_Object = MibTableColumn
isdnAARRowStatus = _IsdnAARRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 3, 1, 4),
    _IsdnAARRowStatus_Type()
)
isdnAARRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnAARRowStatus.setStatus("current")
_IsdnDLinkTable_Object = MibTable
isdnDLinkTable = _IsdnDLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4)
)
if mibBuilder.loadTexts:
    isdnDLinkTable.setStatus("current")
_IsdnDLinkEntry_Object = MibTableRow
isdnDLinkEntry = _IsdnDLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1)
)
isdnDLinkEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "isdnDLinkRack"),
    (0, "ZTE-AN-ISDN-MIB", "isdnDLinkShelf"),
    (0, "ZTE-AN-ISDN-MIB", "isdnDLinkSlot"),
    (0, "ZTE-AN-ISDN-MIB", "isdnDLinkPCMNo"),
    (0, "ZTE-AN-ISDN-MIB", "isdnDLinkLinkIdx"),
)
if mibBuilder.loadTexts:
    isdnDLinkEntry.setStatus("current")
_IsdnDLinkRack_Type = Integer32
_IsdnDLinkRack_Object = MibTableColumn
isdnDLinkRack = _IsdnDLinkRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 1),
    _IsdnDLinkRack_Type()
)
isdnDLinkRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnDLinkRack.setStatus("current")
_IsdnDLinkShelf_Type = Integer32
_IsdnDLinkShelf_Object = MibTableColumn
isdnDLinkShelf = _IsdnDLinkShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 2),
    _IsdnDLinkShelf_Type()
)
isdnDLinkShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnDLinkShelf.setStatus("current")
_IsdnDLinkSlot_Type = Integer32
_IsdnDLinkSlot_Object = MibTableColumn
isdnDLinkSlot = _IsdnDLinkSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 3),
    _IsdnDLinkSlot_Type()
)
isdnDLinkSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnDLinkSlot.setStatus("current")


class _IsdnDLinkPCMNo_Type(Integer32):
    """Custom type isdnDLinkPCMNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IsdnDLinkPCMNo_Type.__name__ = "Integer32"
_IsdnDLinkPCMNo_Object = MibTableColumn
isdnDLinkPCMNo = _IsdnDLinkPCMNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 4),
    _IsdnDLinkPCMNo_Type()
)
isdnDLinkPCMNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnDLinkPCMNo.setStatus("current")


class _IsdnDLinkLinkIdx_Type(Integer32):
    """Custom type isdnDLinkLinkIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IsdnDLinkLinkIdx_Type.__name__ = "Integer32"
_IsdnDLinkLinkIdx_Object = MibTableColumn
isdnDLinkLinkIdx = _IsdnDLinkLinkIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 5),
    _IsdnDLinkLinkIdx_Type()
)
isdnDLinkLinkIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnDLinkLinkIdx.setStatus("current")


class _IsdnDLinkIfID_Type(Integer32):
    """Custom type isdnDLinkIfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnDLinkIfID_Type.__name__ = "Integer32"
_IsdnDLinkIfID_Object = MibTableColumn
isdnDLinkIfID = _IsdnDLinkIfID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 6),
    _IsdnDLinkIfID_Type()
)
isdnDLinkIfID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDLinkIfID.setStatus("current")


class _IsdnDLinkLinkID_Type(Integer32):
    """Custom type isdnDLinkLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_IsdnDLinkLinkID_Type.__name__ = "Integer32"
_IsdnDLinkLinkID_Object = MibTableColumn
isdnDLinkLinkID = _IsdnDLinkLinkID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 7),
    _IsdnDLinkLinkID_Type()
)
isdnDLinkLinkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDLinkLinkID.setStatus("current")


class _IsdnDLinkLinkInfo_Type(Integer32):
    """Custom type isdnDLinkLinkInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 0),
          ("subscriberSide", 1))
    )


_IsdnDLinkLinkInfo_Type.__name__ = "Integer32"
_IsdnDLinkLinkInfo_Object = MibTableColumn
isdnDLinkLinkInfo = _IsdnDLinkLinkInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 8),
    _IsdnDLinkLinkInfo_Type()
)
isdnDLinkLinkInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDLinkLinkInfo.setStatus("current")


class _IsdnDLinkASID_Type(Integer32):
    """Custom type isdnDLinkASID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IsdnDLinkASID_Type.__name__ = "Integer32"
_IsdnDLinkASID_Object = MibTableColumn
isdnDLinkASID = _IsdnDLinkASID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 9),
    _IsdnDLinkASID_Type()
)
isdnDLinkASID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDLinkASID.setStatus("current")


class _IsdnDLinkNumber_Type(Integer32):
    """Custom type isdnDLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IsdnDLinkNumber_Type.__name__ = "Integer32"
_IsdnDLinkNumber_Object = MibTableColumn
isdnDLinkNumber = _IsdnDLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 10),
    _IsdnDLinkNumber_Type()
)
isdnDLinkNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDLinkNumber.setStatus("current")


class _IsdnDLinkProtocol_Type(Integer32):
    """Custom type isdnDLinkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ptl2BplusD", 1),
          ("ptl30BplusD", 2),
          ("ptl23BplusD", 3))
    )


_IsdnDLinkProtocol_Type.__name__ = "Integer32"
_IsdnDLinkProtocol_Object = MibTableColumn
isdnDLinkProtocol = _IsdnDLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 11),
    _IsdnDLinkProtocol_Type()
)
isdnDLinkProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDLinkProtocol.setStatus("current")
_IsdnDLinkStatus_Type = Integer32
_IsdnDLinkStatus_Object = MibTableColumn
isdnDLinkStatus = _IsdnDLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 12),
    _IsdnDLinkStatus_Type()
)
isdnDLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDLinkStatus.setStatus("current")
_IsdnDLinkRowStatus_Type = RowStatus
_IsdnDLinkRowStatus_Object = MibTableColumn
isdnDLinkRowStatus = _IsdnDLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 4, 1, 13),
    _IsdnDLinkRowStatus_Type()
)
isdnDLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDLinkRowStatus.setStatus("current")
_LoopbackTable_Object = MibTable
loopbackTable = _LoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6)
)
if mibBuilder.loadTexts:
    loopbackTable.setStatus("current")
_LoopbackEntry_Object = MibTableRow
loopbackEntry = _LoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6, 1)
)
loopbackEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "loopbackrack"),
    (0, "ZTE-AN-ISDN-MIB", "loopbackshelf"),
    (0, "ZTE-AN-ISDN-MIB", "loopbackslot"),
    (0, "ZTE-AN-ISDN-MIB", "loopbackportno"),
)
if mibBuilder.loadTexts:
    loopbackEntry.setStatus("current")
_Loopbackrack_Type = Integer32
_Loopbackrack_Object = MibTableColumn
loopbackrack = _Loopbackrack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6, 1, 1),
    _Loopbackrack_Type()
)
loopbackrack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loopbackrack.setStatus("current")
_Loopbackshelf_Type = Integer32
_Loopbackshelf_Object = MibTableColumn
loopbackshelf = _Loopbackshelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6, 1, 2),
    _Loopbackshelf_Type()
)
loopbackshelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loopbackshelf.setStatus("current")
_Loopbackslot_Type = Integer32
_Loopbackslot_Object = MibTableColumn
loopbackslot = _Loopbackslot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6, 1, 3),
    _Loopbackslot_Type()
)
loopbackslot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loopbackslot.setStatus("current")
_Loopbackportno_Type = Integer32
_Loopbackportno_Object = MibTableColumn
loopbackportno = _Loopbackportno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6, 1, 4),
    _Loopbackportno_Type()
)
loopbackportno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loopbackportno.setStatus("current")


class _Loopbacklooptype_Type(Integer32):
    """Custom type loopbacklooptype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localLoopback", 1),
          ("remoteLineLoopback", 2),
          ("noLoopback", 3))
    )


_Loopbacklooptype_Type.__name__ = "Integer32"
_Loopbacklooptype_Object = MibTableColumn
loopbacklooptype = _Loopbacklooptype_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 6, 1, 5),
    _Loopbacklooptype_Type()
)
loopbacklooptype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbacklooptype.setStatus("current")
_MsagIsdnCapabilityTable_Object = MibTable
msagIsdnCapabilityTable = _MsagIsdnCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7)
)
if mibBuilder.loadTexts:
    msagIsdnCapabilityTable.setStatus("current")
_MsagIsdnCapabilityEntry_Object = MibTableRow
msagIsdnCapabilityEntry = _MsagIsdnCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1)
)
msagIsdnCapabilityEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "isdnkrack"),
    (0, "ZTE-AN-ISDN-MIB", "isdnshelf"),
    (0, "ZTE-AN-ISDN-MIB", "isdnslot"),
    (0, "ZTE-AN-ISDN-MIB", "isdnportno"),
)
if mibBuilder.loadTexts:
    msagIsdnCapabilityEntry.setStatus("current")


class _Isdnkrack_Type(Integer32):
    """Custom type isdnkrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Isdnkrack_Type.__name__ = "Integer32"
_Isdnkrack_Object = MibTableColumn
isdnkrack = _Isdnkrack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 1),
    _Isdnkrack_Type()
)
isdnkrack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnkrack.setStatus("current")


class _Isdnshelf_Type(Integer32):
    """Custom type isdnshelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Isdnshelf_Type.__name__ = "Integer32"
_Isdnshelf_Object = MibTableColumn
isdnshelf = _Isdnshelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 2),
    _Isdnshelf_Type()
)
isdnshelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnshelf.setStatus("current")


class _Isdnslot_Type(Integer32):
    """Custom type isdnslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_Isdnslot_Type.__name__ = "Integer32"
_Isdnslot_Object = MibTableColumn
isdnslot = _Isdnslot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 3),
    _Isdnslot_Type()
)
isdnslot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnslot.setStatus("current")


class _Isdnportno_Type(Integer32):
    """Custom type isdnportno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Isdnportno_Type.__name__ = "Integer32"
_Isdnportno_Object = MibTableColumn
isdnportno = _Isdnportno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 4),
    _Isdnportno_Type()
)
isdnportno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnportno.setStatus("current")


class _IsdnLossOfSignal_Type(Unsigned32):
    """Custom type isdnLossOfSignal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsdnLossOfSignal_Type.__name__ = "Unsigned32"
_IsdnLossOfSignal_Object = MibTableColumn
isdnLossOfSignal = _IsdnLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 20),
    _IsdnLossOfSignal_Type()
)
isdnLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLossOfSignal.setStatus("current")


class _IsdnLossOfPower_Type(Unsigned32):
    """Custom type isdnLossOfPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsdnLossOfPower_Type.__name__ = "Unsigned32"
_IsdnLossOfPower_Object = MibTableColumn
isdnLossOfPower = _IsdnLossOfPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 21),
    _IsdnLossOfPower_Type()
)
isdnLossOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLossOfPower.setStatus("current")


class _IsdnLossOfFrame_Type(Unsigned32):
    """Custom type isdnLossOfFrame based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsdnLossOfFrame_Type.__name__ = "Unsigned32"
_IsdnLossOfFrame_Object = MibTableColumn
isdnLossOfFrame = _IsdnLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 22),
    _IsdnLossOfFrame_Type()
)
isdnLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLossOfFrame.setStatus("current")


class _IsdnClear_Type(Integer32):
    """Custom type isdnClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IsdnClear_Type.__name__ = "Integer32"
_IsdnClear_Object = MibTableColumn
isdnClear = _IsdnClear_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 7, 1, 23),
    _IsdnClear_Type()
)
isdnClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnClear.setStatus("current")
_ZxAnIsdnPortActiveStatusTable_Object = MibTable
zxAnIsdnPortActiveStatusTable = _ZxAnIsdnPortActiveStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8)
)
if mibBuilder.loadTexts:
    zxAnIsdnPortActiveStatusTable.setStatus("current")
_ZxAnIsdnPortActiveStatusEntry_Object = MibTableRow
zxAnIsdnPortActiveStatusEntry = _ZxAnIsdnPortActiveStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1)
)
zxAnIsdnPortActiveStatusEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnPortRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnPortShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnPortSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnPortNo"),
)
if mibBuilder.loadTexts:
    zxAnIsdnPortActiveStatusEntry.setStatus("current")
_ZxAnIsdnPortRack_Type = Integer32
_ZxAnIsdnPortRack_Object = MibTableColumn
zxAnIsdnPortRack = _ZxAnIsdnPortRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1, 1),
    _ZxAnIsdnPortRack_Type()
)
zxAnIsdnPortRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnPortRack.setStatus("current")
_ZxAnIsdnPortShelf_Type = Integer32
_ZxAnIsdnPortShelf_Object = MibTableColumn
zxAnIsdnPortShelf = _ZxAnIsdnPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1, 2),
    _ZxAnIsdnPortShelf_Type()
)
zxAnIsdnPortShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnPortShelf.setStatus("current")
_ZxAnIsdnPortSlot_Type = Integer32
_ZxAnIsdnPortSlot_Object = MibTableColumn
zxAnIsdnPortSlot = _ZxAnIsdnPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1, 3),
    _ZxAnIsdnPortSlot_Type()
)
zxAnIsdnPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnPortSlot.setStatus("current")
_ZxAnIsdnPortNo_Type = Integer32
_ZxAnIsdnPortNo_Object = MibTableColumn
zxAnIsdnPortNo = _ZxAnIsdnPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1, 4),
    _ZxAnIsdnPortNo_Type()
)
zxAnIsdnPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnPortNo.setStatus("current")


class _ZxAnIsdnPortL1ActiveStatus_Type(Integer32):
    """Custom type zxAnIsdnPortL1ActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keepActive", 0),
          ("notKeepActive", 1))
    )


_ZxAnIsdnPortL1ActiveStatus_Type.__name__ = "Integer32"
_ZxAnIsdnPortL1ActiveStatus_Object = MibTableColumn
zxAnIsdnPortL1ActiveStatus = _ZxAnIsdnPortL1ActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1, 5),
    _ZxAnIsdnPortL1ActiveStatus_Type()
)
zxAnIsdnPortL1ActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnPortL1ActiveStatus.setStatus("current")


class _ZxAnIsdnPortL2ActiveStatus_Type(Integer32):
    """Custom type zxAnIsdnPortL2ActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keepActive", 1),
          ("notKeepActive", 2))
    )


_ZxAnIsdnPortL2ActiveStatus_Type.__name__ = "Integer32"
_ZxAnIsdnPortL2ActiveStatus_Object = MibTableColumn
zxAnIsdnPortL2ActiveStatus = _ZxAnIsdnPortL2ActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 8, 1, 6),
    _ZxAnIsdnPortL2ActiveStatus_Type()
)
zxAnIsdnPortL2ActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnPortL2ActiveStatus.setStatus("current")
_ZxAnIsdnUIfCfgTable_Object = MibTable
zxAnIsdnUIfCfgTable = _ZxAnIsdnUIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9)
)
if mibBuilder.loadTexts:
    zxAnIsdnUIfCfgTable.setStatus("current")
_ZxAnIsdnUIfCfgEntry_Object = MibTableRow
zxAnIsdnUIfCfgEntry = _ZxAnIsdnUIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1)
)
zxAnIsdnUIfCfgEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnUIfRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnUIfShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnUIfSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnUIfNo"),
)
if mibBuilder.loadTexts:
    zxAnIsdnUIfCfgEntry.setStatus("current")
_ZxAnIsdnUIfRack_Type = Integer32
_ZxAnIsdnUIfRack_Object = MibTableColumn
zxAnIsdnUIfRack = _ZxAnIsdnUIfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 1),
    _ZxAnIsdnUIfRack_Type()
)
zxAnIsdnUIfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnUIfRack.setStatus("current")
_ZxAnIsdnUIfShelf_Type = Integer32
_ZxAnIsdnUIfShelf_Object = MibTableColumn
zxAnIsdnUIfShelf = _ZxAnIsdnUIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 2),
    _ZxAnIsdnUIfShelf_Type()
)
zxAnIsdnUIfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnUIfShelf.setStatus("current")
_ZxAnIsdnUIfSlot_Type = Integer32
_ZxAnIsdnUIfSlot_Object = MibTableColumn
zxAnIsdnUIfSlot = _ZxAnIsdnUIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 3),
    _ZxAnIsdnUIfSlot_Type()
)
zxAnIsdnUIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnUIfSlot.setStatus("current")
_ZxAnIsdnUIfNo_Type = Integer32
_ZxAnIsdnUIfNo_Object = MibTableColumn
zxAnIsdnUIfNo = _ZxAnIsdnUIfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 4),
    _ZxAnIsdnUIfNo_Type()
)
zxAnIsdnUIfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnUIfNo.setStatus("current")


class _ZxAnIsdnUIfRemotePowerFeedEnable_Type(Integer32):
    """Custom type zxAnIsdnUIfRemotePowerFeedEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnIsdnUIfRemotePowerFeedEnable_Type.__name__ = "Integer32"
_ZxAnIsdnUIfRemotePowerFeedEnable_Object = MibTableColumn
zxAnIsdnUIfRemotePowerFeedEnable = _ZxAnIsdnUIfRemotePowerFeedEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 5),
    _ZxAnIsdnUIfRemotePowerFeedEnable_Type()
)
zxAnIsdnUIfRemotePowerFeedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnUIfRemotePowerFeedEnable.setStatus("current")


class _ZxAnIsdnUIfTrapEnable_Type(Integer32):
    """Custom type zxAnIsdnUIfTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnIsdnUIfTrapEnable_Type.__name__ = "Integer32"
_ZxAnIsdnUIfTrapEnable_Object = MibTableColumn
zxAnIsdnUIfTrapEnable = _ZxAnIsdnUIfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 6),
    _ZxAnIsdnUIfTrapEnable_Type()
)
zxAnIsdnUIfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnUIfTrapEnable.setStatus("current")


class _ZxAnIsdnUIfActiveStatus_Type(Integer32):
    """Custom type zxAnIsdnUIfActiveStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ZxAnIsdnUIfActiveStatus_Type.__name__ = "Integer32"
_ZxAnIsdnUIfActiveStatus_Object = MibTableColumn
zxAnIsdnUIfActiveStatus = _ZxAnIsdnUIfActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 7),
    _ZxAnIsdnUIfActiveStatus_Type()
)
zxAnIsdnUIfActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnUIfActiveStatus.setStatus("current")


class _ZxAnIsdnUIfSoftReset_Type(Integer32):
    """Custom type zxAnIsdnUIfSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZxAnIsdnUIfSoftReset_Type.__name__ = "Integer32"
_ZxAnIsdnUIfSoftReset_Object = MibTableColumn
zxAnIsdnUIfSoftReset = _ZxAnIsdnUIfSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 8),
    _ZxAnIsdnUIfSoftReset_Type()
)
zxAnIsdnUIfSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnUIfSoftReset.setStatus("current")


class _ZxAnIsdnUIfAbnormalReason_Type(Integer32):
    """Custom type zxAnIsdnUIfAbnormalReason based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("errorIndication2", 1),
          ("errorIndication3", 2),
          ("lossOfSignalLevel", 3),
          ("reSyncIndication", 4),
          ("frameJump", 5),
          ("uIfActivationIndication", 6),
          ("uIfdeactivationIndication", 7),
          ("other", 255))
    )


_ZxAnIsdnUIfAbnormalReason_Type.__name__ = "Integer32"
_ZxAnIsdnUIfAbnormalReason_Object = MibTableColumn
zxAnIsdnUIfAbnormalReason = _ZxAnIsdnUIfAbnormalReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 9, 1, 9),
    _ZxAnIsdnUIfAbnormalReason_Type()
)
zxAnIsdnUIfAbnormalReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnUIfAbnormalReason.setStatus("current")
_ZxAnIsdnSIfCfgTable_Object = MibTable
zxAnIsdnSIfCfgTable = _ZxAnIsdnSIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10)
)
if mibBuilder.loadTexts:
    zxAnIsdnSIfCfgTable.setStatus("current")
_ZxAnIsdnSIfCfgEntry_Object = MibTableRow
zxAnIsdnSIfCfgEntry = _ZxAnIsdnSIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1)
)
zxAnIsdnSIfCfgEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnSIfRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnSIfShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnSIfSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnSIfNo"),
)
if mibBuilder.loadTexts:
    zxAnIsdnSIfCfgEntry.setStatus("current")
_ZxAnIsdnSIfRack_Type = Integer32
_ZxAnIsdnSIfRack_Object = MibTableColumn
zxAnIsdnSIfRack = _ZxAnIsdnSIfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 1),
    _ZxAnIsdnSIfRack_Type()
)
zxAnIsdnSIfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnSIfRack.setStatus("current")
_ZxAnIsdnSIfShelf_Type = Integer32
_ZxAnIsdnSIfShelf_Object = MibTableColumn
zxAnIsdnSIfShelf = _ZxAnIsdnSIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 2),
    _ZxAnIsdnSIfShelf_Type()
)
zxAnIsdnSIfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnSIfShelf.setStatus("current")
_ZxAnIsdnSIfSlot_Type = Integer32
_ZxAnIsdnSIfSlot_Object = MibTableColumn
zxAnIsdnSIfSlot = _ZxAnIsdnSIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 3),
    _ZxAnIsdnSIfSlot_Type()
)
zxAnIsdnSIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnSIfSlot.setStatus("current")
_ZxAnIsdnSIfNo_Type = Integer32
_ZxAnIsdnSIfNo_Object = MibTableColumn
zxAnIsdnSIfNo = _ZxAnIsdnSIfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 4),
    _ZxAnIsdnSIfNo_Type()
)
zxAnIsdnSIfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnSIfNo.setStatus("current")


class _ZxAnIsdnSIfTrapEnable_Type(Integer32):
    """Custom type zxAnIsdnSIfTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnIsdnSIfTrapEnable_Type.__name__ = "Integer32"
_ZxAnIsdnSIfTrapEnable_Object = MibTableColumn
zxAnIsdnSIfTrapEnable = _ZxAnIsdnSIfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 5),
    _ZxAnIsdnSIfTrapEnable_Type()
)
zxAnIsdnSIfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnSIfTrapEnable.setStatus("current")


class _ZxAnIsdnSIfSyncStatus_Type(Integer32):
    """Custom type zxAnIsdnSIfSyncStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 1),
          ("unsynchronized", 2))
    )


_ZxAnIsdnSIfSyncStatus_Type.__name__ = "Integer32"
_ZxAnIsdnSIfSyncStatus_Object = MibTableColumn
zxAnIsdnSIfSyncStatus = _ZxAnIsdnSIfSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 6),
    _ZxAnIsdnSIfSyncStatus_Type()
)
zxAnIsdnSIfSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnSIfSyncStatus.setStatus("current")


class _ZxAnIsdnSIfAbnormalReason_Type(Integer32):
    """Custom type zxAnIsdnSIfAbnormalReason based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("errorIndication2", 1),
          ("errorIndication3", 2),
          ("lossOfSignalLevel", 3),
          ("reSyncIndication", 4),
          ("frameJump", 5),
          ("uIfActivationIndication", 6),
          ("uIfdeactivationIndication", 7),
          ("other", 255))
    )


_ZxAnIsdnSIfAbnormalReason_Type.__name__ = "Integer32"
_ZxAnIsdnSIfAbnormalReason_Object = MibTableColumn
zxAnIsdnSIfAbnormalReason = _ZxAnIsdnSIfAbnormalReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 10, 1, 7),
    _ZxAnIsdnSIfAbnormalReason_Type()
)
zxAnIsdnSIfAbnormalReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnSIfAbnormalReason.setStatus("current")
_ZxAnIsdnBertMgmtGroup_ObjectIdentity = ObjectIdentity
zxAnIsdnBertMgmtGroup = _ZxAnIsdnBertMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11)
)
_ZxAnIsdnBertConfTable_Object = MibTable
zxAnIsdnBertConfTable = _ZxAnIsdnBertConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1)
)
if mibBuilder.loadTexts:
    zxAnIsdnBertConfTable.setStatus("current")
_ZxAnIsdnBertConfEntry_Object = MibTableRow
zxAnIsdnBertConfEntry = _ZxAnIsdnBertConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1)
)
zxAnIsdnBertConfEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertConfRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertConfShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertConfSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertConfCircuit"),
)
if mibBuilder.loadTexts:
    zxAnIsdnBertConfEntry.setStatus("current")
_ZxAnIsdnBertConfRack_Type = Integer32
_ZxAnIsdnBertConfRack_Object = MibTableColumn
zxAnIsdnBertConfRack = _ZxAnIsdnBertConfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 1),
    _ZxAnIsdnBertConfRack_Type()
)
zxAnIsdnBertConfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertConfRack.setStatus("current")
_ZxAnIsdnBertConfShelf_Type = Integer32
_ZxAnIsdnBertConfShelf_Object = MibTableColumn
zxAnIsdnBertConfShelf = _ZxAnIsdnBertConfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 2),
    _ZxAnIsdnBertConfShelf_Type()
)
zxAnIsdnBertConfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertConfShelf.setStatus("current")
_ZxAnIsdnBertConfSlot_Type = Integer32
_ZxAnIsdnBertConfSlot_Object = MibTableColumn
zxAnIsdnBertConfSlot = _ZxAnIsdnBertConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 3),
    _ZxAnIsdnBertConfSlot_Type()
)
zxAnIsdnBertConfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertConfSlot.setStatus("current")
_ZxAnIsdnBertConfCircuit_Type = Integer32
_ZxAnIsdnBertConfCircuit_Object = MibTableColumn
zxAnIsdnBertConfCircuit = _ZxAnIsdnBertConfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 4),
    _ZxAnIsdnBertConfCircuit_Type()
)
zxAnIsdnBertConfCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertConfCircuit.setStatus("current")


class _ZxAnIsdnBertAction_Type(Integer32):
    """Custom type zxAnIsdnBertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_ZxAnIsdnBertAction_Type.__name__ = "Integer32"
_ZxAnIsdnBertAction_Object = MibTableColumn
zxAnIsdnBertAction = _ZxAnIsdnBertAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 5),
    _ZxAnIsdnBertAction_Type()
)
zxAnIsdnBertAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnBertAction.setStatus("current")


class _ZxAnIsdnBertLoopbackPosition_Type(Integer32):
    """Custom type zxAnIsdnBertLoopbackPosition based on Integer32"""
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
        *(("local", 1),
          ("nt", 2),
          ("teTa", 3))
    )


_ZxAnIsdnBertLoopbackPosition_Type.__name__ = "Integer32"
_ZxAnIsdnBertLoopbackPosition_Object = MibTableColumn
zxAnIsdnBertLoopbackPosition = _ZxAnIsdnBertLoopbackPosition_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 6),
    _ZxAnIsdnBertLoopbackPosition_Type()
)
zxAnIsdnBertLoopbackPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnBertLoopbackPosition.setStatus("current")


class _ZxAnIsdnBertThresholdLevel_Type(Integer32):
    """Custom type zxAnIsdnBertThresholdLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tenENegtive3", 3),
          ("tenENegtive4", 4),
          ("tenENegtive5", 5),
          ("tenENegtive6", 6))
    )


_ZxAnIsdnBertThresholdLevel_Type.__name__ = "Integer32"
_ZxAnIsdnBertThresholdLevel_Object = MibTableColumn
zxAnIsdnBertThresholdLevel = _ZxAnIsdnBertThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 7),
    _ZxAnIsdnBertThresholdLevel_Type()
)
zxAnIsdnBertThresholdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnBertThresholdLevel.setStatus("current")


class _ZxAnIsdnBertMeasurePrecision_Type(Integer32):
    """Custom type zxAnIsdnBertMeasurePrecision based on Integer32"""
    defaultValue = 1

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
        *(("neg30To45", 1),
          ("neg22To30", 2),
          ("neg17To20", 3),
          ("neg12To14", 4))
    )


_ZxAnIsdnBertMeasurePrecision_Type.__name__ = "Integer32"
_ZxAnIsdnBertMeasurePrecision_Object = MibTableColumn
zxAnIsdnBertMeasurePrecision = _ZxAnIsdnBertMeasurePrecision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 8),
    _ZxAnIsdnBertMeasurePrecision_Type()
)
zxAnIsdnBertMeasurePrecision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnBertMeasurePrecision.setStatus("current")


class _ZxAnIsdnBertForceTest_Type(TruthValue):
    """Custom type zxAnIsdnBertForceTest based on TruthValue"""
    defaultValue = 2


_ZxAnIsdnBertForceTest_Type.__name__ = "TruthValue"
_ZxAnIsdnBertForceTest_Object = MibTableColumn
zxAnIsdnBertForceTest = _ZxAnIsdnBertForceTest_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 9),
    _ZxAnIsdnBertForceTest_Type()
)
zxAnIsdnBertForceTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnBertForceTest.setStatus("current")


class _ZxAnIsdnBertStartDateAndTime_Type(DisplayString):
    """Custom type zxAnIsdnBertStartDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnIsdnBertStartDateAndTime_Type.__name__ = "DisplayString"
_ZxAnIsdnBertStartDateAndTime_Object = MibTableColumn
zxAnIsdnBertStartDateAndTime = _ZxAnIsdnBertStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 10),
    _ZxAnIsdnBertStartDateAndTime_Type()
)
zxAnIsdnBertStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertStartDateAndTime.setStatus("current")


class _ZxAnIsdnBertOperStatus_Type(Integer32):
    """Custom type zxAnIsdnBertOperStatus based on Integer32"""
    defaultValue = 1

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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnIsdnBertOperStatus_Type.__name__ = "Integer32"
_ZxAnIsdnBertOperStatus_Object = MibTableColumn
zxAnIsdnBertOperStatus = _ZxAnIsdnBertOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 11),
    _ZxAnIsdnBertOperStatus_Type()
)
zxAnIsdnBertOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertOperStatus.setStatus("current")


class _ZxAnIsdnBertResult_Type(Integer32):
    """Custom type zxAnIsdnBertResult based on Integer32"""
    defaultValue = 1

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
        *(("noResult", 1),
          ("pass", 2),
          ("notPass", 3),
          ("failed", 4))
    )


_ZxAnIsdnBertResult_Type.__name__ = "Integer32"
_ZxAnIsdnBertResult_Object = MibTableColumn
zxAnIsdnBertResult = _ZxAnIsdnBertResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 12),
    _ZxAnIsdnBertResult_Type()
)
zxAnIsdnBertResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertResult.setStatus("current")
_ZxAnIsdnBertRowStatus_Type = RowStatus
_ZxAnIsdnBertRowStatus_Object = MibTableColumn
zxAnIsdnBertRowStatus = _ZxAnIsdnBertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 1, 1, 20),
    _ZxAnIsdnBertRowStatus_Type()
)
zxAnIsdnBertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnBertRowStatus.setStatus("current")
_ZxAnIsdnBertStatsTable_Object = MibTable
zxAnIsdnBertStatsTable = _ZxAnIsdnBertStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2)
)
if mibBuilder.loadTexts:
    zxAnIsdnBertStatsTable.setStatus("current")
_ZxAnIsdnBertStatsEntry_Object = MibTableRow
zxAnIsdnBertStatsEntry = _ZxAnIsdnBertStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1)
)
zxAnIsdnBertStatsEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertStatsRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertStatsShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertStatsSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnBertStatsCircuit"),
)
if mibBuilder.loadTexts:
    zxAnIsdnBertStatsEntry.setStatus("current")
_ZxAnIsdnBertStatsRack_Type = Integer32
_ZxAnIsdnBertStatsRack_Object = MibTableColumn
zxAnIsdnBertStatsRack = _ZxAnIsdnBertStatsRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 1),
    _ZxAnIsdnBertStatsRack_Type()
)
zxAnIsdnBertStatsRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertStatsRack.setStatus("current")
_ZxAnIsdnBertStatsShelf_Type = Integer32
_ZxAnIsdnBertStatsShelf_Object = MibTableColumn
zxAnIsdnBertStatsShelf = _ZxAnIsdnBertStatsShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 2),
    _ZxAnIsdnBertStatsShelf_Type()
)
zxAnIsdnBertStatsShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertStatsShelf.setStatus("current")
_ZxAnIsdnBertStatsSlot_Type = Integer32
_ZxAnIsdnBertStatsSlot_Object = MibTableColumn
zxAnIsdnBertStatsSlot = _ZxAnIsdnBertStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 3),
    _ZxAnIsdnBertStatsSlot_Type()
)
zxAnIsdnBertStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertStatsSlot.setStatus("current")
_ZxAnIsdnBertStatsCircuit_Type = Integer32
_ZxAnIsdnBertStatsCircuit_Object = MibTableColumn
zxAnIsdnBertStatsCircuit = _ZxAnIsdnBertStatsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 4),
    _ZxAnIsdnBertStatsCircuit_Type()
)
zxAnIsdnBertStatsCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnBertStatsCircuit.setStatus("current")
_ZxAnIsdnBertTimeElapsed_Type = Integer32
_ZxAnIsdnBertTimeElapsed_Object = MibTableColumn
zxAnIsdnBertTimeElapsed = _ZxAnIsdnBertTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 5),
    _ZxAnIsdnBertTimeElapsed_Type()
)
zxAnIsdnBertTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIsdnBertTimeElapsed.setUnits("10ms")
_ZxAnIsdnBertTxTotalBits_Type = Counter64
_ZxAnIsdnBertTxTotalBits_Object = MibTableColumn
zxAnIsdnBertTxTotalBits = _ZxAnIsdnBertTxTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 6),
    _ZxAnIsdnBertTxTotalBits_Type()
)
zxAnIsdnBertTxTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertTxTotalBits.setStatus("current")
_ZxAnIsdnBertRxTotalBits_Type = Counter64
_ZxAnIsdnBertRxTotalBits_Object = MibTableColumn
zxAnIsdnBertRxTotalBits = _ZxAnIsdnBertRxTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 7),
    _ZxAnIsdnBertRxTotalBits_Type()
)
zxAnIsdnBertRxTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertRxTotalBits.setStatus("current")
_ZxAnIsdnBertRxErrorBits_Type = Counter32
_ZxAnIsdnBertRxErrorBits_Object = MibTableColumn
zxAnIsdnBertRxErrorBits = _ZxAnIsdnBertRxErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 8),
    _ZxAnIsdnBertRxErrorBits_Type()
)
zxAnIsdnBertRxErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertRxErrorBits.setStatus("current")


class _ZxAnIsdnBertRxBitErrorRatio_Type(Unsigned32):
    """Custom type zxAnIsdnBertRxBitErrorRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnIsdnBertRxBitErrorRatio_Type.__name__ = "Unsigned32"
_ZxAnIsdnBertRxBitErrorRatio_Object = MibTableColumn
zxAnIsdnBertRxBitErrorRatio = _ZxAnIsdnBertRxBitErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 11, 2, 1, 9),
    _ZxAnIsdnBertRxBitErrorRatio_Type()
)
zxAnIsdnBertRxBitErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnBertRxBitErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIsdnBertRxBitErrorRatio.setUnits("percents")
_ZxAnIsdnTrunkTerminationIdTable_Object = MibTable
zxAnIsdnTrunkTerminationIdTable = _ZxAnIsdnTrunkTerminationIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12)
)
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTerminationIdTable.setStatus("current")
_ZxAnIsdnTrunkTerminationIdEntry_Object = MibTableRow
zxAnIsdnTrunkTerminationIdEntry = _ZxAnIsdnTrunkTerminationIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1)
)
zxAnIsdnTrunkTerminationIdEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkTidRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkTidShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkTidSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkTidDsx1LinkNo"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkTidDsx1TsNo"),
)
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTerminationIdEntry.setStatus("current")
_ZxAnIsdnTrunkTidRack_Type = Integer32
_ZxAnIsdnTrunkTidRack_Object = MibTableColumn
zxAnIsdnTrunkTidRack = _ZxAnIsdnTrunkTidRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 1),
    _ZxAnIsdnTrunkTidRack_Type()
)
zxAnIsdnTrunkTidRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidRack.setStatus("current")
_ZxAnIsdnTrunkTidShelf_Type = Integer32
_ZxAnIsdnTrunkTidShelf_Object = MibTableColumn
zxAnIsdnTrunkTidShelf = _ZxAnIsdnTrunkTidShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 2),
    _ZxAnIsdnTrunkTidShelf_Type()
)
zxAnIsdnTrunkTidShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidShelf.setStatus("current")
_ZxAnIsdnTrunkTidSlot_Type = Integer32
_ZxAnIsdnTrunkTidSlot_Object = MibTableColumn
zxAnIsdnTrunkTidSlot = _ZxAnIsdnTrunkTidSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 3),
    _ZxAnIsdnTrunkTidSlot_Type()
)
zxAnIsdnTrunkTidSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidSlot.setStatus("current")


class _ZxAnIsdnTrunkTidDsx1LinkNo_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidDsx1LinkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ZxAnIsdnTrunkTidDsx1LinkNo_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidDsx1LinkNo_Object = MibTableColumn
zxAnIsdnTrunkTidDsx1LinkNo = _ZxAnIsdnTrunkTidDsx1LinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 4),
    _ZxAnIsdnTrunkTidDsx1LinkNo_Type()
)
zxAnIsdnTrunkTidDsx1LinkNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidDsx1LinkNo.setStatus("current")


class _ZxAnIsdnTrunkTidDsx1TsNo_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidDsx1TsNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZxAnIsdnTrunkTidDsx1TsNo_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidDsx1TsNo_Object = MibTableColumn
zxAnIsdnTrunkTidDsx1TsNo = _ZxAnIsdnTrunkTidDsx1TsNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 5),
    _ZxAnIsdnTrunkTidDsx1TsNo_Type()
)
zxAnIsdnTrunkTidDsx1TsNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidDsx1TsNo.setStatus("current")


class _ZxAnIsdnTrunkTidPrefix_Type(DisplayString):
    """Custom type zxAnIsdnTrunkTidPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnIsdnTrunkTidPrefix_Type.__name__ = "DisplayString"
_ZxAnIsdnTrunkTidPrefix_Object = MibTableColumn
zxAnIsdnTrunkTidPrefix = _ZxAnIsdnTrunkTidPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 6),
    _ZxAnIsdnTrunkTidPrefix_Type()
)
zxAnIsdnTrunkTidPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidPrefix.setStatus("current")


class _ZxAnIsdnTrunkTidType_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3))
    )


_ZxAnIsdnTrunkTidType_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidType_Object = MibTableColumn
zxAnIsdnTrunkTidType = _ZxAnIsdnTrunkTidType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 7),
    _ZxAnIsdnTrunkTidType_Type()
)
zxAnIsdnTrunkTidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidType.setStatus("current")


class _ZxAnIsdnTrunkTidOperNum_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidOperNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ZxAnIsdnTrunkTidOperNum_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidOperNum_Object = MibTableColumn
zxAnIsdnTrunkTidOperNum = _ZxAnIsdnTrunkTidOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 8),
    _ZxAnIsdnTrunkTidOperNum_Type()
)
zxAnIsdnTrunkTidOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidOperNum.setStatus("current")


class _ZxAnIsdnTrunkTidDigitBeginNo_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidDigitBeginNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnIsdnTrunkTidDigitBeginNo_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidDigitBeginNo_Object = MibTableColumn
zxAnIsdnTrunkTidDigitBeginNo = _ZxAnIsdnTrunkTidDigitBeginNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 9),
    _ZxAnIsdnTrunkTidDigitBeginNo_Type()
)
zxAnIsdnTrunkTidDigitBeginNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidDigitBeginNo.setStatus("current")


class _ZxAnIsdnTrunkTidDigitLength_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidDigitLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_ZxAnIsdnTrunkTidDigitLength_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidDigitLength_Object = MibTableColumn
zxAnIsdnTrunkTidDigitLength = _ZxAnIsdnTrunkTidDigitLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 10),
    _ZxAnIsdnTrunkTidDigitLength_Type()
)
zxAnIsdnTrunkTidDigitLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidDigitLength.setStatus("current")


class _ZxAnIsdnTrunkTidMgId_Type(Integer32):
    """Custom type zxAnIsdnTrunkTidMgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnIsdnTrunkTidMgId_Type.__name__ = "Integer32"
_ZxAnIsdnTrunkTidMgId_Object = MibTableColumn
zxAnIsdnTrunkTidMgId = _ZxAnIsdnTrunkTidMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 11),
    _ZxAnIsdnTrunkTidMgId_Type()
)
zxAnIsdnTrunkTidMgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidMgId.setStatus("current")


class _ZxAnIsdnTrunkTerminationId_Type(DisplayString):
    """Custom type zxAnIsdnTrunkTerminationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnIsdnTrunkTerminationId_Type.__name__ = "DisplayString"
_ZxAnIsdnTrunkTerminationId_Object = MibTableColumn
zxAnIsdnTrunkTerminationId = _ZxAnIsdnTrunkTerminationId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 12),
    _ZxAnIsdnTrunkTerminationId_Type()
)
zxAnIsdnTrunkTerminationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTerminationId.setStatus("current")
_ZxAnIsdnTrunkTidRowStatus_Type = RowStatus
_ZxAnIsdnTrunkTidRowStatus_Object = MibTableColumn
zxAnIsdnTrunkTidRowStatus = _ZxAnIsdnTrunkTidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 12, 1, 50),
    _ZxAnIsdnTrunkTidRowStatus_Type()
)
zxAnIsdnTrunkTidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTidRowStatus.setStatus("current")
_ZxAnIsdnTrunkTable_Object = MibTable
zxAnIsdnTrunkTable = _ZxAnIsdnTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13)
)
if mibBuilder.loadTexts:
    zxAnIsdnTrunkTable.setStatus("current")
_ZxAnIsdnTrunkEntry_Object = MibTableRow
zxAnIsdnTrunkEntry = _ZxAnIsdnTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1)
)
zxAnIsdnTrunkEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkDsx1LinkNo"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnTrunkDsx1TsNo"),
)
if mibBuilder.loadTexts:
    zxAnIsdnTrunkEntry.setStatus("current")
_ZxAnIsdnTrunkRack_Type = Integer32
_ZxAnIsdnTrunkRack_Object = MibTableColumn
zxAnIsdnTrunkRack = _ZxAnIsdnTrunkRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1, 1),
    _ZxAnIsdnTrunkRack_Type()
)
zxAnIsdnTrunkRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkRack.setStatus("current")
_ZxAnIsdnTrunkShelf_Type = Integer32
_ZxAnIsdnTrunkShelf_Object = MibTableColumn
zxAnIsdnTrunkShelf = _ZxAnIsdnTrunkShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1, 2),
    _ZxAnIsdnTrunkShelf_Type()
)
zxAnIsdnTrunkShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkShelf.setStatus("current")
_ZxAnIsdnTrunkSlot_Type = Integer32
_ZxAnIsdnTrunkSlot_Object = MibTableColumn
zxAnIsdnTrunkSlot = _ZxAnIsdnTrunkSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1, 3),
    _ZxAnIsdnTrunkSlot_Type()
)
zxAnIsdnTrunkSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkSlot.setStatus("current")
_ZxAnIsdnTrunkDsx1LinkNo_Type = Integer32
_ZxAnIsdnTrunkDsx1LinkNo_Object = MibTableColumn
zxAnIsdnTrunkDsx1LinkNo = _ZxAnIsdnTrunkDsx1LinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1, 4),
    _ZxAnIsdnTrunkDsx1LinkNo_Type()
)
zxAnIsdnTrunkDsx1LinkNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkDsx1LinkNo.setStatus("current")
_ZxAnIsdnTrunkDsx1TsNo_Type = Integer32
_ZxAnIsdnTrunkDsx1TsNo_Object = MibTableColumn
zxAnIsdnTrunkDsx1TsNo = _ZxAnIsdnTrunkDsx1TsNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1, 5),
    _ZxAnIsdnTrunkDsx1TsNo_Type()
)
zxAnIsdnTrunkDsx1TsNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkDsx1TsNo.setStatus("current")


class _ZxAnIsdnTrunkStatus_Type(Bits):
    """Custom type zxAnIsdnTrunkStatus based on Bits"""
    namedValues = NamedValues(
        *(("idle", 0),
          ("commOff", 1),
          ("powerOff", 2),
          ("fault", 3),
          ("manualBlock", 4),
          ("seizure", 5),
          ("spc", 6))
    )

_ZxAnIsdnTrunkStatus_Type.__name__ = "Bits"
_ZxAnIsdnTrunkStatus_Object = MibTableColumn
zxAnIsdnTrunkStatus = _ZxAnIsdnTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 13, 1, 6),
    _ZxAnIsdnTrunkStatus_Type()
)
zxAnIsdnTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnTrunkStatus.setStatus("current")
_ZxAnIsdnCallStatsTable_Object = MibTable
zxAnIsdnCallStatsTable = _ZxAnIsdnCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14)
)
if mibBuilder.loadTexts:
    zxAnIsdnCallStatsTable.setStatus("current")
_ZxAnIsdnCallStatsEntry_Object = MibTableRow
zxAnIsdnCallStatsEntry = _ZxAnIsdnCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1)
)
zxAnIsdnCallStatsEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnCallStatsRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnCallStatsShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnCallStatsSlot"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnCallStatsPort"),
)
if mibBuilder.loadTexts:
    zxAnIsdnCallStatsEntry.setStatus("current")
_ZxAnIsdnCallStatsRack_Type = Integer32
_ZxAnIsdnCallStatsRack_Object = MibTableColumn
zxAnIsdnCallStatsRack = _ZxAnIsdnCallStatsRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 1),
    _ZxAnIsdnCallStatsRack_Type()
)
zxAnIsdnCallStatsRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnCallStatsRack.setStatus("current")
_ZxAnIsdnCallStatsShelf_Type = Integer32
_ZxAnIsdnCallStatsShelf_Object = MibTableColumn
zxAnIsdnCallStatsShelf = _ZxAnIsdnCallStatsShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 2),
    _ZxAnIsdnCallStatsShelf_Type()
)
zxAnIsdnCallStatsShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnCallStatsShelf.setStatus("current")
_ZxAnIsdnCallStatsSlot_Type = Integer32
_ZxAnIsdnCallStatsSlot_Object = MibTableColumn
zxAnIsdnCallStatsSlot = _ZxAnIsdnCallStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 3),
    _ZxAnIsdnCallStatsSlot_Type()
)
zxAnIsdnCallStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnCallStatsSlot.setStatus("current")
_ZxAnIsdnCallStatsPort_Type = Integer32
_ZxAnIsdnCallStatsPort_Object = MibTableColumn
zxAnIsdnCallStatsPort = _ZxAnIsdnCallStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 4),
    _ZxAnIsdnCallStatsPort_Type()
)
zxAnIsdnCallStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnCallStatsPort.setStatus("current")
_ZxAnIsdnSuccessIncomingCalls_Type = Counter32
_ZxAnIsdnSuccessIncomingCalls_Object = MibTableColumn
zxAnIsdnSuccessIncomingCalls = _ZxAnIsdnSuccessIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 5),
    _ZxAnIsdnSuccessIncomingCalls_Type()
)
zxAnIsdnSuccessIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnSuccessIncomingCalls.setStatus("current")
_ZxAnIsdnFailedIncomingCalls_Type = Counter32
_ZxAnIsdnFailedIncomingCalls_Object = MibTableColumn
zxAnIsdnFailedIncomingCalls = _ZxAnIsdnFailedIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 6),
    _ZxAnIsdnFailedIncomingCalls_Type()
)
zxAnIsdnFailedIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnFailedIncomingCalls.setStatus("current")
_ZxAnIsdnSuccessOutgoingCalls_Type = Counter32
_ZxAnIsdnSuccessOutgoingCalls_Object = MibTableColumn
zxAnIsdnSuccessOutgoingCalls = _ZxAnIsdnSuccessOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 7),
    _ZxAnIsdnSuccessOutgoingCalls_Type()
)
zxAnIsdnSuccessOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnSuccessOutgoingCalls.setStatus("current")
_ZxAnIsdnFailedOutgoingCalls_Type = Counter32
_ZxAnIsdnFailedOutgoingCalls_Object = MibTableColumn
zxAnIsdnFailedOutgoingCalls = _ZxAnIsdnFailedOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 8),
    _ZxAnIsdnFailedOutgoingCalls_Type()
)
zxAnIsdnFailedOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnFailedOutgoingCalls.setStatus("current")
_ZxAnIsdnActiveIncomingCalls_Type = Counter32
_ZxAnIsdnActiveIncomingCalls_Object = MibTableColumn
zxAnIsdnActiveIncomingCalls = _ZxAnIsdnActiveIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 9),
    _ZxAnIsdnActiveIncomingCalls_Type()
)
zxAnIsdnActiveIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnActiveIncomingCalls.setStatus("current")
_ZxAnIsdnActiveOutgoingCalls_Type = Counter32
_ZxAnIsdnActiveOutgoingCalls_Object = MibTableColumn
zxAnIsdnActiveOutgoingCalls = _ZxAnIsdnActiveOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 14, 1, 10),
    _ZxAnIsdnActiveOutgoingCalls_Type()
)
zxAnIsdnActiveOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIsdnActiveOutgoingCalls.setStatus("current")
_ZxAnIsdnRemotePowerSupplyTable_Object = MibTable
zxAnIsdnRemotePowerSupplyTable = _ZxAnIsdnRemotePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 15)
)
if mibBuilder.loadTexts:
    zxAnIsdnRemotePowerSupplyTable.setStatus("current")
_ZxAnIsdnRemotePowerSupplyEntry_Object = MibTableRow
zxAnIsdnRemotePowerSupplyEntry = _ZxAnIsdnRemotePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 15, 1)
)
zxAnIsdnRemotePowerSupplyEntry.setIndexNames(
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnRemotePowerSupplyRack"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnRemotePowerSupplyShelf"),
    (0, "ZTE-AN-ISDN-MIB", "zxAnIsdnRemotePowerSupplySlot"),
)
if mibBuilder.loadTexts:
    zxAnIsdnRemotePowerSupplyEntry.setStatus("current")
_ZxAnIsdnRemotePowerSupplyRack_Type = Integer32
_ZxAnIsdnRemotePowerSupplyRack_Object = MibTableColumn
zxAnIsdnRemotePowerSupplyRack = _ZxAnIsdnRemotePowerSupplyRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 15, 1, 1),
    _ZxAnIsdnRemotePowerSupplyRack_Type()
)
zxAnIsdnRemotePowerSupplyRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnRemotePowerSupplyRack.setStatus("current")
_ZxAnIsdnRemotePowerSupplyShelf_Type = Integer32
_ZxAnIsdnRemotePowerSupplyShelf_Object = MibTableColumn
zxAnIsdnRemotePowerSupplyShelf = _ZxAnIsdnRemotePowerSupplyShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 15, 1, 2),
    _ZxAnIsdnRemotePowerSupplyShelf_Type()
)
zxAnIsdnRemotePowerSupplyShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnRemotePowerSupplyShelf.setStatus("current")
_ZxAnIsdnRemotePowerSupplySlot_Type = Integer32
_ZxAnIsdnRemotePowerSupplySlot_Object = MibTableColumn
zxAnIsdnRemotePowerSupplySlot = _ZxAnIsdnRemotePowerSupplySlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 15, 1, 3),
    _ZxAnIsdnRemotePowerSupplySlot_Type()
)
zxAnIsdnRemotePowerSupplySlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIsdnRemotePowerSupplySlot.setStatus("current")


class _ZxAnIsdnRemotePowerSupplyEnable_Type(Integer32):
    """Custom type zxAnIsdnRemotePowerSupplyEnable based on Integer32"""
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


_ZxAnIsdnRemotePowerSupplyEnable_Type.__name__ = "Integer32"
_ZxAnIsdnRemotePowerSupplyEnable_Object = MibTableColumn
zxAnIsdnRemotePowerSupplyEnable = _ZxAnIsdnRemotePowerSupplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 15, 1, 4),
    _ZxAnIsdnRemotePowerSupplyEnable_Type()
)
zxAnIsdnRemotePowerSupplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIsdnRemotePowerSupplyEnable.setStatus("current")
_ZxAnIsdnTrapObjects_ObjectIdentity = ObjectIdentity
zxAnIsdnTrapObjects = _ZxAnIsdnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 100)
)

# Managed Objects groups


# Notification objects

zxAnIsdnSInterfaceUnsyncAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 100, 1)
)
zxAnIsdnSInterfaceUnsyncAlm.setObjects(
    ("ZTE-AN-ISDN-MIB", "zxAnIsdnSIfSyncStatus")
)
if mibBuilder.loadTexts:
    zxAnIsdnSInterfaceUnsyncAlm.setStatus(
        "current"
    )

zxAnIsdnSInterfaceUnsyncClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 100, 2)
)
zxAnIsdnSInterfaceUnsyncClr.setObjects(
    ("ZTE-AN-ISDN-MIB", "zxAnIsdnSIfSyncStatus")
)
if mibBuilder.loadTexts:
    zxAnIsdnSInterfaceUnsyncClr.setStatus(
        "current"
    )

zxAnIsdnUInterfaceAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 100, 3)
)
zxAnIsdnUInterfaceAbnormal.setObjects(
    ("ZTE-AN-ISDN-MIB", "zxAnIsdnUIfAbnormalReason")
)
if mibBuilder.loadTexts:
    zxAnIsdnUInterfaceAbnormal.setStatus(
        "current"
    )

zxAnIsdnSInterfaceAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 4, 100, 4)
)
zxAnIsdnSInterfaceAbnormal.setObjects(
    ("ZTE-AN-ISDN-MIB", "zxAnIsdnSIfAbnormalReason")
)
if mibBuilder.loadTexts:
    zxAnIsdnSInterfaceAbnormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ISDN-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnISDNMib": zxAnISDNMib,
       "msagmajorVersion": msagmajorVersion,
       "msagISDNService": msagISDNService,
       "isdnAppServerTable": isdnAppServerTable,
       "isdnAppServerEntry": isdnAppServerEntry,
       "isdnAppServerID": isdnAppServerID,
       "isdnAppServerProtocol": isdnAppServerProtocol,
       "isdnAppServerMode": isdnAppServerMode,
       "isdnAppServerModeEval": isdnAppServerModeEval,
       "isdnAppServerStatus": isdnAppServerStatus,
       "isdnAppServerRowStatus": isdnAppServerRowStatus,
       "isdnAppServerProcTable": isdnAppServerProcTable,
       "isdnAppServerProcEntry": isdnAppServerProcEntry,
       "isdnASPID": isdnASPID,
       "isdnASPDestPort": isdnASPDestPort,
       "isdnASPLoclPort": isdnASPLoclPort,
       "isdnASPSctpID": isdnASPSctpID,
       "isdnASPUpProto": isdnASPUpProto,
       "isdnASPDownProto": isdnASPDownProto,
       "isdnASPDestIP": isdnASPDestIP,
       "isdnASPInStream": isdnASPInStream,
       "isdnASPOutStream": isdnASPOutStream,
       "isdnASPStat": isdnASPStat,
       "isdnASPModule": isdnASPModule,
       "isdnASPClieOrServ": isdnASPClieOrServ,
       "isdnASPRowStatus": isdnASPRowStatus,
       "isdnASASPRelationTable": isdnASASPRelationTable,
       "isdnASASPRelationEntry": isdnASASPRelationEntry,
       "isdnAARASPID": isdnAARASPID,
       "isdnAARASID": isdnAARASID,
       "isdnAARQueue": isdnAARQueue,
       "isdnAARRowStatus": isdnAARRowStatus,
       "isdnDLinkTable": isdnDLinkTable,
       "isdnDLinkEntry": isdnDLinkEntry,
       "isdnDLinkRack": isdnDLinkRack,
       "isdnDLinkShelf": isdnDLinkShelf,
       "isdnDLinkSlot": isdnDLinkSlot,
       "isdnDLinkPCMNo": isdnDLinkPCMNo,
       "isdnDLinkLinkIdx": isdnDLinkLinkIdx,
       "isdnDLinkIfID": isdnDLinkIfID,
       "isdnDLinkLinkID": isdnDLinkLinkID,
       "isdnDLinkLinkInfo": isdnDLinkLinkInfo,
       "isdnDLinkASID": isdnDLinkASID,
       "isdnDLinkNumber": isdnDLinkNumber,
       "isdnDLinkProtocol": isdnDLinkProtocol,
       "isdnDLinkStatus": isdnDLinkStatus,
       "isdnDLinkRowStatus": isdnDLinkRowStatus,
       "loopbackTable": loopbackTable,
       "loopbackEntry": loopbackEntry,
       "loopbackrack": loopbackrack,
       "loopbackshelf": loopbackshelf,
       "loopbackslot": loopbackslot,
       "loopbackportno": loopbackportno,
       "loopbacklooptype": loopbacklooptype,
       "msagIsdnCapabilityTable": msagIsdnCapabilityTable,
       "msagIsdnCapabilityEntry": msagIsdnCapabilityEntry,
       "isdnkrack": isdnkrack,
       "isdnshelf": isdnshelf,
       "isdnslot": isdnslot,
       "isdnportno": isdnportno,
       "isdnLossOfSignal": isdnLossOfSignal,
       "isdnLossOfPower": isdnLossOfPower,
       "isdnLossOfFrame": isdnLossOfFrame,
       "isdnClear": isdnClear,
       "zxAnIsdnPortActiveStatusTable": zxAnIsdnPortActiveStatusTable,
       "zxAnIsdnPortActiveStatusEntry": zxAnIsdnPortActiveStatusEntry,
       "zxAnIsdnPortRack": zxAnIsdnPortRack,
       "zxAnIsdnPortShelf": zxAnIsdnPortShelf,
       "zxAnIsdnPortSlot": zxAnIsdnPortSlot,
       "zxAnIsdnPortNo": zxAnIsdnPortNo,
       "zxAnIsdnPortL1ActiveStatus": zxAnIsdnPortL1ActiveStatus,
       "zxAnIsdnPortL2ActiveStatus": zxAnIsdnPortL2ActiveStatus,
       "zxAnIsdnUIfCfgTable": zxAnIsdnUIfCfgTable,
       "zxAnIsdnUIfCfgEntry": zxAnIsdnUIfCfgEntry,
       "zxAnIsdnUIfRack": zxAnIsdnUIfRack,
       "zxAnIsdnUIfShelf": zxAnIsdnUIfShelf,
       "zxAnIsdnUIfSlot": zxAnIsdnUIfSlot,
       "zxAnIsdnUIfNo": zxAnIsdnUIfNo,
       "zxAnIsdnUIfRemotePowerFeedEnable": zxAnIsdnUIfRemotePowerFeedEnable,
       "zxAnIsdnUIfTrapEnable": zxAnIsdnUIfTrapEnable,
       "zxAnIsdnUIfActiveStatus": zxAnIsdnUIfActiveStatus,
       "zxAnIsdnUIfSoftReset": zxAnIsdnUIfSoftReset,
       "zxAnIsdnUIfAbnormalReason": zxAnIsdnUIfAbnormalReason,
       "zxAnIsdnSIfCfgTable": zxAnIsdnSIfCfgTable,
       "zxAnIsdnSIfCfgEntry": zxAnIsdnSIfCfgEntry,
       "zxAnIsdnSIfRack": zxAnIsdnSIfRack,
       "zxAnIsdnSIfShelf": zxAnIsdnSIfShelf,
       "zxAnIsdnSIfSlot": zxAnIsdnSIfSlot,
       "zxAnIsdnSIfNo": zxAnIsdnSIfNo,
       "zxAnIsdnSIfTrapEnable": zxAnIsdnSIfTrapEnable,
       "zxAnIsdnSIfSyncStatus": zxAnIsdnSIfSyncStatus,
       "zxAnIsdnSIfAbnormalReason": zxAnIsdnSIfAbnormalReason,
       "zxAnIsdnBertMgmtGroup": zxAnIsdnBertMgmtGroup,
       "zxAnIsdnBertConfTable": zxAnIsdnBertConfTable,
       "zxAnIsdnBertConfEntry": zxAnIsdnBertConfEntry,
       "zxAnIsdnBertConfRack": zxAnIsdnBertConfRack,
       "zxAnIsdnBertConfShelf": zxAnIsdnBertConfShelf,
       "zxAnIsdnBertConfSlot": zxAnIsdnBertConfSlot,
       "zxAnIsdnBertConfCircuit": zxAnIsdnBertConfCircuit,
       "zxAnIsdnBertAction": zxAnIsdnBertAction,
       "zxAnIsdnBertLoopbackPosition": zxAnIsdnBertLoopbackPosition,
       "zxAnIsdnBertThresholdLevel": zxAnIsdnBertThresholdLevel,
       "zxAnIsdnBertMeasurePrecision": zxAnIsdnBertMeasurePrecision,
       "zxAnIsdnBertForceTest": zxAnIsdnBertForceTest,
       "zxAnIsdnBertStartDateAndTime": zxAnIsdnBertStartDateAndTime,
       "zxAnIsdnBertOperStatus": zxAnIsdnBertOperStatus,
       "zxAnIsdnBertResult": zxAnIsdnBertResult,
       "zxAnIsdnBertRowStatus": zxAnIsdnBertRowStatus,
       "zxAnIsdnBertStatsTable": zxAnIsdnBertStatsTable,
       "zxAnIsdnBertStatsEntry": zxAnIsdnBertStatsEntry,
       "zxAnIsdnBertStatsRack": zxAnIsdnBertStatsRack,
       "zxAnIsdnBertStatsShelf": zxAnIsdnBertStatsShelf,
       "zxAnIsdnBertStatsSlot": zxAnIsdnBertStatsSlot,
       "zxAnIsdnBertStatsCircuit": zxAnIsdnBertStatsCircuit,
       "zxAnIsdnBertTimeElapsed": zxAnIsdnBertTimeElapsed,
       "zxAnIsdnBertTxTotalBits": zxAnIsdnBertTxTotalBits,
       "zxAnIsdnBertRxTotalBits": zxAnIsdnBertRxTotalBits,
       "zxAnIsdnBertRxErrorBits": zxAnIsdnBertRxErrorBits,
       "zxAnIsdnBertRxBitErrorRatio": zxAnIsdnBertRxBitErrorRatio,
       "zxAnIsdnTrunkTerminationIdTable": zxAnIsdnTrunkTerminationIdTable,
       "zxAnIsdnTrunkTerminationIdEntry": zxAnIsdnTrunkTerminationIdEntry,
       "zxAnIsdnTrunkTidRack": zxAnIsdnTrunkTidRack,
       "zxAnIsdnTrunkTidShelf": zxAnIsdnTrunkTidShelf,
       "zxAnIsdnTrunkTidSlot": zxAnIsdnTrunkTidSlot,
       "zxAnIsdnTrunkTidDsx1LinkNo": zxAnIsdnTrunkTidDsx1LinkNo,
       "zxAnIsdnTrunkTidDsx1TsNo": zxAnIsdnTrunkTidDsx1TsNo,
       "zxAnIsdnTrunkTidPrefix": zxAnIsdnTrunkTidPrefix,
       "zxAnIsdnTrunkTidType": zxAnIsdnTrunkTidType,
       "zxAnIsdnTrunkTidOperNum": zxAnIsdnTrunkTidOperNum,
       "zxAnIsdnTrunkTidDigitBeginNo": zxAnIsdnTrunkTidDigitBeginNo,
       "zxAnIsdnTrunkTidDigitLength": zxAnIsdnTrunkTidDigitLength,
       "zxAnIsdnTrunkTidMgId": zxAnIsdnTrunkTidMgId,
       "zxAnIsdnTrunkTerminationId": zxAnIsdnTrunkTerminationId,
       "zxAnIsdnTrunkTidRowStatus": zxAnIsdnTrunkTidRowStatus,
       "zxAnIsdnTrunkTable": zxAnIsdnTrunkTable,
       "zxAnIsdnTrunkEntry": zxAnIsdnTrunkEntry,
       "zxAnIsdnTrunkRack": zxAnIsdnTrunkRack,
       "zxAnIsdnTrunkShelf": zxAnIsdnTrunkShelf,
       "zxAnIsdnTrunkSlot": zxAnIsdnTrunkSlot,
       "zxAnIsdnTrunkDsx1LinkNo": zxAnIsdnTrunkDsx1LinkNo,
       "zxAnIsdnTrunkDsx1TsNo": zxAnIsdnTrunkDsx1TsNo,
       "zxAnIsdnTrunkStatus": zxAnIsdnTrunkStatus,
       "zxAnIsdnCallStatsTable": zxAnIsdnCallStatsTable,
       "zxAnIsdnCallStatsEntry": zxAnIsdnCallStatsEntry,
       "zxAnIsdnCallStatsRack": zxAnIsdnCallStatsRack,
       "zxAnIsdnCallStatsShelf": zxAnIsdnCallStatsShelf,
       "zxAnIsdnCallStatsSlot": zxAnIsdnCallStatsSlot,
       "zxAnIsdnCallStatsPort": zxAnIsdnCallStatsPort,
       "zxAnIsdnSuccessIncomingCalls": zxAnIsdnSuccessIncomingCalls,
       "zxAnIsdnFailedIncomingCalls": zxAnIsdnFailedIncomingCalls,
       "zxAnIsdnSuccessOutgoingCalls": zxAnIsdnSuccessOutgoingCalls,
       "zxAnIsdnFailedOutgoingCalls": zxAnIsdnFailedOutgoingCalls,
       "zxAnIsdnActiveIncomingCalls": zxAnIsdnActiveIncomingCalls,
       "zxAnIsdnActiveOutgoingCalls": zxAnIsdnActiveOutgoingCalls,
       "zxAnIsdnRemotePowerSupplyTable": zxAnIsdnRemotePowerSupplyTable,
       "zxAnIsdnRemotePowerSupplyEntry": zxAnIsdnRemotePowerSupplyEntry,
       "zxAnIsdnRemotePowerSupplyRack": zxAnIsdnRemotePowerSupplyRack,
       "zxAnIsdnRemotePowerSupplyShelf": zxAnIsdnRemotePowerSupplyShelf,
       "zxAnIsdnRemotePowerSupplySlot": zxAnIsdnRemotePowerSupplySlot,
       "zxAnIsdnRemotePowerSupplyEnable": zxAnIsdnRemotePowerSupplyEnable,
       "zxAnIsdnTrapObjects": zxAnIsdnTrapObjects,
       "zxAnIsdnSInterfaceUnsyncAlm": zxAnIsdnSInterfaceUnsyncAlm,
       "zxAnIsdnSInterfaceUnsyncClr": zxAnIsdnSInterfaceUnsyncClr,
       "zxAnIsdnUInterfaceAbnormal": zxAnIsdnUInterfaceAbnormal,
       "zxAnIsdnSInterfaceAbnormal": zxAnIsdnSInterfaceAbnormal}
)
