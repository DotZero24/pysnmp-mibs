# SNMP MIB module (HM2-ETB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-ETB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:55:27 2025
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

hm2EtbMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130)
)
if mibBuilder.loadTexts:
    hm2EtbMib.setRevisions(
        ("2015-08-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2CstUuid(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x-2x-2x-2x-6x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_Hm2EtbMibObjects_ObjectIdentity = ObjectIdentity
hm2EtbMibObjects = _Hm2EtbMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1)
)
_Hm2TtdpGroup_ObjectIdentity = ObjectIdentity
hm2TtdpGroup = _Hm2TtdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1)
)
_Hm2TtdpAdminState_Type = HmEnabledStatus
_Hm2TtdpAdminState_Object = MibScalar
hm2TtdpAdminState = _Hm2TtdpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 1),
    _Hm2TtdpAdminState_Type()
)
hm2TtdpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpAdminState.setStatus("current")


class _Hm2TtdpOperState_Type(Integer32):
    """Custom type hm2TtdpOperState based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("lagsNotCreated", 1),
          ("lagsCreatedNotUp", 2),
          ("lagsNoMemberPort", 3),
          ("routingNotReady", 4),
          ("lagsReady", 5),
          ("componentDisable", 6),
          ("localETBNInhibit", 7),
          ("remoteETBNInhibit", 8),
          ("appInhibit", 9),
          ("consistUUIDMissing", 10),
          ("backboneIDMissing", 11),
          ("etbnCountMissing", 12),
          ("cnCountMissing", 13),
          ("ownETBNIdMissing", 14),
          ("etbnHasNoCN", 15),
          ("running", 16),
          ("singleDeviceInaugurated", 17),
          ("trainInaugurated", 18))
    )


_Hm2TtdpOperState_Type.__name__ = "Integer32"
_Hm2TtdpOperState_Object = MibScalar
hm2TtdpOperState = _Hm2TtdpOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 2),
    _Hm2TtdpOperState_Type()
)
hm2TtdpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TtdpOperState.setStatus("current")


class _Hm2TtdpCstCnCnt_Type(Integer32):
    """Custom type hm2TtdpCstCnCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hm2TtdpCstCnCnt_Type.__name__ = "Integer32"
_Hm2TtdpCstCnCnt_Object = MibScalar
hm2TtdpCstCnCnt = _Hm2TtdpCstCnCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 3),
    _Hm2TtdpCstCnCnt_Type()
)
hm2TtdpCstCnCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpCstCnCnt.setStatus("current")


class _Hm2TtdpCstEtbnCnt_Type(Integer32):
    """Custom type hm2TtdpCstEtbnCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2TtdpCstEtbnCnt_Type.__name__ = "Integer32"
_Hm2TtdpCstEtbnCnt_Object = MibScalar
hm2TtdpCstEtbnCnt = _Hm2TtdpCstEtbnCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 4),
    _Hm2TtdpCstEtbnCnt_Type()
)
hm2TtdpCstEtbnCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpCstEtbnCnt.setStatus("current")
_Hm2TtdpCstUuid_Type = Hm2CstUuid
_Hm2TtdpCstUuid_Object = MibScalar
hm2TtdpCstUuid = _Hm2TtdpCstUuid_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 5),
    _Hm2TtdpCstUuid_Type()
)
hm2TtdpCstUuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpCstUuid.setStatus("current")


class _Hm2TtdpCstCurrentEtbnNumber_Type(Integer32):
    """Custom type hm2TtdpCstCurrentEtbnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2TtdpCstCurrentEtbnNumber_Type.__name__ = "Integer32"
_Hm2TtdpCstCurrentEtbnNumber_Object = MibScalar
hm2TtdpCstCurrentEtbnNumber = _Hm2TtdpCstCurrentEtbnNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 6),
    _Hm2TtdpCstCurrentEtbnNumber_Type()
)
hm2TtdpCstCurrentEtbnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpCstCurrentEtbnNumber.setStatus("current")


class _Hm2TtdpBackboneId_Type(Integer32):
    """Custom type hm2TtdpBackboneId based on Integer32"""
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
        *(("tcms", 1),
          ("multimedia", 2),
          ("notSpecialized1", 3),
          ("notSpecialized2", 4))
    )


_Hm2TtdpBackboneId_Type.__name__ = "Integer32"
_Hm2TtdpBackboneId_Object = MibScalar
hm2TtdpBackboneId = _Hm2TtdpBackboneId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 7),
    _Hm2TtdpBackboneId_Type()
)
hm2TtdpBackboneId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpBackboneId.setStatus("current")


