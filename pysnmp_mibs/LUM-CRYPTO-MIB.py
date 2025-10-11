# SNMP MIB module (LUM-CRYPTO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-CRYPTO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:30 2025
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

(lumCryptoMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumCryptoMIB",
    "lumModules")

(AdminStatusWithNA,
 CommandString,
 FaultStatusWithNA,
 MgmtNameString,
 OnOff,
 OperStatusWithNA,
 ResetWithNA,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "CommandString",
    "FaultStatusWithNA",
    "MgmtNameString",
    "OnOff",
    "OperStatusWithNA",
    "ResetWithNA",
    "SignalStatusWithNA",
    "Unsigned32WithNA")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumCryptoMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 71)
)
if mibBuilder.loadTexts:
    lumCryptoMIBModule.setRevisions(
        ("2018-10-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CryptoPeriodWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("period15minutes", 1),
          ("period24hours", 2),
          ("notApplicable", 2147483647))
    )



class CryptoMeasurementTypeWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("both", 3),
          ("notApplicable", 2147483647))
    )



class BooleanWithNA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )



# MIB Managed Objects in the order of their OIDs

_LumCryptoConfs_ObjectIdentity = ObjectIdentity
lumCryptoConfs = _LumCryptoConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1)
)
_LumCryptoGroups_ObjectIdentity = ObjectIdentity
lumCryptoGroups = _LumCryptoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1)
)
_LumCryptoCompl_ObjectIdentity = ObjectIdentity
lumCryptoCompl = _LumCryptoCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 2)
)
_LumCryptoMIBObjects_ObjectIdentity = ObjectIdentity
lumCryptoMIBObjects = _LumCryptoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2)
)
_CryptoGeneral_ObjectIdentity = ObjectIdentity
cryptoGeneral = _CryptoGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1)
)
_CryptoGeneralConfigLastChangeTime_Type = DateAndTime
_CryptoGeneralConfigLastChangeTime_Object = MibScalar
cryptoGeneralConfigLastChangeTime = _CryptoGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 1),
    _CryptoGeneralConfigLastChangeTime_Type()
)
cryptoGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralConfigLastChangeTime.setStatus("current")
_CryptoGeneralStateLastChangeTime_Type = DateAndTime
_CryptoGeneralStateLastChangeTime_Object = MibScalar
cryptoGeneralStateLastChangeTime = _CryptoGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 2),
    _CryptoGeneralStateLastChangeTime_Type()
)
cryptoGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralStateLastChangeTime.setStatus("current")
_CryptoGeneralCryptoAuthTableSize_Type = Unsigned32
_CryptoGeneralCryptoAuthTableSize_Object = MibScalar
cryptoGeneralCryptoAuthTableSize = _CryptoGeneralCryptoAuthTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 3),
    _CryptoGeneralCryptoAuthTableSize_Type()
)
cryptoGeneralCryptoAuthTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoAuthTableSize.setStatus("current")
_CryptoGeneralCryptoAuthConfigLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoAuthConfigLastChangeTime_Object = MibScalar
cryptoGeneralCryptoAuthConfigLastChangeTime = _CryptoGeneralCryptoAuthConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 4),
    _CryptoGeneralCryptoAuthConfigLastChangeTime_Type()
)
cryptoGeneralCryptoAuthConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoAuthConfigLastChangeTime.setStatus("current")
_CryptoGeneralCryptoAuthStateLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoAuthStateLastChangeTime_Object = MibScalar
cryptoGeneralCryptoAuthStateLastChangeTime = _CryptoGeneralCryptoAuthStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 5),
    _CryptoGeneralCryptoAuthStateLastChangeTime_Type()
)
cryptoGeneralCryptoAuthStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoAuthStateLastChangeTime.setStatus("current")
_CryptoGeneralCryptoIKEPeerTableSize_Type = Unsigned32
_CryptoGeneralCryptoIKEPeerTableSize_Object = MibScalar
cryptoGeneralCryptoIKEPeerTableSize = _CryptoGeneralCryptoIKEPeerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 6),
    _CryptoGeneralCryptoIKEPeerTableSize_Type()
)
cryptoGeneralCryptoIKEPeerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoIKEPeerTableSize.setStatus("current")
_CryptoGeneralCryptoIKEPeerConfigLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoIKEPeerConfigLastChangeTime_Object = MibScalar
cryptoGeneralCryptoIKEPeerConfigLastChangeTime = _CryptoGeneralCryptoIKEPeerConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 7),
    _CryptoGeneralCryptoIKEPeerConfigLastChangeTime_Type()
)
cryptoGeneralCryptoIKEPeerConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoIKEPeerConfigLastChangeTime.setStatus("current")
_CryptoGeneralCryptoIKEPeerStateLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoIKEPeerStateLastChangeTime_Object = MibScalar
cryptoGeneralCryptoIKEPeerStateLastChangeTime = _CryptoGeneralCryptoIKEPeerStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 8),
    _CryptoGeneralCryptoIKEPeerStateLastChangeTime_Type()
)
cryptoGeneralCryptoIKEPeerStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoIKEPeerStateLastChangeTime.setStatus("current")
_CryptoGeneralCryptoDataplaneEncryptionTableSize_Type = Unsigned32
_CryptoGeneralCryptoDataplaneEncryptionTableSize_Object = MibScalar
cryptoGeneralCryptoDataplaneEncryptionTableSize = _CryptoGeneralCryptoDataplaneEncryptionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 9),
    _CryptoGeneralCryptoDataplaneEncryptionTableSize_Type()
)
cryptoGeneralCryptoDataplaneEncryptionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoDataplaneEncryptionTableSize.setStatus("current")
_CryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime_Object = MibScalar
cryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime = _CryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 10),
    _CryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime_Type()
)
cryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime.setStatus("current")
_CryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime_Object = MibScalar
cryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime = _CryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 11),
    _CryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime_Type()
)
cryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime.setStatus("current")
_CryptoGeneralCryptoPmadminTableSize_Type = Unsigned32
_CryptoGeneralCryptoPmadminTableSize_Object = MibScalar
cryptoGeneralCryptoPmadminTableSize = _CryptoGeneralCryptoPmadminTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 12),
    _CryptoGeneralCryptoPmadminTableSize_Type()
)
cryptoGeneralCryptoPmadminTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoPmadminTableSize.setStatus("current")
_CryptoGeneralCryptoPmadminConfigLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoPmadminConfigLastChangeTime_Object = MibScalar
cryptoGeneralCryptoPmadminConfigLastChangeTime = _CryptoGeneralCryptoPmadminConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 13),
    _CryptoGeneralCryptoPmadminConfigLastChangeTime_Type()
)
cryptoGeneralCryptoPmadminConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoPmadminConfigLastChangeTime.setStatus("current")
_CryptoGeneralCryptoPmadminStateLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoPmadminStateLastChangeTime_Object = MibScalar
cryptoGeneralCryptoPmadminStateLastChangeTime = _CryptoGeneralCryptoPmadminStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 14),
    _CryptoGeneralCryptoPmadminStateLastChangeTime_Type()
)
cryptoGeneralCryptoPmadminStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoPmadminStateLastChangeTime.setStatus("current")
_CryptoGeneralCryptoPerformanceTableSize_Type = Unsigned32
_CryptoGeneralCryptoPerformanceTableSize_Object = MibScalar
cryptoGeneralCryptoPerformanceTableSize = _CryptoGeneralCryptoPerformanceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 15),
    _CryptoGeneralCryptoPerformanceTableSize_Type()
)
cryptoGeneralCryptoPerformanceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoPerformanceTableSize.setStatus("current")
_CryptoGeneralCryptoPerformanceConfigLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoPerformanceConfigLastChangeTime_Object = MibScalar
cryptoGeneralCryptoPerformanceConfigLastChangeTime = _CryptoGeneralCryptoPerformanceConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 16),
    _CryptoGeneralCryptoPerformanceConfigLastChangeTime_Type()
)
cryptoGeneralCryptoPerformanceConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoPerformanceConfigLastChangeTime.setStatus("current")
_CryptoGeneralCryptoPerformanceStateLastChangeTime_Type = DateAndTime
_CryptoGeneralCryptoPerformanceStateLastChangeTime_Object = MibScalar
cryptoGeneralCryptoPerformanceStateLastChangeTime = _CryptoGeneralCryptoPerformanceStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 1, 17),
    _CryptoGeneralCryptoPerformanceStateLastChangeTime_Type()
)
cryptoGeneralCryptoPerformanceStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoGeneralCryptoPerformanceStateLastChangeTime.setStatus("current")
_CryptoAuthList_ObjectIdentity = ObjectIdentity
cryptoAuthList = _CryptoAuthList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2)
)
_CryptoAuthTable_Object = MibTable
cryptoAuthTable = _CryptoAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cryptoAuthTable.setStatus("current")
_CryptoAuthEntry_Object = MibTableRow
cryptoAuthEntry = _CryptoAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1)
)
cryptoAuthEntry.setIndexNames(
    (0, "LUM-CRYPTO-MIB", "cryptoAuthIndex"),
)
if mibBuilder.loadTexts:
    cryptoAuthEntry.setStatus("current")
