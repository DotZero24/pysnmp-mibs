# SNMP MIB module (SPECTRA-LOGIC-STRATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/spectralogic/SPECTRA-LOGIC-STRATA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:28 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

spectralogic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3478)
)
if mibBuilder.loadTexts:
    spectralogic.setRevisions(
        ("2016-10-31 00:00",
         "2016-03-04 00:00",
         "2015-02-04 00:00",
         "2014-05-05 00:00",
         "2012-11-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class KBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class MBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class GBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SpectraLogicStrataEventSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("info", 2),
          ("warning", 3),
          ("error", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Strata_ObjectIdentity = ObjectIdentity
strata = _Strata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1)
)
_CUsers_ObjectIdentity = ObjectIdentity
cUsers = _CUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1)
)
_CUserTable_Object = MibTable
cUserTable = _CUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cUserTable.setStatus("current")
_CUserEntry_Object = MibTableRow
cUserEntry = _CUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1, 1)
)
cUserEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cUserIndex"),
)
if mibBuilder.loadTexts:
    cUserEntry.setStatus("current")


class _CUserIndex_Type(Integer32):
    """Custom type cUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CUserIndex_Type.__name__ = "Integer32"
_CUserIndex_Object = MibTableColumn
cUserIndex = _CUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1, 1, 1),
    _CUserIndex_Type()
)
cUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cUserIndex.setStatus("current")
_CUserID_Type = DisplayString
_CUserID_Object = MibTableColumn
cUserID = _CUserID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1, 1, 2),
    _CUserID_Type()
)
cUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUserID.setStatus("current")
_CUserUsername_Type = DisplayString
_CUserUsername_Object = MibTableColumn
cUserUsername = _CUserUsername_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1, 1, 3),
    _CUserUsername_Type()
)
cUserUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUserUsername.setStatus("current")
_CUserFullname_Type = DisplayString
_CUserFullname_Object = MibTableColumn
cUserFullname = _CUserFullname_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1, 1, 4),
    _CUserFullname_Type()
)
cUserFullname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUserFullname.setStatus("current")
_CUserRole_Type = DisplayString
_CUserRole_Object = MibTableColumn
cUserRole = _CUserRole_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 1, 1, 1, 5),
    _CUserRole_Type()
)
cUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cUserRole.setStatus("current")
_CNetworkInterfaces_ObjectIdentity = ObjectIdentity
cNetworkInterfaces = _CNetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2)
)
_CNetworkInterfaceTable_Object = MibTable
cNetworkInterfaceTable = _CNetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cNetworkInterfaceTable.setStatus("current")
_CNetworkInterfaceEntry_Object = MibTableRow
cNetworkInterfaceEntry = _CNetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1)
)
cNetworkInterfaceEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cNetworkInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cNetworkInterfaceEntry.setStatus("current")


class _CNetworkInterfaceIndex_Type(Integer32):
    """Custom type cNetworkInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CNetworkInterfaceIndex_Type.__name__ = "Integer32"
_CNetworkInterfaceIndex_Object = MibTableColumn
cNetworkInterfaceIndex = _CNetworkInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 1),
    _CNetworkInterfaceIndex_Type()
)
cNetworkInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cNetworkInterfaceIndex.setStatus("current")
_CNetworkInterfaceID_Type = DisplayString
_CNetworkInterfaceID_Object = MibTableColumn
cNetworkInterfaceID = _CNetworkInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 2),
    _CNetworkInterfaceID_Type()
)
cNetworkInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceID.setStatus("current")
_CNetworkInterfaceName_Type = DisplayString
_CNetworkInterfaceName_Object = MibTableColumn
cNetworkInterfaceName = _CNetworkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 3),
    _CNetworkInterfaceName_Type()
)
cNetworkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceName.setStatus("current")
_CNetworkInterfaceLinkStatus_Type = DisplayString
_CNetworkInterfaceLinkStatus_Object = MibTableColumn
cNetworkInterfaceLinkStatus = _CNetworkInterfaceLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 4),
    _CNetworkInterfaceLinkStatus_Type()
)
cNetworkInterfaceLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceLinkStatus.setStatus("current")
_CNetworkInterfaceIPAddress_Type = DisplayString
_CNetworkInterfaceIPAddress_Object = MibTableColumn
cNetworkInterfaceIPAddress = _CNetworkInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 5),
    _CNetworkInterfaceIPAddress_Type()
)
cNetworkInterfaceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceIPAddress.setStatus("current")
_CNetworkInterfaceNetmask_Type = DisplayString
_CNetworkInterfaceNetmask_Object = MibTableColumn
cNetworkInterfaceNetmask = _CNetworkInterfaceNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 6),
    _CNetworkInterfaceNetmask_Type()
)
cNetworkInterfaceNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceNetmask.setStatus("current")
_CNetworkInterfaceDefaultGateway_Type = DisplayString
_CNetworkInterfaceDefaultGateway_Object = MibTableColumn
cNetworkInterfaceDefaultGateway = _CNetworkInterfaceDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 7),
    _CNetworkInterfaceDefaultGateway_Type()
)
cNetworkInterfaceDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceDefaultGateway.setStatus("current")
_CNetworkInterfaceDHCP_Type = DisplayString
_CNetworkInterfaceDHCP_Object = MibTableColumn
cNetworkInterfaceDHCP = _CNetworkInterfaceDHCP_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 8),
    _CNetworkInterfaceDHCP_Type()
)
cNetworkInterfaceDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceDHCP.setStatus("current")
_CNetworkInterfaceMACAddress_Type = DisplayString
_CNetworkInterfaceMACAddress_Object = MibTableColumn
cNetworkInterfaceMACAddress = _CNetworkInterfaceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 10),
    _CNetworkInterfaceMACAddress_Type()
)
cNetworkInterfaceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceMACAddress.setStatus("current")
_CNetworkInterfaceMTU_Type = Integer32
_CNetworkInterfaceMTU_Object = MibTableColumn
cNetworkInterfaceMTU = _CNetworkInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 2, 1, 1, 11),
    _CNetworkInterfaceMTU_Type()
)
cNetworkInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNetworkInterfaceMTU.setStatus("current")
_CTimeManagement_ObjectIdentity = ObjectIdentity
cTimeManagement = _CTimeManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3)
)
_CNTPTable_Object = MibTable
cNTPTable = _CNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cNTPTable.setStatus("current")
_CNTPEntry_Object = MibTableRow
cNTPEntry = _CNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1, 1)
)
cNTPEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cNTPIndex"),
)
if mibBuilder.loadTexts:
    cNTPEntry.setStatus("current")


class _CNTPIndex_Type(Integer32):
    """Custom type cNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CNTPIndex_Type.__name__ = "Integer32"
_CNTPIndex_Object = MibTableColumn
cNTPIndex = _CNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1, 1, 1),
    _CNTPIndex_Type()
)
cNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cNTPIndex.setStatus("current")
_CNTPEnabled_Type = TruthValue
_CNTPEnabled_Object = MibTableColumn
cNTPEnabled = _CNTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1, 1, 2),
    _CNTPEnabled_Type()
)
cNTPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNTPEnabled.setStatus("current")
_CNTPAddress1_Type = DisplayString
_CNTPAddress1_Object = MibTableColumn
cNTPAddress1 = _CNTPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1, 1, 3),
    _CNTPAddress1_Type()
)
cNTPAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNTPAddress1.setStatus("current")
_CNTPAddress2_Type = DisplayString
_CNTPAddress2_Object = MibTableColumn
cNTPAddress2 = _CNTPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1, 1, 4),
    _CNTPAddress2_Type()
)
cNTPAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNTPAddress2.setStatus("current")
_CNTPSynchronized_Type = DisplayString
_CNTPSynchronized_Object = MibTableColumn
cNTPSynchronized = _CNTPSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 3, 1, 1, 5),
    _CNTPSynchronized_Type()
)
cNTPSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNTPSynchronized.setStatus("current")
_CLogs_ObjectIdentity = ObjectIdentity
cLogs = _CLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4)
)
_CLogTable_Object = MibTable
cLogTable = _CLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLogTable.setStatus("current")
_CLogEntry_Object = MibTableRow
cLogEntry = _CLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4, 1, 1)
)
cLogEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cLogIndex"),
)
if mibBuilder.loadTexts:
    cLogEntry.setStatus("current")


class _CLogIndex_Type(Integer32):
    """Custom type cLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CLogIndex_Type.__name__ = "Integer32"
_CLogIndex_Object = MibTableColumn
cLogIndex = _CLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4, 1, 1, 1),
    _CLogIndex_Type()
)
cLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLogIndex.setStatus("current")
_CLogID_Type = DisplayString
_CLogID_Object = MibTableColumn
cLogID = _CLogID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4, 1, 1, 2),
    _CLogID_Type()
)
cLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLogID.setStatus("current")
_CLogCreationDate_Type = DateAndTime
_CLogCreationDate_Object = MibTableColumn
cLogCreationDate = _CLogCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4, 1, 1, 3),
    _CLogCreationDate_Type()
)
cLogCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLogCreationDate.setStatus("current")
_CLogSize_Type = KBytes
_CLogSize_Object = MibTableColumn
cLogSize = _CLogSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 1, 4, 1, 1, 4),
    _CLogSize_Type()
)
cLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLogSize.setStatus("current")
if mibBuilder.loadTexts:
    cLogSize.setUnits("KBytes")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2)
)
_CPools_ObjectIdentity = ObjectIdentity
cPools = _CPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1)
)
_CPoolTable_Object = MibTable
cPoolTable = _CPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cPoolTable.setStatus("current")
_CPoolEntry_Object = MibTableRow
cPoolEntry = _CPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1)
)
cPoolEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cPoolIndex"),
)
if mibBuilder.loadTexts:
    cPoolEntry.setStatus("current")


