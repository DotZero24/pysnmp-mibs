# SNMP MIB module (H3C-VSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-VSAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:51 2025
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
 H3cFcDmState,
 H3cFcDomainId,
 H3cFcDomainIdList,
 H3cFcDomainIdOrZero,
 H3cFcDomainPriority,
 H3cFcNameId,
 H3cFcNameIdOrZero,
 H3cFcVsanIndex) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcAddressId",
    "H3cFcDmState",
    "H3cFcDomainId",
    "H3cFcDomainIdList",
    "H3cFcDomainIdOrZero",
    "H3cFcDomainPriority",
    "H3cFcNameId",
    "H3cFcNameIdOrZero",
    "H3cFcVsanIndex")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

h3cSan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127)
)
if mibBuilder.loadTexts:
    h3cSan.setRevisions(
        ("2014-07-25 18:40",
         "2014-05-09 18:40",
         "2014-03-04 15:50",
         "2013-02-28 09:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVsan_ObjectIdentity = ObjectIdentity
h3cVsan = _H3cVsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1)
)
_H3cVsanMibObjects_ObjectIdentity = ObjectIdentity
h3cVsanMibObjects = _H3cVsanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1)
)
_H3cVsanDmConfiguration_ObjectIdentity = ObjectIdentity
h3cVsanDmConfiguration = _H3cVsanDmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1)
)
_H3cVsanTable_Object = MibTable
h3cVsanTable = _H3cVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVsanTable.setStatus("current")
_H3cVsanEntry_Object = MibTableRow
h3cVsanEntry = _H3cVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1, 1)
)
h3cVsanEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cVsanEntry.setStatus("current")
_H3cVsanIndex_Type = H3cFcVsanIndex
_H3cVsanIndex_Object = MibTableColumn
h3cVsanIndex = _H3cVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1, 1, 1),
    _H3cVsanIndex_Type()
)
h3cVsanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVsanIndex.setStatus("current")


class _H3cVsanCoreSwitchName_Type(H3cFcNameIdOrZero):
    """Custom type h3cVsanCoreSwitchName based on H3cFcNameIdOrZero"""
    subtypeSpec = H3cFcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_H3cVsanCoreSwitchName_Type.__name__ = "H3cFcNameIdOrZero"
_H3cVsanCoreSwitchName_Object = MibTableColumn
h3cVsanCoreSwitchName = _H3cVsanCoreSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1, 1, 2),
    _H3cVsanCoreSwitchName_Type()
)
h3cVsanCoreSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanCoreSwitchName.setStatus("current")
_H3cVsanRowStatus_Type = RowStatus
_H3cVsanRowStatus_Object = MibTableColumn
h3cVsanRowStatus = _H3cVsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1, 1, 3),
    _H3cVsanRowStatus_Type()
)
h3cVsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsanRowStatus.setStatus("current")


