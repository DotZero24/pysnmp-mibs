# SNMP MIB module (HPVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPVC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:35:49 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TransportAddress,
 TransportAddressType) = mibBuilder.importSymbols(
    "TRANSPORT-ADDRESS-MIB",
    "TransportAddress",
    "TransportAddressType")


# MODULE-IDENTITY

vcDomainMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vcDomainMIB.setRevisions(
        ("2017-04-05 00:00",
         "2017-02-28 00:00",
         "2016-08-10 00:00",
         "2016-03-21 00:00",
         "2014-03-05 00:00",
         "2013-10-25 00:00",
         "2012-12-12 00:00",
         "2012-06-27 00:00",
         "2010-03-08 00:00",
         "2009-06-27 00:00",
         "2009-02-17 00:00",
         "2009-01-08 00:00",
         "2008-12-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VcManagedStatus(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normal", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6),
          ("disabled", 7),
          ("info", 8))
    )



class VcDomainModuleRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unintegrated", 1),
          ("primaryProtected", 2),
          ("primaryUnprotected", 3),
          ("standby", 4),
          ("other", 5))
    )



class VcModuleType(TextualConvention, Integer32):
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
        *(("vcModuleEnet", 1),
          ("vcModuleFC", 2),
          ("vcModuleOther", 3))
    )



class VcPortType(TextualConvention, Integer32):
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
        *(("vcEnetPhysicalPort", 1),
          ("vcEnetLogicallPort", 2),
          ("vcFCPort", 3))
    )



class VcDomainReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(700,
              701,
              702,
              703,
              706,
              707,
              709,
              712,
              713,
              714,
              715,
              801,
              802,
              803,
              901)
        )
    )
    namedValues = NamedValues(
        *(("vcDomainOk", 700),
          ("vcDomainAbnormalEnclosuresAndProfiles", 701),
          ("vcDomainSomeEnclosuresAbnormal", 702),
          ("vcDomainUnmappedProfileConnections", 703),
          ("vcDomainStackingFailed", 706),
          ("vcDomainStackingNotRedundant", 707),
          ("vcDomainSomeProfilesAbnormal", 709),
          ("vcDomainUnknown", 712),
          ("vcDomainOverProvisioned", 713),
          ("vcDomainMixedTAA", 714),
          ("vcDomainInvalidPXEBootOrderProfileConnection", 715),
          ("vcDomainSflowIndirectlyDisabled", 801),
          ("vcDomainSflowFailed", 802),
          ("vcDomainSflowDegraded", 803),
          ("vcDomainPortMonitorIndirectlyDisabled", 901))
    )



class VcEnclosureReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(600,
              601,
              602,
              603,
              604,
              605,
              606,
              607)
        )
    )
    namedValues = NamedValues(
        *(("vcEnclosureOk", 600),
          ("vcEnclosureAllEnetModulesFailed", 601),
          ("vcEnclosureSomeEnetModulesAbnormal", 602),
          ("vcEnclosureSomeModulesOrServersIncompatible", 603),
          ("vcEnclosureSomeFcModulesAbnormal", 604),
          ("vcEnclosureSomeServersAbnormal", 605),
          ("vcEnclosureUnknown", 606),
          ("vcEnclosureMixedTAAModules", 607))
    )



class VcModuleReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(400,
              401,
              402,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              412,
              413,
              414)
        )
    )
    namedValues = NamedValues(
        *(("vcEnetmoduleOk", 400),
          ("vcEnetmoduleEnclosureDown", 401),
          ("vcEnetmoduleModuleMissing", 402),
          ("vcEnetmodulePortprotect", 404),
          ("vcEnetmoduleIncompatible", 405),
          ("vcEnetmoduleHwDegraded", 406),
          ("vcEnetmoduleUnknown", 407),
          ("vcFcmoduleOk", 408),
          ("vcFcmoduleEnclosureDown", 409),
          ("vcFcmoduleModuleMissing", 410),
          ("vcFcmoduleHwDegraded", 412),
          ("vcFcmoduleIncompatible", 413),
          ("vcFcmoduleUnknown", 414))
    )



class VcPortReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vcEnetPortOK", 1)
    )



class VcPhysicalServerReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(500,
              501,
              502,
              503,
              504)
        )
    )
    namedValues = NamedValues(
        *(("vcPhysicalServerOk", 500),
          ("vcPhysicalServerEnclosureDown", 501),
          ("vcPhysicalServerFailed", 502),
          ("vcPhysicalServerDegraded", 503),
          ("vcPhysicalServerUnknown", 504))
    )



class VcFcFabricReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("vcFabricOk", 200),
          ("vcFabricNoPortsConfigured", 202),
          ("vcFabricSomePortsAbnormal", 203),
          ("vcFabricAllPortsAbnormal", 204),
          ("vcFabricWwnMismatch", 205),
          ("vcFabricUnknown", 206))
    )



class VcEnetNetworkReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              104,
              105,
              106,
              109)
        )
    )
    namedValues = NamedValues(
        *(("vcNetworkOk", 100),
          ("vcNetworkUnknown", 101),
          ("vcNetworkDisabled", 102),
          ("vcNetworkAbnormal", 104),
          ("vcNetworkFailed", 105),
          ("vcNetworkDegraded", 106),
          ("vcNetworkNoPortsAssignedToPrivateNetwork", 109))
    )



class VcProfileReasonCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              301,
              304,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317)
        )
    )
    namedValues = NamedValues(
        *(("vcProfileOk", 300),
          ("vcProfileServerAbnormal", 301),
          ("vcProfileAllConnectionsFailed", 304),
          ("vcProfileSomeConnectionsUnmapped", 309),
          ("vcProfileAllConnectionsAbnormal", 310),
          ("vcProfileSomeConnectionsAbnormal", 311),
          ("vcProfileUEFIBootmodeIncompatibleWithServer", 312),
          ("vcProfileUnknown", 313),
          ("vcProfileConnectionInvalidPXEBootOrder", 314),
          ("vcProfileConnectionDuplicateIscsiInitiatorIP", 315),
          ("vcProfileConnectionDuplicateIscsiInitiatorName", 316),
          ("vcProfileConnectionDuplicateIscsiInitiatorNameIP", 317))
    )



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_HpSysMgt_ObjectIdentity = ObjectIdentity
hpSysMgt = _HpSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5)
)
_HpEmbeddedServerMgt_ObjectIdentity = ObjectIdentity
hpEmbeddedServerMgt = _HpEmbeddedServerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7)
)
_HpModuleMgmtProc_ObjectIdentity = ObjectIdentity
hpModuleMgmtProc = _HpModuleMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5)
)
_VirtualConnect_ObjectIdentity = ObjectIdentity
virtualConnect = _VirtualConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2)
)
_VcDomainMIBObjects_ObjectIdentity = ObjectIdentity
vcDomainMIBObjects = _VcDomainMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1)
)
_VcDomain_ObjectIdentity = ObjectIdentity
vcDomain = _VcDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1)
)
_VcDomainName_Type = SnmpAdminString
_VcDomainName_Object = MibScalar
vcDomainName = _VcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 1),
    _VcDomainName_Type()
)
vcDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainName.setStatus("current")
_VcDomainManagedStatus_Type = VcManagedStatus
_VcDomainManagedStatus_Object = MibScalar
vcDomainManagedStatus = _VcDomainManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 2),
    _VcDomainManagedStatus_Type()
)
vcDomainManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainManagedStatus.setStatus("current")
_VcDomainPrimaryAddressType_Type = TransportAddressType
_VcDomainPrimaryAddressType_Object = MibScalar
vcDomainPrimaryAddressType = _VcDomainPrimaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 3),
    _VcDomainPrimaryAddressType_Type()
)
vcDomainPrimaryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainPrimaryAddressType.setStatus("current")
_VcDomainPrimaryAddress_Type = TransportAddress
_VcDomainPrimaryAddress_Object = MibScalar
vcDomainPrimaryAddress = _VcDomainPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 4),
    _VcDomainPrimaryAddress_Type()
)
vcDomainPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainPrimaryAddress.setStatus("current")
_VcDomainCheckpointValid_Type = TruthValue
_VcDomainCheckpointValid_Object = MibScalar
vcDomainCheckpointValid = _VcDomainCheckpointValid_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 5),
    _VcDomainCheckpointValid_Type()
)
vcDomainCheckpointValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainCheckpointValid.setStatus("current")
_VcDomainLastCheckpointTime_Type = SnmpAdminString
_VcDomainLastCheckpointTime_Object = MibScalar
vcDomainLastCheckpointTime = _VcDomainLastCheckpointTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 6),
    _VcDomainLastCheckpointTime_Type()
)
vcDomainLastCheckpointTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainLastCheckpointTime.setStatus("current")
_VcDomainStackingLinkRedundant_Type = TruthValue
_VcDomainStackingLinkRedundant_Object = MibScalar
vcDomainStackingLinkRedundant = _VcDomainStackingLinkRedundant_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 7),
    _VcDomainStackingLinkRedundant_Type()
)
vcDomainStackingLinkRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainStackingLinkRedundant.setStatus("current")
_VcDomainRootCause_Type = SnmpAdminString
_VcDomainRootCause_Object = MibScalar
vcDomainRootCause = _VcDomainRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 8),
    _VcDomainRootCause_Type()
)
vcDomainRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainRootCause.setStatus("current")
_VcDomainCause_Type = SnmpAdminString
_VcDomainCause_Object = MibScalar
vcDomainCause = _VcDomainCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 9),
    _VcDomainCause_Type()
)
vcDomainCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainCause.setStatus("current")
_VcDomainReasonCode_Type = VcDomainReasonCodeType
_VcDomainReasonCode_Object = MibScalar
vcDomainReasonCode = _VcDomainReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 10),
    _VcDomainReasonCode_Type()
)
vcDomainReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainReasonCode.setStatus("current")
_VcDomainPrimaryAddressIpv6_Type = TransportAddress
_VcDomainPrimaryAddressIpv6_Object = MibScalar
vcDomainPrimaryAddressIpv6 = _VcDomainPrimaryAddressIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 1, 11),
    _VcDomainPrimaryAddressIpv6_Type()
)
vcDomainPrimaryAddressIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcDomainPrimaryAddressIpv6.setStatus("current")
_VcEnclosure_ObjectIdentity = ObjectIdentity
vcEnclosure = _VcEnclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2)
)
_VcEnclosureTable_Object = MibTable
vcEnclosureTable = _VcEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vcEnclosureTable.setStatus("current")
_VcEnclosureEntry_Object = MibTableRow
vcEnclosureEntry = _VcEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1)
)
vcEnclosureEntry.setIndexNames(
    (0, "HPVC-MIB", "vcEnclosureIndex"),
)
if mibBuilder.loadTexts:
    vcEnclosureEntry.setStatus("current")
