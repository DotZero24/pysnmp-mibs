# SNMP MIB module (TIMETRA-MACSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-MACSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:57:22 2025
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

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "VlanIdOrNone")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID")


# MODULE-IDENTITY

timetraMacsecMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 114)
)
if mibBuilder.loadTexts:
    timetraMacsecMIBModule.setRevisions(
        ("2017-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxMacsecConformance_ObjectIdentity = ObjectIdentity
tmnxMacsecConformance = _TmnxMacsecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114)
)
_TmnxMacsecCompliances_ObjectIdentity = ObjectIdentity
tmnxMacsecCompliances = _TmnxMacsecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 1)
)
_TmnxMacsecGroups_ObjectIdentity = ObjectIdentity
tmnxMacsecGroups = _TmnxMacsecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2)
)
_TmnxMacsecObjects_ObjectIdentity = ObjectIdentity
tmnxMacsecObjects = _TmnxMacsecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114)
)
_TmnxMacsecConfigTimestamps_ObjectIdentity = ObjectIdentity
tmnxMacsecConfigTimestamps = _TmnxMacsecConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 1)
)
_TmnxMacsecConnAssocTableLstChngd_Type = TimeStamp
_TmnxMacsecConnAssocTableLstChngd_Object = MibScalar
tmnxMacsecConnAssocTableLstChngd = _TmnxMacsecConnAssocTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 1, 1),
    _TmnxMacsecConnAssocTableLstChngd_Type()
)
tmnxMacsecConnAssocTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocTableLstChngd.setStatus("current")
_TmnxMacsecStaticCakTableLstChngd_Type = TimeStamp
_TmnxMacsecStaticCakTableLstChngd_Object = MibScalar
tmnxMacsecStaticCakTableLstChngd = _TmnxMacsecStaticCakTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 1, 2),
    _TmnxMacsecStaticCakTableLstChngd_Type()
)
tmnxMacsecStaticCakTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakTableLstChngd.setStatus("current")
_TmnxMacsecPreSharedKeyTblLstChng_Type = TimeStamp
_TmnxMacsecPreSharedKeyTblLstChng_Object = MibScalar
tmnxMacsecPreSharedKeyTblLstChng = _TmnxMacsecPreSharedKeyTblLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 1, 3),
    _TmnxMacsecPreSharedKeyTblLstChng_Type()
)
tmnxMacsecPreSharedKeyTblLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyTblLstChng.setStatus("current")
_TmnxMacsecPortTableLastChanged_Type = TimeStamp
_TmnxMacsecPortTableLastChanged_Object = MibScalar
tmnxMacsecPortTableLastChanged = _TmnxMacsecPortTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 1, 4),
    _TmnxMacsecPortTableLastChanged_Type()
)
tmnxMacsecPortTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortTableLastChanged.setStatus("current")
_TmnxMacsecConfigurations_ObjectIdentity = ObjectIdentity
tmnxMacsecConfigurations = _TmnxMacsecConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2)
)
_TmnxMacsecConfigurationObjects_ObjectIdentity = ObjectIdentity
tmnxMacsecConfigurationObjects = _TmnxMacsecConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 1)
)
_TmnxMacsecConnAssocTable_Object = MibTable
tmnxMacsecConnAssocTable = _TmnxMacsecConnAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocTable.setStatus("current")
_TmnxMacsecConnAssocEntry_Object = MibTableRow
tmnxMacsecConnAssocEntry = _TmnxMacsecConnAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1)
)
tmnxMacsecConnAssocEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocName"),
)
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocEntry.setStatus("current")
_TmnxMacsecConnAssocName_Type = TNamedItem
_TmnxMacsecConnAssocName_Object = MibTableColumn
tmnxMacsecConnAssocName = _TmnxMacsecConnAssocName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 1),
    _TmnxMacsecConnAssocName_Type()
)
tmnxMacsecConnAssocName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocName.setStatus("current")
_TmnxMacsecConnAssocLastChanged_Type = TimeStamp
_TmnxMacsecConnAssocLastChanged_Object = MibTableColumn
tmnxMacsecConnAssocLastChanged = _TmnxMacsecConnAssocLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 2),
    _TmnxMacsecConnAssocLastChanged_Type()
)
tmnxMacsecConnAssocLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocLastChanged.setStatus("current")
_TmnxMacsecConnAssocRowStatus_Type = RowStatus
_TmnxMacsecConnAssocRowStatus_Object = MibTableColumn
tmnxMacsecConnAssocRowStatus = _TmnxMacsecConnAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 3),
    _TmnxMacsecConnAssocRowStatus_Type()
)
tmnxMacsecConnAssocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocRowStatus.setStatus("current")


class _TmnxMacsecConnAssocAdminState_Type(TmnxAdminState):
    """Custom type tmnxMacsecConnAssocAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMacsecConnAssocAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMacsecConnAssocAdminState_Object = MibTableColumn
tmnxMacsecConnAssocAdminState = _TmnxMacsecConnAssocAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 4),
    _TmnxMacsecConnAssocAdminState_Type()
)
tmnxMacsecConnAssocAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocAdminState.setStatus("current")


class _TmnxMacsecConnAssocDescription_Type(TItemDescription):
    """Custom type tmnxMacsecConnAssocDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMacsecConnAssocDescription_Type.__name__ = "TItemDescription"
_TmnxMacsecConnAssocDescription_Object = MibTableColumn
tmnxMacsecConnAssocDescription = _TmnxMacsecConnAssocDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 5),
    _TmnxMacsecConnAssocDescription_Type()
)
tmnxMacsecConnAssocDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocDescription.setStatus("current")


class _TmnxMacsecConnAssocMacsecEncrypt_Type(TruthValue):
    """Custom type tmnxMacsecConnAssocMacsecEncrypt based on TruthValue"""
    defaultValue = 1


_TmnxMacsecConnAssocMacsecEncrypt_Type.__name__ = "TruthValue"
_TmnxMacsecConnAssocMacsecEncrypt_Object = MibTableColumn
tmnxMacsecConnAssocMacsecEncrypt = _TmnxMacsecConnAssocMacsecEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 6),
    _TmnxMacsecConnAssocMacsecEncrypt_Type()
)
tmnxMacsecConnAssocMacsecEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocMacsecEncrypt.setStatus("current")


class _TmnxMacsecConnAssocClearTagMode_Type(Integer32):
    """Custom type tmnxMacsecConnAssocClearTagMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("single-tag", 1),
          ("dual-tag", 2))
    )


_TmnxMacsecConnAssocClearTagMode_Type.__name__ = "Integer32"
_TmnxMacsecConnAssocClearTagMode_Object = MibTableColumn
tmnxMacsecConnAssocClearTagMode = _TmnxMacsecConnAssocClearTagMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 7),
    _TmnxMacsecConnAssocClearTagMode_Type()
)
tmnxMacsecConnAssocClearTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocClearTagMode.setStatus("current")


class _TmnxMacsecConnAssocReplayWndwSz_Type(Unsigned32):
    """Custom type tmnxMacsecConnAssocReplayWndwSz based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_TmnxMacsecConnAssocReplayWndwSz_Type.__name__ = "Unsigned32"
_TmnxMacsecConnAssocReplayWndwSz_Object = MibTableColumn
tmnxMacsecConnAssocReplayWndwSz = _TmnxMacsecConnAssocReplayWndwSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 10),
    _TmnxMacsecConnAssocReplayWndwSz_Type()
)
tmnxMacsecConnAssocReplayWndwSz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocReplayWndwSz.setStatus("current")


class _TmnxMacsecConnAssocReplayProtect_Type(TruthValue):
    """Custom type tmnxMacsecConnAssocReplayProtect based on TruthValue"""
    defaultValue = 2


_TmnxMacsecConnAssocReplayProtect_Type.__name__ = "TruthValue"
_TmnxMacsecConnAssocReplayProtect_Object = MibTableColumn
tmnxMacsecConnAssocReplayProtect = _TmnxMacsecConnAssocReplayProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 11),
    _TmnxMacsecConnAssocReplayProtect_Type()
)
tmnxMacsecConnAssocReplayProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocReplayProtect.setStatus("current")


class _TmnxMacsecConnAssocCipherSuite_Type(Integer32):
    """Custom type tmnxMacsecConnAssocCipherSuite based on Integer32"""
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
        *(("gcm-aes-128", 1),
          ("gcm-aes-256", 2),
          ("gcm-aes-xpn-128", 3),
          ("gcm-aes-xpn-256", 4))
    )


_TmnxMacsecConnAssocCipherSuite_Type.__name__ = "Integer32"
_TmnxMacsecConnAssocCipherSuite_Object = MibTableColumn
tmnxMacsecConnAssocCipherSuite = _TmnxMacsecConnAssocCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 12),
    _TmnxMacsecConnAssocCipherSuite_Type()
)
tmnxMacsecConnAssocCipherSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocCipherSuite.setStatus("current")


class _TmnxMacsecConnAssocEncrptnOffset_Type(Unsigned32):
    """Custom type tmnxMacsecConnAssocEncrptnOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(50, 50),
    )


_TmnxMacsecConnAssocEncrptnOffset_Type.__name__ = "Unsigned32"
_TmnxMacsecConnAssocEncrptnOffset_Object = MibTableColumn
tmnxMacsecConnAssocEncrptnOffset = _TmnxMacsecConnAssocEncrptnOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 13),
    _TmnxMacsecConnAssocEncrptnOffset_Type()
)
tmnxMacsecConnAssocEncrptnOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocEncrptnOffset.setStatus("current")


class _TmnxMacsecConnAssocDelayProtectn_Type(TruthValue):
    """Custom type tmnxMacsecConnAssocDelayProtectn based on TruthValue"""
    defaultValue = 2


_TmnxMacsecConnAssocDelayProtectn_Type.__name__ = "TruthValue"
_TmnxMacsecConnAssocDelayProtectn_Object = MibTableColumn
tmnxMacsecConnAssocDelayProtectn = _TmnxMacsecConnAssocDelayProtectn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 2, 1, 14),
    _TmnxMacsecConnAssocDelayProtectn_Type()
)
tmnxMacsecConnAssocDelayProtectn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecConnAssocDelayProtectn.setStatus("current")
_TmnxMacsecStaticCakTable_Object = MibTable
tmnxMacsecStaticCakTable = _TmnxMacsecStaticCakTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakTable.setStatus("current")
_TmnxMacsecStaticCakEntry_Object = MibTableRow
tmnxMacsecStaticCakEntry = _TmnxMacsecStaticCakEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakEntry.setStatus("current")
_TmnxMacsecStaticCakLastChanged_Type = TimeStamp
_TmnxMacsecStaticCakLastChanged_Object = MibTableColumn
tmnxMacsecStaticCakLastChanged = _TmnxMacsecStaticCakLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 3, 1, 1),
    _TmnxMacsecStaticCakLastChanged_Type()
)
tmnxMacsecStaticCakLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakLastChanged.setStatus("current")


class _TmnxMacsecStaticCakKeyServerPrio_Type(Unsigned32):
    """Custom type tmnxMacsecStaticCakKeyServerPrio based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxMacsecStaticCakKeyServerPrio_Type.__name__ = "Unsigned32"
_TmnxMacsecStaticCakKeyServerPrio_Object = MibTableColumn
tmnxMacsecStaticCakKeyServerPrio = _TmnxMacsecStaticCakKeyServerPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 3, 1, 2),
    _TmnxMacsecStaticCakKeyServerPrio_Type()
)
tmnxMacsecStaticCakKeyServerPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakKeyServerPrio.setStatus("current")


class _TmnxMacsecStaticCakActivePsk_Type(Unsigned32):
    """Custom type tmnxMacsecStaticCakActivePsk based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxMacsecStaticCakActivePsk_Type.__name__ = "Unsigned32"
_TmnxMacsecStaticCakActivePsk_Object = MibTableColumn
tmnxMacsecStaticCakActivePsk = _TmnxMacsecStaticCakActivePsk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 3, 1, 3),
    _TmnxMacsecStaticCakActivePsk_Type()
)
tmnxMacsecStaticCakActivePsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakActivePsk.setStatus("current")


class _TmnxMacsecStaticCakMkaHelloInt_Type(Unsigned32):
    """Custom type tmnxMacsecStaticCakMkaHelloInt based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
        ValueRangeConstraint(500, 500),
    )


_TmnxMacsecStaticCakMkaHelloInt_Type.__name__ = "Unsigned32"
_TmnxMacsecStaticCakMkaHelloInt_Object = MibTableColumn
tmnxMacsecStaticCakMkaHelloInt = _TmnxMacsecStaticCakMkaHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 3, 1, 4),
    _TmnxMacsecStaticCakMkaHelloInt_Type()
)
tmnxMacsecStaticCakMkaHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecStaticCakMkaHelloInt.setStatus("current")
_TmnxMacsecPreSharedKeyTable_Object = MibTable
tmnxMacsecPreSharedKeyTable = _TmnxMacsecPreSharedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyTable.setStatus("current")
_TmnxMacsecPreSharedKeyEntry_Object = MibTableRow
tmnxMacsecPreSharedKeyEntry = _TmnxMacsecPreSharedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1)
)
tmnxMacsecPreSharedKeyEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocName"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyIndex"),
)
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyEntry.setStatus("current")


