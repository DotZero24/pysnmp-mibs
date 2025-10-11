# SNMP MIB module (ARICENT-DCB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-DCB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:16 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(lldpXdot1dcbxAdminApplicationPriorityAppEntry,) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-DCBX-MIB",
    "lldpXdot1dcbxAdminApplicationPriorityAppEntry")

(lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

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

fsDcbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22)
)
if mibBuilder.loadTexts:
    fsDcbMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class DcbAdminMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("on", 1),
          ("off", 2))
    )



class DcbState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("init", 1),
          ("rxrecommended", 2),
          ("ceedisabled", 3),
          ("uselocalcfg", 4),
          ("usepeercfg", 5))
    )



class DcbxVersion(TextualConvention, Integer32):
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
        *(("auto", 1),
          ("ieee", 2),
          ("cee", 3),
          ("unknown", 4))
    )



class DcbStateMachineType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 1),
          ("symmetric", 2),
          ("feature", 3))
    )



class FsLldpXdot1dcbxTCSupportedCapacity(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 7),
    )



class DcbxStatus(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("peerNotAdvFeat", 1),
          ("peerNotAdvDcbx", 2),
          ("notAdvertise", 3),
          ("disabled", 4),
          ("peerDisabled", 5),
          ("peerInError", 6),
          ("peerNWillingCompatibleCfg", 7),
          ("cfgNotCompatible", 8),
          ("ok", 9),
          ("unknown", 10))
    )



# MIB Managed Objects in the order of their OIDs

_FsDcbSystem_ObjectIdentity = ObjectIdentity
fsDcbSystem = _FsDcbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 1)
)


class _FsDcbPfcMinThreshold_Type(Unsigned32):
    """Custom type fsDcbPfcMinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDcbPfcMinThreshold_Type.__name__ = "Unsigned32"
_FsDcbPfcMinThreshold_Object = MibScalar
fsDcbPfcMinThreshold = _FsDcbPfcMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 1, 1),
    _FsDcbPfcMinThreshold_Type()
)
fsDcbPfcMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcbPfcMinThreshold.setStatus("current")


class _FsDcbPfcMaxThreshold_Type(Unsigned32):
    """Custom type fsDcbPfcMaxThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDcbPfcMaxThreshold_Type.__name__ = "Unsigned32"
_FsDcbPfcMaxThreshold_Object = MibScalar
fsDcbPfcMaxThreshold = _FsDcbPfcMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 1, 2),
    _FsDcbPfcMaxThreshold_Type()
)
fsDcbPfcMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcbPfcMaxThreshold.setStatus("current")