_VcEnclosureIndex_Type = Integer32
_VcEnclosureIndex_Object = MibTableColumn
vcEnclosureIndex = _VcEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 1),
    _VcEnclosureIndex_Type()
)
vcEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureIndex.setStatus("current")
_VcEnclosureName_Type = SnmpAdminString
_VcEnclosureName_Object = MibTableColumn
vcEnclosureName = _VcEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 2),
    _VcEnclosureName_Type()
)
vcEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureName.setStatus("current")
_VcEnclosureManagedStatus_Type = VcManagedStatus
_VcEnclosureManagedStatus_Object = MibTableColumn
vcEnclosureManagedStatus = _VcEnclosureManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 3),
    _VcEnclosureManagedStatus_Type()
)
vcEnclosureManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureManagedStatus.setStatus("current")
_VcEnclosureAddressType_Type = TransportAddressType
_VcEnclosureAddressType_Object = MibTableColumn
vcEnclosureAddressType = _VcEnclosureAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 4),
    _VcEnclosureAddressType_Type()
)
vcEnclosureAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureAddressType.setStatus("current")
_VcEnclosureAddress_Type = TransportAddress
_VcEnclosureAddress_Object = MibTableColumn
vcEnclosureAddress = _VcEnclosureAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 5),
    _VcEnclosureAddress_Type()
)
vcEnclosureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureAddress.setStatus("current")
_VcEnclosureUUID_Type = SnmpAdminString
_VcEnclosureUUID_Object = MibTableColumn
vcEnclosureUUID = _VcEnclosureUUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 6),
    _VcEnclosureUUID_Type()
)
vcEnclosureUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureUUID.setStatus("current")
_VcEnclosureRootCause_Type = SnmpAdminString
_VcEnclosureRootCause_Object = MibTableColumn
vcEnclosureRootCause = _VcEnclosureRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 7),
    _VcEnclosureRootCause_Type()
)
vcEnclosureRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureRootCause.setStatus("current")
_VcEnclosureCause_Type = SnmpAdminString
_VcEnclosureCause_Object = MibTableColumn
vcEnclosureCause = _VcEnclosureCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 8),
    _VcEnclosureCause_Type()
)
vcEnclosureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureCause.setStatus("current")
_VcEnclosureReasonCode_Type = VcEnclosureReasonCodeType
_VcEnclosureReasonCode_Object = MibTableColumn
vcEnclosureReasonCode = _VcEnclosureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 9),
    _VcEnclosureReasonCode_Type()
)
vcEnclosureReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureReasonCode.setStatus("current")
_VcEnclosureAddressIpv6_Type = TransportAddress
_VcEnclosureAddressIpv6_Object = MibTableColumn
vcEnclosureAddressIpv6 = _VcEnclosureAddressIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 2, 1, 1, 10),
    _VcEnclosureAddressIpv6_Type()
)
vcEnclosureAddressIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnclosureAddressIpv6.setStatus("current")
_VcModule_ObjectIdentity = ObjectIdentity
vcModule = _VcModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3)
)
_VcModuleTable_Object = MibTable
vcModuleTable = _VcModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vcModuleTable.setStatus("current")
_VcModuleEntry_Object = MibTableRow
vcModuleEntry = _VcModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1)
)
vcModuleEntry.setIndexNames(
    (0, "HPVC-MIB", "vcModuleIndex"),
)
if mibBuilder.loadTexts:
    vcModuleEntry.setStatus("current")
_VcModuleIndex_Type = Integer32
_VcModuleIndex_Object = MibTableColumn
vcModuleIndex = _VcModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 1),
    _VcModuleIndex_Type()
)
vcModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleIndex.setStatus("current")
_VcModuleType_Type = VcModuleType
_VcModuleType_Object = MibTableColumn
vcModuleType = _VcModuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 2),
    _VcModuleType_Type()
)
vcModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleType.setStatus("current")
_VcModuleManagedStatus_Type = VcManagedStatus
_VcModuleManagedStatus_Object = MibTableColumn
vcModuleManagedStatus = _VcModuleManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 3),
    _VcModuleManagedStatus_Type()
)
vcModuleManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleManagedStatus.setStatus("current")
_VcModulePartNumber_Type = SnmpAdminString
_VcModulePartNumber_Object = MibTableColumn
vcModulePartNumber = _VcModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 4),
    _VcModulePartNumber_Type()
)
vcModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModulePartNumber.setStatus("current")
_VcModuleSerialNumber_Type = SnmpAdminString
_VcModuleSerialNumber_Object = MibTableColumn
vcModuleSerialNumber = _VcModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 5),
    _VcModuleSerialNumber_Type()
)
vcModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleSerialNumber.setStatus("current")
_VcModuleProductName_Type = SnmpAdminString
_VcModuleProductName_Object = MibTableColumn
vcModuleProductName = _VcModuleProductName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 6),
    _VcModuleProductName_Type()
)
vcModuleProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleProductName.setStatus("current")
_VcModuleFwRev_Type = SnmpAdminString
_VcModuleFwRev_Object = MibTableColumn
vcModuleFwRev = _VcModuleFwRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 7),
    _VcModuleFwRev_Type()
)
vcModuleFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleFwRev.setStatus("current")
_VcModuleEnclosurePointer_Type = RowPointer
_VcModuleEnclosurePointer_Object = MibTableColumn
vcModuleEnclosurePointer = _VcModuleEnclosurePointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 8),
    _VcModuleEnclosurePointer_Type()
)
vcModuleEnclosurePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleEnclosurePointer.setStatus("current")
_VcModuleLocation_Type = Unsigned32
_VcModuleLocation_Object = MibTableColumn
vcModuleLocation = _VcModuleLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 9),
    _VcModuleLocation_Type()
)
vcModuleLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleLocation.setStatus("current")
_VcModuleAddressType_Type = TransportAddressType
_VcModuleAddressType_Object = MibTableColumn
vcModuleAddressType = _VcModuleAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 10),
    _VcModuleAddressType_Type()
)
vcModuleAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleAddressType.setStatus("current")
_VcModuleAddress_Type = TransportAddress
_VcModuleAddress_Object = MibTableColumn
vcModuleAddress = _VcModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 11),
    _VcModuleAddress_Type()
)
vcModuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleAddress.setStatus("current")
_VcModuleID_Type = SnmpAdminString
_VcModuleID_Object = MibTableColumn
vcModuleID = _VcModuleID_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 12),
    _VcModuleID_Type()
)
vcModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleID.setStatus("current")
_VcModuleRootCause_Type = SnmpAdminString
_VcModuleRootCause_Object = MibTableColumn
vcModuleRootCause = _VcModuleRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 13),
    _VcModuleRootCause_Type()
)
vcModuleRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleRootCause.setStatus("current")
_VcModuleCause_Type = SnmpAdminString
_VcModuleCause_Object = MibTableColumn
vcModuleCause = _VcModuleCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 14),
    _VcModuleCause_Type()
)
vcModuleCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleCause.setStatus("current")
_VcModuleReasonCode_Type = VcModuleReasonCodeType
_VcModuleReasonCode_Object = MibTableColumn
vcModuleReasonCode = _VcModuleReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 15),
    _VcModuleReasonCode_Type()
)
vcModuleReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleReasonCode.setStatus("current")
_VcModuleAddressIpv6_Type = TransportAddress
_VcModuleAddressIpv6_Object = MibTableColumn
vcModuleAddressIpv6 = _VcModuleAddressIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 3, 1, 1, 16),
    _VcModuleAddressIpv6_Type()
)
vcModuleAddressIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleAddressIpv6.setStatus("current")
_VcPort_ObjectIdentity = ObjectIdentity
vcPort = _VcPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4)
)
_VcPortTable_Object = MibTable
vcPortTable = _VcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vcPortTable.setStatus("current")
_VcPortEntry_Object = MibTableRow
vcPortEntry = _VcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1)
)
vcPortEntry.setIndexNames(
    (0, "HPVC-MIB", "vcPortIndex"),
)
if mibBuilder.loadTexts:
    vcPortEntry.setStatus("current")