_CryptoAuthIndex_Type = Unsigned32
_CryptoAuthIndex_Object = MibTableColumn
cryptoAuthIndex = _CryptoAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 1),
    _CryptoAuthIndex_Type()
)
cryptoAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthIndex.setStatus("current")
_CryptoAuthUId_Type = Unsigned32
_CryptoAuthUId_Object = MibTableColumn
cryptoAuthUId = _CryptoAuthUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 2),
    _CryptoAuthUId_Type()
)
cryptoAuthUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthUId.setStatus("current")
_CryptoAuthName_Type = MgmtNameString
_CryptoAuthName_Object = MibTableColumn
cryptoAuthName = _CryptoAuthName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 3),
    _CryptoAuthName_Type()
)
cryptoAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthName.setStatus("current")
_CryptoAuthIdentity_Type = MgmtNameString
_CryptoAuthIdentity_Object = MibTableColumn
cryptoAuthIdentity = _CryptoAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 4),
    _CryptoAuthIdentity_Type()
)
cryptoAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthIdentity.setStatus("current")


class _CryptoAuthReAuthInterval_Type(Unsigned32):
    """Custom type cryptoAuthReAuthInterval based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CryptoAuthReAuthInterval_Type.__name__ = "Unsigned32"
_CryptoAuthReAuthInterval_Object = MibTableColumn
cryptoAuthReAuthInterval = _CryptoAuthReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 5),
    _CryptoAuthReAuthInterval_Type()
)
cryptoAuthReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoAuthReAuthInterval.setStatus("current")
_CryptoAuthReAuth_Type = CommandString
_CryptoAuthReAuth_Object = MibTableColumn
cryptoAuthReAuth = _CryptoAuthReAuth_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 6),
    _CryptoAuthReAuth_Type()
)
cryptoAuthReAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthReAuth.setStatus("current")
_CryptoAuthCreateIKEPeer_Type = CommandString
_CryptoAuthCreateIKEPeer_Object = MibTableColumn
cryptoAuthCreateIKEPeer = _CryptoAuthCreateIKEPeer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 7),
    _CryptoAuthCreateIKEPeer_Type()
)
cryptoAuthCreateIKEPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthCreateIKEPeer.setStatus("current")
_CryptoAuthenticationGenerateUniqueID_Type = CommandString
_CryptoAuthenticationGenerateUniqueID_Object = MibTableColumn
cryptoAuthenticationGenerateUniqueID = _CryptoAuthenticationGenerateUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 8),
    _CryptoAuthenticationGenerateUniqueID_Type()
)
cryptoAuthenticationGenerateUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoAuthenticationGenerateUniqueID.setStatus("current")


class _CryptoGeneratedUniqueIdentity_Type(MgmtNameString):
    """Custom type cryptoGeneratedUniqueIdentity based on MgmtNameString"""
    defaultValue = OctetString("")


_CryptoGeneratedUniqueIdentity_Type.__name__ = "MgmtNameString"
_CryptoGeneratedUniqueIdentity_Object = MibTableColumn
cryptoGeneratedUniqueIdentity = _CryptoGeneratedUniqueIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 2, 1, 1, 9),
    _CryptoGeneratedUniqueIdentity_Type()
)
cryptoGeneratedUniqueIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoGeneratedUniqueIdentity.setStatus("current")
_CryptoIKEPeerList_ObjectIdentity = ObjectIdentity
cryptoIKEPeerList = _CryptoIKEPeerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3)
)
_CryptoIKEPeerTable_Object = MibTable
cryptoIKEPeerTable = _CryptoIKEPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cryptoIKEPeerTable.setStatus("current")
_CryptoIKEPeerEntry_Object = MibTableRow
cryptoIKEPeerEntry = _CryptoIKEPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1)
)
cryptoIKEPeerEntry.setIndexNames(
    (0, "LUM-CRYPTO-MIB", "cryptoIKEPeerIndex"),
)
if mibBuilder.loadTexts:
    cryptoIKEPeerEntry.setStatus("current")
_CryptoIKEPeerIndex_Type = Unsigned32
_CryptoIKEPeerIndex_Object = MibTableColumn
cryptoIKEPeerIndex = _CryptoIKEPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 1),
    _CryptoIKEPeerIndex_Type()
)
cryptoIKEPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerIndex.setStatus("current")
_CryptoIKEPeerUId_Type = Unsigned32
_CryptoIKEPeerUId_Object = MibTableColumn
cryptoIKEPeerUId = _CryptoIKEPeerUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 2),
    _CryptoIKEPeerUId_Type()
)
cryptoIKEPeerUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerUId.setStatus("current")
_CryptoIKEPeerName_Type = MgmtNameString
_CryptoIKEPeerName_Object = MibTableColumn
cryptoIKEPeerName = _CryptoIKEPeerName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 3),
    _CryptoIKEPeerName_Type()
)
cryptoIKEPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerName.setStatus("current")


class _CryptoIKEPeerIdentity_Type(MgmtNameString):
    """Custom type cryptoIKEPeerIdentity based on MgmtNameString"""
    defaultValue = OctetString("")


_CryptoIKEPeerIdentity_Type.__name__ = "MgmtNameString"
_CryptoIKEPeerIdentity_Object = MibTableColumn
cryptoIKEPeerIdentity = _CryptoIKEPeerIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 4),
    _CryptoIKEPeerIdentity_Type()
)
cryptoIKEPeerIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerIdentity.setStatus("current")


class _CryptoIKEPeerExpectedIKEPeerIdentity_Type(MgmtNameString):
    """Custom type cryptoIKEPeerExpectedIKEPeerIdentity based on MgmtNameString"""
    defaultValue = OctetString("")


_CryptoIKEPeerExpectedIKEPeerIdentity_Type.__name__ = "MgmtNameString"
_CryptoIKEPeerExpectedIKEPeerIdentity_Object = MibTableColumn
cryptoIKEPeerExpectedIKEPeerIdentity = _CryptoIKEPeerExpectedIKEPeerIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 5),
    _CryptoIKEPeerExpectedIKEPeerIdentity_Type()
)
cryptoIKEPeerExpectedIKEPeerIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoIKEPeerExpectedIKEPeerIdentity.setStatus("current")


class _CryptoIKEPeerAuthScheme_Type(Integer32):
    """Custom type cryptoIKEPeerAuthScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("psk", 1)
    )