class _TmnxMacsecPreSharedKeyIndex_Type(Unsigned32):
    """Custom type tmnxMacsecPreSharedKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxMacsecPreSharedKeyIndex_Type.__name__ = "Unsigned32"
_TmnxMacsecPreSharedKeyIndex_Object = MibTableColumn
tmnxMacsecPreSharedKeyIndex = _TmnxMacsecPreSharedKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1, 1),
    _TmnxMacsecPreSharedKeyIndex_Type()
)
tmnxMacsecPreSharedKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyIndex.setStatus("current")
_TmnxMacsecPreSharedKeyLastChangd_Type = TimeStamp
_TmnxMacsecPreSharedKeyLastChangd_Object = MibTableColumn
tmnxMacsecPreSharedKeyLastChangd = _TmnxMacsecPreSharedKeyLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1, 2),
    _TmnxMacsecPreSharedKeyLastChangd_Type()
)
tmnxMacsecPreSharedKeyLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyLastChangd.setStatus("current")
_TmnxMacsecPreSharedKeyRowStatus_Type = RowStatus
_TmnxMacsecPreSharedKeyRowStatus_Object = MibTableColumn
tmnxMacsecPreSharedKeyRowStatus = _TmnxMacsecPreSharedKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1, 3),
    _TmnxMacsecPreSharedKeyRowStatus_Type()
)
tmnxMacsecPreSharedKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyRowStatus.setStatus("current")


class _TmnxMacsecPreSharedKeyEncrptType_Type(Integer32):
    """Custom type tmnxMacsecPreSharedKeyEncrptType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes-128-cmac", 1),
          ("aes-256-cmac", 2))
    )


_TmnxMacsecPreSharedKeyEncrptType_Type.__name__ = "Integer32"
_TmnxMacsecPreSharedKeyEncrptType_Object = MibTableColumn
tmnxMacsecPreSharedKeyEncrptType = _TmnxMacsecPreSharedKeyEncrptType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1, 4),
    _TmnxMacsecPreSharedKeyEncrptType_Type()
)
tmnxMacsecPreSharedKeyEncrptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyEncrptType.setStatus("current")


class _TmnxMacsecPreSharedKeyCak_Type(DisplayString):
    """Custom type tmnxMacsecPreSharedKeyCak based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxMacsecPreSharedKeyCak_Type.__name__ = "DisplayString"
_TmnxMacsecPreSharedKeyCak_Object = MibTableColumn
tmnxMacsecPreSharedKeyCak = _TmnxMacsecPreSharedKeyCak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1, 5),
    _TmnxMacsecPreSharedKeyCak_Type()
)
tmnxMacsecPreSharedKeyCak.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyCak.setStatus("current")


class _TmnxMacsecPreSharedKeyCakName_Type(DisplayString):
    """Custom type tmnxMacsecPreSharedKeyCakName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxMacsecPreSharedKeyCakName_Type.__name__ = "DisplayString"
_TmnxMacsecPreSharedKeyCakName_Object = MibTableColumn
tmnxMacsecPreSharedKeyCakName = _TmnxMacsecPreSharedKeyCakName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 4, 1, 6),
    _TmnxMacsecPreSharedKeyCakName_Type()
)
tmnxMacsecPreSharedKeyCakName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPreSharedKeyCakName.setStatus("current")
_TmnxMacsecPortTable_Object = MibTable
tmnxMacsecPortTable = _TmnxMacsecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxMacsecPortTable.setStatus("current")
_TmnxMacsecPortEntry_Object = MibTableRow
tmnxMacsecPortEntry = _TmnxMacsecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1)
)
tmnxMacsecPortEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
)
if mibBuilder.loadTexts:
    tmnxMacsecPortEntry.setStatus("current")
_TmnxMacsecPortId_Type = TmnxPortID
_TmnxMacsecPortId_Object = MibTableColumn
tmnxMacsecPortId = _TmnxMacsecPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 1),
    _TmnxMacsecPortId_Type()
)
tmnxMacsecPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecPortId.setStatus("current")


class _TmnxMacsecVlanId_Type(Integer32):
    """Custom type tmnxMacsecVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TmnxMacsecVlanId_Type.__name__ = "Integer32"
_TmnxMacsecVlanId_Object = MibTableColumn
tmnxMacsecVlanId = _TmnxMacsecVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 2),
    _TmnxMacsecVlanId_Type()
)
tmnxMacsecVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecVlanId.setStatus("current")
_TmnxMacsecPortLastChanged_Type = TimeStamp
_TmnxMacsecPortLastChanged_Object = MibTableColumn
tmnxMacsecPortLastChanged = _TmnxMacsecPortLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 3),
    _TmnxMacsecPortLastChanged_Type()
)
tmnxMacsecPortLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortLastChanged.setStatus("current")


class _TmnxMacsecPortEapolDestAddress_Type(MacAddress):
    """Custom type tmnxMacsecPortEapolDestAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMacsecPortEapolDestAddress_Type.__name__ = "MacAddress"
_TmnxMacsecPortEapolDestAddress_Object = MibTableColumn
tmnxMacsecPortEapolDestAddress = _TmnxMacsecPortEapolDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 4),
    _TmnxMacsecPortEapolDestAddress_Type()
)
tmnxMacsecPortEapolDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortEapolDestAddress.setStatus("current")


class _TmnxMacsecPortCaName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMacsecPortCaName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMacsecPortCaName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMacsecPortCaName_Object = MibTableColumn
tmnxMacsecPortCaName = _TmnxMacsecPortCaName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 5),
    _TmnxMacsecPortCaName_Type()
)
tmnxMacsecPortCaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortCaName.setStatus("current")


class _TmnxMacsecPortAdminState_Type(TmnxAdminState):
    """Custom type tmnxMacsecPortAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMacsecPortAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMacsecPortAdminState_Object = MibTableColumn
tmnxMacsecPortAdminState = _TmnxMacsecPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 6),
    _TmnxMacsecPortAdminState_Type()
)
tmnxMacsecPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortAdminState.setStatus("current")


class _TmnxMacsecPortMaxPeers_Type(Unsigned32):
    """Custom type tmnxMacsecPortMaxPeers based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxMacsecPortMaxPeers_Type.__name__ = "Unsigned32"
_TmnxMacsecPortMaxPeers_Object = MibTableColumn
tmnxMacsecPortMaxPeers = _TmnxMacsecPortMaxPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 7),
    _TmnxMacsecPortMaxPeers_Type()
)
tmnxMacsecPortMaxPeers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortMaxPeers.setStatus("current")


class _TmnxMacsecPortExcludeLacp_Type(TruthValue):
    """Custom type tmnxMacsecPortExcludeLacp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortExcludeLacp_Type.__name__ = "TruthValue"
_TmnxMacsecPortExcludeLacp_Object = MibTableColumn
tmnxMacsecPortExcludeLacp = _TmnxMacsecPortExcludeLacp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 8),
    _TmnxMacsecPortExcludeLacp_Type()
)
tmnxMacsecPortExcludeLacp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortExcludeLacp.setStatus("obsolete")


class _TmnxMacsecPortExcludeLldp_Type(TruthValue):
    """Custom type tmnxMacsecPortExcludeLldp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortExcludeLldp_Type.__name__ = "TruthValue"
_TmnxMacsecPortExcludeLldp_Object = MibTableColumn
tmnxMacsecPortExcludeLldp = _TmnxMacsecPortExcludeLldp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 9),
    _TmnxMacsecPortExcludeLldp_Type()
)
tmnxMacsecPortExcludeLldp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortExcludeLldp.setStatus("obsolete")


class _TmnxMacsecPortExcludeCdp_Type(TruthValue):
    """Custom type tmnxMacsecPortExcludeCdp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortExcludeCdp_Type.__name__ = "TruthValue"
_TmnxMacsecPortExcludeCdp_Object = MibTableColumn
tmnxMacsecPortExcludeCdp = _TmnxMacsecPortExcludeCdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 10),
    _TmnxMacsecPortExcludeCdp_Type()
)
tmnxMacsecPortExcludeCdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortExcludeCdp.setStatus("obsolete")


class _TmnxMacsecPortExcludeEapolStart_Type(TruthValue):
    """Custom type tmnxMacsecPortExcludeEapolStart based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortExcludeEapolStart_Type.__name__ = "TruthValue"
_TmnxMacsecPortExcludeEapolStart_Object = MibTableColumn
tmnxMacsecPortExcludeEapolStart = _TmnxMacsecPortExcludeEapolStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 11),
    _TmnxMacsecPortExcludeEapolStart_Type()
)
tmnxMacsecPortExcludeEapolStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortExcludeEapolStart.setStatus("obsolete")


class _TmnxMacsecPortRxTrafficEncrption_Type(TruthValue):
    """Custom type tmnxMacsecPortRxTrafficEncrption based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortRxTrafficEncrption_Type.__name__ = "TruthValue"
_TmnxMacsecPortRxTrafficEncrption_Object = MibTableColumn
tmnxMacsecPortRxTrafficEncrption = _TmnxMacsecPortRxTrafficEncrption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 12),
    _TmnxMacsecPortRxTrafficEncrption_Type()
)
tmnxMacsecPortRxTrafficEncrption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortRxTrafficEncrption.setStatus("obsolete")
_TmnxMacsecPortRowStatus_Type = RowStatus
_TmnxMacsecPortRowStatus_Object = MibTableColumn
tmnxMacsecPortRowStatus = _TmnxMacsecPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 13),
    _TmnxMacsecPortRowStatus_Type()
)
tmnxMacsecPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortRowStatus.setStatus("current")


class _TmnxMacsecPortEncapType_Type(Integer32):
    """Custom type tmnxMacsecPortEncapType based on Integer32"""
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
        *(("all-match", 1),
          ("untagged", 2),
          ("single-tag", 3),
          ("double-tag", 4))
    )


_TmnxMacsecPortEncapType_Type.__name__ = "Integer32"
_TmnxMacsecPortEncapType_Object = MibTableColumn
tmnxMacsecPortEncapType = _TmnxMacsecPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 14),
    _TmnxMacsecPortEncapType_Type()
)
tmnxMacsecPortEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortEncapType.setStatus("current")
_TmnxMacsecPortEncapMatch_Type = TmnxEncapVal
_TmnxMacsecPortEncapMatch_Object = MibTableColumn
tmnxMacsecPortEncapMatch = _TmnxMacsecPortEncapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 5, 1, 15),
    _TmnxMacsecPortEncapMatch_Type()
)
tmnxMacsecPortEncapMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecPortEncapMatch.setStatus("current")
_TmnxMacsecPortGlobalTable_Object = MibTable
tmnxMacsecPortGlobalTable = _TmnxMacsecPortGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalTable.setStatus("current")
_TmnxMacsecPortGlobalEntry_Object = MibTableRow
tmnxMacsecPortGlobalEntry = _TmnxMacsecPortGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1)
)
tmnxMacsecPortGlobalEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
)
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalEntry.setStatus("current")


class _TmnxMacsecPortGlobalRxTrafEncrpt_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalRxTrafEncrpt based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalRxTrafEncrpt_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalRxTrafEncrpt_Object = MibTableColumn
tmnxMacsecPortGlobalRxTrafEncrpt = _TmnxMacsecPortGlobalRxTrafEncrpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 1),
    _TmnxMacsecPortGlobalRxTrafEncrpt_Type()
)
tmnxMacsecPortGlobalRxTrafEncrpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalRxTrafEncrpt.setStatus("current")


class _TmnxMacsecPortGlobalExcludeLacp_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcludeLacp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcludeLacp_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcludeLacp_Object = MibTableColumn
tmnxMacsecPortGlobalExcludeLacp = _TmnxMacsecPortGlobalExcludeLacp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 2),
    _TmnxMacsecPortGlobalExcludeLacp_Type()
)
tmnxMacsecPortGlobalExcludeLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcludeLacp.setStatus("current")


class _TmnxMacsecPortGlobalExcludeLldp_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcludeLldp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcludeLldp_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcludeLldp_Object = MibTableColumn
tmnxMacsecPortGlobalExcludeLldp = _TmnxMacsecPortGlobalExcludeLldp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 3),
    _TmnxMacsecPortGlobalExcludeLldp_Type()
)
tmnxMacsecPortGlobalExcludeLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcludeLldp.setStatus("current")


class _TmnxMacsecPortGlobalExcludeCdp_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcludeCdp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcludeCdp_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcludeCdp_Object = MibTableColumn
tmnxMacsecPortGlobalExcludeCdp = _TmnxMacsecPortGlobalExcludeCdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 4),
    _TmnxMacsecPortGlobalExcludeCdp_Type()
)
tmnxMacsecPortGlobalExcludeCdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcludeCdp.setStatus("current")


class _TmnxMacsecPortGlblExcldEaplStart_Type(TruthValue):
    """Custom type tmnxMacsecPortGlblExcldEaplStart based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlblExcldEaplStart_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlblExcldEaplStart_Object = MibTableColumn
tmnxMacsecPortGlblExcldEaplStart = _TmnxMacsecPortGlblExcldEaplStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 5),
    _TmnxMacsecPortGlblExcldEaplStart_Type()
)
tmnxMacsecPortGlblExcldEaplStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlblExcldEaplStart.setStatus("current")


class _TmnxMacsecPortGlobalExcldeEfmOam_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcldeEfmOam based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcldeEfmOam_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcldeEfmOam_Object = MibTableColumn
tmnxMacsecPortGlobalExcldeEfmOam = _TmnxMacsecPortGlobalExcldeEfmOam_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 6),
    _TmnxMacsecPortGlobalExcldeEfmOam_Type()
)
tmnxMacsecPortGlobalExcldeEfmOam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcldeEfmOam.setStatus("current")


