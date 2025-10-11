# SNMP MIB module (CPQHSV300V9-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQHSV300V9-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:23 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqElementManager_ObjectIdentity = ObjectIdentity
cpqElementManager = _CpqElementManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136)
)
_CpqHSV_ObjectIdentity = ObjectIdentity
cpqHSV = _CpqHSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1)
)
_CpqHSVAgent_ObjectIdentity = ObjectIdentity
cpqHSVAgent = _CpqHSVAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1)
)
_AgManufacturer_Type = DisplayString
_AgManufacturer_Object = MibScalar
agManufacturer = _AgManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 1),
    _AgManufacturer_Type()
)
agManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agManufacturer.setStatus("mandatory")
_AgMajVersion_Type = Integer32
_AgMajVersion_Object = MibScalar
agMajVersion = _AgMajVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 2),
    _AgMajVersion_Type()
)
agMajVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMajVersion.setStatus("mandatory")
_AgMinVersion_Type = Integer32
_AgMinVersion_Object = MibScalar
agMinVersion = _AgMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 3),
    _AgMinVersion_Type()
)
agMinVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMinVersion.setStatus("mandatory")
_AgHostName_Type = DisplayString
_AgHostName_Object = MibScalar
agHostName = _AgHostName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 4),
    _AgHostName_Type()
)
agHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agHostName.setStatus("mandatory")
_AgEnterprise_Type = ObjectIdentifier
_AgEnterprise_Object = MibScalar
agEnterprise = _AgEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 5),
    _AgEnterprise_Type()
)
agEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnterprise.setStatus("mandatory")
_AgDescription_Type = DisplayString
_AgDescription_Object = MibScalar
agDescription = _AgDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 6),
    _AgDescription_Type()
)
agDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDescription.setStatus("mandatory")
_AgStatusTable_Object = MibTable
agStatusTable = _AgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7)
)
if mibBuilder.loadTexts:
    agStatusTable.setStatus("mandatory")
_AgentEntry_Object = MibTableRow
agentEntry = _AgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1)
)
agentEntry.setIndexNames(
    (0, "CPQHSV300V9-MIB", "agentEntryIndex"),
)
if mibBuilder.loadTexts:
    agentEntry.setStatus("mandatory")
_AgentEntryIndex_Type = Integer32
_AgentEntryIndex_Object = MibTableColumn
agentEntryIndex = _AgentEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 1),
    _AgentEntryIndex_Type()
)
agentEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEntryIndex.setStatus("mandatory")