class _H3cVsanName_Type(SnmpAdminString):
    """Custom type h3cVsanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cVsanName_Type.__name__ = "SnmpAdminString"
_H3cVsanName_Object = MibTableColumn
h3cVsanName = _H3cVsanName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1, 1, 4),
    _H3cVsanName_Type()
)
h3cVsanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsanName.setStatus("current")
_H3cVsanWorkingMode_Type = Integer32
_H3cVsanWorkingMode_Object = MibTableColumn
h3cVsanWorkingMode = _H3cVsanWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 1, 1, 5),
    _H3cVsanWorkingMode_Type()
)
h3cVsanWorkingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsanWorkingMode.setStatus("current")
_H3cVsanDmTable_Object = MibTable
h3cVsanDmTable = _H3cVsanDmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVsanDmTable.setStatus("current")
_H3cVsanDmEntry_Object = MibTableRow
h3cVsanDmEntry = _H3cVsanDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1)
)
h3cVsanDmEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cVsanDmEntry.setStatus("current")


class _H3cVsanDmDomainConfigureEnable_Type(TruthValue):
    """Custom type h3cVsanDmDomainConfigureEnable based on TruthValue"""
    defaultValue = 1


_H3cVsanDmDomainConfigureEnable_Type.__name__ = "TruthValue"
_H3cVsanDmDomainConfigureEnable_Object = MibTableColumn
h3cVsanDmDomainConfigureEnable = _H3cVsanDmDomainConfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 1),
    _H3cVsanDmDomainConfigureEnable_Type()
)
h3cVsanDmDomainConfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmDomainConfigureEnable.setStatus("current")
_H3cVsanDmFabricNameConfigured_Type = H3cFcNameIdOrZero
_H3cVsanDmFabricNameConfigured_Object = MibTableColumn
h3cVsanDmFabricNameConfigured = _H3cVsanDmFabricNameConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 2),
    _H3cVsanDmFabricNameConfigured_Type()
)
h3cVsanDmFabricNameConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmFabricNameConfigured.setStatus("current")


class _H3cVsanDmPriorityConfigured_Type(H3cFcDomainPriority):
    """Custom type h3cVsanDmPriorityConfigured based on H3cFcDomainPriority"""
    defaultValue = 128


_H3cVsanDmPriorityConfigured_Type.__name__ = "H3cFcDomainPriority"
_H3cVsanDmPriorityConfigured_Object = MibTableColumn
h3cVsanDmPriorityConfigured = _H3cVsanDmPriorityConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 3),
    _H3cVsanDmPriorityConfigured_Type()
)
h3cVsanDmPriorityConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmPriorityConfigured.setStatus("current")
_H3cVsanDmAllowedDomainIdList_Type = H3cFcDomainIdList
_H3cVsanDmAllowedDomainIdList_Object = MibTableColumn
h3cVsanDmAllowedDomainIdList = _H3cVsanDmAllowedDomainIdList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 4),
    _H3cVsanDmAllowedDomainIdList_Type()
)
h3cVsanDmAllowedDomainIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmAllowedDomainIdList.setStatus("current")


class _H3cVsanDmDomainIdConfigured_Type(H3cFcDomainIdOrZero):
    """Custom type h3cVsanDmDomainIdConfigured based on H3cFcDomainIdOrZero"""
    defaultValue = 0


_H3cVsanDmDomainIdConfigured_Type.__name__ = "H3cFcDomainIdOrZero"
_H3cVsanDmDomainIdConfigured_Object = MibTableColumn
h3cVsanDmDomainIdConfigured = _H3cVsanDmDomainIdConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 5),
    _H3cVsanDmDomainIdConfigured_Type()
)
h3cVsanDmDomainIdConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmDomainIdConfigured.setStatus("current")


class _H3cVsanDmDomainIdTypeConfigured_Type(Integer32):
    """Custom type h3cVsanDmDomainIdTypeConfigured based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("preferred", 2))
    )


_H3cVsanDmDomainIdTypeConfigured_Type.__name__ = "Integer32"
_H3cVsanDmDomainIdTypeConfigured_Object = MibTableColumn
h3cVsanDmDomainIdTypeConfigured = _H3cVsanDmDomainIdTypeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 6),
    _H3cVsanDmDomainIdTypeConfigured_Type()
)
h3cVsanDmDomainIdTypeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmDomainIdTypeConfigured.setStatus("current")


class _H3cVsanDmAutoReconfigureEnable_Type(TruthValue):
    """Custom type h3cVsanDmAutoReconfigureEnable based on TruthValue"""
    defaultValue = 2


_H3cVsanDmAutoReconfigureEnable_Type.__name__ = "TruthValue"
_H3cVsanDmAutoReconfigureEnable_Object = MibTableColumn
h3cVsanDmAutoReconfigureEnable = _H3cVsanDmAutoReconfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 7),
    _H3cVsanDmAutoReconfigureEnable_Type()
)
h3cVsanDmAutoReconfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmAutoReconfigureEnable.setStatus("current")


class _H3cVsanDmDomainRestart_Type(Integer32):
    """Custom type h3cVsanDmDomainRestart based on Integer32"""
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
        *(("noOperation", 1),
          ("nonDisruptive", 2),
          ("disruptive", 3))
    )