class _TmnxMacsecPortGlobalExcldeEthCfm_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcldeEthCfm based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcldeEthCfm_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcldeEthCfm_Object = MibTableColumn
tmnxMacsecPortGlobalExcldeEthCfm = _TmnxMacsecPortGlobalExcldeEthCfm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 7),
    _TmnxMacsecPortGlobalExcldeEthCfm_Type()
)
tmnxMacsecPortGlobalExcldeEthCfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcldeEthCfm.setStatus("current")


class _TmnxMacsecPortGlobalExcludePtp_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcludePtp based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcludePtp_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcludePtp_Object = MibTableColumn
tmnxMacsecPortGlobalExcludePtp = _TmnxMacsecPortGlobalExcludePtp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 8),
    _TmnxMacsecPortGlobalExcludePtp_Type()
)
tmnxMacsecPortGlobalExcludePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcludePtp.setStatus("current")


class _TmnxMacsecPortGlobalExcludeUbfd_Type(TruthValue):
    """Custom type tmnxMacsecPortGlobalExcludeUbfd based on TruthValue"""
    defaultValue = 2


_TmnxMacsecPortGlobalExcludeUbfd_Type.__name__ = "TruthValue"
_TmnxMacsecPortGlobalExcludeUbfd_Object = MibTableColumn
tmnxMacsecPortGlobalExcludeUbfd = _TmnxMacsecPortGlobalExcludeUbfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 9),
    _TmnxMacsecPortGlobalExcludeUbfd_Type()
)
tmnxMacsecPortGlobalExcludeUbfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlobalExcludeUbfd.setStatus("current")


class _TmnxMacsecPortGlblExcldMacPolicy_Type(Unsigned32):
    """Custom type tmnxMacsecPortGlblExcldMacPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_TmnxMacsecPortGlblExcldMacPolicy_Type.__name__ = "Unsigned32"
_TmnxMacsecPortGlblExcldMacPolicy_Object = MibTableColumn
tmnxMacsecPortGlblExcldMacPolicy = _TmnxMacsecPortGlblExcldMacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 6, 1, 10),
    _TmnxMacsecPortGlblExcldMacPolicy_Type()
)
tmnxMacsecPortGlblExcldMacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMacsecPortGlblExcldMacPolicy.setStatus("current")
_TmnxMacsecMacPolicyGroupTable_Object = MibTable
tmnxMacsecMacPolicyGroupTable = _TmnxMacsecMacPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxMacsecMacPolicyGroupTable.setStatus("current")
_TmnxMacsecMacPolicyGroupEntry_Object = MibTableRow
tmnxMacsecMacPolicyGroupEntry = _TmnxMacsecMacPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 7, 1)
)
tmnxMacsecMacPolicyGroupEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecMacPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxMacsecMacPolicyGroupEntry.setStatus("current")


class _TmnxMacsecMacPolicyId_Type(Unsigned32):
    """Custom type tmnxMacsecMacPolicyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxMacsecMacPolicyId_Type.__name__ = "Unsigned32"
_TmnxMacsecMacPolicyId_Object = MibTableColumn
tmnxMacsecMacPolicyId = _TmnxMacsecMacPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 7, 1, 1),
    _TmnxMacsecMacPolicyId_Type()
)
tmnxMacsecMacPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecMacPolicyId.setStatus("current")
_TmnxMacsecMacPolicyGrpRowStatus_Type = RowStatus
_TmnxMacsecMacPolicyGrpRowStatus_Object = MibTableColumn
tmnxMacsecMacPolicyGrpRowStatus = _TmnxMacsecMacPolicyGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 7, 1, 2),
    _TmnxMacsecMacPolicyGrpRowStatus_Type()
)
tmnxMacsecMacPolicyGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecMacPolicyGrpRowStatus.setStatus("current")
_TmnxMacsecDestMacAddressTable_Object = MibTable
tmnxMacsecDestMacAddressTable = _TmnxMacsecDestMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxMacsecDestMacAddressTable.setStatus("current")
_TmnxMacsecDestMacAddressEntry_Object = MibTableRow
tmnxMacsecDestMacAddressEntry = _TmnxMacsecDestMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 8, 2)
)
tmnxMacsecDestMacAddressEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecMacPolicyId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecDestMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxMacsecDestMacAddressEntry.setStatus("current")
_TmnxMacsecDestMacAddress_Type = MacAddress
_TmnxMacsecDestMacAddress_Object = MibTableColumn
tmnxMacsecDestMacAddress = _TmnxMacsecDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 8, 2, 1),
    _TmnxMacsecDestMacAddress_Type()
)
tmnxMacsecDestMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecDestMacAddress.setStatus("current")
_TmnxMacsecDestMacAddrRowStatus_Type = RowStatus
_TmnxMacsecDestMacAddrRowStatus_Object = MibTableColumn
tmnxMacsecDestMacAddrRowStatus = _TmnxMacsecDestMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 2, 8, 2, 2),
    _TmnxMacsecDestMacAddrRowStatus_Type()
)
tmnxMacsecDestMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacsecDestMacAddrRowStatus.setStatus("current")
_TmnxMacsecStats_ObjectIdentity = ObjectIdentity
tmnxMacsecStats = _TmnxMacsecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3)
)
_TmnxMacsecStatsObjects_ObjectIdentity = ObjectIdentity
tmnxMacsecStatsObjects = _TmnxMacsecStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 1)
)
_TmnxMacsecMkaStatsTable_Object = MibTable
tmnxMacsecMkaStatsTable = _TmnxMacsecMkaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsTable.setStatus("current")
_TmnxMacsecMkaStatsEntry_Object = MibTableRow
tmnxMacsecMkaStatsEntry = _TmnxMacsecMkaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1)
)
tmnxMacsecMkaStatsEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecCkn"),
)
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsEntry.setStatus("current")


class _TmnxMacsecCkn_Type(OctetString):
    """Custom type tmnxMacsecCkn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxMacsecCkn_Type.__name__ = "OctetString"
_TmnxMacsecCkn_Object = MibTableColumn
tmnxMacsecCkn = _TmnxMacsecCkn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 1),
    _TmnxMacsecCkn_Type()
)
tmnxMacsecCkn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecCkn.setStatus("current")


class _TmnxMacsecMkaStatsMemberId_Type(OctetString):
    """Custom type tmnxMacsecMkaStatsMemberId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_TmnxMacsecMkaStatsMemberId_Type.__name__ = "OctetString"
_TmnxMacsecMkaStatsMemberId_Object = MibTableColumn
tmnxMacsecMkaStatsMemberId = _TmnxMacsecMkaStatsMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 2),
    _TmnxMacsecMkaStatsMemberId_Type()
)
tmnxMacsecMkaStatsMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsMemberId.setStatus("current")


class _TmnxMacsecMkaStatsCakName_Type(DisplayString):
    """Custom type tmnxMacsecMkaStatsCakName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxMacsecMkaStatsCakName_Type.__name__ = "DisplayString"
_TmnxMacsecMkaStatsCakName_Object = MibTableColumn
tmnxMacsecMkaStatsCakName = _TmnxMacsecMkaStatsCakName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 3),
    _TmnxMacsecMkaStatsCakName_Type()
)
tmnxMacsecMkaStatsCakName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsCakName.setStatus("current")
_TmnxMacsecMkaStatsTransmitInt_Type = Unsigned32
_TmnxMacsecMkaStatsTransmitInt_Object = MibTableColumn
tmnxMacsecMkaStatsTransmitInt = _TmnxMacsecMkaStatsTransmitInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 4),
    _TmnxMacsecMkaStatsTransmitInt_Type()
)
tmnxMacsecMkaStatsTransmitInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsTransmitInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsTransmitInt.setUnits("milliseconds")


class _TmnxMacsecMkaStatsOutboundSci_Type(OctetString):
    """Custom type tmnxMacsecMkaStatsOutboundSci based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxMacsecMkaStatsOutboundSci_Type.__name__ = "OctetString"
_TmnxMacsecMkaStatsOutboundSci_Object = MibTableColumn
tmnxMacsecMkaStatsOutboundSci = _TmnxMacsecMkaStatsOutboundSci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 5),
    _TmnxMacsecMkaStatsOutboundSci_Type()
)
tmnxMacsecMkaStatsOutboundSci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsOutboundSci.setStatus("current")
_TmnxMacsecMkaStatsMessageNumber_Type = Unsigned32
_TmnxMacsecMkaStatsMessageNumber_Object = MibTableColumn
tmnxMacsecMkaStatsMessageNumber = _TmnxMacsecMkaStatsMessageNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 6),
    _TmnxMacsecMkaStatsMessageNumber_Type()
)
tmnxMacsecMkaStatsMessageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsMessageNumber.setStatus("current")
_TmnxMacsecMkaStatsKeyNumber_Type = Unsigned32
_TmnxMacsecMkaStatsKeyNumber_Object = MibTableColumn
tmnxMacsecMkaStatsKeyNumber = _TmnxMacsecMkaStatsKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 7),
    _TmnxMacsecMkaStatsKeyNumber_Type()
)
tmnxMacsecMkaStatsKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsKeyNumber.setStatus("current")
_TmnxMacsecMkaStatsKeyServer_Type = TruthValue
_TmnxMacsecMkaStatsKeyServer_Object = MibTableColumn
tmnxMacsecMkaStatsKeyServer = _TmnxMacsecMkaStatsKeyServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 8),
    _TmnxMacsecMkaStatsKeyServer_Type()
)
tmnxMacsecMkaStatsKeyServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsKeyServer.setStatus("current")
_TmnxMacsecMkaStatsKeyServerPrio_Type = Unsigned32
_TmnxMacsecMkaStatsKeyServerPrio_Object = MibTableColumn
tmnxMacsecMkaStatsKeyServerPrio = _TmnxMacsecMkaStatsKeyServerPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 9),
    _TmnxMacsecMkaStatsKeyServerPrio_Type()
)
tmnxMacsecMkaStatsKeyServerPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsKeyServerPrio.setStatus("current")
_TmnxMacsecMkaStatsLatestSakAn_Type = Unsigned32
_TmnxMacsecMkaStatsLatestSakAn_Object = MibTableColumn
tmnxMacsecMkaStatsLatestSakAn = _TmnxMacsecMkaStatsLatestSakAn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 10),
    _TmnxMacsecMkaStatsLatestSakAn_Type()
)
tmnxMacsecMkaStatsLatestSakAn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsLatestSakAn.setStatus("current")


class _TmnxMacsecMkaStatsLatestSakKi_Type(OctetString):
    """Custom type tmnxMacsecMkaStatsLatestSakKi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxMacsecMkaStatsLatestSakKi_Type.__name__ = "OctetString"
_TmnxMacsecMkaStatsLatestSakKi_Object = MibTableColumn
tmnxMacsecMkaStatsLatestSakKi = _TmnxMacsecMkaStatsLatestSakKi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 11),
    _TmnxMacsecMkaStatsLatestSakKi_Type()
)
tmnxMacsecMkaStatsLatestSakKi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsLatestSakKi.setStatus("current")
_TmnxMacsecMkaStatsPreviousSakAn_Type = Unsigned32
_TmnxMacsecMkaStatsPreviousSakAn_Object = MibTableColumn
tmnxMacsecMkaStatsPreviousSakAn = _TmnxMacsecMkaStatsPreviousSakAn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 12),
    _TmnxMacsecMkaStatsPreviousSakAn_Type()
)
tmnxMacsecMkaStatsPreviousSakAn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPreviousSakAn.setStatus("current")


class _TmnxMacsecMkaStatsPreviousSakKi_Type(OctetString):
    """Custom type tmnxMacsecMkaStatsPreviousSakKi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxMacsecMkaStatsPreviousSakKi_Type.__name__ = "OctetString"