class _CPoolIndex_Type(Integer32):
    """Custom type cPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CPoolIndex_Type.__name__ = "Integer32"
_CPoolIndex_Object = MibTableColumn
cPoolIndex = _CPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 1),
    _CPoolIndex_Type()
)
cPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPoolIndex.setStatus("current")
_CPoolID_Type = DisplayString
_CPoolID_Object = MibTableColumn
cPoolID = _CPoolID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 2),
    _CPoolID_Type()
)
cPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolID.setStatus("current")
_CPoolName_Type = DisplayString
_CPoolName_Object = MibTableColumn
cPoolName = _CPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 3),
    _CPoolName_Type()
)
cPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolName.setStatus("current")
_CPoolCreationDate_Type = DateAndTime
_CPoolCreationDate_Object = MibTableColumn
cPoolCreationDate = _CPoolCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 4),
    _CPoolCreationDate_Type()
)
cPoolCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolCreationDate.setStatus("current")
_CPoolRawSize_Type = GBytes
_CPoolRawSize_Object = MibTableColumn
cPoolRawSize = _CPoolRawSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 5),
    _CPoolRawSize_Type()
)
cPoolRawSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolRawSize.setStatus("current")
if mibBuilder.loadTexts:
    cPoolRawSize.setUnits("GBytes")
_CPoolAvailableSize_Type = GBytes
_CPoolAvailableSize_Object = MibTableColumn
cPoolAvailableSize = _CPoolAvailableSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 6),
    _CPoolAvailableSize_Type()
)
cPoolAvailableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolAvailableSize.setStatus("current")
if mibBuilder.loadTexts:
    cPoolAvailableSize.setUnits("GBytes")
_CPoolUsedSize_Type = GBytes
_CPoolUsedSize_Object = MibTableColumn
cPoolUsedSize = _CPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 7),
    _CPoolUsedSize_Type()
)
cPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolUsedSize.setStatus("current")
if mibBuilder.loadTexts:
    cPoolUsedSize.setUnits("GBytes")
_CPoolOverheadSize_Type = GBytes
_CPoolOverheadSize_Object = MibTableColumn
cPoolOverheadSize = _CPoolOverheadSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 8),
    _CPoolOverheadSize_Type()
)
cPoolOverheadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolOverheadSize.setStatus("current")
if mibBuilder.loadTexts:
    cPoolOverheadSize.setUnits("GBytes")
_CPoolProtectionLevel_Type = DisplayString
_CPoolProtectionLevel_Object = MibTableColumn
cPoolProtectionLevel = _CPoolProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 9),
    _CPoolProtectionLevel_Type()
)
cPoolProtectionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolProtectionLevel.setStatus("current")
_CPoolNumberOfDiskArrays_Type = Integer32
_CPoolNumberOfDiskArrays_Object = MibTableColumn
cPoolNumberOfDiskArrays = _CPoolNumberOfDiskArrays_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 10),
    _CPoolNumberOfDiskArrays_Type()
)
cPoolNumberOfDiskArrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolNumberOfDiskArrays.setStatus("current")
_CPoolStatus_Type = DisplayString
_CPoolStatus_Object = MibTableColumn
cPoolStatus = _CPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 11),
    _CPoolStatus_Type()
)
cPoolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolStatus.setStatus("current")
_CPoolHighWaterMark_Type = Integer32
_CPoolHighWaterMark_Object = MibTableColumn
cPoolHighWaterMark = _CPoolHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 1, 1, 1, 12),
    _CPoolHighWaterMark_Type()
)
cPoolHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPoolHighWaterMark.setStatus("current")
_CVolumes_ObjectIdentity = ObjectIdentity
cVolumes = _CVolumes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2)
)
_CVolumeTable_Object = MibTable
cVolumeTable = _CVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cVolumeTable.setStatus("current")
_CVolumeEntry_Object = MibTableRow
cVolumeEntry = _CVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1)
)
cVolumeEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cVolumeIndex"),
)
if mibBuilder.loadTexts:
    cVolumeEntry.setStatus("current")


class _CVolumeIndex_Type(Integer32):
    """Custom type cVolumeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CVolumeIndex_Type.__name__ = "Integer32"
_CVolumeIndex_Object = MibTableColumn
cVolumeIndex = _CVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 1),
    _CVolumeIndex_Type()
)
cVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVolumeIndex.setStatus("current")
_CVolumeID_Type = DisplayString
_CVolumeID_Object = MibTableColumn
cVolumeID = _CVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 2),
    _CVolumeID_Type()
)
cVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeID.setStatus("current")
_CVolumeName_Type = DisplayString
_CVolumeName_Object = MibTableColumn
cVolumeName = _CVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 3),
    _CVolumeName_Type()
)
cVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeName.setStatus("current")
_CVolumePoolID_Type = DisplayString
_CVolumePoolID_Object = MibTableColumn
cVolumePoolID = _CVolumePoolID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 4),
    _CVolumePoolID_Type()
)
cVolumePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumePoolID.setStatus("current")
_CVolumePoolName_Type = DisplayString
_CVolumePoolName_Object = MibTableColumn
cVolumePoolName = _CVolumePoolName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 5),
    _CVolumePoolName_Type()
)
cVolumePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumePoolName.setStatus("current")
_CVolumeCreationDate_Type = DateAndTime
_CVolumeCreationDate_Object = MibTableColumn
cVolumeCreationDate = _CVolumeCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 6),
    _CVolumeCreationDate_Type()
)
cVolumeCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeCreationDate.setStatus("current")
_CVolumeMaximumSize_Type = GBytes
_CVolumeMaximumSize_Object = MibTableColumn
cVolumeMaximumSize = _CVolumeMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 7),
    _CVolumeMaximumSize_Type()
)
cVolumeMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeMaximumSize.setStatus("current")
if mibBuilder.loadTexts:
    cVolumeMaximumSize.setUnits("GBytes")
_CVolumeMinimumSize_Type = GBytes
_CVolumeMinimumSize_Object = MibTableColumn
cVolumeMinimumSize = _CVolumeMinimumSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 8),
    _CVolumeMinimumSize_Type()
)
cVolumeMinimumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeMinimumSize.setStatus("current")
if mibBuilder.loadTexts:
    cVolumeMinimumSize.setUnits("GBytes")
_CVolumeUsedSpace_Type = GBytes
_CVolumeUsedSpace_Object = MibTableColumn
cVolumeUsedSpace = _CVolumeUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 9),
    _CVolumeUsedSpace_Type()
)
cVolumeUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    cVolumeUsedSpace.setUnits("GBytes")
_CVolumeCompressionEnabled_Type = TruthValue
_CVolumeCompressionEnabled_Object = MibTableColumn
cVolumeCompressionEnabled = _CVolumeCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 10),
    _CVolumeCompressionEnabled_Type()
)
cVolumeCompressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeCompressionEnabled.setStatus("current")
_CVolumeReadOnly_Type = TruthValue
_CVolumeReadOnly_Object = MibTableColumn
cVolumeReadOnly = _CVolumeReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 11),
    _CVolumeReadOnly_Type()
)
cVolumeReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeReadOnly.setStatus("current")
_CVolumeAtimeEnabled_Type = TruthValue
_CVolumeAtimeEnabled_Object = MibTableColumn
cVolumeAtimeEnabled = _CVolumeAtimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 1, 1, 12),
    _CVolumeAtimeEnabled_Type()
)
cVolumeAtimeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVolumeAtimeEnabled.setStatus("current")
_CSnapshotTable_Object = MibTable
cSnapshotTable = _CSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cSnapshotTable.setStatus("current")
_CSnapshotEntry_Object = MibTableRow
cSnapshotEntry = _CSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1)
)
cSnapshotEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cSnapshotIndex"),
)
if mibBuilder.loadTexts:
    cSnapshotEntry.setStatus("current")


class _CSnapshotIndex_Type(Integer32):
    """Custom type cSnapshotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CSnapshotIndex_Type.__name__ = "Integer32"
_CSnapshotIndex_Object = MibTableColumn
cSnapshotIndex = _CSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1, 1),
    _CSnapshotIndex_Type()
)
cSnapshotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSnapshotIndex.setStatus("current")
_CSnapshotID_Type = DisplayString
_CSnapshotID_Object = MibTableColumn
cSnapshotID = _CSnapshotID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1, 2),
    _CSnapshotID_Type()
)
cSnapshotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotID.setStatus("current")
_CSnapshotName_Type = DisplayString
_CSnapshotName_Object = MibTableColumn
cSnapshotName = _CSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1, 3),
    _CSnapshotName_Type()
)
cSnapshotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotName.setStatus("current")
_CSnapshotVolumeID_Type = DisplayString
_CSnapshotVolumeID_Object = MibTableColumn
cSnapshotVolumeID = _CSnapshotVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1, 4),
    _CSnapshotVolumeID_Type()
)
cSnapshotVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotVolumeID.setStatus("current")
_CSnapshotCreationDate_Type = DateAndTime
_CSnapshotCreationDate_Object = MibTableColumn
cSnapshotCreationDate = _CSnapshotCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1, 5),
    _CSnapshotCreationDate_Type()
)
cSnapshotCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotCreationDate.setStatus("current")
_CSnapshotSize_Type = Integer32
_CSnapshotSize_Object = MibTableColumn
cSnapshotSize = _CSnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 2, 1, 6),
    _CSnapshotSize_Type()
)
cSnapshotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotSize.setStatus("current")
_CSnapshotScheduleTable_Object = MibTable
cSnapshotScheduleTable = _CSnapshotScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cSnapshotScheduleTable.setStatus("current")
_CSnapshotScheduleEntry_Object = MibTableRow
cSnapshotScheduleEntry = _CSnapshotScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1)
)
cSnapshotScheduleEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cSnapshotScheduleIndex"),
)
if mibBuilder.loadTexts:
    cSnapshotScheduleEntry.setStatus("current")


class _CSnapshotScheduleIndex_Type(Integer32):
    """Custom type cSnapshotScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CSnapshotScheduleIndex_Type.__name__ = "Integer32"
_CSnapshotScheduleIndex_Object = MibTableColumn
cSnapshotScheduleIndex = _CSnapshotScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 1),
    _CSnapshotScheduleIndex_Type()
)
cSnapshotScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSnapshotScheduleIndex.setStatus("current")
_CSnapshotScheduleID_Type = DisplayString
_CSnapshotScheduleID_Object = MibTableColumn
cSnapshotScheduleID = _CSnapshotScheduleID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 2),
    _CSnapshotScheduleID_Type()
)
cSnapshotScheduleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleID.setStatus("current")
_CSnapshotScheduleName_Type = DisplayString
_CSnapshotScheduleName_Object = MibTableColumn
cSnapshotScheduleName = _CSnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 3),
    _CSnapshotScheduleName_Type()
)
cSnapshotScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleName.setStatus("current")
_CSnapshotScheduleVolumeID_Type = DisplayString
_CSnapshotScheduleVolumeID_Object = MibTableColumn
cSnapshotScheduleVolumeID = _CSnapshotScheduleVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 4),
    _CSnapshotScheduleVolumeID_Type()
)
cSnapshotScheduleVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleVolumeID.setStatus("current")
_CSnapshotScheduleMaximumNumberOfSnapshots_Type = DisplayString
_CSnapshotScheduleMaximumNumberOfSnapshots_Object = MibTableColumn
cSnapshotScheduleMaximumNumberOfSnapshots = _CSnapshotScheduleMaximumNumberOfSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 5),
    _CSnapshotScheduleMaximumNumberOfSnapshots_Type()
)
cSnapshotScheduleMaximumNumberOfSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleMaximumNumberOfSnapshots.setStatus("current")
_CSnapshotScheduleCronString_Type = DisplayString
_CSnapshotScheduleCronString_Object = MibTableColumn
cSnapshotScheduleCronString = _CSnapshotScheduleCronString_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 6),
    _CSnapshotScheduleCronString_Type()
)
cSnapshotScheduleCronString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleCronString.setStatus("current")
_CSnapshotScheduleStartTime_Type = DisplayString
_CSnapshotScheduleStartTime_Object = MibTableColumn
cSnapshotScheduleStartTime = _CSnapshotScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 7),
    _CSnapshotScheduleStartTime_Type()
)
cSnapshotScheduleStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleStartTime.setStatus("current")
_CSnapshotScheduleFrequency_Type = DisplayString
_CSnapshotScheduleFrequency_Object = MibTableColumn
cSnapshotScheduleFrequency = _CSnapshotScheduleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 8),
    _CSnapshotScheduleFrequency_Type()
)
cSnapshotScheduleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleFrequency.setStatus("current")
_CSnapshotScheduleRepeatInterval_Type = DisplayString
_CSnapshotScheduleRepeatInterval_Object = MibTableColumn
cSnapshotScheduleRepeatInterval = _CSnapshotScheduleRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 3, 1, 9),
    _CSnapshotScheduleRepeatInterval_Type()
)
cSnapshotScheduleRepeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSnapshotScheduleRepeatInterval.setStatus("current")
_CCIFSShareTable_Object = MibTable
cCIFSShareTable = _CCIFSShareTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cCIFSShareTable.setStatus("current")
_CCIFSShareEntry_Object = MibTableRow
cCIFSShareEntry = _CCIFSShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4, 1)
)
cCIFSShareEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cCIFSShareIndex"),
)
if mibBuilder.loadTexts:
    cCIFSShareEntry.setStatus("current")