class _AgentStatus_Type(Integer32):
    """Custom type agentStatus based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_AgentStatus_Type.__name__ = "Integer32"
_AgentStatus_Object = MibTableColumn
agentStatus = _AgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 2),
    _AgentStatus_Type()
)
agentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatus.setStatus("mandatory")
_AgentEventCode_Type = Integer32
_AgentEventCode_Object = MibTableColumn
agentEventCode = _AgentEventCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 3),
    _AgentEventCode_Type()
)
agentEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventCode.setStatus("mandatory")
_AgentEventLevel_Type = Integer32
_AgentEventLevel_Object = MibTableColumn
agentEventLevel = _AgentEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 4),
    _AgentEventLevel_Type()
)
agentEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventLevel.setStatus("mandatory")
_AgentEventTimeDate_Type = DisplayString
_AgentEventTimeDate_Object = MibTableColumn
agentEventTimeDate = _AgentEventTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 5),
    _AgentEventTimeDate_Type()
)
agentEventTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventTimeDate.setStatus("mandatory")
_AgentEventDescription_Type = DisplayString
_AgentEventDescription_Object = MibTableColumn
agentEventDescription = _AgentEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 6),
    _AgentEventDescription_Type()
)
agentEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventDescription.setStatus("mandatory")
_CpqHSVServer_ObjectIdentity = ObjectIdentity
cpqHSVServer = _CpqHSVServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2)
)
_SrvCPU_Type = DisplayString
_SrvCPU_Object = MibScalar
srvCPU = _SrvCPU_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 1),
    _SrvCPU_Type()
)
srvCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCPU.setStatus("mandatory")
_SrvComputerType_Type = DisplayString
_SrvComputerType_Object = MibScalar
srvComputerType = _SrvComputerType_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 2),
    _SrvComputerType_Type()
)
srvComputerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvComputerType.setStatus("mandatory")
_SrvModel_Type = Integer32
_SrvModel_Object = MibScalar
srvModel = _SrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 3),
    _SrvModel_Type()
)
srvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvModel.setStatus("mandatory")
_SrvSubModel_Type = Integer32
_SrvSubModel_Object = MibScalar
srvSubModel = _SrvSubModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 4),
    _SrvSubModel_Type()
)
srvSubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvSubModel.setStatus("mandatory")
_SrvBiosVersion_Type = DisplayString
_SrvBiosVersion_Object = MibScalar
srvBiosVersion = _SrvBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 5),
    _SrvBiosVersion_Type()
)
srvBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvBiosVersion.setStatus("mandatory")
_SrvOS_Type = DisplayString
_SrvOS_Object = MibScalar
srvOS = _SrvOS_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 6),
    _SrvOS_Type()
)
srvOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOS.setStatus("mandatory")
_SrvOSMajVersion_Type = Integer32
_SrvOSMajVersion_Object = MibScalar
srvOSMajVersion = _SrvOSMajVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 7),
    _SrvOSMajVersion_Type()
)
srvOSMajVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOSMajVersion.setStatus("mandatory")
_SrvOSMinVersion_Type = Integer32
_SrvOSMinVersion_Object = MibScalar
srvOSMinVersion = _SrvOSMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 8),
    _SrvOSMinVersion_Type()
)
srvOSMinVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOSMinVersion.setStatus("mandatory")
_HsvObject_ObjectIdentity = ObjectIdentity
hsvObject = _HsvObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3)
)
_Scell_ObjectIdentity = ObjectIdentity
scell = _Scell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1)
)
_ScellTotal_Type = Integer32
_ScellTotal_Object = MibScalar
scellTotal = _ScellTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 1),
    _ScellTotal_Type()
)
scellTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellTotal.setStatus("mandatory")
_ScellStatusTable_Object = MibTable
scellStatusTable = _ScellStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    scellStatusTable.setStatus("mandatory")
_ScellEntry_Object = MibTableRow
scellEntry = _ScellEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1)
)
scellEntry.setIndexNames(
    (0, "CPQHSV300V9-MIB", "scellEntryIndex"),
)
if mibBuilder.loadTexts:
    scellEntry.setStatus("mandatory")
_ScellEntryIndex_Type = Integer32
_ScellEntryIndex_Object = MibTableColumn
scellEntryIndex = _ScellEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 1),
    _ScellEntryIndex_Type()
)
scellEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEntryIndex.setStatus("mandatory")
_ScellName_Type = DisplayString
_ScellName_Object = MibTableColumn
scellName = _ScellName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 2),
    _ScellName_Type()
)
scellName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellName.setStatus("mandatory")
_ScellUUID_Type = DisplayString
_ScellUUID_Object = MibTableColumn
scellUUID = _ScellUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 3),
    _ScellUUID_Type()
)
scellUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellUUID.setStatus("mandatory")


class _ScellStatus_Type(Integer32):
    """Custom type scellStatus based on Integer32"""
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
        *(("informational", 1),
          ("minor", 2),
          ("major", 3),
          ("failed", 4))
    )


_ScellStatus_Type.__name__ = "Integer32"
_ScellStatus_Object = MibTableColumn
scellStatus = _ScellStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 4),
    _ScellStatus_Type()
)
scellStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellStatus.setStatus("mandatory")
_ScellEventDescription_Type = DisplayString
_ScellEventDescription_Object = MibTableColumn
scellEventDescription = _ScellEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 5),
    _ScellEventDescription_Type()
)
scellEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEventDescription.setStatus("mandatory")
_ScellEventTimeDate_Type = DisplayString
_ScellEventTimeDate_Object = MibTableColumn
scellEventTimeDate = _ScellEventTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 6),
    _ScellEventTimeDate_Type()
)
scellEventTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEventTimeDate.setStatus("mandatory")
_ScellEventCode_Type = DisplayString
_ScellEventCode_Object = MibTableColumn
scellEventCode = _ScellEventCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 7),
    _ScellEventCode_Type()
)
scellEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEventCode.setStatus("mandatory")
_ScellSWComponent_Type = Integer32
_ScellSWComponent_Object = MibTableColumn
scellSWComponent = _ScellSWComponent_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 8),
    _ScellSWComponent_Type()
)
scellSWComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellSWComponent.setStatus("mandatory")
_ScellECode_Type = Integer32
_ScellECode_Object = MibTableColumn
scellECode = _ScellECode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 9),
    _ScellECode_Type()
)
scellECode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellECode.setStatus("mandatory")
_ScellCAC_Type = Integer32
_ScellCAC_Object = MibTableColumn
scellCAC = _ScellCAC_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 10),
    _ScellCAC_Type()
)
scellCAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellCAC.setStatus("mandatory")
_ScellEIP_Type = Integer32
_ScellEIP_Object = MibTableColumn
scellEIP = _ScellEIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 11),
    _ScellEIP_Type()
)
scellEIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEIP.setStatus("mandatory")
_ScellNameDateTime_Type = DisplayString
_ScellNameDateTime_Object = MibTableColumn
scellNameDateTime = _ScellNameDateTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 12),
    _ScellNameDateTime_Type()
)
scellNameDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellNameDateTime.setStatus("mandatory")
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 2)
)
_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3)
)
_HostTotal_Type = Integer32
_HostTotal_Object = MibScalar
hostTotal = _HostTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 1),
    _HostTotal_Type()
)
hostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTotal.setStatus("mandatory")
_HostStatusTable_Object = MibTable
hostStatusTable = _HostStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hostStatusTable.setStatus("mandatory")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1)
)
hostEntry.setIndexNames(
    (0, "CPQHSV300V9-MIB", "hostEntryIndex"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("mandatory")
_HostEntryIndex_Type = Integer32
_HostEntryIndex_Object = MibTableColumn
hostEntryIndex = _HostEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 1),
    _HostEntryIndex_Type()
)
hostEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostEntryIndex.setStatus("mandatory")
_HostName_Type = DisplayString
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_HostUUID_Type = DisplayString
_HostUUID_Object = MibTableColumn
hostUUID = _HostUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 3),
    _HostUUID_Type()
)
hostUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostUUID.setStatus("mandatory")


class _HostStatus_Type(Integer32):
    """Custom type hostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 0),
          ("minor", 1),
          ("major", 2),
          ("critical", 3))
    )