_CryptoIKEPeerAuthScheme_Type.__name__ = "Integer32"
_CryptoIKEPeerAuthScheme_Object = MibTableColumn
cryptoIKEPeerAuthScheme = _CryptoIKEPeerAuthScheme_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 6),
    _CryptoIKEPeerAuthScheme_Type()
)
cryptoIKEPeerAuthScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoIKEPeerAuthScheme.setStatus("current")


class _CryptoIKEPeerPSK_Type(DisplayString):
    """Custom type cryptoIKEPeerPSK based on DisplayString"""
    defaultValue = OctetString("")


_CryptoIKEPeerPSK_Type.__name__ = "DisplayString"
_CryptoIKEPeerPSK_Object = MibTableColumn
cryptoIKEPeerPSK = _CryptoIKEPeerPSK_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 7),
    _CryptoIKEPeerPSK_Type()
)
cryptoIKEPeerPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoIKEPeerPSK.setStatus("current")


class _CryptoIKEPeerAdminStatus_Type(Integer32):
    """Custom type cryptoIKEPeerAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("service", 2))
    )


_CryptoIKEPeerAdminStatus_Type.__name__ = "Integer32"
_CryptoIKEPeerAdminStatus_Object = MibTableColumn
cryptoIKEPeerAdminStatus = _CryptoIKEPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 8),
    _CryptoIKEPeerAdminStatus_Type()
)
cryptoIKEPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoIKEPeerAdminStatus.setStatus("current")
_CryptoIKEPeerOperStatus_Type = OperStatusWithNA
_CryptoIKEPeerOperStatus_Object = MibTableColumn
cryptoIKEPeerOperStatus = _CryptoIKEPeerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 9),
    _CryptoIKEPeerOperStatus_Type()
)
cryptoIKEPeerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerOperStatus.setStatus("current")
_CryptoIKEPeerLastReAuthTime_Type = DateAndTime
_CryptoIKEPeerLastReAuthTime_Object = MibTableColumn
cryptoIKEPeerLastReAuthTime = _CryptoIKEPeerLastReAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 10),
    _CryptoIKEPeerLastReAuthTime_Type()
)
cryptoIKEPeerLastReAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerLastReAuthTime.setStatus("current")


class _CryptoIKEPeerReKeyInterval_Type(Unsigned32):
    """Custom type cryptoIKEPeerReKeyInterval based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86400),
    )


_CryptoIKEPeerReKeyInterval_Type.__name__ = "Unsigned32"
_CryptoIKEPeerReKeyInterval_Object = MibTableColumn
cryptoIKEPeerReKeyInterval = _CryptoIKEPeerReKeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 11),
    _CryptoIKEPeerReKeyInterval_Type()
)
cryptoIKEPeerReKeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoIKEPeerReKeyInterval.setStatus("current")
_CryptoIKEPeerLastReKeyTime_Type = DateAndTime
_CryptoIKEPeerLastReKeyTime_Object = MibTableColumn
cryptoIKEPeerLastReKeyTime = _CryptoIKEPeerLastReKeyTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 12),
    _CryptoIKEPeerLastReKeyTime_Type()
)
cryptoIKEPeerLastReKeyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerLastReKeyTime.setStatus("current")
_CryptoIKEPeerReKey_Type = CommandString
_CryptoIKEPeerReKey_Object = MibTableColumn
cryptoIKEPeerReKey = _CryptoIKEPeerReKey_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 13),
    _CryptoIKEPeerReKey_Type()
)
cryptoIKEPeerReKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerReKey.setStatus("current")
_CryptoIKEPeerConfigMismatch_Type = FaultStatusWithNA
_CryptoIKEPeerConfigMismatch_Object = MibTableColumn
cryptoIKEPeerConfigMismatch = _CryptoIKEPeerConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 14),
    _CryptoIKEPeerConfigMismatch_Type()
)
cryptoIKEPeerConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerConfigMismatch.setStatus("current")
_CryptoIKEPeerUnreachable_Type = FaultStatusWithNA
_CryptoIKEPeerUnreachable_Object = MibTableColumn
cryptoIKEPeerUnreachable = _CryptoIKEPeerUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 15),
    _CryptoIKEPeerUnreachable_Type()
)
cryptoIKEPeerUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerUnreachable.setStatus("current")
_CryptoIKEPeerAuthenticationFailure_Type = FaultStatusWithNA
_CryptoIKEPeerAuthenticationFailure_Object = MibTableColumn
cryptoIKEPeerAuthenticationFailure = _CryptoIKEPeerAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 16),
    _CryptoIKEPeerAuthenticationFailure_Type()
)
cryptoIKEPeerAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerAuthenticationFailure.setStatus("current")
_CryptoIKEPeerReKeyFailure_Type = FaultStatusWithNA
_CryptoIKEPeerReKeyFailure_Object = MibTableColumn
cryptoIKEPeerReKeyFailure = _CryptoIKEPeerReKeyFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 3, 1, 1, 17),
    _CryptoIKEPeerReKeyFailure_Type()
)
cryptoIKEPeerReKeyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoIKEPeerReKeyFailure.setStatus("current")
_CryptoDataplaneEncryptionList_ObjectIdentity = ObjectIdentity
cryptoDataplaneEncryptionList = _CryptoDataplaneEncryptionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4)
)
_CryptoDataplaneEncryptionTable_Object = MibTable
cryptoDataplaneEncryptionTable = _CryptoDataplaneEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionTable.setStatus("current")
_CryptoDataplaneEncryptionEntry_Object = MibTableRow
cryptoDataplaneEncryptionEntry = _CryptoDataplaneEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1)
)
cryptoDataplaneEncryptionEntry.setIndexNames(
    (0, "LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionIndex"),
)
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionEntry.setStatus("current")
_CryptoDataplaneEncryptionIndex_Type = Unsigned32
_CryptoDataplaneEncryptionIndex_Object = MibTableColumn
cryptoDataplaneEncryptionIndex = _CryptoDataplaneEncryptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 1),
    _CryptoDataplaneEncryptionIndex_Type()
)
cryptoDataplaneEncryptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionIndex.setStatus("current")
_CryptoDataplaneEncryptionUId_Type = Unsigned32
_CryptoDataplaneEncryptionUId_Object = MibTableColumn
cryptoDataplaneEncryptionUId = _CryptoDataplaneEncryptionUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 2),
    _CryptoDataplaneEncryptionUId_Type()
)
cryptoDataplaneEncryptionUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionUId.setStatus("current")
_CryptoDataplaneEncryptionName_Type = MgmtNameString
_CryptoDataplaneEncryptionName_Object = MibTableColumn
cryptoDataplaneEncryptionName = _CryptoDataplaneEncryptionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 3),
    _CryptoDataplaneEncryptionName_Type()
)
cryptoDataplaneEncryptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionName.setStatus("current")
_CryptoDataplaneEncryptionLocalDataplaneId_Type = MgmtNameString
_CryptoDataplaneEncryptionLocalDataplaneId_Object = MibTableColumn
cryptoDataplaneEncryptionLocalDataplaneId = _CryptoDataplaneEncryptionLocalDataplaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 4),
    _CryptoDataplaneEncryptionLocalDataplaneId_Type()
)
cryptoDataplaneEncryptionLocalDataplaneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionLocalDataplaneId.setStatus("current")


class _CryptoDataplaneEncryptionExpectedPeerDataplaneId_Type(MgmtNameString):
    """Custom type cryptoDataplaneEncryptionExpectedPeerDataplaneId based on MgmtNameString"""
    defaultValue = OctetString("")