class _CCIFSShareIndex_Type(Integer32):
    """Custom type cCIFSShareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CCIFSShareIndex_Type.__name__ = "Integer32"
_CCIFSShareIndex_Object = MibTableColumn
cCIFSShareIndex = _CCIFSShareIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4, 1, 1),
    _CCIFSShareIndex_Type()
)
cCIFSShareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCIFSShareIndex.setStatus("current")
_CCIFSShareID_Type = DisplayString
_CCIFSShareID_Object = MibTableColumn
cCIFSShareID = _CCIFSShareID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4, 1, 2),
    _CCIFSShareID_Type()
)
cCIFSShareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCIFSShareID.setStatus("current")
_CCIFSShareName_Type = DisplayString
_CCIFSShareName_Object = MibTableColumn
cCIFSShareName = _CCIFSShareName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4, 1, 3),
    _CCIFSShareName_Type()
)
cCIFSShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCIFSShareName.setStatus("current")
_CCIFSSharePath_Type = DisplayString
_CCIFSSharePath_Object = MibTableColumn
cCIFSSharePath = _CCIFSSharePath_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4, 1, 4),
    _CCIFSSharePath_Type()
)
cCIFSSharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCIFSSharePath.setStatus("current")
_CCIFSShareReadOnly_Type = DisplayString
_CCIFSShareReadOnly_Object = MibTableColumn
cCIFSShareReadOnly = _CCIFSShareReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 4, 1, 5),
    _CCIFSShareReadOnly_Type()
)
cCIFSShareReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCIFSShareReadOnly.setStatus("current")
_CNFSShareTable_Object = MibTable
cNFSShareTable = _CNFSShareTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cNFSShareTable.setStatus("current")
_CNFSShareEntry_Object = MibTableRow
cNFSShareEntry = _CNFSShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1)
)
cNFSShareEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cNFSShareIndex"),
)
if mibBuilder.loadTexts:
    cNFSShareEntry.setStatus("current")


class _CNFSShareIndex_Type(Integer32):
    """Custom type cNFSShareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CNFSShareIndex_Type.__name__ = "Integer32"
_CNFSShareIndex_Object = MibTableColumn
cNFSShareIndex = _CNFSShareIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 1),
    _CNFSShareIndex_Type()
)
cNFSShareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cNFSShareIndex.setStatus("current")
_CNFSShareID_Type = DisplayString
_CNFSShareID_Object = MibTableColumn
cNFSShareID = _CNFSShareID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 2),
    _CNFSShareID_Type()
)
cNFSShareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSShareID.setStatus("current")
_CNFSShareMountPoint_Type = DisplayString
_CNFSShareMountPoint_Object = MibTableColumn
cNFSShareMountPoint = _CNFSShareMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 3),
    _CNFSShareMountPoint_Type()
)
cNFSShareMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSShareMountPoint.setStatus("current")
_CNFSSharePath_Type = DisplayString
_CNFSSharePath_Object = MibTableColumn
cNFSSharePath = _CNFSSharePath_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 4),
    _CNFSSharePath_Type()
)
cNFSSharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSSharePath.setStatus("current")
_CNFSShareAccessControl_Type = DisplayString
_CNFSShareAccessControl_Object = MibTableColumn
cNFSShareAccessControl = _CNFSShareAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 5),
    _CNFSShareAccessControl_Type()
)
cNFSShareAccessControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSShareAccessControl.setStatus("current")
_CNFSShareAnonymousUUID_Type = DisplayString
_CNFSShareAnonymousUUID_Object = MibTableColumn
cNFSShareAnonymousUUID = _CNFSShareAnonymousUUID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 6),
    _CNFSShareAnonymousUUID_Type()
)
cNFSShareAnonymousUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSShareAnonymousUUID.setStatus("current")
_CNFSShareComment_Type = DisplayString
_CNFSShareComment_Object = MibTableColumn
cNFSShareComment = _CNFSShareComment_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 2, 2, 5, 1, 7),
    _CNFSShareComment_Type()
)
cNFSShareComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSShareComment.setStatus("current")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3)
)
_CNFSServiceTable_Object = MibTable
cNFSServiceTable = _CNFSServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cNFSServiceTable.setStatus("current")
_CNFSServiceEntry_Object = MibTableRow
cNFSServiceEntry = _CNFSServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1)
)
cNFSServiceEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cNFSServiceIndex"),
)
if mibBuilder.loadTexts:
    cNFSServiceEntry.setStatus("current")


class _CNFSServiceIndex_Type(Integer32):
    """Custom type cNFSServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CNFSServiceIndex_Type.__name__ = "Integer32"
_CNFSServiceIndex_Object = MibTableColumn
cNFSServiceIndex = _CNFSServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1, 1),
    _CNFSServiceIndex_Type()
)
cNFSServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cNFSServiceIndex.setStatus("current")
_CNFSServiceID_Type = DisplayString
_CNFSServiceID_Object = MibTableColumn
cNFSServiceID = _CNFSServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1, 2),
    _CNFSServiceID_Type()
)
cNFSServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSServiceID.setStatus("current")
_CNFSServiceStatus_Type = DisplayString
_CNFSServiceStatus_Object = MibTableColumn
cNFSServiceStatus = _CNFSServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1, 3),
    _CNFSServiceStatus_Type()
)
cNFSServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSServiceStatus.setStatus("current")
_CNFSServiceTcpEnabled_Type = DisplayString
_CNFSServiceTcpEnabled_Object = MibTableColumn
cNFSServiceTcpEnabled = _CNFSServiceTcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1, 4),
    _CNFSServiceTcpEnabled_Type()
)
cNFSServiceTcpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSServiceTcpEnabled.setStatus("current")
_CNFSServiceUdpEnabled_Type = DisplayString
_CNFSServiceUdpEnabled_Object = MibTableColumn
cNFSServiceUdpEnabled = _CNFSServiceUdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1, 5),
    _CNFSServiceUdpEnabled_Type()
)
cNFSServiceUdpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSServiceUdpEnabled.setStatus("current")
_CNFSServiceThreads_Type = Integer32
_CNFSServiceThreads_Object = MibTableColumn
cNFSServiceThreads = _CNFSServiceThreads_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 1, 1, 6),
    _CNFSServiceThreads_Type()
)
cNFSServiceThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNFSServiceThreads.setStatus("current")
_CADServiceTable_Object = MibTable
cADServiceTable = _CADServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cADServiceTable.setStatus("current")
_CADServiceEntry_Object = MibTableRow
cADServiceEntry = _CADServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1)
)
cADServiceEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cADServiceIndex"),
)
if mibBuilder.loadTexts:
    cADServiceEntry.setStatus("current")


class _CADServiceIndex_Type(Integer32):
    """Custom type cADServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CADServiceIndex_Type.__name__ = "Integer32"
_CADServiceIndex_Object = MibTableColumn
cADServiceIndex = _CADServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1, 1),
    _CADServiceIndex_Type()
)
cADServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cADServiceIndex.setStatus("current")
_CADServiceID_Type = DisplayString
_CADServiceID_Object = MibTableColumn
cADServiceID = _CADServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1, 2),
    _CADServiceID_Type()
)
cADServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cADServiceID.setStatus("current")
_CADServiceStatus_Type = DisplayString
_CADServiceStatus_Object = MibTableColumn
cADServiceStatus = _CADServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1, 3),
    _CADServiceStatus_Type()
)
cADServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cADServiceStatus.setStatus("current")
_CADServiceActiveDirectoryJoined_Type = TruthValue
_CADServiceActiveDirectoryJoined_Object = MibTableColumn
cADServiceActiveDirectoryJoined = _CADServiceActiveDirectoryJoined_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1, 4),
    _CADServiceActiveDirectoryJoined_Type()
)
cADServiceActiveDirectoryJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cADServiceActiveDirectoryJoined.setStatus("current")
_CADServiceHostname_Type = DisplayString
_CADServiceHostname_Object = MibTableColumn
cADServiceHostname = _CADServiceHostname_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1, 5),
    _CADServiceHostname_Type()
)
cADServiceHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cADServiceHostname.setStatus("current")
_CADServiceDnsDomainName_Type = DisplayString
_CADServiceDnsDomainName_Object = MibTableColumn
cADServiceDnsDomainName = _CADServiceDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 2, 1, 6),
    _CADServiceDnsDomainName_Type()
)
cADServiceDnsDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cADServiceDnsDomainName.setStatus("current")
_CSNMPService_ObjectIdentity = ObjectIdentity
cSNMPService = _CSNMPService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3)
)
_CSNMPClientTable_Object = MibTable
cSNMPClientTable = _CSNMPClientTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cSNMPClientTable.setStatus("current")
_CSNMPClientEntry_Object = MibTableRow
cSNMPClientEntry = _CSNMPClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1, 1)
)
cSNMPClientEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "cSNMPClientIndex"),
)
if mibBuilder.loadTexts:
    cSNMPClientEntry.setStatus("current")


class _CSNMPClientIndex_Type(Integer32):
    """Custom type cSNMPClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CSNMPClientIndex_Type.__name__ = "Integer32"
_CSNMPClientIndex_Object = MibTableColumn
cSNMPClientIndex = _CSNMPClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1, 1, 1),
    _CSNMPClientIndex_Type()
)
cSNMPClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSNMPClientIndex.setStatus("current")
_CSNMPClientHost_Type = DisplayString
_CSNMPClientHost_Object = MibTableColumn
cSNMPClientHost = _CSNMPClientHost_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1, 1, 2),
    _CSNMPClientHost_Type()
)
cSNMPClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSNMPClientHost.setStatus("current")
_CSNMPClientNotifications_Type = TruthValue
_CSNMPClientNotifications_Object = MibTableColumn
cSNMPClientNotifications = _CSNMPClientNotifications_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1, 1, 3),
    _CSNMPClientNotifications_Type()
)
cSNMPClientNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSNMPClientNotifications.setStatus("current")
_CSNMPClientPort_Type = Integer32
_CSNMPClientPort_Object = MibTableColumn
cSNMPClientPort = _CSNMPClientPort_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1, 1, 4),
    _CSNMPClientPort_Type()
)
cSNMPClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSNMPClientPort.setStatus("current")
_CSNMPClientCommunityString_Type = DisplayString
_CSNMPClientCommunityString_Object = MibTableColumn
cSNMPClientCommunityString = _CSNMPClientCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 1, 3, 3, 1, 1, 5),
    _CSNMPClientCommunityString_Type()
)
cSNMPClientCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSNMPClientCommunityString.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1)
)
_SChassisTable_Object = MibTable
sChassisTable = _SChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sChassisTable.setStatus("current")
_SChassisEntry_Object = MibTableRow
sChassisEntry = _SChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1)
)
sChassisEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sChassisIndex"),
)
if mibBuilder.loadTexts:
    sChassisEntry.setStatus("current")


class _SChassisIndex_Type(Integer32):
    """Custom type sChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SChassisIndex_Type.__name__ = "Integer32"