_TmnxMacsecMkaStatsPreviousSakKi_Object = MibTableColumn
tmnxMacsecMkaStatsPreviousSakKi = _TmnxMacsecMkaStatsPreviousSakKi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 13),
    _TmnxMacsecMkaStatsPreviousSakKi_Type()
)
tmnxMacsecMkaStatsPreviousSakKi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPreviousSakKi.setStatus("current")
_TmnxMacsecMkaStatsPeerRemTimeout_Type = Counter64
_TmnxMacsecMkaStatsPeerRemTimeout_Object = MibTableColumn
tmnxMacsecMkaStatsPeerRemTimeout = _TmnxMacsecMkaStatsPeerRemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 14),
    _TmnxMacsecMkaStatsPeerRemTimeout_Type()
)
tmnxMacsecMkaStatsPeerRemTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPeerRemTimeout.setStatus("current")
_TmnxMacsecMkaStatsCknNotFound_Type = Counter64
_TmnxMacsecMkaStatsCknNotFound_Object = MibTableColumn
tmnxMacsecMkaStatsCknNotFound = _TmnxMacsecMkaStatsCknNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 15),
    _TmnxMacsecMkaStatsCknNotFound_Type()
)
tmnxMacsecMkaStatsCknNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsCknNotFound.setStatus("current")
_TmnxMacsecMkaStatsNewLivePeer_Type = Counter64
_TmnxMacsecMkaStatsNewLivePeer_Object = MibTableColumn
tmnxMacsecMkaStatsNewLivePeer = _TmnxMacsecMkaStatsNewLivePeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 16),
    _TmnxMacsecMkaStatsNewLivePeer_Type()
)
tmnxMacsecMkaStatsNewLivePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsNewLivePeer.setStatus("current")
_TmnxMacsecMkaStatsSakGenerated_Type = Counter64
_TmnxMacsecMkaStatsSakGenerated_Object = MibTableColumn
tmnxMacsecMkaStatsSakGenerated = _TmnxMacsecMkaStatsSakGenerated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 17),
    _TmnxMacsecMkaStatsSakGenerated_Type()
)
tmnxMacsecMkaStatsSakGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakGenerated.setStatus("current")
_TmnxMacsecMkaStatsSakInstalledTx_Type = Counter64
_TmnxMacsecMkaStatsSakInstalledTx_Object = MibTableColumn
tmnxMacsecMkaStatsSakInstalledTx = _TmnxMacsecMkaStatsSakInstalledTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 18),
    _TmnxMacsecMkaStatsSakInstalledTx_Type()
)
tmnxMacsecMkaStatsSakInstalledTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakInstalledTx.setStatus("current")
_TmnxMacsecMkaStatsSakInstalledRx_Type = Counter64
_TmnxMacsecMkaStatsSakInstalledRx_Object = MibTableColumn
tmnxMacsecMkaStatsSakInstalledRx = _TmnxMacsecMkaStatsSakInstalledRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 19),
    _TmnxMacsecMkaStatsSakInstalledRx_Type()
)
tmnxMacsecMkaStatsSakInstalledRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakInstalledRx.setStatus("current")
_TmnxMacsecMkaStatsPduTooSmall_Type = Counter64
_TmnxMacsecMkaStatsPduTooSmall_Object = MibTableColumn
tmnxMacsecMkaStatsPduTooSmall = _TmnxMacsecMkaStatsPduTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 20),
    _TmnxMacsecMkaStatsPduTooSmall_Type()
)
tmnxMacsecMkaStatsPduTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPduTooSmall.setStatus("current")
_TmnxMacsecMkaStatsPduTooBig_Type = Counter64
_TmnxMacsecMkaStatsPduTooBig_Object = MibTableColumn
tmnxMacsecMkaStatsPduTooBig = _TmnxMacsecMkaStatsPduTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 21),
    _TmnxMacsecMkaStatsPduTooBig_Type()
)
tmnxMacsecMkaStatsPduTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPduTooBig.setStatus("current")
_TmnxMacsecMkaStatsPduNotQuadSize_Type = Counter64
_TmnxMacsecMkaStatsPduNotQuadSize_Object = MibTableColumn
tmnxMacsecMkaStatsPduNotQuadSize = _TmnxMacsecMkaStatsPduNotQuadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 22),
    _TmnxMacsecMkaStatsPduNotQuadSize_Type()
)
tmnxMacsecMkaStatsPduNotQuadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPduNotQuadSize.setStatus("current")
_TmnxMacsecMkaStatsPduInvalidNum_Type = Counter64
_TmnxMacsecMkaStatsPduInvalidNum_Object = MibTableColumn
tmnxMacsecMkaStatsPduInvalidNum = _TmnxMacsecMkaStatsPduInvalidNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 23),
    _TmnxMacsecMkaStatsPduInvalidNum_Type()
)
tmnxMacsecMkaStatsPduInvalidNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPduInvalidNum.setStatus("current")
_TmnxMacsecMkaStatsParamSzInvalid_Type = Counter64
_TmnxMacsecMkaStatsParamSzInvalid_Object = MibTableColumn
tmnxMacsecMkaStatsParamSzInvalid = _TmnxMacsecMkaStatsParamSzInvalid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 24),
    _TmnxMacsecMkaStatsParamSzInvalid_Type()
)
tmnxMacsecMkaStatsParamSzInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsParamSzInvalid.setStatus("current")
_TmnxMacsecMkaStatsLvnessChckFail_Type = Counter64
_TmnxMacsecMkaStatsLvnessChckFail_Object = MibTableColumn
tmnxMacsecMkaStatsLvnessChckFail = _TmnxMacsecMkaStatsLvnessChckFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 25),
    _TmnxMacsecMkaStatsLvnessChckFail_Type()
)
tmnxMacsecMkaStatsLvnessChckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsLvnessChckFail.setStatus("current")
_TmnxMacsecMkaStatsParamNotQuadSz_Type = Counter64
_TmnxMacsecMkaStatsParamNotQuadSz_Object = MibTableColumn
tmnxMacsecMkaStatsParamNotQuadSz = _TmnxMacsecMkaStatsParamNotQuadSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 26),
    _TmnxMacsecMkaStatsParamNotQuadSz_Type()
)
tmnxMacsecMkaStatsParamNotQuadSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsParamNotQuadSz.setStatus("current")
_TmnxMacsecMkaStatsUnsupportedAgi_Type = Counter64
_TmnxMacsecMkaStatsUnsupportedAgi_Object = MibTableColumn
tmnxMacsecMkaStatsUnsupportedAgi = _TmnxMacsecMkaStatsUnsupportedAgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 27),
    _TmnxMacsecMkaStatsUnsupportedAgi_Type()
)
tmnxMacsecMkaStatsUnsupportedAgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsUnsupportedAgi.setStatus("current")
_TmnxMacsecMkaStatsInvldCknLength_Type = Counter64
_TmnxMacsecMkaStatsInvldCknLength_Object = MibTableColumn
tmnxMacsecMkaStatsInvldCknLength = _TmnxMacsecMkaStatsInvldCknLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 28),
    _TmnxMacsecMkaStatsInvldCknLength_Type()
)
tmnxMacsecMkaStatsInvldCknLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsInvldCknLength.setStatus("current")
_TmnxMacsecMkaStatsIcvCheckFailed_Type = Counter64
_TmnxMacsecMkaStatsIcvCheckFailed_Object = MibTableColumn
tmnxMacsecMkaStatsIcvCheckFailed = _TmnxMacsecMkaStatsIcvCheckFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 29),
    _TmnxMacsecMkaStatsIcvCheckFailed_Type()
)
tmnxMacsecMkaStatsIcvCheckFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsIcvCheckFailed.setStatus("current")
_TmnxMacsecMkaStatsPeerSameMid_Type = Counter64
_TmnxMacsecMkaStatsPeerSameMid_Object = MibTableColumn
tmnxMacsecMkaStatsPeerSameMid = _TmnxMacsecMkaStatsPeerSameMid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 30),
    _TmnxMacsecMkaStatsPeerSameMid_Type()
)
tmnxMacsecMkaStatsPeerSameMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPeerSameMid.setStatus("current")
_TmnxMacsecMkaStatsSakNonLivePeer_Type = Counter64
_TmnxMacsecMkaStatsSakNonLivePeer_Object = MibTableColumn
tmnxMacsecMkaStatsSakNonLivePeer = _TmnxMacsecMkaStatsSakNonLivePeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 31),
    _TmnxMacsecMkaStatsSakNonLivePeer_Type()
)
tmnxMacsecMkaStatsSakNonLivePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakNonLivePeer.setStatus("current")
_TmnxMacsecMkaStatsSakNoKeyServer_Type = Counter64
_TmnxMacsecMkaStatsSakNoKeyServer_Object = MibTableColumn
tmnxMacsecMkaStatsSakNoKeyServer = _TmnxMacsecMkaStatsSakNoKeyServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 32),
    _TmnxMacsecMkaStatsSakNoKeyServer_Type()
)
tmnxMacsecMkaStatsSakNoKeyServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakNoKeyServer.setStatus("current")
_TmnxMacsecMkaStatsSakDecryptFail_Type = Counter64
_TmnxMacsecMkaStatsSakDecryptFail_Object = MibTableColumn
tmnxMacsecMkaStatsSakDecryptFail = _TmnxMacsecMkaStatsSakDecryptFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 33),
    _TmnxMacsecMkaStatsSakDecryptFail_Type()
)
tmnxMacsecMkaStatsSakDecryptFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakDecryptFail.setStatus("current")
_TmnxMacsecMkaStatsSakEncryptFail_Type = Counter64
_TmnxMacsecMkaStatsSakEncryptFail_Object = MibTableColumn
tmnxMacsecMkaStatsSakEncryptFail = _TmnxMacsecMkaStatsSakEncryptFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 34),
    _TmnxMacsecMkaStatsSakEncryptFail_Type()
)
tmnxMacsecMkaStatsSakEncryptFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakEncryptFail.setStatus("current")
_TmnxMacsecMkaStatsKeyNumInvalid_Type = Counter64
_TmnxMacsecMkaStatsKeyNumInvalid_Object = MibTableColumn
tmnxMacsecMkaStatsKeyNumInvalid = _TmnxMacsecMkaStatsKeyNumInvalid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 35),
    _TmnxMacsecMkaStatsKeyNumInvalid_Type()
)
tmnxMacsecMkaStatsKeyNumInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsKeyNumInvalid.setStatus("current")
_TmnxMacsecMkaStatsSakInstallFail_Type = Counter64
_TmnxMacsecMkaStatsSakInstallFail_Object = MibTableColumn
tmnxMacsecMkaStatsSakInstallFail = _TmnxMacsecMkaStatsSakInstallFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 36),
    _TmnxMacsecMkaStatsSakInstallFail_Type()
)
tmnxMacsecMkaStatsSakInstallFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsSakInstallFail.setStatus("current")
_TmnxMacsecMkaStatsCakInfoMissing_Type = Counter64
_TmnxMacsecMkaStatsCakInfoMissing_Object = MibTableColumn
tmnxMacsecMkaStatsCakInfoMissing = _TmnxMacsecMkaStatsCakInfoMissing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 37),
    _TmnxMacsecMkaStatsCakInfoMissing_Type()
)
tmnxMacsecMkaStatsCakInfoMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsCakInfoMissing.setStatus("current")
_TmnxMacsecMkaStatsMxPeersSetZero_Type = Counter64
_TmnxMacsecMkaStatsMxPeersSetZero_Object = MibTableColumn
tmnxMacsecMkaStatsMxPeersSetZero = _TmnxMacsecMkaStatsMxPeersSetZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 38),
    _TmnxMacsecMkaStatsMxPeersSetZero_Type()
)
tmnxMacsecMkaStatsMxPeersSetZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsMxPeersSetZero.setStatus("current")
_TmnxMacsecMkaStatsOperState_Type = TmnxOperState
_TmnxMacsecMkaStatsOperState_Object = MibTableColumn
tmnxMacsecMkaStatsOperState = _TmnxMacsecMkaStatsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 39),
    _TmnxMacsecMkaStatsOperState_Type()
)
tmnxMacsecMkaStatsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsOperState.setStatus("current")


class _TmnxMacsecMkaStatsOperOffset_Type(Unsigned32):
    """Custom type tmnxMacsecMkaStatsOperOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(50, 50),
    )


_TmnxMacsecMkaStatsOperOffset_Type.__name__ = "Unsigned32"
_TmnxMacsecMkaStatsOperOffset_Object = MibTableColumn
tmnxMacsecMkaStatsOperOffset = _TmnxMacsecMkaStatsOperOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 40),
    _TmnxMacsecMkaStatsOperOffset_Type()
)
tmnxMacsecMkaStatsOperOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsOperOffset.setStatus("current")


class _TmnxMacsecMkaStatsOperCipher_Type(Integer32):
    """Custom type tmnxMacsecMkaStatsOperCipher based on Integer32"""
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
        *(("gcm-aes-128", 1),
          ("gcm-aes-256", 2),
          ("gcm-aes-xpn-128", 3),
          ("gcm-aes-xpn-256", 4))
    )


_TmnxMacsecMkaStatsOperCipher_Type.__name__ = "Integer32"
_TmnxMacsecMkaStatsOperCipher_Object = MibTableColumn
tmnxMacsecMkaStatsOperCipher = _TmnxMacsecMkaStatsOperCipher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 41),
    _TmnxMacsecMkaStatsOperCipher_Type()
)
tmnxMacsecMkaStatsOperCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsOperCipher.setStatus("current")
_TmnxMacsecMkaStatsLatestSakLpn_Type = Counter64
_TmnxMacsecMkaStatsLatestSakLpn_Object = MibTableColumn
tmnxMacsecMkaStatsLatestSakLpn = _TmnxMacsecMkaStatsLatestSakLpn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 42),
    _TmnxMacsecMkaStatsLatestSakLpn_Type()
)
tmnxMacsecMkaStatsLatestSakLpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsLatestSakLpn.setStatus("current")
_TmnxMacsecMkaStatsPreviousSakLpn_Type = Counter64
_TmnxMacsecMkaStatsPreviousSakLpn_Object = MibTableColumn
tmnxMacsecMkaStatsPreviousSakLpn = _TmnxMacsecMkaStatsPreviousSakLpn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 43),
    _TmnxMacsecMkaStatsPreviousSakLpn_Type()
)
tmnxMacsecMkaStatsPreviousSakLpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsPreviousSakLpn.setStatus("current")


class _TmnxMacsecMkaStatsEncapType_Type(Integer32):
    """Custom type tmnxMacsecMkaStatsEncapType based on Integer32"""
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
        *(("all-match", 1),
          ("untagged", 2),
          ("single-tag", 3),
          ("double-tag", 4))
    )


_TmnxMacsecMkaStatsEncapType_Type.__name__ = "Integer32"
_TmnxMacsecMkaStatsEncapType_Object = MibTableColumn
tmnxMacsecMkaStatsEncapType = _TmnxMacsecMkaStatsEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 44),
    _TmnxMacsecMkaStatsEncapType_Type()
)
tmnxMacsecMkaStatsEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsEncapType.setStatus("current")
_TmnxMacsecMkaStatsEncapMatch_Type = TmnxEncapVal
_TmnxMacsecMkaStatsEncapMatch_Object = MibTableColumn
tmnxMacsecMkaStatsEncapMatch = _TmnxMacsecMkaStatsEncapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 2, 1, 45),
    _TmnxMacsecMkaStatsEncapMatch_Type()
)
tmnxMacsecMkaStatsEncapMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaStatsEncapMatch.setStatus("current")
_TmnxMacsecMkaPeerListTable_Object = MibTable
tmnxMacsecMkaPeerListTable = _TmnxMacsecMkaPeerListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListTable.setStatus("current")
_TmnxMacsecMkaPeerListEntry_Object = MibTableRow
tmnxMacsecMkaPeerListEntry = _TmnxMacsecMkaPeerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1)
)
tmnxMacsecMkaPeerListEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecCkn"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListMi"),
)
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListEntry.setStatus("current")


class _TmnxMacsecMkaPeerListMi_Type(OctetString):
    """Custom type tmnxMacsecMkaPeerListMi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_TmnxMacsecMkaPeerListMi_Type.__name__ = "OctetString"