_H3cVsanDmDomainRestart_Type.__name__ = "Integer32"
_H3cVsanDmDomainRestart_Object = MibTableColumn
h3cVsanDmDomainRestart = _H3cVsanDmDomainRestart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 8),
    _H3cVsanDmDomainRestart_Type()
)
h3cVsanDmDomainRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmDomainRestart.setStatus("current")
_H3cVsanDmState_Type = H3cFcDmState
_H3cVsanDmState_Object = MibTableColumn
h3cVsanDmState = _H3cVsanDmState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 9),
    _H3cVsanDmState_Type()
)
h3cVsanDmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmState.setStatus("current")
_H3cVsanDmDomainIdAssigned_Type = H3cFcDomainIdOrZero
_H3cVsanDmDomainIdAssigned_Object = MibTableColumn
h3cVsanDmDomainIdAssigned = _H3cVsanDmDomainIdAssigned_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 10),
    _H3cVsanDmDomainIdAssigned_Type()
)
h3cVsanDmDomainIdAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmDomainIdAssigned.setStatus("current")
_H3cVsanDmPrincipalSwitchWWN_Type = H3cFcNameId
_H3cVsanDmPrincipalSwitchWWN_Object = MibTableColumn
h3cVsanDmPrincipalSwitchWWN = _H3cVsanDmPrincipalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 11),
    _H3cVsanDmPrincipalSwitchWWN_Type()
)
h3cVsanDmPrincipalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmPrincipalSwitchWWN.setStatus("current")
_H3cVsanDmLocalSwitchWWN_Type = H3cFcNameId
_H3cVsanDmLocalSwitchWWN_Object = MibTableColumn
h3cVsanDmLocalSwitchWWN = _H3cVsanDmLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 12),
    _H3cVsanDmLocalSwitchWWN_Type()
)
h3cVsanDmLocalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmLocalSwitchWWN.setStatus("current")
_H3cVsanDmPrincipalSwRunPriority_Type = H3cFcDomainPriority
_H3cVsanDmPrincipalSwRunPriority_Object = MibTableColumn
h3cVsanDmPrincipalSwRunPriority = _H3cVsanDmPrincipalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 13),
    _H3cVsanDmPrincipalSwRunPriority_Type()
)
h3cVsanDmPrincipalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmPrincipalSwRunPriority.setStatus("current")
_H3cVsanDmLocalSwRunPriority_Type = H3cFcDomainPriority
_H3cVsanDmLocalSwRunPriority_Object = MibTableColumn
h3cVsanDmLocalSwRunPriority = _H3cVsanDmLocalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 14),
    _H3cVsanDmLocalSwRunPriority_Type()
)
h3cVsanDmLocalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmLocalSwRunPriority.setStatus("current")
_H3cVsanDmPrincipalSwSlctCnt_Type = Counter32
_H3cVsanDmPrincipalSwSlctCnt_Object = MibTableColumn
h3cVsanDmPrincipalSwSlctCnt = _H3cVsanDmPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 15),
    _H3cVsanDmPrincipalSwSlctCnt_Type()
)
h3cVsanDmPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmPrincipalSwSlctCnt.setStatus("current")
_H3cVsanDmLocalPrincipalSwSlctCnt_Type = Counter32
_H3cVsanDmLocalPrincipalSwSlctCnt_Object = MibTableColumn
h3cVsanDmLocalPrincipalSwSlctCnt = _H3cVsanDmLocalPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 16),
    _H3cVsanDmLocalPrincipalSwSlctCnt_Type()
)
h3cVsanDmLocalPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmLocalPrincipalSwSlctCnt.setStatus("current")
_H3cVsanDmBFCnt_Type = Counter32
_H3cVsanDmBFCnt_Object = MibTableColumn
h3cVsanDmBFCnt = _H3cVsanDmBFCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 17),
    _H3cVsanDmBFCnt_Type()
)
h3cVsanDmBFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmBFCnt.setStatus("current")
_H3cVsanDmRCFCnt_Type = Counter32
_H3cVsanDmRCFCnt_Object = MibTableColumn
h3cVsanDmRCFCnt = _H3cVsanDmRCFCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 2, 1, 18),
    _H3cVsanDmRCFCnt_Type()
)
h3cVsanDmRCFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmRCFCnt.setStatus("current")
_H3cVsanDmIfConfigTable_Object = MibTable
h3cVsanDmIfConfigTable = _H3cVsanDmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVsanDmIfConfigTable.setStatus("current")
_H3cVsanDmIfConfigEntry_Object = MibTableRow
h3cVsanDmIfConfigEntry = _H3cVsanDmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 3, 1)
)
h3cVsanDmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cVsanDmIfConfigEntry.setStatus("current")