_VcPortIndex_Type = Integer32
_VcPortIndex_Object = MibTableColumn
vcPortIndex = _VcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 1),
    _VcPortIndex_Type()
)
vcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortIndex.setStatus("current")
_VcPortType_Type = VcPortType
_VcPortType_Object = MibTableColumn
vcPortType = _VcPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 2),
    _VcPortType_Type()
)
vcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortType.setStatus("current")
_VcPortManagedStatus_Type = VcManagedStatus
_VcPortManagedStatus_Object = MibTableColumn
vcPortManagedStatus = _VcPortManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 3),
    _VcPortManagedStatus_Type()
)
vcPortManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortManagedStatus.setStatus("current")
_VcPortManagerAddressType_Type = TransportAddressType
_VcPortManagerAddressType_Object = MibTableColumn
vcPortManagerAddressType = _VcPortManagerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 4),
    _VcPortManagerAddressType_Type()
)
vcPortManagerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortManagerAddressType.setStatus("current")
_VcPortManagerAddress_Type = TransportAddress
_VcPortManagerAddress_Object = MibTableColumn
vcPortManagerAddress = _VcPortManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 5),
    _VcPortManagerAddress_Type()
)
vcPortManagerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortManagerAddress.setStatus("current")
_VcPortPhysicalPortPointer_Type = RowPointer
_VcPortPhysicalPortPointer_Object = MibTableColumn
vcPortPhysicalPortPointer = _VcPortPhysicalPortPointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 6),
    _VcPortPhysicalPortPointer_Type()
)
vcPortPhysicalPortPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortPhysicalPortPointer.setStatus("current")
_VcPortContainerPointer_Type = RowPointer
_VcPortContainerPointer_Object = MibTableColumn
vcPortContainerPointer = _VcPortContainerPointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 4, 1, 1, 7),
    _VcPortContainerPointer_Type()
)
vcPortContainerPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPortContainerPointer.setStatus("current")
_VcPhysicalServer_ObjectIdentity = ObjectIdentity
vcPhysicalServer = _VcPhysicalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5)
)
_VcPhysicalServerTable_Object = MibTable
vcPhysicalServerTable = _VcPhysicalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    vcPhysicalServerTable.setStatus("current")
_VcPhysicalServerEntry_Object = MibTableRow
vcPhysicalServerEntry = _VcPhysicalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1)
)
vcPhysicalServerEntry.setIndexNames(
    (0, "HPVC-MIB", "vcPhysicalServerIndex"),
)
if mibBuilder.loadTexts:
    vcPhysicalServerEntry.setStatus("current")
_VcPhysicalServerIndex_Type = Integer32
_VcPhysicalServerIndex_Object = MibTableColumn
vcPhysicalServerIndex = _VcPhysicalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 1),
    _VcPhysicalServerIndex_Type()
)
vcPhysicalServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerIndex.setStatus("current")
_VcPhysicalServerEnclosureIndex_Type = Integer32
_VcPhysicalServerEnclosureIndex_Object = MibTableColumn
vcPhysicalServerEnclosureIndex = _VcPhysicalServerEnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 2),
    _VcPhysicalServerEnclosureIndex_Type()
)
vcPhysicalServerEnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerEnclosureIndex.setStatus("current")
_VcPhysicalServerManagedStatus_Type = VcManagedStatus
_VcPhysicalServerManagedStatus_Object = MibTableColumn
vcPhysicalServerManagedStatus = _VcPhysicalServerManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 3),
    _VcPhysicalServerManagedStatus_Type()
)
vcPhysicalServerManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerManagedStatus.setStatus("current")
_VcPhysicalServerPartNumber_Type = SnmpAdminString
_VcPhysicalServerPartNumber_Object = MibTableColumn
vcPhysicalServerPartNumber = _VcPhysicalServerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 4),
    _VcPhysicalServerPartNumber_Type()
)
vcPhysicalServerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerPartNumber.setStatus("current")
_VcPhysicalServerSerialNumber_Type = SnmpAdminString
_VcPhysicalServerSerialNumber_Object = MibTableColumn
vcPhysicalServerSerialNumber = _VcPhysicalServerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 5),
    _VcPhysicalServerSerialNumber_Type()
)
vcPhysicalServerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerSerialNumber.setStatus("current")
_VcPhysicalServerProductName_Type = SnmpAdminString
_VcPhysicalServerProductName_Object = MibTableColumn
vcPhysicalServerProductName = _VcPhysicalServerProductName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 6),
    _VcPhysicalServerProductName_Type()
)
vcPhysicalServerProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerProductName.setStatus("current")
_VcPhysicalServerLocation_Type = Unsigned32
_VcPhysicalServerLocation_Object = MibTableColumn
vcPhysicalServerLocation = _VcPhysicalServerLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 7),
    _VcPhysicalServerLocation_Type()
)
vcPhysicalServerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerLocation.setStatus("current")
_VcPhysicalServerRootCause_Type = SnmpAdminString
_VcPhysicalServerRootCause_Object = MibTableColumn
vcPhysicalServerRootCause = _VcPhysicalServerRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 8),
    _VcPhysicalServerRootCause_Type()
)
vcPhysicalServerRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerRootCause.setStatus("current")
_VcPhysicalServerCause_Type = SnmpAdminString
_VcPhysicalServerCause_Object = MibTableColumn
vcPhysicalServerCause = _VcPhysicalServerCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 9),
    _VcPhysicalServerCause_Type()
)
vcPhysicalServerCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerCause.setStatus("current")
_VcPhysicalServerReasonCode_Type = VcPhysicalServerReasonCodeType
_VcPhysicalServerReasonCode_Object = MibTableColumn
vcPhysicalServerReasonCode = _VcPhysicalServerReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 5, 1, 1, 10),
    _VcPhysicalServerReasonCode_Type()
)
vcPhysicalServerReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPhysicalServerReasonCode.setStatus("current")
_VcEnetNetwork_ObjectIdentity = ObjectIdentity
vcEnetNetwork = _VcEnetNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6)
)
_VcEnetNetworkTable_Object = MibTable
vcEnetNetworkTable = _VcEnetNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    vcEnetNetworkTable.setStatus("current")
_VcEnetNetworkEntry_Object = MibTableRow
vcEnetNetworkEntry = _VcEnetNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1)
)
vcEnetNetworkEntry.setIndexNames(
    (0, "HPVC-MIB", "vcEnetNetworkIndex"),
)
if mibBuilder.loadTexts:
    vcEnetNetworkEntry.setStatus("current")
_VcEnetNetworkIndex_Type = Integer32
_VcEnetNetworkIndex_Object = MibTableColumn
vcEnetNetworkIndex = _VcEnetNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 1),
    _VcEnetNetworkIndex_Type()
)
vcEnetNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkIndex.setStatus("current")
_VcEnetNetworkName_Type = SnmpAdminString
_VcEnetNetworkName_Object = MibTableColumn
vcEnetNetworkName = _VcEnetNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 2),
    _VcEnetNetworkName_Type()
)
vcEnetNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkName.setStatus("current")
_VcEnetNetworkManagedStatus_Type = VcManagedStatus
_VcEnetNetworkManagedStatus_Object = MibTableColumn
vcEnetNetworkManagedStatus = _VcEnetNetworkManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 3),
    _VcEnetNetworkManagedStatus_Type()
)
vcEnetNetworkManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkManagedStatus.setStatus("current")
_VcEnetNetworkUplinkVlanId_Type = Unsigned32
_VcEnetNetworkUplinkVlanId_Object = MibTableColumn
vcEnetNetworkUplinkVlanId = _VcEnetNetworkUplinkVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 4),
    _VcEnetNetworkUplinkVlanId_Type()
)
vcEnetNetworkUplinkVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkUplinkVlanId.setStatus("current")
_VcEnetNetworkRootCause_Type = SnmpAdminString
_VcEnetNetworkRootCause_Object = MibTableColumn
vcEnetNetworkRootCause = _VcEnetNetworkRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 5),
    _VcEnetNetworkRootCause_Type()
)
vcEnetNetworkRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkRootCause.setStatus("current")
_VcEnetNetworkCause_Type = SnmpAdminString
_VcEnetNetworkCause_Object = MibTableColumn
vcEnetNetworkCause = _VcEnetNetworkCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 6),
    _VcEnetNetworkCause_Type()
)
vcEnetNetworkCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkCause.setStatus("current")
_VcEnetNetworkReasonCode_Type = VcEnetNetworkReasonCodeType
_VcEnetNetworkReasonCode_Object = MibTableColumn
vcEnetNetworkReasonCode = _VcEnetNetworkReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 6, 1, 1, 7),
    _VcEnetNetworkReasonCode_Type()
)
vcEnetNetworkReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkReasonCode.setStatus("current")
_VcFcFabric_ObjectIdentity = ObjectIdentity
vcFcFabric = _VcFcFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7)
)
_VcFcFabricTable_Object = MibTable
vcFcFabricTable = _VcFcFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    vcFcFabricTable.setStatus("current")
_VcFcFabricEntry_Object = MibTableRow
vcFcFabricEntry = _VcFcFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1)
)
vcFcFabricEntry.setIndexNames(
    (0, "HPVC-MIB", "vcFcFabricIndex"),
)
if mibBuilder.loadTexts:
    vcFcFabricEntry.setStatus("current")