class _FsDcbMaxPfcProfiles_Type(Unsigned32):
    """Custom type fsDcbMaxPfcProfiles based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FsDcbMaxPfcProfiles_Type.__name__ = "Unsigned32"
_FsDcbMaxPfcProfiles_Object = MibScalar
fsDcbMaxPfcProfiles = _FsDcbMaxPfcProfiles_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 1, 3),
    _FsDcbMaxPfcProfiles_Type()
)
fsDcbMaxPfcProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbMaxPfcProfiles.setStatus("current")
_FsDcbObjects_ObjectIdentity = ObjectIdentity
fsDcbObjects = _FsDcbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2)
)
_FsDcbPortTable_Object = MibTable
fsDcbPortTable = _FsDcbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1)
)
if mibBuilder.loadTexts:
    fsDcbPortTable.setStatus("current")
_FsDcbPortEntry_Object = MibTableRow
fsDcbPortEntry = _FsDcbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1)
)
fsDcbPortEntry.setIndexNames(
    (0, "ARICENT-DCB-MIB", "fsDcbPortNumber"),
)
if mibBuilder.loadTexts:
    fsDcbPortEntry.setStatus("current")
_FsDcbPortNumber_Type = InterfaceIndex
_FsDcbPortNumber_Object = MibTableColumn
fsDcbPortNumber = _FsDcbPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 1),
    _FsDcbPortNumber_Type()
)
fsDcbPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDcbPortNumber.setStatus("current")


class _FsDcbETSAdminStatus_Type(EnabledStatus):
    """Custom type fsDcbETSAdminStatus based on EnabledStatus"""
    defaultValue = 2


_FsDcbETSAdminStatus_Type.__name__ = "EnabledStatus"
_FsDcbETSAdminStatus_Object = MibTableColumn
fsDcbETSAdminStatus = _FsDcbETSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 2),
    _FsDcbETSAdminStatus_Type()
)
fsDcbETSAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbETSAdminStatus.setStatus("current")


class _FsDcbPFCAdminStatus_Type(EnabledStatus):
    """Custom type fsDcbPFCAdminStatus based on EnabledStatus"""
    defaultValue = 2


_FsDcbPFCAdminStatus_Type.__name__ = "EnabledStatus"
_FsDcbPFCAdminStatus_Object = MibTableColumn
fsDcbPFCAdminStatus = _FsDcbPFCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 3),
    _FsDcbPFCAdminStatus_Type()
)
fsDcbPFCAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbPFCAdminStatus.setStatus("current")
_FsDcbRowStatus_Type = RowStatus
_FsDcbRowStatus_Object = MibTableColumn
fsDcbRowStatus = _FsDcbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 4),
    _FsDcbRowStatus_Type()
)
fsDcbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcbRowStatus.setStatus("current")


class _FsDcbAppPriAdminStatus_Type(EnabledStatus):
    """Custom type fsDcbAppPriAdminStatus based on EnabledStatus"""
    defaultValue = 2


_FsDcbAppPriAdminStatus_Type.__name__ = "EnabledStatus"
_FsDcbAppPriAdminStatus_Object = MibTableColumn
fsDcbAppPriAdminStatus = _FsDcbAppPriAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 5),
    _FsDcbAppPriAdminStatus_Type()
)
fsDcbAppPriAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbAppPriAdminStatus.setStatus("current")
_FsDcbOperVersion_Type = DcbxVersion
_FsDcbOperVersion_Object = MibTableColumn
fsDcbOperVersion = _FsDcbOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 6),
    _FsDcbOperVersion_Type()
)
fsDcbOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbOperVersion.setStatus("current")
_FsDcbMaxVersion_Type = DcbxVersion
_FsDcbMaxVersion_Object = MibTableColumn
fsDcbMaxVersion = _FsDcbMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 7),
    _FsDcbMaxVersion_Type()
)
fsDcbMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbMaxVersion.setStatus("current")
_FsDcbPeerOperVersion_Type = DcbxVersion
_FsDcbPeerOperVersion_Object = MibTableColumn
fsDcbPeerOperVersion = _FsDcbPeerOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 8),
    _FsDcbPeerOperVersion_Type()
)
fsDcbPeerOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbPeerOperVersion.setStatus("current")
_FsDcbPeerMaxVersion_Type = DcbxVersion
_FsDcbPeerMaxVersion_Object = MibTableColumn
fsDcbPeerMaxVersion = _FsDcbPeerMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 2, 1, 1, 9),
    _FsDcbPeerMaxVersion_Type()
)
fsDcbPeerMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbPeerMaxVersion.setStatus("current")
_FsDcbApplicationObjects_ObjectIdentity = ObjectIdentity
fsDcbApplicationObjects = _FsDcbApplicationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3)
)
_FsDCBXObjects_ObjectIdentity = ObjectIdentity
fsDCBXObjects = _FsDCBXObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1)
)
_FsDCBXScalars_ObjectIdentity = ObjectIdentity
fsDCBXScalars = _FsDCBXScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 1)
)


class _FsDcbxGlobalTraceLevel_Type(Integer32):
    """Custom type fsDcbxGlobalTraceLevel based on Integer32"""
    defaultValue = 256


_FsDcbxGlobalTraceLevel_Type.__name__ = "Integer32"
_FsDcbxGlobalTraceLevel_Object = MibScalar
fsDcbxGlobalTraceLevel = _FsDcbxGlobalTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 1, 1),
    _FsDcbxGlobalTraceLevel_Type()
)
fsDcbxGlobalTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcbxGlobalTraceLevel.setStatus("current")
_FsDCBXPortTable_Object = MibTable
fsDCBXPortTable = _FsDCBXPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fsDCBXPortTable.setStatus("current")
_FsDCBXPortEntry_Object = MibTableRow
fsDCBXPortEntry = _FsDCBXPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 2, 1)
)
fsDCBXPortEntry.setIndexNames(
    (0, "ARICENT-DCB-MIB", "fsDCBXPortNumber"),
)
if mibBuilder.loadTexts:
    fsDCBXPortEntry.setStatus("current")
_FsDCBXPortNumber_Type = InterfaceIndex
_FsDCBXPortNumber_Object = MibTableColumn
fsDCBXPortNumber = _FsDCBXPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 2, 1, 1),
    _FsDCBXPortNumber_Type()
)
fsDCBXPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDCBXPortNumber.setStatus("current")


class _FsDCBXAdminStatus_Type(EnabledStatus):
    """Custom type fsDCBXAdminStatus based on EnabledStatus"""
    defaultValue = 1


_FsDCBXAdminStatus_Type.__name__ = "EnabledStatus"
_FsDCBXAdminStatus_Object = MibTableColumn
fsDCBXAdminStatus = _FsDCBXAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 2, 1, 2),
    _FsDCBXAdminStatus_Type()
)
fsDCBXAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDCBXAdminStatus.setStatus("current")


class _FsDCBXMode_Type(DcbxVersion):
    """Custom type fsDCBXMode based on DcbxVersion"""
    defaultValue = 1


_FsDCBXMode_Type.__name__ = "DcbxVersion"
_FsDCBXMode_Object = MibTableColumn
fsDCBXMode = _FsDCBXMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 1, 2, 1, 3),
    _FsDCBXMode_Type()
)
fsDCBXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDCBXMode.setStatus("current")
_FsETSObjects_ObjectIdentity = ObjectIdentity
fsETSObjects = _FsETSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2)
)
_FsETSScalars_ObjectIdentity = ObjectIdentity
fsETSScalars = _FsETSScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 1)
)


class _FsETSSystemControl_Type(Integer32):
    """Custom type fsETSSystemControl based on Integer32"""
    defaultValue = 1

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


_FsETSSystemControl_Type.__name__ = "Integer32"
_FsETSSystemControl_Object = MibScalar
fsETSSystemControl = _FsETSSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 1, 1),
    _FsETSSystemControl_Type()
)
fsETSSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSSystemControl.setStatus("current")


class _FsETSModuleStatus_Type(EnabledStatus):
    """Custom type fsETSModuleStatus based on EnabledStatus"""
    defaultValue = 1


_FsETSModuleStatus_Type.__name__ = "EnabledStatus"
_FsETSModuleStatus_Object = MibScalar
fsETSModuleStatus = _FsETSModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 1, 2),
    _FsETSModuleStatus_Type()
)
fsETSModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSModuleStatus.setStatus("current")


class _FsETSClearCounters_Type(TruthValue):
    """Custom type fsETSClearCounters based on TruthValue"""
    defaultValue = 2


_FsETSClearCounters_Type.__name__ = "TruthValue"
_FsETSClearCounters_Object = MibScalar
fsETSClearCounters = _FsETSClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 1, 3),
    _FsETSClearCounters_Type()
)
fsETSClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSClearCounters.setStatus("current")


class _FsETSGlobalEnableTrap_Type(Integer32):
    """Custom type fsETSGlobalEnableTrap based on Integer32"""
    defaultValue = 3


_FsETSGlobalEnableTrap_Type.__name__ = "Integer32"
_FsETSGlobalEnableTrap_Object = MibScalar
fsETSGlobalEnableTrap = _FsETSGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 1, 4),
    _FsETSGlobalEnableTrap_Type()
)
fsETSGlobalEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSGlobalEnableTrap.setStatus("current")
_FsETSGeneratedTrapCount_Type = Unsigned32
_FsETSGeneratedTrapCount_Object = MibScalar
fsETSGeneratedTrapCount = _FsETSGeneratedTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 1, 5),
    _FsETSGeneratedTrapCount_Type()
)
fsETSGeneratedTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSGeneratedTrapCount.setStatus("current")
_FsETSPortTable_Object = MibTable
fsETSPortTable = _FsETSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fsETSPortTable.setStatus("current")
_FsETSPortEntry_Object = MibTableRow
fsETSPortEntry = _FsETSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1)
)
fsETSPortEntry.setIndexNames(
    (0, "ARICENT-DCB-MIB", "fsETSPortNumber"),
)
if mibBuilder.loadTexts:
    fsETSPortEntry.setStatus("current")
_FsETSPortNumber_Type = InterfaceIndex
_FsETSPortNumber_Object = MibTableColumn
fsETSPortNumber = _FsETSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 1),
    _FsETSPortNumber_Type()
)
fsETSPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsETSPortNumber.setStatus("current")


class _FsETSAdminMode_Type(DcbAdminMode):
    """Custom type fsETSAdminMode based on DcbAdminMode"""
    defaultValue = 2


_FsETSAdminMode_Type.__name__ = "DcbAdminMode"
_FsETSAdminMode_Object = MibTableColumn
fsETSAdminMode = _FsETSAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 2),
    _FsETSAdminMode_Type()
)
fsETSAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSAdminMode.setStatus("current")
_FsETSDcbxOperState_Type = DcbState
_FsETSDcbxOperState_Object = MibTableColumn
fsETSDcbxOperState = _FsETSDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 3),
    _FsETSDcbxOperState_Type()
)
fsETSDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSDcbxOperState.setStatus("current")
_FsETSDcbxStateMachine_Type = DcbStateMachineType
_FsETSDcbxStateMachine_Object = MibTableColumn
fsETSDcbxStateMachine = _FsETSDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 4),
    _FsETSDcbxStateMachine_Type()
)
fsETSDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSDcbxStateMachine.setStatus("current")


class _FsETSClearTLVCounters_Type(TruthValue):
    """Custom type fsETSClearTLVCounters based on TruthValue"""
    defaultValue = 2


_FsETSClearTLVCounters_Type.__name__ = "TruthValue"
_FsETSClearTLVCounters_Object = MibTableColumn
fsETSClearTLVCounters = _FsETSClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 5),
    _FsETSClearTLVCounters_Type()
)
fsETSClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSClearTLVCounters.setStatus("current")
_FsETSConfTxTLVCounter_Type = Counter32
_FsETSConfTxTLVCounter_Object = MibTableColumn
fsETSConfTxTLVCounter = _FsETSConfTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 6),
    _FsETSConfTxTLVCounter_Type()
)
fsETSConfTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSConfTxTLVCounter.setStatus("current")
_FsETSConfRxTLVCounter_Type = Counter32
_FsETSConfRxTLVCounter_Object = MibTableColumn
fsETSConfRxTLVCounter = _FsETSConfRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 7),
    _FsETSConfRxTLVCounter_Type()
)
fsETSConfRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSConfRxTLVCounter.setStatus("current")
_FsETSConfRxTLVErrors_Type = Counter32
_FsETSConfRxTLVErrors_Object = MibTableColumn
fsETSConfRxTLVErrors = _FsETSConfRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 8),
    _FsETSConfRxTLVErrors_Type()
)
fsETSConfRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSConfRxTLVErrors.setStatus("current")
_FsETSRecoTxTLVCounter_Type = Counter32
_FsETSRecoTxTLVCounter_Object = MibTableColumn
fsETSRecoTxTLVCounter = _FsETSRecoTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 9),
    _FsETSRecoTxTLVCounter_Type()
)
fsETSRecoTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSRecoTxTLVCounter.setStatus("current")
_FsETSRecoRxTLVCounter_Type = Counter32
_FsETSRecoRxTLVCounter_Object = MibTableColumn
fsETSRecoRxTLVCounter = _FsETSRecoRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 10),
    _FsETSRecoRxTLVCounter_Type()
)
fsETSRecoRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSRecoRxTLVCounter.setStatus("current")
_FsETSRecoRxTLVErrors_Type = Counter32
_FsETSRecoRxTLVErrors_Object = MibTableColumn
fsETSRecoRxTLVErrors = _FsETSRecoRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 11),
    _FsETSRecoRxTLVErrors_Type()
)
fsETSRecoRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSRecoRxTLVErrors.setStatus("current")
_FsETSTcSuppTxTLVCounter_Type = Counter32
_FsETSTcSuppTxTLVCounter_Object = MibTableColumn
fsETSTcSuppTxTLVCounter = _FsETSTcSuppTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 12),
    _FsETSTcSuppTxTLVCounter_Type()
)
fsETSTcSuppTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSTcSuppTxTLVCounter.setStatus("current")
_FsETSTcSuppRxTLVCounter_Type = Counter32
_FsETSTcSuppRxTLVCounter_Object = MibTableColumn
fsETSTcSuppRxTLVCounter = _FsETSTcSuppRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 13),
    _FsETSTcSuppRxTLVCounter_Type()
)
fsETSTcSuppRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSTcSuppRxTLVCounter.setStatus("current")
_FsETSTcSuppRxTLVErrors_Type = Counter32
_FsETSTcSuppRxTLVErrors_Object = MibTableColumn
fsETSTcSuppRxTLVErrors = _FsETSTcSuppRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 14),
    _FsETSTcSuppRxTLVErrors_Type()
)
fsETSTcSuppRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSTcSuppRxTLVErrors.setStatus("current")
_FsETSRowStatus_Type = RowStatus
_FsETSRowStatus_Object = MibTableColumn
fsETSRowStatus = _FsETSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 15),
    _FsETSRowStatus_Type()
)
fsETSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsETSRowStatus.setStatus("current")
_FsETSSyncd_Type = TruthValue
_FsETSSyncd_Object = MibTableColumn
fsETSSyncd = _FsETSSyncd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 16),
    _FsETSSyncd_Type()
)
fsETSSyncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSSyncd.setStatus("current")
_FsETSError_Type = TruthValue
_FsETSError_Object = MibTableColumn
fsETSError = _FsETSError_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 17),
    _FsETSError_Type()
)
fsETSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSError.setStatus("current")
_FsETSDcbxStatus_Type = DcbxStatus
_FsETSDcbxStatus_Object = MibTableColumn
fsETSDcbxStatus = _FsETSDcbxStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 2, 2, 1, 18),
    _FsETSDcbxStatus_Type()
)
fsETSDcbxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsETSDcbxStatus.setStatus("current")
_FsPFCObjects_ObjectIdentity = ObjectIdentity
fsPFCObjects = _FsPFCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3)
)
_FsPFCScalars_ObjectIdentity = ObjectIdentity
fsPFCScalars = _FsPFCScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 1)
)


class _FsPFCSystemControl_Type(Integer32):
    """Custom type fsPFCSystemControl based on Integer32"""
    defaultValue = 1

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


_FsPFCSystemControl_Type.__name__ = "Integer32"
_FsPFCSystemControl_Object = MibScalar
fsPFCSystemControl = _FsPFCSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 1, 1),
    _FsPFCSystemControl_Type()
)
fsPFCSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCSystemControl.setStatus("current")


class _FsPFCModuleStatus_Type(EnabledStatus):
    """Custom type fsPFCModuleStatus based on EnabledStatus"""
    defaultValue = 1


_FsPFCModuleStatus_Type.__name__ = "EnabledStatus"
_FsPFCModuleStatus_Object = MibScalar
fsPFCModuleStatus = _FsPFCModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 1, 2),
    _FsPFCModuleStatus_Type()
)
fsPFCModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCModuleStatus.setStatus("current")


class _FsPFCClearCounters_Type(TruthValue):
    """Custom type fsPFCClearCounters based on TruthValue"""
    defaultValue = 2


_FsPFCClearCounters_Type.__name__ = "TruthValue"
_FsPFCClearCounters_Object = MibScalar
fsPFCClearCounters = _FsPFCClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 1, 3),
    _FsPFCClearCounters_Type()
)
fsPFCClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCClearCounters.setStatus("current")


class _FsPFCGlobalEnableTrap_Type(Integer32):
    """Custom type fsPFCGlobalEnableTrap based on Integer32"""
    defaultValue = 3


_FsPFCGlobalEnableTrap_Type.__name__ = "Integer32"
_FsPFCGlobalEnableTrap_Object = MibScalar
fsPFCGlobalEnableTrap = _FsPFCGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 1, 4),
    _FsPFCGlobalEnableTrap_Type()
)
fsPFCGlobalEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCGlobalEnableTrap.setStatus("current")
_FsPFCGeneratedTrapCount_Type = Unsigned32
_FsPFCGeneratedTrapCount_Object = MibScalar
fsPFCGeneratedTrapCount = _FsPFCGeneratedTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 1, 5),
    _FsPFCGeneratedTrapCount_Type()
)
fsPFCGeneratedTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCGeneratedTrapCount.setStatus("current")
_FsPFCPortTable_Object = MibTable
fsPFCPortTable = _FsPFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fsPFCPortTable.setStatus("current")
_FsPFCPortEntry_Object = MibTableRow
fsPFCPortEntry = _FsPFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1)
)
fsPFCPortEntry.setIndexNames(
    (0, "ARICENT-DCB-MIB", "fsPFCPortNumber"),
)
if mibBuilder.loadTexts:
    fsPFCPortEntry.setStatus("current")
_FsPFCPortNumber_Type = InterfaceIndex
_FsPFCPortNumber_Object = MibTableColumn
fsPFCPortNumber = _FsPFCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 1),
    _FsPFCPortNumber_Type()
)
fsPFCPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPFCPortNumber.setStatus("current")


class _FsPFCAdminMode_Type(DcbAdminMode):
    """Custom type fsPFCAdminMode based on DcbAdminMode"""
    defaultValue = 2


_FsPFCAdminMode_Type.__name__ = "DcbAdminMode"
_FsPFCAdminMode_Object = MibTableColumn
fsPFCAdminMode = _FsPFCAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 2),
    _FsPFCAdminMode_Type()
)
fsPFCAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCAdminMode.setStatus("current")
_FsPFCDcbxOperState_Type = DcbState
_FsPFCDcbxOperState_Object = MibTableColumn
fsPFCDcbxOperState = _FsPFCDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 3),
    _FsPFCDcbxOperState_Type()
)
fsPFCDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCDcbxOperState.setStatus("current")
_FsPFCDcbxStateMachine_Type = DcbStateMachineType
_FsPFCDcbxStateMachine_Object = MibTableColumn
fsPFCDcbxStateMachine = _FsPFCDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 4),
    _FsPFCDcbxStateMachine_Type()
)
fsPFCDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCDcbxStateMachine.setStatus("current")


class _FsPFCClearTLVCounters_Type(TruthValue):
    """Custom type fsPFCClearTLVCounters based on TruthValue"""
    defaultValue = 2


_FsPFCClearTLVCounters_Type.__name__ = "TruthValue"
_FsPFCClearTLVCounters_Object = MibTableColumn
fsPFCClearTLVCounters = _FsPFCClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 5),
    _FsPFCClearTLVCounters_Type()
)
fsPFCClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCClearTLVCounters.setStatus("current")
_FsPFCTxTLVCounter_Type = Counter32
_FsPFCTxTLVCounter_Object = MibTableColumn
fsPFCTxTLVCounter = _FsPFCTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 6),
    _FsPFCTxTLVCounter_Type()
)
fsPFCTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxTLVCounter.setStatus("current")
_FsPFCRxTLVCounter_Type = Counter32
_FsPFCRxTLVCounter_Object = MibTableColumn
fsPFCRxTLVCounter = _FsPFCRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 7),
    _FsPFCRxTLVCounter_Type()
)
fsPFCRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxTLVCounter.setStatus("current")
_FsPFCRxTLVErrors_Type = Counter32
_FsPFCRxTLVErrors_Object = MibTableColumn
fsPFCRxTLVErrors = _FsPFCRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 8),
    _FsPFCRxTLVErrors_Type()
)
fsPFCRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxTLVErrors.setStatus("current")
_FsPFCRowStatus_Type = RowStatus
_FsPFCRowStatus_Object = MibTableColumn
fsPFCRowStatus = _FsPFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 9),
    _FsPFCRowStatus_Type()
)
fsPFCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCRowStatus.setStatus("current")
_FsPFCSyncd_Type = TruthValue
_FsPFCSyncd_Object = MibTableColumn
fsPFCSyncd = _FsPFCSyncd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 10),
    _FsPFCSyncd_Type()
)
fsPFCSyncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCSyncd.setStatus("current")
_FsPFCError_Type = TruthValue
_FsPFCError_Object = MibTableColumn
fsPFCError = _FsPFCError_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 11),
    _FsPFCError_Type()
)
fsPFCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCError.setStatus("current")
_FsPFCDcbxStatus_Type = DcbxStatus
_FsPFCDcbxStatus_Object = MibTableColumn
fsPFCDcbxStatus = _FsPFCDcbxStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 12),
    _FsPFCDcbxStatus_Type()
)
fsPFCDcbxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCDcbxStatus.setStatus("current")
_FsPFCRxPauseFrameCounter_Type = Counter32
_FsPFCRxPauseFrameCounter_Object = MibTableColumn
fsPFCRxPauseFrameCounter = _FsPFCRxPauseFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 13),
    _FsPFCRxPauseFrameCounter_Type()
)
fsPFCRxPauseFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameCounter.setStatus("current")
_FsPFCTxPauseFrameCounter_Type = Counter32
_FsPFCTxPauseFrameCounter_Object = MibTableColumn
fsPFCTxPauseFrameCounter = _FsPFCTxPauseFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 14),
    _FsPFCTxPauseFrameCounter_Type()
)
fsPFCTxPauseFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameCounter.setStatus("current")
_FsPFCRxPauseFrameP0Counter_Type = Counter32
_FsPFCRxPauseFrameP0Counter_Object = MibTableColumn
fsPFCRxPauseFrameP0Counter = _FsPFCRxPauseFrameP0Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 15),
    _FsPFCRxPauseFrameP0Counter_Type()
)
fsPFCRxPauseFrameP0Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP0Counter.setStatus("current")
_FsPFCRxPauseFrameP1Counter_Type = Counter32
_FsPFCRxPauseFrameP1Counter_Object = MibTableColumn
fsPFCRxPauseFrameP1Counter = _FsPFCRxPauseFrameP1Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 16),
    _FsPFCRxPauseFrameP1Counter_Type()
)
fsPFCRxPauseFrameP1Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP1Counter.setStatus("current")
_FsPFCRxPauseFrameP2Counter_Type = Counter32
_FsPFCRxPauseFrameP2Counter_Object = MibTableColumn
fsPFCRxPauseFrameP2Counter = _FsPFCRxPauseFrameP2Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 17),
    _FsPFCRxPauseFrameP2Counter_Type()
)
fsPFCRxPauseFrameP2Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP2Counter.setStatus("current")
_FsPFCRxPauseFrameP3Counter_Type = Counter32
_FsPFCRxPauseFrameP3Counter_Object = MibTableColumn
fsPFCRxPauseFrameP3Counter = _FsPFCRxPauseFrameP3Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 18),
    _FsPFCRxPauseFrameP3Counter_Type()
)
fsPFCRxPauseFrameP3Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP3Counter.setStatus("current")
_FsPFCRxPauseFrameP4Counter_Type = Counter32
_FsPFCRxPauseFrameP4Counter_Object = MibTableColumn
fsPFCRxPauseFrameP4Counter = _FsPFCRxPauseFrameP4Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 19),
    _FsPFCRxPauseFrameP4Counter_Type()
)
fsPFCRxPauseFrameP4Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP4Counter.setStatus("current")
_FsPFCRxPauseFrameP5Counter_Type = Counter32
_FsPFCRxPauseFrameP5Counter_Object = MibTableColumn
fsPFCRxPauseFrameP5Counter = _FsPFCRxPauseFrameP5Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 20),
    _FsPFCRxPauseFrameP5Counter_Type()
)
fsPFCRxPauseFrameP5Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP5Counter.setStatus("current")
_FsPFCRxPauseFrameP6Counter_Type = Counter32
_FsPFCRxPauseFrameP6Counter_Object = MibTableColumn
fsPFCRxPauseFrameP6Counter = _FsPFCRxPauseFrameP6Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 21),
    _FsPFCRxPauseFrameP6Counter_Type()
)
fsPFCRxPauseFrameP6Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP6Counter.setStatus("current")
_FsPFCRxPauseFrameP7Counter_Type = Counter32
_FsPFCRxPauseFrameP7Counter_Object = MibTableColumn
fsPFCRxPauseFrameP7Counter = _FsPFCRxPauseFrameP7Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 22),
    _FsPFCRxPauseFrameP7Counter_Type()
)
fsPFCRxPauseFrameP7Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCRxPauseFrameP7Counter.setStatus("current")
_FsPFCTxPauseFrameP0Counter_Type = Counter32
_FsPFCTxPauseFrameP0Counter_Object = MibTableColumn
fsPFCTxPauseFrameP0Counter = _FsPFCTxPauseFrameP0Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 23),
    _FsPFCTxPauseFrameP0Counter_Type()
)
fsPFCTxPauseFrameP0Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP0Counter.setStatus("current")
_FsPFCTxPauseFrameP1Counter_Type = Counter32
_FsPFCTxPauseFrameP1Counter_Object = MibTableColumn
fsPFCTxPauseFrameP1Counter = _FsPFCTxPauseFrameP1Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 24),
    _FsPFCTxPauseFrameP1Counter_Type()
)
fsPFCTxPauseFrameP1Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP1Counter.setStatus("current")
_FsPFCTxPauseFrameP2Counter_Type = Counter32
_FsPFCTxPauseFrameP2Counter_Object = MibTableColumn
fsPFCTxPauseFrameP2Counter = _FsPFCTxPauseFrameP2Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 25),
    _FsPFCTxPauseFrameP2Counter_Type()
)
fsPFCTxPauseFrameP2Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP2Counter.setStatus("current")
_FsPFCTxPauseFrameP3Counter_Type = Counter32
_FsPFCTxPauseFrameP3Counter_Object = MibTableColumn
fsPFCTxPauseFrameP3Counter = _FsPFCTxPauseFrameP3Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 26),
    _FsPFCTxPauseFrameP3Counter_Type()
)
fsPFCTxPauseFrameP3Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP3Counter.setStatus("current")
_FsPFCTxPauseFrameP4Counter_Type = Counter32
_FsPFCTxPauseFrameP4Counter_Object = MibTableColumn
fsPFCTxPauseFrameP4Counter = _FsPFCTxPauseFrameP4Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 27),
    _FsPFCTxPauseFrameP4Counter_Type()
)
fsPFCTxPauseFrameP4Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP4Counter.setStatus("current")
_FsPFCTxPauseFrameP5Counter_Type = Counter32
_FsPFCTxPauseFrameP5Counter_Object = MibTableColumn
fsPFCTxPauseFrameP5Counter = _FsPFCTxPauseFrameP5Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 28),
    _FsPFCTxPauseFrameP5Counter_Type()
)
fsPFCTxPauseFrameP5Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP5Counter.setStatus("current")
_FsPFCTxPauseFrameP6Counter_Type = Counter32
_FsPFCTxPauseFrameP6Counter_Object = MibTableColumn
fsPFCTxPauseFrameP6Counter = _FsPFCTxPauseFrameP6Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 29),
    _FsPFCTxPauseFrameP6Counter_Type()
)
fsPFCTxPauseFrameP6Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP6Counter.setStatus("current")
_FsPFCTxPauseFrameP7Counter_Type = Counter32
_FsPFCTxPauseFrameP7Counter_Object = MibTableColumn
fsPFCTxPauseFrameP7Counter = _FsPFCTxPauseFrameP7Counter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 30),
    _FsPFCTxPauseFrameP7Counter_Type()
)
fsPFCTxPauseFrameP7Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCTxPauseFrameP7Counter.setStatus("current")
_FsPFCDataFrameDiscardCounter_Type = Counter32
_FsPFCDataFrameDiscardCounter_Object = MibTableColumn
fsPFCDataFrameDiscardCounter = _FsPFCDataFrameDiscardCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 31),
    _FsPFCDataFrameDiscardCounter_Type()
)
fsPFCDataFrameDiscardCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPFCDataFrameDiscardCounter.setStatus("current")


class _FsPFCClearPauseFrameCounters_Type(TruthValue):
    """Custom type fsPFCClearPauseFrameCounters based on TruthValue"""
    defaultValue = 2


_FsPFCClearPauseFrameCounters_Type.__name__ = "TruthValue"
_FsPFCClearPauseFrameCounters_Object = MibTableColumn
fsPFCClearPauseFrameCounters = _FsPFCClearPauseFrameCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 3, 2, 1, 32),
    _FsPFCClearPauseFrameCounters_Type()
)
fsPFCClearPauseFrameCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPFCClearPauseFrameCounters.setStatus("current")
_FsAppPriObjects_ObjectIdentity = ObjectIdentity
fsAppPriObjects = _FsAppPriObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4)
)
_FsAppPriScalars_ObjectIdentity = ObjectIdentity
fsAppPriScalars = _FsAppPriScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 1)
)


class _FsAppPriSystemControl_Type(Integer32):
    """Custom type fsAppPriSystemControl based on Integer32"""
    defaultValue = 1

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


_FsAppPriSystemControl_Type.__name__ = "Integer32"
_FsAppPriSystemControl_Object = MibScalar
fsAppPriSystemControl = _FsAppPriSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 1, 1),
    _FsAppPriSystemControl_Type()
)
fsAppPriSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriSystemControl.setStatus("current")


class _FsAppPriModuleStatus_Type(EnabledStatus):
    """Custom type fsAppPriModuleStatus based on EnabledStatus"""
    defaultValue = 1


_FsAppPriModuleStatus_Type.__name__ = "EnabledStatus"
_FsAppPriModuleStatus_Object = MibScalar
fsAppPriModuleStatus = _FsAppPriModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 1, 2),
    _FsAppPriModuleStatus_Type()
)
fsAppPriModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriModuleStatus.setStatus("current")


class _FsAppPriClearCounters_Type(TruthValue):
    """Custom type fsAppPriClearCounters based on TruthValue"""
    defaultValue = 2


_FsAppPriClearCounters_Type.__name__ = "TruthValue"
_FsAppPriClearCounters_Object = MibScalar
fsAppPriClearCounters = _FsAppPriClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 1, 3),
    _FsAppPriClearCounters_Type()
)
fsAppPriClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriClearCounters.setStatus("current")


class _FsAppPriGlobalEnableTrap_Type(Integer32):
    """Custom type fsAppPriGlobalEnableTrap based on Integer32"""
    defaultValue = 3


_FsAppPriGlobalEnableTrap_Type.__name__ = "Integer32"
_FsAppPriGlobalEnableTrap_Object = MibScalar
fsAppPriGlobalEnableTrap = _FsAppPriGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 1, 4),
    _FsAppPriGlobalEnableTrap_Type()
)
fsAppPriGlobalEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriGlobalEnableTrap.setStatus("current")
_FsAppPriGeneratedTrapCount_Type = Unsigned32
_FsAppPriGeneratedTrapCount_Object = MibScalar
fsAppPriGeneratedTrapCount = _FsAppPriGeneratedTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 1, 5),
    _FsAppPriGeneratedTrapCount_Type()
)
fsAppPriGeneratedTrapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriGeneratedTrapCount.setStatus("current")
_FsAppPriPortTable_Object = MibTable
fsAppPriPortTable = _FsAppPriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2)
)
if mibBuilder.loadTexts:
    fsAppPriPortTable.setStatus("current")
_FsAppPriPortEntry_Object = MibTableRow
fsAppPriPortEntry = _FsAppPriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1)
)
fsAppPriPortEntry.setIndexNames(
    (0, "ARICENT-DCB-MIB", "fsAppPriPortNumber"),
)
if mibBuilder.loadTexts:
    fsAppPriPortEntry.setStatus("current")
_FsAppPriPortNumber_Type = InterfaceIndex
_FsAppPriPortNumber_Object = MibTableColumn
fsAppPriPortNumber = _FsAppPriPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 1),
    _FsAppPriPortNumber_Type()
)
fsAppPriPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAppPriPortNumber.setStatus("current")


class _FsAppPriAdminMode_Type(DcbAdminMode):
    """Custom type fsAppPriAdminMode based on DcbAdminMode"""
    defaultValue = 2


_FsAppPriAdminMode_Type.__name__ = "DcbAdminMode"
_FsAppPriAdminMode_Object = MibTableColumn
fsAppPriAdminMode = _FsAppPriAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 2),
    _FsAppPriAdminMode_Type()
)
fsAppPriAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriAdminMode.setStatus("current")
_FsAppPriDcbxOperState_Type = DcbState
_FsAppPriDcbxOperState_Object = MibTableColumn
fsAppPriDcbxOperState = _FsAppPriDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 3),
    _FsAppPriDcbxOperState_Type()
)
fsAppPriDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriDcbxOperState.setStatus("current")
_FsAppPriDcbxStateMachine_Type = DcbStateMachineType
_FsAppPriDcbxStateMachine_Object = MibTableColumn
fsAppPriDcbxStateMachine = _FsAppPriDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 4),
    _FsAppPriDcbxStateMachine_Type()
)
fsAppPriDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriDcbxStateMachine.setStatus("current")


class _FsAppPriClearTLVCounters_Type(TruthValue):
    """Custom type fsAppPriClearTLVCounters based on TruthValue"""
    defaultValue = 2


_FsAppPriClearTLVCounters_Type.__name__ = "TruthValue"
_FsAppPriClearTLVCounters_Object = MibTableColumn
fsAppPriClearTLVCounters = _FsAppPriClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 5),
    _FsAppPriClearTLVCounters_Type()
)
fsAppPriClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriClearTLVCounters.setStatus("current")
_FsAppPriTxTLVCounter_Type = Counter32
_FsAppPriTxTLVCounter_Object = MibTableColumn
fsAppPriTxTLVCounter = _FsAppPriTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 6),
    _FsAppPriTxTLVCounter_Type()
)
fsAppPriTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriTxTLVCounter.setStatus("current")
_FsAppPriRxTLVCounter_Type = Counter32
_FsAppPriRxTLVCounter_Object = MibTableColumn
fsAppPriRxTLVCounter = _FsAppPriRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 7),
    _FsAppPriRxTLVCounter_Type()
)
fsAppPriRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriRxTLVCounter.setStatus("current")
_FsAppPriRxTLVErrors_Type = Counter32
_FsAppPriRxTLVErrors_Object = MibTableColumn
fsAppPriRxTLVErrors = _FsAppPriRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 8),
    _FsAppPriRxTLVErrors_Type()
)
fsAppPriRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriRxTLVErrors.setStatus("current")
_FsAppPriAppProtocols_Type = Unsigned32
_FsAppPriAppProtocols_Object = MibTableColumn
fsAppPriAppProtocols = _FsAppPriAppProtocols_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 9),
    _FsAppPriAppProtocols_Type()
)
fsAppPriAppProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriAppProtocols.setStatus("current")
_FsAppPriRowStatus_Type = RowStatus
_FsAppPriRowStatus_Object = MibTableColumn
fsAppPriRowStatus = _FsAppPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 10),
    _FsAppPriRowStatus_Type()
)
fsAppPriRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriRowStatus.setStatus("current")
_FsAppPriSyncd_Type = TruthValue
_FsAppPriSyncd_Object = MibTableColumn
fsAppPriSyncd = _FsAppPriSyncd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 11),
    _FsAppPriSyncd_Type()
)
fsAppPriSyncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriSyncd.setStatus("current")
_FsAppPriError_Type = TruthValue
_FsAppPriError_Object = MibTableColumn
fsAppPriError = _FsAppPriError_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 12),
    _FsAppPriError_Type()
)
fsAppPriError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriError.setStatus("current")
_FsAppPriDcbxStatus_Type = DcbxStatus
_FsAppPriDcbxStatus_Object = MibTableColumn
fsAppPriDcbxStatus = _FsAppPriDcbxStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 2, 1, 13),
    _FsAppPriDcbxStatus_Type()
)
fsAppPriDcbxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAppPriDcbxStatus.setStatus("current")
_FsAppPriXAppTable_Object = MibTable
fsAppPriXAppTable = _FsAppPriXAppTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 3)
)
if mibBuilder.loadTexts:
    fsAppPriXAppTable.setStatus("current")
_FsAppPriXAppEntry_Object = MibTableRow
fsAppPriXAppEntry = _FsAppPriXAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fsAppPriXAppEntry.setStatus("current")
_FsAppPriXAppRowStatus_Type = RowStatus
_FsAppPriXAppRowStatus_Object = MibTableColumn
fsAppPriXAppRowStatus = _FsAppPriXAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 3, 1, 1),
    _FsAppPriXAppRowStatus_Type()
)
fsAppPriXAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAppPriXAppRowStatus.setStatus("current")
_FslldpXdot1dcbxLocApplicationPriorityBasicTable_Object = MibTable
fslldpXdot1dcbxLocApplicationPriorityBasicTable = _FslldpXdot1dcbxLocApplicationPriorityBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 4)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxLocApplicationPriorityBasicTable.setStatus("current")
_FslldpXdot1dcbxLocApplicationPriorityBasicEntry_Object = MibTableRow
fslldpXdot1dcbxLocApplicationPriorityBasicEntry = _FslldpXdot1dcbxLocApplicationPriorityBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 4, 1)
)
fslldpXdot1dcbxLocApplicationPriorityBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxLocApplicationPriorityBasicEntry.setStatus("current")
_FslldpXdot1dcbxLocApplicationPriorityWilling_Type = TruthValue
_FslldpXdot1dcbxLocApplicationPriorityWilling_Object = MibTableColumn
fslldpXdot1dcbxLocApplicationPriorityWilling = _FslldpXdot1dcbxLocApplicationPriorityWilling_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 4, 1, 1),
    _FslldpXdot1dcbxLocApplicationPriorityWilling_Type()
)
fslldpXdot1dcbxLocApplicationPriorityWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxLocApplicationPriorityWilling.setStatus("current")
_FslldpXdot1dcbxAdminApplicationPriorityBasicTable_Object = MibTable
fslldpXdot1dcbxAdminApplicationPriorityBasicTable = _FslldpXdot1dcbxAdminApplicationPriorityBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 5)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxAdminApplicationPriorityBasicTable.setStatus("current")
_FslldpXdot1dcbxAdminApplicationPriorityBasicEntry_Object = MibTableRow
fslldpXdot1dcbxAdminApplicationPriorityBasicEntry = _FslldpXdot1dcbxAdminApplicationPriorityBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 5, 1)
)
fslldpXdot1dcbxAdminApplicationPriorityBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxAdminApplicationPriorityBasicEntry.setStatus("current")


class _FslldpXdot1dcbxAdminApplicationPriorityWilling_Type(TruthValue):
    """Custom type fslldpXdot1dcbxAdminApplicationPriorityWilling based on TruthValue"""
    defaultValue = 2


_FslldpXdot1dcbxAdminApplicationPriorityWilling_Type.__name__ = "TruthValue"
_FslldpXdot1dcbxAdminApplicationPriorityWilling_Object = MibTableColumn
fslldpXdot1dcbxAdminApplicationPriorityWilling = _FslldpXdot1dcbxAdminApplicationPriorityWilling_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 5, 1, 1),
    _FslldpXdot1dcbxAdminApplicationPriorityWilling_Type()
)
fslldpXdot1dcbxAdminApplicationPriorityWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxAdminApplicationPriorityWilling.setStatus("current")
_FslldpXdot1dcbxRemApplicationPriorityBasicTable_Object = MibTable
fslldpXdot1dcbxRemApplicationPriorityBasicTable = _FslldpXdot1dcbxRemApplicationPriorityBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 6)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxRemApplicationPriorityBasicTable.setStatus("current")
_FslldpXdot1dcbxRemApplicationPriorityBasicEntry_Object = MibTableRow
fslldpXdot1dcbxRemApplicationPriorityBasicEntry = _FslldpXdot1dcbxRemApplicationPriorityBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 6, 1)
)
fslldpXdot1dcbxRemApplicationPriorityBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxRemApplicationPriorityBasicEntry.setStatus("current")
_FslldpXdot1dcbxRemApplicationPriorityWilling_Type = TruthValue
_FslldpXdot1dcbxRemApplicationPriorityWilling_Object = MibTableColumn
fslldpXdot1dcbxRemApplicationPriorityWilling = _FslldpXdot1dcbxRemApplicationPriorityWilling_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 4, 6, 1, 1),
    _FslldpXdot1dcbxRemApplicationPriorityWilling_Type()
)
fslldpXdot1dcbxRemApplicationPriorityWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxRemApplicationPriorityWilling.setStatus("current")
_FsTCSupportedObjects_ObjectIdentity = ObjectIdentity
fsTCSupportedObjects = _FsTCSupportedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5)
)
_FslldpXdot1dcbxConfigTCSupportedTable_Object = MibTable
fslldpXdot1dcbxConfigTCSupportedTable = _FslldpXdot1dcbxConfigTCSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 1)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxConfigTCSupportedTable.setStatus("current")
_FslldpXdot1dcbxConfigTCSupportedEntry_Object = MibTableRow
fslldpXdot1dcbxConfigTCSupportedEntry = _FslldpXdot1dcbxConfigTCSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxConfigTCSupportedEntry.setStatus("current")


class _FslldpXdot1dcbxConfigTCSupportedTxEnable_Type(TruthValue):
    """Custom type fslldpXdot1dcbxConfigTCSupportedTxEnable based on TruthValue"""
    defaultValue = 2


_FslldpXdot1dcbxConfigTCSupportedTxEnable_Type.__name__ = "TruthValue"
_FslldpXdot1dcbxConfigTCSupportedTxEnable_Object = MibTableColumn
fslldpXdot1dcbxConfigTCSupportedTxEnable = _FslldpXdot1dcbxConfigTCSupportedTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 1, 1, 1),
    _FslldpXdot1dcbxConfigTCSupportedTxEnable_Type()
)
fslldpXdot1dcbxConfigTCSupportedTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxConfigTCSupportedTxEnable.setStatus("current")
_FslldpXdot1dcbxLocTCSupportedTable_Object = MibTable
fslldpXdot1dcbxLocTCSupportedTable = _FslldpXdot1dcbxLocTCSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 2)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxLocTCSupportedTable.setStatus("current")
_FslldpXdot1dcbxLocTCSupportedEntry_Object = MibTableRow
fslldpXdot1dcbxLocTCSupportedEntry = _FslldpXdot1dcbxLocTCSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 2, 1)
)
fslldpXdot1dcbxLocTCSupportedEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxLocTCSupportedEntry.setStatus("current")
_FslldpXdot1dcbxLocTCSupported_Type = FsLldpXdot1dcbxTCSupportedCapacity
_FslldpXdot1dcbxLocTCSupported_Object = MibTableColumn
fslldpXdot1dcbxLocTCSupported = _FslldpXdot1dcbxLocTCSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 2, 1, 1),
    _FslldpXdot1dcbxLocTCSupported_Type()
)
fslldpXdot1dcbxLocTCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxLocTCSupported.setStatus("current")
_FslldpXdot1dcbxRemTCSupportedTable_Object = MibTable
fslldpXdot1dcbxRemTCSupportedTable = _FslldpXdot1dcbxRemTCSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 3)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxRemTCSupportedTable.setStatus("current")
_FslldpXdot1dcbxRemTCSupportedEntry_Object = MibTableRow
fslldpXdot1dcbxRemTCSupportedEntry = _FslldpXdot1dcbxRemTCSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 3, 1)
)
fslldpXdot1dcbxRemTCSupportedEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxRemTCSupportedEntry.setStatus("current")
_FslldpXdot1dcbxRemTCSupported_Type = FsLldpXdot1dcbxTCSupportedCapacity
_FslldpXdot1dcbxRemTCSupported_Object = MibTableColumn
fslldpXdot1dcbxRemTCSupported = _FslldpXdot1dcbxRemTCSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 3, 1, 1),
    _FslldpXdot1dcbxRemTCSupported_Type()
)
fslldpXdot1dcbxRemTCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxRemTCSupported.setStatus("current")
_FslldpXdot1dcbxAdminTCSupportedTable_Object = MibTable
fslldpXdot1dcbxAdminTCSupportedTable = _FslldpXdot1dcbxAdminTCSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 4)
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxAdminTCSupportedTable.setStatus("current")
_FslldpXdot1dcbxAdminTCSupportedEntry_Object = MibTableRow
fslldpXdot1dcbxAdminTCSupportedEntry = _FslldpXdot1dcbxAdminTCSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 4, 1)
)
fslldpXdot1dcbxAdminTCSupportedEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    fslldpXdot1dcbxAdminTCSupportedEntry.setStatus("current")
_FslldpXdot1dcbxAdminTCSupported_Type = FsLldpXdot1dcbxTCSupportedCapacity
_FslldpXdot1dcbxAdminTCSupported_Object = MibTableColumn
fslldpXdot1dcbxAdminTCSupported = _FslldpXdot1dcbxAdminTCSupported_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 5, 4, 1, 1),
    _FslldpXdot1dcbxAdminTCSupported_Type()
)
fslldpXdot1dcbxAdminTCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fslldpXdot1dcbxAdminTCSupported.setStatus("current")
_FsDcbxCEEObjects_ObjectIdentity = ObjectIdentity
fsDcbxCEEObjects = _FsDcbxCEEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6)
)
_FsDcbxCEEScalars_ObjectIdentity = ObjectIdentity
fsDcbxCEEScalars = _FsDcbxCEEScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 1)
)


class _FsDcbxCEEGlobalEnableTrap_Type(Integer32):
    """Custom type fsDcbxCEEGlobalEnableTrap based on Integer32"""
    defaultValue = 0


_FsDcbxCEEGlobalEnableTrap_Type.__name__ = "Integer32"
_FsDcbxCEEGlobalEnableTrap_Object = MibScalar
fsDcbxCEEGlobalEnableTrap = _FsDcbxCEEGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 1, 1),
    _FsDcbxCEEGlobalEnableTrap_Type()
)
fsDcbxCEEGlobalEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcbxCEEGlobalEnableTrap.setStatus("current")
_FsDcbxCEEGeneratedTrapCount_Type = Unsigned32
_FsDcbxCEEGeneratedTrapCount_Object = MibScalar
fsDcbxCEEGeneratedTrapCount = _FsDcbxCEEGeneratedTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 1, 2),
    _FsDcbxCEEGeneratedTrapCount_Type()
)
fsDcbxCEEGeneratedTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEEGeneratedTrapCount.setStatus("current")


class _FsDcbxCEEClearCounters_Type(TruthValue):
    """Custom type fsDcbxCEEClearCounters based on TruthValue"""
    defaultValue = 2


_FsDcbxCEEClearCounters_Type.__name__ = "TruthValue"
_FsDcbxCEEClearCounters_Object = MibScalar
fsDcbxCEEClearCounters = _FsDcbxCEEClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 1, 3),
    _FsDcbxCEEClearCounters_Type()
)
fsDcbxCEEClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcbxCEEClearCounters.setStatus("current")
_FsDcbxCEECtrlTable_Object = MibTable
fsDcbxCEECtrlTable = _FsDcbxCEECtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2)
)
if mibBuilder.loadTexts:
    fsDcbxCEECtrlTable.setStatus("current")
_FsDcbxCEECtrlEntry_Object = MibTableRow
fsDcbxCEECtrlEntry = _FsDcbxCEECtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1)
)
fsDcbxCEECtrlEntry.setIndexNames(
    (0, "ARICENT-DCB-MIB", "fsDcbxCEECtrlPortNumber"),
)
if mibBuilder.loadTexts:
    fsDcbxCEECtrlEntry.setStatus("current")
_FsDcbxCEECtrlPortNumber_Type = InterfaceIndex
_FsDcbxCEECtrlPortNumber_Object = MibTableColumn
fsDcbxCEECtrlPortNumber = _FsDcbxCEECtrlPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 1),
    _FsDcbxCEECtrlPortNumber_Type()
)
fsDcbxCEECtrlPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlPortNumber.setStatus("current")
_FsDcbxCEECtrlSeqNo_Type = Unsigned32
_FsDcbxCEECtrlSeqNo_Object = MibTableColumn
fsDcbxCEECtrlSeqNo = _FsDcbxCEECtrlSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 2),
    _FsDcbxCEECtrlSeqNo_Type()
)
fsDcbxCEECtrlSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlSeqNo.setStatus("current")
_FsDcbxCEECtrlAckNo_Type = Unsigned32
_FsDcbxCEECtrlAckNo_Object = MibTableColumn
fsDcbxCEECtrlAckNo = _FsDcbxCEECtrlAckNo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 3),
    _FsDcbxCEECtrlAckNo_Type()
)
fsDcbxCEECtrlAckNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlAckNo.setStatus("current")
_FsDcbxCEECtrlRcvdAckNo_Type = Unsigned32
_FsDcbxCEECtrlRcvdAckNo_Object = MibTableColumn
fsDcbxCEECtrlRcvdAckNo = _FsDcbxCEECtrlRcvdAckNo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 4),
    _FsDcbxCEECtrlRcvdAckNo_Type()
)
fsDcbxCEECtrlRcvdAckNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlRcvdAckNo.setStatus("current")
_FsDcbxCEECtrlTxTLVCounter_Type = Counter32
_FsDcbxCEECtrlTxTLVCounter_Object = MibTableColumn
fsDcbxCEECtrlTxTLVCounter = _FsDcbxCEECtrlTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 5),
    _FsDcbxCEECtrlTxTLVCounter_Type()
)
fsDcbxCEECtrlTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlTxTLVCounter.setStatus("current")
_FsDcbxCEECtrlRxTLVCounter_Type = Counter32
_FsDcbxCEECtrlRxTLVCounter_Object = MibTableColumn
fsDcbxCEECtrlRxTLVCounter = _FsDcbxCEECtrlRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 6),
    _FsDcbxCEECtrlRxTLVCounter_Type()
)
fsDcbxCEECtrlRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlRxTLVCounter.setStatus("current")
_FsDcbxCEECtrlRxTLVErrorCounter_Type = Counter32
_FsDcbxCEECtrlRxTLVErrorCounter_Object = MibTableColumn
fsDcbxCEECtrlRxTLVErrorCounter = _FsDcbxCEECtrlRxTLVErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 3, 6, 2, 1, 7),
    _FsDcbxCEECtrlRxTLVErrorCounter_Type()
)
fsDcbxCEECtrlRxTLVErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDcbxCEECtrlRxTLVErrorCounter.setStatus("current")
_FsDcbNotificationObjects_ObjectIdentity = ObjectIdentity
fsDcbNotificationObjects = _FsDcbNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4)
)
_FsDCBTraps_ObjectIdentity = ObjectIdentity
fsDCBTraps = _FsDCBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0)
)
_FsDCBTrapObjects_ObjectIdentity = ObjectIdentity
fsDCBTrapObjects = _FsDCBTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 1)
)
_FsDcbTrapPortNumber_Type = InterfaceIndex
_FsDcbTrapPortNumber_Object = MibScalar
fsDcbTrapPortNumber = _FsDcbTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 1, 1),
    _FsDcbTrapPortNumber_Type()
)
fsDcbTrapPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDcbTrapPortNumber.setStatus("current")
_FsDcbPeerUpStatus_Type = TruthValue
_FsDcbPeerUpStatus_Object = MibScalar
fsDcbPeerUpStatus = _FsDcbPeerUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 1, 2),
    _FsDcbPeerUpStatus_Type()
)
fsDcbPeerUpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDcbPeerUpStatus.setStatus("current")


class _FsDcbFeatureType_Type(Integer32):
    """Custom type fsDcbFeatureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("priorityGroup", 1),
          ("priorityFlowControl", 2),
          ("applicationPriority", 3))
    )