class _H3cVsanDmIfConfigRcfReject_Type(TruthValue):
    """Custom type h3cVsanDmIfConfigRcfReject based on TruthValue"""
    defaultValue = 2


_H3cVsanDmIfConfigRcfReject_Type.__name__ = "TruthValue"
_H3cVsanDmIfConfigRcfReject_Object = MibTableColumn
h3cVsanDmIfConfigRcfReject = _H3cVsanDmIfConfigRcfReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 3, 1, 1),
    _H3cVsanDmIfConfigRcfReject_Type()
)
h3cVsanDmIfConfigRcfReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmIfConfigRcfReject.setStatus("current")
_H3cVsanFcIdTable_Object = MibTable
h3cVsanFcIdTable = _H3cVsanFcIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3cVsanFcIdTable.setStatus("current")
_H3cVsanFcIdEntry_Object = MibTableRow
h3cVsanFcIdEntry = _H3cVsanFcIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 4, 1)
)
h3cVsanFcIdEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cVsanFcIdEntry.setStatus("current")
_H3cVsanFreeFcIds_Type = Counter32
_H3cVsanFreeFcIds_Object = MibTableColumn
h3cVsanFreeFcIds = _H3cVsanFreeFcIds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 4, 1, 1),
    _H3cVsanFreeFcIds_Type()
)
h3cVsanFreeFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanFreeFcIds.setStatus("current")
_H3cVsanAssignedFcIds_Type = Counter32
_H3cVsanAssignedFcIds_Object = MibTableColumn
h3cVsanAssignedFcIds = _H3cVsanAssignedFcIds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 4, 1, 2),
    _H3cVsanAssignedFcIds_Type()
)
h3cVsanAssignedFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanAssignedFcIds.setStatus("current")


class _H3cVsanFcIdPersistency_Type(TruthValue):
    """Custom type h3cVsanFcIdPersistency based on TruthValue"""
    defaultValue = 1


_H3cVsanFcIdPersistency_Type.__name__ = "TruthValue"
_H3cVsanFcIdPersistency_Object = MibTableColumn
h3cVsanFcIdPersistency = _H3cVsanFcIdPersistency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 4, 1, 3),
    _H3cVsanFcIdPersistency_Type()
)
h3cVsanFcIdPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistency.setStatus("current")


class _H3cVsanFcIdPurge_Type(Integer32):
    """Custom type h3cVsanFcIdPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("enable", 2))
    )


_H3cVsanFcIdPurge_Type.__name__ = "Integer32"
_H3cVsanFcIdPurge_Object = MibTableColumn
h3cVsanFcIdPurge = _H3cVsanFcIdPurge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 4, 1, 4),
    _H3cVsanFcIdPurge_Type()
)
h3cVsanFcIdPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanFcIdPurge.setStatus("current")
_H3cVsanFcIdPersistencyTable_Object = MibTable
h3cVsanFcIdPersistencyTable = _H3cVsanFcIdPersistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyTable.setStatus("current")
_H3cVsanFcIdPersistencyEntry_Object = MibTableRow
h3cVsanFcIdPersistencyEntry = _H3cVsanFcIdPersistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5, 1)
)
h3cVsanFcIdPersistencyEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanFcIdPersistencyWwn"),
)
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyEntry.setStatus("current")
_H3cVsanFcIdPersistencyWwn_Type = H3cFcNameId
_H3cVsanFcIdPersistencyWwn_Object = MibTableColumn
h3cVsanFcIdPersistencyWwn = _H3cVsanFcIdPersistencyWwn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5, 1, 1),
    _H3cVsanFcIdPersistencyWwn_Type()
)
h3cVsanFcIdPersistencyWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyWwn.setStatus("current")
_H3cVsanFcIdPersistencyFcId_Type = H3cFcAddressId
_H3cVsanFcIdPersistencyFcId_Object = MibTableColumn
h3cVsanFcIdPersistencyFcId = _H3cVsanFcIdPersistencyFcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5, 1, 2),
    _H3cVsanFcIdPersistencyFcId_Type()
)
h3cVsanFcIdPersistencyFcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyFcId.setStatus("current")
_H3cVsanFcIdPersistencyUsed_Type = TruthValue
_H3cVsanFcIdPersistencyUsed_Object = MibTableColumn
h3cVsanFcIdPersistencyUsed = _H3cVsanFcIdPersistencyUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5, 1, 3),
    _H3cVsanFcIdPersistencyUsed_Type()
)
h3cVsanFcIdPersistencyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyUsed.setStatus("current")


class _H3cVsanFcIdPersistencyType_Type(Integer32):
    """Custom type h3cVsanFcIdPersistencyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_H3cVsanFcIdPersistencyType_Type.__name__ = "Integer32"
