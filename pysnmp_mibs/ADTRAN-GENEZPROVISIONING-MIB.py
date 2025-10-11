# SNMP MIB module (ADTRAN-GENEZPROVISIONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENEZPROVISIONING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:34 2025
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

(adGenSlotProdPartNumber,
 adGenSlotProdSwVersion) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotProdPartNumber",
    "adGenSlotProdSwVersion")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

(adGenEZProv,
 adGenEZProvID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenEZProv",
    "adGenEZProvID")

(AdGenTrapVersion,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "AdGenTrapVersion")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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

adGenEZProvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 24, 1)
)
if mibBuilder.loadTexts:
    adGenEZProvMIB.setRevisions(
        ("2010-04-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEZProvEvents_ObjectIdentity = ObjectIdentity
adGenEZProvEvents = _AdGenEZProvEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 0)
)
_AdGenEZProvStatus_ObjectIdentity = ObjectIdentity
adGenEZProvStatus = _AdGenEZProvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1)
)
_AdGenEZProvIPAddress_Type = IpAddress
_AdGenEZProvIPAddress_Object = MibScalar
adGenEZProvIPAddress = _AdGenEZProvIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 1),
    _AdGenEZProvIPAddress_Type()
)
adGenEZProvIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvIPAddress.setStatus("current")
_AdGenEZProvSNMPReadCommunity_Type = DisplayString
_AdGenEZProvSNMPReadCommunity_Object = MibScalar
adGenEZProvSNMPReadCommunity = _AdGenEZProvSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 2),
    _AdGenEZProvSNMPReadCommunity_Type()
)
adGenEZProvSNMPReadCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvSNMPReadCommunity.setStatus("current")
_AdGenEZProvSNMPWriteCommunity_Type = DisplayString
_AdGenEZProvSNMPWriteCommunity_Object = MibScalar
adGenEZProvSNMPWriteCommunity = _AdGenEZProvSNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 3),
    _AdGenEZProvSNMPWriteCommunity_Type()
)
adGenEZProvSNMPWriteCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvSNMPWriteCommunity.setStatus("current")
_AdGenEZProvBootCodeVersion_Type = DisplayString
_AdGenEZProvBootCodeVersion_Object = MibScalar
adGenEZProvBootCodeVersion = _AdGenEZProvBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 4),
    _AdGenEZProvBootCodeVersion_Type()
)
adGenEZProvBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvBootCodeVersion.setStatus("current")
_AdGenEZProvAppCodeVersion_Type = DisplayString
_AdGenEZProvAppCodeVersion_Object = MibScalar
adGenEZProvAppCodeVersion = _AdGenEZProvAppCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 5),
    _AdGenEZProvAppCodeVersion_Type()
)
adGenEZProvAppCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvAppCodeVersion.setStatus("current")
_AdGenEZProvConfigCrc32_Type = Unsigned32
_AdGenEZProvConfigCrc32_Object = MibScalar
adGenEZProvConfigCrc32 = _AdGenEZProvConfigCrc32_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 6),
    _AdGenEZProvConfigCrc32_Type()
)
adGenEZProvConfigCrc32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvConfigCrc32.setStatus("current")
_AdGenEZProvStatusString_Type = DisplayString
_AdGenEZProvStatusString_Object = MibScalar
adGenEZProvStatusString = _AdGenEZProvStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 1, 7),
    _AdGenEZProvStatusString_Type()
)
adGenEZProvStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEZProvStatusString.setStatus("current")
_AdGenEZProvConfig_ObjectIdentity = ObjectIdentity
adGenEZProvConfig = _AdGenEZProvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 2)
)
_AdGenEZProvActiveHostIpAddress_Type = IpAddress
_AdGenEZProvActiveHostIpAddress_Object = MibScalar
adGenEZProvActiveHostIpAddress = _AdGenEZProvActiveHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 2, 1),
    _AdGenEZProvActiveHostIpAddress_Type()
)
adGenEZProvActiveHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEZProvActiveHostIpAddress.setStatus("current")
_AdGenEZProvBootCodeFilename_Type = DisplayString
_AdGenEZProvBootCodeFilename_Object = MibScalar
adGenEZProvBootCodeFilename = _AdGenEZProvBootCodeFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 2, 2),
    _AdGenEZProvBootCodeFilename_Type()
)
adGenEZProvBootCodeFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEZProvBootCodeFilename.setStatus("current")
_AdGenEZProvAppCodeFilename_Type = DisplayString
_AdGenEZProvAppCodeFilename_Object = MibScalar
adGenEZProvAppCodeFilename = _AdGenEZProvAppCodeFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 2, 3),
    _AdGenEZProvAppCodeFilename_Type()
)
adGenEZProvAppCodeFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEZProvAppCodeFilename.setStatus("current")
_AdGenEZProvConfigFilename_Type = DisplayString
_AdGenEZProvConfigFilename_Object = MibScalar
adGenEZProvConfigFilename = _AdGenEZProvConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 2, 4),
    _AdGenEZProvConfigFilename_Type()
)
adGenEZProvConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEZProvConfigFilename.setStatus("current")
_AdGenEZProvEnabled_Type = TruthValue
_AdGenEZProvEnabled_Object = MibScalar
adGenEZProvEnabled = _AdGenEZProvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 2, 5),
    _AdGenEZProvEnabled_Type()
)
adGenEZProvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEZProvEnabled.setStatus("current")
_AdGenEZProvHosts_ObjectIdentity = ObjectIdentity
adGenEZProvHosts = _AdGenEZProvHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 3)
)
_AdGenEZProvHostTable_Object = MibTable
adGenEZProvHostTable = _AdGenEZProvHostTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 3, 1)
)
if mibBuilder.loadTexts:
    adGenEZProvHostTable.setStatus("current")
