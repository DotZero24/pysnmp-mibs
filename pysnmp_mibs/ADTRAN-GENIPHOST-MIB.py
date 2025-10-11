# SNMP MIB module (ADTRAN-GENIPHOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENIPHOST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:35 2025
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

(adGenIpHost,
 adGenIpHostID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenIpHost",
    "adGenIpHostID")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

adGenIpHostIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 18, 1)
)
if mibBuilder.loadTexts:
    adGenIpHostIdentity.setRevisions(
        ("2016-01-11 00:00",
         "2012-01-20 00:00",
         "2009-11-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenIpHostServiceOrInterface(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("serviceSIP", 1),
          ("serviceMGCP", 2),
          ("serviceRFVideo", 3),
          ("serviceRADIUS", 4),
          ("interfacePseudowire", 50),
          ("interfacePacketTiming", 51))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenIpHostProvisioning_ObjectIdentity = ObjectIdentity
adGenIpHostProvisioning = _AdGenIpHostProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1)
)
_AdGenIpHostProvErrorTable_Object = MibTable
adGenIpHostProvErrorTable = _AdGenIpHostProvErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 1)
)
if mibBuilder.loadTexts:
    adGenIpHostProvErrorTable.setStatus("current")
_AdGenIpHostProvErrorEntry_Object = MibTableRow
adGenIpHostProvErrorEntry = _AdGenIpHostProvErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 1, 1)
)
adGenIpHostProvErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenIpHostProvErrorEntry.setStatus("current")
_AdGenIpHostProvCurrentNumber_Type = Integer32
_AdGenIpHostProvCurrentNumber_Object = MibTableColumn
adGenIpHostProvCurrentNumber = _AdGenIpHostProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 1, 1, 1),
    _AdGenIpHostProvCurrentNumber_Type()
)
adGenIpHostProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostProvCurrentNumber.setStatus("current")
_AdGenIpHostProvLastCreateError_Type = DisplayString
_AdGenIpHostProvLastCreateError_Object = MibTableColumn
adGenIpHostProvLastCreateError = _AdGenIpHostProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 1, 1, 2),
    _AdGenIpHostProvLastCreateError_Type()
)
adGenIpHostProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostProvLastCreateError.setStatus("current")
_AdGenIpHostProvTable_Object = MibTable
adGenIpHostProvTable = _AdGenIpHostProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2)
)
if mibBuilder.loadTexts:
    adGenIpHostProvTable.setStatus("current")
_AdGenIpHostProvEntry_Object = MibTableRow
adGenIpHostProvEntry = _AdGenIpHostProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1)
)
adGenIpHostProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "ADTRAN-GENIPHOST-MIB", "adGenIpHostEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenIpHostProvEntry.setStatus("current")