_SChassisIndex_Object = MibTableColumn
sChassisIndex = _SChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 1),
    _SChassisIndex_Type()
)
sChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sChassisIndex.setStatus("current")
_SChassisID_Type = DisplayString
_SChassisID_Object = MibTableColumn
sChassisID = _SChassisID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 2),
    _SChassisID_Type()
)
sChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisID.setStatus("current")
_SChassisType_Type = DisplayString
_SChassisType_Object = MibTableColumn
sChassisType = _SChassisType_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 3),
    _SChassisType_Type()
)
sChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisType.setStatus("current")
_SChassisStatus_Type = DisplayString
_SChassisStatus_Object = MibTableColumn
sChassisStatus = _SChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 4),
    _SChassisStatus_Type()
)
sChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisStatus.setStatus("current")
_SChassisModel_Type = DisplayString
_SChassisModel_Object = MibTableColumn
sChassisModel = _SChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 5),
    _SChassisModel_Type()
)
sChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisModel.setStatus("current")
_SChassisSerialNumber_Type = DisplayString
_SChassisSerialNumber_Object = MibTableColumn
sChassisSerialNumber = _SChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 6),
    _SChassisSerialNumber_Type()
)
sChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisSerialNumber.setStatus("current")
_SChassisMemory_Type = GBytes
_SChassisMemory_Object = MibTableColumn
sChassisMemory = _SChassisMemory_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 7),
    _SChassisMemory_Type()
)
sChassisMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisMemory.setStatus("current")
if mibBuilder.loadTexts:
    sChassisMemory.setUnits("GBytes")
_SChassisRawCapacity_Type = GBytes
_SChassisRawCapacity_Object = MibTableColumn
sChassisRawCapacity = _SChassisRawCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 1, 1, 8),
    _SChassisRawCapacity_Type()
)
sChassisRawCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sChassisRawCapacity.setStatus("current")
if mibBuilder.loadTexts:
    sChassisRawCapacity.setUnits("GBytes")
_SCPUTable_Object = MibTable
sCPUTable = _SCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sCPUTable.setStatus("current")
_SCPUEntry_Object = MibTableRow
sCPUEntry = _SCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2, 1)
)
sCPUEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sCPUIndex"),
)
if mibBuilder.loadTexts:
    sCPUEntry.setStatus("current")


class _SCPUIndex_Type(Integer32):
    """Custom type sCPUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SCPUIndex_Type.__name__ = "Integer32"
_SCPUIndex_Object = MibTableColumn
sCPUIndex = _SCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2, 1, 1),
    _SCPUIndex_Type()
)
sCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCPUIndex.setStatus("current")
_SCPUChassisID_Type = DisplayString
_SCPUChassisID_Object = MibTableColumn
sCPUChassisID = _SCPUChassisID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2, 1, 2),
    _SCPUChassisID_Type()
)
sCPUChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCPUChassisID.setStatus("current")
_SCPUSlot_Type = Integer32
_SCPUSlot_Object = MibTableColumn
sCPUSlot = _SCPUSlot_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2, 1, 3),
    _SCPUSlot_Type()
)
sCPUSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCPUSlot.setStatus("current")
_SCPUStatus_Type = DisplayString
_SCPUStatus_Object = MibTableColumn
sCPUStatus = _SCPUStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2, 1, 4),
    _SCPUStatus_Type()
)
sCPUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCPUStatus.setStatus("current")
_SCPUTemperature_Type = Integer32
_SCPUTemperature_Object = MibTableColumn
sCPUTemperature = _SCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 2, 1, 5),
    _SCPUTemperature_Type()
)
sCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCPUTemperature.setStatus("current")
_SBootDriveTable_Object = MibTable
sBootDriveTable = _SBootDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sBootDriveTable.setStatus("current")
_SBootDriveEntry_Object = MibTableRow
sBootDriveEntry = _SBootDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1)
)
sBootDriveEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sBootDriveIndex"),
)
if mibBuilder.loadTexts:
    sBootDriveEntry.setStatus("current")


class _SBootDriveIndex_Type(Integer32):
    """Custom type sBootDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SBootDriveIndex_Type.__name__ = "Integer32"
_SBootDriveIndex_Object = MibTableColumn
sBootDriveIndex = _SBootDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 1),
    _SBootDriveIndex_Type()
)
sBootDriveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sBootDriveIndex.setStatus("current")
_SBootDriveChassisID_Type = DisplayString
_SBootDriveChassisID_Object = MibTableColumn
sBootDriveChassisID = _SBootDriveChassisID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 2),
    _SBootDriveChassisID_Type()
)
sBootDriveChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveChassisID.setStatus("current")
_SBootDriveSlot_Type = Integer32
_SBootDriveSlot_Object = MibTableColumn
sBootDriveSlot = _SBootDriveSlot_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 3),
    _SBootDriveSlot_Type()
)
sBootDriveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveSlot.setStatus("current")
_SBootDriveStatus_Type = DisplayString
_SBootDriveStatus_Object = MibTableColumn
sBootDriveStatus = _SBootDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 4),
    _SBootDriveStatus_Type()
)
sBootDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveStatus.setStatus("current")
_SBootDriveManufacturer_Type = DisplayString
_SBootDriveManufacturer_Object = MibTableColumn
sBootDriveManufacturer = _SBootDriveManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 5),
    _SBootDriveManufacturer_Type()
)
sBootDriveManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveManufacturer.setStatus("current")
_SBootDriveModel_Type = DisplayString
_SBootDriveModel_Object = MibTableColumn
sBootDriveModel = _SBootDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 6),
    _SBootDriveModel_Type()
)
sBootDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveModel.setStatus("current")
_SBootDriveSize_Type = GBytes
_SBootDriveSize_Object = MibTableColumn
sBootDriveSize = _SBootDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 7),
    _SBootDriveSize_Type()
)
sBootDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveSize.setStatus("current")
if mibBuilder.loadTexts:
    sBootDriveSize.setUnits("GBytes")
_SBootDriveSerialNumber_Type = DisplayString
_SBootDriveSerialNumber_Object = MibTableColumn
sBootDriveSerialNumber = _SBootDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 3, 1, 8),
    _SBootDriveSerialNumber_Type()
)
sBootDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBootDriveSerialNumber.setStatus("current")
_SDataDriveTable_Object = MibTable
sDataDriveTable = _SDataDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sDataDriveTable.setStatus("current")
_SDataDriveEntry_Object = MibTableRow
sDataDriveEntry = _SDataDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1)
)
sDataDriveEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sDataDriveIndex"),
)
if mibBuilder.loadTexts:
    sDataDriveEntry.setStatus("current")


class _SDataDriveIndex_Type(Integer32):
    """Custom type sDataDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SDataDriveIndex_Type.__name__ = "Integer32"
_SDataDriveIndex_Object = MibTableColumn
sDataDriveIndex = _SDataDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 1),
    _SDataDriveIndex_Type()
)
sDataDriveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sDataDriveIndex.setStatus("current")
_SDataDriveChassis_Type = DisplayString
_SDataDriveChassis_Object = MibTableColumn
sDataDriveChassis = _SDataDriveChassis_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 2),
    _SDataDriveChassis_Type()
)
sDataDriveChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDriveChassis.setStatus("current")
_SDataDriveSlot_Type = Integer32
_SDataDriveSlot_Object = MibTableColumn
sDataDriveSlot = _SDataDriveSlot_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 3),
    _SDataDriveSlot_Type()
)
sDataDriveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDriveSlot.setStatus("current")
_SDataDriveStatus_Type = DisplayString
_SDataDriveStatus_Object = MibTableColumn
sDataDriveStatus = _SDataDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 4),
    _SDataDriveStatus_Type()
)
sDataDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDriveStatus.setStatus("current")
_SDataDriveSize_Type = GBytes
_SDataDriveSize_Object = MibTableColumn
sDataDriveSize = _SDataDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 5),
    _SDataDriveSize_Type()
)
sDataDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDriveSize.setStatus("current")
if mibBuilder.loadTexts:
    sDataDriveSize.setUnits("GBytes")
_SDataDriveSerialNumber_Type = DisplayString
_SDataDriveSerialNumber_Object = MibTableColumn
sDataDriveSerialNumber = _SDataDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 6),
    _SDataDriveSerialNumber_Type()
)
sDataDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDriveSerialNumber.setStatus("current")
_SDataDrivePoolID_Type = DisplayString
_SDataDrivePoolID_Object = MibTableColumn
sDataDrivePoolID = _SDataDrivePoolID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 7),
    _SDataDrivePoolID_Type()
)
sDataDrivePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDrivePoolID.setStatus("current")
_SDataDrivePoolName_Type = DisplayString
_SDataDrivePoolName_Object = MibTableColumn
sDataDrivePoolName = _SDataDrivePoolName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 4, 1, 8),
    _SDataDrivePoolName_Type()
)
sDataDrivePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDataDrivePoolName.setStatus("current")
_SFanTable_Object = MibTable
sFanTable = _SFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    sFanTable.setStatus("current")
_SFanEntry_Object = MibTableRow
sFanEntry = _SFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5, 1)
)
sFanEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sFanIndex"),
)
if mibBuilder.loadTexts:
    sFanEntry.setStatus("current")


class _SFanIndex_Type(Integer32):
    """Custom type sFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SFanIndex_Type.__name__ = "Integer32"
_SFanIndex_Object = MibTableColumn
sFanIndex = _SFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5, 1, 1),
    _SFanIndex_Type()
)
sFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFanIndex.setStatus("current")
_SFanChassisID_Type = DisplayString
_SFanChassisID_Object = MibTableColumn
sFanChassisID = _SFanChassisID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5, 1, 2),
    _SFanChassisID_Type()
)
sFanChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFanChassisID.setStatus("current")
_SFanSlot_Type = Integer32
_SFanSlot_Object = MibTableColumn
sFanSlot = _SFanSlot_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5, 1, 3),
    _SFanSlot_Type()
)
sFanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFanSlot.setStatus("current")
_SFanStatus_Type = DisplayString
_SFanStatus_Object = MibTableColumn
sFanStatus = _SFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5, 1, 4),
    _SFanStatus_Type()
)
sFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFanStatus.setStatus("current")
_SFanSpeed_Type = Integer32
_SFanSpeed_Object = MibTableColumn
sFanSpeed = _SFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 5, 1, 5),
    _SFanSpeed_Type()
)
sFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFanSpeed.setStatus("current")
_SPowerSupplyTable_Object = MibTable
sPowerSupplyTable = _SPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    sPowerSupplyTable.setStatus("current")
_SPowerSupplyEntry_Object = MibTableRow
sPowerSupplyEntry = _SPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7, 1)
)
sPowerSupplyEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    sPowerSupplyEntry.setStatus("current")