_CryptoDataplaneEncryptionExpectedPeerDataplaneId_Type.__name__ = "MgmtNameString"
_CryptoDataplaneEncryptionExpectedPeerDataplaneId_Object = MibTableColumn
cryptoDataplaneEncryptionExpectedPeerDataplaneId = _CryptoDataplaneEncryptionExpectedPeerDataplaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 5),
    _CryptoDataplaneEncryptionExpectedPeerDataplaneId_Type()
)
cryptoDataplaneEncryptionExpectedPeerDataplaneId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionExpectedPeerDataplaneId.setStatus("current")
_CryptoDataplaneEncryptionDiscoveredPeerDataplaneId_Type = MgmtNameString
_CryptoDataplaneEncryptionDiscoveredPeerDataplaneId_Object = MibTableColumn
cryptoDataplaneEncryptionDiscoveredPeerDataplaneId = _CryptoDataplaneEncryptionDiscoveredPeerDataplaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 6),
    _CryptoDataplaneEncryptionDiscoveredPeerDataplaneId_Type()
)
cryptoDataplaneEncryptionDiscoveredPeerDataplaneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionDiscoveredPeerDataplaneId.setStatus("current")


class _CryptoDataplaneEncryptionOTNOHAllocation_Type(Integer32):
    """Custom type cryptoDataplaneEncryptionOTNOHAllocation based on Integer32"""
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
        *(("apspcctcm3", 1),
          ("apspcctcm1", 2),
          ("tcm1", 3),
          ("tcm3", 4))
    )


_CryptoDataplaneEncryptionOTNOHAllocation_Type.__name__ = "Integer32"
_CryptoDataplaneEncryptionOTNOHAllocation_Object = MibTableColumn
cryptoDataplaneEncryptionOTNOHAllocation = _CryptoDataplaneEncryptionOTNOHAllocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 7),
    _CryptoDataplaneEncryptionOTNOHAllocation_Type()
)
cryptoDataplaneEncryptionOTNOHAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionOTNOHAllocation.setStatus("current")


class _CryptoDataplaneEncryptionIKEPeerIdentity_Type(Integer32):
    """Custom type cryptoDataplaneEncryptionIKEPeerIdentity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ikePeer1", 1),
          ("ikePeer2", 2),
          ("ikePeer3", 3),
          ("ikePeer4", 4),
          ("ikePeer5", 5),
          ("ikePeer6", 6),
          ("ikePeer7", 7),
          ("ikePeer8", 8),
          ("ikePeer9", 9),
          ("ikePeer10", 10),
          ("ikePeer11", 11),
          ("ikePeer12", 12),
          ("ikePeer13", 13),
          ("ikePeer14", 14),
          ("ikePeer15", 15),
          ("ikePeer16", 16),
          ("notApplicable", 2147483647))
    )


_CryptoDataplaneEncryptionIKEPeerIdentity_Type.__name__ = "Integer32"
_CryptoDataplaneEncryptionIKEPeerIdentity_Object = MibTableColumn
cryptoDataplaneEncryptionIKEPeerIdentity = _CryptoDataplaneEncryptionIKEPeerIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 8),
    _CryptoDataplaneEncryptionIKEPeerIdentity_Type()
)
cryptoDataplaneEncryptionIKEPeerIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionIKEPeerIdentity.setStatus("current")


class _CryptoDataplaneEncryptionReKeyInterval_Type(Unsigned32):
    """Custom type cryptoDataplaneEncryptionReKeyInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CryptoDataplaneEncryptionReKeyInterval_Type.__name__ = "Unsigned32"
_CryptoDataplaneEncryptionReKeyInterval_Object = MibTableColumn
cryptoDataplaneEncryptionReKeyInterval = _CryptoDataplaneEncryptionReKeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 9),
    _CryptoDataplaneEncryptionReKeyInterval_Type()
)
cryptoDataplaneEncryptionReKeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionReKeyInterval.setStatus("current")


class _CryptoDataplaneEncryptionFailurePolicy_Type(Integer32):
    """Custom type cryptoDataplaneEncryptionFailurePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continueop", 1),
          ("killtraffic", 2))
    )


_CryptoDataplaneEncryptionFailurePolicy_Type.__name__ = "Integer32"
_CryptoDataplaneEncryptionFailurePolicy_Object = MibTableColumn
cryptoDataplaneEncryptionFailurePolicy = _CryptoDataplaneEncryptionFailurePolicy_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 10),
    _CryptoDataplaneEncryptionFailurePolicy_Type()
)
cryptoDataplaneEncryptionFailurePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionFailurePolicy.setStatus("current")


class _CryptoDataplaneEncryptionTrafficKillTimeOffset_Type(Unsigned32):
    """Custom type cryptoDataplaneEncryptionTrafficKillTimeOffset based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CryptoDataplaneEncryptionTrafficKillTimeOffset_Type.__name__ = "Unsigned32"
_CryptoDataplaneEncryptionTrafficKillTimeOffset_Object = MibTableColumn
cryptoDataplaneEncryptionTrafficKillTimeOffset = _CryptoDataplaneEncryptionTrafficKillTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 11),
    _CryptoDataplaneEncryptionTrafficKillTimeOffset_Type()
)
cryptoDataplaneEncryptionTrafficKillTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionTrafficKillTimeOffset.setStatus("current")