class _Hm2TtdpLocalEtbnInhibit_Type(TruthValue):
    """Custom type hm2TtdpLocalEtbnInhibit based on TruthValue"""
    defaultValue = 2


_Hm2TtdpLocalEtbnInhibit_Type.__name__ = "TruthValue"
_Hm2TtdpLocalEtbnInhibit_Object = MibScalar
hm2TtdpLocalEtbnInhibit = _Hm2TtdpLocalEtbnInhibit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 8),
    _Hm2TtdpLocalEtbnInhibit_Type()
)
hm2TtdpLocalEtbnInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpLocalEtbnInhibit.setStatus("current")


class _Hm2TtdpETBNRole_Type(Integer32):
    """Custom type hm2TtdpETBNRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("router", 2))
    )


_Hm2TtdpETBNRole_Type.__name__ = "Integer32"
_Hm2TtdpETBNRole_Object = MibScalar
hm2TtdpETBNRole = _Hm2TtdpETBNRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 9),
    _Hm2TtdpETBNRole_Type()
)
hm2TtdpETBNRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpETBNRole.setStatus("current")
_Hm2TtdpCnToEtbnTable_Object = MibTable
hm2TtdpCnToEtbnTable = _Hm2TtdpCnToEtbnTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnTable.setStatus("current")
_Hm2TtdpCnToEtbnEntry_Object = MibTableRow
hm2TtdpCnToEtbnEntry = _Hm2TtdpCnToEtbnEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20, 1)
)
hm2TtdpCnToEtbnEntry.setIndexNames(
    (0, "HM2-ETB-MIB", "hm2TtdpCnToEtbnTableIdx"),
    (0, "HM2-ETB-MIB", "hm2TtdpCnToEtbnCnTableIdx"),
)
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnEntry.setStatus("current")


class _Hm2TtdpCnToEtbnTableIdx_Type(Integer32):
    """Custom type hm2TtdpCnToEtbnTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2TtdpCnToEtbnTableIdx_Type.__name__ = "Integer32"
_Hm2TtdpCnToEtbnTableIdx_Object = MibTableColumn
hm2TtdpCnToEtbnTableIdx = _Hm2TtdpCnToEtbnTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20, 1, 1),
    _Hm2TtdpCnToEtbnTableIdx_Type()
)
hm2TtdpCnToEtbnTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnTableIdx.setStatus("current")