class _SPowerSupplyIndex_Type(Integer32):
    """Custom type sPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SPowerSupplyIndex_Type.__name__ = "Integer32"
_SPowerSupplyIndex_Object = MibTableColumn
sPowerSupplyIndex = _SPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7, 1, 1),
    _SPowerSupplyIndex_Type()
)
sPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sPowerSupplyIndex.setStatus("current")
_SPowerSupplyChassisID_Type = DisplayString
_SPowerSupplyChassisID_Object = MibTableColumn
sPowerSupplyChassisID = _SPowerSupplyChassisID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7, 1, 2),
    _SPowerSupplyChassisID_Type()
)
sPowerSupplyChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPowerSupplyChassisID.setStatus("current")
_SPowerSupplySlot_Type = Integer32
_SPowerSupplySlot_Object = MibTableColumn
sPowerSupplySlot = _SPowerSupplySlot_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7, 1, 3),
    _SPowerSupplySlot_Type()
)
sPowerSupplySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPowerSupplySlot.setStatus("current")
_SPowerSupplyStatus_Type = DisplayString
_SPowerSupplyStatus_Object = MibTableColumn
sPowerSupplyStatus = _SPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7, 1, 4),
    _SPowerSupplyStatus_Type()
)
sPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPowerSupplyStatus.setStatus("current")
_SPowerSupplyWatts_Type = Integer32
_SPowerSupplyWatts_Object = MibTableColumn
sPowerSupplyWatts = _SPowerSupplyWatts_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 7, 1, 5),
    _SPowerSupplyWatts_Type()
)
sPowerSupplyWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPowerSupplyWatts.setStatus("current")
_STapeDriveTable_Object = MibTable
sTapeDriveTable = _STapeDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8)
)
if mibBuilder.loadTexts:
    sTapeDriveTable.setStatus("current")
_STapeDriveEntry_Object = MibTableRow
sTapeDriveEntry = _STapeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1)
)
sTapeDriveEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "sTapeDriveIndex"),
)
if mibBuilder.loadTexts:
    sTapeDriveEntry.setStatus("current")


class _STapeDriveIndex_Type(Integer32):
    """Custom type sTapeDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_STapeDriveIndex_Type.__name__ = "Integer32"
_STapeDriveIndex_Object = MibTableColumn
sTapeDriveIndex = _STapeDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 1),
    _STapeDriveIndex_Type()
)
sTapeDriveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sTapeDriveIndex.setStatus("current")
_STapeDrivePartition_Type = DisplayString
_STapeDrivePartition_Object = MibTableColumn
sTapeDrivePartition = _STapeDrivePartition_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 2),
    _STapeDrivePartition_Type()
)
sTapeDrivePartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTapeDrivePartition.setStatus("current")
_STapeDriveStatus_Type = DisplayString
_STapeDriveStatus_Object = MibTableColumn
sTapeDriveStatus = _STapeDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 3),
    _STapeDriveStatus_Type()
)
sTapeDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTapeDriveStatus.setStatus("current")
_STapeDriveType_Type = DisplayString
_STapeDriveType_Object = MibTableColumn
sTapeDriveType = _STapeDriveType_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 4),
    _STapeDriveType_Type()
)
sTapeDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTapeDriveType.setStatus("current")
_STapeDriveSerialNumber_Type = DisplayString
_STapeDriveSerialNumber_Object = MibTableColumn
sTapeDriveSerialNumber = _STapeDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 5),
    _STapeDriveSerialNumber_Type()
)
sTapeDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTapeDriveSerialNumber.setStatus("current")
_STapeDriveTapeBarcode_Type = DisplayString
_STapeDriveTapeBarcode_Object = MibTableColumn
sTapeDriveTapeBarcode = _STapeDriveTapeBarcode_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 6),
    _STapeDriveTapeBarcode_Type()
)
sTapeDriveTapeBarcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTapeDriveTapeBarcode.setStatus("current")
_STapeDriveErrorMesssage_Type = DisplayString
_STapeDriveErrorMesssage_Object = MibScalar
sTapeDriveErrorMesssage = _STapeDriveErrorMesssage_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 2, 1, 8, 1, 7),
    _STapeDriveErrorMesssage_Type()
)
sTapeDriveErrorMesssage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTapeDriveErrorMesssage.setStatus("current")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3)
)
_PPoolStatistics_ObjectIdentity = ObjectIdentity
pPoolStatistics = _PPoolStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1)
)
_PPoolStatisticsTable_Object = MibTable
pPoolStatisticsTable = _PPoolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pPoolStatisticsTable.setStatus("current")
_PPoolStatisticsEntry_Object = MibTableRow
pPoolStatisticsEntry = _PPoolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1)
)
pPoolStatisticsEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "pPoolStatisticsIndex"),
)
if mibBuilder.loadTexts:
    pPoolStatisticsEntry.setStatus("current")


class _PPoolStatisticsIndex_Type(Integer32):
    """Custom type pPoolStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PPoolStatisticsIndex_Type.__name__ = "Integer32"
_PPoolStatisticsIndex_Object = MibTableColumn
pPoolStatisticsIndex = _PPoolStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 1),
    _PPoolStatisticsIndex_Type()
)
pPoolStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pPoolStatisticsIndex.setStatus("current")
_PPoolStatisticsPoolID_Type = DisplayString
_PPoolStatisticsPoolID_Object = MibTableColumn
pPoolStatisticsPoolID = _PPoolStatisticsPoolID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 2),
    _PPoolStatisticsPoolID_Type()
)
pPoolStatisticsPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsPoolID.setStatus("current")
_PPoolStatisticsPoolName_Type = DisplayString
_PPoolStatisticsPoolName_Object = MibTableColumn
pPoolStatisticsPoolName = _PPoolStatisticsPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 3),
    _PPoolStatisticsPoolName_Type()
)
pPoolStatisticsPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsPoolName.setStatus("current")
_PPoolStatisticsCollectionTime_Type = DisplayString
_PPoolStatisticsCollectionTime_Object = MibTableColumn
pPoolStatisticsCollectionTime = _PPoolStatisticsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 4),
    _PPoolStatisticsCollectionTime_Type()
)
pPoolStatisticsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsCollectionTime.setStatus("current")
_PPoolStatisticsReadIOPs_Type = DisplayString
_PPoolStatisticsReadIOPs_Object = MibTableColumn
pPoolStatisticsReadIOPs = _PPoolStatisticsReadIOPs_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 5),
    _PPoolStatisticsReadIOPs_Type()
)
pPoolStatisticsReadIOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsReadIOPs.setStatus("current")
_PPoolStatisticsWriteIOPs_Type = DisplayString
_PPoolStatisticsWriteIOPs_Object = MibTableColumn
pPoolStatisticsWriteIOPs = _PPoolStatisticsWriteIOPs_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 6),
    _PPoolStatisticsWriteIOPs_Type()
)
pPoolStatisticsWriteIOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsWriteIOPs.setStatus("current")
_PPoolStatisticsReadBytesPerSecond_Type = DisplayString
_PPoolStatisticsReadBytesPerSecond_Object = MibTableColumn
pPoolStatisticsReadBytesPerSecond = _PPoolStatisticsReadBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 7),
    _PPoolStatisticsReadBytesPerSecond_Type()
)
pPoolStatisticsReadBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsReadBytesPerSecond.setStatus("current")
_PPoolStatisticsWriteBytesPerSecond_Type = DisplayString
_PPoolStatisticsWriteBytesPerSecond_Object = MibTableColumn
pPoolStatisticsWriteBytesPerSecond = _PPoolStatisticsWriteBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 1, 1, 1, 8),
    _PPoolStatisticsWriteBytesPerSecond_Type()
)
pPoolStatisticsWriteBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPoolStatisticsWriteBytesPerSecond.setStatus("current")
_PDataDriveStatistics_ObjectIdentity = ObjectIdentity
pDataDriveStatistics = _PDataDriveStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2)
)
_PDataDriveStatisticsTable_Object = MibTable
pDataDriveStatisticsTable = _PDataDriveStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pDataDriveStatisticsTable.setStatus("current")
_PDataDriveStatisticsEntry_Object = MibTableRow
pDataDriveStatisticsEntry = _PDataDriveStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1)
)
pDataDriveStatisticsEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "pDataDriveStatisticsIndex"),
)
if mibBuilder.loadTexts:
    pDataDriveStatisticsEntry.setStatus("current")


class _PDataDriveStatisticsIndex_Type(Integer32):
    """Custom type pDataDriveStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PDataDriveStatisticsIndex_Type.__name__ = "Integer32"
_PDataDriveStatisticsIndex_Object = MibTableColumn
pDataDriveStatisticsIndex = _PDataDriveStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 1),
    _PDataDriveStatisticsIndex_Type()
)
pDataDriveStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pDataDriveStatisticsIndex.setStatus("current")
_PDataDriveStatisticsCaseID_Type = DisplayString
_PDataDriveStatisticsCaseID_Object = MibTableColumn
pDataDriveStatisticsCaseID = _PDataDriveStatisticsCaseID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 2),
    _PDataDriveStatisticsCaseID_Type()
)
pDataDriveStatisticsCaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsCaseID.setStatus("current")
_PDataDriveStatisticsCaseSerialNumber_Type = DisplayString
_PDataDriveStatisticsCaseSerialNumber_Object = MibTableColumn
pDataDriveStatisticsCaseSerialNumber = _PDataDriveStatisticsCaseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 3),
    _PDataDriveStatisticsCaseSerialNumber_Type()
)
pDataDriveStatisticsCaseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsCaseSerialNumber.setStatus("current")
_PDataDriveStatisticsCaseType_Type = DisplayString
_PDataDriveStatisticsCaseType_Object = MibTableColumn
pDataDriveStatisticsCaseType = _PDataDriveStatisticsCaseType_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 4),
    _PDataDriveStatisticsCaseType_Type()
)
pDataDriveStatisticsCaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsCaseType.setStatus("current")
_PDataDriveStatisticsDataDriveID_Type = DisplayString
_PDataDriveStatisticsDataDriveID_Object = MibTableColumn
pDataDriveStatisticsDataDriveID = _PDataDriveStatisticsDataDriveID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 5),
    _PDataDriveStatisticsDataDriveID_Type()
)
pDataDriveStatisticsDataDriveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsDataDriveID.setStatus("current")
_PDataDriveStatisticsDataDriveSlot_Type = Integer32
_PDataDriveStatisticsDataDriveSlot_Object = MibTableColumn
pDataDriveStatisticsDataDriveSlot = _PDataDriveStatisticsDataDriveSlot_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 6),
    _PDataDriveStatisticsDataDriveSlot_Type()
)
pDataDriveStatisticsDataDriveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsDataDriveSlot.setStatus("current")
_PDataDriveStatisticsCollectionTime_Type = DisplayString
_PDataDriveStatisticsCollectionTime_Object = MibTableColumn
pDataDriveStatisticsCollectionTime = _PDataDriveStatisticsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 7),
    _PDataDriveStatisticsCollectionTime_Type()
)
pDataDriveStatisticsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsCollectionTime.setStatus("current")
_PDataDriveStatisticsReadMBPerSecond_Type = DisplayString
_PDataDriveStatisticsReadMBPerSecond_Object = MibTableColumn
pDataDriveStatisticsReadMBPerSecond = _PDataDriveStatisticsReadMBPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 8),
    _PDataDriveStatisticsReadMBPerSecond_Type()
)
pDataDriveStatisticsReadMBPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsReadMBPerSecond.setStatus("current")
_PDataDriveStatisticsWriteMBPerSecond_Type = DisplayString
_PDataDriveStatisticsWriteMBPerSecond_Object = MibTableColumn
pDataDriveStatisticsWriteMBPerSecond = _PDataDriveStatisticsWriteMBPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 9),
    _PDataDriveStatisticsWriteMBPerSecond_Type()
)
pDataDriveStatisticsWriteMBPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsWriteMBPerSecond.setStatus("current")
_PDataDriveStatisticsReadLatencyInMilliseconds_Type = DisplayString
_PDataDriveStatisticsReadLatencyInMilliseconds_Object = MibTableColumn
pDataDriveStatisticsReadLatencyInMilliseconds = _PDataDriveStatisticsReadLatencyInMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 10),
    _PDataDriveStatisticsReadLatencyInMilliseconds_Type()
)
pDataDriveStatisticsReadLatencyInMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsReadLatencyInMilliseconds.setStatus("current")
_PDataDriveStatisticsWriteLatencyInMilliseconds_Type = DisplayString
_PDataDriveStatisticsWriteLatencyInMilliseconds_Object = MibTableColumn
pDataDriveStatisticsWriteLatencyInMilliseconds = _PDataDriveStatisticsWriteLatencyInMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 2, 1, 1, 11),
    _PDataDriveStatisticsWriteLatencyInMilliseconds_Type()
)
pDataDriveStatisticsWriteLatencyInMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataDriveStatisticsWriteLatencyInMilliseconds.setStatus("current")
_PCPUStatistics_ObjectIdentity = ObjectIdentity
pCPUStatistics = _PCPUStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3)
)
_PCPUStatisticsTable_Object = MibTable
pCPUStatisticsTable = _PCPUStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    pCPUStatisticsTable.setStatus("current")
_PCPUStatisticsEntry_Object = MibTableRow
pCPUStatisticsEntry = _PCPUStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1)
)
pCPUStatisticsEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "pCPUStatisticsIndex"),
)
if mibBuilder.loadTexts:
    pCPUStatisticsEntry.setStatus("current")