class _CryptoDataplaneEncryptionEncryptionMode_Type(Integer32):
    """Custom type cryptoDataplaneEncryptionEncryptionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 1),
          ("gcm", 2))
    )


_CryptoDataplaneEncryptionEncryptionMode_Type.__name__ = "Integer32"
_CryptoDataplaneEncryptionEncryptionMode_Object = MibTableColumn
cryptoDataplaneEncryptionEncryptionMode = _CryptoDataplaneEncryptionEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 12),
    _CryptoDataplaneEncryptionEncryptionMode_Type()
)
cryptoDataplaneEncryptionEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionEncryptionMode.setStatus("current")
_CryptoDataplaneEncryptionLastReKeyTimeTx_Type = DateAndTime
_CryptoDataplaneEncryptionLastReKeyTimeTx_Object = MibTableColumn
cryptoDataplaneEncryptionLastReKeyTimeTx = _CryptoDataplaneEncryptionLastReKeyTimeTx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 13),
    _CryptoDataplaneEncryptionLastReKeyTimeTx_Type()
)
cryptoDataplaneEncryptionLastReKeyTimeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionLastReKeyTimeTx.setStatus("current")
_CryptoDataplaneEncryptionLastReKeyTimeRx_Type = DateAndTime
_CryptoDataplaneEncryptionLastReKeyTimeRx_Object = MibTableColumn
cryptoDataplaneEncryptionLastReKeyTimeRx = _CryptoDataplaneEncryptionLastReKeyTimeRx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 14),
    _CryptoDataplaneEncryptionLastReKeyTimeRx_Type()
)
cryptoDataplaneEncryptionLastReKeyTimeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionLastReKeyTimeRx.setStatus("current")
_CryptoDataplaneEncryptionPeerDpIdMismatch_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionPeerDpIdMismatch_Object = MibTableColumn
cryptoDataplaneEncryptionPeerDpIdMismatch = _CryptoDataplaneEncryptionPeerDpIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 15),
    _CryptoDataplaneEncryptionPeerDpIdMismatch_Type()
)
cryptoDataplaneEncryptionPeerDpIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionPeerDpIdMismatch.setStatus("current")
_CryptoDataplaneEncryptionConfigMismatch_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionConfigMismatch_Object = MibTableColumn
cryptoDataplaneEncryptionConfigMismatch = _CryptoDataplaneEncryptionConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 16),
    _CryptoDataplaneEncryptionConfigMismatch_Type()
)
cryptoDataplaneEncryptionConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionConfigMismatch.setStatus("current")
_CryptoDataplaneEncryptionReKeyFailure_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionReKeyFailure_Object = MibTableColumn
cryptoDataplaneEncryptionReKeyFailure = _CryptoDataplaneEncryptionReKeyFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 17),
    _CryptoDataplaneEncryptionReKeyFailure_Type()
)
cryptoDataplaneEncryptionReKeyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionReKeyFailure.setStatus("current")
_CryptoDataplaneEncryptionRXKeyRotationFailure_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionRXKeyRotationFailure_Object = MibTableColumn
cryptoDataplaneEncryptionRXKeyRotationFailure = _CryptoDataplaneEncryptionRXKeyRotationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 18),
    _CryptoDataplaneEncryptionRXKeyRotationFailure_Type()
)
cryptoDataplaneEncryptionRXKeyRotationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionRXKeyRotationFailure.setStatus("current")
_CryptoDataplaneEncryptionIVExhausted_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionIVExhausted_Object = MibTableColumn
cryptoDataplaneEncryptionIVExhausted = _CryptoDataplaneEncryptionIVExhausted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 19),
    _CryptoDataplaneEncryptionIVExhausted_Type()
)
cryptoDataplaneEncryptionIVExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionIVExhausted.setStatus("current")
_CryptoDataplaneEncryptionFunctionBlocked_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionFunctionBlocked_Object = MibTableColumn
cryptoDataplaneEncryptionFunctionBlocked = _CryptoDataplaneEncryptionFunctionBlocked_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 20),
    _CryptoDataplaneEncryptionFunctionBlocked_Type()
)
cryptoDataplaneEncryptionFunctionBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionFunctionBlocked.setStatus("current")
_CryptoDataplaneEncryptionUnexpectedRxKeyId_Type = FaultStatusWithNA
_CryptoDataplaneEncryptionUnexpectedRxKeyId_Object = MibTableColumn
cryptoDataplaneEncryptionUnexpectedRxKeyId = _CryptoDataplaneEncryptionUnexpectedRxKeyId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 21),
    _CryptoDataplaneEncryptionUnexpectedRxKeyId_Type()
)
cryptoDataplaneEncryptionUnexpectedRxKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionUnexpectedRxKeyId.setStatus("current")
_CryptoDataplaneEncryptionReKey_Type = CommandString
_CryptoDataplaneEncryptionReKey_Object = MibTableColumn
cryptoDataplaneEncryptionReKey = _CryptoDataplaneEncryptionReKey_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 4, 1, 1, 22),
    _CryptoDataplaneEncryptionReKey_Type()
)
cryptoDataplaneEncryptionReKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionReKey.setStatus("current")
_CryptoPmadminList_ObjectIdentity = ObjectIdentity
cryptoPmadminList = _CryptoPmadminList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5)
)
_CryptoPmadminTable_Object = MibTable
cryptoPmadminTable = _CryptoPmadminTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cryptoPmadminTable.setStatus("current")
_CryptoPmadminEntry_Object = MibTableRow
cryptoPmadminEntry = _CryptoPmadminEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1, 1)
)
cryptoPmadminEntry.setIndexNames(
    (0, "LUM-CRYPTO-MIB", "cryptoPmadminIndex"),
)
if mibBuilder.loadTexts:
    cryptoPmadminEntry.setStatus("current")
_CryptoPmadminIndex_Type = Unsigned32
_CryptoPmadminIndex_Object = MibTableColumn
cryptoPmadminIndex = _CryptoPmadminIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1, 1, 1),
    _CryptoPmadminIndex_Type()
)
cryptoPmadminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPmadminIndex.setStatus("current")
_CryptoPmadminName_Type = MgmtNameString
_CryptoPmadminName_Object = MibTableColumn
cryptoPmadminName = _CryptoPmadminName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1, 1, 2),
    _CryptoPmadminName_Type()
)
cryptoPmadminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoPmadminName.setStatus("current")
_CryptoPmadminUId_Type = Unsigned32
_CryptoPmadminUId_Object = MibTableColumn
cryptoPmadminUId = _CryptoPmadminUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1, 1, 3),
    _CryptoPmadminUId_Type()
)
cryptoPmadminUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPmadminUId.setStatus("current")
_CryptoPmadminConnAdminIfIndex_Type = Unsigned32WithNA
_CryptoPmadminConnAdminIfIndex_Object = MibTableColumn
cryptoPmadminConnAdminIfIndex = _CryptoPmadminConnAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1, 1, 4),
    _CryptoPmadminConnAdminIfIndex_Type()
)
cryptoPmadminConnAdminIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoPmadminConnAdminIfIndex.setStatus("current")


class _CryptoPmadminUpId_Type(Unsigned32):
    """Custom type cryptoPmadminUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CryptoPmadminUpId_Type.__name__ = "Unsigned32"
_CryptoPmadminUpId_Object = MibTableColumn
cryptoPmadminUpId = _CryptoPmadminUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 5, 1, 1, 5),
    _CryptoPmadminUpId_Type()
)
cryptoPmadminUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPmadminUpId.setStatus("current")
_CryptoPerformanceList_ObjectIdentity = ObjectIdentity
cryptoPerformanceList = _CryptoPerformanceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6)
)
_CryptoPerformanceTable_Object = MibTable
cryptoPerformanceTable = _CryptoPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cryptoPerformanceTable.setStatus("current")
_CryptoPerformanceEntry_Object = MibTableRow
cryptoPerformanceEntry = _CryptoPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1)
)
cryptoPerformanceEntry.setIndexNames(
    (0, "LUM-CRYPTO-MIB", "cryptoPerformanceIndex"),
)
if mibBuilder.loadTexts:
    cryptoPerformanceEntry.setStatus("current")
_CryptoPerformanceIndex_Type = Unsigned32
_CryptoPerformanceIndex_Object = MibTableColumn
cryptoPerformanceIndex = _CryptoPerformanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 1),
    _CryptoPerformanceIndex_Type()
)
cryptoPerformanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceIndex.setStatus("current")
_CryptoPerformanceName_Type = MgmtNameString
_CryptoPerformanceName_Object = MibTableColumn
cryptoPerformanceName = _CryptoPerformanceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 2),
    _CryptoPerformanceName_Type()
)
cryptoPerformanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoPerformanceName.setStatus("current")
_CryptoPerformanceUId_Type = Unsigned32
_CryptoPerformanceUId_Object = MibTableColumn
cryptoPerformanceUId = _CryptoPerformanceUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 3),
    _CryptoPerformanceUId_Type()
)
cryptoPerformanceUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceUId.setStatus("current")
_CryptoPerformanceConnAdminIfIndex_Type = Unsigned32WithNA
_CryptoPerformanceConnAdminIfIndex_Object = MibTableColumn
cryptoPerformanceConnAdminIfIndex = _CryptoPerformanceConnAdminIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 4),
    _CryptoPerformanceConnAdminIfIndex_Type()
)
cryptoPerformanceConnAdminIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoPerformanceConnAdminIfIndex.setStatus("current")
_CryptoPerformancePeriod_Type = CryptoPeriodWithNA
_CryptoPerformancePeriod_Object = MibTableColumn
cryptoPerformancePeriod = _CryptoPerformancePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 5),
    _CryptoPerformancePeriod_Type()
)
cryptoPerformancePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoPerformancePeriod.setStatus("current")
_CryptoPerformanceType_Type = CryptoMeasurementTypeWithNA
_CryptoPerformanceType_Object = MibTableColumn
cryptoPerformanceType = _CryptoPerformanceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 6),
    _CryptoPerformanceType_Type()
)
cryptoPerformanceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cryptoPerformanceType.setStatus("current")
_CryptoPerformanceCounterNulledFrames_Type = Counter64
_CryptoPerformanceCounterNulledFrames_Object = MibTableColumn
cryptoPerformanceCounterNulledFrames = _CryptoPerformanceCounterNulledFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 7),
    _CryptoPerformanceCounterNulledFrames_Type()
)
cryptoPerformanceCounterNulledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterNulledFrames.setStatus("current")
_CryptoPerformanceCounterAuthFail_Type = Counter64
_CryptoPerformanceCounterAuthFail_Object = MibTableColumn
cryptoPerformanceCounterAuthFail = _CryptoPerformanceCounterAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 8),
    _CryptoPerformanceCounterAuthFail_Type()
)
cryptoPerformanceCounterAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterAuthFail.setStatus("current")
_CryptoPerformanceCounterIvTrouble_Type = Counter64
_CryptoPerformanceCounterIvTrouble_Object = MibTableColumn
cryptoPerformanceCounterIvTrouble = _CryptoPerformanceCounterIvTrouble_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 9),
    _CryptoPerformanceCounterIvTrouble_Type()
)
cryptoPerformanceCounterIvTrouble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterIvTrouble.setStatus("current")
_CryptoPerformanceCounterReplayErr_Type = Counter64
_CryptoPerformanceCounterReplayErr_Object = MibTableColumn
cryptoPerformanceCounterReplayErr = _CryptoPerformanceCounterReplayErr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 10),
    _CryptoPerformanceCounterReplayErr_Type()
)
cryptoPerformanceCounterReplayErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterReplayErr.setStatus("current")
_CryptoPerformanceCounterTotalFrames_Type = Counter64
_CryptoPerformanceCounterTotalFrames_Object = MibTableColumn
cryptoPerformanceCounterTotalFrames = _CryptoPerformanceCounterTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 11),
    _CryptoPerformanceCounterTotalFrames_Type()
)
cryptoPerformanceCounterTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterTotalFrames.setStatus("current")
_CryptoPerformanceCounterAuthFrames_Type = Counter64
_CryptoPerformanceCounterAuthFrames_Object = MibTableColumn
cryptoPerformanceCounterAuthFrames = _CryptoPerformanceCounterAuthFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 12),
    _CryptoPerformanceCounterAuthFrames_Type()
)
cryptoPerformanceCounterAuthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterAuthFrames.setStatus("current")
_CryptoPerformanceCounterEncryptedFrames_Type = Counter64
_CryptoPerformanceCounterEncryptedFrames_Object = MibTableColumn
cryptoPerformanceCounterEncryptedFrames = _CryptoPerformanceCounterEncryptedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 13),
    _CryptoPerformanceCounterEncryptedFrames_Type()
)
cryptoPerformanceCounterEncryptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceCounterEncryptedFrames.setStatus("current")