_HostStatus_Type.__name__ = "Integer32"
_HostStatus_Object = MibTableColumn
hostStatus = _HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 4),
    _HostStatus_Type()
)
hostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatus.setStatus("mandatory")
_Nsc_ObjectIdentity = ObjectIdentity
nsc = _Nsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4)
)
_NscTotal_Type = Integer32
_NscTotal_Object = MibScalar
nscTotal = _NscTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 1),
    _NscTotal_Type()
)
nscTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscTotal.setStatus("mandatory")
_NscStatusTable_Object = MibTable
nscStatusTable = _NscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    nscStatusTable.setStatus("mandatory")
_NscEntry_Object = MibTableRow
nscEntry = _NscEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1)
)
nscEntry.setIndexNames(
    (0, "CPQHSV300V9-MIB", "nscEntryIndex"),
)
if mibBuilder.loadTexts:
    nscEntry.setStatus("mandatory")
_NscEntryIndex_Type = Integer32
_NscEntryIndex_Object = MibTableColumn
nscEntryIndex = _NscEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 1),
    _NscEntryIndex_Type()
)
nscEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscEntryIndex.setStatus("mandatory")
_NscName_Type = DisplayString
_NscName_Object = MibTableColumn
nscName = _NscName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 2),
    _NscName_Type()
)
nscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscName.setStatus("mandatory")
_NscUUID_Type = DisplayString
_NscUUID_Object = MibTableColumn
nscUUID = _NscUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 3),
    _NscUUID_Type()
)
nscUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscUUID.setStatus("mandatory")


class _NscStatus_Type(Integer32):
    """Custom type nscStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 0),
          ("minor", 1),
          ("major", 2),
          ("critical", 3))
    )


_NscStatus_Type.__name__ = "Integer32"
_NscStatus_Object = MibTableColumn
nscStatus = _NscStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 4),
    _NscStatus_Type()
)
nscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscStatus.setStatus("mandatory")
_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8)
)
_ShelfTotal_Type = Integer32
_ShelfTotal_Object = MibScalar
shelfTotal = _ShelfTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 1),
    _ShelfTotal_Type()
)
shelfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTotal.setStatus("mandatory")
_ShelfStatusTable_Object = MibTable
shelfStatusTable = _ShelfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    shelfStatusTable.setStatus("mandatory")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1)
)
shelfEntry.setIndexNames(
    (0, "CPQHSV300V9-MIB", "shelfEntryIndex"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("mandatory")
_ShelfEntryIndex_Type = Integer32
_ShelfEntryIndex_Object = MibTableColumn
shelfEntryIndex = _ShelfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 1),
    _ShelfEntryIndex_Type()
)
shelfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfEntryIndex.setStatus("mandatory")


class _ShelfStatus_Type(Integer32):
    """Custom type shelfStatus based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_ShelfStatus_Type.__name__ = "Integer32"