class _Hm2TtdpCnToEtbnCnTableIdx_Type(Integer32):
    """Custom type hm2TtdpCnToEtbnCnTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hm2TtdpCnToEtbnCnTableIdx_Type.__name__ = "Integer32"
_Hm2TtdpCnToEtbnCnTableIdx_Object = MibTableColumn
hm2TtdpCnToEtbnCnTableIdx = _Hm2TtdpCnToEtbnCnTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20, 1, 2),
    _Hm2TtdpCnToEtbnCnTableIdx_Type()
)
hm2TtdpCnToEtbnCnTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnCnTableIdx.setStatus("current")


class _Hm2TtdpCnToEtbnIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2TtdpCnToEtbnIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2TtdpCnToEtbnIntf_Type.__name__ = "InterfaceIndexOrZero"
_Hm2TtdpCnToEtbnIntf_Object = MibTableColumn
hm2TtdpCnToEtbnIntf = _Hm2TtdpCnToEtbnIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20, 1, 3),
    _Hm2TtdpCnToEtbnIntf_Type()
)
hm2TtdpCnToEtbnIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnIntf.setStatus("current")


class _Hm2TtdpCnToEtbnUseDHCPServer_Type(Integer32):
    """Custom type hm2TtdpCnToEtbnUseDHCPServer based on Integer32"""
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
        *(("none", 1),
          ("dhcp", 2),
          ("nat", 3))
    )


_Hm2TtdpCnToEtbnUseDHCPServer_Type.__name__ = "Integer32"
_Hm2TtdpCnToEtbnUseDHCPServer_Object = MibTableColumn
hm2TtdpCnToEtbnUseDHCPServer = _Hm2TtdpCnToEtbnUseDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20, 1, 4),
    _Hm2TtdpCnToEtbnUseDHCPServer_Type()
)
hm2TtdpCnToEtbnUseDHCPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnUseDHCPServer.setStatus("current")
_Hm2TtdpCnToEtbnRowStatus_Type = RowStatus
_Hm2TtdpCnToEtbnRowStatus_Object = MibTableColumn
hm2TtdpCnToEtbnRowStatus = _Hm2TtdpCnToEtbnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 1, 1, 20, 1, 5),
    _Hm2TtdpCnToEtbnRowStatus_Type()
)
hm2TtdpCnToEtbnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2TtdpCnToEtbnRowStatus.setStatus("current")
_Hm2EtbMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2EtbMibSNMPExtensionGroup = _Hm2EtbMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 3)
)
_Hm2TttdpWrongEtbnIdWhenSettingPortError_ObjectIdentity = ObjectIdentity
hm2TttdpWrongEtbnIdWhenSettingPortError = _Hm2TttdpWrongEtbnIdWhenSettingPortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 3, 1)
)
if mibBuilder.loadTexts:
    hm2TttdpWrongEtbnIdWhenSettingPortError.setStatus("current")
_Hm2TttdpChangeSettingWhileTttdpEnabledError_ObjectIdentity = ObjectIdentity
hm2TttdpChangeSettingWhileTttdpEnabledError = _Hm2TttdpChangeSettingWhileTttdpEnabledError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 3, 2)
)
if mibBuilder.loadTexts:
    hm2TttdpChangeSettingWhileTttdpEnabledError.setStatus("current")
_Hm2TttdpEnableTtdpButLagsNotCreatedError_ObjectIdentity = ObjectIdentity
hm2TttdpEnableTtdpButLagsNotCreatedError = _Hm2TttdpEnableTtdpButLagsNotCreatedError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 3, 3)
)
if mibBuilder.loadTexts:
    hm2TttdpEnableTtdpButLagsNotCreatedError.setStatus("current")
_Hm2TttdpAddConsistNetworkToSwitchError_ObjectIdentity = ObjectIdentity
hm2TttdpAddConsistNetworkToSwitchError = _Hm2TttdpAddConsistNetworkToSwitchError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 130, 3, 4)
)
if mibBuilder.loadTexts:
    hm2TttdpAddConsistNetworkToSwitchError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-ETB-MIB",
    **{"Hm2CstUuid": Hm2CstUuid,
       "hm2EtbMib": hm2EtbMib,
       "hm2EtbMibObjects": hm2EtbMibObjects,
       "hm2TtdpGroup": hm2TtdpGroup,
       "hm2TtdpAdminState": hm2TtdpAdminState,
       "hm2TtdpOperState": hm2TtdpOperState,
       "hm2TtdpCstCnCnt": hm2TtdpCstCnCnt,
       "hm2TtdpCstEtbnCnt": hm2TtdpCstEtbnCnt,
       "hm2TtdpCstUuid": hm2TtdpCstUuid,
       "hm2TtdpCstCurrentEtbnNumber": hm2TtdpCstCurrentEtbnNumber,
       "hm2TtdpBackboneId": hm2TtdpBackboneId,
       "hm2TtdpLocalEtbnInhibit": hm2TtdpLocalEtbnInhibit,
       "hm2TtdpETBNRole": hm2TtdpETBNRole,
       "hm2TtdpCnToEtbnTable": hm2TtdpCnToEtbnTable,
       "hm2TtdpCnToEtbnEntry": hm2TtdpCnToEtbnEntry,
       "hm2TtdpCnToEtbnTableIdx": hm2TtdpCnToEtbnTableIdx,
       "hm2TtdpCnToEtbnCnTableIdx": hm2TtdpCnToEtbnCnTableIdx,
       "hm2TtdpCnToEtbnIntf": hm2TtdpCnToEtbnIntf,
       "hm2TtdpCnToEtbnUseDHCPServer": hm2TtdpCnToEtbnUseDHCPServer,
       "hm2TtdpCnToEtbnRowStatus": hm2TtdpCnToEtbnRowStatus,
       "hm2EtbMibSNMPExtensionGroup": hm2EtbMibSNMPExtensionGroup,
       "hm2TttdpWrongEtbnIdWhenSettingPortError": hm2TttdpWrongEtbnIdWhenSettingPortError,
       "hm2TttdpChangeSettingWhileTttdpEnabledError": hm2TttdpChangeSettingWhileTttdpEnabledError,
       "hm2TttdpEnableTtdpButLagsNotCreatedError": hm2TttdpEnableTtdpButLagsNotCreatedError,
       "hm2TttdpAddConsistNetworkToSwitchError": hm2TttdpAddConsistNetworkToSwitchError}
)