_TmnxMacsecMkaPeerListMi_Object = MibTableColumn
tmnxMacsecMkaPeerListMi = _TmnxMacsecMkaPeerListMi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1, 1),
    _TmnxMacsecMkaPeerListMi_Type()
)
tmnxMacsecMkaPeerListMi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListMi.setStatus("current")
_TmnxMacsecMkaPeerListMn_Type = Counter64
_TmnxMacsecMkaPeerListMn_Object = MibTableColumn
tmnxMacsecMkaPeerListMn = _TmnxMacsecMkaPeerListMn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1, 2),
    _TmnxMacsecMkaPeerListMn_Type()
)
tmnxMacsecMkaPeerListMn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListMn.setStatus("current")


class _TmnxMacsecMkaPeerListType_Type(Integer32):
    """Custom type tmnxMacsecMkaPeerListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("livePeerList", 1),
          ("potentialPeerList", 2))
    )


_TmnxMacsecMkaPeerListType_Type.__name__ = "Integer32"
_TmnxMacsecMkaPeerListType_Object = MibTableColumn
tmnxMacsecMkaPeerListType = _TmnxMacsecMkaPeerListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1, 3),
    _TmnxMacsecMkaPeerListType_Type()
)
tmnxMacsecMkaPeerListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListType.setStatus("current")


class _TmnxMacsecMkaPeerListSci_Type(OctetString):
    """Custom type tmnxMacsecMkaPeerListSci based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxMacsecMkaPeerListSci_Type.__name__ = "OctetString"
_TmnxMacsecMkaPeerListSci_Object = MibTableColumn
tmnxMacsecMkaPeerListSci = _TmnxMacsecMkaPeerListSci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1, 4),
    _TmnxMacsecMkaPeerListSci_Type()
)
tmnxMacsecMkaPeerListSci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListSci.setStatus("current")
_TmnxMacsecMkaPeerListKeyServPrio_Type = Counter64
_TmnxMacsecMkaPeerListKeyServPrio_Object = MibTableColumn
tmnxMacsecMkaPeerListKeyServPrio = _TmnxMacsecMkaPeerListKeyServPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1, 5),
    _TmnxMacsecMkaPeerListKeyServPrio_Type()
)
tmnxMacsecMkaPeerListKeyServPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListKeyServPrio.setStatus("current")
_TmnxMacsecMkaPeerListLowstAcptPn_Type = Counter64
_TmnxMacsecMkaPeerListLowstAcptPn_Object = MibTableColumn
tmnxMacsecMkaPeerListLowstAcptPn = _TmnxMacsecMkaPeerListLowstAcptPn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 3, 1, 6),
    _TmnxMacsecMkaPeerListLowstAcptPn_Type()
)
tmnxMacsecMkaPeerListLowstAcptPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecMkaPeerListLowstAcptPn.setStatus("current")
_TmnxMacsecPortStatsTable_Object = MibTable
tmnxMacsecPortStatsTable = _TmnxMacsecPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsTable.setStatus("current")
_TmnxMacsecPortStatsEntry_Object = MibTableRow
tmnxMacsecPortStatsEntry = _TmnxMacsecPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsEntry.setStatus("current")
_TmnxMacsecPortStatsTxUntaggdPkts_Type = Counter64
_TmnxMacsecPortStatsTxUntaggdPkts_Object = MibTableColumn
tmnxMacsecPortStatsTxUntaggdPkts = _TmnxMacsecPortStatsTxUntaggdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1, 1),
    _TmnxMacsecPortStatsTxUntaggdPkts_Type()
)
tmnxMacsecPortStatsTxUntaggdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsTxUntaggdPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsTxUntaggdPkts.setUnits("Packets")
_TmnxMacsecPortStatsTxTooLongPkts_Type = Counter64
_TmnxMacsecPortStatsTxTooLongPkts_Object = MibTableColumn
tmnxMacsecPortStatsTxTooLongPkts = _TmnxMacsecPortStatsTxTooLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1, 2),
    _TmnxMacsecPortStatsTxTooLongPkts_Type()
)
tmnxMacsecPortStatsTxTooLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsTxTooLongPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsTxTooLongPkts.setUnits("Packets")
_TmnxMacsecPortStatsRxNoTagPkts_Type = Counter64
_TmnxMacsecPortStatsRxNoTagPkts_Object = MibTableColumn
tmnxMacsecPortStatsRxNoTagPkts = _TmnxMacsecPortStatsRxNoTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1, 3),
    _TmnxMacsecPortStatsRxNoTagPkts_Type()
)
tmnxMacsecPortStatsRxNoTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxNoTagPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxNoTagPkts.setUnits("Packets")
_TmnxMacsecPortStatsRxBadTagPkts_Type = Counter64
_TmnxMacsecPortStatsRxBadTagPkts_Object = MibTableColumn
tmnxMacsecPortStatsRxBadTagPkts = _TmnxMacsecPortStatsRxBadTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1, 4),
    _TmnxMacsecPortStatsRxBadTagPkts_Type()
)
tmnxMacsecPortStatsRxBadTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxBadTagPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxBadTagPkts.setUnits("Packets")
_TmnxMacsecPortStatsRxNoSciPkts_Type = Counter64
_TmnxMacsecPortStatsRxNoSciPkts_Object = MibTableColumn
tmnxMacsecPortStatsRxNoSciPkts = _TmnxMacsecPortStatsRxNoSciPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1, 7),
    _TmnxMacsecPortStatsRxNoSciPkts_Type()
)
tmnxMacsecPortStatsRxNoSciPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxNoSciPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxNoSciPkts.setUnits("Packets")
_TmnxMacsecPortStatsRxOverrunPkts_Type = Counter64
_TmnxMacsecPortStatsRxOverrunPkts_Object = MibTableColumn
tmnxMacsecPortStatsRxOverrunPkts = _TmnxMacsecPortStatsRxOverrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 4, 1, 8),
    _TmnxMacsecPortStatsRxOverrunPkts_Type()
)
tmnxMacsecPortStatsRxOverrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxOverrunPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecPortStatsRxOverrunPkts.setUnits("Packets")
_TmnxMacsecTxSAStatsTable_Object = MibTable
tmnxMacsecTxSAStatsTable = _TmnxMacsecTxSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxMacsecTxSAStatsTable.setStatus("current")
_TmnxMacsecTxSAStatsEntry_Object = MibTableRow
tmnxMacsecTxSAStatsEntry = _TmnxMacsecTxSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 5, 1)
)
tmnxMacsecTxSAStatsEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecTxSAAn"),
)
if mibBuilder.loadTexts:
    tmnxMacsecTxSAStatsEntry.setStatus("current")
_TmnxMacsecTxSAAn_Type = Unsigned32
_TmnxMacsecTxSAAn_Object = MibTableColumn
tmnxMacsecTxSAAn = _TmnxMacsecTxSAAn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 5, 1, 1),
    _TmnxMacsecTxSAAn_Type()
)
tmnxMacsecTxSAAn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecTxSAAn.setStatus("current")
_TmnxMacsecTxSAStatsProtectedPkts_Type = Counter32
_TmnxMacsecTxSAStatsProtectedPkts_Object = MibTableColumn
tmnxMacsecTxSAStatsProtectedPkts = _TmnxMacsecTxSAStatsProtectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 5, 1, 2),
    _TmnxMacsecTxSAStatsProtectedPkts_Type()
)
tmnxMacsecTxSAStatsProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecTxSAStatsProtectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecTxSAStatsProtectedPkts.setUnits("Packets")
_TmnxMacsecTxSAStatsEncryptedPkts_Type = Counter32
_TmnxMacsecTxSAStatsEncryptedPkts_Object = MibTableColumn
tmnxMacsecTxSAStatsEncryptedPkts = _TmnxMacsecTxSAStatsEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 5, 1, 3),
    _TmnxMacsecTxSAStatsEncryptedPkts_Type()
)
tmnxMacsecTxSAStatsEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecTxSAStatsEncryptedPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecTxSAStatsEncryptedPkts.setUnits("Packets")
_TmnxMacsecTxSCStatsTable_Object = MibTable
tmnxMacsecTxSCStatsTable = _TmnxMacsecTxSCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsTable.setStatus("current")
_TmnxMacsecTxSCStatsEntry_Object = MibTableRow
tmnxMacsecTxSCStatsEntry = _TmnxMacsecTxSCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 6, 1)
)
tmnxMacsecTxSCStatsEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
)
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsEntry.setStatus("current")
_TmnxMacsecTxSCStatsProtectedPkts_Type = Counter64
_TmnxMacsecTxSCStatsProtectedPkts_Object = MibTableColumn
tmnxMacsecTxSCStatsProtectedPkts = _TmnxMacsecTxSCStatsProtectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 6, 1, 1),
    _TmnxMacsecTxSCStatsProtectedPkts_Type()
)
tmnxMacsecTxSCStatsProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsProtectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsProtectedPkts.setUnits("Packets")
_TmnxMacsecTxSCStatsEncryptedPkts_Type = Counter64
_TmnxMacsecTxSCStatsEncryptedPkts_Object = MibTableColumn
tmnxMacsecTxSCStatsEncryptedPkts = _TmnxMacsecTxSCStatsEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 6, 1, 4),
    _TmnxMacsecTxSCStatsEncryptedPkts_Type()
)
tmnxMacsecTxSCStatsEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsEncryptedPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsEncryptedPkts.setUnits("Packets")
_TmnxMacsecTxSCStatsOctetsProtctd_Type = Counter64
_TmnxMacsecTxSCStatsOctetsProtctd_Object = MibTableColumn
tmnxMacsecTxSCStatsOctetsProtctd = _TmnxMacsecTxSCStatsOctetsProtctd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 6, 1, 5),
    _TmnxMacsecTxSCStatsOctetsProtctd_Type()
)
tmnxMacsecTxSCStatsOctetsProtctd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsOctetsProtctd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsOctetsProtctd.setUnits("Octets")
_TmnxMacsecTxSCStatsOctetsEncrptd_Type = Counter64
_TmnxMacsecTxSCStatsOctetsEncrptd_Object = MibTableColumn
tmnxMacsecTxSCStatsOctetsEncrptd = _TmnxMacsecTxSCStatsOctetsEncrptd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 6, 1, 6),
    _TmnxMacsecTxSCStatsOctetsEncrptd_Type()
)
tmnxMacsecTxSCStatsOctetsEncrptd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsOctetsEncrptd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecTxSCStatsOctetsEncrptd.setUnits("Octets")
_TmnxMacsecRxSAStatsTable_Object = MibTable
tmnxMacsecRxSAStatsTable = _TmnxMacsecRxSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsTable.setStatus("current")
_TmnxMacsecRxSAStatsEntry_Object = MibTableRow
tmnxMacsecRxSAStatsEntry = _TmnxMacsecRxSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7, 1)
)
tmnxMacsecRxSAStatsEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecRxSci"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecRxSAAn"),
)
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsEntry.setStatus("current")