class _PCPUStatisticsIndex_Type(Integer32):
    """Custom type pCPUStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PCPUStatisticsIndex_Type.__name__ = "Integer32"
_PCPUStatisticsIndex_Object = MibTableColumn
pCPUStatisticsIndex = _PCPUStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1, 1),
    _PCPUStatisticsIndex_Type()
)
pCPUStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pCPUStatisticsIndex.setStatus("current")
_PCPUStatisticsServerID_Type = DisplayString
_PCPUStatisticsServerID_Object = MibTableColumn
pCPUStatisticsServerID = _PCPUStatisticsServerID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1, 2),
    _PCPUStatisticsServerID_Type()
)
pCPUStatisticsServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCPUStatisticsServerID.setStatus("current")
_PCPUStatisticsServerSerialNumber_Type = DisplayString
_PCPUStatisticsServerSerialNumber_Object = MibTableColumn
pCPUStatisticsServerSerialNumber = _PCPUStatisticsServerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1, 3),
    _PCPUStatisticsServerSerialNumber_Type()
)
pCPUStatisticsServerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCPUStatisticsServerSerialNumber.setStatus("current")
_PCPUStatisticsCollectionTime_Type = DisplayString
_PCPUStatisticsCollectionTime_Object = MibTableColumn
pCPUStatisticsCollectionTime = _PCPUStatisticsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1, 4),
    _PCPUStatisticsCollectionTime_Type()
)
pCPUStatisticsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCPUStatisticsCollectionTime.setStatus("current")
_PCPUStatisticsIdlePercent_Type = DisplayString
_PCPUStatisticsIdlePercent_Object = MibTableColumn
pCPUStatisticsIdlePercent = _PCPUStatisticsIdlePercent_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1, 5),
    _PCPUStatisticsIdlePercent_Type()
)
pCPUStatisticsIdlePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCPUStatisticsIdlePercent.setStatus("current")
_PCPUStatisticsUtilizationPercent_Type = DisplayString
_PCPUStatisticsUtilizationPercent_Object = MibTableColumn
pCPUStatisticsUtilizationPercent = _PCPUStatisticsUtilizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 3, 1, 1, 6),
    _PCPUStatisticsUtilizationPercent_Type()
)
pCPUStatisticsUtilizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCPUStatisticsUtilizationPercent.setStatus("current")
_PNetworkStatistics_ObjectIdentity = ObjectIdentity
pNetworkStatistics = _PNetworkStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4)
)
_PNetworkStatisticsTable_Object = MibTable
pNetworkStatisticsTable = _PNetworkStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1)
)
if mibBuilder.loadTexts:
    pNetworkStatisticsTable.setStatus("current")
_PNetworkStatisticsEntry_Object = MibTableRow
pNetworkStatisticsEntry = _PNetworkStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1)
)
pNetworkStatisticsEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "pNetworkStatisticsIndex"),
)
if mibBuilder.loadTexts:
    pNetworkStatisticsEntry.setStatus("current")


class _PNetworkStatisticsIndex_Type(Integer32):
    """Custom type pNetworkStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PNetworkStatisticsIndex_Type.__name__ = "Integer32"
_PNetworkStatisticsIndex_Object = MibTableColumn
pNetworkStatisticsIndex = _PNetworkStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 1),
    _PNetworkStatisticsIndex_Type()
)
pNetworkStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsIndex.setStatus("current")
_PNetworkStatisticsInterfaceID_Type = DisplayString
_PNetworkStatisticsInterfaceID_Object = MibTableColumn
pNetworkStatisticsInterfaceID = _PNetworkStatisticsInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 2),
    _PNetworkStatisticsInterfaceID_Type()
)
pNetworkStatisticsInterfaceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsInterfaceID.setStatus("current")
_PNetworkStatisticsLinkStatus_Type = DisplayString
_PNetworkStatisticsLinkStatus_Object = MibTableColumn
pNetworkStatisticsLinkStatus = _PNetworkStatisticsLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 3),
    _PNetworkStatisticsLinkStatus_Type()
)
pNetworkStatisticsLinkStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsLinkStatus.setStatus("current")
_PNetworkStatisticsCollectionTime_Type = DisplayString
_PNetworkStatisticsCollectionTime_Object = MibTableColumn
pNetworkStatisticsCollectionTime = _PNetworkStatisticsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 4),
    _PNetworkStatisticsCollectionTime_Type()
)
pNetworkStatisticsCollectionTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsCollectionTime.setStatus("current")
_PNetworkStatisticsBytesIn_Type = DisplayString
_PNetworkStatisticsBytesIn_Object = MibTableColumn
pNetworkStatisticsBytesIn = _PNetworkStatisticsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 5),
    _PNetworkStatisticsBytesIn_Type()
)
pNetworkStatisticsBytesIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsBytesIn.setStatus("current")
_PNetworkStatisticsBytesOut_Type = DisplayString
_PNetworkStatisticsBytesOut_Object = MibTableColumn
pNetworkStatisticsBytesOut = _PNetworkStatisticsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 6),
    _PNetworkStatisticsBytesOut_Type()
)
pNetworkStatisticsBytesOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsBytesOut.setStatus("current")
_PNetworkStatisticsPacketsIn_Type = DisplayString
_PNetworkStatisticsPacketsIn_Object = MibTableColumn
pNetworkStatisticsPacketsIn = _PNetworkStatisticsPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 7),
    _PNetworkStatisticsPacketsIn_Type()
)
pNetworkStatisticsPacketsIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsPacketsIn.setStatus("current")
_PNetworkStatisticsPacketsOut_Type = DisplayString
_PNetworkStatisticsPacketsOut_Object = MibTableColumn
pNetworkStatisticsPacketsOut = _PNetworkStatisticsPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 8),
    _PNetworkStatisticsPacketsOut_Type()
)
pNetworkStatisticsPacketsOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsPacketsOut.setStatus("current")
_PNetworkStatisticsErrorsIn_Type = DisplayString
_PNetworkStatisticsErrorsIn_Object = MibTableColumn
pNetworkStatisticsErrorsIn = _PNetworkStatisticsErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 9),
    _PNetworkStatisticsErrorsIn_Type()
)
pNetworkStatisticsErrorsIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsErrorsIn.setStatus("current")
_PNetworkStatisticsErrorsOut_Type = DisplayString
_PNetworkStatisticsErrorsOut_Object = MibTableColumn
pNetworkStatisticsErrorsOut = _PNetworkStatisticsErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 10),
    _PNetworkStatisticsErrorsOut_Type()
)
pNetworkStatisticsErrorsOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsErrorsOut.setStatus("current")
_PNetworkStatisticsDropsIn_Type = DisplayString
_PNetworkStatisticsDropsIn_Object = MibTableColumn
pNetworkStatisticsDropsIn = _PNetworkStatisticsDropsIn_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 11),
    _PNetworkStatisticsDropsIn_Type()
)
pNetworkStatisticsDropsIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsDropsIn.setStatus("current")
_PNetworkStatisticsCollisions_Type = DisplayString
_PNetworkStatisticsCollisions_Object = MibTableColumn
pNetworkStatisticsCollisions = _PNetworkStatisticsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 4, 1, 1, 12),
    _PNetworkStatisticsCollisions_Type()
)
pNetworkStatisticsCollisions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pNetworkStatisticsCollisions.setStatus("current")
_PTapeDriveStatistics_ObjectIdentity = ObjectIdentity
pTapeDriveStatistics = _PTapeDriveStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5)
)
_PTapeDriveStatisticsTable_Object = MibTable
pTapeDriveStatisticsTable = _PTapeDriveStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1)
)
if mibBuilder.loadTexts:
    pTapeDriveStatisticsTable.setStatus("current")
_PTapeDriveStatisticsEntry_Object = MibTableRow
pTapeDriveStatisticsEntry = _PTapeDriveStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1)
)
pTapeDriveStatisticsEntry.setIndexNames(
    (0, "SPECTRA-LOGIC-STRATA-MIB", "pTapeDriveStatisticsIndex"),
)
if mibBuilder.loadTexts:
    pTapeDriveStatisticsEntry.setStatus("current")