_H3cVsanFcIdPersistencyType_Object = MibTableColumn
h3cVsanFcIdPersistencyType = _H3cVsanFcIdPersistencyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5, 1, 4),
    _H3cVsanFcIdPersistencyType_Type()
)
h3cVsanFcIdPersistencyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyType.setStatus("current")
_H3cVsanFcIdPersistencyRowStatus_Type = RowStatus
_H3cVsanFcIdPersistencyRowStatus_Object = MibTableColumn
h3cVsanFcIdPersistencyRowStatus = _H3cVsanFcIdPersistencyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 1, 5, 1, 5),
    _H3cVsanFcIdPersistencyRowStatus_Type()
)
h3cVsanFcIdPersistencyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsanFcIdPersistencyRowStatus.setStatus("current")
_H3cVsanDmInformation_ObjectIdentity = ObjectIdentity
h3cVsanDmInformation = _H3cVsanDmInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2)
)
_H3cVsanDmDatabaseTable_Object = MibTable
h3cVsanDmDatabaseTable = _H3cVsanDmDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cVsanDmDatabaseTable.setStatus("current")
_H3cVsanDmDatabaseEntry_Object = MibTableRow
h3cVsanDmDatabaseEntry = _H3cVsanDmDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 1, 1)
)
h3cVsanDmDatabaseEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanDmDatabaseDomainId"),
)
if mibBuilder.loadTexts:
    h3cVsanDmDatabaseEntry.setStatus("current")
_H3cVsanDmDatabaseDomainId_Type = H3cFcDomainId
_H3cVsanDmDatabaseDomainId_Object = MibTableColumn
h3cVsanDmDatabaseDomainId = _H3cVsanDmDatabaseDomainId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 1, 1, 1),
    _H3cVsanDmDatabaseDomainId_Type()
)
h3cVsanDmDatabaseDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsanDmDatabaseDomainId.setStatus("current")
_H3cVsanDmDatabaseSwitchWWN_Type = H3cFcNameId
_H3cVsanDmDatabaseSwitchWWN_Object = MibTableColumn
h3cVsanDmDatabaseSwitchWWN = _H3cVsanDmDatabaseSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 1, 1, 2),
    _H3cVsanDmDatabaseSwitchWWN_Type()
)
h3cVsanDmDatabaseSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmDatabaseSwitchWWN.setStatus("current")
_H3cVsanDmIfInfoTable_Object = MibTable
h3cVsanDmIfInfoTable = _H3cVsanDmIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cVsanDmIfInfoTable.setStatus("current")
_H3cVsanDmIfInfoEntry_Object = MibTableRow
h3cVsanDmIfInfoEntry = _H3cVsanDmIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 2, 1)
)
h3cVsanDmIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cVsanDmIfInfoEntry.setStatus("current")


class _H3cVsanDmIfInfoRole_Type(Integer32):
    """Custom type h3cVsanDmIfInfoRole based on Integer32"""
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
        *(("nonPrincipal", 1),
          ("principalUpstream", 2),
          ("principalDownstream", 3),
          ("isolated", 4),
          ("unknown", 5))
    )


_H3cVsanDmIfInfoRole_Type.__name__ = "Integer32"
_H3cVsanDmIfInfoRole_Object = MibTableColumn
h3cVsanDmIfInfoRole = _H3cVsanDmIfInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 2, 2, 1, 1),
    _H3cVsanDmIfInfoRole_Type()
)
h3cVsanDmIfInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsanDmIfInfoRole.setStatus("current")
_H3cVsanDmNotifications_ObjectIdentity = ObjectIdentity
h3cVsanDmNotifications = _H3cVsanDmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3)
)
_H3cVsanDmNotificationPrefix_ObjectIdentity = ObjectIdentity
h3cVsanDmNotificationPrefix = _H3cVsanDmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 0)
)
_H3cVsanDmNotificationSwitch_ObjectIdentity = ObjectIdentity
h3cVsanDmNotificationSwitch = _H3cVsanDmNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 1)
)