class _AdGenIpHostEntryIndex_Type(DisplayString):
    """Custom type adGenIpHostEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenIpHostEntryIndex_Type.__name__ = "DisplayString"
_AdGenIpHostEntryIndex_Object = MibTableColumn
adGenIpHostEntryIndex = _AdGenIpHostEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 1),
    _AdGenIpHostEntryIndex_Type()
)
adGenIpHostEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIpHostEntryIndex.setStatus("current")
_AdGenIpHostProvRowStatus_Type = RowStatus
_AdGenIpHostProvRowStatus_Object = MibTableColumn
adGenIpHostProvRowStatus = _AdGenIpHostProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 2),
    _AdGenIpHostProvRowStatus_Type()
)
adGenIpHostProvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvRowStatus.setStatus("current")
_AdGenIpHostProvLastErrorString_Type = DisplayString
_AdGenIpHostProvLastErrorString_Object = MibTableColumn
adGenIpHostProvLastErrorString = _AdGenIpHostProvLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 3),
    _AdGenIpHostProvLastErrorString_Type()
)
adGenIpHostProvLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostProvLastErrorString.setStatus("current")
_AdGenIpHostProvStatus_Type = DisplayString
_AdGenIpHostProvStatus_Object = MibTableColumn
adGenIpHostProvStatus = _AdGenIpHostProvStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 4),
    _AdGenIpHostProvStatus_Type()
)
adGenIpHostProvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostProvStatus.setStatus("current")
_AdGenIpHostSubInterfaceIndex_Type = Integer32
_AdGenIpHostSubInterfaceIndex_Object = MibTableColumn
adGenIpHostSubInterfaceIndex = _AdGenIpHostSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 5),
    _AdGenIpHostSubInterfaceIndex_Type()
)
adGenIpHostSubInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostSubInterfaceIndex.setStatus("current")
_AdGenIpHostProvIpAddress_Type = IpAddress
_AdGenIpHostProvIpAddress_Object = MibTableColumn
adGenIpHostProvIpAddress = _AdGenIpHostProvIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 6),
    _AdGenIpHostProvIpAddress_Type()
)
adGenIpHostProvIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvIpAddress.setStatus("current")
_AdGenIpHostProvIpSubnetMask_Type = IpAddress
_AdGenIpHostProvIpSubnetMask_Object = MibTableColumn
adGenIpHostProvIpSubnetMask = _AdGenIpHostProvIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 7),
    _AdGenIpHostProvIpSubnetMask_Type()
)
adGenIpHostProvIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvIpSubnetMask.setStatus("current")
_AdGenIpHostProvIpDefaultGateway_Type = IpAddress
_AdGenIpHostProvIpDefaultGateway_Object = MibTableColumn
adGenIpHostProvIpDefaultGateway = _AdGenIpHostProvIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 8),
    _AdGenIpHostProvIpDefaultGateway_Type()
)
adGenIpHostProvIpDefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvIpDefaultGateway.setStatus("current")
_AdGenIpHostProvDomainName_Type = DisplayString
_AdGenIpHostProvDomainName_Object = MibTableColumn
adGenIpHostProvDomainName = _AdGenIpHostProvDomainName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 9),
    _AdGenIpHostProvDomainName_Type()
)
adGenIpHostProvDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvDomainName.setStatus("current")
_AdGenIpHostProvDomainNameAddServer_Type = IpAddress
_AdGenIpHostProvDomainNameAddServer_Object = MibTableColumn
adGenIpHostProvDomainNameAddServer = _AdGenIpHostProvDomainNameAddServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 10),
    _AdGenIpHostProvDomainNameAddServer_Type()
)
adGenIpHostProvDomainNameAddServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvDomainNameAddServer.setStatus("current")
_AdGenIpHostProvDomainNameRemoveServer_Type = IpAddress
_AdGenIpHostProvDomainNameRemoveServer_Object = MibTableColumn
adGenIpHostProvDomainNameRemoveServer = _AdGenIpHostProvDomainNameRemoveServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 11),
    _AdGenIpHostProvDomainNameRemoveServer_Type()
)
adGenIpHostProvDomainNameRemoveServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvDomainNameRemoveServer.setStatus("current")


class _AdGenIpHostProvDomainNameServerList_Type(OctetString):
    """Custom type adGenIpHostProvDomainNameServerList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_AdGenIpHostProvDomainNameServerList_Type.__name__ = "OctetString"
_AdGenIpHostProvDomainNameServerList_Object = MibTableColumn
adGenIpHostProvDomainNameServerList = _AdGenIpHostProvDomainNameServerList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 12),
    _AdGenIpHostProvDomainNameServerList_Type()
)
adGenIpHostProvDomainNameServerList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvDomainNameServerList.setStatus("current")
_AdGenIpHostProvDomainLookup_Type = TruthValue
_AdGenIpHostProvDomainLookup_Object = MibTableColumn
adGenIpHostProvDomainLookup = _AdGenIpHostProvDomainLookup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 13),
    _AdGenIpHostProvDomainLookup_Type()
)
adGenIpHostProvDomainLookup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvDomainLookup.setStatus("current")