_FsDcbFeatureType_Type.__name__ = "Integer32"
_FsDcbFeatureType_Object = MibScalar
fsDcbFeatureType = _FsDcbFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 1, 3),
    _FsDcbFeatureType_Type()
)
fsDcbFeatureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDcbFeatureType.setStatus("current")
lldpXdot1dcbxAdminApplicationPriorityAppEntry.registerAugmentions(
    ("ARICENT-DCB-MIB",
     "fsAppPriXAppEntry")
)
fsAppPriXAppEntry.setIndexNames(*lldpXdot1dcbxAdminApplicationPriorityAppEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("ARICENT-DCB-MIB",
     "fslldpXdot1dcbxConfigTCSupportedEntry")
)
fslldpXdot1dcbxConfigTCSupportedEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsETSModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 1)
)
fsETSModuleStatusTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsETSModuleStatus")
)
if mibBuilder.loadTexts:
    fsETSModuleStatusTrap.setStatus(
        "current"
    )

fsETSPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 2)
)
fsETSPortAdminStatusTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsETSAdminMode"))
)
if mibBuilder.loadTexts:
    fsETSPortAdminStatusTrap.setStatus(
        "current"
    )

fsETSPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 3)
)
fsETSPortPeerStatusTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    fsETSPortPeerStatusTrap.setStatus(
        "current"
    )

fsETSPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 4)
)
fsETSPortDcbxOperStateTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsETSDcbxOperState"))
)
if mibBuilder.loadTexts:
    fsETSPortDcbxOperStateTrap.setStatus(
        "current"
    )

fsPFCModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 5)
)
fsPFCModuleStatusTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsPFCModuleStatus")
)
if mibBuilder.loadTexts:
    fsPFCModuleStatusTrap.setStatus(
        "current"
    )

fsPFCPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 6)
)
fsPFCPortAdminStatusTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsPFCAdminMode"))
)
if mibBuilder.loadTexts:
    fsPFCPortAdminStatusTrap.setStatus(
        "current"
    )

fsPFCPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 7)
)
fsPFCPortPeerStatusTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    fsPFCPortPeerStatusTrap.setStatus(
        "current"
    )

fsPFCPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 8)
)
fsPFCPortDcbxOperStateTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsPFCDcbxOperState"))
)
if mibBuilder.loadTexts:
    fsPFCPortDcbxOperStateTrap.setStatus(
        "current"
    )

fsAppPriModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 9)
)
fsAppPriModuleStatusTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsAppPriModuleStatus")
)
if mibBuilder.loadTexts:
    fsAppPriModuleStatusTrap.setStatus(
        "current"
    )

fsAppPriPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 10)
)
fsAppPriPortAdminStatusTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsAppPriAdminMode"))
)
if mibBuilder.loadTexts:
    fsAppPriPortAdminStatusTrap.setStatus(
        "current"
    )

fsAppPriPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 11)
)
fsAppPriPortPeerStatusTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    fsAppPriPortPeerStatusTrap.setStatus(
        "current"
    )

fsAppPriPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 12)
)
fsAppPriPortDcbxOperStateTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsAppPriDcbxOperState"))
)
if mibBuilder.loadTexts:
    fsAppPriPortDcbxOperStateTrap.setStatus(
        "current"
    )

fsDcbxCEELldpTxDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 13)
)
fsDcbxCEELldpTxDisabledTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsDcbTrapPortNumber")
)
if mibBuilder.loadTexts:
    fsDcbxCEELldpTxDisabledTrap.setStatus(
        "current"
    )

fsDcbxCEELldpRxDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 14)
)
fsDcbxCEELldpRxDisabledTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsDcbTrapPortNumber")
)
if mibBuilder.loadTexts:
    fsDcbxCEELldpRxDisabledTrap.setStatus(
        "current"
    )

fsDcbxCEEDupControlTlvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 15)
)
fsDcbxCEEDupControlTlvTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsDcbTrapPortNumber")
)
if mibBuilder.loadTexts:
    fsDcbxCEEDupControlTlvTrap.setStatus(
        "current"
    )

fsDcbxCEEPeerNoRespTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 16)
)
fsDcbxCEEPeerNoRespTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbFeatureType"))
)
if mibBuilder.loadTexts:
    fsDcbxCEEPeerNoRespTrap.setStatus(
        "current"
    )

fsDcbxCEEDupFeatureTlvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 17)
)
fsDcbxCEEDupFeatureTlvTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbFeatureType"))
)
if mibBuilder.loadTexts:
    fsDcbxCEEDupFeatureTlvTrap.setStatus(
        "current"
    )

fsDcbxCEEPeerNoFeatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 18)
)
fsDcbxCEEPeerNoFeatureTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbFeatureType"))
)
if mibBuilder.loadTexts:
    fsDcbxCEEPeerNoFeatureTrap.setStatus(
        "current"
    )

fsDcbxCEEFeatureErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 19)
)
fsDcbxCEEFeatureErrorTrap.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDcbFeatureType"))
)
if mibBuilder.loadTexts:
    fsDcbxCEEFeatureErrorTrap.setStatus(
        "current"
    )

fsDcbxCEEAppPriProtocolNotSuppTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 20)
)
fsDcbxCEEAppPriProtocolNotSuppTrap.setObjects(
    ("ARICENT-DCB-MIB", "fsDcbTrapPortNumber")
)
if mibBuilder.loadTexts:
    fsDcbxCEEAppPriProtocolNotSuppTrap.setStatus(
        "current"
    )

fsDcbxCEEVersionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 22, 4, 0, 21)
)
fsDcbxCEEVersionChanged.setObjects(
      *(("ARICENT-DCB-MIB", "fsDcbTrapPortNumber"),
        ("ARICENT-DCB-MIB", "fsDCBXMode"))
)
if mibBuilder.loadTexts:
    fsDcbxCEEVersionChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-DCB-MIB",
    **{"EnabledStatus": EnabledStatus,
       "DcbAdminMode": DcbAdminMode,
       "DcbState": DcbState,
       "DcbxVersion": DcbxVersion,
       "DcbStateMachineType": DcbStateMachineType,
       "FsLldpXdot1dcbxTCSupportedCapacity": FsLldpXdot1dcbxTCSupportedCapacity,
       "DcbxStatus": DcbxStatus,
       "fsDcbMIB": fsDcbMIB,
       "fsDcbSystem": fsDcbSystem,
       "fsDcbPfcMinThreshold": fsDcbPfcMinThreshold,
       "fsDcbPfcMaxThreshold": fsDcbPfcMaxThreshold,
       "fsDcbMaxPfcProfiles": fsDcbMaxPfcProfiles,
       "fsDcbObjects": fsDcbObjects,
       "fsDcbPortTable": fsDcbPortTable,
       "fsDcbPortEntry": fsDcbPortEntry,
       "fsDcbPortNumber": fsDcbPortNumber,
       "fsDcbETSAdminStatus": fsDcbETSAdminStatus,
       "fsDcbPFCAdminStatus": fsDcbPFCAdminStatus,
       "fsDcbRowStatus": fsDcbRowStatus,
       "fsDcbAppPriAdminStatus": fsDcbAppPriAdminStatus,
       "fsDcbOperVersion": fsDcbOperVersion,
       "fsDcbMaxVersion": fsDcbMaxVersion,
       "fsDcbPeerOperVersion": fsDcbPeerOperVersion,
       "fsDcbPeerMaxVersion": fsDcbPeerMaxVersion,
       "fsDcbApplicationObjects": fsDcbApplicationObjects,
       "fsDCBXObjects": fsDCBXObjects,
       "fsDCBXScalars": fsDCBXScalars,
       "fsDcbxGlobalTraceLevel": fsDcbxGlobalTraceLevel,
       "fsDCBXPortTable": fsDCBXPortTable,
       "fsDCBXPortEntry": fsDCBXPortEntry,
       "fsDCBXPortNumber": fsDCBXPortNumber,
       "fsDCBXAdminStatus": fsDCBXAdminStatus,
       "fsDCBXMode": fsDCBXMode,
       "fsETSObjects": fsETSObjects,
       "fsETSScalars": fsETSScalars,
       "fsETSSystemControl": fsETSSystemControl,
       "fsETSModuleStatus": fsETSModuleStatus,
       "fsETSClearCounters": fsETSClearCounters,
       "fsETSGlobalEnableTrap": fsETSGlobalEnableTrap,
       "fsETSGeneratedTrapCount": fsETSGeneratedTrapCount,
       "fsETSPortTable": fsETSPortTable,
       "fsETSPortEntry": fsETSPortEntry,
       "fsETSPortNumber": fsETSPortNumber,
       "fsETSAdminMode": fsETSAdminMode,
       "fsETSDcbxOperState": fsETSDcbxOperState,
       "fsETSDcbxStateMachine": fsETSDcbxStateMachine,
       "fsETSClearTLVCounters": fsETSClearTLVCounters,
       "fsETSConfTxTLVCounter": fsETSConfTxTLVCounter,
       "fsETSConfRxTLVCounter": fsETSConfRxTLVCounter,
       "fsETSConfRxTLVErrors": fsETSConfRxTLVErrors,
       "fsETSRecoTxTLVCounter": fsETSRecoTxTLVCounter,
       "fsETSRecoRxTLVCounter": fsETSRecoRxTLVCounter,
       "fsETSRecoRxTLVErrors": fsETSRecoRxTLVErrors,
       "fsETSTcSuppTxTLVCounter": fsETSTcSuppTxTLVCounter,
       "fsETSTcSuppRxTLVCounter": fsETSTcSuppRxTLVCounter,
       "fsETSTcSuppRxTLVErrors": fsETSTcSuppRxTLVErrors,
       "fsETSRowStatus": fsETSRowStatus,
       "fsETSSyncd": fsETSSyncd,
       "fsETSError": fsETSError,
       "fsETSDcbxStatus": fsETSDcbxStatus,
       "fsPFCObjects": fsPFCObjects,
       "fsPFCScalars": fsPFCScalars,
       "fsPFCSystemControl": fsPFCSystemControl,
       "fsPFCModuleStatus": fsPFCModuleStatus,
       "fsPFCClearCounters": fsPFCClearCounters,
       "fsPFCGlobalEnableTrap": fsPFCGlobalEnableTrap,
       "fsPFCGeneratedTrapCount": fsPFCGeneratedTrapCount,
       "fsPFCPortTable": fsPFCPortTable,
       "fsPFCPortEntry": fsPFCPortEntry,
       "fsPFCPortNumber": fsPFCPortNumber,
       "fsPFCAdminMode": fsPFCAdminMode,
       "fsPFCDcbxOperState": fsPFCDcbxOperState,
       "fsPFCDcbxStateMachine": fsPFCDcbxStateMachine,
       "fsPFCClearTLVCounters": fsPFCClearTLVCounters,
       "fsPFCTxTLVCounter": fsPFCTxTLVCounter,
       "fsPFCRxTLVCounter": fsPFCRxTLVCounter,
       "fsPFCRxTLVErrors": fsPFCRxTLVErrors,
       "fsPFCRowStatus": fsPFCRowStatus,
       "fsPFCSyncd": fsPFCSyncd,
       "fsPFCError": fsPFCError,
       "fsPFCDcbxStatus": fsPFCDcbxStatus,
       "fsPFCRxPauseFrameCounter": fsPFCRxPauseFrameCounter,
       "fsPFCTxPauseFrameCounter": fsPFCTxPauseFrameCounter,
       "fsPFCRxPauseFrameP0Counter": fsPFCRxPauseFrameP0Counter,
       "fsPFCRxPauseFrameP1Counter": fsPFCRxPauseFrameP1Counter,
       "fsPFCRxPauseFrameP2Counter": fsPFCRxPauseFrameP2Counter,
       "fsPFCRxPauseFrameP3Counter": fsPFCRxPauseFrameP3Counter,
       "fsPFCRxPauseFrameP4Counter": fsPFCRxPauseFrameP4Counter,
       "fsPFCRxPauseFrameP5Counter": fsPFCRxPauseFrameP5Counter,
       "fsPFCRxPauseFrameP6Counter": fsPFCRxPauseFrameP6Counter,
       "fsPFCRxPauseFrameP7Counter": fsPFCRxPauseFrameP7Counter,
       "fsPFCTxPauseFrameP0Counter": fsPFCTxPauseFrameP0Counter,
       "fsPFCTxPauseFrameP1Counter": fsPFCTxPauseFrameP1Counter,
       "fsPFCTxPauseFrameP2Counter": fsPFCTxPauseFrameP2Counter,
       "fsPFCTxPauseFrameP3Counter": fsPFCTxPauseFrameP3Counter,
       "fsPFCTxPauseFrameP4Counter": fsPFCTxPauseFrameP4Counter,
       "fsPFCTxPauseFrameP5Counter": fsPFCTxPauseFrameP5Counter,
       "fsPFCTxPauseFrameP6Counter": fsPFCTxPauseFrameP6Counter,
       "fsPFCTxPauseFrameP7Counter": fsPFCTxPauseFrameP7Counter,
       "fsPFCDataFrameDiscardCounter": fsPFCDataFrameDiscardCounter,
       "fsPFCClearPauseFrameCounters": fsPFCClearPauseFrameCounters,
       "fsAppPriObjects": fsAppPriObjects,
       "fsAppPriScalars": fsAppPriScalars,
       "fsAppPriSystemControl": fsAppPriSystemControl,
       "fsAppPriModuleStatus": fsAppPriModuleStatus,
       "fsAppPriClearCounters": fsAppPriClearCounters,
       "fsAppPriGlobalEnableTrap": fsAppPriGlobalEnableTrap,
       "fsAppPriGeneratedTrapCount": fsAppPriGeneratedTrapCount,
       "fsAppPriPortTable": fsAppPriPortTable,
       "fsAppPriPortEntry": fsAppPriPortEntry,
       "fsAppPriPortNumber": fsAppPriPortNumber,
       "fsAppPriAdminMode": fsAppPriAdminMode,
       "fsAppPriDcbxOperState": fsAppPriDcbxOperState,
       "fsAppPriDcbxStateMachine": fsAppPriDcbxStateMachine,
       "fsAppPriClearTLVCounters": fsAppPriClearTLVCounters,
       "fsAppPriTxTLVCounter": fsAppPriTxTLVCounter,
       "fsAppPriRxTLVCounter": fsAppPriRxTLVCounter,
       "fsAppPriRxTLVErrors": fsAppPriRxTLVErrors,
       "fsAppPriAppProtocols": fsAppPriAppProtocols,
       "fsAppPriRowStatus": fsAppPriRowStatus,
       "fsAppPriSyncd": fsAppPriSyncd,
       "fsAppPriError": fsAppPriError,
       "fsAppPriDcbxStatus": fsAppPriDcbxStatus,
       "fsAppPriXAppTable": fsAppPriXAppTable,
       "fsAppPriXAppEntry": fsAppPriXAppEntry,
       "fsAppPriXAppRowStatus": fsAppPriXAppRowStatus,
       "fslldpXdot1dcbxLocApplicationPriorityBasicTable": fslldpXdot1dcbxLocApplicationPriorityBasicTable,
       "fslldpXdot1dcbxLocApplicationPriorityBasicEntry": fslldpXdot1dcbxLocApplicationPriorityBasicEntry,
       "fslldpXdot1dcbxLocApplicationPriorityWilling": fslldpXdot1dcbxLocApplicationPriorityWilling,
       "fslldpXdot1dcbxAdminApplicationPriorityBasicTable": fslldpXdot1dcbxAdminApplicationPriorityBasicTable,
       "fslldpXdot1dcbxAdminApplicationPriorityBasicEntry": fslldpXdot1dcbxAdminApplicationPriorityBasicEntry,
       "fslldpXdot1dcbxAdminApplicationPriorityWilling": fslldpXdot1dcbxAdminApplicationPriorityWilling,
       "fslldpXdot1dcbxRemApplicationPriorityBasicTable": fslldpXdot1dcbxRemApplicationPriorityBasicTable,
       "fslldpXdot1dcbxRemApplicationPriorityBasicEntry": fslldpXdot1dcbxRemApplicationPriorityBasicEntry,
       "fslldpXdot1dcbxRemApplicationPriorityWilling": fslldpXdot1dcbxRemApplicationPriorityWilling,
       "fsTCSupportedObjects": fsTCSupportedObjects,
       "fslldpXdot1dcbxConfigTCSupportedTable": fslldpXdot1dcbxConfigTCSupportedTable,
       "fslldpXdot1dcbxConfigTCSupportedEntry": fslldpXdot1dcbxConfigTCSupportedEntry,
       "fslldpXdot1dcbxConfigTCSupportedTxEnable": fslldpXdot1dcbxConfigTCSupportedTxEnable,
       "fslldpXdot1dcbxLocTCSupportedTable": fslldpXdot1dcbxLocTCSupportedTable,
       "fslldpXdot1dcbxLocTCSupportedEntry": fslldpXdot1dcbxLocTCSupportedEntry,
       "fslldpXdot1dcbxLocTCSupported": fslldpXdot1dcbxLocTCSupported,
       "fslldpXdot1dcbxRemTCSupportedTable": fslldpXdot1dcbxRemTCSupportedTable,
       "fslldpXdot1dcbxRemTCSupportedEntry": fslldpXdot1dcbxRemTCSupportedEntry,
       "fslldpXdot1dcbxRemTCSupported": fslldpXdot1dcbxRemTCSupported,
       "fslldpXdot1dcbxAdminTCSupportedTable": fslldpXdot1dcbxAdminTCSupportedTable,
       "fslldpXdot1dcbxAdminTCSupportedEntry": fslldpXdot1dcbxAdminTCSupportedEntry,
       "fslldpXdot1dcbxAdminTCSupported": fslldpXdot1dcbxAdminTCSupported,
       "fsDcbxCEEObjects": fsDcbxCEEObjects,
       "fsDcbxCEEScalars": fsDcbxCEEScalars,
       "fsDcbxCEEGlobalEnableTrap": fsDcbxCEEGlobalEnableTrap,
       "fsDcbxCEEGeneratedTrapCount": fsDcbxCEEGeneratedTrapCount,
       "fsDcbxCEEClearCounters": fsDcbxCEEClearCounters,
       "fsDcbxCEECtrlTable": fsDcbxCEECtrlTable,
       "fsDcbxCEECtrlEntry": fsDcbxCEECtrlEntry,
       "fsDcbxCEECtrlPortNumber": fsDcbxCEECtrlPortNumber,
       "fsDcbxCEECtrlSeqNo": fsDcbxCEECtrlSeqNo,
       "fsDcbxCEECtrlAckNo": fsDcbxCEECtrlAckNo,
       "fsDcbxCEECtrlRcvdAckNo": fsDcbxCEECtrlRcvdAckNo,
       "fsDcbxCEECtrlTxTLVCounter": fsDcbxCEECtrlTxTLVCounter,
       "fsDcbxCEECtrlRxTLVCounter": fsDcbxCEECtrlRxTLVCounter,
       "fsDcbxCEECtrlRxTLVErrorCounter": fsDcbxCEECtrlRxTLVErrorCounter,
       "fsDcbNotificationObjects": fsDcbNotificationObjects,
       "fsDCBTraps": fsDCBTraps,
       "fsETSModuleStatusTrap": fsETSModuleStatusTrap,
       "fsETSPortAdminStatusTrap": fsETSPortAdminStatusTrap,
       "fsETSPortPeerStatusTrap": fsETSPortPeerStatusTrap,
       "fsETSPortDcbxOperStateTrap": fsETSPortDcbxOperStateTrap,
       "fsPFCModuleStatusTrap": fsPFCModuleStatusTrap,
       "fsPFCPortAdminStatusTrap": fsPFCPortAdminStatusTrap,
       "fsPFCPortPeerStatusTrap": fsPFCPortPeerStatusTrap,
       "fsPFCPortDcbxOperStateTrap": fsPFCPortDcbxOperStateTrap,
       "fsAppPriModuleStatusTrap": fsAppPriModuleStatusTrap,
       "fsAppPriPortAdminStatusTrap": fsAppPriPortAdminStatusTrap,
       "fsAppPriPortPeerStatusTrap": fsAppPriPortPeerStatusTrap,
       "fsAppPriPortDcbxOperStateTrap": fsAppPriPortDcbxOperStateTrap,
       "fsDcbxCEELldpTxDisabledTrap": fsDcbxCEELldpTxDisabledTrap,
       "fsDcbxCEELldpRxDisabledTrap": fsDcbxCEELldpRxDisabledTrap,
       "fsDcbxCEEDupControlTlvTrap": fsDcbxCEEDupControlTlvTrap,
       "fsDcbxCEEPeerNoRespTrap": fsDcbxCEEPeerNoRespTrap,
       "fsDcbxCEEDupFeatureTlvTrap": fsDcbxCEEDupFeatureTlvTrap,
       "fsDcbxCEEPeerNoFeatureTrap": fsDcbxCEEPeerNoFeatureTrap,
       "fsDcbxCEEFeatureErrorTrap": fsDcbxCEEFeatureErrorTrap,
       "fsDcbxCEEAppPriProtocolNotSuppTrap": fsDcbxCEEAppPriProtocolNotSuppTrap,
       "fsDcbxCEEVersionChanged": fsDcbxCEEVersionChanged,
       "fsDCBTrapObjects": fsDCBTrapObjects,
       "fsDcbTrapPortNumber": fsDcbTrapPortNumber,
       "fsDcbPeerUpStatus": fsDcbPeerUpStatus,
       "fsDcbFeatureType": fsDcbFeatureType}
)