class _CryptoPerformanceThresholdNulledFrames_Type(Counter64):
    """Custom type cryptoPerformanceThresholdNulledFrames based on Counter64"""
    defaultValue = 20


_CryptoPerformanceThresholdNulledFrames_Type.__name__ = "Counter64"
_CryptoPerformanceThresholdNulledFrames_Object = MibTableColumn
cryptoPerformanceThresholdNulledFrames = _CryptoPerformanceThresholdNulledFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 14),
    _CryptoPerformanceThresholdNulledFrames_Type()
)
cryptoPerformanceThresholdNulledFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPerformanceThresholdNulledFrames.setStatus("current")


class _CryptoPerformanceThresholdAuthFail_Type(Counter64):
    """Custom type cryptoPerformanceThresholdAuthFail based on Counter64"""
    defaultValue = 20


_CryptoPerformanceThresholdAuthFail_Type.__name__ = "Counter64"
_CryptoPerformanceThresholdAuthFail_Object = MibTableColumn
cryptoPerformanceThresholdAuthFail = _CryptoPerformanceThresholdAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 15),
    _CryptoPerformanceThresholdAuthFail_Type()
)
cryptoPerformanceThresholdAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPerformanceThresholdAuthFail.setStatus("current")


class _CryptoPerformanceThresholdIvTrouble_Type(Counter64):
    """Custom type cryptoPerformanceThresholdIvTrouble based on Counter64"""
    defaultValue = 20


_CryptoPerformanceThresholdIvTrouble_Type.__name__ = "Counter64"
_CryptoPerformanceThresholdIvTrouble_Object = MibTableColumn
cryptoPerformanceThresholdIvTrouble = _CryptoPerformanceThresholdIvTrouble_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 16),
    _CryptoPerformanceThresholdIvTrouble_Type()
)
cryptoPerformanceThresholdIvTrouble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPerformanceThresholdIvTrouble.setStatus("current")


class _CryptoPerformanceThresholdReplayErr_Type(Counter64):
    """Custom type cryptoPerformanceThresholdReplayErr based on Counter64"""
    defaultValue = 20


_CryptoPerformanceThresholdReplayErr_Type.__name__ = "Counter64"
_CryptoPerformanceThresholdReplayErr_Object = MibTableColumn
cryptoPerformanceThresholdReplayErr = _CryptoPerformanceThresholdReplayErr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 17),
    _CryptoPerformanceThresholdReplayErr_Type()
)
cryptoPerformanceThresholdReplayErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cryptoPerformanceThresholdReplayErr.setStatus("current")
_CryptoPerformanceFaultStatusNulledFrames_Type = FaultStatusWithNA
_CryptoPerformanceFaultStatusNulledFrames_Object = MibTableColumn
cryptoPerformanceFaultStatusNulledFrames = _CryptoPerformanceFaultStatusNulledFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 18),
    _CryptoPerformanceFaultStatusNulledFrames_Type()
)
cryptoPerformanceFaultStatusNulledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceFaultStatusNulledFrames.setStatus("current")
_CryptoPerformanceFaultStatusAuthFail_Type = FaultStatusWithNA
_CryptoPerformanceFaultStatusAuthFail_Object = MibTableColumn
cryptoPerformanceFaultStatusAuthFail = _CryptoPerformanceFaultStatusAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 19),
    _CryptoPerformanceFaultStatusAuthFail_Type()
)
cryptoPerformanceFaultStatusAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceFaultStatusAuthFail.setStatus("current")
_CryptoPerformanceFaultStatusIvTrouble_Type = FaultStatusWithNA
_CryptoPerformanceFaultStatusIvTrouble_Object = MibTableColumn
cryptoPerformanceFaultStatusIvTrouble = _CryptoPerformanceFaultStatusIvTrouble_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 20),
    _CryptoPerformanceFaultStatusIvTrouble_Type()
)
cryptoPerformanceFaultStatusIvTrouble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceFaultStatusIvTrouble.setStatus("current")
_CryptoPerformanceFaultStatusReplayErr_Type = FaultStatusWithNA
_CryptoPerformanceFaultStatusReplayErr_Object = MibTableColumn
cryptoPerformanceFaultStatusReplayErr = _CryptoPerformanceFaultStatusReplayErr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 21),
    _CryptoPerformanceFaultStatusReplayErr_Type()
)
cryptoPerformanceFaultStatusReplayErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceFaultStatusReplayErr.setStatus("current")