class _TmnxMacsecRxSci_Type(OctetString):
    """Custom type tmnxMacsecRxSci based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxMacsecRxSci_Type.__name__ = "OctetString"
_TmnxMacsecRxSci_Object = MibTableColumn
tmnxMacsecRxSci = _TmnxMacsecRxSci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7, 1, 1),
    _TmnxMacsecRxSci_Type()
)
tmnxMacsecRxSci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecRxSci.setStatus("current")
_TmnxMacsecRxSAAn_Type = Unsigned32
_TmnxMacsecRxSAAn_Object = MibTableColumn
tmnxMacsecRxSAAn = _TmnxMacsecRxSAAn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7, 1, 2),
    _TmnxMacsecRxSAAn_Type()
)
tmnxMacsecRxSAAn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAAn.setStatus("current")
_TmnxMacsecRxSAStatsNoUsingSAPkts_Type = Counter32
_TmnxMacsecRxSAStatsNoUsingSAPkts_Object = MibTableColumn
tmnxMacsecRxSAStatsNoUsingSAPkts = _TmnxMacsecRxSAStatsNoUsingSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7, 1, 3),
    _TmnxMacsecRxSAStatsNoUsingSAPkts_Type()
)
tmnxMacsecRxSAStatsNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsNoUsingSAPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsNoUsingSAPkts.setUnits("Packets")
_TmnxMacsecRxSAStatsNotValidPkts_Type = Counter32
_TmnxMacsecRxSAStatsNotValidPkts_Object = MibTableColumn
tmnxMacsecRxSAStatsNotValidPkts = _TmnxMacsecRxSAStatsNotValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7, 1, 4),
    _TmnxMacsecRxSAStatsNotValidPkts_Type()
)
tmnxMacsecRxSAStatsNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsNotValidPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsNotValidPkts.setUnits("Packets")
_TmnxMacsecRxSAStatsOKPkts_Type = Counter32
_TmnxMacsecRxSAStatsOKPkts_Object = MibTableColumn
tmnxMacsecRxSAStatsOKPkts = _TmnxMacsecRxSAStatsOKPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 7, 1, 5),
    _TmnxMacsecRxSAStatsOKPkts_Type()
)
tmnxMacsecRxSAStatsOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsOKPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSAStatsOKPkts.setUnits("Packets")
_TmnxMacsecRxSCStatsTable_Object = MibTable
tmnxMacsecRxSCStatsTable = _TmnxMacsecRxSCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsTable.setStatus("current")
_TmnxMacsecRxSCStatsEntry_Object = MibTableRow
tmnxMacsecRxSCStatsEntry = _TmnxMacsecRxSCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1)
)
tmnxMacsecRxSCStatsEntry.setIndexNames(
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecPortId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecVlanId"),
    (0, "TIMETRA-MACSEC-MIB", "tmnxMacsecRxSci"),
)
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsEntry.setStatus("current")
_TmnxMacsecRxSCStatsNoUsingSAPkts_Type = Counter64
_TmnxMacsecRxSCStatsNoUsingSAPkts_Object = MibTableColumn
tmnxMacsecRxSCStatsNoUsingSAPkts = _TmnxMacsecRxSCStatsNoUsingSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 1),
    _TmnxMacsecRxSCStatsNoUsingSAPkts_Type()
)
tmnxMacsecRxSCStatsNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsNoUsingSAPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsNoUsingSAPkts.setUnits("Packets")
_TmnxMacsecRxSCStatsLatePkts_Type = Counter64
_TmnxMacsecRxSCStatsLatePkts_Object = MibTableColumn
tmnxMacsecRxSCStatsLatePkts = _TmnxMacsecRxSCStatsLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 2),
    _TmnxMacsecRxSCStatsLatePkts_Type()
)
tmnxMacsecRxSCStatsLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsLatePkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsLatePkts.setUnits("Packets")
_TmnxMacsecRxSCStatsNotValidPkts_Type = Counter64
_TmnxMacsecRxSCStatsNotValidPkts_Object = MibTableColumn
tmnxMacsecRxSCStatsNotValidPkts = _TmnxMacsecRxSCStatsNotValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 3),
    _TmnxMacsecRxSCStatsNotValidPkts_Type()
)
tmnxMacsecRxSCStatsNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsNotValidPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsNotValidPkts.setUnits("Packets")
_TmnxMacsecRxSCStatsDelayedPkts_Type = Counter64
_TmnxMacsecRxSCStatsDelayedPkts_Object = MibTableColumn
tmnxMacsecRxSCStatsDelayedPkts = _TmnxMacsecRxSCStatsDelayedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 4),
    _TmnxMacsecRxSCStatsDelayedPkts_Type()
)
tmnxMacsecRxSCStatsDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsDelayedPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsDelayedPkts.setUnits("Packets")
_TmnxMacsecRxSCStatsUncheckedPkts_Type = Counter64
_TmnxMacsecRxSCStatsUncheckedPkts_Object = MibTableColumn
tmnxMacsecRxSCStatsUncheckedPkts = _TmnxMacsecRxSCStatsUncheckedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 5),
    _TmnxMacsecRxSCStatsUncheckedPkts_Type()
)
tmnxMacsecRxSCStatsUncheckedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsUncheckedPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsUncheckedPkts.setUnits("Packets")
_TmnxMacsecRxSCStatsOKPkts_Type = Counter64
_TmnxMacsecRxSCStatsOKPkts_Object = MibTableColumn
tmnxMacsecRxSCStatsOKPkts = _TmnxMacsecRxSCStatsOKPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 6),
    _TmnxMacsecRxSCStatsOKPkts_Type()
)
tmnxMacsecRxSCStatsOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsOKPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsOKPkts.setUnits("Packets")
_TmnxMacsecRxSCStatsOctsValidated_Type = Counter64
_TmnxMacsecRxSCStatsOctsValidated_Object = MibTableColumn
tmnxMacsecRxSCStatsOctsValidated = _TmnxMacsecRxSCStatsOctsValidated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 7),
    _TmnxMacsecRxSCStatsOctsValidated_Type()
)
tmnxMacsecRxSCStatsOctsValidated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsOctsValidated.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsOctsValidated.setUnits("Octets")
_TmnxMacsecRxSCStatsOctsDecrypted_Type = Counter64
_TmnxMacsecRxSCStatsOctsDecrypted_Object = MibTableColumn
tmnxMacsecRxSCStatsOctsDecrypted = _TmnxMacsecRxSCStatsOctsDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 3, 8, 1, 8),
    _TmnxMacsecRxSCStatsOctsDecrypted_Type()
)
tmnxMacsecRxSCStatsOctsDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsOctsDecrypted.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMacsecRxSCStatsOctsDecrypted.setUnits("Octets")
_TmnxMacsecNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxMacsecNotifyObjects = _TmnxMacsecNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 4)
)
_TmnxMacsecNotifyPortId_Type = TmnxPortID
_TmnxMacsecNotifyPortId_Object = MibScalar
tmnxMacsecNotifyPortId = _TmnxMacsecNotifyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 4, 1),
    _TmnxMacsecNotifyPortId_Type()
)
tmnxMacsecNotifyPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMacsecNotifyPortId.setStatus("current")
_TmnxMacsecNotifyVlanId_Type = VlanIdOrNone
_TmnxMacsecNotifyVlanId_Object = MibScalar
tmnxMacsecNotifyVlanId = _TmnxMacsecNotifyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 4, 2),
    _TmnxMacsecNotifyVlanId_Type()
)
tmnxMacsecNotifyVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMacsecNotifyVlanId.setStatus("current")


class _TmnxMacsecNotifyPeerMi_Type(OctetString):
    """Custom type tmnxMacsecNotifyPeerMi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_TmnxMacsecNotifyPeerMi_Type.__name__ = "OctetString"
_TmnxMacsecNotifyPeerMi_Object = MibScalar
tmnxMacsecNotifyPeerMi = _TmnxMacsecNotifyPeerMi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 4, 3),
    _TmnxMacsecNotifyPeerMi_Type()
)
tmnxMacsecNotifyPeerMi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMacsecNotifyPeerMi.setStatus("current")
_TmnxMacsecNotifySecurityZone_Type = Unsigned32
_TmnxMacsecNotifySecurityZone_Object = MibScalar
tmnxMacsecNotifySecurityZone = _TmnxMacsecNotifySecurityZone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 4, 4),
    _TmnxMacsecNotifySecurityZone_Type()
)
tmnxMacsecNotifySecurityZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMacsecNotifySecurityZone.setStatus("current")
_TmnxMacsecNotifyAssociationNum_Type = Unsigned32
_TmnxMacsecNotifyAssociationNum_Object = MibScalar
tmnxMacsecNotifyAssociationNum = _TmnxMacsecNotifyAssociationNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 114, 4, 5),
    _TmnxMacsecNotifyAssociationNum_Type()
)
tmnxMacsecNotifyAssociationNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMacsecNotifyAssociationNum.setStatus("current")
_TmnxMacsecNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMacsecNotifyPrefix = _TmnxMacsecNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114)
)
_TmnxMacsecNofitications_ObjectIdentity = ObjectIdentity
tmnxMacsecNofitications = _TmnxMacsecNofitications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1)
)
tmnxMacsecConnAssocEntry.registerAugmentions(
    ("TIMETRA-MACSEC-MIB",
     "tmnxMacsecStaticCakEntry")
)
tmnxMacsecStaticCakEntry.setIndexNames(*tmnxMacsecConnAssocEntry.getIndexNames())
tmnxMacsecPortEntry.registerAugmentions(
    ("TIMETRA-MACSEC-MIB",
     "tmnxMacsecPortStatsEntry")
)
tmnxMacsecPortStatsEntry.setIndexNames(*tmnxMacsecPortEntry.getIndexNames())

# Managed Objects groups

tmnxMacsecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 1)
)
tmnxMacsecGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocLastChanged"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocRowStatus"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocAdminState"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocDescription"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocMacsecEncrypt"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocClearTagMode"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocReplayWndwSz"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocCipherSuite"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocReplayProtect"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocEncrptnOffset"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakLastChanged"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakKeyServerPrio"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakActivePsk"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyLastChangd"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyRowStatus"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyEncrptType"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCak"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocTableLstChngd"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakTableLstChngd"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyTblLstChng"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortTableLastChanged"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortLastChanged"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortEapolDestAddress"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortAdminState"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortMaxPeers"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortRowStatus"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalRxTrafEncrpt"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcludeLacp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcludeLldp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcludeCdp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlblExcldEaplStart"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcldeEfmOam"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcldeEthCfm"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortEncapType"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortEncapMatch"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakMkaHelloInt"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcludePtp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlobalExcludeUbfd"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortGlblExcldMacPolicy"))
)
if mibBuilder.loadTexts:
    tmnxMacsecGroup.setStatus("current")

tmnxMacsecStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 2)
)
tmnxMacsecStatsGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsMemberId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsCakName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsTransmitInt"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsOutboundSci"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsMessageNumber"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsKeyNumber"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsKeyServer"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsKeyServerPrio"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsLatestSakAn"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsLatestSakKi"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPreviousSakAn"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPreviousSakKi"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPeerRemTimeout"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsCknNotFound"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsNewLivePeer"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakGenerated"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakInstalledTx"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakInstalledRx"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPduTooSmall"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPduTooBig"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPduNotQuadSize"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPduInvalidNum"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsParamSzInvalid"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsLvnessChckFail"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsParamNotQuadSz"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsUnsupportedAgi"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsInvldCknLength"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsIcvCheckFailed"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPeerSameMid"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakNonLivePeer"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakNoKeyServer"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakDecryptFail"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakEncryptFail"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsKeyNumInvalid"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsSakInstallFail"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsCakInfoMissing"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsMxPeersSetZero"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsOperState"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsOperOffset"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsOperCipher"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListMn"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListType"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListSci"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListKeyServPrio"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListLowstAcptPn"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortStatsTxUntaggdPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortStatsTxTooLongPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortStatsRxNoTagPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortStatsRxBadTagPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortStatsRxNoSciPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortStatsRxOverrunPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecTxSAStatsProtectedPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecTxSAStatsEncryptedPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecTxSCStatsProtectedPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecTxSCStatsEncryptedPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecTxSCStatsOctetsProtctd"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecTxSCStatsOctetsEncrptd"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSAStatsNoUsingSAPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSAStatsNotValidPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSAStatsOKPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsNoUsingSAPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsLatePkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsNotValidPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsDelayedPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsUncheckedPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsOKPkts"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsOctsValidated"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsOctsDecrypted"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsLatestSakLpn"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPreviousSakLpn"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsEncapType"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsEncapMatch"))
)
if mibBuilder.loadTexts:
    tmnxMacsecStatsGroup.setStatus("current")

tmnxMacsecNotificationObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 3)
)
tmnxMacsecNotificationObjsGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPeerMi"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifySecurityZone"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyAssociationNum"))
)
if mibBuilder.loadTexts:
    tmnxMacsecNotificationObjsGroup.setStatus("current")

tmnxMacsecObsoletedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 5)
)
tmnxMacsecObsoletedObjectsGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecPortRxTrafficEncrption"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortExcludeLacp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortExcludeLldp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortExcludeCdp"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortExcludeEapolStart"))
)
if mibBuilder.loadTexts:
    tmnxMacsecObsoletedObjectsGroup.setStatus("current")

tmnxMacsecDestMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 6)
)
tmnxMacsecDestMacAddrGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecMacPolicyGrpRowStatus"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecDestMacAddrRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMacsecDestMacAddrGroup.setStatus("current")

tmnxMacsecDdpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 9)
)
tmnxMacsecDdpObjectGroup.setObjects(
    ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocDelayProtectn")
)
if mibBuilder.loadTexts:
    tmnxMacsecDdpObjectGroup.setStatus("current")


# Notification objects

tmnxMacsecConfiguredPortCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 1)
)
tmnxMacsecConfiguredPortCA.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"))
)
if mibBuilder.loadTexts:
    tmnxMacsecConfiguredPortCA.setStatus(
        "current"
    )

tmnxMacsecUnconfiguredPortCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 2)
)
tmnxMacsecUnconfiguredPortCA.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"))
)
if mibBuilder.loadTexts:
    tmnxMacsecUnconfiguredPortCA.setStatus(
        "current"
    )

tmnxMacsecEnabledPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 3)
)
tmnxMacsecEnabledPort.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"))
)
if mibBuilder.loadTexts:
    tmnxMacsecEnabledPort.setStatus(
        "current"
    )

tmnxMacsecDisabledPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 4)
)
tmnxMacsecDisabledPort.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"))
)
if mibBuilder.loadTexts:
    tmnxMacsecDisabledPort.setStatus(
        "current"
    )

tmnxMacsecMaxPeerLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 5)
)
tmnxMacsecMaxPeerLimitExceeded.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifySecurityZone"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPeerMi"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListSci"))
)
if mibBuilder.loadTexts:
    tmnxMacsecMaxPeerLimitExceeded.setStatus(
        "current"
    )

tmnxMkaSessionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 6)
)
tmnxMkaSessionEstablished.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListSci"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortEapolDestAddress"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsKeyServerPrio"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakKeyServerPrio"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocCipherSuite"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecConnAssocEncrptnOffset"))
)
if mibBuilder.loadTexts:
    tmnxMkaSessionEstablished.setStatus(
        "current"
    )

tmnxMkaPskRollover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 7)
)
tmnxMkaPskRollover.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStaticCakActivePsk"))
)
if mibBuilder.loadTexts:
    tmnxMkaPskRollover.setStatus(
        "current"
    )

tmnxMkaSessionEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 8)
)
tmnxMkaSessionEnded.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListSci"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"))
)
if mibBuilder.loadTexts:
    tmnxMkaSessionEnded.setStatus(
        "current"
    )

tmnxMkaOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 9)
)
tmnxMkaOperStateChanged.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsOperState"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"))
)
if mibBuilder.loadTexts:
    tmnxMkaOperStateChanged.setStatus(
        "current"
    )

tmnxMacsecMaxPeerLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 10)
)
tmnxMacsecMaxPeerLimitCleared.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifySecurityZone"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPeerMi"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaPeerListSci"))
)
if mibBuilder.loadTexts:
    tmnxMacsecMaxPeerLimitCleared.setStatus(
        "current"
    )

tmnxMacsecCaCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 11)
)
tmnxMacsecCaCreate.setObjects(
    ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName")
)
if mibBuilder.loadTexts:
    tmnxMacsecCaCreate.setStatus(
        "current"
    )

tmnxMacsecSakCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 12)
)
tmnxMacsecSakCreate.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyAssociationNum"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"))
)
if mibBuilder.loadTexts:
    tmnxMacsecSakCreate.setStatus(
        "current"
    )

tmnxMacsecSakInstalledRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 13)
)
tmnxMacsecSakInstalledRx.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyAssociationNum"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"))
)
if mibBuilder.loadTexts:
    tmnxMacsecSakInstalledRx.setStatus(
        "current"
    )

tmnxMacsecSakInstalledTx = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 14)
)
tmnxMacsecSakInstalledTx.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyAssociationNum"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"))
)
if mibBuilder.loadTexts:
    tmnxMacsecSakInstalledTx.setStatus(
        "current"
    )

tmnxMacsecMkaReplayAttemptDisc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 15)
)
tmnxMacsecMkaReplayAttemptDisc.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecPortCaName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaStatsPduInvalidNum"))
)
if mibBuilder.loadTexts:
    tmnxMacsecMkaReplayAttemptDisc.setStatus(
        "current"
    )

tmnxMacsecDpReplayAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 16)
)
tmnxMacsecDpReplayAttempt.setObjects(
    ("TIMETRA-MACSEC-MIB", "tmnxMacsecRxSCStatsLatePkts")
)
if mibBuilder.loadTexts:
    tmnxMacsecDpReplayAttempt.setStatus(
        "current"
    )

tmnxMacsecSakDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 114, 1, 17)
)
tmnxMacsecSakDelete.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyAssociationNum"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecPreSharedKeyCakName"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyPortId"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotifyVlanId"))
)
if mibBuilder.loadTexts:
    tmnxMacsecSakDelete.setStatus(
        "current"
    )


# Notifications groups

tmnxMacsecNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 4)
)
tmnxMacsecNotificationGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecConfiguredPortCA"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecUnconfiguredPortCA"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecEnabledPort"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecDisabledPort"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMaxPeerLimitExceeded"),
        ("TIMETRA-MACSEC-MIB", "tmnxMkaSessionEstablished"),
        ("TIMETRA-MACSEC-MIB", "tmnxMkaPskRollover"),
        ("TIMETRA-MACSEC-MIB", "tmnxMkaSessionEnded"),
        ("TIMETRA-MACSEC-MIB", "tmnxMkaOperStateChanged"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMaxPeerLimitCleared"))
)
if mibBuilder.loadTexts:
    tmnxMacsecNotificationGroup.setStatus(
        "current"
    )

tmnxMacsecNiapsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 2, 8)
)
tmnxMacsecNiapsNotificationGroup.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecCaCreate"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecSakCreate"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecSakInstalledRx"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecSakInstalledTx"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecMkaReplayAttemptDisc"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecDpReplayAttempt"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecSakDelete"))
)
if mibBuilder.loadTexts:
    tmnxMacsecNiapsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMacsecComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 1, 1)
)
tmnxMacsecComplianceV15v0.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecGroup"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecStatsGroup"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotificationObjsGroup"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxMacsecComplianceV15v0.setStatus(
        "current"
    )

tmnxMacsecComplianceV19v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 1, 2)
)
tmnxMacsecComplianceV19v0.setObjects(
    ("TIMETRA-MACSEC-MIB", "tmnxMacsecDestMacAddrGroup")
)
if mibBuilder.loadTexts:
    tmnxMacsecComplianceV19v0.setStatus(
        "current"
    )