_VcFcFabricIndex_Type = Integer32
_VcFcFabricIndex_Object = MibTableColumn
vcFcFabricIndex = _VcFcFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1, 1),
    _VcFcFabricIndex_Type()
)
vcFcFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricIndex.setStatus("current")
_VcFcFabricName_Type = SnmpAdminString
_VcFcFabricName_Object = MibTableColumn
vcFcFabricName = _VcFcFabricName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1, 2),
    _VcFcFabricName_Type()
)
vcFcFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricName.setStatus("current")
_VcFcFabricManagedStatus_Type = VcManagedStatus
_VcFcFabricManagedStatus_Object = MibTableColumn
vcFcFabricManagedStatus = _VcFcFabricManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1, 3),
    _VcFcFabricManagedStatus_Type()
)
vcFcFabricManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricManagedStatus.setStatus("current")
_VcFcFabricRootCause_Type = SnmpAdminString
_VcFcFabricRootCause_Object = MibTableColumn
vcFcFabricRootCause = _VcFcFabricRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1, 4),
    _VcFcFabricRootCause_Type()
)
vcFcFabricRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricRootCause.setStatus("current")
_VcFcFabricCause_Type = SnmpAdminString
_VcFcFabricCause_Object = MibTableColumn
vcFcFabricCause = _VcFcFabricCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1, 5),
    _VcFcFabricCause_Type()
)
vcFcFabricCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricCause.setStatus("current")
_VcFcFabricReasonCode_Type = VcFcFabricReasonCodeType
_VcFcFabricReasonCode_Object = MibTableColumn
vcFcFabricReasonCode = _VcFcFabricReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 7, 1, 1, 6),
    _VcFcFabricReasonCode_Type()
)
vcFcFabricReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricReasonCode.setStatus("current")
_VcProfile_ObjectIdentity = ObjectIdentity
vcProfile = _VcProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8)
)
_VcProfileTable_Object = MibTable
vcProfileTable = _VcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    vcProfileTable.setStatus("current")
_VcProfileEntry_Object = MibTableRow
vcProfileEntry = _VcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1)
)
vcProfileEntry.setIndexNames(
    (0, "HPVC-MIB", "vcProfileIndex"),
)
if mibBuilder.loadTexts:
    vcProfileEntry.setStatus("current")
_VcProfileIndex_Type = Integer32
_VcProfileIndex_Object = MibTableColumn
vcProfileIndex = _VcProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 1),
    _VcProfileIndex_Type()
)
vcProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileIndex.setStatus("current")
_VcProfileName_Type = SnmpAdminString
_VcProfileName_Object = MibTableColumn
vcProfileName = _VcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 2),
    _VcProfileName_Type()
)
vcProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileName.setStatus("current")
_VcProfileManagedStatus_Type = VcManagedStatus
_VcProfileManagedStatus_Object = MibTableColumn
vcProfileManagedStatus = _VcProfileManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 3),
    _VcProfileManagedStatus_Type()
)
vcProfileManagedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileManagedStatus.setStatus("current")
_VcProfilePhysicalServerIndex_Type = Unsigned32
_VcProfilePhysicalServerIndex_Object = MibTableColumn
vcProfilePhysicalServerIndex = _VcProfilePhysicalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 4),
    _VcProfilePhysicalServerIndex_Type()
)
vcProfilePhysicalServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfilePhysicalServerIndex.setStatus("current")
_VcProfileLogicalSerialNumber_Type = SnmpAdminString
_VcProfileLogicalSerialNumber_Object = MibTableColumn
vcProfileLogicalSerialNumber = _VcProfileLogicalSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 5),
    _VcProfileLogicalSerialNumber_Type()
)
vcProfileLogicalSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileLogicalSerialNumber.setStatus("current")
_VcProfileRootCause_Type = SnmpAdminString
_VcProfileRootCause_Object = MibTableColumn
vcProfileRootCause = _VcProfileRootCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 6),
    _VcProfileRootCause_Type()
)
vcProfileRootCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileRootCause.setStatus("current")
_VcProfileCause_Type = SnmpAdminString
_VcProfileCause_Object = MibTableColumn
vcProfileCause = _VcProfileCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 7),
    _VcProfileCause_Type()
)
vcProfileCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileCause.setStatus("current")
_VcProfileReasonCode_Type = VcProfileReasonCodeType
_VcProfileReasonCode_Object = MibTableColumn
vcProfileReasonCode = _VcProfileReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 8, 1, 1, 8),
    _VcProfileReasonCode_Type()
)
vcProfileReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileReasonCode.setStatus("current")
_VcEnetNetworkVcPortMap_ObjectIdentity = ObjectIdentity
vcEnetNetworkVcPortMap = _VcEnetNetworkVcPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 9)
)
_VcEnetNetworkVcPortMapTable_Object = MibTable
vcEnetNetworkVcPortMapTable = _VcEnetNetworkVcPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    vcEnetNetworkVcPortMapTable.setStatus("current")
_VcEnetNetworkVcPortMapEntry_Object = MibTableRow
vcEnetNetworkVcPortMapEntry = _VcEnetNetworkVcPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 9, 1, 1)
)
vcEnetNetworkVcPortMapEntry.setIndexNames(
    (0, "HPVC-MIB", "vcEnetNetworkVcPortMapNetworkIndex"),
    (0, "HPVC-MIB", "vcEnetNetworkVcPortMapVcPortIndex"),
)
if mibBuilder.loadTexts:
    vcEnetNetworkVcPortMapEntry.setStatus("current")
_VcEnetNetworkVcPortMapNetworkIndex_Type = Integer32
_VcEnetNetworkVcPortMapNetworkIndex_Object = MibTableColumn
vcEnetNetworkVcPortMapNetworkIndex = _VcEnetNetworkVcPortMapNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 9, 1, 1, 1),
    _VcEnetNetworkVcPortMapNetworkIndex_Type()
)
vcEnetNetworkVcPortMapNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkVcPortMapNetworkIndex.setStatus("current")
_VcEnetNetworkVcPortMapVcPortIndex_Type = Integer32
_VcEnetNetworkVcPortMapVcPortIndex_Object = MibTableColumn
vcEnetNetworkVcPortMapVcPortIndex = _VcEnetNetworkVcPortMapVcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 9, 1, 1, 2),
    _VcEnetNetworkVcPortMapVcPortIndex_Type()
)
vcEnetNetworkVcPortMapVcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcEnetNetworkVcPortMapVcPortIndex.setStatus("current")
_VcFcFabricVcPortMap_ObjectIdentity = ObjectIdentity
vcFcFabricVcPortMap = _VcFcFabricVcPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 10)
)
_VcFcFabricVcPortMapTable_Object = MibTable
vcFcFabricVcPortMapTable = _VcFcFabricVcPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    vcFcFabricVcPortMapTable.setStatus("current")
_VcFcFabricVcPortMapEntry_Object = MibTableRow
vcFcFabricVcPortMapEntry = _VcFcFabricVcPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 10, 1, 1)
)
vcFcFabricVcPortMapEntry.setIndexNames(
    (0, "HPVC-MIB", "vcFcFabricVcPortMapFcFabricIndex"),
    (0, "HPVC-MIB", "vcFcFabricVcPortMapVcPortIndex"),
)
if mibBuilder.loadTexts:
    vcFcFabricVcPortMapEntry.setStatus("current")