_ShelfStatus_Object = MibTableColumn
shelfStatus = _ShelfStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 2),
    _ShelfStatus_Type()
)
shelfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfStatus.setStatus("mandatory")
_ShelfId_Type = Integer32
_ShelfId_Object = MibTableColumn
shelfId = _ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 3),
    _ShelfId_Type()
)
shelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfId.setStatus("mandatory")
_ShelfElementType_Type = Integer32
_ShelfElementType_Object = MibTableColumn
shelfElementType = _ShelfElementType_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 4),
    _ShelfElementType_Type()
)
shelfElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfElementType.setStatus("mandatory")
_ShelfElementNum_Type = Integer32
_ShelfElementNum_Object = MibTableColumn
shelfElementNum = _ShelfElementNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 5),
    _ShelfElementNum_Type()
)
shelfElementNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfElementNum.setStatus("mandatory")
_ShelfErrorCode_Type = Integer32
_ShelfErrorCode_Object = MibTableColumn
shelfErrorCode = _ShelfErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 6),
    _ShelfErrorCode_Type()
)
shelfErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfErrorCode.setStatus("mandatory")
_MaHSVMibRev_ObjectIdentity = ObjectIdentity
maHSVMibRev = _MaHSVMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 4)
)
_MaHSVMibRevMajor_Type = Integer32
_MaHSVMibRevMajor_Object = MibScalar
maHSVMibRevMajor = _MaHSVMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 4, 1),
    _MaHSVMibRevMajor_Type()
)
maHSVMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maHSVMibRevMajor.setStatus("mandatory")
_MaHSVMibRevMinor_Type = Integer32
_MaHSVMibRevMinor_Object = MibScalar
maHSVMibRevMinor = _MaHSVMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 4, 2),
    _MaHSVMibRevMinor_Type()
)
maHSVMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maHSVMibRevMinor.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQHSV300V9-MIB",
    **{"compaq": compaq,
       "cpqElementManager": cpqElementManager,
       "cpqHSV": cpqHSV,
       "cpqHSVAgent": cpqHSVAgent,
       "agManufacturer": agManufacturer,
       "agMajVersion": agMajVersion,
       "agMinVersion": agMinVersion,
       "agHostName": agHostName,
       "agEnterprise": agEnterprise,
       "agDescription": agDescription,
       "agStatusTable": agStatusTable,
       "agentEntry": agentEntry,
       "agentEntryIndex": agentEntryIndex,
       "agentStatus": agentStatus,
       "agentEventCode": agentEventCode,
       "agentEventLevel": agentEventLevel,
       "agentEventTimeDate": agentEventTimeDate,
       "agentEventDescription": agentEventDescription,
       "cpqHSVServer": cpqHSVServer,
       "srvCPU": srvCPU,
       "srvComputerType": srvComputerType,
       "srvModel": srvModel,
       "srvSubModel": srvSubModel,
       "srvBiosVersion": srvBiosVersion,
       "srvOS": srvOS,
       "srvOSMajVersion": srvOSMajVersion,
       "srvOSMinVersion": srvOSMinVersion,
       "hsvObject": hsvObject,
       "scell": scell,
       "scellTotal": scellTotal,
       "scellStatusTable": scellStatusTable,
       "scellEntry": scellEntry,
       "scellEntryIndex": scellEntryIndex,
       "scellName": scellName,
       "scellUUID": scellUUID,
       "scellStatus": scellStatus,
       "scellEventDescription": scellEventDescription,
       "scellEventTimeDate": scellEventTimeDate,
       "scellEventCode": scellEventCode,
       "scellSWComponent": scellSWComponent,
       "scellECode": scellECode,
       "scellCAC": scellCAC,
       "scellEIP": scellEIP,
       "scellNameDateTime": scellNameDateTime,
       "agent": agent,
       "host": host,
       "hostTotal": hostTotal,
       "hostStatusTable": hostStatusTable,
       "hostEntry": hostEntry,
       "hostEntryIndex": hostEntryIndex,
       "hostName": hostName,
       "hostUUID": hostUUID,
       "hostStatus": hostStatus,
       "nsc": nsc,
       "nscTotal": nscTotal,
       "nscStatusTable": nscStatusTable,
       "nscEntry": nscEntry,
       "nscEntryIndex": nscEntryIndex,
       "nscName": nscName,
       "nscUUID": nscUUID,
       "nscStatus": nscStatus,
       "shelf": shelf,
       "shelfTotal": shelfTotal,
       "shelfStatusTable": shelfStatusTable,
       "shelfEntry": shelfEntry,
       "shelfEntryIndex": shelfEntryIndex,
       "shelfStatus": shelfStatus,
       "shelfId": shelfId,
       "shelfElementType": shelfElementType,
       "shelfElementNum": shelfElementNum,
       "shelfErrorCode": shelfErrorCode,
       "maHSVMibRev": maHSVMibRev,
       "maHSVMibRevMajor": maHSVMibRevMajor,
       "maHSVMibRevMinor": maHSVMibRevMinor}
)