class _H3cVsanDmFabricChangeNotifyEnable_Type(TruthValue):
    """Custom type h3cVsanDmFabricChangeNotifyEnable based on TruthValue"""
    defaultValue = 2


_H3cVsanDmFabricChangeNotifyEnable_Type.__name__ = "TruthValue"
_H3cVsanDmFabricChangeNotifyEnable_Object = MibScalar
h3cVsanDmFabricChangeNotifyEnable = _H3cVsanDmFabricChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 1, 1),
    _H3cVsanDmFabricChangeNotifyEnable_Type()
)
h3cVsanDmFabricChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmFabricChangeNotifyEnable.setStatus("current")


class _H3cVsanDmDomainIdChangeNotifyEnable_Type(TruthValue):
    """Custom type h3cVsanDmDomainIdChangeNotifyEnable based on TruthValue"""
    defaultValue = 2


_H3cVsanDmDomainIdChangeNotifyEnable_Type.__name__ = "TruthValue"
_H3cVsanDmDomainIdChangeNotifyEnable_Object = MibScalar
h3cVsanDmDomainIdChangeNotifyEnable = _H3cVsanDmDomainIdChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 1, 2),
    _H3cVsanDmDomainIdChangeNotifyEnable_Type()
)
h3cVsanDmDomainIdChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsanDmDomainIdChangeNotifyEnable.setStatus("current")

# Managed Objects groups


# Notification objects

h3cVsanDmDomainIdNotAssignedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 0, 1)
)
h3cVsanDmDomainIdNotAssignedNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-VSAN-MIB", "h3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    h3cVsanDmDomainIdNotAssignedNotify.setStatus(
        "current"
    )

h3cVsanDmNewPrincipalSwitchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 0, 2)
)
h3cVsanDmNewPrincipalSwitchNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-VSAN-MIB", "h3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    h3cVsanDmNewPrincipalSwitchNotify.setStatus(
        "current"
    )

h3cVsanDmFabricChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 0, 3)
)
h3cVsanDmFabricChangeNotify.setObjects(
    ("H3C-VSAN-MIB", "h3cVsanIndex")
)
if mibBuilder.loadTexts:
    h3cVsanDmFabricChangeNotify.setStatus(
        "current"
    )