_AdGenEZProvHostEntry_Object = MibTableRow
adGenEZProvHostEntry = _AdGenEZProvHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 3, 1, 1)
)
adGenEZProvHostEntry.setIndexNames(
    (0, "ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvHostIP"),
)
if mibBuilder.loadTexts:
    adGenEZProvHostEntry.setStatus("current")
_AdGenEZProvHostIP_Type = IpAddress
_AdGenEZProvHostIP_Object = MibTableColumn
adGenEZProvHostIP = _AdGenEZProvHostIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 3, 1, 1, 1),
    _AdGenEZProvHostIP_Type()
)
adGenEZProvHostIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEZProvHostIP.setStatus("current")
_AdGenEZProvHostTrapVersion_Type = AdGenTrapVersion
_AdGenEZProvHostTrapVersion_Object = MibTableColumn
adGenEZProvHostTrapVersion = _AdGenEZProvHostTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 3, 1, 1, 2),
    _AdGenEZProvHostTrapVersion_Type()
)
adGenEZProvHostTrapVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEZProvHostTrapVersion.setStatus("current")
_AdGenEZProvHostRowStatus_Type = RowStatus
_AdGenEZProvHostRowStatus_Object = MibTableColumn
adGenEZProvHostRowStatus = _AdGenEZProvHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 3, 1, 1, 3),
    _AdGenEZProvHostRowStatus_Type()
)
adGenEZProvHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEZProvHostRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

adGenEZProvRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 0, 1)
)
adGenEZProvRequest.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvSNMPReadCommunity"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvSNMPWriteCommunity"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdPartNumber"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvIPAddress"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvBootCodeVersion"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvAppCodeVersion"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvConfigCrc32"))
)
if mibBuilder.loadTexts:
    adGenEZProvRequest.setStatus(
        "current"
    )

adGenEZProvFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 24, 0, 2)
)
adGenEZProvFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdPartNumber"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvIPAddress"),
        ("ADTRAN-GENEZPROVISIONING-MIB", "adGenEZProvStatusString"))
)
if mibBuilder.loadTexts:
    adGenEZProvFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENEZPROVISIONING-MIB",
    **{"adGenEZProvEvents": adGenEZProvEvents,
       "adGenEZProvRequest": adGenEZProvRequest,
       "adGenEZProvFailure": adGenEZProvFailure,
       "adGenEZProvStatus": adGenEZProvStatus,
       "adGenEZProvIPAddress": adGenEZProvIPAddress,
       "adGenEZProvSNMPReadCommunity": adGenEZProvSNMPReadCommunity,
       "adGenEZProvSNMPWriteCommunity": adGenEZProvSNMPWriteCommunity,
       "adGenEZProvBootCodeVersion": adGenEZProvBootCodeVersion,
       "adGenEZProvAppCodeVersion": adGenEZProvAppCodeVersion,
       "adGenEZProvConfigCrc32": adGenEZProvConfigCrc32,
       "adGenEZProvStatusString": adGenEZProvStatusString,
       "adGenEZProvConfig": adGenEZProvConfig,
       "adGenEZProvActiveHostIpAddress": adGenEZProvActiveHostIpAddress,
       "adGenEZProvBootCodeFilename": adGenEZProvBootCodeFilename,
       "adGenEZProvAppCodeFilename": adGenEZProvAppCodeFilename,
       "adGenEZProvConfigFilename": adGenEZProvConfigFilename,
       "adGenEZProvEnabled": adGenEZProvEnabled,
       "adGenEZProvHosts": adGenEZProvHosts,
       "adGenEZProvHostTable": adGenEZProvHostTable,
       "adGenEZProvHostEntry": adGenEZProvHostEntry,
       "adGenEZProvHostIP": adGenEZProvHostIP,
       "adGenEZProvHostTrapVersion": adGenEZProvHostTrapVersion,
       "adGenEZProvHostRowStatus": adGenEZProvHostRowStatus,
       "adGenEZProvMIB": adGenEZProvMIB}
)
