# SNMP MIB module (SVRCLU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/SVRCLU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:33:23 2025
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ClusterType(Integer32):
    """Custom type ClusterType based on Integer32"""
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
              3601,
              3602,
              3603,
              3604,
              23200,
              23201)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("digitalNT", 3),
          ("microsoftNT", 4),
          ("digitalUnixASE", 5),
          ("digitalUnixTCR", 6),
          ("openVMS", 7),
          ("compaqTruClusterAvailableServer", 3601),
          ("compaqTruClusterProductionServer", 3602),
          ("compaqTruClusterServer", 3603),
          ("compaqOpenVms", 3604),
          ("cpqclusterMSCS", 23200),
          ("compaqMSCS", 23201))
    )





class ClusterStatus(Integer32):
    """Custom type ClusterStatus based on Integer32"""
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
          ("other", 2),
          ("notInstalled", 3),
          ("notRunning", 4),
          ("initializing", 5),
          ("running", 6),
          ("suspended", 7),
          ("failed", 8))
    )





class MemberStatus(Integer32):
    """Custom type MemberStatus based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("new", 3),
          ("normal", 4),
          ("removed", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_Mib_extensions_1_ObjectIdentity = ObjectIdentity
mib_extensions_1 = _Mib_extensions_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_SvrSystem_ObjectIdentity = ObjectIdentity
svrSystem = _SvrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22)
)
_SvrCluster_ObjectIdentity = ObjectIdentity
svrCluster = _SvrCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4)
)
_SvrClu_ObjectIdentity = ObjectIdentity
svrClu = _SvrClu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1)
)
_SvrCluObjects_ObjectIdentity = ObjectIdentity
svrCluObjects = _SvrCluObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1)
)
_SvrCluMibInfo_ObjectIdentity = ObjectIdentity
svrCluMibInfo = _SvrCluMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 1)
)
_SvrCluMibMajorRev_Type = Integer32
_SvrCluMibMajorRev_Object = MibScalar
svrCluMibMajorRev = _SvrCluMibMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 1, 1),
    _SvrCluMibMajorRev_Type()
)
svrCluMibMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMibMajorRev.setStatus("mandatory")
_SvrCluMibMinorRev_Type = Integer32
_SvrCluMibMinorRev_Object = MibScalar
svrCluMibMinorRev = _SvrCluMibMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 1, 2),
    _SvrCluMibMinorRev_Type()
)
svrCluMibMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMibMinorRev.setStatus("mandatory")
_SvrCluClusterInfo_ObjectIdentity = ObjectIdentity
svrCluClusterInfo = _SvrCluClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2)
)
_SvrCluSoftwareVendor_Type = DisplayString
_SvrCluSoftwareVendor_Object = MibScalar
svrCluSoftwareVendor = _SvrCluSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 1),
    _SvrCluSoftwareVendor_Type()
)
svrCluSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluSoftwareVendor.setStatus("mandatory")
_SvrCluSoftwareVersion_Type = DisplayString
_SvrCluSoftwareVersion_Object = MibScalar
svrCluSoftwareVersion = _SvrCluSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 2),
    _SvrCluSoftwareVersion_Type()
)
svrCluSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluSoftwareVersion.setStatus("mandatory")
_SvrCluSoftwareStatus_Type = ClusterStatus
_SvrCluSoftwareStatus_Object = MibScalar
svrCluSoftwareStatus = _SvrCluSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 3),
    _SvrCluSoftwareStatus_Type()
)
svrCluSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluSoftwareStatus.setStatus("mandatory")
_SvrCluClusterType_Type = ClusterType
_SvrCluClusterType_Object = MibScalar
svrCluClusterType = _SvrCluClusterType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 4),
    _SvrCluClusterType_Type()
)
svrCluClusterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluClusterType.setStatus("mandatory")
_SvrCluExtensionOID_Type = ObjectIdentifier
_SvrCluExtensionOID_Object = MibScalar
svrCluExtensionOID = _SvrCluExtensionOID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 5),
    _SvrCluExtensionOID_Type()
)
svrCluExtensionOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluExtensionOID.setStatus("mandatory")
_SvrCluThisMember_Type = Integer32
_SvrCluThisMember_Object = MibScalar
svrCluThisMember = _SvrCluThisMember_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 6),
    _SvrCluThisMember_Type()
)
svrCluThisMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluThisMember.setStatus("mandatory")
_SvrCluClusterName_Type = DisplayString
_SvrCluClusterName_Object = MibScalar
svrCluClusterName = _SvrCluClusterName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 7),
    _SvrCluClusterName_Type()
)
svrCluClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluClusterName.setStatus("mandatory")
_SvrCluClusterAddressTable_Object = MibTable
svrCluClusterAddressTable = _SvrCluClusterAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    svrCluClusterAddressTable.setStatus("mandatory")
_SvrCluClusterAddressEntry_Object = MibTableRow
svrCluClusterAddressEntry = _SvrCluClusterAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 8, 1)
)
svrCluClusterAddressEntry.setIndexNames(
    (0, "SVRCLU-MIB", "svrCluClusterAddressIndex"),
)
if mibBuilder.loadTexts:
    svrCluClusterAddressEntry.setStatus("mandatory")
_SvrCluClusterAddressIndex_Type = Integer32
_SvrCluClusterAddressIndex_Object = MibTableColumn
svrCluClusterAddressIndex = _SvrCluClusterAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 8, 1, 1),
    _SvrCluClusterAddressIndex_Type()
)
svrCluClusterAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluClusterAddressIndex.setStatus("mandatory")
_SvrCluClusterAddress_Type = IpAddress
_SvrCluClusterAddress_Object = MibTableColumn
svrCluClusterAddress = _SvrCluClusterAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 8, 1, 2),
    _SvrCluClusterAddress_Type()
)
svrCluClusterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluClusterAddress.setStatus("mandatory")
_SvrCluServiceName_Type = DisplayString
_SvrCluServiceName_Object = MibScalar
svrCluServiceName = _SvrCluServiceName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 9),
    _SvrCluServiceName_Type()
)
svrCluServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluServiceName.setStatus("mandatory")
_SvrCluMemberTable_Object = MibTable
svrCluMemberTable = _SvrCluMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    svrCluMemberTable.setStatus("mandatory")
_SvrCluMemberEntry_Object = MibTableRow
svrCluMemberEntry = _SvrCluMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 11, 1)
)
svrCluMemberEntry.setIndexNames(
    (0, "SVRCLU-MIB", "svrCluMemberIndex"),
)
if mibBuilder.loadTexts:
    svrCluMemberEntry.setStatus("mandatory")
_SvrCluMemberIndex_Type = Integer32
_SvrCluMemberIndex_Object = MibTableColumn
svrCluMemberIndex = _SvrCluMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 11, 1, 1),
    _SvrCluMemberIndex_Type()
)
svrCluMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMemberIndex.setStatus("mandatory")
_SvrCluMemberName_Type = DisplayString
_SvrCluMemberName_Object = MibTableColumn
svrCluMemberName = _SvrCluMemberName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 11, 1, 2),
    _SvrCluMemberName_Type()
)
svrCluMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMemberName.setStatus("mandatory")
_SvrCluMemberComment_Type = DisplayString
_SvrCluMemberComment_Object = MibTableColumn
svrCluMemberComment = _SvrCluMemberComment_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 11, 1, 3),
    _SvrCluMemberComment_Type()
)
svrCluMemberComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMemberComment.setStatus("mandatory")
_SvrCluMemberStatus_Type = MemberStatus
_SvrCluMemberStatus_Object = MibTableColumn
svrCluMemberStatus = _SvrCluMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 11, 1, 4),
    _SvrCluMemberStatus_Type()
)
svrCluMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMemberStatus.setStatus("mandatory")
_SvrCluMemberAddressTable_Object = MibTable
svrCluMemberAddressTable = _SvrCluMemberAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    svrCluMemberAddressTable.setStatus("mandatory")
_SvrCluMemberAddressEntry_Object = MibTableRow
svrCluMemberAddressEntry = _SvrCluMemberAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 12, 1)
)
svrCluMemberAddressEntry.setIndexNames(
    (0, "SVRCLU-MIB", "svrCluMemberIndex"),
    (0, "SVRCLU-MIB", "svrCluMemberAddressIndex"),
)
if mibBuilder.loadTexts:
    svrCluMemberAddressEntry.setStatus("mandatory")
_SvrCluMemberAddressIndex_Type = Integer32
_SvrCluMemberAddressIndex_Object = MibTableColumn
svrCluMemberAddressIndex = _SvrCluMemberAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 12, 1, 1),
    _SvrCluMemberAddressIndex_Type()
)
svrCluMemberAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMemberAddressIndex.setStatus("mandatory")
_SvrCluMemberAddress_Type = IpAddress
_SvrCluMemberAddress_Object = MibTableColumn
svrCluMemberAddress = _SvrCluMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 1, 2, 12, 1, 2),
    _SvrCluMemberAddress_Type()
)
svrCluMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCluMemberAddress.setStatus("mandatory")
_SvrCluConformance_ObjectIdentity = ObjectIdentity
svrCluConformance = _SvrCluConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 2)
)

# Managed Objects groups


# Notification objects

svrCluMemberAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 0, 100)
)
svrCluMemberAdded.setObjects(
      *(("SVRCLU-MIB", "svrCluMemberIndex"),
        ("SVRCLU-MIB", "svrCluMemberName"))
)
if mibBuilder.loadTexts:
    svrCluMemberAdded.setStatus(
        ""
    )

svrCluMemberDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 1, 0, 101)
)
svrCluMemberDeleted.setObjects(
      *(("SVRCLU-MIB", "svrCluMemberIndex"),
        ("SVRCLU-MIB", "svrCluMemberName"))
)
if mibBuilder.loadTexts:
    svrCluMemberDeleted.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SVRCLU-MIB",
    **{"ClusterType": ClusterType,
       "ClusterStatus": ClusterStatus,
       "MemberStatus": MemberStatus,
       "dec": dec,
       "ema": ema,
       "mib-extensions-1": mib_extensions_1,
       "svrSystem": svrSystem,
       "svrCluster": svrCluster,
       "svrClu": svrClu,
       "svrCluMemberAdded": svrCluMemberAdded,
       "svrCluMemberDeleted": svrCluMemberDeleted,
       "svrCluObjects": svrCluObjects,
       "svrCluMibInfo": svrCluMibInfo,
       "svrCluMibMajorRev": svrCluMibMajorRev,
       "svrCluMibMinorRev": svrCluMibMinorRev,
       "svrCluClusterInfo": svrCluClusterInfo,
       "svrCluSoftwareVendor": svrCluSoftwareVendor,
       "svrCluSoftwareVersion": svrCluSoftwareVersion,
       "svrCluSoftwareStatus": svrCluSoftwareStatus,
       "svrCluClusterType": svrCluClusterType,
       "svrCluExtensionOID": svrCluExtensionOID,
       "svrCluThisMember": svrCluThisMember,
       "svrCluClusterName": svrCluClusterName,
       "svrCluClusterAddressTable": svrCluClusterAddressTable,
       "svrCluClusterAddressEntry": svrCluClusterAddressEntry,
       "svrCluClusterAddressIndex": svrCluClusterAddressIndex,
       "svrCluClusterAddress": svrCluClusterAddress,
       "svrCluServiceName": svrCluServiceName,
       "svrCluMemberTable": svrCluMemberTable,
       "svrCluMemberEntry": svrCluMemberEntry,
       "svrCluMemberIndex": svrCluMemberIndex,
       "svrCluMemberName": svrCluMemberName,
       "svrCluMemberComment": svrCluMemberComment,
       "svrCluMemberStatus": svrCluMemberStatus,
       "svrCluMemberAddressTable": svrCluMemberAddressTable,
       "svrCluMemberAddressEntry": svrCluMemberAddressEntry,
       "svrCluMemberAddressIndex": svrCluMemberAddressIndex,
       "svrCluMemberAddress": svrCluMemberAddress,
       "svrCluConformance": svrCluConformance}
)