tmnxMacsecComplianceV20v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 114, 1, 3)
)
tmnxMacsecComplianceV20v0.setObjects(
      *(("TIMETRA-MACSEC-MIB", "tmnxMacsecNiapsNotificationGroup"),
        ("TIMETRA-MACSEC-MIB", "tmnxMacsecDdpObjectGroup"))
)
if mibBuilder.loadTexts:
    tmnxMacsecComplianceV20v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MACSEC-MIB",
    **{"timetraMacsecMIBModule": timetraMacsecMIBModule,
       "tmnxMacsecConformance": tmnxMacsecConformance,
       "tmnxMacsecCompliances": tmnxMacsecCompliances,
       "tmnxMacsecComplianceV15v0": tmnxMacsecComplianceV15v0,
       "tmnxMacsecComplianceV19v0": tmnxMacsecComplianceV19v0,
       "tmnxMacsecComplianceV20v0": tmnxMacsecComplianceV20v0,
       "tmnxMacsecGroups": tmnxMacsecGroups,
       "tmnxMacsecGroup": tmnxMacsecGroup,
       "tmnxMacsecStatsGroup": tmnxMacsecStatsGroup,
       "tmnxMacsecNotificationObjsGroup": tmnxMacsecNotificationObjsGroup,
       "tmnxMacsecNotificationGroup": tmnxMacsecNotificationGroup,
       "tmnxMacsecObsoletedObjectsGroup": tmnxMacsecObsoletedObjectsGroup,
       "tmnxMacsecDestMacAddrGroup": tmnxMacsecDestMacAddrGroup,
       "tmnxMacsecNiapsNotificationGroup": tmnxMacsecNiapsNotificationGroup,
       "tmnxMacsecDdpObjectGroup": tmnxMacsecDdpObjectGroup,
       "tmnxMacsecObjects": tmnxMacsecObjects,
       "tmnxMacsecConfigTimestamps": tmnxMacsecConfigTimestamps,
       "tmnxMacsecConnAssocTableLstChngd": tmnxMacsecConnAssocTableLstChngd,
       "tmnxMacsecStaticCakTableLstChngd": tmnxMacsecStaticCakTableLstChngd,
       "tmnxMacsecPreSharedKeyTblLstChng": tmnxMacsecPreSharedKeyTblLstChng,
       "tmnxMacsecPortTableLastChanged": tmnxMacsecPortTableLastChanged,
       "tmnxMacsecConfigurations": tmnxMacsecConfigurations,
       "tmnxMacsecConfigurationObjects": tmnxMacsecConfigurationObjects,
       "tmnxMacsecConnAssocTable": tmnxMacsecConnAssocTable,
       "tmnxMacsecConnAssocEntry": tmnxMacsecConnAssocEntry,
       "tmnxMacsecConnAssocName": tmnxMacsecConnAssocName,
       "tmnxMacsecConnAssocLastChanged": tmnxMacsecConnAssocLastChanged,
       "tmnxMacsecConnAssocRowStatus": tmnxMacsecConnAssocRowStatus,
       "tmnxMacsecConnAssocAdminState": tmnxMacsecConnAssocAdminState,
       "tmnxMacsecConnAssocDescription": tmnxMacsecConnAssocDescription,
       "tmnxMacsecConnAssocMacsecEncrypt": tmnxMacsecConnAssocMacsecEncrypt,
       "tmnxMacsecConnAssocClearTagMode": tmnxMacsecConnAssocClearTagMode,
       "tmnxMacsecConnAssocReplayWndwSz": tmnxMacsecConnAssocReplayWndwSz,
       "tmnxMacsecConnAssocReplayProtect": tmnxMacsecConnAssocReplayProtect,
       "tmnxMacsecConnAssocCipherSuite": tmnxMacsecConnAssocCipherSuite,
       "tmnxMacsecConnAssocEncrptnOffset": tmnxMacsecConnAssocEncrptnOffset,
       "tmnxMacsecConnAssocDelayProtectn": tmnxMacsecConnAssocDelayProtectn,
       "tmnxMacsecStaticCakTable": tmnxMacsecStaticCakTable,
       "tmnxMacsecStaticCakEntry": tmnxMacsecStaticCakEntry,
       "tmnxMacsecStaticCakLastChanged": tmnxMacsecStaticCakLastChanged,
       "tmnxMacsecStaticCakKeyServerPrio": tmnxMacsecStaticCakKeyServerPrio,
       "tmnxMacsecStaticCakActivePsk": tmnxMacsecStaticCakActivePsk,
       "tmnxMacsecStaticCakMkaHelloInt": tmnxMacsecStaticCakMkaHelloInt,
       "tmnxMacsecPreSharedKeyTable": tmnxMacsecPreSharedKeyTable,
       "tmnxMacsecPreSharedKeyEntry": tmnxMacsecPreSharedKeyEntry,
       "tmnxMacsecPreSharedKeyIndex": tmnxMacsecPreSharedKeyIndex,
       "tmnxMacsecPreSharedKeyLastChangd": tmnxMacsecPreSharedKeyLastChangd,
       "tmnxMacsecPreSharedKeyRowStatus": tmnxMacsecPreSharedKeyRowStatus,
       "tmnxMacsecPreSharedKeyEncrptType": tmnxMacsecPreSharedKeyEncrptType,
       "tmnxMacsecPreSharedKeyCak": tmnxMacsecPreSharedKeyCak,
       "tmnxMacsecPreSharedKeyCakName": tmnxMacsecPreSharedKeyCakName,
       "tmnxMacsecPortTable": tmnxMacsecPortTable,
       "tmnxMacsecPortEntry": tmnxMacsecPortEntry,
       "tmnxMacsecPortId": tmnxMacsecPortId,
       "tmnxMacsecVlanId": tmnxMacsecVlanId,
       "tmnxMacsecPortLastChanged": tmnxMacsecPortLastChanged,
       "tmnxMacsecPortEapolDestAddress": tmnxMacsecPortEapolDestAddress,
       "tmnxMacsecPortCaName": tmnxMacsecPortCaName,
       "tmnxMacsecPortAdminState": tmnxMacsecPortAdminState,
       "tmnxMacsecPortMaxPeers": tmnxMacsecPortMaxPeers,
       "tmnxMacsecPortExcludeLacp": tmnxMacsecPortExcludeLacp,
       "tmnxMacsecPortExcludeLldp": tmnxMacsecPortExcludeLldp,
       "tmnxMacsecPortExcludeCdp": tmnxMacsecPortExcludeCdp,
       "tmnxMacsecPortExcludeEapolStart": tmnxMacsecPortExcludeEapolStart,
       "tmnxMacsecPortRxTrafficEncrption": tmnxMacsecPortRxTrafficEncrption,
       "tmnxMacsecPortRowStatus": tmnxMacsecPortRowStatus,
       "tmnxMacsecPortEncapType": tmnxMacsecPortEncapType,
       "tmnxMacsecPortEncapMatch": tmnxMacsecPortEncapMatch,
       "tmnxMacsecPortGlobalTable": tmnxMacsecPortGlobalTable,
       "tmnxMacsecPortGlobalEntry": tmnxMacsecPortGlobalEntry,
       "tmnxMacsecPortGlobalRxTrafEncrpt": tmnxMacsecPortGlobalRxTrafEncrpt,
       "tmnxMacsecPortGlobalExcludeLacp": tmnxMacsecPortGlobalExcludeLacp,
       "tmnxMacsecPortGlobalExcludeLldp": tmnxMacsecPortGlobalExcludeLldp,
       "tmnxMacsecPortGlobalExcludeCdp": tmnxMacsecPortGlobalExcludeCdp,
       "tmnxMacsecPortGlblExcldEaplStart": tmnxMacsecPortGlblExcldEaplStart,
       "tmnxMacsecPortGlobalExcldeEfmOam": tmnxMacsecPortGlobalExcldeEfmOam,
       "tmnxMacsecPortGlobalExcldeEthCfm": tmnxMacsecPortGlobalExcldeEthCfm,
       "tmnxMacsecPortGlobalExcludePtp": tmnxMacsecPortGlobalExcludePtp,
       "tmnxMacsecPortGlobalExcludeUbfd": tmnxMacsecPortGlobalExcludeUbfd,
       "tmnxMacsecPortGlblExcldMacPolicy": tmnxMacsecPortGlblExcldMacPolicy,
       "tmnxMacsecMacPolicyGroupTable": tmnxMacsecMacPolicyGroupTable,
       "tmnxMacsecMacPolicyGroupEntry": tmnxMacsecMacPolicyGroupEntry,
       "tmnxMacsecMacPolicyId": tmnxMacsecMacPolicyId,
       "tmnxMacsecMacPolicyGrpRowStatus": tmnxMacsecMacPolicyGrpRowStatus,
       "tmnxMacsecDestMacAddressTable": tmnxMacsecDestMacAddressTable,
       "tmnxMacsecDestMacAddressEntry": tmnxMacsecDestMacAddressEntry,
       "tmnxMacsecDestMacAddress": tmnxMacsecDestMacAddress,
       "tmnxMacsecDestMacAddrRowStatus": tmnxMacsecDestMacAddrRowStatus,
       "tmnxMacsecStats": tmnxMacsecStats,
       "tmnxMacsecStatsObjects": tmnxMacsecStatsObjects,
       "tmnxMacsecMkaStatsTable": tmnxMacsecMkaStatsTable,
       "tmnxMacsecMkaStatsEntry": tmnxMacsecMkaStatsEntry,
       "tmnxMacsecCkn": tmnxMacsecCkn,
       "tmnxMacsecMkaStatsMemberId": tmnxMacsecMkaStatsMemberId,
       "tmnxMacsecMkaStatsCakName": tmnxMacsecMkaStatsCakName,
       "tmnxMacsecMkaStatsTransmitInt": tmnxMacsecMkaStatsTransmitInt,
       "tmnxMacsecMkaStatsOutboundSci": tmnxMacsecMkaStatsOutboundSci,
       "tmnxMacsecMkaStatsMessageNumber": tmnxMacsecMkaStatsMessageNumber,
       "tmnxMacsecMkaStatsKeyNumber": tmnxMacsecMkaStatsKeyNumber,
       "tmnxMacsecMkaStatsKeyServer": tmnxMacsecMkaStatsKeyServer,
       "tmnxMacsecMkaStatsKeyServerPrio": tmnxMacsecMkaStatsKeyServerPrio,
       "tmnxMacsecMkaStatsLatestSakAn": tmnxMacsecMkaStatsLatestSakAn,
       "tmnxMacsecMkaStatsLatestSakKi": tmnxMacsecMkaStatsLatestSakKi,
       "tmnxMacsecMkaStatsPreviousSakAn": tmnxMacsecMkaStatsPreviousSakAn,
       "tmnxMacsecMkaStatsPreviousSakKi": tmnxMacsecMkaStatsPreviousSakKi,
       "tmnxMacsecMkaStatsPeerRemTimeout": tmnxMacsecMkaStatsPeerRemTimeout,
       "tmnxMacsecMkaStatsCknNotFound": tmnxMacsecMkaStatsCknNotFound,
       "tmnxMacsecMkaStatsNewLivePeer": tmnxMacsecMkaStatsNewLivePeer,
       "tmnxMacsecMkaStatsSakGenerated": tmnxMacsecMkaStatsSakGenerated,
       "tmnxMacsecMkaStatsSakInstalledTx": tmnxMacsecMkaStatsSakInstalledTx,
       "tmnxMacsecMkaStatsSakInstalledRx": tmnxMacsecMkaStatsSakInstalledRx,
       "tmnxMacsecMkaStatsPduTooSmall": tmnxMacsecMkaStatsPduTooSmall,
       "tmnxMacsecMkaStatsPduTooBig": tmnxMacsecMkaStatsPduTooBig,
       "tmnxMacsecMkaStatsPduNotQuadSize": tmnxMacsecMkaStatsPduNotQuadSize,
       "tmnxMacsecMkaStatsPduInvalidNum": tmnxMacsecMkaStatsPduInvalidNum,
       "tmnxMacsecMkaStatsParamSzInvalid": tmnxMacsecMkaStatsParamSzInvalid,
       "tmnxMacsecMkaStatsLvnessChckFail": tmnxMacsecMkaStatsLvnessChckFail,
       "tmnxMacsecMkaStatsParamNotQuadSz": tmnxMacsecMkaStatsParamNotQuadSz,
       "tmnxMacsecMkaStatsUnsupportedAgi": tmnxMacsecMkaStatsUnsupportedAgi,
       "tmnxMacsecMkaStatsInvldCknLength": tmnxMacsecMkaStatsInvldCknLength,
       "tmnxMacsecMkaStatsIcvCheckFailed": tmnxMacsecMkaStatsIcvCheckFailed,
       "tmnxMacsecMkaStatsPeerSameMid": tmnxMacsecMkaStatsPeerSameMid,
       "tmnxMacsecMkaStatsSakNonLivePeer": tmnxMacsecMkaStatsSakNonLivePeer,
       "tmnxMacsecMkaStatsSakNoKeyServer": tmnxMacsecMkaStatsSakNoKeyServer,
       "tmnxMacsecMkaStatsSakDecryptFail": tmnxMacsecMkaStatsSakDecryptFail,
       "tmnxMacsecMkaStatsSakEncryptFail": tmnxMacsecMkaStatsSakEncryptFail,
       "tmnxMacsecMkaStatsKeyNumInvalid": tmnxMacsecMkaStatsKeyNumInvalid,
       "tmnxMacsecMkaStatsSakInstallFail": tmnxMacsecMkaStatsSakInstallFail,
       "tmnxMacsecMkaStatsCakInfoMissing": tmnxMacsecMkaStatsCakInfoMissing,
       "tmnxMacsecMkaStatsMxPeersSetZero": tmnxMacsecMkaStatsMxPeersSetZero,
       "tmnxMacsecMkaStatsOperState": tmnxMacsecMkaStatsOperState,
       "tmnxMacsecMkaStatsOperOffset": tmnxMacsecMkaStatsOperOffset,
       "tmnxMacsecMkaStatsOperCipher": tmnxMacsecMkaStatsOperCipher,
       "tmnxMacsecMkaStatsLatestSakLpn": tmnxMacsecMkaStatsLatestSakLpn,
       "tmnxMacsecMkaStatsPreviousSakLpn": tmnxMacsecMkaStatsPreviousSakLpn,
       "tmnxMacsecMkaStatsEncapType": tmnxMacsecMkaStatsEncapType,
       "tmnxMacsecMkaStatsEncapMatch": tmnxMacsecMkaStatsEncapMatch,
       "tmnxMacsecMkaPeerListTable": tmnxMacsecMkaPeerListTable,
       "tmnxMacsecMkaPeerListEntry": tmnxMacsecMkaPeerListEntry,
       "tmnxMacsecMkaPeerListMi": tmnxMacsecMkaPeerListMi,
       "tmnxMacsecMkaPeerListMn": tmnxMacsecMkaPeerListMn,
       "tmnxMacsecMkaPeerListType": tmnxMacsecMkaPeerListType,
       "tmnxMacsecMkaPeerListSci": tmnxMacsecMkaPeerListSci,
       "tmnxMacsecMkaPeerListKeyServPrio": tmnxMacsecMkaPeerListKeyServPrio,
       "tmnxMacsecMkaPeerListLowstAcptPn": tmnxMacsecMkaPeerListLowstAcptPn,
       "tmnxMacsecPortStatsTable": tmnxMacsecPortStatsTable,
       "tmnxMacsecPortStatsEntry": tmnxMacsecPortStatsEntry,
       "tmnxMacsecPortStatsTxUntaggdPkts": tmnxMacsecPortStatsTxUntaggdPkts,
       "tmnxMacsecPortStatsTxTooLongPkts": tmnxMacsecPortStatsTxTooLongPkts,
       "tmnxMacsecPortStatsRxNoTagPkts": tmnxMacsecPortStatsRxNoTagPkts,
       "tmnxMacsecPortStatsRxBadTagPkts": tmnxMacsecPortStatsRxBadTagPkts,
       "tmnxMacsecPortStatsRxNoSciPkts": tmnxMacsecPortStatsRxNoSciPkts,
       "tmnxMacsecPortStatsRxOverrunPkts": tmnxMacsecPortStatsRxOverrunPkts,
       "tmnxMacsecTxSAStatsTable": tmnxMacsecTxSAStatsTable,
       "tmnxMacsecTxSAStatsEntry": tmnxMacsecTxSAStatsEntry,
       "tmnxMacsecTxSAAn": tmnxMacsecTxSAAn,
       "tmnxMacsecTxSAStatsProtectedPkts": tmnxMacsecTxSAStatsProtectedPkts,
       "tmnxMacsecTxSAStatsEncryptedPkts": tmnxMacsecTxSAStatsEncryptedPkts,
       "tmnxMacsecTxSCStatsTable": tmnxMacsecTxSCStatsTable,
       "tmnxMacsecTxSCStatsEntry": tmnxMacsecTxSCStatsEntry,
       "tmnxMacsecTxSCStatsProtectedPkts": tmnxMacsecTxSCStatsProtectedPkts,
       "tmnxMacsecTxSCStatsEncryptedPkts": tmnxMacsecTxSCStatsEncryptedPkts,
       "tmnxMacsecTxSCStatsOctetsProtctd": tmnxMacsecTxSCStatsOctetsProtctd,
       "tmnxMacsecTxSCStatsOctetsEncrptd": tmnxMacsecTxSCStatsOctetsEncrptd,
       "tmnxMacsecRxSAStatsTable": tmnxMacsecRxSAStatsTable,
       "tmnxMacsecRxSAStatsEntry": tmnxMacsecRxSAStatsEntry,
       "tmnxMacsecRxSci": tmnxMacsecRxSci,
       "tmnxMacsecRxSAAn": tmnxMacsecRxSAAn,
       "tmnxMacsecRxSAStatsNoUsingSAPkts": tmnxMacsecRxSAStatsNoUsingSAPkts,
       "tmnxMacsecRxSAStatsNotValidPkts": tmnxMacsecRxSAStatsNotValidPkts,
       "tmnxMacsecRxSAStatsOKPkts": tmnxMacsecRxSAStatsOKPkts,
       "tmnxMacsecRxSCStatsTable": tmnxMacsecRxSCStatsTable,
       "tmnxMacsecRxSCStatsEntry": tmnxMacsecRxSCStatsEntry,
       "tmnxMacsecRxSCStatsNoUsingSAPkts": tmnxMacsecRxSCStatsNoUsingSAPkts,
       "tmnxMacsecRxSCStatsLatePkts": tmnxMacsecRxSCStatsLatePkts,
       "tmnxMacsecRxSCStatsNotValidPkts": tmnxMacsecRxSCStatsNotValidPkts,
       "tmnxMacsecRxSCStatsDelayedPkts": tmnxMacsecRxSCStatsDelayedPkts,
       "tmnxMacsecRxSCStatsUncheckedPkts": tmnxMacsecRxSCStatsUncheckedPkts,
       "tmnxMacsecRxSCStatsOKPkts": tmnxMacsecRxSCStatsOKPkts,
       "tmnxMacsecRxSCStatsOctsValidated": tmnxMacsecRxSCStatsOctsValidated,
       "tmnxMacsecRxSCStatsOctsDecrypted": tmnxMacsecRxSCStatsOctsDecrypted,
       "tmnxMacsecNotifyObjects": tmnxMacsecNotifyObjects,
       "tmnxMacsecNotifyPortId": tmnxMacsecNotifyPortId,
       "tmnxMacsecNotifyVlanId": tmnxMacsecNotifyVlanId,
       "tmnxMacsecNotifyPeerMi": tmnxMacsecNotifyPeerMi,
       "tmnxMacsecNotifySecurityZone": tmnxMacsecNotifySecurityZone,
       "tmnxMacsecNotifyAssociationNum": tmnxMacsecNotifyAssociationNum,
       "tmnxMacsecNotifyPrefix": tmnxMacsecNotifyPrefix,
       "tmnxMacsecNofitications": tmnxMacsecNofitications,
       "tmnxMacsecConfiguredPortCA": tmnxMacsecConfiguredPortCA,
       "tmnxMacsecUnconfiguredPortCA": tmnxMacsecUnconfiguredPortCA,
       "tmnxMacsecEnabledPort": tmnxMacsecEnabledPort,
       "tmnxMacsecDisabledPort": tmnxMacsecDisabledPort,
       "tmnxMacsecMaxPeerLimitExceeded": tmnxMacsecMaxPeerLimitExceeded,
       "tmnxMkaSessionEstablished": tmnxMkaSessionEstablished,
       "tmnxMkaPskRollover": tmnxMkaPskRollover,
       "tmnxMkaSessionEnded": tmnxMkaSessionEnded,
       "tmnxMkaOperStateChanged": tmnxMkaOperStateChanged,
       "tmnxMacsecMaxPeerLimitCleared": tmnxMacsecMaxPeerLimitCleared,
       "tmnxMacsecCaCreate": tmnxMacsecCaCreate,
       "tmnxMacsecSakCreate": tmnxMacsecSakCreate,
       "tmnxMacsecSakInstalledRx": tmnxMacsecSakInstalledRx,
       "tmnxMacsecSakInstalledTx": tmnxMacsecSakInstalledTx,
       "tmnxMacsecMkaReplayAttemptDisc": tmnxMacsecMkaReplayAttemptDisc,
       "tmnxMacsecDpReplayAttempt": tmnxMacsecDpReplayAttempt,
       "tmnxMacsecSakDelete": tmnxMacsecSakDelete}
)