class _AdGenIpHostProvIpAssignMode_Type(Integer32):
    """Custom type adGenIpHostProvIpAssignMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_AdGenIpHostProvIpAssignMode_Type.__name__ = "Integer32"
_AdGenIpHostProvIpAssignMode_Object = MibTableColumn
adGenIpHostProvIpAssignMode = _AdGenIpHostProvIpAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 14),
    _AdGenIpHostProvIpAssignMode_Type()
)
adGenIpHostProvIpAssignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostProvIpAssignMode.setStatus("current")
_AdGenIpHostConnectLastErrorString_Type = DisplayString
_AdGenIpHostConnectLastErrorString_Object = MibTableColumn
adGenIpHostConnectLastErrorString = _AdGenIpHostConnectLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 1, 2, 1, 15),
    _AdGenIpHostConnectLastErrorString_Type()
)
adGenIpHostConnectLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostConnectLastErrorString.setStatus("current")
_AdGenIpHostStatus_ObjectIdentity = ObjectIdentity
adGenIpHostStatus = _AdGenIpHostStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 2)
)
_AdGenIpHostStatTable_Object = MibTable
adGenIpHostStatTable = _AdGenIpHostStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 2, 1)
)
if mibBuilder.loadTexts:
    adGenIpHostStatTable.setStatus("current")
_AdGenIpHostStatEntry_Object = MibTableRow
adGenIpHostStatEntry = _AdGenIpHostStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 2, 1, 1)
)
adGenIpHostStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "ADTRAN-GENIPHOST-MIB", "adGenIpHostEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenIpHostStatEntry.setStatus("current")
_AdGenIpHostStatIpAddress_Type = IpAddress
_AdGenIpHostStatIpAddress_Object = MibTableColumn
adGenIpHostStatIpAddress = _AdGenIpHostStatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 2, 1, 1, 1),
    _AdGenIpHostStatIpAddress_Type()
)
adGenIpHostStatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostStatIpAddress.setStatus("current")
_AdGenIpHostStatGateway_Type = IpAddress
_AdGenIpHostStatGateway_Object = MibTableColumn
adGenIpHostStatGateway = _AdGenIpHostStatGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 2, 1, 1, 2),
    _AdGenIpHostStatGateway_Type()
)
adGenIpHostStatGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostStatGateway.setStatus("current")
_AdGenIpHostStatIpSubnetMask_Type = IpAddress
_AdGenIpHostStatIpSubnetMask_Object = MibTableColumn
adGenIpHostStatIpSubnetMask = _AdGenIpHostStatIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 2, 1, 1, 3),
    _AdGenIpHostStatIpSubnetMask_Type()
)
adGenIpHostStatIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpHostStatIpSubnetMask.setStatus("current")
_AdGenIpHostConnect_ObjectIdentity = ObjectIdentity
adGenIpHostConnect = _AdGenIpHostConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 3)
)
_AdGenIpHostConnectTable_Object = MibTable
adGenIpHostConnectTable = _AdGenIpHostConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 3, 1)
)
if mibBuilder.loadTexts:
    adGenIpHostConnectTable.setStatus("current")
_AdGenIpHostConnectEntry_Object = MibTableRow
adGenIpHostConnectEntry = _AdGenIpHostConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 3, 1, 1)
)
adGenIpHostConnectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENIPHOST-MIB", "adGenIpHostServiceOrInterface"),
    (0, "ADTRAN-GENIPHOST-MIB", "adGenIpHostConnectIfIndex"),
    (1, "ADTRAN-GENIPHOST-MIB", "adGenIpHostEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenIpHostConnectEntry.setStatus("current")
_AdGenIpHostServiceOrInterface_Type = AdGenIpHostServiceOrInterface
_AdGenIpHostServiceOrInterface_Object = MibTableColumn
adGenIpHostServiceOrInterface = _AdGenIpHostServiceOrInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 3, 1, 1, 1),
    _AdGenIpHostServiceOrInterface_Type()
)
adGenIpHostServiceOrInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIpHostServiceOrInterface.setStatus("current")
_AdGenIpHostConnectIfIndex_Type = InterfaceIndexOrZero
_AdGenIpHostConnectIfIndex_Object = MibTableColumn
adGenIpHostConnectIfIndex = _AdGenIpHostConnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 3, 1, 1, 2),
    _AdGenIpHostConnectIfIndex_Type()
)
adGenIpHostConnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIpHostConnectIfIndex.setStatus("current")
_AdGenIpHostConnectRowStatus_Type = RowStatus
_AdGenIpHostConnectRowStatus_Object = MibTableColumn
adGenIpHostConnectRowStatus = _AdGenIpHostConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 18, 3, 1, 1, 3),
    _AdGenIpHostConnectRowStatus_Type()
)
adGenIpHostConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpHostConnectRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENIPHOST-MIB",
    **{"AdGenIpHostServiceOrInterface": AdGenIpHostServiceOrInterface,
       "adGenIpHostProvisioning": adGenIpHostProvisioning,
       "adGenIpHostProvErrorTable": adGenIpHostProvErrorTable,
       "adGenIpHostProvErrorEntry": adGenIpHostProvErrorEntry,
       "adGenIpHostProvCurrentNumber": adGenIpHostProvCurrentNumber,
       "adGenIpHostProvLastCreateError": adGenIpHostProvLastCreateError,
       "adGenIpHostProvTable": adGenIpHostProvTable,
       "adGenIpHostProvEntry": adGenIpHostProvEntry,
       "adGenIpHostEntryIndex": adGenIpHostEntryIndex,
       "adGenIpHostProvRowStatus": adGenIpHostProvRowStatus,
       "adGenIpHostProvLastErrorString": adGenIpHostProvLastErrorString,
       "adGenIpHostProvStatus": adGenIpHostProvStatus,
       "adGenIpHostSubInterfaceIndex": adGenIpHostSubInterfaceIndex,
       "adGenIpHostProvIpAddress": adGenIpHostProvIpAddress,
       "adGenIpHostProvIpSubnetMask": adGenIpHostProvIpSubnetMask,
       "adGenIpHostProvIpDefaultGateway": adGenIpHostProvIpDefaultGateway,
       "adGenIpHostProvDomainName": adGenIpHostProvDomainName,
       "adGenIpHostProvDomainNameAddServer": adGenIpHostProvDomainNameAddServer,
       "adGenIpHostProvDomainNameRemoveServer": adGenIpHostProvDomainNameRemoveServer,
       "adGenIpHostProvDomainNameServerList": adGenIpHostProvDomainNameServerList,
       "adGenIpHostProvDomainLookup": adGenIpHostProvDomainLookup,
       "adGenIpHostProvIpAssignMode": adGenIpHostProvIpAssignMode,
       "adGenIpHostConnectLastErrorString": adGenIpHostConnectLastErrorString,
       "adGenIpHostStatus": adGenIpHostStatus,
       "adGenIpHostStatTable": adGenIpHostStatTable,
       "adGenIpHostStatEntry": adGenIpHostStatEntry,
       "adGenIpHostStatIpAddress": adGenIpHostStatIpAddress,
       "adGenIpHostStatGateway": adGenIpHostStatGateway,
       "adGenIpHostStatIpSubnetMask": adGenIpHostStatIpSubnetMask,
       "adGenIpHostConnect": adGenIpHostConnect,
       "adGenIpHostConnectTable": adGenIpHostConnectTable,
       "adGenIpHostConnectEntry": adGenIpHostConnectEntry,
       "adGenIpHostServiceOrInterface": adGenIpHostServiceOrInterface,
       "adGenIpHostConnectIfIndex": adGenIpHostConnectIfIndex,
       "adGenIpHostConnectRowStatus": adGenIpHostConnectRowStatus,
       "adGenIpHostIdentity": adGenIpHostIdentity}
)