class _CryptoPerformanceUpId_Type(Unsigned32):
    """Custom type cryptoPerformanceUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CryptoPerformanceUpId_Type.__name__ = "Unsigned32"
_CryptoPerformanceUpId_Object = MibTableColumn
cryptoPerformanceUpId = _CryptoPerformanceUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 2, 6, 1, 1, 22),
    _CryptoPerformanceUpId_Type()
)
cryptoPerformanceUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cryptoPerformanceUpId.setStatus("current")

# Managed Objects groups

cryptoGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1, 1)
)
cryptoGeneralGroupV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoGeneralConfigLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralStateLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoAuthTableSize"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoAuthConfigLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoAuthStateLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoIKEPeerTableSize"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoIKEPeerConfigLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoIKEPeerStateLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoDataplaneEncryptionTableSize"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoPmadminTableSize"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoPmadminConfigLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoPmadminStateLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoPerformanceTableSize"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoPerformanceConfigLastChangeTime"),
        ("LUM-CRYPTO-MIB", "cryptoGeneralCryptoPerformanceStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    cryptoGeneralGroupV1.setStatus("current")

cryptoAuthGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1, 2)
)
cryptoAuthGroupV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoAuthIndex"),
        ("LUM-CRYPTO-MIB", "cryptoAuthUId"),
        ("LUM-CRYPTO-MIB", "cryptoAuthName"),
        ("LUM-CRYPTO-MIB", "cryptoAuthIdentity"),
        ("LUM-CRYPTO-MIB", "cryptoAuthReAuthInterval"),
        ("LUM-CRYPTO-MIB", "cryptoAuthReAuth"),
        ("LUM-CRYPTO-MIB", "cryptoAuthCreateIKEPeer"),
        ("LUM-CRYPTO-MIB", "cryptoAuthenticationGenerateUniqueID"),
        ("LUM-CRYPTO-MIB", "cryptoGeneratedUniqueIdentity"))
)
if mibBuilder.loadTexts:
    cryptoAuthGroupV1.setStatus("current")

cryptoIKEPeerGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1, 3)
)
cryptoIKEPeerGroupV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoIKEPeerIndex"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerUId"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerName"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerIdentity"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerExpectedIKEPeerIdentity"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerAuthScheme"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerPSK"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerAdminStatus"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerOperStatus"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerLastReAuthTime"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerReKeyInterval"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerLastReKeyTime"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerReKey"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerConfigMismatch"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerUnreachable"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerAuthenticationFailure"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerReKeyFailure"))
)
if mibBuilder.loadTexts:
    cryptoIKEPeerGroupV1.setStatus("current")

cryptoDataplaneEncryptionGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1, 4)
)
cryptoDataplaneEncryptionGroupV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionIndex"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionUId"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionName"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionLocalDataplaneId"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionExpectedPeerDataplaneId"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionDiscoveredPeerDataplaneId"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionOTNOHAllocation"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionIKEPeerIdentity"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionReKeyInterval"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionFailurePolicy"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionTrafficKillTimeOffset"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionEncryptionMode"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionLastReKeyTimeTx"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionLastReKeyTimeRx"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionPeerDpIdMismatch"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionConfigMismatch"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionReKeyFailure"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionRXKeyRotationFailure"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionIVExhausted"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionFunctionBlocked"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionUnexpectedRxKeyId"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionReKey"))
)
if mibBuilder.loadTexts:
    cryptoDataplaneEncryptionGroupV1.setStatus("current")

cryptoPmadminGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1, 5)
)
cryptoPmadminGroupV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoPmadminIndex"),
        ("LUM-CRYPTO-MIB", "cryptoPmadminName"),
        ("LUM-CRYPTO-MIB", "cryptoPmadminUId"),
        ("LUM-CRYPTO-MIB", "cryptoPmadminConnAdminIfIndex"),
        ("LUM-CRYPTO-MIB", "cryptoPmadminUpId"))
)
if mibBuilder.loadTexts:
    cryptoPmadminGroupV1.setStatus("current")

cryptoPerformanceGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 1, 6)
)
cryptoPerformanceGroupV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoPerformanceIndex"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceName"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceUId"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceConnAdminIfIndex"),
        ("LUM-CRYPTO-MIB", "cryptoPerformancePeriod"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceType"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterNulledFrames"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterAuthFail"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterIvTrouble"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterReplayErr"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterTotalFrames"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterAuthFrames"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceCounterEncryptedFrames"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceThresholdNulledFrames"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceThresholdAuthFail"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceThresholdIvTrouble"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceThresholdReplayErr"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceFaultStatusNulledFrames"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceFaultStatusAuthFail"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceFaultStatusIvTrouble"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceFaultStatusReplayErr"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceUpId"))
)
if mibBuilder.loadTexts:
    cryptoPerformanceGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumCryptoComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 73, 1, 2, 1)
)
lumCryptoComplV1.setObjects(
      *(("LUM-CRYPTO-MIB", "cryptoGeneralGroupV1"),
        ("LUM-CRYPTO-MIB", "cryptoAuthGroupV1"),
        ("LUM-CRYPTO-MIB", "cryptoIKEPeerGroupV1"),
        ("LUM-CRYPTO-MIB", "cryptoDataplaneEncryptionGroupV1"),
        ("LUM-CRYPTO-MIB", "cryptoPmadminGroupV1"),
        ("LUM-CRYPTO-MIB", "cryptoPerformanceGroupV1"))
)
if mibBuilder.loadTexts:
    lumCryptoComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-CRYPTO-MIB",
    **{"CryptoPeriodWithNA": CryptoPeriodWithNA,
       "CryptoMeasurementTypeWithNA": CryptoMeasurementTypeWithNA,
       "BooleanWithNA": BooleanWithNA,
       "lumCryptoMIBModule": lumCryptoMIBModule,
       "lumCryptoConfs": lumCryptoConfs,
       "lumCryptoGroups": lumCryptoGroups,
       "cryptoGeneralGroupV1": cryptoGeneralGroupV1,
       "cryptoAuthGroupV1": cryptoAuthGroupV1,
       "cryptoIKEPeerGroupV1": cryptoIKEPeerGroupV1,
       "cryptoDataplaneEncryptionGroupV1": cryptoDataplaneEncryptionGroupV1,
       "cryptoPmadminGroupV1": cryptoPmadminGroupV1,
       "cryptoPerformanceGroupV1": cryptoPerformanceGroupV1,
       "lumCryptoCompl": lumCryptoCompl,
       "lumCryptoComplV1": lumCryptoComplV1,
       "lumCryptoMIBObjects": lumCryptoMIBObjects,
       "cryptoGeneral": cryptoGeneral,
       "cryptoGeneralConfigLastChangeTime": cryptoGeneralConfigLastChangeTime,
       "cryptoGeneralStateLastChangeTime": cryptoGeneralStateLastChangeTime,
       "cryptoGeneralCryptoAuthTableSize": cryptoGeneralCryptoAuthTableSize,
       "cryptoGeneralCryptoAuthConfigLastChangeTime": cryptoGeneralCryptoAuthConfigLastChangeTime,
       "cryptoGeneralCryptoAuthStateLastChangeTime": cryptoGeneralCryptoAuthStateLastChangeTime,
       "cryptoGeneralCryptoIKEPeerTableSize": cryptoGeneralCryptoIKEPeerTableSize,
       "cryptoGeneralCryptoIKEPeerConfigLastChangeTime": cryptoGeneralCryptoIKEPeerConfigLastChangeTime,
       "cryptoGeneralCryptoIKEPeerStateLastChangeTime": cryptoGeneralCryptoIKEPeerStateLastChangeTime,
       "cryptoGeneralCryptoDataplaneEncryptionTableSize": cryptoGeneralCryptoDataplaneEncryptionTableSize,
       "cryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime": cryptoGeneralCryptoDataplaneEncryptionConfigLastChangeTime,
       "cryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime": cryptoGeneralCryptoDataplaneEncryptionStateLastChangeTime,
       "cryptoGeneralCryptoPmadminTableSize": cryptoGeneralCryptoPmadminTableSize,
       "cryptoGeneralCryptoPmadminConfigLastChangeTime": cryptoGeneralCryptoPmadminConfigLastChangeTime,
       "cryptoGeneralCryptoPmadminStateLastChangeTime": cryptoGeneralCryptoPmadminStateLastChangeTime,
       "cryptoGeneralCryptoPerformanceTableSize": cryptoGeneralCryptoPerformanceTableSize,
       "cryptoGeneralCryptoPerformanceConfigLastChangeTime": cryptoGeneralCryptoPerformanceConfigLastChangeTime,
       "cryptoGeneralCryptoPerformanceStateLastChangeTime": cryptoGeneralCryptoPerformanceStateLastChangeTime,
       "cryptoAuthList": cryptoAuthList,
       "cryptoAuthTable": cryptoAuthTable,
       "cryptoAuthEntry": cryptoAuthEntry,
       "cryptoAuthIndex": cryptoAuthIndex,
       "cryptoAuthUId": cryptoAuthUId,
       "cryptoAuthName": cryptoAuthName,
       "cryptoAuthIdentity": cryptoAuthIdentity,
       "cryptoAuthReAuthInterval": cryptoAuthReAuthInterval,
       "cryptoAuthReAuth": cryptoAuthReAuth,
       "cryptoAuthCreateIKEPeer": cryptoAuthCreateIKEPeer,
       "cryptoAuthenticationGenerateUniqueID": cryptoAuthenticationGenerateUniqueID,
       "cryptoGeneratedUniqueIdentity": cryptoGeneratedUniqueIdentity,
       "cryptoIKEPeerList": cryptoIKEPeerList,
       "cryptoIKEPeerTable": cryptoIKEPeerTable,
       "cryptoIKEPeerEntry": cryptoIKEPeerEntry,
       "cryptoIKEPeerIndex": cryptoIKEPeerIndex,
       "cryptoIKEPeerUId": cryptoIKEPeerUId,
       "cryptoIKEPeerName": cryptoIKEPeerName,
       "cryptoIKEPeerIdentity": cryptoIKEPeerIdentity,
       "cryptoIKEPeerExpectedIKEPeerIdentity": cryptoIKEPeerExpectedIKEPeerIdentity,
       "cryptoIKEPeerAuthScheme": cryptoIKEPeerAuthScheme,
       "cryptoIKEPeerPSK": cryptoIKEPeerPSK,
       "cryptoIKEPeerAdminStatus": cryptoIKEPeerAdminStatus,
       "cryptoIKEPeerOperStatus": cryptoIKEPeerOperStatus,
       "cryptoIKEPeerLastReAuthTime": cryptoIKEPeerLastReAuthTime,
       "cryptoIKEPeerReKeyInterval": cryptoIKEPeerReKeyInterval,
       "cryptoIKEPeerLastReKeyTime": cryptoIKEPeerLastReKeyTime,
       "cryptoIKEPeerReKey": cryptoIKEPeerReKey,
       "cryptoIKEPeerConfigMismatch": cryptoIKEPeerConfigMismatch,
       "cryptoIKEPeerUnreachable": cryptoIKEPeerUnreachable,
       "cryptoIKEPeerAuthenticationFailure": cryptoIKEPeerAuthenticationFailure,
       "cryptoIKEPeerReKeyFailure": cryptoIKEPeerReKeyFailure,
       "cryptoDataplaneEncryptionList": cryptoDataplaneEncryptionList,
       "cryptoDataplaneEncryptionTable": cryptoDataplaneEncryptionTable,
       "cryptoDataplaneEncryptionEntry": cryptoDataplaneEncryptionEntry,
       "cryptoDataplaneEncryptionIndex": cryptoDataplaneEncryptionIndex,
       "cryptoDataplaneEncryptionUId": cryptoDataplaneEncryptionUId,
       "cryptoDataplaneEncryptionName": cryptoDataplaneEncryptionName,
       "cryptoDataplaneEncryptionLocalDataplaneId": cryptoDataplaneEncryptionLocalDataplaneId,
       "cryptoDataplaneEncryptionExpectedPeerDataplaneId": cryptoDataplaneEncryptionExpectedPeerDataplaneId,
       "cryptoDataplaneEncryptionDiscoveredPeerDataplaneId": cryptoDataplaneEncryptionDiscoveredPeerDataplaneId,
       "cryptoDataplaneEncryptionOTNOHAllocation": cryptoDataplaneEncryptionOTNOHAllocation,
       "cryptoDataplaneEncryptionIKEPeerIdentity": cryptoDataplaneEncryptionIKEPeerIdentity,
       "cryptoDataplaneEncryptionReKeyInterval": cryptoDataplaneEncryptionReKeyInterval,
       "cryptoDataplaneEncryptionFailurePolicy": cryptoDataplaneEncryptionFailurePolicy,
       "cryptoDataplaneEncryptionTrafficKillTimeOffset": cryptoDataplaneEncryptionTrafficKillTimeOffset,
       "cryptoDataplaneEncryptionEncryptionMode": cryptoDataplaneEncryptionEncryptionMode,
       "cryptoDataplaneEncryptionLastReKeyTimeTx": cryptoDataplaneEncryptionLastReKeyTimeTx,
       "cryptoDataplaneEncryptionLastReKeyTimeRx": cryptoDataplaneEncryptionLastReKeyTimeRx,
       "cryptoDataplaneEncryptionPeerDpIdMismatch": cryptoDataplaneEncryptionPeerDpIdMismatch,
       "cryptoDataplaneEncryptionConfigMismatch": cryptoDataplaneEncryptionConfigMismatch,
       "cryptoDataplaneEncryptionReKeyFailure": cryptoDataplaneEncryptionReKeyFailure,
       "cryptoDataplaneEncryptionRXKeyRotationFailure": cryptoDataplaneEncryptionRXKeyRotationFailure,
       "cryptoDataplaneEncryptionIVExhausted": cryptoDataplaneEncryptionIVExhausted,
       "cryptoDataplaneEncryptionFunctionBlocked": cryptoDataplaneEncryptionFunctionBlocked,
       "cryptoDataplaneEncryptionUnexpectedRxKeyId": cryptoDataplaneEncryptionUnexpectedRxKeyId,
       "cryptoDataplaneEncryptionReKey": cryptoDataplaneEncryptionReKey,
       "cryptoPmadminList": cryptoPmadminList,
       "cryptoPmadminTable": cryptoPmadminTable,
       "cryptoPmadminEntry": cryptoPmadminEntry,
       "cryptoPmadminIndex": cryptoPmadminIndex,
       "cryptoPmadminName": cryptoPmadminName,
       "cryptoPmadminUId": cryptoPmadminUId,
       "cryptoPmadminConnAdminIfIndex": cryptoPmadminConnAdminIfIndex,
       "cryptoPmadminUpId": cryptoPmadminUpId,
       "cryptoPerformanceList": cryptoPerformanceList,
       "cryptoPerformanceTable": cryptoPerformanceTable,
       "cryptoPerformanceEntry": cryptoPerformanceEntry,
       "cryptoPerformanceIndex": cryptoPerformanceIndex,
       "cryptoPerformanceName": cryptoPerformanceName,
       "cryptoPerformanceUId": cryptoPerformanceUId,
       "cryptoPerformanceConnAdminIfIndex": cryptoPerformanceConnAdminIfIndex,
       "cryptoPerformancePeriod": cryptoPerformancePeriod,
       "cryptoPerformanceType": cryptoPerformanceType,
       "cryptoPerformanceCounterNulledFrames": cryptoPerformanceCounterNulledFrames,
       "cryptoPerformanceCounterAuthFail": cryptoPerformanceCounterAuthFail,
       "cryptoPerformanceCounterIvTrouble": cryptoPerformanceCounterIvTrouble,
       "cryptoPerformanceCounterReplayErr": cryptoPerformanceCounterReplayErr,
       "cryptoPerformanceCounterTotalFrames": cryptoPerformanceCounterTotalFrames,
       "cryptoPerformanceCounterAuthFrames": cryptoPerformanceCounterAuthFrames,
       "cryptoPerformanceCounterEncryptedFrames": cryptoPerformanceCounterEncryptedFrames,
       "cryptoPerformanceThresholdNulledFrames": cryptoPerformanceThresholdNulledFrames,
       "cryptoPerformanceThresholdAuthFail": cryptoPerformanceThresholdAuthFail,
       "cryptoPerformanceThresholdIvTrouble": cryptoPerformanceThresholdIvTrouble,
       "cryptoPerformanceThresholdReplayErr": cryptoPerformanceThresholdReplayErr,
       "cryptoPerformanceFaultStatusNulledFrames": cryptoPerformanceFaultStatusNulledFrames,
       "cryptoPerformanceFaultStatusAuthFail": cryptoPerformanceFaultStatusAuthFail,
       "cryptoPerformanceFaultStatusIvTrouble": cryptoPerformanceFaultStatusIvTrouble,
       "cryptoPerformanceFaultStatusReplayErr": cryptoPerformanceFaultStatusReplayErr,
       "cryptoPerformanceUpId": cryptoPerformanceUpId}
)