h3cVsanDmDomainIdChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 1, 1, 3, 0, 4)
)
h3cVsanDmDomainIdChangeNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-VSAN-MIB", "h3cVsanDmDomainIdAssigned"),
        ("H3C-VSAN-MIB", "h3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    h3cVsanDmDomainIdChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VSAN-MIB",
    **{"h3cSan": h3cSan,
       "h3cVsan": h3cVsan,
       "h3cVsanMibObjects": h3cVsanMibObjects,
       "h3cVsanDmConfiguration": h3cVsanDmConfiguration,
       "h3cVsanTable": h3cVsanTable,
       "h3cVsanEntry": h3cVsanEntry,
       "h3cVsanIndex": h3cVsanIndex,
       "h3cVsanCoreSwitchName": h3cVsanCoreSwitchName,
       "h3cVsanRowStatus": h3cVsanRowStatus,
       "h3cVsanName": h3cVsanName,
       "h3cVsanWorkingMode": h3cVsanWorkingMode,
       "h3cVsanDmTable": h3cVsanDmTable,
       "h3cVsanDmEntry": h3cVsanDmEntry,
       "h3cVsanDmDomainConfigureEnable": h3cVsanDmDomainConfigureEnable,
       "h3cVsanDmFabricNameConfigured": h3cVsanDmFabricNameConfigured,
       "h3cVsanDmPriorityConfigured": h3cVsanDmPriorityConfigured,
       "h3cVsanDmAllowedDomainIdList": h3cVsanDmAllowedDomainIdList,
       "h3cVsanDmDomainIdConfigured": h3cVsanDmDomainIdConfigured,
       "h3cVsanDmDomainIdTypeConfigured": h3cVsanDmDomainIdTypeConfigured,
       "h3cVsanDmAutoReconfigureEnable": h3cVsanDmAutoReconfigureEnable,
       "h3cVsanDmDomainRestart": h3cVsanDmDomainRestart,
       "h3cVsanDmState": h3cVsanDmState,
       "h3cVsanDmDomainIdAssigned": h3cVsanDmDomainIdAssigned,
       "h3cVsanDmPrincipalSwitchWWN": h3cVsanDmPrincipalSwitchWWN,
       "h3cVsanDmLocalSwitchWWN": h3cVsanDmLocalSwitchWWN,
       "h3cVsanDmPrincipalSwRunPriority": h3cVsanDmPrincipalSwRunPriority,
       "h3cVsanDmLocalSwRunPriority": h3cVsanDmLocalSwRunPriority,
       "h3cVsanDmPrincipalSwSlctCnt": h3cVsanDmPrincipalSwSlctCnt,
       "h3cVsanDmLocalPrincipalSwSlctCnt": h3cVsanDmLocalPrincipalSwSlctCnt,
       "h3cVsanDmBFCnt": h3cVsanDmBFCnt,
       "h3cVsanDmRCFCnt": h3cVsanDmRCFCnt,
       "h3cVsanDmIfConfigTable": h3cVsanDmIfConfigTable,
       "h3cVsanDmIfConfigEntry": h3cVsanDmIfConfigEntry,
       "h3cVsanDmIfConfigRcfReject": h3cVsanDmIfConfigRcfReject,
       "h3cVsanFcIdTable": h3cVsanFcIdTable,
       "h3cVsanFcIdEntry": h3cVsanFcIdEntry,
       "h3cVsanFreeFcIds": h3cVsanFreeFcIds,
       "h3cVsanAssignedFcIds": h3cVsanAssignedFcIds,
       "h3cVsanFcIdPersistency": h3cVsanFcIdPersistency,
       "h3cVsanFcIdPurge": h3cVsanFcIdPurge,
       "h3cVsanFcIdPersistencyTable": h3cVsanFcIdPersistencyTable,
       "h3cVsanFcIdPersistencyEntry": h3cVsanFcIdPersistencyEntry,
       "h3cVsanFcIdPersistencyWwn": h3cVsanFcIdPersistencyWwn,
       "h3cVsanFcIdPersistencyFcId": h3cVsanFcIdPersistencyFcId,
       "h3cVsanFcIdPersistencyUsed": h3cVsanFcIdPersistencyUsed,
       "h3cVsanFcIdPersistencyType": h3cVsanFcIdPersistencyType,
       "h3cVsanFcIdPersistencyRowStatus": h3cVsanFcIdPersistencyRowStatus,
       "h3cVsanDmInformation": h3cVsanDmInformation,
       "h3cVsanDmDatabaseTable": h3cVsanDmDatabaseTable,
       "h3cVsanDmDatabaseEntry": h3cVsanDmDatabaseEntry,
       "h3cVsanDmDatabaseDomainId": h3cVsanDmDatabaseDomainId,
       "h3cVsanDmDatabaseSwitchWWN": h3cVsanDmDatabaseSwitchWWN,
       "h3cVsanDmIfInfoTable": h3cVsanDmIfInfoTable,
       "h3cVsanDmIfInfoEntry": h3cVsanDmIfInfoEntry,
       "h3cVsanDmIfInfoRole": h3cVsanDmIfInfoRole,
       "h3cVsanDmNotifications": h3cVsanDmNotifications,
       "h3cVsanDmNotificationPrefix": h3cVsanDmNotificationPrefix,
       "h3cVsanDmDomainIdNotAssignedNotify": h3cVsanDmDomainIdNotAssignedNotify,
       "h3cVsanDmNewPrincipalSwitchNotify": h3cVsanDmNewPrincipalSwitchNotify,
       "h3cVsanDmFabricChangeNotify": h3cVsanDmFabricChangeNotify,
       "h3cVsanDmDomainIdChangeNotify": h3cVsanDmDomainIdChangeNotify,
       "h3cVsanDmNotificationSwitch": h3cVsanDmNotificationSwitch,
       "h3cVsanDmFabricChangeNotifyEnable": h3cVsanDmFabricChangeNotifyEnable,
       "h3cVsanDmDomainIdChangeNotifyEnable": h3cVsanDmDomainIdChangeNotifyEnable}
)