class _PTapeDriveStatisticsIndex_Type(Integer32):
    """Custom type pTapeDriveStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PTapeDriveStatisticsIndex_Type.__name__ = "Integer32"
_PTapeDriveStatisticsIndex_Object = MibTableColumn
pTapeDriveStatisticsIndex = _PTapeDriveStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 1),
    _PTapeDriveStatisticsIndex_Type()
)
pTapeDriveStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsIndex.setStatus("current")
_PTapeDriveStatisticsTapeDriveID_Type = DisplayString
_PTapeDriveStatisticsTapeDriveID_Object = MibTableColumn
pTapeDriveStatisticsTapeDriveID = _PTapeDriveStatisticsTapeDriveID_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 2),
    _PTapeDriveStatisticsTapeDriveID_Type()
)
pTapeDriveStatisticsTapeDriveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsTapeDriveID.setStatus("current")
_PTapeDriveStatisticsTapeDriveSerialNumber_Type = DisplayString
_PTapeDriveStatisticsTapeDriveSerialNumber_Object = MibTableColumn
pTapeDriveStatisticsTapeDriveSerialNumber = _PTapeDriveStatisticsTapeDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 3),
    _PTapeDriveStatisticsTapeDriveSerialNumber_Type()
)
pTapeDriveStatisticsTapeDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsTapeDriveSerialNumber.setStatus("current")
_PTapeDriveStatisticsCollectionTime_Type = DisplayString
_PTapeDriveStatisticsCollectionTime_Object = MibTableColumn
pTapeDriveStatisticsCollectionTime = _PTapeDriveStatisticsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 4),
    _PTapeDriveStatisticsCollectionTime_Type()
)
pTapeDriveStatisticsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsCollectionTime.setStatus("current")
_PTapeDriveStatisticsReadMBPerSecond_Type = DisplayString
_PTapeDriveStatisticsReadMBPerSecond_Object = MibTableColumn
pTapeDriveStatisticsReadMBPerSecond = _PTapeDriveStatisticsReadMBPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 5),
    _PTapeDriveStatisticsReadMBPerSecond_Type()
)
pTapeDriveStatisticsReadMBPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsReadMBPerSecond.setStatus("current")
_PTapeDriveStatisticsWriteMBPerSecond_Type = DisplayString
_PTapeDriveStatisticsWriteMBPerSecond_Object = MibTableColumn
pTapeDriveStatisticsWriteMBPerSecond = _PTapeDriveStatisticsWriteMBPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 6),
    _PTapeDriveStatisticsWriteMBPerSecond_Type()
)
pTapeDriveStatisticsWriteMBPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsWriteMBPerSecond.setStatus("current")
_PTapeDriveStatisticsReadLatencyInMilliseconds_Type = DisplayString
_PTapeDriveStatisticsReadLatencyInMilliseconds_Object = MibTableColumn
pTapeDriveStatisticsReadLatencyInMilliseconds = _PTapeDriveStatisticsReadLatencyInMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 7),
    _PTapeDriveStatisticsReadLatencyInMilliseconds_Type()
)
pTapeDriveStatisticsReadLatencyInMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsReadLatencyInMilliseconds.setStatus("current")
_PTapeDriveStatisticsWriteLatencyInMilliseconds_Type = DisplayString
_PTapeDriveStatisticsWriteLatencyInMilliseconds_Object = MibTableColumn
pTapeDriveStatisticsWriteLatencyInMilliseconds = _PTapeDriveStatisticsWriteLatencyInMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 3, 5, 1, 1, 8),
    _PTapeDriveStatisticsWriteLatencyInMilliseconds_Type()
)
pTapeDriveStatisticsWriteLatencyInMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTapeDriveStatisticsWriteLatencyInMilliseconds.setStatus("current")
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4)
)
_NStrataEvent_ObjectIdentity = ObjectIdentity
nStrataEvent = _NStrataEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 1)
)
_EventSeverity_Type = SpectraLogicStrataEventSeverity
_EventSeverity_Object = MibScalar
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 1, 1),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventTimestamp_Type = DateAndTime
_EventTimestamp_Object = MibScalar
eventTimestamp = _EventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 1, 2),
    _EventTimestamp_Type()
)
eventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimestamp.setStatus("current")
_NStrataEvents_ObjectIdentity = ObjectIdentity
nStrataEvents = _NStrataEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2)
)

# Managed Objects groups


# Notification objects

nCPUStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 1)
)
nCPUStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sCPUChassisID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sCPUSlot"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sCPUTemperature"))
)
if mibBuilder.loadTexts:
    nCPUStatus.setStatus(
        "current"
    )

nBootDriveStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 2)
)
nBootDriveStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sBootDriveChassisID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sBootDriveSlot"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sBootDriveSerialNumber"))
)
if mibBuilder.loadTexts:
    nBootDriveStatus.setStatus(
        "current"
    )

nDataDriveStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 3)
)
nDataDriveStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sDataDriveChassis"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sDataDriveSlot"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sDataDriveSerialNumber"))
)
if mibBuilder.loadTexts:
    nDataDriveStatus.setStatus(
        "current"
    )

nFanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 4)
)
nFanStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sFanChassisID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sFanSlot"))
)
if mibBuilder.loadTexts:
    nFanStatus.setStatus(
        "current"
    )

nPoolStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 6)
)
nPoolStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "cPoolID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "cPoolName"))
)
if mibBuilder.loadTexts:
    nPoolStatus.setStatus(
        "current"
    )

nPowerSupplyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 7)
)
nPowerSupplyStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sPowerSupplyChassisID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sPowerSupplySlot"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sPowerSupplyWatts"))
)
if mibBuilder.loadTexts:
    nPowerSupplyStatus.setStatus(
        "current"
    )

nScheduledASLSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 8)
)
nScheduledASLSent.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"))
)
if mibBuilder.loadTexts:
    nScheduledASLSent.setStatus(
        "current"
    )

nHighWaterMarkStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 9)
)
nHighWaterMarkStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "cPoolID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "cPoolName"))
)
if mibBuilder.loadTexts:
    nHighWaterMarkStatus.setStatus(
        "current"
    )

nUsbStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 10)
)
nUsbStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"))
)
if mibBuilder.loadTexts:
    nUsbStatus.setStatus(
        "current"
    )

nBootDriveLifespan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 11)
)
nBootDriveLifespan.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sBootDriveChassisID"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sBootDriveSlot"),
        ("SPECTRA-LOGIC-STRATA-MIB", "sBootDriveSerialNumber"))
)
if mibBuilder.loadTexts:
    nBootDriveLifespan.setStatus(
        "current"
    )

nNetworkInterfaceStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3478, 6, 4, 2, 13)
)
nNetworkInterfaceStatus.setObjects(
      *(("SPECTRA-LOGIC-STRATA-MIB", "eventSeverity"),
        ("SPECTRA-LOGIC-STRATA-MIB", "eventTimestamp"),
        ("SPECTRA-LOGIC-STRATA-MIB", "cNetworkInterfaceName"),
        ("SPECTRA-LOGIC-STRATA-MIB", "cNetworkInterfaceLinkStatus"))
)
if mibBuilder.loadTexts:
    nNetworkInterfaceStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPECTRA-LOGIC-STRATA-MIB",
    **{"KBytes": KBytes,
       "MBytes": MBytes,
       "GBytes": GBytes,
       "SpectraLogicStrataEventSeverity": SpectraLogicStrataEventSeverity,
       "spectralogic": spectralogic,
       "strata": strata,
       "configuration": configuration,
       "system": system,
       "cUsers": cUsers,
       "cUserTable": cUserTable,
       "cUserEntry": cUserEntry,
       "cUserIndex": cUserIndex,
       "cUserID": cUserID,
       "cUserUsername": cUserUsername,
       "cUserFullname": cUserFullname,
       "cUserRole": cUserRole,
       "cNetworkInterfaces": cNetworkInterfaces,
       "cNetworkInterfaceTable": cNetworkInterfaceTable,
       "cNetworkInterfaceEntry": cNetworkInterfaceEntry,
       "cNetworkInterfaceIndex": cNetworkInterfaceIndex,
       "cNetworkInterfaceID": cNetworkInterfaceID,
       "cNetworkInterfaceName": cNetworkInterfaceName,
       "cNetworkInterfaceLinkStatus": cNetworkInterfaceLinkStatus,
       "cNetworkInterfaceIPAddress": cNetworkInterfaceIPAddress,
       "cNetworkInterfaceNetmask": cNetworkInterfaceNetmask,
       "cNetworkInterfaceDefaultGateway": cNetworkInterfaceDefaultGateway,
       "cNetworkInterfaceDHCP": cNetworkInterfaceDHCP,
       "cNetworkInterfaceMACAddress": cNetworkInterfaceMACAddress,
       "cNetworkInterfaceMTU": cNetworkInterfaceMTU,
       "cTimeManagement": cTimeManagement,
       "cNTPTable": cNTPTable,
       "cNTPEntry": cNTPEntry,
       "cNTPIndex": cNTPIndex,
       "cNTPEnabled": cNTPEnabled,
       "cNTPAddress1": cNTPAddress1,
       "cNTPAddress2": cNTPAddress2,
       "cNTPSynchronized": cNTPSynchronized,
       "cLogs": cLogs,
       "cLogTable": cLogTable,
       "cLogEntry": cLogEntry,
       "cLogIndex": cLogIndex,
       "cLogID": cLogID,
       "cLogCreationDate": cLogCreationDate,
       "cLogSize": cLogSize,
       "storage": storage,
       "cPools": cPools,
       "cPoolTable": cPoolTable,
       "cPoolEntry": cPoolEntry,
       "cPoolIndex": cPoolIndex,
       "cPoolID": cPoolID,
       "cPoolName": cPoolName,
       "cPoolCreationDate": cPoolCreationDate,
       "cPoolRawSize": cPoolRawSize,
       "cPoolAvailableSize": cPoolAvailableSize,
       "cPoolUsedSize": cPoolUsedSize,
       "cPoolOverheadSize": cPoolOverheadSize,
       "cPoolProtectionLevel": cPoolProtectionLevel,
       "cPoolNumberOfDiskArrays": cPoolNumberOfDiskArrays,
       "cPoolStatus": cPoolStatus,
       "cPoolHighWaterMark": cPoolHighWaterMark,
       "cVolumes": cVolumes,
       "cVolumeTable": cVolumeTable,
       "cVolumeEntry": cVolumeEntry,
       "cVolumeIndex": cVolumeIndex,
       "cVolumeID": cVolumeID,
       "cVolumeName": cVolumeName,
       "cVolumePoolID": cVolumePoolID,
       "cVolumePoolName": cVolumePoolName,
       "cVolumeCreationDate": cVolumeCreationDate,
       "cVolumeMaximumSize": cVolumeMaximumSize,
       "cVolumeMinimumSize": cVolumeMinimumSize,
       "cVolumeUsedSpace": cVolumeUsedSpace,
       "cVolumeCompressionEnabled": cVolumeCompressionEnabled,
       "cVolumeReadOnly": cVolumeReadOnly,
       "cVolumeAtimeEnabled": cVolumeAtimeEnabled,
       "cSnapshotTable": cSnapshotTable,
       "cSnapshotEntry": cSnapshotEntry,
       "cSnapshotIndex": cSnapshotIndex,
       "cSnapshotID": cSnapshotID,
       "cSnapshotName": cSnapshotName,
       "cSnapshotVolumeID": cSnapshotVolumeID,
       "cSnapshotCreationDate": cSnapshotCreationDate,
       "cSnapshotSize": cSnapshotSize,
       "cSnapshotScheduleTable": cSnapshotScheduleTable,
       "cSnapshotScheduleEntry": cSnapshotScheduleEntry,
       "cSnapshotScheduleIndex": cSnapshotScheduleIndex,
       "cSnapshotScheduleID": cSnapshotScheduleID,
       "cSnapshotScheduleName": cSnapshotScheduleName,
       "cSnapshotScheduleVolumeID": cSnapshotScheduleVolumeID,
       "cSnapshotScheduleMaximumNumberOfSnapshots": cSnapshotScheduleMaximumNumberOfSnapshots,
       "cSnapshotScheduleCronString": cSnapshotScheduleCronString,
       "cSnapshotScheduleStartTime": cSnapshotScheduleStartTime,
       "cSnapshotScheduleFrequency": cSnapshotScheduleFrequency,
       "cSnapshotScheduleRepeatInterval": cSnapshotScheduleRepeatInterval,
       "cCIFSShareTable": cCIFSShareTable,
       "cCIFSShareEntry": cCIFSShareEntry,
       "cCIFSShareIndex": cCIFSShareIndex,
       "cCIFSShareID": cCIFSShareID,
       "cCIFSShareName": cCIFSShareName,
       "cCIFSSharePath": cCIFSSharePath,
       "cCIFSShareReadOnly": cCIFSShareReadOnly,
       "cNFSShareTable": cNFSShareTable,
       "cNFSShareEntry": cNFSShareEntry,
       "cNFSShareIndex": cNFSShareIndex,
       "cNFSShareID": cNFSShareID,
       "cNFSShareMountPoint": cNFSShareMountPoint,
       "cNFSSharePath": cNFSSharePath,
       "cNFSShareAccessControl": cNFSShareAccessControl,
       "cNFSShareAnonymousUUID": cNFSShareAnonymousUUID,
       "cNFSShareComment": cNFSShareComment,
       "services": services,
       "cNFSServiceTable": cNFSServiceTable,
       "cNFSServiceEntry": cNFSServiceEntry,
       "cNFSServiceIndex": cNFSServiceIndex,
       "cNFSServiceID": cNFSServiceID,
       "cNFSServiceStatus": cNFSServiceStatus,
       "cNFSServiceTcpEnabled": cNFSServiceTcpEnabled,
       "cNFSServiceUdpEnabled": cNFSServiceUdpEnabled,
       "cNFSServiceThreads": cNFSServiceThreads,
       "cADServiceTable": cADServiceTable,
       "cADServiceEntry": cADServiceEntry,
       "cADServiceIndex": cADServiceIndex,
       "cADServiceID": cADServiceID,
       "cADServiceStatus": cADServiceStatus,
       "cADServiceActiveDirectoryJoined": cADServiceActiveDirectoryJoined,
       "cADServiceHostname": cADServiceHostname,
       "cADServiceDnsDomainName": cADServiceDnsDomainName,
       "cSNMPService": cSNMPService,
       "cSNMPClientTable": cSNMPClientTable,
       "cSNMPClientEntry": cSNMPClientEntry,
       "cSNMPClientIndex": cSNMPClientIndex,
       "cSNMPClientHost": cSNMPClientHost,
       "cSNMPClientNotifications": cSNMPClientNotifications,
       "cSNMPClientPort": cSNMPClientPort,
       "cSNMPClientCommunityString": cSNMPClientCommunityString,
       "status": status,
       "hardware": hardware,
       "sChassisTable": sChassisTable,
       "sChassisEntry": sChassisEntry,
       "sChassisIndex": sChassisIndex,
       "sChassisID": sChassisID,
       "sChassisType": sChassisType,
       "sChassisStatus": sChassisStatus,
       "sChassisModel": sChassisModel,
       "sChassisSerialNumber": sChassisSerialNumber,
       "sChassisMemory": sChassisMemory,
       "sChassisRawCapacity": sChassisRawCapacity,
       "sCPUTable": sCPUTable,
       "sCPUEntry": sCPUEntry,
       "sCPUIndex": sCPUIndex,
       "sCPUChassisID": sCPUChassisID,
       "sCPUSlot": sCPUSlot,
       "sCPUStatus": sCPUStatus,
       "sCPUTemperature": sCPUTemperature,
       "sBootDriveTable": sBootDriveTable,
       "sBootDriveEntry": sBootDriveEntry,
       "sBootDriveIndex": sBootDriveIndex,
       "sBootDriveChassisID": sBootDriveChassisID,
       "sBootDriveSlot": sBootDriveSlot,
       "sBootDriveStatus": sBootDriveStatus,
       "sBootDriveManufacturer": sBootDriveManufacturer,
       "sBootDriveModel": sBootDriveModel,
       "sBootDriveSize": sBootDriveSize,
       "sBootDriveSerialNumber": sBootDriveSerialNumber,
       "sDataDriveTable": sDataDriveTable,
       "sDataDriveEntry": sDataDriveEntry,
       "sDataDriveIndex": sDataDriveIndex,
       "sDataDriveChassis": sDataDriveChassis,
       "sDataDriveSlot": sDataDriveSlot,
       "sDataDriveStatus": sDataDriveStatus,
       "sDataDriveSize": sDataDriveSize,
       "sDataDriveSerialNumber": sDataDriveSerialNumber,
       "sDataDrivePoolID": sDataDrivePoolID,
       "sDataDrivePoolName": sDataDrivePoolName,
       "sFanTable": sFanTable,
       "sFanEntry": sFanEntry,
       "sFanIndex": sFanIndex,
       "sFanChassisID": sFanChassisID,
       "sFanSlot": sFanSlot,
       "sFanStatus": sFanStatus,
       "sFanSpeed": sFanSpeed,
       "sPowerSupplyTable": sPowerSupplyTable,
       "sPowerSupplyEntry": sPowerSupplyEntry,
       "sPowerSupplyIndex": sPowerSupplyIndex,
       "sPowerSupplyChassisID": sPowerSupplyChassisID,
       "sPowerSupplySlot": sPowerSupplySlot,
       "sPowerSupplyStatus": sPowerSupplyStatus,
       "sPowerSupplyWatts": sPowerSupplyWatts,
       "sTapeDriveTable": sTapeDriveTable,
       "sTapeDriveEntry": sTapeDriveEntry,
       "sTapeDriveIndex": sTapeDriveIndex,
       "sTapeDrivePartition": sTapeDrivePartition,
       "sTapeDriveStatus": sTapeDriveStatus,
       "sTapeDriveType": sTapeDriveType,
       "sTapeDriveSerialNumber": sTapeDriveSerialNumber,
       "sTapeDriveTapeBarcode": sTapeDriveTapeBarcode,
       "sTapeDriveErrorMesssage": sTapeDriveErrorMesssage,
       "performance": performance,
       "pPoolStatistics": pPoolStatistics,
       "pPoolStatisticsTable": pPoolStatisticsTable,
       "pPoolStatisticsEntry": pPoolStatisticsEntry,
       "pPoolStatisticsIndex": pPoolStatisticsIndex,
       "pPoolStatisticsPoolID": pPoolStatisticsPoolID,
       "pPoolStatisticsPoolName": pPoolStatisticsPoolName,
       "pPoolStatisticsCollectionTime": pPoolStatisticsCollectionTime,
       "pPoolStatisticsReadIOPs": pPoolStatisticsReadIOPs,
       "pPoolStatisticsWriteIOPs": pPoolStatisticsWriteIOPs,
       "pPoolStatisticsReadBytesPerSecond": pPoolStatisticsReadBytesPerSecond,
       "pPoolStatisticsWriteBytesPerSecond": pPoolStatisticsWriteBytesPerSecond,
       "pDataDriveStatistics": pDataDriveStatistics,
       "pDataDriveStatisticsTable": pDataDriveStatisticsTable,
       "pDataDriveStatisticsEntry": pDataDriveStatisticsEntry,
       "pDataDriveStatisticsIndex": pDataDriveStatisticsIndex,
       "pDataDriveStatisticsCaseID": pDataDriveStatisticsCaseID,
       "pDataDriveStatisticsCaseSerialNumber": pDataDriveStatisticsCaseSerialNumber,
       "pDataDriveStatisticsCaseType": pDataDriveStatisticsCaseType,
       "pDataDriveStatisticsDataDriveID": pDataDriveStatisticsDataDriveID,
       "pDataDriveStatisticsDataDriveSlot": pDataDriveStatisticsDataDriveSlot,
       "pDataDriveStatisticsCollectionTime": pDataDriveStatisticsCollectionTime,
       "pDataDriveStatisticsReadMBPerSecond": pDataDriveStatisticsReadMBPerSecond,
       "pDataDriveStatisticsWriteMBPerSecond": pDataDriveStatisticsWriteMBPerSecond,
       "pDataDriveStatisticsReadLatencyInMilliseconds": pDataDriveStatisticsReadLatencyInMilliseconds,
       "pDataDriveStatisticsWriteLatencyInMilliseconds": pDataDriveStatisticsWriteLatencyInMilliseconds,
       "pCPUStatistics": pCPUStatistics,
       "pCPUStatisticsTable": pCPUStatisticsTable,
       "pCPUStatisticsEntry": pCPUStatisticsEntry,
       "pCPUStatisticsIndex": pCPUStatisticsIndex,
       "pCPUStatisticsServerID": pCPUStatisticsServerID,
       "pCPUStatisticsServerSerialNumber": pCPUStatisticsServerSerialNumber,
       "pCPUStatisticsCollectionTime": pCPUStatisticsCollectionTime,
       "pCPUStatisticsIdlePercent": pCPUStatisticsIdlePercent,
       "pCPUStatisticsUtilizationPercent": pCPUStatisticsUtilizationPercent,
       "pNetworkStatistics": pNetworkStatistics,
       "pNetworkStatisticsTable": pNetworkStatisticsTable,
       "pNetworkStatisticsEntry": pNetworkStatisticsEntry,
       "pNetworkStatisticsIndex": pNetworkStatisticsIndex,
       "pNetworkStatisticsInterfaceID": pNetworkStatisticsInterfaceID,
       "pNetworkStatisticsLinkStatus": pNetworkStatisticsLinkStatus,
       "pNetworkStatisticsCollectionTime": pNetworkStatisticsCollectionTime,
       "pNetworkStatisticsBytesIn": pNetworkStatisticsBytesIn,
       "pNetworkStatisticsBytesOut": pNetworkStatisticsBytesOut,
       "pNetworkStatisticsPacketsIn": pNetworkStatisticsPacketsIn,
       "pNetworkStatisticsPacketsOut": pNetworkStatisticsPacketsOut,
       "pNetworkStatisticsErrorsIn": pNetworkStatisticsErrorsIn,
       "pNetworkStatisticsErrorsOut": pNetworkStatisticsErrorsOut,
       "pNetworkStatisticsDropsIn": pNetworkStatisticsDropsIn,
       "pNetworkStatisticsCollisions": pNetworkStatisticsCollisions,
       "pTapeDriveStatistics": pTapeDriveStatistics,
       "pTapeDriveStatisticsTable": pTapeDriveStatisticsTable,
       "pTapeDriveStatisticsEntry": pTapeDriveStatisticsEntry,
       "pTapeDriveStatisticsIndex": pTapeDriveStatisticsIndex,
       "pTapeDriveStatisticsTapeDriveID": pTapeDriveStatisticsTapeDriveID,
       "pTapeDriveStatisticsTapeDriveSerialNumber": pTapeDriveStatisticsTapeDriveSerialNumber,
       "pTapeDriveStatisticsCollectionTime": pTapeDriveStatisticsCollectionTime,
       "pTapeDriveStatisticsReadMBPerSecond": pTapeDriveStatisticsReadMBPerSecond,
       "pTapeDriveStatisticsWriteMBPerSecond": pTapeDriveStatisticsWriteMBPerSecond,
       "pTapeDriveStatisticsReadLatencyInMilliseconds": pTapeDriveStatisticsReadLatencyInMilliseconds,
       "pTapeDriveStatisticsWriteLatencyInMilliseconds": pTapeDriveStatisticsWriteLatencyInMilliseconds,
       "notification": notification,
       "nStrataEvent": nStrataEvent,
       "eventSeverity": eventSeverity,
       "eventTimestamp": eventTimestamp,
       "nStrataEvents": nStrataEvents,
       "nCPUStatus": nCPUStatus,
       "nBootDriveStatus": nBootDriveStatus,
       "nDataDriveStatus": nDataDriveStatus,
       "nFanStatus": nFanStatus,
       "nPoolStatus": nPoolStatus,
       "nPowerSupplyStatus": nPowerSupplyStatus,
       "nScheduledASLSent": nScheduledASLSent,
       "nHighWaterMarkStatus": nHighWaterMarkStatus,
       "nUsbStatus": nUsbStatus,
       "nBootDriveLifespan": nBootDriveLifespan,
       "nNetworkInterfaceStatus": nNetworkInterfaceStatus}
)