_VcFcFabricVcPortMapFcFabricIndex_Type = Integer32
_VcFcFabricVcPortMapFcFabricIndex_Object = MibTableColumn
vcFcFabricVcPortMapFcFabricIndex = _VcFcFabricVcPortMapFcFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 10, 1, 1, 1),
    _VcFcFabricVcPortMapFcFabricIndex_Type()
)
vcFcFabricVcPortMapFcFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricVcPortMapFcFabricIndex.setStatus("current")
_VcFcFabricVcPortMapVcPortIndex_Type = Integer32
_VcFcFabricVcPortMapVcPortIndex_Object = MibTableColumn
vcFcFabricVcPortMapVcPortIndex = _VcFcFabricVcPortMapVcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 10, 1, 1, 2),
    _VcFcFabricVcPortMapVcPortIndex_Type()
)
vcFcFabricVcPortMapVcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcFcFabricVcPortMapVcPortIndex.setStatus("current")
_VcProfileNetworkMap_ObjectIdentity = ObjectIdentity
vcProfileNetworkMap = _VcProfileNetworkMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 11)
)
_VcProfileNetworkMapTable_Object = MibTable
vcProfileNetworkMapTable = _VcProfileNetworkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    vcProfileNetworkMapTable.setStatus("current")
_VcProfileNetworkMapEntry_Object = MibTableRow
vcProfileNetworkMapEntry = _VcProfileNetworkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 11, 1, 1)
)
vcProfileNetworkMapEntry.setIndexNames(
    (0, "HPVC-MIB", "vcProfileNetworkMapProfileIndex"),
    (0, "HPVC-MIB", "vcProfileNetworkMapConnectionIndex"),
)
if mibBuilder.loadTexts:
    vcProfileNetworkMapEntry.setStatus("current")
_VcProfileNetworkMapProfileIndex_Type = Integer32
_VcProfileNetworkMapProfileIndex_Object = MibTableColumn
vcProfileNetworkMapProfileIndex = _VcProfileNetworkMapProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 11, 1, 1, 1),
    _VcProfileNetworkMapProfileIndex_Type()
)
vcProfileNetworkMapProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileNetworkMapProfileIndex.setStatus("current")
_VcProfileNetworkMapConnectionIndex_Type = Integer32
_VcProfileNetworkMapConnectionIndex_Object = MibTableColumn
vcProfileNetworkMapConnectionIndex = _VcProfileNetworkMapConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 11, 1, 1, 2),
    _VcProfileNetworkMapConnectionIndex_Type()
)
vcProfileNetworkMapConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileNetworkMapConnectionIndex.setStatus("current")
_VcProfileNetworkMapNetworkIndex_Type = Integer32
_VcProfileNetworkMapNetworkIndex_Object = MibTableColumn
vcProfileNetworkMapNetworkIndex = _VcProfileNetworkMapNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 11, 1, 1, 3),
    _VcProfileNetworkMapNetworkIndex_Type()
)
vcProfileNetworkMapNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileNetworkMapNetworkIndex.setStatus("current")
_VcProfileFcFabricMap_ObjectIdentity = ObjectIdentity
vcProfileFcFabricMap = _VcProfileFcFabricMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 12)
)
_VcProfileFcFabricMapTable_Object = MibTable
vcProfileFcFabricMapTable = _VcProfileFcFabricMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vcProfileFcFabricMapTable.setStatus("current")
_VcProfileFcFabricMapEntry_Object = MibTableRow
vcProfileFcFabricMapEntry = _VcProfileFcFabricMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 12, 1, 1)
)
vcProfileFcFabricMapEntry.setIndexNames(
    (0, "HPVC-MIB", "vcProfileFcFabricMapProfileIndex"),
    (0, "HPVC-MIB", "vcProfileFcFabricMapConnectionIndex"),
)
if mibBuilder.loadTexts:
    vcProfileFcFabricMapEntry.setStatus("current")
_VcProfileFcFabricMapProfileIndex_Type = Integer32
_VcProfileFcFabricMapProfileIndex_Object = MibTableColumn
vcProfileFcFabricMapProfileIndex = _VcProfileFcFabricMapProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 12, 1, 1, 1),
    _VcProfileFcFabricMapProfileIndex_Type()
)
vcProfileFcFabricMapProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileFcFabricMapProfileIndex.setStatus("current")
_VcProfileFcFabricMapConnectionIndex_Type = Integer32
_VcProfileFcFabricMapConnectionIndex_Object = MibTableColumn
vcProfileFcFabricMapConnectionIndex = _VcProfileFcFabricMapConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 12, 1, 1, 2),
    _VcProfileFcFabricMapConnectionIndex_Type()
)
vcProfileFcFabricMapConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileFcFabricMapConnectionIndex.setStatus("current")
_VcProfileFcFabricMapFcFabricIndex_Type = Integer32
_VcProfileFcFabricMapFcFabricIndex_Object = MibTableColumn
vcProfileFcFabricMapFcFabricIndex = _VcProfileFcFabricMapFcFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 1, 12, 1, 1, 3),
    _VcProfileFcFabricMapFcFabricIndex_Type()
)
vcProfileFcFabricMapFcFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcProfileFcFabricMapFcFabricIndex.setStatus("current")
_VcDomainMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
vcDomainMIBNotificationPrefix = _VcDomainMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2)
)
_VcDomainMIBNotifications_ObjectIdentity = ObjectIdentity
vcDomainMIBNotifications = _VcDomainMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0)
)
_VcDomainMIBNotificationObjects_ObjectIdentity = ObjectIdentity
vcDomainMIBNotificationObjects = _VcDomainMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 1)
)
_VcDomainMIBConformance_ObjectIdentity = ObjectIdentity
vcDomainMIBConformance = _VcDomainMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3)
)
_VcDomainMIBCompliances_ObjectIdentity = ObjectIdentity
vcDomainMIBCompliances = _VcDomainMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 1)
)
_VcDomainMIBGroups_ObjectIdentity = ObjectIdentity
vcDomainMIBGroups = _VcDomainMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2)
)

# Managed Objects groups

vcDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 1)
)
vcDomainGroup.setObjects(
      *(("HPVC-MIB", "vcDomainName"),
        ("HPVC-MIB", "vcDomainManagedStatus"),
        ("HPVC-MIB", "vcDomainPrimaryAddressType"),
        ("HPVC-MIB", "vcDomainPrimaryAddress"),
        ("HPVC-MIB", "vcDomainCheckpointValid"),
        ("HPVC-MIB", "vcDomainLastCheckpointTime"),
        ("HPVC-MIB", "vcDomainStackingLinkRedundant"),
        ("HPVC-MIB", "vcDomainRootCause"),
        ("HPVC-MIB", "vcDomainCause"),
        ("HPVC-MIB", "vcDomainReasonCode"),
        ("HPVC-MIB", "vcDomainPrimaryAddressIpv6"))
)
if mibBuilder.loadTexts:
    vcDomainGroup.setStatus("current")

vcEnclosureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 2)
)
vcEnclosureGroup.setObjects(
      *(("HPVC-MIB", "vcEnclosureIndex"),
        ("HPVC-MIB", "vcEnclosureName"),
        ("HPVC-MIB", "vcEnclosureManagedStatus"),
        ("HPVC-MIB", "vcEnclosureAddressType"),
        ("HPVC-MIB", "vcEnclosureAddress"),
        ("HPVC-MIB", "vcEnclosureUUID"),
        ("HPVC-MIB", "vcEnclosureRootCause"),
        ("HPVC-MIB", "vcEnclosureCause"),
        ("HPVC-MIB", "vcEnclosureReasonCode"),
        ("HPVC-MIB", "vcEnclosureAddressIpv6"))
)
if mibBuilder.loadTexts:
    vcEnclosureGroup.setStatus("current")

vcModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 3)
)
vcModuleGroup.setObjects(
      *(("HPVC-MIB", "vcModuleIndex"),
        ("HPVC-MIB", "vcModuleType"),
        ("HPVC-MIB", "vcModuleManagedStatus"),
        ("HPVC-MIB", "vcModulePartNumber"),
        ("HPVC-MIB", "vcModuleFwRev"),
        ("HPVC-MIB", "vcModuleEnclosurePointer"),
        ("HPVC-MIB", "vcModuleLocation"),
        ("HPVC-MIB", "vcModuleAddressType"),
        ("HPVC-MIB", "vcModuleAddress"),
        ("HPVC-MIB", "vcModuleID"),
        ("HPVC-MIB", "vcModuleRootCause"),
        ("HPVC-MIB", "vcModuleCause"),
        ("HPVC-MIB", "vcModuleReasonCode"),
        ("HPVC-MIB", "vcModuleAddressIpv6"))
)
if mibBuilder.loadTexts:
    vcModuleGroup.setStatus("current")

vcPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 4)
)
vcPortGroup.setObjects(
      *(("HPVC-MIB", "vcPortIndex"),
        ("HPVC-MIB", "vcPortType"),
        ("HPVC-MIB", "vcPortManagedStatus"),
        ("HPVC-MIB", "vcPortManagerAddressType"),
        ("HPVC-MIB", "vcPortManagerAddress"),
        ("HPVC-MIB", "vcPortContainerPointer"),
        ("HPVC-MIB", "vcPortPhysicalPortPointer"))
)
if mibBuilder.loadTexts:
    vcPortGroup.setStatus("current")

vcPhysicalServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 5)
)
vcPhysicalServerGroup.setObjects(
      *(("HPVC-MIB", "vcPhysicalServerIndex"),
        ("HPVC-MIB", "vcPhysicalServerEnclosureIndex"),
        ("HPVC-MIB", "vcPhysicalServerManagedStatus"),
        ("HPVC-MIB", "vcPhysicalServerLocation"),
        ("HPVC-MIB", "vcPhysicalServerRootCause"),
        ("HPVC-MIB", "vcPhysicalServerCause"),
        ("HPVC-MIB", "vcPhysicalServerReasonCode"))
)
if mibBuilder.loadTexts:
    vcPhysicalServerGroup.setStatus("current")

vcFcFabricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 6)
)
vcFcFabricGroup.setObjects(
      *(("HPVC-MIB", "vcFcFabricIndex"),
        ("HPVC-MIB", "vcFcFabricName"),
        ("HPVC-MIB", "vcFcFabricManagedStatus"),
        ("HPVC-MIB", "vcFcFabricRootCause"),
        ("HPVC-MIB", "vcFcFabricCause"),
        ("HPVC-MIB", "vcFcFabricReasonCode"))
)
if mibBuilder.loadTexts:
    vcFcFabricGroup.setStatus("current")

vcEnetNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 7)
)
vcEnetNetworkGroup.setObjects(
      *(("HPVC-MIB", "vcEnetNetworkIndex"),
        ("HPVC-MIB", "vcEnetNetworkName"),
        ("HPVC-MIB", "vcEnetNetworkManagedStatus"),
        ("HPVC-MIB", "vcEnetNetworkUplinkVlanId"),
        ("HPVC-MIB", "vcEnetNetworkRootCause"),
        ("HPVC-MIB", "vcEnetNetworkCause"),
        ("HPVC-MIB", "vcEnetNetworkReasonCode"))
)
if mibBuilder.loadTexts:
    vcEnetNetworkGroup.setStatus("current")

vcProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 8)
)
vcProfileGroup.setObjects(
      *(("HPVC-MIB", "vcProfileIndex"),
        ("HPVC-MIB", "vcProfileName"),
        ("HPVC-MIB", "vcProfileManagedStatus"),
        ("HPVC-MIB", "vcProfilePhysicalServerIndex"),
        ("HPVC-MIB", "vcProfileLogicalSerialNumber"),
        ("HPVC-MIB", "vcProfileRootCause"),
        ("HPVC-MIB", "vcProfileCause"),
        ("HPVC-MIB", "vcProfileReasonCode"))
)
if mibBuilder.loadTexts:
    vcProfileGroup.setStatus("current")

vcEnetNetworkVcPortMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 9)
)
vcEnetNetworkVcPortMapGroup.setObjects(
      *(("HPVC-MIB", "vcEnetNetworkVcPortMapNetworkIndex"),
        ("HPVC-MIB", "vcEnetNetworkVcPortMapVcPortIndex"))
)
if mibBuilder.loadTexts:
    vcEnetNetworkVcPortMapGroup.setStatus("current")

vcFcFabricVcPortMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 10)
)
vcFcFabricVcPortMapGroup.setObjects(
      *(("HPVC-MIB", "vcFcFabricVcPortMapFcFabricIndex"),
        ("HPVC-MIB", "vcFcFabricVcPortMapVcPortIndex"))
)
if mibBuilder.loadTexts:
    vcFcFabricVcPortMapGroup.setStatus("current")

vcProfileNetworkMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 11)
)
vcProfileNetworkMapGroup.setObjects(
      *(("HPVC-MIB", "vcProfileNetworkMapProfileIndex"),
        ("HPVC-MIB", "vcProfileNetworkMapNetworkIndex"))
)
if mibBuilder.loadTexts:
    vcProfileNetworkMapGroup.setStatus("current")

vcProfileFcFabricMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 12)
)
vcProfileFcFabricMapGroup.setObjects(
      *(("HPVC-MIB", "vcProfileFcFabricMapProfileIndex"),
        ("HPVC-MIB", "vcProfileFcFabricMapFcFabricIndex"))
)
if mibBuilder.loadTexts:
    vcProfileFcFabricMapGroup.setStatus("current")


# Notification objects

vcDomainManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 1)
)
vcDomainManagedStatusChange.setObjects(
    ("HPVC-MIB", "vcDomainManagedStatus")
)
if mibBuilder.loadTexts:
    vcDomainManagedStatusChange.setStatus(
        "deprecated"
    )

vcCheckpointTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 2)
)
vcCheckpointTimeout.setObjects(
      *(("HPVC-MIB", "vcDomainCheckpointValid"),
        ("HPVC-MIB", "vcDomainLastCheckpointTime"))
)
if mibBuilder.loadTexts:
    vcCheckpointTimeout.setStatus(
        "current"
    )

vcCheckpointCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 3)
)
vcCheckpointCompleted.setObjects(
    ("HPVC-MIB", "vcDomainCheckpointValid")
)
if mibBuilder.loadTexts:
    vcCheckpointCompleted.setStatus(
        "current"
    )

vcEnetNetworkManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 4)
)
vcEnetNetworkManagedStatusChange.setObjects(
      *(("HPVC-MIB", "vcEnetNetworkManagedStatus"),
        ("HPVC-MIB", "vcEnetNetworkIndex"))
)
if mibBuilder.loadTexts:
    vcEnetNetworkManagedStatusChange.setStatus(
        "deprecated"
    )

vcFcFabricManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 5)
)
vcFcFabricManagedStatusChange.setObjects(
      *(("HPVC-MIB", "vcFcFabricManagedStatus"),
        ("HPVC-MIB", "vcFcFabricIndex"))
)
if mibBuilder.loadTexts:
    vcFcFabricManagedStatusChange.setStatus(
        "deprecated"
    )

vcModuleManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 6)
)
vcModuleManagedStatusChange.setObjects(
      *(("HPVC-MIB", "vcModuleManagedStatus"),
        ("HPVC-MIB", "vcModuleIndex"))
)
if mibBuilder.loadTexts:
    vcModuleManagedStatusChange.setStatus(
        "deprecated"
    )

vcEnclosureManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 7)
)
vcEnclosureManagedStatusChange.setObjects(
      *(("HPVC-MIB", "vcEnclosureManagedStatus"),
        ("HPVC-MIB", "vcEnclosureIndex"))
)
if mibBuilder.loadTexts:
    vcEnclosureManagedStatusChange.setStatus(
        "deprecated"
    )

vcPhysicalServerManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 8)
)
vcPhysicalServerManagedStatusChange.setObjects(
      *(("HPVC-MIB", "vcPhysicalServerManagedStatus"),
        ("HPVC-MIB", "vcPhysicalServerIndex"))
)
if mibBuilder.loadTexts:
    vcPhysicalServerManagedStatusChange.setStatus(
        "deprecated"
    )

vcProfileManagedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 9)
)
vcProfileManagedStatusChange.setObjects(
      *(("HPVC-MIB", "vcProfileManagedStatus"),
        ("HPVC-MIB", "vcProfileIndex"))
)
if mibBuilder.loadTexts:
    vcProfileManagedStatusChange.setStatus(
        "deprecated"
    )

vcTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 10)
)
vcTestTrap.setObjects(
    ("HPVC-MIB", "vcDomainName")
)
if mibBuilder.loadTexts:
    vcTestTrap.setStatus(
        "current"
    )

vcDomainStackingLinkRendundancyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 11)
)
vcDomainStackingLinkRendundancyStatusChange.setObjects(
    ("HPVC-MIB", "vcDomainStackingLinkRedundant")
)
if mibBuilder.loadTexts:
    vcDomainStackingLinkRendundancyStatusChange.setStatus(
        "current"
    )

vcDomainManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 12)
)
vcDomainManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcDomainManagedStatus"),
        ("HPVC-MIB", "vcDomainRootCause"),
        ("HPVC-MIB", "vcDomainCause"),
        ("HPVC-MIB", "vcDomainReasonCode"))
)
if mibBuilder.loadTexts:
    vcDomainManagedStatusChanged.setStatus(
        "current"
    )

vcEnclosureManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 13)
)
vcEnclosureManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcEnclosureIndex"),
        ("HPVC-MIB", "vcEnclosureName"),
        ("HPVC-MIB", "vcEnclosureManagedStatus"),
        ("HPVC-MIB", "vcEnclosureRootCause"),
        ("HPVC-MIB", "vcEnclosureCause"),
        ("HPVC-MIB", "vcEnclosureReasonCode"))
)
if mibBuilder.loadTexts:
    vcEnclosureManagedStatusChanged.setStatus(
        "current"
    )

vcModuleManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 14)
)
vcModuleManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcModuleIndex"),
        ("HPVC-MIB", "vcModuleManagedStatus"),
        ("HPVC-MIB", "vcModuleRootCause"),
        ("HPVC-MIB", "vcModuleCause"),
        ("HPVC-MIB", "vcModuleReasonCode"))
)
if mibBuilder.loadTexts:
    vcModuleManagedStatusChanged.setStatus(
        "current"
    )

vcPhysicalServerManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 16)
)
vcPhysicalServerManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcPhysicalServerIndex"),
        ("HPVC-MIB", "vcPhysicalServerManagedStatus"),
        ("HPVC-MIB", "vcPhysicalServerRootCause"),
        ("HPVC-MIB", "vcPhysicalServerCause"),
        ("HPVC-MIB", "vcPhysicalServerReasonCode"))
)
if mibBuilder.loadTexts:
    vcPhysicalServerManagedStatusChanged.setStatus(
        "current"
    )

vcFcFabricManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 17)
)
vcFcFabricManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcFcFabricIndex"),
        ("HPVC-MIB", "vcFcFabricName"),
        ("HPVC-MIB", "vcFcFabricManagedStatus"),
        ("HPVC-MIB", "vcFcFabricRootCause"),
        ("HPVC-MIB", "vcFcFabricCause"),
        ("HPVC-MIB", "vcFcFabricReasonCode"))
)
if mibBuilder.loadTexts:
    vcFcFabricManagedStatusChanged.setStatus(
        "current"
    )

vcEnetNetworkManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 18)
)
vcEnetNetworkManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcEnetNetworkIndex"),
        ("HPVC-MIB", "vcEnetNetworkName"),
        ("HPVC-MIB", "vcEnetNetworkManagedStatus"),
        ("HPVC-MIB", "vcEnetNetworkRootCause"),
        ("HPVC-MIB", "vcEnetNetworkCause"),
        ("HPVC-MIB", "vcEnetNetworkReasonCode"))
)
if mibBuilder.loadTexts:
    vcEnetNetworkManagedStatusChanged.setStatus(
        "current"
    )

vcProfileManagedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 2, 0, 19)
)
vcProfileManagedStatusChanged.setObjects(
      *(("HPVC-MIB", "vcProfileIndex"),
        ("HPVC-MIB", "vcProfileName"),
        ("HPVC-MIB", "vcProfileManagedStatus"),
        ("HPVC-MIB", "vcProfileRootCause"),
        ("HPVC-MIB", "vcProfileCause"),
        ("HPVC-MIB", "vcProfileReasonCode"))
)
if mibBuilder.loadTexts:
    vcProfileManagedStatusChanged.setStatus(
        "current"
    )


# Notifications groups

vcManagedStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 13)
)
vcManagedStatusNotificationsGroup.setObjects(
      *(("HPVC-MIB", "vcDomainManagedStatusChange"),
        ("HPVC-MIB", "vcCheckpointTimeout"),
        ("HPVC-MIB", "vcCheckpointCompleted"),
        ("HPVC-MIB", "vcEnetNetworkManagedStatusChange"),
        ("HPVC-MIB", "vcFcFabricManagedStatusChange"),
        ("HPVC-MIB", "vcModuleManagedStatusChange"),
        ("HPVC-MIB", "vcEnclosureManagedStatusChange"),
        ("HPVC-MIB", "vcPhysicalServerManagedStatusChange"),
        ("HPVC-MIB", "vcProfileManagedStatusChange"),
        ("HPVC-MIB", "vcTestTrap"),
        ("HPVC-MIB", "vcDomainStackingLinkRendundancyStatusChange"))
)
if mibBuilder.loadTexts:
    vcManagedStatusNotificationsGroup.setStatus(
        "deprecated"
    )

vcManagedStatusNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 2, 14)
)
vcManagedStatusNotificationsGroup2.setObjects(
      *(("HPVC-MIB", "vcDomainManagedStatusChanged"),
        ("HPVC-MIB", "vcCheckpointTimeout"),
        ("HPVC-MIB", "vcCheckpointCompleted"),
        ("HPVC-MIB", "vcEnetNetworkManagedStatusChanged"),
        ("HPVC-MIB", "vcFcFabricManagedStatusChanged"),
        ("HPVC-MIB", "vcModuleManagedStatusChanged"),
        ("HPVC-MIB", "vcEnclosureManagedStatusChanged"),
        ("HPVC-MIB", "vcPhysicalServerManagedStatusChanged"),
        ("HPVC-MIB", "vcProfileManagedStatusChanged"),
        ("HPVC-MIB", "vcTestTrap"),
        ("HPVC-MIB", "vcDomainStackingLinkRendundancyStatusChange"))
)
if mibBuilder.loadTexts:
    vcManagedStatusNotificationsGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vcDomainMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 1, 3, 1, 1)
)
vcDomainMIBCompliance.setObjects(
      *(("HPVC-MIB", "vcDomainGroup"),
        ("HPVC-MIB", "vcEnclosureGroup"),
        ("HPVC-MIB", "vcModuleGroup"),
        ("HPVC-MIB", "vcPortGroup"),
        ("HPVC-MIB", "vcPhysicalServerGroup"),
        ("HPVC-MIB", "vcFcFabricGroup"),
        ("HPVC-MIB", "vcEnetNetworkGroup"),
        ("HPVC-MIB", "vcProfileGroup"),
        ("HPVC-MIB", "vcEnetNetworkVcPortMapGroup"),
        ("HPVC-MIB", "vcFcFabricVcPortMapGroup"),
        ("HPVC-MIB", "vcProfileNetworkMapGroup"),
        ("HPVC-MIB", "vcProfileFcFabricMapGroup"),
        ("HPVC-MIB", "vcManagedStatusNotificationsGroup"),
        ("HPVC-MIB", "vcManagedStatusNotificationsGroup2"))
)
if mibBuilder.loadTexts:
    vcDomainMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPVC-MIB",
    **{"VcManagedStatus": VcManagedStatus,
       "VcDomainModuleRole": VcDomainModuleRole,
       "VcModuleType": VcModuleType,
       "VcPortType": VcPortType,
       "VcDomainReasonCodeType": VcDomainReasonCodeType,
       "VcEnclosureReasonCodeType": VcEnclosureReasonCodeType,
       "VcModuleReasonCodeType": VcModuleReasonCodeType,
       "VcPortReasonCodeType": VcPortReasonCodeType,
       "VcPhysicalServerReasonCodeType": VcPhysicalServerReasonCodeType,
       "VcFcFabricReasonCodeType": VcFcFabricReasonCodeType,
       "VcEnetNetworkReasonCodeType": VcEnetNetworkReasonCodeType,
       "VcProfileReasonCodeType": VcProfileReasonCodeType,
       "hp": hp,
       "hpSysMgt": hpSysMgt,
       "hpEmbeddedServerMgt": hpEmbeddedServerMgt,
       "hpModuleMgmtProc": hpModuleMgmtProc,
       "virtualConnect": virtualConnect,
       "vcDomainMIB": vcDomainMIB,
       "vcDomainMIBObjects": vcDomainMIBObjects,
       "vcDomain": vcDomain,
       "vcDomainName": vcDomainName,
       "vcDomainManagedStatus": vcDomainManagedStatus,
       "vcDomainPrimaryAddressType": vcDomainPrimaryAddressType,
       "vcDomainPrimaryAddress": vcDomainPrimaryAddress,
       "vcDomainCheckpointValid": vcDomainCheckpointValid,
       "vcDomainLastCheckpointTime": vcDomainLastCheckpointTime,
       "vcDomainStackingLinkRedundant": vcDomainStackingLinkRedundant,
       "vcDomainRootCause": vcDomainRootCause,
       "vcDomainCause": vcDomainCause,
       "vcDomainReasonCode": vcDomainReasonCode,
       "vcDomainPrimaryAddressIpv6": vcDomainPrimaryAddressIpv6,
       "vcEnclosure": vcEnclosure,
       "vcEnclosureTable": vcEnclosureTable,
       "vcEnclosureEntry": vcEnclosureEntry,
       "vcEnclosureIndex": vcEnclosureIndex,
       "vcEnclosureName": vcEnclosureName,
       "vcEnclosureManagedStatus": vcEnclosureManagedStatus,
       "vcEnclosureAddressType": vcEnclosureAddressType,
       "vcEnclosureAddress": vcEnclosureAddress,
       "vcEnclosureUUID": vcEnclosureUUID,
       "vcEnclosureRootCause": vcEnclosureRootCause,
       "vcEnclosureCause": vcEnclosureCause,
       "vcEnclosureReasonCode": vcEnclosureReasonCode,
       "vcEnclosureAddressIpv6": vcEnclosureAddressIpv6,
       "vcModule": vcModule,
       "vcModuleTable": vcModuleTable,
       "vcModuleEntry": vcModuleEntry,
       "vcModuleIndex": vcModuleIndex,
       "vcModuleType": vcModuleType,
       "vcModuleManagedStatus": vcModuleManagedStatus,
       "vcModulePartNumber": vcModulePartNumber,
       "vcModuleSerialNumber": vcModuleSerialNumber,
       "vcModuleProductName": vcModuleProductName,
       "vcModuleFwRev": vcModuleFwRev,
       "vcModuleEnclosurePointer": vcModuleEnclosurePointer,
       "vcModuleLocation": vcModuleLocation,
       "vcModuleAddressType": vcModuleAddressType,
       "vcModuleAddress": vcModuleAddress,
       "vcModuleID": vcModuleID,
       "vcModuleRootCause": vcModuleRootCause,
       "vcModuleCause": vcModuleCause,
       "vcModuleReasonCode": vcModuleReasonCode,
       "vcModuleAddressIpv6": vcModuleAddressIpv6,
       "vcPort": vcPort,
       "vcPortTable": vcPortTable,
       "vcPortEntry": vcPortEntry,
       "vcPortIndex": vcPortIndex,
       "vcPortType": vcPortType,
       "vcPortManagedStatus": vcPortManagedStatus,
       "vcPortManagerAddressType": vcPortManagerAddressType,
       "vcPortManagerAddress": vcPortManagerAddress,
       "vcPortPhysicalPortPointer": vcPortPhysicalPortPointer,
       "vcPortContainerPointer": vcPortContainerPointer,
       "vcPhysicalServer": vcPhysicalServer,
       "vcPhysicalServerTable": vcPhysicalServerTable,
       "vcPhysicalServerEntry": vcPhysicalServerEntry,
       "vcPhysicalServerIndex": vcPhysicalServerIndex,
       "vcPhysicalServerEnclosureIndex": vcPhysicalServerEnclosureIndex,
       "vcPhysicalServerManagedStatus": vcPhysicalServerManagedStatus,
       "vcPhysicalServerPartNumber": vcPhysicalServerPartNumber,
       "vcPhysicalServerSerialNumber": vcPhysicalServerSerialNumber,
       "vcPhysicalServerProductName": vcPhysicalServerProductName,
       "vcPhysicalServerLocation": vcPhysicalServerLocation,
       "vcPhysicalServerRootCause": vcPhysicalServerRootCause,
       "vcPhysicalServerCause": vcPhysicalServerCause,
       "vcPhysicalServerReasonCode": vcPhysicalServerReasonCode,
       "vcEnetNetwork": vcEnetNetwork,
       "vcEnetNetworkTable": vcEnetNetworkTable,
       "vcEnetNetworkEntry": vcEnetNetworkEntry,
       "vcEnetNetworkIndex": vcEnetNetworkIndex,
       "vcEnetNetworkName": vcEnetNetworkName,
       "vcEnetNetworkManagedStatus": vcEnetNetworkManagedStatus,
       "vcEnetNetworkUplinkVlanId": vcEnetNetworkUplinkVlanId,
       "vcEnetNetworkRootCause": vcEnetNetworkRootCause,
       "vcEnetNetworkCause": vcEnetNetworkCause,
       "vcEnetNetworkReasonCode": vcEnetNetworkReasonCode,
       "vcFcFabric": vcFcFabric,
       "vcFcFabricTable": vcFcFabricTable,
       "vcFcFabricEntry": vcFcFabricEntry,
       "vcFcFabricIndex": vcFcFabricIndex,
       "vcFcFabricName": vcFcFabricName,
       "vcFcFabricManagedStatus": vcFcFabricManagedStatus,
       "vcFcFabricRootCause": vcFcFabricRootCause,
       "vcFcFabricCause": vcFcFabricCause,
       "vcFcFabricReasonCode": vcFcFabricReasonCode,
       "vcProfile": vcProfile,
       "vcProfileTable": vcProfileTable,
       "vcProfileEntry": vcProfileEntry,
       "vcProfileIndex": vcProfileIndex,
       "vcProfileName": vcProfileName,
       "vcProfileManagedStatus": vcProfileManagedStatus,
       "vcProfilePhysicalServerIndex": vcProfilePhysicalServerIndex,
       "vcProfileLogicalSerialNumber": vcProfileLogicalSerialNumber,
       "vcProfileRootCause": vcProfileRootCause,
       "vcProfileCause": vcProfileCause,
       "vcProfileReasonCode": vcProfileReasonCode,
       "vcEnetNetworkVcPortMap": vcEnetNetworkVcPortMap,
       "vcEnetNetworkVcPortMapTable": vcEnetNetworkVcPortMapTable,
       "vcEnetNetworkVcPortMapEntry": vcEnetNetworkVcPortMapEntry,
       "vcEnetNetworkVcPortMapNetworkIndex": vcEnetNetworkVcPortMapNetworkIndex,
       "vcEnetNetworkVcPortMapVcPortIndex": vcEnetNetworkVcPortMapVcPortIndex,
       "vcFcFabricVcPortMap": vcFcFabricVcPortMap,
       "vcFcFabricVcPortMapTable": vcFcFabricVcPortMapTable,
       "vcFcFabricVcPortMapEntry": vcFcFabricVcPortMapEntry,
       "vcFcFabricVcPortMapFcFabricIndex": vcFcFabricVcPortMapFcFabricIndex,
       "vcFcFabricVcPortMapVcPortIndex": vcFcFabricVcPortMapVcPortIndex,
       "vcProfileNetworkMap": vcProfileNetworkMap,
       "vcProfileNetworkMapTable": vcProfileNetworkMapTable,
       "vcProfileNetworkMapEntry": vcProfileNetworkMapEntry,
       "vcProfileNetworkMapProfileIndex": vcProfileNetworkMapProfileIndex,
       "vcProfileNetworkMapConnectionIndex": vcProfileNetworkMapConnectionIndex,
       "vcProfileNetworkMapNetworkIndex": vcProfileNetworkMapNetworkIndex,
       "vcProfileFcFabricMap": vcProfileFcFabricMap,
       "vcProfileFcFabricMapTable": vcProfileFcFabricMapTable,
       "vcProfileFcFabricMapEntry": vcProfileFcFabricMapEntry,
       "vcProfileFcFabricMapProfileIndex": vcProfileFcFabricMapProfileIndex,
       "vcProfileFcFabricMapConnectionIndex": vcProfileFcFabricMapConnectionIndex,
       "vcProfileFcFabricMapFcFabricIndex": vcProfileFcFabricMapFcFabricIndex,
       "vcDomainMIBNotificationPrefix": vcDomainMIBNotificationPrefix,
       "vcDomainMIBNotifications": vcDomainMIBNotifications,
       "vcDomainManagedStatusChange": vcDomainManagedStatusChange,
       "vcCheckpointTimeout": vcCheckpointTimeout,
       "vcCheckpointCompleted": vcCheckpointCompleted,
       "vcEnetNetworkManagedStatusChange": vcEnetNetworkManagedStatusChange,
       "vcFcFabricManagedStatusChange": vcFcFabricManagedStatusChange,
       "vcModuleManagedStatusChange": vcModuleManagedStatusChange,
       "vcEnclosureManagedStatusChange": vcEnclosureManagedStatusChange,
       "vcPhysicalServerManagedStatusChange": vcPhysicalServerManagedStatusChange,
       "vcProfileManagedStatusChange": vcProfileManagedStatusChange,
       "vcTestTrap": vcTestTrap,
       "vcDomainStackingLinkRendundancyStatusChange": vcDomainStackingLinkRendundancyStatusChange,
       "vcDomainManagedStatusChanged": vcDomainManagedStatusChanged,
       "vcEnclosureManagedStatusChanged": vcEnclosureManagedStatusChanged,
       "vcModuleManagedStatusChanged": vcModuleManagedStatusChanged,
       "vcPhysicalServerManagedStatusChanged": vcPhysicalServerManagedStatusChanged,
       "vcFcFabricManagedStatusChanged": vcFcFabricManagedStatusChanged,
       "vcEnetNetworkManagedStatusChanged": vcEnetNetworkManagedStatusChanged,
       "vcProfileManagedStatusChanged": vcProfileManagedStatusChanged,
       "vcDomainMIBNotificationObjects": vcDomainMIBNotificationObjects,
       "vcDomainMIBConformance": vcDomainMIBConformance,
       "vcDomainMIBCompliances": vcDomainMIBCompliances,
       "vcDomainMIBCompliance": vcDomainMIBCompliance,
       "vcDomainMIBGroups": vcDomainMIBGroups,
       "vcDomainGroup": vcDomainGroup,
       "vcEnclosureGroup": vcEnclosureGroup,
       "vcModuleGroup": vcModuleGroup,
       "vcPortGroup": vcPortGroup,
       "vcPhysicalServerGroup": vcPhysicalServerGroup,
       "vcFcFabricGroup": vcFcFabricGroup,
       "vcEnetNetworkGroup": vcEnetNetworkGroup,
       "vcProfileGroup": vcProfileGroup,
       "vcEnetNetworkVcPortMapGroup": vcEnetNetworkVcPortMapGroup,
       "vcFcFabricVcPortMapGroup": vcFcFabricVcPortMapGroup,
       "vcProfileNetworkMapGroup": vcProfileNetworkMapGroup,
       "vcProfileFcFabricMapGroup": vcProfileFcFabricMapGroup,
       "vcManagedStatusNotificationsGroup": vcManagedStatusNotificationsGroup,
       "vcManagedStatusNotificationsGroup2": vcManagedStatusNotificationsGroup2}
)
