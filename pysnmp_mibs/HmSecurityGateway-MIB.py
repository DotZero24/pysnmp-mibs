# SNMP MIB module (HmSecurityGateway-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HmSecurityGateway-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:23 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_HmSecurityGateway_ObjectIdentity = ObjectIdentity
hmSecurityGateway = _HmSecurityGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51)
)
_HmSecVPN_ObjectIdentity = ObjectIdentity
hmSecVPN = _HmSecVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1)
)
_HmSecVPNMachine_ObjectIdentity = ObjectIdentity
hmSecVPNMachine = _HmSecVPNMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 1)
)
_HmSecVPNMachineCert_Type = DisplayString
_HmSecVPNMachineCert_Object = MibScalar
hmSecVPNMachineCert = _HmSecVPNMachineCert_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 1, 1),
    _HmSecVPNMachineCert_Type()
)
hmSecVPNMachineCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNMachineCert.setStatus("mandatory")
_HmSecVPNMachinePrivate_Type = DisplayString
_HmSecVPNMachinePrivate_Object = MibScalar
hmSecVPNMachinePrivate = _HmSecVPNMachinePrivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 1, 2),
    _HmSecVPNMachinePrivate_Type()
)
hmSecVPNMachinePrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNMachinePrivate.setStatus("mandatory")
_HmSecVPNConnectionTable_Object = MibTable
hmSecVPNConnectionTable = _HmSecVPNConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2)
)
if mibBuilder.loadTexts:
    hmSecVPNConnectionTable.setStatus("mandatory")
_HmSecVPNConnectionEntry_Object = MibTableRow
hmSecVPNConnectionEntry = _HmSecVPNConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1)
)
hmSecVPNConnectionEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecVPNconIndex"),
)
if mibBuilder.loadTexts:
    hmSecVPNConnectionEntry.setStatus("mandatory")


class _HmSecVPNconIndex_Type(Integer32):
    """Custom type hmSecVPNconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecVPNconIndex_Type.__name__ = "Integer32"
_HmSecVPNconIndex_Object = MibTableColumn
hmSecVPNconIndex = _HmSecVPNconIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 1),
    _HmSecVPNconIndex_Type()
)
hmSecVPNconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecVPNconIndex.setStatus("mandatory")
_HmSecVPNconName_Type = DisplayString
_HmSecVPNconName_Object = MibTableColumn
hmSecVPNconName = _HmSecVPNconName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 2),
    _HmSecVPNconName_Type()
)
hmSecVPNconName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNconName.setStatus("mandatory")


class _HmSecVPNconEnabled_Type(Integer32):
    """Custom type hmSecVPNconEnabled based on Integer32"""
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


_HmSecVPNconEnabled_Type.__name__ = "Integer32"
_HmSecVPNconEnabled_Object = MibTableColumn
hmSecVPNconEnabled = _HmSecVPNconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 3),
    _HmSecVPNconEnabled_Type()
)
hmSecVPNconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNconEnabled.setStatus("mandatory")
_HmSecVPNremGW_Type = DisplayString
_HmSecVPNremGW_Object = MibTableColumn
hmSecVPNremGW = _HmSecVPNremGW_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 4),
    _HmSecVPNremGW_Type()
)
hmSecVPNremGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNremGW.setStatus("mandatory")


class _HmSecVPNconType_Type(Integer32):
    """Custom type hmSecVPNconType based on Integer32"""
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
        *(("transport", 1),
          ("tunnel", 2),
          ("l2tp-w2k", 3),
          ("l2tp-ssh", 4))
    )


_HmSecVPNconType_Type.__name__ = "Integer32"
_HmSecVPNconType_Object = MibTableColumn
hmSecVPNconType = _HmSecVPNconType_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 5),
    _HmSecVPNconType_Type()
)
hmSecVPNconType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNconType.setStatus("mandatory")
_HmSecVPNlocalNet_Type = IpAddress
_HmSecVPNlocalNet_Object = MibTableColumn
hmSecVPNlocalNet = _HmSecVPNlocalNet_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 6),
    _HmSecVPNlocalNet_Type()
)
hmSecVPNlocalNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNlocalNet.setStatus("deprecated")
_HmSecVPNlocalMask_Type = IpAddress
_HmSecVPNlocalMask_Object = MibTableColumn
hmSecVPNlocalMask = _HmSecVPNlocalMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 7),
    _HmSecVPNlocalMask_Type()
)
hmSecVPNlocalMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNlocalMask.setStatus("deprecated")
_HmSecVPNremoteNet_Type = IpAddress
_HmSecVPNremoteNet_Object = MibTableColumn
hmSecVPNremoteNet = _HmSecVPNremoteNet_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 8),
    _HmSecVPNremoteNet_Type()
)
hmSecVPNremoteNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNremoteNet.setStatus("deprecated")
_HmSecVPNremoteMask_Type = IpAddress
_HmSecVPNremoteMask_Object = MibTableColumn
hmSecVPNremoteMask = _HmSecVPNremoteMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 9),
    _HmSecVPNremoteMask_Type()
)
hmSecVPNremoteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNremoteMask.setStatus("deprecated")


class _HmSecVPNauthType_Type(Integer32):
    """Custom type hmSecVPNauthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("x509", 2))
    )


_HmSecVPNauthType_Type.__name__ = "Integer32"
_HmSecVPNauthType_Object = MibTableColumn
hmSecVPNauthType = _HmSecVPNauthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 10),
    _HmSecVPNauthType_Type()
)
hmSecVPNauthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNauthType.setStatus("mandatory")
_HmSecVPNpsk_Type = DisplayString
_HmSecVPNpsk_Object = MibTableColumn
hmSecVPNpsk = _HmSecVPNpsk_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 11),
    _HmSecVPNpsk_Type()
)
hmSecVPNpsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNpsk.setStatus("mandatory")
_HmSecVPNx509_Type = DisplayString
_HmSecVPNx509_Object = MibTableColumn
hmSecVPNx509 = _HmSecVPNx509_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 12),
    _HmSecVPNx509_Type()
)
hmSecVPNx509.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNx509.setStatus("mandatory")


class _HmSecVPNikeDH_Type(Integer32):
    """Custom type hmSecVPNikeDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("modp1024", 2),
          ("modp1536", 3),
          ("modp2048", 4),
          ("modp3072", 5),
          ("modp4096", 6))
    )


_HmSecVPNikeDH_Type.__name__ = "Integer32"
_HmSecVPNikeDH_Object = MibTableColumn
hmSecVPNikeDH = _HmSecVPNikeDH_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 13),
    _HmSecVPNikeDH_Type()
)
hmSecVPNikeDH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNikeDH.setStatus("mandatory")


class _HmSecVPNikeHash_Type(Integer32):
    """Custom type hmSecVPNikeHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("md5", 2),
          ("sha1", 3))
    )


_HmSecVPNikeHash_Type.__name__ = "Integer32"
_HmSecVPNikeHash_Object = MibTableColumn
hmSecVPNikeHash = _HmSecVPNikeHash_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 14),
    _HmSecVPNikeHash_Type()
)
hmSecVPNikeHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNikeHash.setStatus("mandatory")


class _HmSecVPNipsecHash_Type(Integer32):
    """Custom type hmSecVPNipsecHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("md5", 2),
          ("sha1", 3))
    )


_HmSecVPNipsecHash_Type.__name__ = "Integer32"
_HmSecVPNipsecHash_Object = MibTableColumn
hmSecVPNipsecHash = _HmSecVPNipsecHash_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 15),
    _HmSecVPNipsecHash_Type()
)
hmSecVPNipsecHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNipsecHash.setStatus("mandatory")


class _HmSecVPNikeAlg_Type(Integer32):
    """Custom type hmSecVPNikeAlg based on Integer32"""
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
        *(("des", 1),
          ("tripledes168", 2),
          ("aes128", 3),
          ("aes192", 4),
          ("aes256", 5))
    )


_HmSecVPNikeAlg_Type.__name__ = "Integer32"
_HmSecVPNikeAlg_Object = MibTableColumn
hmSecVPNikeAlg = _HmSecVPNikeAlg_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 16),
    _HmSecVPNikeAlg_Type()
)
hmSecVPNikeAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNikeAlg.setStatus("mandatory")


class _HmSecVPNipsecAlg_Type(Integer32):
    """Custom type hmSecVPNipsecAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("tripledes168", 2),
          ("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("null", 6))
    )


_HmSecVPNipsecAlg_Type.__name__ = "Integer32"
_HmSecVPNipsecAlg_Object = MibTableColumn
hmSecVPNipsecAlg = _HmSecVPNipsecAlg_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 17),
    _HmSecVPNipsecAlg_Type()
)
hmSecVPNipsecAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNipsecAlg.setStatus("mandatory")


class _HmSecVPNpfs_Type(Integer32):
    """Custom type hmSecVPNpfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("all", 2),
          ("modp1024", 3),
          ("modp1536", 4),
          ("modp2048", 5),
          ("modp3072", 6),
          ("modp4096", 7))
    )


_HmSecVPNpfs_Type.__name__ = "Integer32"
_HmSecVPNpfs_Object = MibTableColumn
hmSecVPNpfs = _HmSecVPNpfs_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 18),
    _HmSecVPNpfs_Type()
)
hmSecVPNpfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNpfs.setStatus("mandatory")


class _HmSecVPNconStartUp_Type(Integer32):
    """Custom type hmSecVPNconStartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("waitForRemote", 2))
    )


_HmSecVPNconStartUp_Type.__name__ = "Integer32"
_HmSecVPNconStartUp_Object = MibTableColumn
hmSecVPNconStartUp = _HmSecVPNconStartUp_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 19),
    _HmSecVPNconStartUp_Type()
)
hmSecVPNconStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNconStartUp.setStatus("mandatory")


class _HmSecVPNvirtIPMethod_Type(Integer32):
    """Custom type hmSecVPNvirtIPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp-over-ipsec", 2))
    )


_HmSecVPNvirtIPMethod_Type.__name__ = "Integer32"
_HmSecVPNvirtIPMethod_Object = MibTableColumn
hmSecVPNvirtIPMethod = _HmSecVPNvirtIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 20),
    _HmSecVPNvirtIPMethod_Type()
)
hmSecVPNvirtIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNvirtIPMethod.setStatus("mandatory")
_HmSecVPNvirtIP_Type = IpAddress
_HmSecVPNvirtIP_Object = MibTableColumn
hmSecVPNvirtIP = _HmSecVPNvirtIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 21),
    _HmSecVPNvirtIP_Type()
)
hmSecVPNvirtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNvirtIP.setStatus("mandatory")


class _HmSecVPNFWLogDefIn_Type(Integer32):
    """Custom type hmSecVPNFWLogDefIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNFWLogDefIn_Type.__name__ = "Integer32"
_HmSecVPNFWLogDefIn_Object = MibTableColumn
hmSecVPNFWLogDefIn = _HmSecVPNFWLogDefIn_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 22),
    _HmSecVPNFWLogDefIn_Type()
)
hmSecVPNFWLogDefIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWLogDefIn.setStatus("mandatory")


class _HmSecVPNFWLogDefOut_Type(Integer32):
    """Custom type hmSecVPNFWLogDefOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNFWLogDefOut_Type.__name__ = "Integer32"
_HmSecVPNFWLogDefOut_Object = MibTableColumn
hmSecVPNFWLogDefOut = _HmSecVPNFWLogDefOut_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 23),
    _HmSecVPNFWLogDefOut_Type()
)
hmSecVPNFWLogDefOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWLogDefOut.setStatus("mandatory")


class _HmSecVPNProtoAH_Type(Integer32):
    """Custom type hmSecVPNProtoAH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNProtoAH_Type.__name__ = "Integer32"
_HmSecVPNProtoAH_Object = MibTableColumn
hmSecVPNProtoAH = _HmSecVPNProtoAH_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 26),
    _HmSecVPNProtoAH_Type()
)
hmSecVPNProtoAH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNProtoAH.setStatus("mandatory")


class _HmSecVPNProtoESP_Type(Integer32):
    """Custom type hmSecVPNProtoESP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNProtoESP_Type.__name__ = "Integer32"
_HmSecVPNProtoESP_Object = MibTableColumn
hmSecVPNProtoESP = _HmSecVPNProtoESP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 27),
    _HmSecVPNProtoESP_Type()
)
hmSecVPNProtoESP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNProtoESP.setStatus("mandatory")


class _HmSecVPNComp_Type(Integer32):
    """Custom type hmSecVPNComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNComp_Type.__name__ = "Integer32"
_HmSecVPNComp_Object = MibTableColumn
hmSecVPNComp = _HmSecVPNComp_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 28),
    _HmSecVPNComp_Type()
)
hmSecVPNComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNComp.setStatus("mandatory")


class _HmSecVPNLocalIDMode_Type(Integer32):
    """Custom type hmSecVPNLocalIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("freeswan", 2))
    )


_HmSecVPNLocalIDMode_Type.__name__ = "Integer32"
_HmSecVPNLocalIDMode_Object = MibTableColumn
hmSecVPNLocalIDMode = _HmSecVPNLocalIDMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 29),
    _HmSecVPNLocalIDMode_Type()
)
hmSecVPNLocalIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNLocalIDMode.setStatus("mandatory")
_HmSecVPNLocalID_Type = DisplayString
_HmSecVPNLocalID_Object = MibTableColumn
hmSecVPNLocalID = _HmSecVPNLocalID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 30),
    _HmSecVPNLocalID_Type()
)
hmSecVPNLocalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNLocalID.setStatus("mandatory")


class _HmSecVPNRemoteIDMode_Type(Integer32):
    """Custom type hmSecVPNRemoteIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("freeswan", 2))
    )


_HmSecVPNRemoteIDMode_Type.__name__ = "Integer32"
_HmSecVPNRemoteIDMode_Object = MibTableColumn
hmSecVPNRemoteIDMode = _HmSecVPNRemoteIDMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 31),
    _HmSecVPNRemoteIDMode_Type()
)
hmSecVPNRemoteIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRemoteIDMode.setStatus("mandatory")
_HmSecVPNRemoteID_Type = DisplayString
_HmSecVPNRemoteID_Object = MibTableColumn
hmSecVPNRemoteID = _HmSecVPNRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 32),
    _HmSecVPNRemoteID_Type()
)
hmSecVPNRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRemoteID.setStatus("mandatory")
_HmSecVPNIkeLifetime_Type = Integer32
_HmSecVPNIkeLifetime_Object = MibTableColumn
hmSecVPNIkeLifetime = _HmSecVPNIkeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 33),
    _HmSecVPNIkeLifetime_Type()
)
hmSecVPNIkeLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNIkeLifetime.setStatus("mandatory")
_HmSecVPNIpsecLifetime_Type = Integer32
_HmSecVPNIpsecLifetime_Object = MibTableColumn
hmSecVPNIpsecLifetime = _HmSecVPNIpsecLifetime_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 34),
    _HmSecVPNIpsecLifetime_Type()
)
hmSecVPNIpsecLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNIpsecLifetime.setStatus("mandatory")
_HmSecVPNRekeyMargin_Type = Integer32
_HmSecVPNRekeyMargin_Object = MibTableColumn
hmSecVPNRekeyMargin = _HmSecVPNRekeyMargin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 35),
    _HmSecVPNRekeyMargin_Type()
)
hmSecVPNRekeyMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRekeyMargin.setStatus("mandatory")
_HmSecVPNRekeyFuzz_Type = Integer32
_HmSecVPNRekeyFuzz_Object = MibTableColumn
hmSecVPNRekeyFuzz = _HmSecVPNRekeyFuzz_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 36),
    _HmSecVPNRekeyFuzz_Type()
)
hmSecVPNRekeyFuzz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRekeyFuzz.setStatus("mandatory")
_HmSecVPNKeyingTries_Type = Integer32
_HmSecVPNKeyingTries_Object = MibTableColumn
hmSecVPNKeyingTries = _HmSecVPNKeyingTries_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 37),
    _HmSecVPNKeyingTries_Type()
)
hmSecVPNKeyingTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNKeyingTries.setStatus("mandatory")


class _HmSecVPNRekey_Type(Integer32):
    """Custom type hmSecVPNRekey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNRekey_Type.__name__ = "Integer32"
_HmSecVPNRekey_Object = MibTableColumn
hmSecVPNRekey = _HmSecVPNRekey_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 38),
    _HmSecVPNRekey_Type()
)
hmSecVPNRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRekey.setStatus("mandatory")


class _HmSecVPNDPDAction_Type(Integer32):
    """Custom type hmSecVPNDPDAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hold", 1),
          ("clear", 2))
    )


_HmSecVPNDPDAction_Type.__name__ = "Integer32"
_HmSecVPNDPDAction_Object = MibTableColumn
hmSecVPNDPDAction = _HmSecVPNDPDAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 39),
    _HmSecVPNDPDAction_Type()
)
hmSecVPNDPDAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDPDAction.setStatus("mandatory")
_HmSecVPNDPDDelay_Type = Integer32
_HmSecVPNDPDDelay_Object = MibTableColumn
hmSecVPNDPDDelay = _HmSecVPNDPDDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 40),
    _HmSecVPNDPDDelay_Type()
)
hmSecVPNDPDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDPDDelay.setStatus("mandatory")
_HmSecVPNDPDTimeout_Type = Integer32
_HmSecVPNDPDTimeout_Object = MibTableColumn
hmSecVPNDPDTimeout = _HmSecVPNDPDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 41),
    _HmSecVPNDPDTimeout_Type()
)
hmSecVPNDPDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDPDTimeout.setStatus("mandatory")
_HmSecVPNRowStatus_Type = RowStatus
_HmSecVPNRowStatus_Object = MibTableColumn
hmSecVPNRowStatus = _HmSecVPNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 42),
    _HmSecVPNRowStatus_Type()
)
hmSecVPNRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRowStatus.setStatus("mandatory")


class _HmSecVPNAggressive_Type(Integer32):
    """Custom type hmSecVPNAggressive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_HmSecVPNAggressive_Type.__name__ = "Integer32"
_HmSecVPNAggressive_Object = MibTableColumn
hmSecVPNAggressive = _HmSecVPNAggressive_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 43),
    _HmSecVPNAggressive_Type()
)
hmSecVPNAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNAggressive.setStatus("mandatory")
_HmSecVPNlocal_Type = DisplayString
_HmSecVPNlocal_Object = MibTableColumn
hmSecVPNlocal = _HmSecVPNlocal_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 44),
    _HmSecVPNlocal_Type()
)
hmSecVPNlocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNlocal.setStatus("mandatory")
_HmSecVPNremote_Type = DisplayString
_HmSecVPNremote_Object = MibTableColumn
hmSecVPNremote = _HmSecVPNremote_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 2, 1, 45),
    _HmSecVPNremote_Type()
)
hmSecVPNremote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNremote.setStatus("mandatory")
_HmSecVPNFW_ObjectIdentity = ObjectIdentity
hmSecVPNFW = _HmSecVPNFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3)
)
_HmSecVPNFWINTable_Object = MibTable
hmSecVPNFWINTable = _HmSecVPNFWINTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hmSecVPNFWINTable.setStatus("mandatory")
_HmSecVPNFWINEntry_Object = MibTableRow
hmSecVPNFWINEntry = _HmSecVPNFWINEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1)
)
hmSecVPNFWINEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecVPNFWINconIndex"),
    (0, "HmSecurityGateway-MIB", "hmSecVPNFWINruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecVPNFWINEntry.setStatus("mandatory")


class _HmSecVPNFWINconIndex_Type(Integer32):
    """Custom type hmSecVPNFWINconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecVPNFWINconIndex_Type.__name__ = "Integer32"
_HmSecVPNFWINconIndex_Object = MibTableColumn
hmSecVPNFWINconIndex = _HmSecVPNFWINconIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 1),
    _HmSecVPNFWINconIndex_Type()
)
hmSecVPNFWINconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecVPNFWINconIndex.setStatus("mandatory")


class _HmSecVPNFWINruleIndex_Type(Integer32):
    """Custom type hmSecVPNFWINruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecVPNFWINruleIndex_Type.__name__ = "Integer32"
_HmSecVPNFWINruleIndex_Object = MibTableColumn
hmSecVPNFWINruleIndex = _HmSecVPNFWINruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 2),
    _HmSecVPNFWINruleIndex_Type()
)
hmSecVPNFWINruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecVPNFWINruleIndex.setStatus("mandatory")
_HmSecVPNFWINsourceIP_Type = DisplayString
_HmSecVPNFWINsourceIP_Object = MibTableColumn
hmSecVPNFWINsourceIP = _HmSecVPNFWINsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 3),
    _HmSecVPNFWINsourceIP_Type()
)
hmSecVPNFWINsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINsourceIP.setStatus("mandatory")
_HmSecVPNFWINdestinationIP_Type = DisplayString
_HmSecVPNFWINdestinationIP_Object = MibTableColumn
hmSecVPNFWINdestinationIP = _HmSecVPNFWINdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 4),
    _HmSecVPNFWINdestinationIP_Type()
)
hmSecVPNFWINdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINdestinationIP.setStatus("mandatory")
_HmSecVPNFWINsport_Type = DisplayString
_HmSecVPNFWINsport_Object = MibTableColumn
hmSecVPNFWINsport = _HmSecVPNFWINsport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 5),
    _HmSecVPNFWINsport_Type()
)
hmSecVPNFWINsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINsport.setStatus("mandatory")
_HmSecVPNFWINdport_Type = DisplayString
_HmSecVPNFWINdport_Object = MibTableColumn
hmSecVPNFWINdport = _HmSecVPNFWINdport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 6),
    _HmSecVPNFWINdport_Type()
)
hmSecVPNFWINdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINdport.setStatus("mandatory")


class _HmSecVPNFWINtarget_Type(Integer32):
    """Custom type hmSecVPNFWINtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecVPNFWINtarget_Type.__name__ = "Integer32"
_HmSecVPNFWINtarget_Object = MibTableColumn
hmSecVPNFWINtarget = _HmSecVPNFWINtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 7),
    _HmSecVPNFWINtarget_Type()
)
hmSecVPNFWINtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINtarget.setStatus("mandatory")


class _HmSecVPNFWINproto_Type(Integer32):
    """Custom type hmSecVPNFWINproto based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("all", 4))
    )


_HmSecVPNFWINproto_Type.__name__ = "Integer32"
_HmSecVPNFWINproto_Object = MibTableColumn
hmSecVPNFWINproto = _HmSecVPNFWINproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 8),
    _HmSecVPNFWINproto_Type()
)
hmSecVPNFWINproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINproto.setStatus("mandatory")


class _HmSecVPNFWINlog_Type(Integer32):
    """Custom type hmSecVPNFWINlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNFWINlog_Type.__name__ = "Integer32"
_HmSecVPNFWINlog_Object = MibTableColumn
hmSecVPNFWINlog = _HmSecVPNFWINlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 9),
    _HmSecVPNFWINlog_Type()
)
hmSecVPNFWINlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINlog.setStatus("mandatory")
_HmSecVPNFWINRowStatus_Type = RowStatus
_HmSecVPNFWINRowStatus_Object = MibTableColumn
hmSecVPNFWINRowStatus = _HmSecVPNFWINRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 10),
    _HmSecVPNFWINRowStatus_Type()
)
hmSecVPNFWINRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINRowStatus.setStatus("mandatory")
_HmSecVPNFWINcomment_Type = DisplayString
_HmSecVPNFWINcomment_Object = MibTableColumn
hmSecVPNFWINcomment = _HmSecVPNFWINcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 1, 1, 11),
    _HmSecVPNFWINcomment_Type()
)
hmSecVPNFWINcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWINcomment.setStatus("mandatory")
_HmSecVPNFWOUTTable_Object = MibTable
hmSecVPNFWOUTTable = _HmSecVPNFWOUTTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hmSecVPNFWOUTTable.setStatus("mandatory")
_HmSecVPNFWOUTEntry_Object = MibTableRow
hmSecVPNFWOUTEntry = _HmSecVPNFWOUTEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1)
)
hmSecVPNFWOUTEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecVPNFWOUTconIndex"),
    (0, "HmSecurityGateway-MIB", "hmSecVPNFWOUTruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecVPNFWOUTEntry.setStatus("mandatory")


class _HmSecVPNFWOUTconIndex_Type(Integer32):
    """Custom type hmSecVPNFWOUTconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecVPNFWOUTconIndex_Type.__name__ = "Integer32"
_HmSecVPNFWOUTconIndex_Object = MibTableColumn
hmSecVPNFWOUTconIndex = _HmSecVPNFWOUTconIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 1),
    _HmSecVPNFWOUTconIndex_Type()
)
hmSecVPNFWOUTconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTconIndex.setStatus("mandatory")


class _HmSecVPNFWOUTruleIndex_Type(Integer32):
    """Custom type hmSecVPNFWOUTruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecVPNFWOUTruleIndex_Type.__name__ = "Integer32"
_HmSecVPNFWOUTruleIndex_Object = MibTableColumn
hmSecVPNFWOUTruleIndex = _HmSecVPNFWOUTruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 2),
    _HmSecVPNFWOUTruleIndex_Type()
)
hmSecVPNFWOUTruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTruleIndex.setStatus("mandatory")
_HmSecVPNFWOUTsourceIP_Type = DisplayString
_HmSecVPNFWOUTsourceIP_Object = MibTableColumn
hmSecVPNFWOUTsourceIP = _HmSecVPNFWOUTsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 3),
    _HmSecVPNFWOUTsourceIP_Type()
)
hmSecVPNFWOUTsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTsourceIP.setStatus("mandatory")
_HmSecVPNFWOUTdestinationIP_Type = DisplayString
_HmSecVPNFWOUTdestinationIP_Object = MibTableColumn
hmSecVPNFWOUTdestinationIP = _HmSecVPNFWOUTdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 4),
    _HmSecVPNFWOUTdestinationIP_Type()
)
hmSecVPNFWOUTdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTdestinationIP.setStatus("mandatory")
_HmSecVPNFWOUTsport_Type = DisplayString
_HmSecVPNFWOUTsport_Object = MibTableColumn
hmSecVPNFWOUTsport = _HmSecVPNFWOUTsport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 5),
    _HmSecVPNFWOUTsport_Type()
)
hmSecVPNFWOUTsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTsport.setStatus("mandatory")
_HmSecVPNFWOUTdport_Type = DisplayString
_HmSecVPNFWOUTdport_Object = MibTableColumn
hmSecVPNFWOUTdport = _HmSecVPNFWOUTdport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 6),
    _HmSecVPNFWOUTdport_Type()
)
hmSecVPNFWOUTdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTdport.setStatus("mandatory")


class _HmSecVPNFWOUTtarget_Type(Integer32):
    """Custom type hmSecVPNFWOUTtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecVPNFWOUTtarget_Type.__name__ = "Integer32"
_HmSecVPNFWOUTtarget_Object = MibTableColumn
hmSecVPNFWOUTtarget = _HmSecVPNFWOUTtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 7),
    _HmSecVPNFWOUTtarget_Type()
)
hmSecVPNFWOUTtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTtarget.setStatus("mandatory")


class _HmSecVPNFWOUTproto_Type(Integer32):
    """Custom type hmSecVPNFWOUTproto based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("all", 4))
    )


_HmSecVPNFWOUTproto_Type.__name__ = "Integer32"
_HmSecVPNFWOUTproto_Object = MibTableColumn
hmSecVPNFWOUTproto = _HmSecVPNFWOUTproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 8),
    _HmSecVPNFWOUTproto_Type()
)
hmSecVPNFWOUTproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTproto.setStatus("mandatory")


class _HmSecVPNFWOUTlog_Type(Integer32):
    """Custom type hmSecVPNFWOUTlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNFWOUTlog_Type.__name__ = "Integer32"
_HmSecVPNFWOUTlog_Object = MibTableColumn
hmSecVPNFWOUTlog = _HmSecVPNFWOUTlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 9),
    _HmSecVPNFWOUTlog_Type()
)
hmSecVPNFWOUTlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTlog.setStatus("mandatory")
_HmSecVPNFWOUTRowStatus_Type = RowStatus
_HmSecVPNFWOUTRowStatus_Object = MibTableColumn
hmSecVPNFWOUTRowStatus = _HmSecVPNFWOUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 10),
    _HmSecVPNFWOUTRowStatus_Type()
)
hmSecVPNFWOUTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTRowStatus.setStatus("mandatory")
_HmSecVPNFWOUTcomment_Type = DisplayString
_HmSecVPNFWOUTcomment_Object = MibTableColumn
hmSecVPNFWOUTcomment = _HmSecVPNFWOUTcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 3, 2, 1, 11),
    _HmSecVPNFWOUTcomment_Type()
)
hmSecVPNFWOUTcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNFWOUTcomment.setStatus("mandatory")
_HmSecVPNDynDNS_ObjectIdentity = ObjectIdentity
hmSecVPNDynDNS = _HmSecVPNDynDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4)
)
_HmSecVPNDynDNSRegister_ObjectIdentity = ObjectIdentity
hmSecVPNDynDNSRegister = _HmSecVPNDynDNSRegister_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1)
)
_HmSecVPNDynDNSReg_Type = TruthValue
_HmSecVPNDynDNSReg_Object = MibScalar
hmSecVPNDynDNSReg = _HmSecVPNDynDNSReg_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 1),
    _HmSecVPNDynDNSReg_Type()
)
hmSecVPNDynDNSReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSReg.setStatus("mandatory")
_HmSecVPNDynDNSRegInterval_Type = Integer32
_HmSecVPNDynDNSRegInterval_Object = MibScalar
hmSecVPNDynDNSRegInterval = _HmSecVPNDynDNSRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 2),
    _HmSecVPNDynDNSRegInterval_Type()
)
hmSecVPNDynDNSRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSRegInterval.setStatus("mandatory")
_HmSecVPNDynDNSRegServer_Type = DisplayString
_HmSecVPNDynDNSRegServer_Object = MibScalar
hmSecVPNDynDNSRegServer = _HmSecVPNDynDNSRegServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 3),
    _HmSecVPNDynDNSRegServer_Type()
)
hmSecVPNDynDNSRegServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSRegServer.setStatus("mandatory")
_HmSecVPNDynDNSRegLogin_Type = DisplayString
_HmSecVPNDynDNSRegLogin_Object = MibScalar
hmSecVPNDynDNSRegLogin = _HmSecVPNDynDNSRegLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 4),
    _HmSecVPNDynDNSRegLogin_Type()
)
hmSecVPNDynDNSRegLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSRegLogin.setStatus("mandatory")
_HmSecVPNDynDNSRegPasswd_Type = DisplayString
_HmSecVPNDynDNSRegPasswd_Object = MibScalar
hmSecVPNDynDNSRegPasswd = _HmSecVPNDynDNSRegPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 5),
    _HmSecVPNDynDNSRegPasswd_Type()
)
hmSecVPNDynDNSRegPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSRegPasswd.setStatus("mandatory")


class _HmSecVPNDynDNSRegProvider_Type(Integer32):
    """Custom type hmSecVPNDynDNSRegProvider based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inominate", 1),
          ("dyndns", 2),
          ("dns4biz", 3))
    )


_HmSecVPNDynDNSRegProvider_Type.__name__ = "Integer32"
_HmSecVPNDynDNSRegProvider_Object = MibScalar
hmSecVPNDynDNSRegProvider = _HmSecVPNDynDNSRegProvider_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 6),
    _HmSecVPNDynDNSRegProvider_Type()
)
hmSecVPNDynDNSRegProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSRegProvider.setStatus("mandatory")
_HmSecVPNDynDNSRegHostname_Type = DisplayString
_HmSecVPNDynDNSRegHostname_Object = MibScalar
hmSecVPNDynDNSRegHostname = _HmSecVPNDynDNSRegHostname_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 1, 7),
    _HmSecVPNDynDNSRegHostname_Type()
)
hmSecVPNDynDNSRegHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSRegHostname.setStatus("mandatory")
_HmSecVPNDynDNSCheck_ObjectIdentity = ObjectIdentity
hmSecVPNDynDNSCheck = _HmSecVPNDynDNSCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 2)
)
_HmSecVPNDynDNSCheckDo_Type = TruthValue
_HmSecVPNDynDNSCheckDo_Object = MibScalar
hmSecVPNDynDNSCheckDo = _HmSecVPNDynDNSCheckDo_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 2, 1),
    _HmSecVPNDynDNSCheckDo_Type()
)
hmSecVPNDynDNSCheckDo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSCheckDo.setStatus("mandatory")
_HmSecVPNDynDNSCheckRefresh_Type = Integer32
_HmSecVPNDynDNSCheckRefresh_Object = MibScalar
hmSecVPNDynDNSCheckRefresh = _HmSecVPNDynDNSCheckRefresh_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 4, 2, 2),
    _HmSecVPNDynDNSCheckRefresh_Type()
)
hmSecVPNDynDNSCheckRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNDynDNSCheckRefresh.setStatus("mandatory")
_HmSecVPNL2TP_ObjectIdentity = ObjectIdentity
hmSecVPNL2TP = _HmSecVPNL2TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5)
)


class _HmSecVPNL2TPStart_Type(Integer32):
    """Custom type hmSecVPNL2TPStart based on Integer32"""
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


_HmSecVPNL2TPStart_Type.__name__ = "Integer32"
_HmSecVPNL2TPStart_Object = MibScalar
hmSecVPNL2TPStart = _HmSecVPNL2TPStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 1),
    _HmSecVPNL2TPStart_Type()
)
hmSecVPNL2TPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNL2TPStart.setStatus("mandatory")
_HmSecVPNL2TPLocalIP_Type = IpAddress
_HmSecVPNL2TPLocalIP_Object = MibScalar
hmSecVPNL2TPLocalIP = _HmSecVPNL2TPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 2),
    _HmSecVPNL2TPLocalIP_Type()
)
hmSecVPNL2TPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNL2TPLocalIP.setStatus("mandatory")
_HmSecVPNL2TPRemoteIPRangeStart_Type = IpAddress
_HmSecVPNL2TPRemoteIPRangeStart_Object = MibScalar
hmSecVPNL2TPRemoteIPRangeStart = _HmSecVPNL2TPRemoteIPRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 3),
    _HmSecVPNL2TPRemoteIPRangeStart_Type()
)
hmSecVPNL2TPRemoteIPRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNL2TPRemoteIPRangeStart.setStatus("mandatory")
_HmSecVPNL2TPRemoteIPRangeEnd_Type = IpAddress
_HmSecVPNL2TPRemoteIPRangeEnd_Object = MibScalar
hmSecVPNL2TPRemoteIPRangeEnd = _HmSecVPNL2TPRemoteIPRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 4),
    _HmSecVPNL2TPRemoteIPRangeEnd_Type()
)
hmSecVPNL2TPRemoteIPRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNL2TPRemoteIPRangeEnd.setStatus("mandatory")
_HmSecVPNL2TPpppdOptTable_Object = MibTable
hmSecVPNL2TPpppdOptTable = _HmSecVPNL2TPpppdOptTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 5)
)
if mibBuilder.loadTexts:
    hmSecVPNL2TPpppdOptTable.setStatus("mandatory")
_HmSecVPNL2TPpppdOptEntry_Object = MibTableRow
hmSecVPNL2TPpppdOptEntry = _HmSecVPNL2TPpppdOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 5, 1)
)
hmSecVPNL2TPpppdOptEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecVPNL2TPpppdOptIndex"),
)
if mibBuilder.loadTexts:
    hmSecVPNL2TPpppdOptEntry.setStatus("mandatory")


class _HmSecVPNL2TPpppdOptIndex_Type(Integer32):
    """Custom type hmSecVPNL2TPpppdOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecVPNL2TPpppdOptIndex_Type.__name__ = "Integer32"
_HmSecVPNL2TPpppdOptIndex_Object = MibTableColumn
hmSecVPNL2TPpppdOptIndex = _HmSecVPNL2TPpppdOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 5, 1, 1),
    _HmSecVPNL2TPpppdOptIndex_Type()
)
hmSecVPNL2TPpppdOptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecVPNL2TPpppdOptIndex.setStatus("mandatory")
_HmSecVPNL2TPpppdOptValue_Type = DisplayString
_HmSecVPNL2TPpppdOptValue_Object = MibTableColumn
hmSecVPNL2TPpppdOptValue = _HmSecVPNL2TPpppdOptValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 5, 1, 2),
    _HmSecVPNL2TPpppdOptValue_Type()
)
hmSecVPNL2TPpppdOptValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNL2TPpppdOptValue.setStatus("mandatory")
_HmSecVPNL2TPpppdOptRowStatus_Type = RowStatus
_HmSecVPNL2TPpppdOptRowStatus_Object = MibTableColumn
hmSecVPNL2TPpppdOptRowStatus = _HmSecVPNL2TPpppdOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 5, 5, 1, 3),
    _HmSecVPNL2TPpppdOptRowStatus_Type()
)
hmSecVPNL2TPpppdOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNL2TPpppdOptRowStatus.setStatus("mandatory")
_HmSecVPNSettings_ObjectIdentity = ObjectIdentity
hmSecVPNSettings = _HmSecVPNSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6)
)


class _HmSecVPNRequireUniqueIDs_Type(Integer32):
    """Custom type hmSecVPNRequireUniqueIDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNRequireUniqueIDs_Type.__name__ = "Integer32"
_HmSecVPNRequireUniqueIDs_Object = MibScalar
hmSecVPNRequireUniqueIDs = _HmSecVPNRequireUniqueIDs_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 1),
    _HmSecVPNRequireUniqueIDs_Type()
)
hmSecVPNRequireUniqueIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNRequireUniqueIDs.setStatus("mandatory")


class _HmSecVPNNatTraversal_Type(Integer32):
    """Custom type hmSecVPNNatTraversal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HmSecVPNNatTraversal_Type.__name__ = "Integer32"
_HmSecVPNNatTraversal_Object = MibScalar
hmSecVPNNatTraversal = _HmSecVPNNatTraversal_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 2),
    _HmSecVPNNatTraversal_Type()
)
hmSecVPNNatTraversal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNNatTraversal.setStatus("mandatory")


class _HmSecVPNNatTPortfloating_Type(Integer32):
    """Custom type hmSecVPNNatTPortfloating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HmSecVPNNatTPortfloating_Type.__name__ = "Integer32"
_HmSecVPNNatTPortfloating_Object = MibScalar
hmSecVPNNatTPortfloating = _HmSecVPNNatTPortfloating_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 3),
    _HmSecVPNNatTPortfloating_Type()
)
hmSecVPNNatTPortfloating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNNatTPortfloating.setStatus("mandatory")
_HmSecVPNNatTKeepAliveInterval_Type = Integer32
_HmSecVPNNatTKeepAliveInterval_Object = MibScalar
hmSecVPNNatTKeepAliveInterval = _HmSecVPNNatTKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 4),
    _HmSecVPNNatTKeepAliveInterval_Type()
)
hmSecVPNNatTKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNNatTKeepAliveInterval.setStatus("mandatory")


class _HmSecVPNNatTKeepAliveForce_Type(Integer32):
    """Custom type hmSecVPNNatTKeepAliveForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNNatTKeepAliveForce_Type.__name__ = "Integer32"
_HmSecVPNNatTKeepAliveForce_Object = MibScalar
hmSecVPNNatTKeepAliveForce = _HmSecVPNNatTKeepAliveForce_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 5),
    _HmSecVPNNatTKeepAliveForce_Type()
)
hmSecVPNNatTKeepAliveForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNNatTKeepAliveForce.setStatus("mandatory")


class _HmSecVPNIkeLog_Type(Integer32):
    """Custom type hmSecVPNIkeLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNIkeLog_Type.__name__ = "Integer32"
_HmSecVPNIkeLog_Object = MibScalar
hmSecVPNIkeLog = _HmSecVPNIkeLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 6),
    _HmSecVPNIkeLog_Type()
)
hmSecVPNIkeLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNIkeLog.setStatus("mandatory")


class _HmSecVPNHideTos_Type(Integer32):
    """Custom type hmSecVPNHideTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNHideTos_Type.__name__ = "Integer32"
_HmSecVPNHideTos_Object = MibScalar
hmSecVPNHideTos = _HmSecVPNHideTos_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 7),
    _HmSecVPNHideTos_Type()
)
hmSecVPNHideTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNHideTos.setStatus("mandatory")
_HmSecVPNmtu_Type = Integer32
_HmSecVPNmtu_Object = MibScalar
hmSecVPNmtu = _HmSecVPNmtu_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 8),
    _HmSecVPNmtu_Type()
)
hmSecVPNmtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNmtu.setStatus("mandatory")


class _HmSecVPNStrictCRLPolicy_Type(Integer32):
    """Custom type hmSecVPNStrictCRLPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNStrictCRLPolicy_Type.__name__ = "Integer32"
_HmSecVPNStrictCRLPolicy_Object = MibScalar
hmSecVPNStrictCRLPolicy = _HmSecVPNStrictCRLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 9),
    _HmSecVPNStrictCRLPolicy_Type()
)
hmSecVPNStrictCRLPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNStrictCRLPolicy.setStatus("mandatory")


class _HmSecVPNNoCertReqSend_Type(Integer32):
    """Custom type hmSecVPNNoCertReqSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecVPNNoCertReqSend_Type.__name__ = "Integer32"
_HmSecVPNNoCertReqSend_Object = MibScalar
hmSecVPNNoCertReqSend = _HmSecVPNNoCertReqSend_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 1, 6, 10),
    _HmSecVPNNoCertReqSend_Type()
)
hmSecVPNNoCertReqSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecVPNNoCertReqSend.setStatus("mandatory")
_HmSecFirewall_ObjectIdentity = ObjectIdentity
hmSecFirewall = _HmSecFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2)
)
_HmSecFirewallIncoming_ObjectIdentity = ObjectIdentity
hmSecFirewallIncoming = _HmSecFirewallIncoming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1)
)
_HmSecFirewallIncomingTable_Object = MibTable
hmSecFirewallIncomingTable = _HmSecFirewallIncomingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hmSecFirewallIncomingTable.setStatus("mandatory")
_HmSecFirewallIncomingEntry_Object = MibTableRow
hmSecFirewallIncomingEntry = _HmSecFirewallIncomingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1)
)
hmSecFirewallIncomingEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecFWINruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecFirewallIncomingEntry.setStatus("mandatory")


class _HmSecFWINruleIndex_Type(Integer32):
    """Custom type hmSecFWINruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecFWINruleIndex_Type.__name__ = "Integer32"
_HmSecFWINruleIndex_Object = MibTableColumn
hmSecFWINruleIndex = _HmSecFWINruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 1),
    _HmSecFWINruleIndex_Type()
)
hmSecFWINruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecFWINruleIndex.setStatus("mandatory")
_HmSecFWINsourceIP_Type = DisplayString
_HmSecFWINsourceIP_Object = MibTableColumn
hmSecFWINsourceIP = _HmSecFWINsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 2),
    _HmSecFWINsourceIP_Type()
)
hmSecFWINsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINsourceIP.setStatus("mandatory")
_HmSecFWINdestinationIP_Type = DisplayString
_HmSecFWINdestinationIP_Object = MibTableColumn
hmSecFWINdestinationIP = _HmSecFWINdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 3),
    _HmSecFWINdestinationIP_Type()
)
hmSecFWINdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINdestinationIP.setStatus("mandatory")
_HmSecFWINsport_Type = DisplayString
_HmSecFWINsport_Object = MibTableColumn
hmSecFWINsport = _HmSecFWINsport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 4),
    _HmSecFWINsport_Type()
)
hmSecFWINsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINsport.setStatus("mandatory")
_HmSecFWINdport_Type = DisplayString
_HmSecFWINdport_Object = MibTableColumn
hmSecFWINdport = _HmSecFWINdport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 5),
    _HmSecFWINdport_Type()
)
hmSecFWINdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINdport.setStatus("mandatory")


class _HmSecFWINtarget_Type(Integer32):
    """Custom type hmSecFWINtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecFWINtarget_Type.__name__ = "Integer32"
_HmSecFWINtarget_Object = MibTableColumn
hmSecFWINtarget = _HmSecFWINtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 6),
    _HmSecFWINtarget_Type()
)
hmSecFWINtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINtarget.setStatus("mandatory")


class _HmSecFWINproto_Type(Integer32):
    """Custom type hmSecFWINproto based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("all", 4))
    )


_HmSecFWINproto_Type.__name__ = "Integer32"
_HmSecFWINproto_Object = MibTableColumn
hmSecFWINproto = _HmSecFWINproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 7),
    _HmSecFWINproto_Type()
)
hmSecFWINproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINproto.setStatus("mandatory")


class _HmSecFWINlog_Type(Integer32):
    """Custom type hmSecFWINlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFWINlog_Type.__name__ = "Integer32"
_HmSecFWINlog_Object = MibTableColumn
hmSecFWINlog = _HmSecFWINlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 8),
    _HmSecFWINlog_Type()
)
hmSecFWINlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINlog.setStatus("mandatory")
_HmSecFWINRowStatus_Type = RowStatus
_HmSecFWINRowStatus_Object = MibTableColumn
hmSecFWINRowStatus = _HmSecFWINRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 9),
    _HmSecFWINRowStatus_Type()
)
hmSecFWINRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINRowStatus.setStatus("mandatory")
_HmSecFWINcomment_Type = DisplayString
_HmSecFWINcomment_Object = MibTableColumn
hmSecFWINcomment = _HmSecFWINcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 1, 1, 10),
    _HmSecFWINcomment_Type()
)
hmSecFWINcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWINcomment.setStatus("mandatory")


class _HmSecFirewallINLogDefault_Type(Integer32):
    """Custom type hmSecFirewallINLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallINLogDefault_Type.__name__ = "Integer32"
_HmSecFirewallINLogDefault_Object = MibScalar
hmSecFirewallINLogDefault = _HmSecFirewallINLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 1, 2),
    _HmSecFirewallINLogDefault_Type()
)
hmSecFirewallINLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallINLogDefault.setStatus("mandatory")
_HmSecFirewallOutgoing_ObjectIdentity = ObjectIdentity
hmSecFirewallOutgoing = _HmSecFirewallOutgoing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2)
)
_HmSecFirewallOutgoingTable_Object = MibTable
hmSecFirewallOutgoingTable = _HmSecFirewallOutgoingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hmSecFirewallOutgoingTable.setStatus("mandatory")
_HmSecFirewallOutgoingEntry_Object = MibTableRow
hmSecFirewallOutgoingEntry = _HmSecFirewallOutgoingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1)
)
hmSecFirewallOutgoingEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecFWOUTruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecFirewallOutgoingEntry.setStatus("mandatory")


class _HmSecFWOUTruleIndex_Type(Integer32):
    """Custom type hmSecFWOUTruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecFWOUTruleIndex_Type.__name__ = "Integer32"
_HmSecFWOUTruleIndex_Object = MibTableColumn
hmSecFWOUTruleIndex = _HmSecFWOUTruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 1),
    _HmSecFWOUTruleIndex_Type()
)
hmSecFWOUTruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecFWOUTruleIndex.setStatus("mandatory")
_HmSecFWOUTsourceIP_Type = DisplayString
_HmSecFWOUTsourceIP_Object = MibTableColumn
hmSecFWOUTsourceIP = _HmSecFWOUTsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 2),
    _HmSecFWOUTsourceIP_Type()
)
hmSecFWOUTsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTsourceIP.setStatus("mandatory")
_HmSecFWOUTdestinationIP_Type = DisplayString
_HmSecFWOUTdestinationIP_Object = MibTableColumn
hmSecFWOUTdestinationIP = _HmSecFWOUTdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 3),
    _HmSecFWOUTdestinationIP_Type()
)
hmSecFWOUTdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTdestinationIP.setStatus("mandatory")
_HmSecFWOUTsport_Type = DisplayString
_HmSecFWOUTsport_Object = MibTableColumn
hmSecFWOUTsport = _HmSecFWOUTsport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 4),
    _HmSecFWOUTsport_Type()
)
hmSecFWOUTsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTsport.setStatus("mandatory")
_HmSecFWOUTdport_Type = DisplayString
_HmSecFWOUTdport_Object = MibTableColumn
hmSecFWOUTdport = _HmSecFWOUTdport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 5),
    _HmSecFWOUTdport_Type()
)
hmSecFWOUTdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTdport.setStatus("mandatory")


class _HmSecFWOUTtarget_Type(Integer32):
    """Custom type hmSecFWOUTtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecFWOUTtarget_Type.__name__ = "Integer32"
_HmSecFWOUTtarget_Object = MibTableColumn
hmSecFWOUTtarget = _HmSecFWOUTtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 6),
    _HmSecFWOUTtarget_Type()
)
hmSecFWOUTtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTtarget.setStatus("mandatory")


class _HmSecFWOUTproto_Type(Integer32):
    """Custom type hmSecFWOUTproto based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("all", 4))
    )


_HmSecFWOUTproto_Type.__name__ = "Integer32"
_HmSecFWOUTproto_Object = MibTableColumn
hmSecFWOUTproto = _HmSecFWOUTproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 7),
    _HmSecFWOUTproto_Type()
)
hmSecFWOUTproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTproto.setStatus("mandatory")


class _HmSecFWOUTlog_Type(Integer32):
    """Custom type hmSecFWOUTlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFWOUTlog_Type.__name__ = "Integer32"
_HmSecFWOUTlog_Object = MibTableColumn
hmSecFWOUTlog = _HmSecFWOUTlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 8),
    _HmSecFWOUTlog_Type()
)
hmSecFWOUTlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTlog.setStatus("mandatory")
_HmSecFWOUTRowStatus_Type = RowStatus
_HmSecFWOUTRowStatus_Object = MibTableColumn
hmSecFWOUTRowStatus = _HmSecFWOUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 9),
    _HmSecFWOUTRowStatus_Type()
)
hmSecFWOUTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTRowStatus.setStatus("mandatory")
_HmSecFWOUTcomment_Type = DisplayString
_HmSecFWOUTcomment_Object = MibTableColumn
hmSecFWOUTcomment = _HmSecFWOUTcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 1, 1, 10),
    _HmSecFWOUTcomment_Type()
)
hmSecFWOUTcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWOUTcomment.setStatus("mandatory")


class _HmSecFirewallOUTLogDefault_Type(Integer32):
    """Custom type hmSecFirewallOUTLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallOUTLogDefault_Type.__name__ = "Integer32"
_HmSecFirewallOUTLogDefault_Object = MibScalar
hmSecFirewallOUTLogDefault = _HmSecFirewallOUTLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 2, 2),
    _HmSecFirewallOUTLogDefault_Type()
)
hmSecFirewallOUTLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallOUTLogDefault.setStatus("mandatory")
_HmSecFirewallPortforwarding_ObjectIdentity = ObjectIdentity
hmSecFirewallPortforwarding = _HmSecFirewallPortforwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3)
)
_HmSecFirewallPortforwardTable_Object = MibTable
hmSecFirewallPortforwardTable = _HmSecFirewallPortforwardTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hmSecFirewallPortforwardTable.setStatus("mandatory")
_HmSecFirewallPortforwardEntry_Object = MibTableRow
hmSecFirewallPortforwardEntry = _HmSecFirewallPortforwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1)
)
hmSecFirewallPortforwardEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecFWPORTFORWruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecFirewallPortforwardEntry.setStatus("mandatory")


class _HmSecFWPORTFORWruleIndex_Type(Integer32):
    """Custom type hmSecFWPORTFORWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecFWPORTFORWruleIndex_Type.__name__ = "Integer32"
_HmSecFWPORTFORWruleIndex_Object = MibTableColumn
hmSecFWPORTFORWruleIndex = _HmSecFWPORTFORWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 1),
    _HmSecFWPORTFORWruleIndex_Type()
)
hmSecFWPORTFORWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWruleIndex.setStatus("mandatory")
_HmSecFWPORTFORWinIP_Type = DisplayString
_HmSecFWPORTFORWinIP_Object = MibTableColumn
hmSecFWPORTFORWinIP = _HmSecFWPORTFORWinIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 2),
    _HmSecFWPORTFORWinIP_Type()
)
hmSecFWPORTFORWinIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWinIP.setStatus("mandatory")
_HmSecFWPORTFORWoutIP_Type = DisplayString
_HmSecFWPORTFORWoutIP_Object = MibTableColumn
hmSecFWPORTFORWoutIP = _HmSecFWPORTFORWoutIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 3),
    _HmSecFWPORTFORWoutIP_Type()
)
hmSecFWPORTFORWoutIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWoutIP.setStatus("mandatory")
_HmSecFWPORTFORWinport_Type = DisplayString
_HmSecFWPORTFORWinport_Object = MibTableColumn
hmSecFWPORTFORWinport = _HmSecFWPORTFORWinport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 4),
    _HmSecFWPORTFORWinport_Type()
)
hmSecFWPORTFORWinport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWinport.setStatus("mandatory")
_HmSecFWPORTFORWoutport_Type = DisplayString
_HmSecFWPORTFORWoutport_Object = MibTableColumn
hmSecFWPORTFORWoutport = _HmSecFWPORTFORWoutport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 5),
    _HmSecFWPORTFORWoutport_Type()
)
hmSecFWPORTFORWoutport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWoutport.setStatus("mandatory")


class _HmSecFWPORTFORWproto_Type(Integer32):
    """Custom type hmSecFWPORTFORWproto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_HmSecFWPORTFORWproto_Type.__name__ = "Integer32"
_HmSecFWPORTFORWproto_Object = MibTableColumn
hmSecFWPORTFORWproto = _HmSecFWPORTFORWproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 6),
    _HmSecFWPORTFORWproto_Type()
)
hmSecFWPORTFORWproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWproto.setStatus("mandatory")


class _HmSecFWPORTFORWlog_Type(Integer32):
    """Custom type hmSecFWPORTFORWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFWPORTFORWlog_Type.__name__ = "Integer32"
_HmSecFWPORTFORWlog_Object = MibTableColumn
hmSecFWPORTFORWlog = _HmSecFWPORTFORWlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 7),
    _HmSecFWPORTFORWlog_Type()
)
hmSecFWPORTFORWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWlog.setStatus("mandatory")
_HmSecFWPORTFORWRowStatus_Type = RowStatus
_HmSecFWPORTFORWRowStatus_Object = MibTableColumn
hmSecFWPORTFORWRowStatus = _HmSecFWPORTFORWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 8),
    _HmSecFWPORTFORWRowStatus_Type()
)
hmSecFWPORTFORWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWRowStatus.setStatus("mandatory")
_HmSecFWPORTFORWsrcIP_Type = DisplayString
_HmSecFWPORTFORWsrcIP_Object = MibTableColumn
hmSecFWPORTFORWsrcIP = _HmSecFWPORTFORWsrcIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 9),
    _HmSecFWPORTFORWsrcIP_Type()
)
hmSecFWPORTFORWsrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWsrcIP.setStatus("mandatory")
_HmSecFWPORTFORWsrcport_Type = DisplayString
_HmSecFWPORTFORWsrcport_Object = MibTableColumn
hmSecFWPORTFORWsrcport = _HmSecFWPORTFORWsrcport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 10),
    _HmSecFWPORTFORWsrcport_Type()
)
hmSecFWPORTFORWsrcport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWsrcport.setStatus("mandatory")
_HmSecFWPORTFORWcomment_Type = DisplayString
_HmSecFWPORTFORWcomment_Object = MibTableColumn
hmSecFWPORTFORWcomment = _HmSecFWPORTFORWcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 3, 1, 1, 11),
    _HmSecFWPORTFORWcomment_Type()
)
hmSecFWPORTFORWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWPORTFORWcomment.setStatus("mandatory")
_HmSecFirewallNAT_ObjectIdentity = ObjectIdentity
hmSecFirewallNAT = _HmSecFirewallNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4)
)
_HmSecFirewallNATRuleTable_Object = MibTable
hmSecFirewallNATRuleTable = _HmSecFirewallNATRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hmSecFirewallNATRuleTable.setStatus("mandatory")
_HmSecFirewallNATRuleEntry_Object = MibTableRow
hmSecFirewallNATRuleEntry = _HmSecFirewallNATRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4, 1, 1)
)
hmSecFirewallNATRuleEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecFWNATruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecFirewallNATRuleEntry.setStatus("mandatory")


class _HmSecFWNATruleIndex_Type(Integer32):
    """Custom type hmSecFWNATruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecFWNATruleIndex_Type.__name__ = "Integer32"
_HmSecFWNATruleIndex_Object = MibTableColumn
hmSecFWNATruleIndex = _HmSecFWNATruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4, 1, 1, 1),
    _HmSecFWNATruleIndex_Type()
)
hmSecFWNATruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecFWNATruleIndex.setStatus("mandatory")
_HmSecFWNATIP_Type = DisplayString
_HmSecFWNATIP_Object = MibTableColumn
hmSecFWNATIP = _HmSecFWNATIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4, 1, 1, 2),
    _HmSecFWNATIP_Type()
)
hmSecFWNATIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWNATIP.setStatus("mandatory")
_HmSecFWNATRowStatus_Type = RowStatus
_HmSecFWNATRowStatus_Object = MibTableColumn
hmSecFWNATRowStatus = _HmSecFWNATRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4, 1, 1, 3),
    _HmSecFWNATRowStatus_Type()
)
hmSecFWNATRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWNATRowStatus.setStatus("mandatory")
_HmSecFWNATOutIP_Type = DisplayString
_HmSecFWNATOutIP_Object = MibTableColumn
hmSecFWNATOutIP = _HmSecFWNATOutIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 4, 1, 1, 4),
    _HmSecFWNATOutIP_Type()
)
hmSecFWNATOutIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFWNATOutIP.setStatus("mandatory")
_HmSecFirewallExtended_ObjectIdentity = ObjectIdentity
hmSecFirewallExtended = _HmSecFirewallExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5)
)
_HmSecFirewallIPConntrackMax_Type = Integer32
_HmSecFirewallIPConntrackMax_Object = MibScalar
hmSecFirewallIPConntrackMax = _HmSecFirewallIPConntrackMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 1),
    _HmSecFirewallIPConntrackMax_Type()
)
hmSecFirewallIPConntrackMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallIPConntrackMax.setStatus("mandatory")
_HmSecFirewallIPSynfloodLimitInt_Type = Integer32
_HmSecFirewallIPSynfloodLimitInt_Object = MibScalar
hmSecFirewallIPSynfloodLimitInt = _HmSecFirewallIPSynfloodLimitInt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 2),
    _HmSecFirewallIPSynfloodLimitInt_Type()
)
hmSecFirewallIPSynfloodLimitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallIPSynfloodLimitInt.setStatus("mandatory")
_HmSecFirewallIPSynfloodLimitExt_Type = Integer32
_HmSecFirewallIPSynfloodLimitExt_Object = MibScalar
hmSecFirewallIPSynfloodLimitExt = _HmSecFirewallIPSynfloodLimitExt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 3),
    _HmSecFirewallIPSynfloodLimitExt_Type()
)
hmSecFirewallIPSynfloodLimitExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallIPSynfloodLimitExt.setStatus("mandatory")
_HmSecFirewallICMPLimitInt_Type = Integer32
_HmSecFirewallICMPLimitInt_Object = MibScalar
hmSecFirewallICMPLimitInt = _HmSecFirewallICMPLimitInt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 4),
    _HmSecFirewallICMPLimitInt_Type()
)
hmSecFirewallICMPLimitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallICMPLimitInt.setStatus("mandatory")
_HmSecFirewallICMPLimitExt_Type = Integer32
_HmSecFirewallICMPLimitExt_Object = MibScalar
hmSecFirewallICMPLimitExt = _HmSecFirewallICMPLimitExt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 5),
    _HmSecFirewallICMPLimitExt_Type()
)
hmSecFirewallICMPLimitExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallICMPLimitExt.setStatus("mandatory")


class _HmSecFirewallEnableConntrackFTP_Type(Integer32):
    """Custom type hmSecFirewallEnableConntrackFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallEnableConntrackFTP_Type.__name__ = "Integer32"
_HmSecFirewallEnableConntrackFTP_Object = MibScalar
hmSecFirewallEnableConntrackFTP = _HmSecFirewallEnableConntrackFTP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 6),
    _HmSecFirewallEnableConntrackFTP_Type()
)
hmSecFirewallEnableConntrackFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallEnableConntrackFTP.setStatus("mandatory")


class _HmSecFirewallConntrackIRC_Type(Integer32):
    """Custom type hmSecFirewallConntrackIRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallConntrackIRC_Type.__name__ = "Integer32"
_HmSecFirewallConntrackIRC_Object = MibScalar
hmSecFirewallConntrackIRC = _HmSecFirewallConntrackIRC_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 7),
    _HmSecFirewallConntrackIRC_Type()
)
hmSecFirewallConntrackIRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallConntrackIRC.setStatus("mandatory")


class _HmSecFirewallConntrackPPTP_Type(Integer32):
    """Custom type hmSecFirewallConntrackPPTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallConntrackPPTP_Type.__name__ = "Integer32"
_HmSecFirewallConntrackPPTP_Object = MibScalar
hmSecFirewallConntrackPPTP = _HmSecFirewallConntrackPPTP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 8),
    _HmSecFirewallConntrackPPTP_Type()
)
hmSecFirewallConntrackPPTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallConntrackPPTP.setStatus("mandatory")
_HmSecFirewallARPLimitInt_Type = Integer32
_HmSecFirewallARPLimitInt_Object = MibScalar
hmSecFirewallARPLimitInt = _HmSecFirewallARPLimitInt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 9),
    _HmSecFirewallARPLimitInt_Type()
)
hmSecFirewallARPLimitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallARPLimitInt.setStatus("mandatory")
_HmSecFirewallARPLimitExt_Type = Integer32
_HmSecFirewallARPLimitExt_Object = MibScalar
hmSecFirewallARPLimitExt = _HmSecFirewallARPLimitExt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 10),
    _HmSecFirewallARPLimitExt_Type()
)
hmSecFirewallARPLimitExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallARPLimitExt.setStatus("mandatory")


class _HmSecFirewallICMPPolicy_Type(Integer32):
    """Custom type hmSecFirewallICMPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("ping", 2),
          ("all", 3))
    )


_HmSecFirewallICMPPolicy_Type.__name__ = "Integer32"
_HmSecFirewallICMPPolicy_Object = MibScalar
hmSecFirewallICMPPolicy = _HmSecFirewallICMPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 11),
    _HmSecFirewallICMPPolicy_Type()
)
hmSecFirewallICMPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallICMPPolicy.setStatus("mandatory")


class _HmSecFirewallConntrackH323_Type(Integer32):
    """Custom type hmSecFirewallConntrackH323 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallConntrackH323_Type.__name__ = "Integer32"
_HmSecFirewallConntrackH323_Object = MibScalar
hmSecFirewallConntrackH323 = _HmSecFirewallConntrackH323_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 12),
    _HmSecFirewallConntrackH323_Type()
)
hmSecFirewallConntrackH323.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallConntrackH323.setStatus("mandatory")


class _HmSecFirewallIpUncleanMatch_Type(Integer32):
    """Custom type hmSecFirewallIpUncleanMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFirewallIpUncleanMatch_Type.__name__ = "Integer32"
_HmSecFirewallIpUncleanMatch_Object = MibScalar
hmSecFirewallIpUncleanMatch = _HmSecFirewallIpUncleanMatch_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 5, 13),
    _HmSecFirewallIpUncleanMatch_Type()
)
hmSecFirewallIpUncleanMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFirewallIpUncleanMatch.setStatus("mandatory")
_HmSecFirewall11NAT_ObjectIdentity = ObjectIdentity
hmSecFirewall11NAT = _HmSecFirewall11NAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6)
)
_HmSecFirewall11NATRuleTable_Object = MibTable
hmSecFirewall11NATRuleTable = _HmSecFirewall11NATRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hmSecFirewall11NATRuleTable.setStatus("mandatory")
_HmSecFirewall11NATRuleEntry_Object = MibTableRow
hmSecFirewall11NATRuleEntry = _HmSecFirewall11NATRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1)
)
hmSecFirewall11NATRuleEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecFW11NATruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecFirewall11NATRuleEntry.setStatus("mandatory")


class _HmSecFW11NATruleIndex_Type(Integer32):
    """Custom type hmSecFW11NATruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecFW11NATruleIndex_Type.__name__ = "Integer32"
_HmSecFW11NATruleIndex_Object = MibTableColumn
hmSecFW11NATruleIndex = _HmSecFW11NATruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1, 1),
    _HmSecFW11NATruleIndex_Type()
)
hmSecFW11NATruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecFW11NATruleIndex.setStatus("mandatory")
_HmSecFW11NATLocal_Type = IpAddress
_HmSecFW11NATLocal_Object = MibTableColumn
hmSecFW11NATLocal = _HmSecFW11NATLocal_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1, 2),
    _HmSecFW11NATLocal_Type()
)
hmSecFW11NATLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFW11NATLocal.setStatus("mandatory")
_HmSecFW11NATRemote_Type = IpAddress
_HmSecFW11NATRemote_Object = MibTableColumn
hmSecFW11NATRemote = _HmSecFW11NATRemote_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1, 3),
    _HmSecFW11NATRemote_Type()
)
hmSecFW11NATRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFW11NATRemote.setStatus("mandatory")
_HmSecFW11NATMask_Type = Integer32
_HmSecFW11NATMask_Object = MibTableColumn
hmSecFW11NATMask = _HmSecFW11NATMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1, 4),
    _HmSecFW11NATMask_Type()
)
hmSecFW11NATMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFW11NATMask.setStatus("mandatory")


class _HmSecFW11NATLog_Type(Integer32):
    """Custom type hmSecFW11NATLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecFW11NATLog_Type.__name__ = "Integer32"
_HmSecFW11NATLog_Object = MibTableColumn
hmSecFW11NATLog = _HmSecFW11NATLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1, 5),
    _HmSecFW11NATLog_Type()
)
hmSecFW11NATLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFW11NATLog.setStatus("mandatory")
_HmSecFW11NATRowStatus_Type = RowStatus
_HmSecFW11NATRowStatus_Object = MibTableColumn
hmSecFW11NATRowStatus = _HmSecFW11NATRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 2, 6, 1, 1, 10),
    _HmSecFW11NATRowStatus_Type()
)
hmSecFW11NATRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecFW11NATRowStatus.setStatus("mandatory")
_HmSecNetwork_ObjectIdentity = ObjectIdentity
hmSecNetwork = _HmSecNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3)
)


class _HmSecNetworkMode_Type(Integer32):
    """Custom type hmSecNetworkMode based on Integer32"""
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
        *(("stealth", 1),
          ("router", 2),
          ("pppoe", 3),
          ("pptp", 4))
    )


_HmSecNetworkMode_Type.__name__ = "Integer32"
_HmSecNetworkMode_Object = MibScalar
hmSecNetworkMode = _HmSecNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 1),
    _HmSecNetworkMode_Type()
)
hmSecNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkMode.setStatus("mandatory")
_HmSecStealth_ObjectIdentity = ObjectIdentity
hmSecStealth = _HmSecStealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2)
)


class _HmSecStealthIPConfMode_Type(Integer32):
    """Custom type hmSecStealthIPConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("static", 2),
          ("multi", 3))
    )


_HmSecStealthIPConfMode_Type.__name__ = "Integer32"
_HmSecStealthIPConfMode_Object = MibScalar
hmSecStealthIPConfMode = _HmSecStealthIPConfMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 1),
    _HmSecStealthIPConfMode_Type()
)
hmSecStealthIPConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthIPConfMode.setStatus("mandatory")
_HmSecStealthIPConfStatic_ObjectIdentity = ObjectIdentity
hmSecStealthIPConfStatic = _HmSecStealthIPConfStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2)
)
_HmSecStealthStaticIP_Type = IpAddress
_HmSecStealthStaticIP_Object = MibScalar
hmSecStealthStaticIP = _HmSecStealthStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 1),
    _HmSecStealthStaticIP_Type()
)
hmSecStealthStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthStaticIP.setStatus("mandatory")
_HmSecStealthStaticMAC_Type = MacAddress
_HmSecStealthStaticMAC_Object = MibScalar
hmSecStealthStaticMAC = _HmSecStealthStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 2),
    _HmSecStealthStaticMAC_Type()
)
hmSecStealthStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthStaticMAC.setStatus("mandatory")


class _HmSecStealthStaticActivate_Type(Integer32):
    """Custom type hmSecStealthStaticActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_HmSecStealthStaticActivate_Type.__name__ = "Integer32"
_HmSecStealthStaticActivate_Object = MibScalar
hmSecStealthStaticActivate = _HmSecStealthStaticActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 3),
    _HmSecStealthStaticActivate_Type()
)
hmSecStealthStaticActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthStaticActivate.setStatus("mandatory")
_HmSecStealthManageIP_Type = IpAddress
_HmSecStealthManageIP_Object = MibScalar
hmSecStealthManageIP = _HmSecStealthManageIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 4),
    _HmSecStealthManageIP_Type()
)
hmSecStealthManageIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthManageIP.setStatus("mandatory")
_HmSecStealthManageNetmask_Type = IpAddress
_HmSecStealthManageNetmask_Object = MibScalar
hmSecStealthManageNetmask = _HmSecStealthManageNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 5),
    _HmSecStealthManageNetmask_Type()
)
hmSecStealthManageNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthManageNetmask.setStatus("mandatory")
_HmSecStealthManageGateway_Type = IpAddress
_HmSecStealthManageGateway_Object = MibScalar
hmSecStealthManageGateway = _HmSecStealthManageGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 6),
    _HmSecStealthManageGateway_Type()
)
hmSecStealthManageGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthManageGateway.setStatus("mandatory")


class _HmSecStealthManageActivate_Type(Integer32):
    """Custom type hmSecStealthManageActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_HmSecStealthManageActivate_Type.__name__ = "Integer32"
_HmSecStealthManageActivate_Object = MibScalar
hmSecStealthManageActivate = _HmSecStealthManageActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 2, 7),
    _HmSecStealthManageActivate_Type()
)
hmSecStealthManageActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthManageActivate.setStatus("mandatory")


class _HmSecStealthHiDiscoveryRelay_Type(Integer32):
    """Custom type hmSecStealthHiDiscoveryRelay based on Integer32"""
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


_HmSecStealthHiDiscoveryRelay_Type.__name__ = "Integer32"
_HmSecStealthHiDiscoveryRelay_Object = MibScalar
hmSecStealthHiDiscoveryRelay = _HmSecStealthHiDiscoveryRelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 3),
    _HmSecStealthHiDiscoveryRelay_Type()
)
hmSecStealthHiDiscoveryRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthHiDiscoveryRelay.setStatus("mandatory")


class _HmSecStealthHiDiscoveryState_Type(Integer32):
    """Custom type hmSecStealthHiDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-write", 1),
          ("read-only", 2),
          ("disabled", 3))
    )


_HmSecStealthHiDiscoveryState_Type.__name__ = "Integer32"
_HmSecStealthHiDiscoveryState_Object = MibScalar
hmSecStealthHiDiscoveryState = _HmSecStealthHiDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 4),
    _HmSecStealthHiDiscoveryState_Type()
)
hmSecStealthHiDiscoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthHiDiscoveryState.setStatus("mandatory")
_HmSecStealthL2Filter_ObjectIdentity = ObjectIdentity
hmSecStealthL2Filter = _HmSecStealthL2Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5)
)
_HmSecL2FilterInternTable_Object = MibTable
hmSecL2FilterInternTable = _HmSecL2FilterInternTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hmSecL2FilterInternTable.setStatus("mandatory")
_HmSecL2FilterInternEntry_Object = MibTableRow
hmSecL2FilterInternEntry = _HmSecL2FilterInternEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1)
)
hmSecL2FilterInternEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecL2FilterInternRuleIndex"),
)
if mibBuilder.loadTexts:
    hmSecL2FilterInternEntry.setStatus("mandatory")


class _HmSecL2FilterInternRuleIndex_Type(Integer32):
    """Custom type hmSecL2FilterInternRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecL2FilterInternRuleIndex_Type.__name__ = "Integer32"
_HmSecL2FilterInternRuleIndex_Object = MibTableColumn
hmSecL2FilterInternRuleIndex = _HmSecL2FilterInternRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 1),
    _HmSecL2FilterInternRuleIndex_Type()
)
hmSecL2FilterInternRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecL2FilterInternRuleIndex.setStatus("mandatory")
_HmSecL2FilterInternRowStatus_Type = RowStatus
_HmSecL2FilterInternRowStatus_Object = MibTableColumn
hmSecL2FilterInternRowStatus = _HmSecL2FilterInternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 2),
    _HmSecL2FilterInternRowStatus_Type()
)
hmSecL2FilterInternRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterInternRowStatus.setStatus("mandatory")
_HmSecL2FilterInternSrcMac_Type = MacAddress
_HmSecL2FilterInternSrcMac_Object = MibTableColumn
hmSecL2FilterInternSrcMac = _HmSecL2FilterInternSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 3),
    _HmSecL2FilterInternSrcMac_Type()
)
hmSecL2FilterInternSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterInternSrcMac.setStatus("mandatory")
_HmSecL2FilterInternDstMac_Type = MacAddress
_HmSecL2FilterInternDstMac_Object = MibTableColumn
hmSecL2FilterInternDstMac = _HmSecL2FilterInternDstMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 4),
    _HmSecL2FilterInternDstMac_Type()
)
hmSecL2FilterInternDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterInternDstMac.setStatus("mandatory")
_HmSecL2FilterInternEthType_Type = Integer32
_HmSecL2FilterInternEthType_Object = MibTableColumn
hmSecL2FilterInternEthType = _HmSecL2FilterInternEthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 5),
    _HmSecL2FilterInternEthType_Type()
)
hmSecL2FilterInternEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterInternEthType.setStatus("mandatory")


class _HmSecL2FilterInternTarget_Type(Integer32):
    """Custom type hmSecL2FilterInternTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecL2FilterInternTarget_Type.__name__ = "Integer32"
_HmSecL2FilterInternTarget_Object = MibTableColumn
hmSecL2FilterInternTarget = _HmSecL2FilterInternTarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 6),
    _HmSecL2FilterInternTarget_Type()
)
hmSecL2FilterInternTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterInternTarget.setStatus("mandatory")
_HmSecL2FilterInternComment_Type = DisplayString
_HmSecL2FilterInternComment_Object = MibTableColumn
hmSecL2FilterInternComment = _HmSecL2FilterInternComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 1, 1, 7),
    _HmSecL2FilterInternComment_Type()
)
hmSecL2FilterInternComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterInternComment.setStatus("mandatory")
_HmSecL2FilterExternTable_Object = MibTable
hmSecL2FilterExternTable = _HmSecL2FilterExternTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    hmSecL2FilterExternTable.setStatus("mandatory")
_HmSecL2FilterExternEntry_Object = MibTableRow
hmSecL2FilterExternEntry = _HmSecL2FilterExternEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1)
)
hmSecL2FilterExternEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecL2FilterExternRuleIndex"),
)
if mibBuilder.loadTexts:
    hmSecL2FilterExternEntry.setStatus("mandatory")


class _HmSecL2FilterExternRuleIndex_Type(Integer32):
    """Custom type hmSecL2FilterExternRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecL2FilterExternRuleIndex_Type.__name__ = "Integer32"
_HmSecL2FilterExternRuleIndex_Object = MibTableColumn
hmSecL2FilterExternRuleIndex = _HmSecL2FilterExternRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 1),
    _HmSecL2FilterExternRuleIndex_Type()
)
hmSecL2FilterExternRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecL2FilterExternRuleIndex.setStatus("mandatory")
_HmSecL2FilterExternRowStatus_Type = RowStatus
_HmSecL2FilterExternRowStatus_Object = MibTableColumn
hmSecL2FilterExternRowStatus = _HmSecL2FilterExternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 2),
    _HmSecL2FilterExternRowStatus_Type()
)
hmSecL2FilterExternRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterExternRowStatus.setStatus("mandatory")
_HmSecL2FilterExternSrcMac_Type = MacAddress
_HmSecL2FilterExternSrcMac_Object = MibTableColumn
hmSecL2FilterExternSrcMac = _HmSecL2FilterExternSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 3),
    _HmSecL2FilterExternSrcMac_Type()
)
hmSecL2FilterExternSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterExternSrcMac.setStatus("mandatory")
_HmSecL2FilterExternDstMac_Type = MacAddress
_HmSecL2FilterExternDstMac_Object = MibTableColumn
hmSecL2FilterExternDstMac = _HmSecL2FilterExternDstMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 4),
    _HmSecL2FilterExternDstMac_Type()
)
hmSecL2FilterExternDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterExternDstMac.setStatus("mandatory")
_HmSecL2FilterExternEthType_Type = Integer32
_HmSecL2FilterExternEthType_Object = MibTableColumn
hmSecL2FilterExternEthType = _HmSecL2FilterExternEthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 5),
    _HmSecL2FilterExternEthType_Type()
)
hmSecL2FilterExternEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterExternEthType.setStatus("mandatory")


class _HmSecL2FilterExternTarget_Type(Integer32):
    """Custom type hmSecL2FilterExternTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecL2FilterExternTarget_Type.__name__ = "Integer32"
_HmSecL2FilterExternTarget_Object = MibTableColumn
hmSecL2FilterExternTarget = _HmSecL2FilterExternTarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 6),
    _HmSecL2FilterExternTarget_Type()
)
hmSecL2FilterExternTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterExternTarget.setStatus("mandatory")
_HmSecL2FilterExternComment_Type = DisplayString
_HmSecL2FilterExternComment_Object = MibTableColumn
hmSecL2FilterExternComment = _HmSecL2FilterExternComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 2, 1, 7),
    _HmSecL2FilterExternComment_Type()
)
hmSecL2FilterExternComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2FilterExternComment.setStatus("mandatory")


class _HmSecStealthL2ForwardGVRP_Type(Integer32):
    """Custom type hmSecStealthL2ForwardGVRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecStealthL2ForwardGVRP_Type.__name__ = "Integer32"
_HmSecStealthL2ForwardGVRP_Object = MibScalar
hmSecStealthL2ForwardGVRP = _HmSecStealthL2ForwardGVRP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 3),
    _HmSecStealthL2ForwardGVRP_Type()
)
hmSecStealthL2ForwardGVRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthL2ForwardGVRP.setStatus("mandatory")


class _HmSecStealthL2ForwardSTP_Type(Integer32):
    """Custom type hmSecStealthL2ForwardSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecStealthL2ForwardSTP_Type.__name__ = "Integer32"
_HmSecStealthL2ForwardSTP_Object = MibScalar
hmSecStealthL2ForwardSTP = _HmSecStealthL2ForwardSTP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 4),
    _HmSecStealthL2ForwardSTP_Type()
)
hmSecStealthL2ForwardSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthL2ForwardSTP.setStatus("mandatory")


class _HmSecStealthL2ForwardDHCP_Type(Integer32):
    """Custom type hmSecStealthL2ForwardDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecStealthL2ForwardDHCP_Type.__name__ = "Integer32"
_HmSecStealthL2ForwardDHCP_Object = MibScalar
hmSecStealthL2ForwardDHCP = _HmSecStealthL2ForwardDHCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 5, 5),
    _HmSecStealthL2ForwardDHCP_Type()
)
hmSecStealthL2ForwardDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthL2ForwardDHCP.setStatus("mandatory")
_HmSecStealthInterface_ObjectIdentity = ObjectIdentity
hmSecStealthInterface = _HmSecStealthInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 6)
)
_HmSecStealthMTU_Type = Integer32
_HmSecStealthMTU_Object = MibScalar
hmSecStealthMTU = _HmSecStealthMTU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 6, 1),
    _HmSecStealthMTU_Type()
)
hmSecStealthMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthMTU.setStatus("mandatory")
_HmSecStealthVlanMTU_Type = Integer32
_HmSecStealthVlanMTU_Object = MibScalar
hmSecStealthVlanMTU = _HmSecStealthVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 6, 2),
    _HmSecStealthVlanMTU_Type()
)
hmSecStealthVlanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthVlanMTU.setStatus("mandatory")


class _HmSecStealthManageUseVLAN_Type(Integer32):
    """Custom type hmSecStealthManageUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecStealthManageUseVLAN_Type.__name__ = "Integer32"
_HmSecStealthManageUseVLAN_Object = MibScalar
hmSecStealthManageUseVLAN = _HmSecStealthManageUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 6, 3),
    _HmSecStealthManageUseVLAN_Type()
)
hmSecStealthManageUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthManageUseVLAN.setStatus("mandatory")
_HmSecStealthManageVLanID_Type = Integer32
_HmSecStealthManageVLanID_Object = MibScalar
hmSecStealthManageVLanID = _HmSecStealthManageVLanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 2, 6, 4),
    _HmSecStealthManageVLanID_Type()
)
hmSecStealthManageVLanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecStealthManageVLanID.setStatus("mandatory")
_HmSecRouter_ObjectIdentity = ObjectIdentity
hmSecRouter = _HmSecRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3)
)
_HmSecRouterLocal_ObjectIdentity = ObjectIdentity
hmSecRouterLocal = _HmSecRouterLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1)
)
_HmSecRouterLocalIP_Type = IpAddress
_HmSecRouterLocalIP_Object = MibScalar
hmSecRouterLocalIP = _HmSecRouterLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 1),
    _HmSecRouterLocalIP_Type()
)
hmSecRouterLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalIP.setStatus("mandatory")
_HmSecRouterLocalNetmask_Type = IpAddress
_HmSecRouterLocalNetmask_Object = MibScalar
hmSecRouterLocalNetmask = _HmSecRouterLocalNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 2),
    _HmSecRouterLocalNetmask_Type()
)
hmSecRouterLocalNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalNetmask.setStatus("mandatory")


class _HmSecRouterLocalActivate_Type(Integer32):
    """Custom type hmSecRouterLocalActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_HmSecRouterLocalActivate_Type.__name__ = "Integer32"
_HmSecRouterLocalActivate_Object = MibScalar
hmSecRouterLocalActivate = _HmSecRouterLocalActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 3),
    _HmSecRouterLocalActivate_Type()
)
hmSecRouterLocalActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalActivate.setStatus("mandatory")
_HmSecRouterLocalAliasesTable_Object = MibTable
hmSecRouterLocalAliasesTable = _HmSecRouterLocalAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hmSecRouterLocalAliasesTable.setStatus("mandatory")
_HmSecRouterLocalAliasesEntry_Object = MibTableRow
hmSecRouterLocalAliasesEntry = _HmSecRouterLocalAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1)
)
hmSecRouterLocalAliasesEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecLocalAliasIndex"),
)
if mibBuilder.loadTexts:
    hmSecRouterLocalAliasesEntry.setStatus("mandatory")


class _HmSecLocalAliasIndex_Type(Integer32):
    """Custom type hmSecLocalAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecLocalAliasIndex_Type.__name__ = "Integer32"
_HmSecLocalAliasIndex_Object = MibTableColumn
hmSecLocalAliasIndex = _HmSecLocalAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1, 1),
    _HmSecLocalAliasIndex_Type()
)
hmSecLocalAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecLocalAliasIndex.setStatus("mandatory")
_HmSecLocalAliasIpAddress_Type = IpAddress
_HmSecLocalAliasIpAddress_Object = MibTableColumn
hmSecLocalAliasIpAddress = _HmSecLocalAliasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1, 2),
    _HmSecLocalAliasIpAddress_Type()
)
hmSecLocalAliasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalAliasIpAddress.setStatus("mandatory")
_HmSecLocalAliasNetmask_Type = IpAddress
_HmSecLocalAliasNetmask_Object = MibTableColumn
hmSecLocalAliasNetmask = _HmSecLocalAliasNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1, 3),
    _HmSecLocalAliasNetmask_Type()
)
hmSecLocalAliasNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalAliasNetmask.setStatus("mandatory")
_HmSecLocalAliasRowStatus_Type = RowStatus
_HmSecLocalAliasRowStatus_Object = MibTableColumn
hmSecLocalAliasRowStatus = _HmSecLocalAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1, 4),
    _HmSecLocalAliasRowStatus_Type()
)
hmSecLocalAliasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalAliasRowStatus.setStatus("mandatory")


class _HmSecLocalAliasUseVLAN_Type(Integer32):
    """Custom type hmSecLocalAliasUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecLocalAliasUseVLAN_Type.__name__ = "Integer32"
_HmSecLocalAliasUseVLAN_Object = MibTableColumn
hmSecLocalAliasUseVLAN = _HmSecLocalAliasUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1, 5),
    _HmSecLocalAliasUseVLAN_Type()
)
hmSecLocalAliasUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalAliasUseVLAN.setStatus("mandatory")
_HmSecLocalAliasVLANid_Type = Integer32
_HmSecLocalAliasVLANid_Object = MibTableColumn
hmSecLocalAliasVLANid = _HmSecLocalAliasVLANid_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 4, 1, 6),
    _HmSecLocalAliasVLANid_Type()
)
hmSecLocalAliasVLANid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalAliasVLANid.setStatus("mandatory")
_HmSecLocalRoutesTable_Object = MibTable
hmSecLocalRoutesTable = _HmSecLocalRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hmSecLocalRoutesTable.setStatus("mandatory")
_HmSecLocalRoutesEntry_Object = MibTableRow
hmSecLocalRoutesEntry = _HmSecLocalRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 5, 1)
)
hmSecLocalRoutesEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecLocalRouteIndex"),
)
if mibBuilder.loadTexts:
    hmSecLocalRoutesEntry.setStatus("mandatory")


class _HmSecLocalRouteIndex_Type(Integer32):
    """Custom type hmSecLocalRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecLocalRouteIndex_Type.__name__ = "Integer32"
_HmSecLocalRouteIndex_Object = MibTableColumn
hmSecLocalRouteIndex = _HmSecLocalRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 5, 1, 1),
    _HmSecLocalRouteIndex_Type()
)
hmSecLocalRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecLocalRouteIndex.setStatus("mandatory")
_HmSecLocalRouteNetwork_Type = DisplayString
_HmSecLocalRouteNetwork_Object = MibTableColumn
hmSecLocalRouteNetwork = _HmSecLocalRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 5, 1, 2),
    _HmSecLocalRouteNetwork_Type()
)
hmSecLocalRouteNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalRouteNetwork.setStatus("mandatory")
_HmSecLocalRouteGateway_Type = IpAddress
_HmSecLocalRouteGateway_Object = MibTableColumn
hmSecLocalRouteGateway = _HmSecLocalRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 5, 1, 3),
    _HmSecLocalRouteGateway_Type()
)
hmSecLocalRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalRouteGateway.setStatus("mandatory")
_HmSecLocalRouteRowStatus_Type = RowStatus
_HmSecLocalRouteRowStatus_Object = MibTableColumn
hmSecLocalRouteRowStatus = _HmSecLocalRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 5, 1, 4),
    _HmSecLocalRouteRowStatus_Type()
)
hmSecLocalRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLocalRouteRowStatus.setStatus("mandatory")
_HmSecRouterLocalDevMTU_Type = Integer32
_HmSecRouterLocalDevMTU_Object = MibScalar
hmSecRouterLocalDevMTU = _HmSecRouterLocalDevMTU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 6),
    _HmSecRouterLocalDevMTU_Type()
)
hmSecRouterLocalDevMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalDevMTU.setStatus("mandatory")


class _HmSecRouterLocalUseVLAN_Type(Integer32):
    """Custom type hmSecRouterLocalUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecRouterLocalUseVLAN_Type.__name__ = "Integer32"
_HmSecRouterLocalUseVLAN_Object = MibScalar
hmSecRouterLocalUseVLAN = _HmSecRouterLocalUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 7),
    _HmSecRouterLocalUseVLAN_Type()
)
hmSecRouterLocalUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalUseVLAN.setStatus("mandatory")
_HmSecRouterLocalVlanId_Type = Integer32
_HmSecRouterLocalVlanId_Object = MibScalar
hmSecRouterLocalVlanId = _HmSecRouterLocalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 8),
    _HmSecRouterLocalVlanId_Type()
)
hmSecRouterLocalVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalVlanId.setStatus("mandatory")
_HmSecRouterLocalDevVlanMTU_Type = Integer32
_HmSecRouterLocalDevVlanMTU_Object = MibScalar
hmSecRouterLocalDevVlanMTU = _HmSecRouterLocalDevVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 1, 9),
    _HmSecRouterLocalDevVlanMTU_Type()
)
hmSecRouterLocalDevVlanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterLocalDevVlanMTU.setStatus("mandatory")
_HmSecRouterExtern_ObjectIdentity = ObjectIdentity
hmSecRouterExtern = _HmSecRouterExtern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2)
)


class _HmSecRouterExternDHCP_Type(Integer32):
    """Custom type hmSecRouterExternDHCP based on Integer32"""
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


_HmSecRouterExternDHCP_Type.__name__ = "Integer32"
_HmSecRouterExternDHCP_Object = MibScalar
hmSecRouterExternDHCP = _HmSecRouterExternDHCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 1),
    _HmSecRouterExternDHCP_Type()
)
hmSecRouterExternDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternDHCP.setStatus("mandatory")
_HmSecRouterExternStatic_ObjectIdentity = ObjectIdentity
hmSecRouterExternStatic = _HmSecRouterExternStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2)
)
_HmSecRouterExternStaticIP_Type = IpAddress
_HmSecRouterExternStaticIP_Object = MibScalar
hmSecRouterExternStaticIP = _HmSecRouterExternStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 1),
    _HmSecRouterExternStaticIP_Type()
)
hmSecRouterExternStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternStaticIP.setStatus("mandatory")
_HmSecRouterExternStaticNetmask_Type = IpAddress
_HmSecRouterExternStaticNetmask_Object = MibScalar
hmSecRouterExternStaticNetmask = _HmSecRouterExternStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 2),
    _HmSecRouterExternStaticNetmask_Type()
)
hmSecRouterExternStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternStaticNetmask.setStatus("mandatory")
_HmSecRouterExternStaticGateway_Type = IpAddress
_HmSecRouterExternStaticGateway_Object = MibScalar
hmSecRouterExternStaticGateway = _HmSecRouterExternStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 3),
    _HmSecRouterExternStaticGateway_Type()
)
hmSecRouterExternStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternStaticGateway.setStatus("mandatory")


class _HmSecRouterExternActivate_Type(Integer32):
    """Custom type hmSecRouterExternActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("valuescached", 2))
    )


_HmSecRouterExternActivate_Type.__name__ = "Integer32"
_HmSecRouterExternActivate_Object = MibScalar
hmSecRouterExternActivate = _HmSecRouterExternActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 4),
    _HmSecRouterExternActivate_Type()
)
hmSecRouterExternActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternActivate.setStatus("mandatory")
_HmSecRouterExternAliasesTable_Object = MibTable
hmSecRouterExternAliasesTable = _HmSecRouterExternAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hmSecRouterExternAliasesTable.setStatus("mandatory")
_HmSecRouterExternAliasesEntry_Object = MibTableRow
hmSecRouterExternAliasesEntry = _HmSecRouterExternAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1)
)
hmSecRouterExternAliasesEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecExternAliasIndex"),
)
if mibBuilder.loadTexts:
    hmSecRouterExternAliasesEntry.setStatus("mandatory")


class _HmSecExternAliasIndex_Type(Integer32):
    """Custom type hmSecExternAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecExternAliasIndex_Type.__name__ = "Integer32"
_HmSecExternAliasIndex_Object = MibTableColumn
hmSecExternAliasIndex = _HmSecExternAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1, 1),
    _HmSecExternAliasIndex_Type()
)
hmSecExternAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecExternAliasIndex.setStatus("mandatory")
_HmSecExternAliasIpAddress_Type = IpAddress
_HmSecExternAliasIpAddress_Object = MibTableColumn
hmSecExternAliasIpAddress = _HmSecExternAliasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1, 2),
    _HmSecExternAliasIpAddress_Type()
)
hmSecExternAliasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternAliasIpAddress.setStatus("mandatory")
_HmSecExternAliasNetmask_Type = IpAddress
_HmSecExternAliasNetmask_Object = MibTableColumn
hmSecExternAliasNetmask = _HmSecExternAliasNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1, 3),
    _HmSecExternAliasNetmask_Type()
)
hmSecExternAliasNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternAliasNetmask.setStatus("mandatory")
_HmSecExternAliasRowStatus_Type = RowStatus
_HmSecExternAliasRowStatus_Object = MibTableColumn
hmSecExternAliasRowStatus = _HmSecExternAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1, 4),
    _HmSecExternAliasRowStatus_Type()
)
hmSecExternAliasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternAliasRowStatus.setStatus("mandatory")


class _HmSecExternAliasUseVLAN_Type(Integer32):
    """Custom type hmSecExternAliasUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecExternAliasUseVLAN_Type.__name__ = "Integer32"
_HmSecExternAliasUseVLAN_Object = MibTableColumn
hmSecExternAliasUseVLAN = _HmSecExternAliasUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1, 5),
    _HmSecExternAliasUseVLAN_Type()
)
hmSecExternAliasUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternAliasUseVLAN.setStatus("mandatory")
_HmSecExternAliasVLANid_Type = Integer32
_HmSecExternAliasVLANid_Object = MibTableColumn
hmSecExternAliasVLANid = _HmSecExternAliasVLANid_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 5, 1, 6),
    _HmSecExternAliasVLANid_Type()
)
hmSecExternAliasVLANid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternAliasVLANid.setStatus("mandatory")
_HmSecExternRoutesTable_Object = MibTable
hmSecExternRoutesTable = _HmSecExternRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hmSecExternRoutesTable.setStatus("mandatory")
_HmSecExternRoutesEntry_Object = MibTableRow
hmSecExternRoutesEntry = _HmSecExternRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 6, 1)
)
hmSecExternRoutesEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecExternRouteIndex"),
)
if mibBuilder.loadTexts:
    hmSecExternRoutesEntry.setStatus("mandatory")


class _HmSecExternRouteIndex_Type(Integer32):
    """Custom type hmSecExternRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecExternRouteIndex_Type.__name__ = "Integer32"
_HmSecExternRouteIndex_Object = MibTableColumn
hmSecExternRouteIndex = _HmSecExternRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 6, 1, 1),
    _HmSecExternRouteIndex_Type()
)
hmSecExternRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecExternRouteIndex.setStatus("mandatory")
_HmSecExternRouteNetwork_Type = DisplayString
_HmSecExternRouteNetwork_Object = MibTableColumn
hmSecExternRouteNetwork = _HmSecExternRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 6, 1, 2),
    _HmSecExternRouteNetwork_Type()
)
hmSecExternRouteNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternRouteNetwork.setStatus("mandatory")
_HmSecExternRouteGateway_Type = IpAddress
_HmSecExternRouteGateway_Object = MibTableColumn
hmSecExternRouteGateway = _HmSecExternRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 6, 1, 3),
    _HmSecExternRouteGateway_Type()
)
hmSecExternRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternRouteGateway.setStatus("mandatory")
_HmSecExternRouteRowStatus_Type = RowStatus
_HmSecExternRouteRowStatus_Object = MibTableColumn
hmSecExternRouteRowStatus = _HmSecExternRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 2, 6, 1, 4),
    _HmSecExternRouteRowStatus_Type()
)
hmSecExternRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecExternRouteRowStatus.setStatus("mandatory")
_HmSecRouterExternDevMTU_Type = Integer32
_HmSecRouterExternDevMTU_Object = MibScalar
hmSecRouterExternDevMTU = _HmSecRouterExternDevMTU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 6),
    _HmSecRouterExternDevMTU_Type()
)
hmSecRouterExternDevMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternDevMTU.setStatus("mandatory")


class _HmSecRouterExternUseVLAN_Type(Integer32):
    """Custom type hmSecRouterExternUseVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecRouterExternUseVLAN_Type.__name__ = "Integer32"
_HmSecRouterExternUseVLAN_Object = MibScalar
hmSecRouterExternUseVLAN = _HmSecRouterExternUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 7),
    _HmSecRouterExternUseVLAN_Type()
)
hmSecRouterExternUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternUseVLAN.setStatus("mandatory")
_HmSecRouterExternVlanId_Type = Integer32
_HmSecRouterExternVlanId_Object = MibScalar
hmSecRouterExternVlanId = _HmSecRouterExternVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 8),
    _HmSecRouterExternVlanId_Type()
)
hmSecRouterExternVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternVlanId.setStatus("mandatory")
_HmSecRouterExternDevVlanMTU_Type = Integer32
_HmSecRouterExternDevVlanMTU_Object = MibScalar
hmSecRouterExternDevVlanMTU = _HmSecRouterExternDevVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 2, 9),
    _HmSecRouterExternDevVlanMTU_Type()
)
hmSecRouterExternDevVlanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterExternDevVlanMTU.setStatus("mandatory")
_HmSecRouterHiDiscovery_ObjectIdentity = ObjectIdentity
hmSecRouterHiDiscovery = _HmSecRouterHiDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 3)
)


class _HmSecRouterHiDiscoveryIntern_Type(Integer32):
    """Custom type hmSecRouterHiDiscoveryIntern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-write", 1),
          ("read-only", 2),
          ("disabled", 3))
    )


_HmSecRouterHiDiscoveryIntern_Type.__name__ = "Integer32"
_HmSecRouterHiDiscoveryIntern_Object = MibScalar
hmSecRouterHiDiscoveryIntern = _HmSecRouterHiDiscoveryIntern_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 3, 1),
    _HmSecRouterHiDiscoveryIntern_Type()
)
hmSecRouterHiDiscoveryIntern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterHiDiscoveryIntern.setStatus("mandatory")


class _HmSecRouterHiDiscoveryExtern_Type(Integer32):
    """Custom type hmSecRouterHiDiscoveryExtern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-write", 1),
          ("read-only", 2),
          ("disabled", 3))
    )


_HmSecRouterHiDiscoveryExtern_Type.__name__ = "Integer32"
_HmSecRouterHiDiscoveryExtern_Object = MibScalar
hmSecRouterHiDiscoveryExtern = _HmSecRouterHiDiscoveryExtern_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 3, 3, 2),
    _HmSecRouterHiDiscoveryExtern_Type()
)
hmSecRouterHiDiscoveryExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterHiDiscoveryExtern.setStatus("mandatory")
_HmSecPPPOE_ObjectIdentity = ObjectIdentity
hmSecPPPOE = _HmSecPPPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4)
)
_HmSecPPPOELogin_Type = DisplayString
_HmSecPPPOELogin_Object = MibScalar
hmSecPPPOELogin = _HmSecPPPOELogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 1),
    _HmSecPPPOELogin_Type()
)
hmSecPPPOELogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOELogin.setStatus("mandatory")
_HmSecPPPOEPasswd_Type = DisplayString
_HmSecPPPOEPasswd_Object = MibScalar
hmSecPPPOEPasswd = _HmSecPPPOEPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 2),
    _HmSecPPPOEPasswd_Type()
)
hmSecPPPOEPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEPasswd.setStatus("mandatory")
_HmSecPPPOEMSS_Type = DisplayString
_HmSecPPPOEMSS_Object = MibScalar
hmSecPPPOEMSS = _HmSecPPPOEMSS_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 3),
    _HmSecPPPOEMSS_Type()
)
hmSecPPPOEMSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEMSS.setStatus("mandatory")
_HmSecPPPOEServiceName_Type = DisplayString
_HmSecPPPOEServiceName_Object = MibScalar
hmSecPPPOEServiceName = _HmSecPPPOEServiceName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 4),
    _HmSecPPPOEServiceName_Type()
)
hmSecPPPOEServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEServiceName.setStatus("obsolete")
_HmSecPPPOEAccessConcentName_Type = DisplayString
_HmSecPPPOEAccessConcentName_Object = MibScalar
hmSecPPPOEAccessConcentName = _HmSecPPPOEAccessConcentName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 5),
    _HmSecPPPOEAccessConcentName_Type()
)
hmSecPPPOEAccessConcentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEAccessConcentName.setStatus("obsolete")


class _HmSecPPPOEHostUnique_Type(Integer32):
    """Custom type hmSecPPPOEHostUnique based on Integer32"""
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


_HmSecPPPOEHostUnique_Type.__name__ = "Integer32"
_HmSecPPPOEHostUnique_Object = MibScalar
hmSecPPPOEHostUnique = _HmSecPPPOEHostUnique_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 6),
    _HmSecPPPOEHostUnique_Type()
)
hmSecPPPOEHostUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEHostUnique.setStatus("obsolete")
_HmSecPPPOEpppdOptionsTable_Object = MibTable
hmSecPPPOEpppdOptionsTable = _HmSecPPPOEpppdOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 7)
)
if mibBuilder.loadTexts:
    hmSecPPPOEpppdOptionsTable.setStatus("mandatory")
_HmSecPPPOEpppdOptionsEntry_Object = MibTableRow
hmSecPPPOEpppdOptionsEntry = _HmSecPPPOEpppdOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 7, 1)
)
hmSecPPPOEpppdOptionsEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecPPPOEpppdOptionsIndex"),
)
if mibBuilder.loadTexts:
    hmSecPPPOEpppdOptionsEntry.setStatus("mandatory")


class _HmSecPPPOEpppdOptionsIndex_Type(Integer32):
    """Custom type hmSecPPPOEpppdOptionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecPPPOEpppdOptionsIndex_Type.__name__ = "Integer32"
_HmSecPPPOEpppdOptionsIndex_Object = MibTableColumn
hmSecPPPOEpppdOptionsIndex = _HmSecPPPOEpppdOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 7, 1, 1),
    _HmSecPPPOEpppdOptionsIndex_Type()
)
hmSecPPPOEpppdOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecPPPOEpppdOptionsIndex.setStatus("mandatory")
_HmSecPPPOEpppdOptionsValue_Type = DisplayString
_HmSecPPPOEpppdOptionsValue_Object = MibTableColumn
hmSecPPPOEpppdOptionsValue = _HmSecPPPOEpppdOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 7, 1, 2),
    _HmSecPPPOEpppdOptionsValue_Type()
)
hmSecPPPOEpppdOptionsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEpppdOptionsValue.setStatus("mandatory")
_HmSecPPPOEpppdOptionsRowStatus_Type = RowStatus
_HmSecPPPOEpppdOptionsRowStatus_Object = MibTableColumn
hmSecPPPOEpppdOptionsRowStatus = _HmSecPPPOEpppdOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 4, 7, 1, 3),
    _HmSecPPPOEpppdOptionsRowStatus_Type()
)
hmSecPPPOEpppdOptionsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPPOEpppdOptionsRowStatus.setStatus("mandatory")
_HmSecDHCP_ObjectIdentity = ObjectIdentity
hmSecDHCP = _HmSecDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5)
)
_HmSecDHCPInt_ObjectIdentity = ObjectIdentity
hmSecDHCPInt = _HmSecDHCPInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1)
)


class _HmSecDHCPIntStart_Type(Integer32):
    """Custom type hmSecDHCPIntStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("enabled-relay", 3))
    )


_HmSecDHCPIntStart_Type.__name__ = "Integer32"
_HmSecDHCPIntStart_Object = MibScalar
hmSecDHCPIntStart = _HmSecDHCPIntStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 1),
    _HmSecDHCPIntStart_Type()
)
hmSecDHCPIntStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntStart.setStatus("mandatory")


class _HmSecDHCPIntPoolEnable_Type(Integer32):
    """Custom type hmSecDHCPIntPoolEnable based on Integer32"""
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


_HmSecDHCPIntPoolEnable_Type.__name__ = "Integer32"
_HmSecDHCPIntPoolEnable_Object = MibScalar
hmSecDHCPIntPoolEnable = _HmSecDHCPIntPoolEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 2),
    _HmSecDHCPIntPoolEnable_Type()
)
hmSecDHCPIntPoolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntPoolEnable.setStatus("mandatory")
_HmSecDHCPIntRangeStart_Type = IpAddress
_HmSecDHCPIntRangeStart_Object = MibScalar
hmSecDHCPIntRangeStart = _HmSecDHCPIntRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 3),
    _HmSecDHCPIntRangeStart_Type()
)
hmSecDHCPIntRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRangeStart.setStatus("mandatory")
_HmSecDHCPIntRangeEnd_Type = IpAddress
_HmSecDHCPIntRangeEnd_Object = MibScalar
hmSecDHCPIntRangeEnd = _HmSecDHCPIntRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 4),
    _HmSecDHCPIntRangeEnd_Type()
)
hmSecDHCPIntRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRangeEnd.setStatus("mandatory")
_HmSecDHCPIntNetmask_Type = IpAddress
_HmSecDHCPIntNetmask_Object = MibScalar
hmSecDHCPIntNetmask = _HmSecDHCPIntNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 5),
    _HmSecDHCPIntNetmask_Type()
)
hmSecDHCPIntNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntNetmask.setStatus("mandatory")
_HmSecDHCPIntGateway_Type = IpAddress
_HmSecDHCPIntGateway_Object = MibScalar
hmSecDHCPIntGateway = _HmSecDHCPIntGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 6),
    _HmSecDHCPIntGateway_Type()
)
hmSecDHCPIntGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntGateway.setStatus("mandatory")
_HmSecDHCPIntDnsServer_Type = IpAddress
_HmSecDHCPIntDnsServer_Object = MibScalar
hmSecDHCPIntDnsServer = _HmSecDHCPIntDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 7),
    _HmSecDHCPIntDnsServer_Type()
)
hmSecDHCPIntDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntDnsServer.setStatus("mandatory")
_HmSecDHCPIntStaticTable_Object = MibTable
hmSecDHCPIntStaticTable = _HmSecDHCPIntStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hmSecDHCPIntStaticTable.setStatus("mandatory")
_HmSecDHCPIntStaticEntry_Object = MibTableRow
hmSecDHCPIntStaticEntry = _HmSecDHCPIntStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 8, 1)
)
hmSecDHCPIntStaticEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecDHCPIntStaticIndex"),
)
if mibBuilder.loadTexts:
    hmSecDHCPIntStaticEntry.setStatus("mandatory")


class _HmSecDHCPIntStaticIndex_Type(Integer32):
    """Custom type hmSecDHCPIntStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecDHCPIntStaticIndex_Type.__name__ = "Integer32"
_HmSecDHCPIntStaticIndex_Object = MibTableColumn
hmSecDHCPIntStaticIndex = _HmSecDHCPIntStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 8, 1, 1),
    _HmSecDHCPIntStaticIndex_Type()
)
hmSecDHCPIntStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecDHCPIntStaticIndex.setStatus("mandatory")
_HmSecDHCPIntStaticMAC_Type = MacAddress
_HmSecDHCPIntStaticMAC_Object = MibTableColumn
hmSecDHCPIntStaticMAC = _HmSecDHCPIntStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 8, 1, 2),
    _HmSecDHCPIntStaticMAC_Type()
)
hmSecDHCPIntStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntStaticMAC.setStatus("mandatory")
_HmSecDHCPIntStaticIP_Type = IpAddress
_HmSecDHCPIntStaticIP_Object = MibTableColumn
hmSecDHCPIntStaticIP = _HmSecDHCPIntStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 8, 1, 3),
    _HmSecDHCPIntStaticIP_Type()
)
hmSecDHCPIntStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntStaticIP.setStatus("mandatory")
_HmSecDHCPIntStaticRowStatus_Type = RowStatus
_HmSecDHCPIntStaticRowStatus_Object = MibTableColumn
hmSecDHCPIntStaticRowStatus = _HmSecDHCPIntStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 8, 1, 4),
    _HmSecDHCPIntStaticRowStatus_Type()
)
hmSecDHCPIntStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntStaticRowStatus.setStatus("mandatory")
_HmSecDHCPIntBroadcast_Type = IpAddress
_HmSecDHCPIntBroadcast_Object = MibScalar
hmSecDHCPIntBroadcast = _HmSecDHCPIntBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 9),
    _HmSecDHCPIntBroadcast_Type()
)
hmSecDHCPIntBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntBroadcast.setStatus("mandatory")
_HmSecDHCPIntWINS_Type = IpAddress
_HmSecDHCPIntWINS_Object = MibScalar
hmSecDHCPIntWINS = _HmSecDHCPIntWINS_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 10),
    _HmSecDHCPIntWINS_Type()
)
hmSecDHCPIntWINS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntWINS.setStatus("mandatory")
_HmSecDHCPIntLeaseTime_Type = Integer32
_HmSecDHCPIntLeaseTime_Object = MibScalar
hmSecDHCPIntLeaseTime = _HmSecDHCPIntLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 11),
    _HmSecDHCPIntLeaseTime_Type()
)
hmSecDHCPIntLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntLeaseTime.setStatus("mandatory")
_HmSecDHCPIntRelayServerTable_Object = MibTable
hmSecDHCPIntRelayServerTable = _HmSecDHCPIntRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 50)
)
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayServerTable.setStatus("mandatory")
_HmSecDHCPIntRelayServerEntry_Object = MibTableRow
hmSecDHCPIntRelayServerEntry = _HmSecDHCPIntRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 50, 1)
)
hmSecDHCPIntRelayServerEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecDHCPIntRelayServerIndex"),
)
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayServerEntry.setStatus("mandatory")


class _HmSecDHCPIntRelayServerIndex_Type(Integer32):
    """Custom type hmSecDHCPIntRelayServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecDHCPIntRelayServerIndex_Type.__name__ = "Integer32"
_HmSecDHCPIntRelayServerIndex_Object = MibTableColumn
hmSecDHCPIntRelayServerIndex = _HmSecDHCPIntRelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 50, 1, 1),
    _HmSecDHCPIntRelayServerIndex_Type()
)
hmSecDHCPIntRelayServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayServerIndex.setStatus("mandatory")
_HmSecDHCPIntRelayServerIP_Type = IpAddress
_HmSecDHCPIntRelayServerIP_Object = MibTableColumn
hmSecDHCPIntRelayServerIP = _HmSecDHCPIntRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 50, 1, 2),
    _HmSecDHCPIntRelayServerIP_Type()
)
hmSecDHCPIntRelayServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayServerIP.setStatus("mandatory")
_HmSecDHCPIntRelayRowStatus_Type = RowStatus
_HmSecDHCPIntRelayRowStatus_Object = MibTableColumn
hmSecDHCPIntRelayRowStatus = _HmSecDHCPIntRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 50, 1, 10),
    _HmSecDHCPIntRelayRowStatus_Type()
)
hmSecDHCPIntRelayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayRowStatus.setStatus("mandatory")
_HmSecDHCPIntRelayMaxHop_Type = Integer32
_HmSecDHCPIntRelayMaxHop_Object = MibScalar
hmSecDHCPIntRelayMaxHop = _HmSecDHCPIntRelayMaxHop_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 51),
    _HmSecDHCPIntRelayMaxHop_Type()
)
hmSecDHCPIntRelayMaxHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayMaxHop.setStatus("mandatory")
_HmSecDHCPIntRelayAppend_Type = TruthValue
_HmSecDHCPIntRelayAppend_Object = MibScalar
hmSecDHCPIntRelayAppend = _HmSecDHCPIntRelayAppend_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 52),
    _HmSecDHCPIntRelayAppend_Type()
)
hmSecDHCPIntRelayAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayAppend.setStatus("mandatory")
_HmSecDHCPIntRelayAppendLimit_Type = Integer32
_HmSecDHCPIntRelayAppendLimit_Object = MibScalar
hmSecDHCPIntRelayAppendLimit = _HmSecDHCPIntRelayAppendLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 53),
    _HmSecDHCPIntRelayAppendLimit_Type()
)
hmSecDHCPIntRelayAppendLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayAppendLimit.setStatus("mandatory")


class _HmSecDHCPIntRelayCircuitInfo_Type(Integer32):
    """Custom type hmSecDHCPIntRelayCircuitInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("if-idx", 2),
          ("if-name", 3),
          ("if-mac", 4),
          ("if-ip", 5),
          ("sysname", 6),
          ("text", 7),
          ("if-prefixed-ip", 8),
          ("rs2", 9))
    )


_HmSecDHCPIntRelayCircuitInfo_Type.__name__ = "Integer32"
_HmSecDHCPIntRelayCircuitInfo_Object = MibScalar
hmSecDHCPIntRelayCircuitInfo = _HmSecDHCPIntRelayCircuitInfo_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 54),
    _HmSecDHCPIntRelayCircuitInfo_Type()
)
hmSecDHCPIntRelayCircuitInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayCircuitInfo.setStatus("mandatory")
_HmSecDHCPIntRelayCircuitText_Type = DisplayString
_HmSecDHCPIntRelayCircuitText_Object = MibScalar
hmSecDHCPIntRelayCircuitText = _HmSecDHCPIntRelayCircuitText_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 55),
    _HmSecDHCPIntRelayCircuitText_Type()
)
hmSecDHCPIntRelayCircuitText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayCircuitText.setStatus("mandatory")


class _HmSecDHCPIntRelayRemoteInfo_Type(Integer32):
    """Custom type hmSecDHCPIntRelayRemoteInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("if-idx", 2),
          ("if-name", 3),
          ("if-mac", 4),
          ("if-ip", 5),
          ("sysname", 6),
          ("text", 7),
          ("if-prefixed-ip", 8),
          ("rs2", 9))
    )


_HmSecDHCPIntRelayRemoteInfo_Type.__name__ = "Integer32"
_HmSecDHCPIntRelayRemoteInfo_Object = MibScalar
hmSecDHCPIntRelayRemoteInfo = _HmSecDHCPIntRelayRemoteInfo_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 56),
    _HmSecDHCPIntRelayRemoteInfo_Type()
)
hmSecDHCPIntRelayRemoteInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayRemoteInfo.setStatus("mandatory")
_HmSecDHCPIntRelayRemoteText_Type = DisplayString
_HmSecDHCPIntRelayRemoteText_Object = MibScalar
hmSecDHCPIntRelayRemoteText = _HmSecDHCPIntRelayRemoteText_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 1, 57),
    _HmSecDHCPIntRelayRemoteText_Type()
)
hmSecDHCPIntRelayRemoteText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPIntRelayRemoteText.setStatus("mandatory")
_HmSecDHCPExt_ObjectIdentity = ObjectIdentity
hmSecDHCPExt = _HmSecDHCPExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2)
)


class _HmSecDHCPExtStart_Type(Integer32):
    """Custom type hmSecDHCPExtStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("enabled-relay", 3))
    )


_HmSecDHCPExtStart_Type.__name__ = "Integer32"
_HmSecDHCPExtStart_Object = MibScalar
hmSecDHCPExtStart = _HmSecDHCPExtStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 1),
    _HmSecDHCPExtStart_Type()
)
hmSecDHCPExtStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtStart.setStatus("mandatory")


class _HmSecDHCPExtPoolEnable_Type(Integer32):
    """Custom type hmSecDHCPExtPoolEnable based on Integer32"""
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


_HmSecDHCPExtPoolEnable_Type.__name__ = "Integer32"
_HmSecDHCPExtPoolEnable_Object = MibScalar
hmSecDHCPExtPoolEnable = _HmSecDHCPExtPoolEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 2),
    _HmSecDHCPExtPoolEnable_Type()
)
hmSecDHCPExtPoolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtPoolEnable.setStatus("mandatory")
_HmSecDHCPExtRangeStart_Type = IpAddress
_HmSecDHCPExtRangeStart_Object = MibScalar
hmSecDHCPExtRangeStart = _HmSecDHCPExtRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 3),
    _HmSecDHCPExtRangeStart_Type()
)
hmSecDHCPExtRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRangeStart.setStatus("mandatory")
_HmSecDHCPExtRangeEnd_Type = IpAddress
_HmSecDHCPExtRangeEnd_Object = MibScalar
hmSecDHCPExtRangeEnd = _HmSecDHCPExtRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 4),
    _HmSecDHCPExtRangeEnd_Type()
)
hmSecDHCPExtRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRangeEnd.setStatus("mandatory")
_HmSecDHCPExtNetmask_Type = IpAddress
_HmSecDHCPExtNetmask_Object = MibScalar
hmSecDHCPExtNetmask = _HmSecDHCPExtNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 5),
    _HmSecDHCPExtNetmask_Type()
)
hmSecDHCPExtNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtNetmask.setStatus("mandatory")
_HmSecDHCPExtGateway_Type = IpAddress
_HmSecDHCPExtGateway_Object = MibScalar
hmSecDHCPExtGateway = _HmSecDHCPExtGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 6),
    _HmSecDHCPExtGateway_Type()
)
hmSecDHCPExtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtGateway.setStatus("mandatory")
_HmSecDHCPExtDnsServer_Type = IpAddress
_HmSecDHCPExtDnsServer_Object = MibScalar
hmSecDHCPExtDnsServer = _HmSecDHCPExtDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 7),
    _HmSecDHCPExtDnsServer_Type()
)
hmSecDHCPExtDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtDnsServer.setStatus("mandatory")
_HmSecDHCPExtStaticTable_Object = MibTable
hmSecDHCPExtStaticTable = _HmSecDHCPExtStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hmSecDHCPExtStaticTable.setStatus("mandatory")
_HmSecDHCPExtStaticEntry_Object = MibTableRow
hmSecDHCPExtStaticEntry = _HmSecDHCPExtStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 8, 1)
)
hmSecDHCPExtStaticEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecDHCPExtStaticIndex"),
)
if mibBuilder.loadTexts:
    hmSecDHCPExtStaticEntry.setStatus("mandatory")


class _HmSecDHCPExtStaticIndex_Type(Integer32):
    """Custom type hmSecDHCPExtStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecDHCPExtStaticIndex_Type.__name__ = "Integer32"
_HmSecDHCPExtStaticIndex_Object = MibTableColumn
hmSecDHCPExtStaticIndex = _HmSecDHCPExtStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 8, 1, 1),
    _HmSecDHCPExtStaticIndex_Type()
)
hmSecDHCPExtStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecDHCPExtStaticIndex.setStatus("mandatory")
_HmSecDHCPExtStaticMAC_Type = MacAddress
_HmSecDHCPExtStaticMAC_Object = MibTableColumn
hmSecDHCPExtStaticMAC = _HmSecDHCPExtStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 8, 1, 2),
    _HmSecDHCPExtStaticMAC_Type()
)
hmSecDHCPExtStaticMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtStaticMAC.setStatus("mandatory")
_HmSecDHCPExtStaticIP_Type = IpAddress
_HmSecDHCPExtStaticIP_Object = MibTableColumn
hmSecDHCPExtStaticIP = _HmSecDHCPExtStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 8, 1, 3),
    _HmSecDHCPExtStaticIP_Type()
)
hmSecDHCPExtStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtStaticIP.setStatus("mandatory")
_HmSecDHCPExtStaticRowStatus_Type = RowStatus
_HmSecDHCPExtStaticRowStatus_Object = MibTableColumn
hmSecDHCPExtStaticRowStatus = _HmSecDHCPExtStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 8, 1, 4),
    _HmSecDHCPExtStaticRowStatus_Type()
)
hmSecDHCPExtStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtStaticRowStatus.setStatus("mandatory")
_HmSecDHCPExtBroadcast_Type = IpAddress
_HmSecDHCPExtBroadcast_Object = MibScalar
hmSecDHCPExtBroadcast = _HmSecDHCPExtBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 9),
    _HmSecDHCPExtBroadcast_Type()
)
hmSecDHCPExtBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtBroadcast.setStatus("mandatory")
_HmSecDHCPExtWINS_Type = IpAddress
_HmSecDHCPExtWINS_Object = MibScalar
hmSecDHCPExtWINS = _HmSecDHCPExtWINS_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 10),
    _HmSecDHCPExtWINS_Type()
)
hmSecDHCPExtWINS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtWINS.setStatus("mandatory")
_HmSecDHCPExtLeaseTime_Type = Integer32
_HmSecDHCPExtLeaseTime_Object = MibScalar
hmSecDHCPExtLeaseTime = _HmSecDHCPExtLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 11),
    _HmSecDHCPExtLeaseTime_Type()
)
hmSecDHCPExtLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtLeaseTime.setStatus("mandatory")
_HmSecDHCPExtRelayServerTable_Object = MibTable
hmSecDHCPExtRelayServerTable = _HmSecDHCPExtRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 50)
)
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayServerTable.setStatus("mandatory")
_HmSecDHCPExtRelayServerEntry_Object = MibTableRow
hmSecDHCPExtRelayServerEntry = _HmSecDHCPExtRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 50, 1)
)
hmSecDHCPExtRelayServerEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecDHCPExtRelayServerIndex"),
)
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayServerEntry.setStatus("mandatory")


class _HmSecDHCPExtRelayServerIndex_Type(Integer32):
    """Custom type hmSecDHCPExtRelayServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecDHCPExtRelayServerIndex_Type.__name__ = "Integer32"
_HmSecDHCPExtRelayServerIndex_Object = MibTableColumn
hmSecDHCPExtRelayServerIndex = _HmSecDHCPExtRelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 50, 1, 1),
    _HmSecDHCPExtRelayServerIndex_Type()
)
hmSecDHCPExtRelayServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayServerIndex.setStatus("mandatory")
_HmSecDHCPExtRelayServerIP_Type = IpAddress
_HmSecDHCPExtRelayServerIP_Object = MibTableColumn
hmSecDHCPExtRelayServerIP = _HmSecDHCPExtRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 50, 1, 2),
    _HmSecDHCPExtRelayServerIP_Type()
)
hmSecDHCPExtRelayServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayServerIP.setStatus("mandatory")
_HmSecDHCPExtRelayRowStatus_Type = RowStatus
_HmSecDHCPExtRelayRowStatus_Object = MibTableColumn
hmSecDHCPExtRelayRowStatus = _HmSecDHCPExtRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 50, 1, 10),
    _HmSecDHCPExtRelayRowStatus_Type()
)
hmSecDHCPExtRelayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayRowStatus.setStatus("mandatory")
_HmSecDHCPExtRelayMaxHop_Type = Integer32
_HmSecDHCPExtRelayMaxHop_Object = MibScalar
hmSecDHCPExtRelayMaxHop = _HmSecDHCPExtRelayMaxHop_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 51),
    _HmSecDHCPExtRelayMaxHop_Type()
)
hmSecDHCPExtRelayMaxHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayMaxHop.setStatus("mandatory")
_HmSecDHCPExtRelayAppend_Type = TruthValue
_HmSecDHCPExtRelayAppend_Object = MibScalar
hmSecDHCPExtRelayAppend = _HmSecDHCPExtRelayAppend_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 52),
    _HmSecDHCPExtRelayAppend_Type()
)
hmSecDHCPExtRelayAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayAppend.setStatus("mandatory")
_HmSecDHCPExtRelayAppendLimit_Type = Integer32
_HmSecDHCPExtRelayAppendLimit_Object = MibScalar
hmSecDHCPExtRelayAppendLimit = _HmSecDHCPExtRelayAppendLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 53),
    _HmSecDHCPExtRelayAppendLimit_Type()
)
hmSecDHCPExtRelayAppendLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayAppendLimit.setStatus("mandatory")


class _HmSecDHCPExtRelayCircuitInfo_Type(Integer32):
    """Custom type hmSecDHCPExtRelayCircuitInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("if-idx", 2),
          ("if-name", 3),
          ("if-mac", 4),
          ("if-ip", 5),
          ("sysname", 6),
          ("text", 7),
          ("if-prefixed-ip", 8),
          ("rs2", 9))
    )


_HmSecDHCPExtRelayCircuitInfo_Type.__name__ = "Integer32"
_HmSecDHCPExtRelayCircuitInfo_Object = MibScalar
hmSecDHCPExtRelayCircuitInfo = _HmSecDHCPExtRelayCircuitInfo_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 54),
    _HmSecDHCPExtRelayCircuitInfo_Type()
)
hmSecDHCPExtRelayCircuitInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayCircuitInfo.setStatus("mandatory")
_HmSecDHCPExtRelayCircuitText_Type = DisplayString
_HmSecDHCPExtRelayCircuitText_Object = MibScalar
hmSecDHCPExtRelayCircuitText = _HmSecDHCPExtRelayCircuitText_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 55),
    _HmSecDHCPExtRelayCircuitText_Type()
)
hmSecDHCPExtRelayCircuitText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayCircuitText.setStatus("mandatory")


class _HmSecDHCPExtRelayRemoteInfo_Type(Integer32):
    """Custom type hmSecDHCPExtRelayRemoteInfo based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("if-idx", 2),
          ("if-name", 3),
          ("if-mac", 4),
          ("if-ip", 5),
          ("sysname", 6),
          ("text", 7),
          ("if-prefixed-ip", 8),
          ("rs2", 9))
    )


_HmSecDHCPExtRelayRemoteInfo_Type.__name__ = "Integer32"
_HmSecDHCPExtRelayRemoteInfo_Object = MibScalar
hmSecDHCPExtRelayRemoteInfo = _HmSecDHCPExtRelayRemoteInfo_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 56),
    _HmSecDHCPExtRelayRemoteInfo_Type()
)
hmSecDHCPExtRelayRemoteInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayRemoteInfo.setStatus("mandatory")
_HmSecDHCPExtRelayRemoteText_Type = DisplayString
_HmSecDHCPExtRelayRemoteText_Object = MibScalar
hmSecDHCPExtRelayRemoteText = _HmSecDHCPExtRelayRemoteText_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 5, 2, 57),
    _HmSecDHCPExtRelayRemoteText_Type()
)
hmSecDHCPExtRelayRemoteText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDHCPExtRelayRemoteText.setStatus("mandatory")
_HmSecDNS_ObjectIdentity = ObjectIdentity
hmSecDNS = _HmSecDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6)
)
_HmSecDNSSearchPath_Type = DisplayString
_HmSecDNSSearchPath_Object = MibScalar
hmSecDNSSearchPath = _HmSecDNSSearchPath_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 1),
    _HmSecDNSSearchPath_Type()
)
hmSecDNSSearchPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDNSSearchPath.setStatus("mandatory")


class _HmSecDNSServerType_Type(Integer32):
    """Custom type hmSecDNSServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("provider", 2),
          ("user", 3))
    )


_HmSecDNSServerType_Type.__name__ = "Integer32"
_HmSecDNSServerType_Object = MibScalar
hmSecDNSServerType = _HmSecDNSServerType_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 2),
    _HmSecDNSServerType_Type()
)
hmSecDNSServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDNSServerType.setStatus("mandatory")
_HmSecDNSUserDefinedServerTable_Object = MibTable
hmSecDNSUserDefinedServerTable = _HmSecDNSUserDefinedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 3)
)
if mibBuilder.loadTexts:
    hmSecDNSUserDefinedServerTable.setStatus("mandatory")
_HmSecDNSUserDefinedServerEntry_Object = MibTableRow
hmSecDNSUserDefinedServerEntry = _HmSecDNSUserDefinedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 3, 1)
)
hmSecDNSUserDefinedServerEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecdnsServerIndex"),
)
if mibBuilder.loadTexts:
    hmSecDNSUserDefinedServerEntry.setStatus("mandatory")


class _HmSecdnsServerIndex_Type(Integer32):
    """Custom type hmSecdnsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecdnsServerIndex_Type.__name__ = "Integer32"
_HmSecdnsServerIndex_Object = MibTableColumn
hmSecdnsServerIndex = _HmSecdnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 3, 1, 1),
    _HmSecdnsServerIndex_Type()
)
hmSecdnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecdnsServerIndex.setStatus("mandatory")
_HmSecdnsServerIP_Type = IpAddress
_HmSecdnsServerIP_Object = MibTableColumn
hmSecdnsServerIP = _HmSecdnsServerIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 3, 1, 2),
    _HmSecdnsServerIP_Type()
)
hmSecdnsServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecdnsServerIP.setStatus("mandatory")
_HmSecdnsServerRowStatus_Type = RowStatus
_HmSecdnsServerRowStatus_Object = MibTableColumn
hmSecdnsServerRowStatus = _HmSecdnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 3, 1, 3),
    _HmSecdnsServerRowStatus_Type()
)
hmSecdnsServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecdnsServerRowStatus.setStatus("mandatory")


class _HmSecDNSCacheEnabled_Type(Integer32):
    """Custom type hmSecDNSCacheEnabled based on Integer32"""
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


_HmSecDNSCacheEnabled_Type.__name__ = "Integer32"
_HmSecDNSCacheEnabled_Object = MibScalar
hmSecDNSCacheEnabled = _HmSecDNSCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 6, 4),
    _HmSecDNSCacheEnabled_Type()
)
hmSecDNSCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecDNSCacheEnabled.setStatus("mandatory")
_HmSecNetworkStatus_ObjectIdentity = ObjectIdentity
hmSecNetworkStatus = _HmSecNetworkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7)
)
_HmSecNetworkStatMode_Type = DisplayString
_HmSecNetworkStatMode_Object = MibScalar
hmSecNetworkStatMode = _HmSecNetworkStatMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 1),
    _HmSecNetworkStatMode_Type()
)
hmSecNetworkStatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatMode.setStatus("mandatory")
_HmSecNetworkStatExtIP_Type = DisplayString
_HmSecNetworkStatExtIP_Object = MibScalar
hmSecNetworkStatExtIP = _HmSecNetworkStatExtIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 2),
    _HmSecNetworkStatExtIP_Type()
)
hmSecNetworkStatExtIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatExtIP.setStatus("mandatory")
_HmSecNetworkStatGateway_Type = DisplayString
_HmSecNetworkStatGateway_Object = MibScalar
hmSecNetworkStatGateway = _HmSecNetworkStatGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 3),
    _HmSecNetworkStatGateway_Type()
)
hmSecNetworkStatGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatGateway.setStatus("mandatory")
_HmSecNetworkStatVPN_Type = DisplayString
_HmSecNetworkStatVPN_Object = MibScalar
hmSecNetworkStatVPN = _HmSecNetworkStatVPN_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 4),
    _HmSecNetworkStatVPN_Type()
)
hmSecNetworkStatVPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatVPN.setStatus("mandatory")
_HmSecNetworkStatDynIPReg_Type = DisplayString
_HmSecNetworkStatDynIPReg_Object = MibScalar
hmSecNetworkStatDynIPReg = _HmSecNetworkStatDynIPReg_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 5),
    _HmSecNetworkStatDynIPReg_Type()
)
hmSecNetworkStatDynIPReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatDynIPReg.setStatus("mandatory")
_HmSecNetworkStatHTTPSRemAccess_Type = DisplayString
_HmSecNetworkStatHTTPSRemAccess_Object = MibScalar
hmSecNetworkStatHTTPSRemAccess = _HmSecNetworkStatHTTPSRemAccess_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 6),
    _HmSecNetworkStatHTTPSRemAccess_Type()
)
hmSecNetworkStatHTTPSRemAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatHTTPSRemAccess.setStatus("mandatory")
_HmSecNetworkStatSSHRemoteAccess_Type = DisplayString
_HmSecNetworkStatSSHRemoteAccess_Object = MibScalar
hmSecNetworkStatSSHRemoteAccess = _HmSecNetworkStatSSHRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 7),
    _HmSecNetworkStatSSHRemoteAccess_Type()
)
hmSecNetworkStatSSHRemoteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatSSHRemoteAccess.setStatus("mandatory")
_HmSecNetworkSoftwareVersion_Type = DisplayString
_HmSecNetworkSoftwareVersion_Object = MibScalar
hmSecNetworkSoftwareVersion = _HmSecNetworkSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 8),
    _HmSecNetworkSoftwareVersion_Type()
)
hmSecNetworkSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkSoftwareVersion.setStatus("mandatory")
_HmSecNetworkStatUptime_Type = DisplayString
_HmSecNetworkStatUptime_Object = MibScalar
hmSecNetworkStatUptime = _HmSecNetworkStatUptime_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 9),
    _HmSecNetworkStatUptime_Type()
)
hmSecNetworkStatUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatUptime.setStatus("mandatory")
_HmSecNetworkStatLanguage_Type = DisplayString
_HmSecNetworkStatLanguage_Object = MibScalar
hmSecNetworkStatLanguage = _HmSecNetworkStatLanguage_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 7, 10),
    _HmSecNetworkStatLanguage_Type()
)
hmSecNetworkStatLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNetworkStatLanguage.setStatus("mandatory")
_HmSecHostname_Type = DisplayString
_HmSecHostname_Object = MibScalar
hmSecHostname = _HmSecHostname_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 8),
    _HmSecHostname_Type()
)
hmSecHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHostname.setStatus("mandatory")


class _HmSecHostnameMode_Type(Integer32):
    """Custom type hmSecHostnameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userDefined", 1),
          ("providerDefined", 2))
    )


_HmSecHostnameMode_Type.__name__ = "Integer32"
_HmSecHostnameMode_Object = MibScalar
hmSecHostnameMode = _HmSecHostnameMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 9),
    _HmSecHostnameMode_Type()
)
hmSecHostnameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHostnameMode.setStatus("mandatory")
_HmSecPPTP_ObjectIdentity = ObjectIdentity
hmSecPPTP = _HmSecPPTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10)
)
_HmSecPPTPLogin_Type = DisplayString
_HmSecPPTPLogin_Object = MibScalar
hmSecPPTPLogin = _HmSecPPTPLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 1),
    _HmSecPPTPLogin_Type()
)
hmSecPPTPLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPLogin.setStatus("mandatory")
_HmSecPPTPassword_Type = DisplayString
_HmSecPPTPassword_Object = MibScalar
hmSecPPTPassword = _HmSecPPTPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 2),
    _HmSecPPTPassword_Type()
)
hmSecPPTPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPassword.setStatus("mandatory")


class _HmSecPPTPLocalIPMode_Type(Integer32):
    """Custom type hmSecPPTPLocalIPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_HmSecPPTPLocalIPMode_Type.__name__ = "Integer32"
_HmSecPPTPLocalIPMode_Object = MibScalar
hmSecPPTPLocalIPMode = _HmSecPPTPLocalIPMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 3),
    _HmSecPPTPLocalIPMode_Type()
)
hmSecPPTPLocalIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPLocalIPMode.setStatus("mandatory")
_HmSecPPTPLocalIP_Type = IpAddress
_HmSecPPTPLocalIP_Object = MibScalar
hmSecPPTPLocalIP = _HmSecPPTPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 4),
    _HmSecPPTPLocalIP_Type()
)
hmSecPPTPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPLocalIP.setStatus("mandatory")
_HmSecPPTPModemIP_Type = IpAddress
_HmSecPPTPModemIP_Object = MibScalar
hmSecPPTPModemIP = _HmSecPPTPModemIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 5),
    _HmSecPPTPModemIP_Type()
)
hmSecPPTPModemIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPModemIP.setStatus("mandatory")
_HmSecPPTPpppdOptionsTable_Object = MibTable
hmSecPPTPpppdOptionsTable = _HmSecPPTPpppdOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 6)
)
if mibBuilder.loadTexts:
    hmSecPPTPpppdOptionsTable.setStatus("mandatory")
_HmSecPPTPpppdOptionsEntry_Object = MibTableRow
hmSecPPTPpppdOptionsEntry = _HmSecPPTPpppdOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 6, 1)
)
hmSecPPTPpppdOptionsEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecPPTPpppdOptionsIndex"),
)
if mibBuilder.loadTexts:
    hmSecPPTPpppdOptionsEntry.setStatus("mandatory")


class _HmSecPPTPpppdOptionsIndex_Type(Integer32):
    """Custom type hmSecPPTPpppdOptionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecPPTPpppdOptionsIndex_Type.__name__ = "Integer32"
_HmSecPPTPpppdOptionsIndex_Object = MibTableColumn
hmSecPPTPpppdOptionsIndex = _HmSecPPTPpppdOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 6, 1, 1),
    _HmSecPPTPpppdOptionsIndex_Type()
)
hmSecPPTPpppdOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecPPTPpppdOptionsIndex.setStatus("mandatory")
_HmSecPPTPpppdOptionsValue_Type = DisplayString
_HmSecPPTPpppdOptionsValue_Object = MibTableColumn
hmSecPPTPpppdOptionsValue = _HmSecPPTPpppdOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 6, 1, 2),
    _HmSecPPTPpppdOptionsValue_Type()
)
hmSecPPTPpppdOptionsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPpppdOptionsValue.setStatus("mandatory")
_HmSecPPTPpppdOptionsRowStatus_Type = RowStatus
_HmSecPPTPpppdOptionsRowStatus_Object = MibTableColumn
hmSecPPTPpppdOptionsRowStatus = _HmSecPPTPpppdOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 10, 6, 1, 3),
    _HmSecPPTPpppdOptionsRowStatus_Type()
)
hmSecPPTPpppdOptionsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecPPTPpppdOptionsRowStatus.setStatus("mandatory")
_HmSecSerial_ObjectIdentity = ObjectIdentity
hmSecSerial = _HmSecSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11)
)
_HmSecSerialBaud_Type = Integer32
_HmSecSerialBaud_Object = MibScalar
hmSecSerialBaud = _HmSecSerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 1),
    _HmSecSerialBaud_Type()
)
hmSecSerialBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialBaud.setStatus("mandatory")


class _HmSecSerialHWHandshakeEnable_Type(Integer32):
    """Custom type hmSecSerialHWHandshakeEnable based on Integer32"""
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


_HmSecSerialHWHandshakeEnable_Type.__name__ = "Integer32"
_HmSecSerialHWHandshakeEnable_Object = MibScalar
hmSecSerialHWHandshakeEnable = _HmSecSerialHWHandshakeEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 2),
    _HmSecSerialHWHandshakeEnable_Type()
)
hmSecSerialHWHandshakeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialHWHandshakeEnable.setStatus("mandatory")
_HmSecSerialPPP_ObjectIdentity = ObjectIdentity
hmSecSerialPPP = _HmSecSerialPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3)
)


class _HmSecSerialPPPEnable_Type(Integer32):
    """Custom type hmSecSerialPPPEnable based on Integer32"""
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


_HmSecSerialPPPEnable_Type.__name__ = "Integer32"
_HmSecSerialPPPEnable_Object = MibScalar
hmSecSerialPPPEnable = _HmSecSerialPPPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 1),
    _HmSecSerialPPPEnable_Type()
)
hmSecSerialPPPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPEnable.setStatus("mandatory")
_HmSecSerialPPPLogin_Type = DisplayString
_HmSecSerialPPPLogin_Object = MibScalar
hmSecSerialPPPLogin = _HmSecSerialPPPLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 2),
    _HmSecSerialPPPLogin_Type()
)
hmSecSerialPPPLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPLogin.setStatus("mandatory")
_HmSecSerialPPPPasswd_Type = DisplayString
_HmSecSerialPPPPasswd_Object = MibScalar
hmSecSerialPPPPasswd = _HmSecSerialPPPPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 3),
    _HmSecSerialPPPPasswd_Type()
)
hmSecSerialPPPPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPPasswd.setStatus("mandatory")
_HmSecSerialPPPLocalIP_Type = IpAddress
_HmSecSerialPPPLocalIP_Object = MibScalar
hmSecSerialPPPLocalIP = _HmSecSerialPPPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 4),
    _HmSecSerialPPPLocalIP_Type()
)
hmSecSerialPPPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPLocalIP.setStatus("mandatory")
_HmSecSerialPPPRemoteIP_Type = IpAddress
_HmSecSerialPPPRemoteIP_Object = MibScalar
hmSecSerialPPPRemoteIP = _HmSecSerialPPPRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 5),
    _HmSecSerialPPPRemoteIP_Type()
)
hmSecSerialPPPRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPRemoteIP.setStatus("mandatory")
_HmSecSerialPPPFWIN_ObjectIdentity = ObjectIdentity
hmSecSerialPPPFWIN = _HmSecSerialPPPFWIN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6)
)
_HmSecSerialPPPFWINTable_Object = MibTable
hmSecSerialPPPFWINTable = _HmSecSerialPPPFWINTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1)
)
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINTable.setStatus("mandatory")
_HmSecSerialPPPFWINEntry_Object = MibTableRow
hmSecSerialPPPFWINEntry = _HmSecSerialPPPFWINEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1)
)
hmSecSerialPPPFWINEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecFWINruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINEntry.setStatus("mandatory")


class _HmSecSerialPPPFWINruleIndex_Type(Integer32):
    """Custom type hmSecSerialPPPFWINruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecSerialPPPFWINruleIndex_Type.__name__ = "Integer32"
_HmSecSerialPPPFWINruleIndex_Object = MibTableColumn
hmSecSerialPPPFWINruleIndex = _HmSecSerialPPPFWINruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 1),
    _HmSecSerialPPPFWINruleIndex_Type()
)
hmSecSerialPPPFWINruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINruleIndex.setStatus("mandatory")
_HmSecSerialPPPFWINsourceIP_Type = DisplayString
_HmSecSerialPPPFWINsourceIP_Object = MibTableColumn
hmSecSerialPPPFWINsourceIP = _HmSecSerialPPPFWINsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 2),
    _HmSecSerialPPPFWINsourceIP_Type()
)
hmSecSerialPPPFWINsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINsourceIP.setStatus("mandatory")
_HmSecSerialPPPFWINdestinationIP_Type = DisplayString
_HmSecSerialPPPFWINdestinationIP_Object = MibTableColumn
hmSecSerialPPPFWINdestinationIP = _HmSecSerialPPPFWINdestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 3),
    _HmSecSerialPPPFWINdestinationIP_Type()
)
hmSecSerialPPPFWINdestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINdestinationIP.setStatus("mandatory")
_HmSecSerialPPPFWINsport_Type = DisplayString
_HmSecSerialPPPFWINsport_Object = MibTableColumn
hmSecSerialPPPFWINsport = _HmSecSerialPPPFWINsport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 4),
    _HmSecSerialPPPFWINsport_Type()
)
hmSecSerialPPPFWINsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINsport.setStatus("mandatory")
_HmSecSerialPPPFWINdport_Type = DisplayString
_HmSecSerialPPPFWINdport_Object = MibTableColumn
hmSecSerialPPPFWINdport = _HmSecSerialPPPFWINdport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 5),
    _HmSecSerialPPPFWINdport_Type()
)
hmSecSerialPPPFWINdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINdport.setStatus("mandatory")


class _HmSecSerialPPPFWINtarget_Type(Integer32):
    """Custom type hmSecSerialPPPFWINtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecSerialPPPFWINtarget_Type.__name__ = "Integer32"
_HmSecSerialPPPFWINtarget_Object = MibTableColumn
hmSecSerialPPPFWINtarget = _HmSecSerialPPPFWINtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 6),
    _HmSecSerialPPPFWINtarget_Type()
)
hmSecSerialPPPFWINtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINtarget.setStatus("mandatory")


class _HmSecSerialPPPFWINproto_Type(Integer32):
    """Custom type hmSecSerialPPPFWINproto based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("all", 4))
    )


_HmSecSerialPPPFWINproto_Type.__name__ = "Integer32"
_HmSecSerialPPPFWINproto_Object = MibTableColumn
hmSecSerialPPPFWINproto = _HmSecSerialPPPFWINproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 7),
    _HmSecSerialPPPFWINproto_Type()
)
hmSecSerialPPPFWINproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINproto.setStatus("mandatory")


class _HmSecSerialPPPFWINlog_Type(Integer32):
    """Custom type hmSecSerialPPPFWINlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSerialPPPFWINlog_Type.__name__ = "Integer32"
_HmSecSerialPPPFWINlog_Object = MibTableColumn
hmSecSerialPPPFWINlog = _HmSecSerialPPPFWINlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 8),
    _HmSecSerialPPPFWINlog_Type()
)
hmSecSerialPPPFWINlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINlog.setStatus("mandatory")
_HmSecSerialPPPFWINRowStatus_Type = RowStatus
_HmSecSerialPPPFWINRowStatus_Object = MibTableColumn
hmSecSerialPPPFWINRowStatus = _HmSecSerialPPPFWINRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 9),
    _HmSecSerialPPPFWINRowStatus_Type()
)
hmSecSerialPPPFWINRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINRowStatus.setStatus("mandatory")
_HmSecSerialPPPFWINcomment_Type = DisplayString
_HmSecSerialPPPFWINcomment_Object = MibTableColumn
hmSecSerialPPPFWINcomment = _HmSecSerialPPPFWINcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 1, 1, 10),
    _HmSecSerialPPPFWINcomment_Type()
)
hmSecSerialPPPFWINcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINcomment.setStatus("mandatory")


class _HmSecSerialPPPFWINLogDefault_Type(Integer32):
    """Custom type hmSecSerialPPPFWINLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSerialPPPFWINLogDefault_Type.__name__ = "Integer32"
_HmSecSerialPPPFWINLogDefault_Object = MibScalar
hmSecSerialPPPFWINLogDefault = _HmSecSerialPPPFWINLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 6, 2),
    _HmSecSerialPPPFWINLogDefault_Type()
)
hmSecSerialPPPFWINLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWINLogDefault.setStatus("mandatory")
_HmSecSerialPPPFWOUT_ObjectIdentity = ObjectIdentity
hmSecSerialPPPFWOUT = _HmSecSerialPPPFWOUT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7)
)
_HmSecSerialPPPFWOUTTable_Object = MibTable
hmSecSerialPPPFWOUTTable = _HmSecSerialPPPFWOUTTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1)
)
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTTable.setStatus("mandatory")
_HmSecSerialPPPFWOUTEntry_Object = MibTableRow
hmSecSerialPPPFWOUTEntry = _HmSecSerialPPPFWOUTEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1)
)
hmSecSerialPPPFWOUTEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecSerialPPPFWOUTruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTEntry.setStatus("mandatory")


class _HmSecSerialPPPFWOUTruleIndex_Type(Integer32):
    """Custom type hmSecSerialPPPFWOUTruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecSerialPPPFWOUTruleIndex_Type.__name__ = "Integer32"
_HmSecSerialPPPFWOUTruleIndex_Object = MibTableColumn
hmSecSerialPPPFWOUTruleIndex = _HmSecSerialPPPFWOUTruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 1),
    _HmSecSerialPPPFWOUTruleIndex_Type()
)
hmSecSerialPPPFWOUTruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTruleIndex.setStatus("mandatory")
_HmSecSerialPPPFWOUTsourceIP_Type = DisplayString
_HmSecSerialPPPFWOUTsourceIP_Object = MibTableColumn
hmSecSerialPPPFWOUTsourceIP = _HmSecSerialPPPFWOUTsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 2),
    _HmSecSerialPPPFWOUTsourceIP_Type()
)
hmSecSerialPPPFWOUTsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTsourceIP.setStatus("mandatory")
_HmSecSerialPPPFWOUTtargetIP_Type = DisplayString
_HmSecSerialPPPFWOUTtargetIP_Object = MibTableColumn
hmSecSerialPPPFWOUTtargetIP = _HmSecSerialPPPFWOUTtargetIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 3),
    _HmSecSerialPPPFWOUTtargetIP_Type()
)
hmSecSerialPPPFWOUTtargetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTtargetIP.setStatus("mandatory")
_HmSecSerialPPPFWOUTsport_Type = DisplayString
_HmSecSerialPPPFWOUTsport_Object = MibTableColumn
hmSecSerialPPPFWOUTsport = _HmSecSerialPPPFWOUTsport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 4),
    _HmSecSerialPPPFWOUTsport_Type()
)
hmSecSerialPPPFWOUTsport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTsport.setStatus("mandatory")
_HmSecSerialPPPFWOUTdport_Type = DisplayString
_HmSecSerialPPPFWOUTdport_Object = MibTableColumn
hmSecSerialPPPFWOUTdport = _HmSecSerialPPPFWOUTdport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 5),
    _HmSecSerialPPPFWOUTdport_Type()
)
hmSecSerialPPPFWOUTdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTdport.setStatus("mandatory")


class _HmSecSerialPPPFWOUTtarget_Type(Integer32):
    """Custom type hmSecSerialPPPFWOUTtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecSerialPPPFWOUTtarget_Type.__name__ = "Integer32"
_HmSecSerialPPPFWOUTtarget_Object = MibTableColumn
hmSecSerialPPPFWOUTtarget = _HmSecSerialPPPFWOUTtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 6),
    _HmSecSerialPPPFWOUTtarget_Type()
)
hmSecSerialPPPFWOUTtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTtarget.setStatus("mandatory")


class _HmSecSerialPPPFWOUTproto_Type(Integer32):
    """Custom type hmSecSerialPPPFWOUTproto based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("all", 4))
    )


_HmSecSerialPPPFWOUTproto_Type.__name__ = "Integer32"
_HmSecSerialPPPFWOUTproto_Object = MibTableColumn
hmSecSerialPPPFWOUTproto = _HmSecSerialPPPFWOUTproto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 7),
    _HmSecSerialPPPFWOUTproto_Type()
)
hmSecSerialPPPFWOUTproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTproto.setStatus("mandatory")


class _HmSecSerialPPPFWOUTlog_Type(Integer32):
    """Custom type hmSecSerialPPPFWOUTlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSerialPPPFWOUTlog_Type.__name__ = "Integer32"
_HmSecSerialPPPFWOUTlog_Object = MibTableColumn
hmSecSerialPPPFWOUTlog = _HmSecSerialPPPFWOUTlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 8),
    _HmSecSerialPPPFWOUTlog_Type()
)
hmSecSerialPPPFWOUTlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTlog.setStatus("mandatory")
_HmSecSerialPPPFWOUTRowStatus_Type = RowStatus
_HmSecSerialPPPFWOUTRowStatus_Object = MibTableColumn
hmSecSerialPPPFWOUTRowStatus = _HmSecSerialPPPFWOUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 9),
    _HmSecSerialPPPFWOUTRowStatus_Type()
)
hmSecSerialPPPFWOUTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTRowStatus.setStatus("mandatory")
_HmSecSerialPPPFWOUTcomment_Type = DisplayString
_HmSecSerialPPPFWOUTcomment_Object = MibTableColumn
hmSecSerialPPPFWOUTcomment = _HmSecSerialPPPFWOUTcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 1, 1, 10),
    _HmSecSerialPPPFWOUTcomment_Type()
)
hmSecSerialPPPFWOUTcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTcomment.setStatus("mandatory")


class _HmSecSerialPPPFWOUTLogDefault_Type(Integer32):
    """Custom type hmSecSerialPPPFWOUTLogDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSerialPPPFWOUTLogDefault_Type.__name__ = "Integer32"
_HmSecSerialPPPFWOUTLogDefault_Object = MibScalar
hmSecSerialPPPFWOUTLogDefault = _HmSecSerialPPPFWOUTLogDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 11, 3, 7, 2),
    _HmSecSerialPPPFWOUTLogDefault_Type()
)
hmSecSerialPPPFWOUTLogDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSerialPPPFWOUTLogDefault.setStatus("mandatory")
_HmSecArpTimeout_Type = Integer32
_HmSecArpTimeout_Object = MibScalar
hmSecArpTimeout = _HmSecArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 3, 12),
    _HmSecArpTimeout_Type()
)
hmSecArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecArpTimeout.setStatus("mandatory")
_HmSecSystem_ObjectIdentity = ObjectIdentity
hmSecSystem = _HmSecSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 4)
)
_HmSecPasswords_ObjectIdentity = ObjectIdentity
hmSecPasswords = _HmSecPasswords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 1)
)
_HmSecRootPassword_Type = DisplayString
_HmSecRootPassword_Object = MibScalar
hmSecRootPassword = _HmSecRootPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 1, 1),
    _HmSecRootPassword_Type()
)
hmSecRootPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRootPassword.setStatus("mandatory")
_HmSecAdminPassword_Type = DisplayString
_HmSecAdminPassword_Object = MibScalar
hmSecAdminPassword = _HmSecAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 1, 2),
    _HmSecAdminPassword_Type()
)
hmSecAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecAdminPassword.setStatus("mandatory")
_HmSecUserPassword_Type = DisplayString
_HmSecUserPassword_Object = MibScalar
hmSecUserPassword = _HmSecUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 1, 3),
    _HmSecUserPassword_Type()
)
hmSecUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUserPassword.setStatus("mandatory")
_HmSecUserPwdEnable_Type = TruthValue
_HmSecUserPwdEnable_Object = MibScalar
hmSecUserPwdEnable = _HmSecUserPwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 1, 4),
    _HmSecUserPwdEnable_Type()
)
hmSecUserPwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUserPwdEnable.setStatus("mandatory")
_HmSecHTTPSRemoteAccess_ObjectIdentity = ObjectIdentity
hmSecHTTPSRemoteAccess = _HmSecHTTPSRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2)
)
_HmSecHTTPSRemoteEnable_Type = TruthValue
_HmSecHTTPSRemoteEnable_Object = MibScalar
hmSecHTTPSRemoteEnable = _HmSecHTTPSRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 1),
    _HmSecHTTPSRemoteEnable_Type()
)
hmSecHTTPSRemoteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSRemoteEnable.setStatus("mandatory")
_HmSecHTTPSRemotePort_Type = DisplayString
_HmSecHTTPSRemotePort_Object = MibScalar
hmSecHTTPSRemotePort = _HmSecHTTPSRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 2),
    _HmSecHTTPSRemotePort_Type()
)
hmSecHTTPSRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSRemotePort.setStatus("mandatory")
_HmSecHTTPSRemoteFWRuleTable_Object = MibTable
hmSecHTTPSRemoteFWRuleTable = _HmSecHTTPSRemoteFWRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hmSecHTTPSRemoteFWRuleTable.setStatus("mandatory")
_HmSecHTTPSRemoteFWRuleEntry_Object = MibTableRow
hmSecHTTPSRemoteFWRuleEntry = _HmSecHTTPSRemoteFWRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1)
)
hmSecHTTPSRemoteFWRuleEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecHTTPSFWruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecHTTPSRemoteFWRuleEntry.setStatus("mandatory")


class _HmSecHTTPSFWruleIndex_Type(Integer32):
    """Custom type hmSecHTTPSFWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecHTTPSFWruleIndex_Type.__name__ = "Integer32"
_HmSecHTTPSFWruleIndex_Object = MibTableColumn
hmSecHTTPSFWruleIndex = _HmSecHTTPSFWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 1),
    _HmSecHTTPSFWruleIndex_Type()
)
hmSecHTTPSFWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecHTTPSFWruleIndex.setStatus("mandatory")
_HmSecHTTPSFWsourceIP_Type = DisplayString
_HmSecHTTPSFWsourceIP_Object = MibTableColumn
hmSecHTTPSFWsourceIP = _HmSecHTTPSFWsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 2),
    _HmSecHTTPSFWsourceIP_Type()
)
hmSecHTTPSFWsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSFWsourceIP.setStatus("mandatory")


class _HmSecHTTPSFWinterface_Type(Integer32):
    """Custom type hmSecHTTPSFWinterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("intern", 2))
    )


_HmSecHTTPSFWinterface_Type.__name__ = "Integer32"
_HmSecHTTPSFWinterface_Object = MibTableColumn
hmSecHTTPSFWinterface = _HmSecHTTPSFWinterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 3),
    _HmSecHTTPSFWinterface_Type()
)
hmSecHTTPSFWinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSFWinterface.setStatus("mandatory")


class _HmSecHTTPSFWtarget_Type(Integer32):
    """Custom type hmSecHTTPSFWtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecHTTPSFWtarget_Type.__name__ = "Integer32"
_HmSecHTTPSFWtarget_Object = MibTableColumn
hmSecHTTPSFWtarget = _HmSecHTTPSFWtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 4),
    _HmSecHTTPSFWtarget_Type()
)
hmSecHTTPSFWtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSFWtarget.setStatus("mandatory")


class _HmSecHTTPSFWlog_Type(Integer32):
    """Custom type hmSecHTTPSFWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecHTTPSFWlog_Type.__name__ = "Integer32"
_HmSecHTTPSFWlog_Object = MibTableColumn
hmSecHTTPSFWlog = _HmSecHTTPSFWlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 5),
    _HmSecHTTPSFWlog_Type()
)
hmSecHTTPSFWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSFWlog.setStatus("mandatory")
_HmSecHTTPSFWRowStatus_Type = RowStatus
_HmSecHTTPSFWRowStatus_Object = MibTableColumn
hmSecHTTPSFWRowStatus = _HmSecHTTPSFWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 6),
    _HmSecHTTPSFWRowStatus_Type()
)
hmSecHTTPSFWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSFWRowStatus.setStatus("mandatory")
_HmSecHTTPSFWcomment_Type = DisplayString
_HmSecHTTPSFWcomment_Object = MibTableColumn
hmSecHTTPSFWcomment = _HmSecHTTPSFWcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 2, 3, 1, 7),
    _HmSecHTTPSFWcomment_Type()
)
hmSecHTTPSFWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecHTTPSFWcomment.setStatus("mandatory")
_HmSecSSHRemoteAccess_ObjectIdentity = ObjectIdentity
hmSecSSHRemoteAccess = _HmSecSSHRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3)
)
_HmSecSSHRemoteEnable_Type = TruthValue
_HmSecSSHRemoteEnable_Object = MibScalar
hmSecSSHRemoteEnable = _HmSecSSHRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 1),
    _HmSecSSHRemoteEnable_Type()
)
hmSecSSHRemoteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHRemoteEnable.setStatus("mandatory")
_HmSecSSHRemotePort_Type = DisplayString
_HmSecSSHRemotePort_Object = MibScalar
hmSecSSHRemotePort = _HmSecSSHRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 2),
    _HmSecSSHRemotePort_Type()
)
hmSecSSHRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHRemotePort.setStatus("mandatory")
_HmSecSSHRemoteFWRuleTable_Object = MibTable
hmSecSSHRemoteFWRuleTable = _HmSecSSHRemoteFWRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hmSecSSHRemoteFWRuleTable.setStatus("mandatory")
_HmSecSSHRemoteFWRuleEntry_Object = MibTableRow
hmSecSSHRemoteFWRuleEntry = _HmSecSSHRemoteFWRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1)
)
hmSecSSHRemoteFWRuleEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecSSHFWruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecSSHRemoteFWRuleEntry.setStatus("mandatory")


class _HmSecSSHFWruleIndex_Type(Integer32):
    """Custom type hmSecSSHFWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecSSHFWruleIndex_Type.__name__ = "Integer32"
_HmSecSSHFWruleIndex_Object = MibTableColumn
hmSecSSHFWruleIndex = _HmSecSSHFWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 1),
    _HmSecSSHFWruleIndex_Type()
)
hmSecSSHFWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecSSHFWruleIndex.setStatus("mandatory")
_HmSecSSHFWsourceIP_Type = DisplayString
_HmSecSSHFWsourceIP_Object = MibTableColumn
hmSecSSHFWsourceIP = _HmSecSSHFWsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 2),
    _HmSecSSHFWsourceIP_Type()
)
hmSecSSHFWsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHFWsourceIP.setStatus("mandatory")


class _HmSecSSHFWinterface_Type(Integer32):
    """Custom type hmSecSSHFWinterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("intern", 2))
    )


_HmSecSSHFWinterface_Type.__name__ = "Integer32"
_HmSecSSHFWinterface_Object = MibTableColumn
hmSecSSHFWinterface = _HmSecSSHFWinterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 3),
    _HmSecSSHFWinterface_Type()
)
hmSecSSHFWinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHFWinterface.setStatus("mandatory")


class _HmSecSSHFWtarget_Type(Integer32):
    """Custom type hmSecSSHFWtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecSSHFWtarget_Type.__name__ = "Integer32"
_HmSecSSHFWtarget_Object = MibTableColumn
hmSecSSHFWtarget = _HmSecSSHFWtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 4),
    _HmSecSSHFWtarget_Type()
)
hmSecSSHFWtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHFWtarget.setStatus("mandatory")


class _HmSecSSHFWlog_Type(Integer32):
    """Custom type hmSecSSHFWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSSHFWlog_Type.__name__ = "Integer32"
_HmSecSSHFWlog_Object = MibTableColumn
hmSecSSHFWlog = _HmSecSSHFWlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 5),
    _HmSecSSHFWlog_Type()
)
hmSecSSHFWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHFWlog.setStatus("mandatory")
_HmSecSSHFWRowStatus_Type = RowStatus
_HmSecSSHFWRowStatus_Object = MibTableColumn
hmSecSSHFWRowStatus = _HmSecSSHFWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 6),
    _HmSecSSHFWRowStatus_Type()
)
hmSecSSHFWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHFWRowStatus.setStatus("mandatory")
_HmSecSSHFWcomment_Type = DisplayString
_HmSecSSHFWcomment_Object = MibTableColumn
hmSecSSHFWcomment = _HmSecSSHFWcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 3, 3, 1, 7),
    _HmSecSSHFWcomment_Type()
)
hmSecSSHFWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSSHFWcomment.setStatus("mandatory")


class _HmSecLanguage_Type(Integer32):
    """Custom type hmSecLanguage based on Integer32"""
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
        *(("automatic", 1),
          ("englisch", 2),
          ("german", 3),
          ("japanese", 4))
    )


_HmSecLanguage_Type.__name__ = "Integer32"
_HmSecLanguage_Object = MibScalar
hmSecLanguage = _HmSecLanguage_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 4),
    _HmSecLanguage_Type()
)
hmSecLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLanguage.setStatus("mandatory")
_HmSecHardwareInformation_ObjectIdentity = ObjectIdentity
hmSecHardwareInformation = _HmSecHardwareInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5)
)
_HmSecHardware_Type = DisplayString
_HmSecHardware_Object = MibScalar
hmSecHardware = _HmSecHardware_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 1),
    _HmSecHardware_Type()
)
hmSecHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecHardware.setStatus("mandatory")
_HmSecCPU_Type = DisplayString
_HmSecCPU_Object = MibScalar
hmSecCPU = _HmSecCPU_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 2),
    _HmSecCPU_Type()
)
hmSecCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecCPU.setStatus("mandatory")
_HmSecCPUFamily_Type = DisplayString
_HmSecCPUFamily_Object = MibScalar
hmSecCPUFamily = _HmSecCPUFamily_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 3),
    _HmSecCPUFamily_Type()
)
hmSecCPUFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecCPUFamily.setStatus("mandatory")
_HmSecCPUStepping_Type = DisplayString
_HmSecCPUStepping_Object = MibScalar
hmSecCPUStepping = _HmSecCPUStepping_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 4),
    _HmSecCPUStepping_Type()
)
hmSecCPUStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecCPUStepping.setStatus("mandatory")
_HmSecCPUSpeed_Type = DisplayString
_HmSecCPUSpeed_Object = MibScalar
hmSecCPUSpeed = _HmSecCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 5),
    _HmSecCPUSpeed_Type()
)
hmSecCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecCPUSpeed.setStatus("mandatory")
_HmSecSystemTemperature_Type = DisplayString
_HmSecSystemTemperature_Object = MibScalar
hmSecSystemTemperature = _HmSecSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 6),
    _HmSecSystemTemperature_Type()
)
hmSecSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecSystemTemperature.setStatus("mandatory")
_HmSecUptime_Type = DisplayString
_HmSecUptime_Object = MibScalar
hmSecUptime = _HmSecUptime_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 7),
    _HmSecUptime_Type()
)
hmSecUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecUptime.setStatus("mandatory")
_HmSecUSMem_Type = DisplayString
_HmSecUSMem_Object = MibScalar
hmSecUSMem = _HmSecUSMem_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 8),
    _HmSecUSMem_Type()
)
hmSecUSMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecUSMem.setStatus("mandatory")
_HmSecMAC1_Type = DisplayString
_HmSecMAC1_Object = MibScalar
hmSecMAC1 = _HmSecMAC1_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 9),
    _HmSecMAC1_Type()
)
hmSecMAC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecMAC1.setStatus("mandatory")
_HmSecMAC2_Type = DisplayString
_HmSecMAC2_Object = MibScalar
hmSecMAC2 = _HmSecMAC2_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 10),
    _HmSecMAC2_Type()
)
hmSecMAC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecMAC2.setStatus("mandatory")
_HmSecMAC3_Type = DisplayString
_HmSecMAC3_Object = MibScalar
hmSecMAC3 = _HmSecMAC3_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 11),
    _HmSecMAC3_Type()
)
hmSecMAC3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecMAC3.setStatus("mandatory")
_HmSecSerialNumber_Type = DisplayString
_HmSecSerialNumber_Object = MibScalar
hmSecSerialNumber = _HmSecSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 12),
    _HmSecSerialNumber_Type()
)
hmSecSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecSerialNumber.setStatus("mandatory")
_HmSecVerParSet_Type = DisplayString
_HmSecVerParSet_Object = MibScalar
hmSecVerParSet = _HmSecVerParSet_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 13),
    _HmSecVerParSet_Type()
)
hmSecVerParSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecVerParSet.setStatus("mandatory")
_HmSecProductName_Type = DisplayString
_HmSecProductName_Object = MibScalar
hmSecProductName = _HmSecProductName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 14),
    _HmSecProductName_Type()
)
hmSecProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecProductName.setStatus("mandatory")
_HmSecOEMName_Type = DisplayString
_HmSecOEMName_Object = MibScalar
hmSecOEMName = _HmSecOEMName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 15),
    _HmSecOEMName_Type()
)
hmSecOEMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecOEMName.setStatus("mandatory")
_HmSecOEMSerial_Type = DisplayString
_HmSecOEMSerial_Object = MibScalar
hmSecOEMSerial = _HmSecOEMSerial_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 16),
    _HmSecOEMSerial_Type()
)
hmSecOEMSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecOEMSerial.setStatus("mandatory")
_HmSecManufacturer_Type = DisplayString
_HmSecManufacturer_Object = MibScalar
hmSecManufacturer = _HmSecManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 17),
    _HmSecManufacturer_Type()
)
hmSecManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecManufacturer.setStatus("mandatory")
_HmSecManuDate_Type = DisplayString
_HmSecManuDate_Object = MibScalar
hmSecManuDate = _HmSecManuDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 18),
    _HmSecManuDate_Type()
)
hmSecManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecManuDate.setStatus("mandatory")
_HmSecBootLoader_Type = DisplayString
_HmSecBootLoader_Object = MibScalar
hmSecBootLoader = _HmSecBootLoader_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 19),
    _HmSecBootLoader_Type()
)
hmSecBootLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBootLoader.setStatus("mandatory")
_HmSecHardwareVersion_Type = DisplayString
_HmSecHardwareVersion_Object = MibScalar
hmSecHardwareVersion = _HmSecHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 20),
    _HmSecHardwareVersion_Type()
)
hmSecHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecHardwareVersion.setStatus("mandatory")
_HmSecRescueSystem_Type = DisplayString
_HmSecRescueSystem_Object = MibScalar
hmSecRescueSystem = _HmSecRescueSystem_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 21),
    _HmSecRescueSystem_Type()
)
hmSecRescueSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecRescueSystem.setStatus("mandatory")
_HmSecProdSoft_Type = DisplayString
_HmSecProdSoft_Object = MibScalar
hmSecProdSoft = _HmSecProdSoft_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 5, 22),
    _HmSecProdSoft_Type()
)
hmSecProdSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecProdSoft.setStatus("mandatory")
_HmSecVersions_ObjectIdentity = ObjectIdentity
hmSecVersions = _HmSecVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7)
)
_HmSecVersion_Type = DisplayString
_HmSecVersion_Object = MibScalar
hmSecVersion = _HmSecVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 1),
    _HmSecVersion_Type()
)
hmSecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecVersion.setStatus("mandatory")
_HmSecBaseVersion_Type = DisplayString
_HmSecBaseVersion_Object = MibScalar
hmSecBaseVersion = _HmSecBaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 2),
    _HmSecBaseVersion_Type()
)
hmSecBaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBaseVersion.setStatus("mandatory")
_HmSecUpdates_Type = DisplayString
_HmSecUpdates_Object = MibScalar
hmSecUpdates = _HmSecUpdates_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 3),
    _HmSecUpdates_Type()
)
hmSecUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecUpdates.setStatus("mandatory")
_HmSecPackageVersionTable_Object = MibTable
hmSecPackageVersionTable = _HmSecPackageVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4)
)
if mibBuilder.loadTexts:
    hmSecPackageVersionTable.setStatus("mandatory")
_HmSecPackageVersionEntry_Object = MibTableRow
hmSecPackageVersionEntry = _HmSecPackageVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4, 1)
)
hmSecPackageVersionEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecPkgIndex"),
)
if mibBuilder.loadTexts:
    hmSecPackageVersionEntry.setStatus("mandatory")


class _HmSecPkgIndex_Type(Integer32):
    """Custom type hmSecPkgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HmSecPkgIndex_Type.__name__ = "Integer32"
_HmSecPkgIndex_Object = MibTableColumn
hmSecPkgIndex = _HmSecPkgIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4, 1, 1),
    _HmSecPkgIndex_Type()
)
hmSecPkgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecPkgIndex.setStatus("mandatory")
_HmSecPkgName_Type = DisplayString
_HmSecPkgName_Object = MibTableColumn
hmSecPkgName = _HmSecPkgName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4, 1, 2),
    _HmSecPkgName_Type()
)
hmSecPkgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPkgName.setStatus("mandatory")
_HmSecPkgVerNum_Type = DisplayString
_HmSecPkgVerNum_Object = MibTableColumn
hmSecPkgVerNum = _HmSecPkgVerNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4, 1, 3),
    _HmSecPkgVerNum_Type()
)
hmSecPkgVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPkgVerNum.setStatus("mandatory")
_HmSecPkgVerVersion_Type = DisplayString
_HmSecPkgVerVersion_Object = MibTableColumn
hmSecPkgVerVersion = _HmSecPkgVerVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4, 1, 4),
    _HmSecPkgVerVersion_Type()
)
hmSecPkgVerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPkgVerVersion.setStatus("mandatory")
_HmSecPkgVerFlavour_Type = DisplayString
_HmSecPkgVerFlavour_Object = MibTableColumn
hmSecPkgVerFlavour = _HmSecPkgVerFlavour_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 7, 4, 1, 5),
    _HmSecPkgVerFlavour_Type()
)
hmSecPkgVerFlavour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPkgVerFlavour.setStatus("mandatory")


class _HmSecAction_Type(Integer32):
    """Custom type hmSecAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_HmSecAction_Type.__name__ = "Integer32"
_HmSecAction_Object = MibScalar
hmSecAction = _HmSecAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 4, 8),
    _HmSecAction_Type()
)
hmSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecAction.setStatus("mandatory")
_HmSecSNMP_ObjectIdentity = ObjectIdentity
hmSecSNMP = _HmSecSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 5)
)


class _HmSecSNMPenableV3_Type(Integer32):
    """Custom type hmSecSNMPenableV3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSNMPenableV3_Type.__name__ = "Integer32"
_HmSecSNMPenableV3_Object = MibScalar
hmSecSNMPenableV3 = _HmSecSNMPenableV3_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 1),
    _HmSecSNMPenableV3_Type()
)
hmSecSNMPenableV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPenableV3.setStatus("mandatory")


class _HmSecSNMPenableV1_Type(Integer32):
    """Custom type hmSecSNMPenableV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSNMPenableV1_Type.__name__ = "Integer32"
_HmSecSNMPenableV1_Object = MibScalar
hmSecSNMPenableV1 = _HmSecSNMPenableV1_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 2),
    _HmSecSNMPenableV1_Type()
)
hmSecSNMPenableV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPenableV1.setStatus("mandatory")
_HmSecSNMPport_Type = DisplayString
_HmSecSNMPport_Object = MibScalar
hmSecSNMPport = _HmSecSNMPport_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 3),
    _HmSecSNMPport_Type()
)
hmSecSNMPport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPport.setStatus("mandatory")
_HmSecSNMPv1ROCommunity_Type = DisplayString
_HmSecSNMPv1ROCommunity_Object = MibScalar
hmSecSNMPv1ROCommunity = _HmSecSNMPv1ROCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 4),
    _HmSecSNMPv1ROCommunity_Type()
)
hmSecSNMPv1ROCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPv1ROCommunity.setStatus("mandatory")
_HmSecSNMPv1RWCommunity_Type = DisplayString
_HmSecSNMPv1RWCommunity_Object = MibScalar
hmSecSNMPv1RWCommunity = _HmSecSNMPv1RWCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 5),
    _HmSecSNMPv1RWCommunity_Type()
)
hmSecSNMPv1RWCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPv1RWCommunity.setStatus("mandatory")
_HmSecSNMPFWRuleTable_Object = MibTable
hmSecSNMPFWRuleTable = _HmSecSNMPFWRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6)
)
if mibBuilder.loadTexts:
    hmSecSNMPFWRuleTable.setStatus("mandatory")
_HmSecSNMPFWRuleEntry_Object = MibTableRow
hmSecSNMPFWRuleEntry = _HmSecSNMPFWRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1)
)
hmSecSNMPFWRuleEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecSNMPFWruleIndex"),
)
if mibBuilder.loadTexts:
    hmSecSNMPFWRuleEntry.setStatus("mandatory")


class _HmSecSNMPFWruleIndex_Type(Integer32):
    """Custom type hmSecSNMPFWruleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecSNMPFWruleIndex_Type.__name__ = "Integer32"
_HmSecSNMPFWruleIndex_Object = MibTableColumn
hmSecSNMPFWruleIndex = _HmSecSNMPFWruleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 1),
    _HmSecSNMPFWruleIndex_Type()
)
hmSecSNMPFWruleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecSNMPFWruleIndex.setStatus("mandatory")
_HmSecSNMPFWsourceIP_Type = DisplayString
_HmSecSNMPFWsourceIP_Object = MibTableColumn
hmSecSNMPFWsourceIP = _HmSecSNMPFWsourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 2),
    _HmSecSNMPFWsourceIP_Type()
)
hmSecSNMPFWsourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPFWsourceIP.setStatus("mandatory")


class _HmSecSNMPFWinterface_Type(Integer32):
    """Custom type hmSecSNMPFWinterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 1),
          ("intern", 2))
    )


_HmSecSNMPFWinterface_Type.__name__ = "Integer32"
_HmSecSNMPFWinterface_Object = MibTableColumn
hmSecSNMPFWinterface = _HmSecSNMPFWinterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 3),
    _HmSecSNMPFWinterface_Type()
)
hmSecSNMPFWinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPFWinterface.setStatus("mandatory")


class _HmSecSNMPFWtarget_Type(Integer32):
    """Custom type hmSecSNMPFWtarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("drop", 3))
    )


_HmSecSNMPFWtarget_Type.__name__ = "Integer32"
_HmSecSNMPFWtarget_Object = MibTableColumn
hmSecSNMPFWtarget = _HmSecSNMPFWtarget_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 4),
    _HmSecSNMPFWtarget_Type()
)
hmSecSNMPFWtarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPFWtarget.setStatus("mandatory")


class _HmSecSNMPFWlog_Type(Integer32):
    """Custom type hmSecSNMPFWlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecSNMPFWlog_Type.__name__ = "Integer32"
_HmSecSNMPFWlog_Object = MibTableColumn
hmSecSNMPFWlog = _HmSecSNMPFWlog_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 5),
    _HmSecSNMPFWlog_Type()
)
hmSecSNMPFWlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPFWlog.setStatus("mandatory")
_HmSecSNMPFWRowStatus_Type = RowStatus
_HmSecSNMPFWRowStatus_Object = MibTableColumn
hmSecSNMPFWRowStatus = _HmSecSNMPFWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 6),
    _HmSecSNMPFWRowStatus_Type()
)
hmSecSNMPFWRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPFWRowStatus.setStatus("mandatory")
_HmSecSNMPFWcomment_Type = DisplayString
_HmSecSNMPFWcomment_Object = MibTableColumn
hmSecSNMPFWcomment = _HmSecSNMPFWcomment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 6, 1, 7),
    _HmSecSNMPFWcomment_Type()
)
hmSecSNMPFWcomment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPFWcomment.setStatus("mandatory")
_HmSecSNMPTrapReceiverTable_Object = MibTable
hmSecSNMPTrapReceiverTable = _HmSecSNMPTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7)
)
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverTable.setStatus("mandatory")
_HmSecSNMPTrapReceiverEntry_Object = MibTableRow
hmSecSNMPTrapReceiverEntry = _HmSecSNMPTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7, 1)
)
hmSecSNMPTrapReceiverEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecSNMPTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverEntry.setStatus("mandatory")


class _HmSecSNMPTrapReceiverIndex_Type(Integer32):
    """Custom type hmSecSNMPTrapReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmSecSNMPTrapReceiverIndex_Type.__name__ = "Integer32"
_HmSecSNMPTrapReceiverIndex_Object = MibTableColumn
hmSecSNMPTrapReceiverIndex = _HmSecSNMPTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7, 1, 1),
    _HmSecSNMPTrapReceiverIndex_Type()
)
hmSecSNMPTrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverIndex.setStatus("mandatory")
_HmSecSNMPTrapReceiverCommunity_Type = DisplayString
_HmSecSNMPTrapReceiverCommunity_Object = MibTableColumn
hmSecSNMPTrapReceiverCommunity = _HmSecSNMPTrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7, 1, 2),
    _HmSecSNMPTrapReceiverCommunity_Type()
)
hmSecSNMPTrapReceiverCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverCommunity.setStatus("mandatory")
_HmSecSNMPTrapReceiverIPAddress_Type = IpAddress
_HmSecSNMPTrapReceiverIPAddress_Object = MibTableColumn
hmSecSNMPTrapReceiverIPAddress = _HmSecSNMPTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7, 1, 3),
    _HmSecSNMPTrapReceiverIPAddress_Type()
)
hmSecSNMPTrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverIPAddress.setStatus("mandatory")
_HmSecSNMPTrapReceiverName_Type = DisplayString
_HmSecSNMPTrapReceiverName_Object = MibTableColumn
hmSecSNMPTrapReceiverName = _HmSecSNMPTrapReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7, 1, 4),
    _HmSecSNMPTrapReceiverName_Type()
)
hmSecSNMPTrapReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverName.setStatus("mandatory")
_HmSecSNMPTrapReceiverRowStatus_Type = RowStatus
_HmSecSNMPTrapReceiverRowStatus_Object = MibTableColumn
hmSecSNMPTrapReceiverRowStatus = _HmSecSNMPTrapReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 7, 1, 5),
    _HmSecSNMPTrapReceiverRowStatus_Type()
)
hmSecSNMPTrapReceiverRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPTrapReceiverRowStatus.setStatus("mandatory")
_HmSecSNMPTrapConfigGroup_ObjectIdentity = ObjectIdentity
hmSecSNMPTrapConfigGroup = _HmSecSNMPTrapConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8)
)


class _HmSecSNMPAuthenticationTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPAuthenticationTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPAuthenticationTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPAuthenticationTrapFlag_Object = MibScalar
hmSecSNMPAuthenticationTrapFlag = _HmSecSNMPAuthenticationTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 1),
    _HmSecSNMPAuthenticationTrapFlag_Type()
)
hmSecSNMPAuthenticationTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPAuthenticationTrapFlag.setStatus("mandatory")


class _HmSecSNMPLinkUpDownTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPLinkUpDownTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPLinkUpDownTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPLinkUpDownTrapFlag_Object = MibScalar
hmSecSNMPLinkUpDownTrapFlag = _HmSecSNMPLinkUpDownTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 2),
    _HmSecSNMPLinkUpDownTrapFlag_Type()
)
hmSecSNMPLinkUpDownTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPLinkUpDownTrapFlag.setStatus("mandatory")


class _HmSecSNMPColdStartTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPColdStartTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPColdStartTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPColdStartTrapFlag_Object = MibScalar
hmSecSNMPColdStartTrapFlag = _HmSecSNMPColdStartTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 3),
    _HmSecSNMPColdStartTrapFlag_Type()
)
hmSecSNMPColdStartTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPColdStartTrapFlag.setStatus("mandatory")


class _HmSecSNMPTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPTrapFlag_Object = MibScalar
hmSecSNMPTrapFlag = _HmSecSNMPTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 4),
    _HmSecSNMPTrapFlag_Type()
)
hmSecSNMPTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPTrapFlag.setStatus("mandatory")


class _HmSecSNMPChassisTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPChassisTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPChassisTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPChassisTrapFlag_Object = MibScalar
hmSecSNMPChassisTrapFlag = _HmSecSNMPChassisTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 5),
    _HmSecSNMPChassisTrapFlag_Type()
)
hmSecSNMPChassisTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPChassisTrapFlag.setStatus("mandatory")


class _HmSecSNMPAgentTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPAgentTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPAgentTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPAgentTrapFlag_Object = MibScalar
hmSecSNMPAgentTrapFlag = _HmSecSNMPAgentTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 6),
    _HmSecSNMPAgentTrapFlag_Type()
)
hmSecSNMPAgentTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPAgentTrapFlag.setStatus("mandatory")


class _HmSecSNMPAvFailTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPAvFailTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPAvFailTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPAvFailTrapFlag_Object = MibScalar
hmSecSNMPAvFailTrapFlag = _HmSecSNMPAvFailTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 7),
    _HmSecSNMPAvFailTrapFlag_Type()
)
hmSecSNMPAvFailTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPAvFailTrapFlag.setStatus("mandatory")


class _HmSecSNMPAvInfoTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPAvInfoTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPAvInfoTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPAvInfoTrapFlag_Object = MibScalar
hmSecSNMPAvInfoTrapFlag = _HmSecSNMPAvInfoTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 8),
    _HmSecSNMPAvInfoTrapFlag_Type()
)
hmSecSNMPAvInfoTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPAvInfoTrapFlag.setStatus("mandatory")


class _HmSecSNMPBladeStateTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPBladeStateTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPBladeStateTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPBladeStateTrapFlag_Object = MibScalar
hmSecSNMPBladeStateTrapFlag = _HmSecSNMPBladeStateTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 9),
    _HmSecSNMPBladeStateTrapFlag_Type()
)
hmSecSNMPBladeStateTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPBladeStateTrapFlag.setStatus("mandatory")


class _HmSecSNMPBladeConfigTrapFlag_Type(Integer32):
    """Custom type hmSecSNMPBladeConfigTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPBladeConfigTrapFlag_Type.__name__ = "Integer32"
_HmSecSNMPBladeConfigTrapFlag_Object = MibScalar
hmSecSNMPBladeConfigTrapFlag = _HmSecSNMPBladeConfigTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 10),
    _HmSecSNMPBladeConfigTrapFlag_Type()
)
hmSecSNMPBladeConfigTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPBladeConfigTrapFlag.setStatus("mandatory")


class _HmSecSNMPRouterRedundancyStatusFlag_Type(Integer32):
    """Custom type hmSecSNMPRouterRedundancyStatusFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecSNMPRouterRedundancyStatusFlag_Type.__name__ = "Integer32"
_HmSecSNMPRouterRedundancyStatusFlag_Object = MibScalar
hmSecSNMPRouterRedundancyStatusFlag = _HmSecSNMPRouterRedundancyStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 5, 8, 11),
    _HmSecSNMPRouterRedundancyStatusFlag_Type()
)
hmSecSNMPRouterRedundancyStatusFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecSNMPRouterRedundancyStatusFlag.setStatus("mandatory")
_HmSecNTP_ObjectIdentity = ObjectIdentity
hmSecNTP = _HmSecNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 6)
)


class _HmSecNTPactivate_Type(Integer32):
    """Custom type hmSecNTPactivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecNTPactivate_Type.__name__ = "Integer32"
_HmSecNTPactivate_Object = MibScalar
hmSecNTPactivate = _HmSecNTPactivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 1),
    _HmSecNTPactivate_Type()
)
hmSecNTPactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecNTPactivate.setStatus("mandatory")


class _HmSecNTPtimestamp_Type(Integer32):
    """Custom type hmSecNTPtimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecNTPtimestamp_Type.__name__ = "Integer32"
_HmSecNTPtimestamp_Object = MibScalar
hmSecNTPtimestamp = _HmSecNTPtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 2),
    _HmSecNTPtimestamp_Type()
)
hmSecNTPtimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecNTPtimestamp.setStatus("mandatory")
_HmSecNTPServerTable_Object = MibTable
hmSecNTPServerTable = _HmSecNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 3)
)
if mibBuilder.loadTexts:
    hmSecNTPServerTable.setStatus("mandatory")
_HmSecNTPServerEntry_Object = MibTableRow
hmSecNTPServerEntry = _HmSecNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 3, 1)
)
hmSecNTPServerEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecNTPServerIndex"),
)
if mibBuilder.loadTexts:
    hmSecNTPServerEntry.setStatus("mandatory")


class _HmSecNTPServerIndex_Type(Integer32):
    """Custom type hmSecNTPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HmSecNTPServerIndex_Type.__name__ = "Integer32"
_HmSecNTPServerIndex_Object = MibTableColumn
hmSecNTPServerIndex = _HmSecNTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 3, 1, 1),
    _HmSecNTPServerIndex_Type()
)
hmSecNTPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecNTPServerIndex.setStatus("mandatory")
_HmSecNTPServerHost_Type = DisplayString
_HmSecNTPServerHost_Object = MibTableColumn
hmSecNTPServerHost = _HmSecNTPServerHost_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 3, 1, 2),
    _HmSecNTPServerHost_Type()
)
hmSecNTPServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecNTPServerHost.setStatus("mandatory")
_HmSecNTPServerRowStatus_Type = RowStatus
_HmSecNTPServerRowStatus_Object = MibTableColumn
hmSecNTPServerRowStatus = _HmSecNTPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 3, 1, 3),
    _HmSecNTPServerRowStatus_Type()
)
hmSecNTPServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecNTPServerRowStatus.setStatus("mandatory")
_HmSecNTPTimezone_Type = DisplayString
_HmSecNTPTimezone_Object = MibScalar
hmSecNTPTimezone = _HmSecNTPTimezone_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 4),
    _HmSecNTPTimezone_Type()
)
hmSecNTPTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecNTPTimezone.setStatus("mandatory")
_HmSecNTPStatus_Type = DisplayString
_HmSecNTPStatus_Object = MibScalar
hmSecNTPStatus = _HmSecNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 6, 5),
    _HmSecNTPStatus_Type()
)
hmSecNTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecNTPStatus.setStatus("mandatory")
_HmSecUpdate_ObjectIdentity = ObjectIdentity
hmSecUpdate = _HmSecUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 7)
)
_HmSecUpdateServerTable_Object = MibTable
hmSecUpdateServerTable = _HmSecUpdateServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1)
)
if mibBuilder.loadTexts:
    hmSecUpdateServerTable.setStatus("mandatory")
_HmSecUpdateServerEntry_Object = MibTableRow
hmSecUpdateServerEntry = _HmSecUpdateServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1)
)
hmSecUpdateServerEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecUpdateServerIndex"),
)
if mibBuilder.loadTexts:
    hmSecUpdateServerEntry.setStatus("mandatory")


class _HmSecUpdateServerIndex_Type(Integer32):
    """Custom type hmSecUpdateServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HmSecUpdateServerIndex_Type.__name__ = "Integer32"
_HmSecUpdateServerIndex_Object = MibTableColumn
hmSecUpdateServerIndex = _HmSecUpdateServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 1),
    _HmSecUpdateServerIndex_Type()
)
hmSecUpdateServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecUpdateServerIndex.setStatus("mandatory")
_HmSecUpdateServer_Type = DisplayString
_HmSecUpdateServer_Object = MibTableColumn
hmSecUpdateServer = _HmSecUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 2),
    _HmSecUpdateServer_Type()
)
hmSecUpdateServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUpdateServer.setStatus("deprecated")
_HmSecUpdateServerRowStatus_Type = RowStatus
_HmSecUpdateServerRowStatus_Object = MibTableColumn
hmSecUpdateServerRowStatus = _HmSecUpdateServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 3),
    _HmSecUpdateServerRowStatus_Type()
)
hmSecUpdateServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUpdateServerRowStatus.setStatus("mandatory")
_HmSecUpdateServerProto_Type = DisplayString
_HmSecUpdateServerProto_Object = MibTableColumn
hmSecUpdateServerProto = _HmSecUpdateServerProto_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 4),
    _HmSecUpdateServerProto_Type()
)
hmSecUpdateServerProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUpdateServerProto.setStatus("mandatory")
_HmSecUpdateServerHost_Type = DisplayString
_HmSecUpdateServerHost_Object = MibTableColumn
hmSecUpdateServerHost = _HmSecUpdateServerHost_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 5),
    _HmSecUpdateServerHost_Type()
)
hmSecUpdateServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUpdateServerHost.setStatus("mandatory")
_HmSecUpdateServerLogin_Type = DisplayString
_HmSecUpdateServerLogin_Object = MibTableColumn
hmSecUpdateServerLogin = _HmSecUpdateServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 6),
    _HmSecUpdateServerLogin_Type()
)
hmSecUpdateServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUpdateServerLogin.setStatus("mandatory")
_HmSecUpdateServerPassword_Type = DisplayString
_HmSecUpdateServerPassword_Object = MibTableColumn
hmSecUpdateServerPassword = _HmSecUpdateServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 7, 1, 1, 7),
    _HmSecUpdateServerPassword_Type()
)
hmSecUpdateServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecUpdateServerPassword.setStatus("mandatory")
_HmSecSNMPError_Type = DisplayString
_HmSecSNMPError_Object = MibScalar
hmSecSNMPError = _HmSecSNMPError_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 8),
    _HmSecSNMPError_Type()
)
hmSecSNMPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecSNMPError.setStatus("mandatory")
_HmSecRedundancy_ObjectIdentity = ObjectIdentity
hmSecRedundancy = _HmSecRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 9)
)
_HmSecL2Redundancy_ObjectIdentity = ObjectIdentity
hmSecL2Redundancy = _HmSecL2Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 1)
)


class _HmSecL2RedundancyEnable_Type(Integer32):
    """Custom type hmSecL2RedundancyEnable based on Integer32"""
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


_HmSecL2RedundancyEnable_Type.__name__ = "Integer32"
_HmSecL2RedundancyEnable_Object = MibScalar
hmSecL2RedundancyEnable = _HmSecL2RedundancyEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 1, 1),
    _HmSecL2RedundancyEnable_Type()
)
hmSecL2RedundancyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2RedundancyEnable.setStatus("mandatory")


class _HmSecL2RedundancyPort_Type(Integer32):
    """Custom type hmSecL2RedundancyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intern", 1),
          ("extern", 2))
    )


_HmSecL2RedundancyPort_Type.__name__ = "Integer32"
_HmSecL2RedundancyPort_Object = MibScalar
hmSecL2RedundancyPort = _HmSecL2RedundancyPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 1, 2),
    _HmSecL2RedundancyPort_Type()
)
hmSecL2RedundancyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecL2RedundancyPort.setStatus("mandatory")
_HmSecRouterRedundancy_ObjectIdentity = ObjectIdentity
hmSecRouterRedundancy = _HmSecRouterRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2)
)


class _HmSecRouterRedundancyEnable_Type(Integer32):
    """Custom type hmSecRouterRedundancyEnable based on Integer32"""
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


_HmSecRouterRedundancyEnable_Type.__name__ = "Integer32"
_HmSecRouterRedundancyEnable_Object = MibScalar
hmSecRouterRedundancyEnable = _HmSecRouterRedundancyEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 1),
    _HmSecRouterRedundancyEnable_Type()
)
hmSecRouterRedundancyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyEnable.setStatus("mandatory")


class _HmSecRouterRedundancyTrack_Type(Integer32):
    """Custom type hmSecRouterRedundancyTrack based on Integer32"""
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


_HmSecRouterRedundancyTrack_Type.__name__ = "Integer32"
_HmSecRouterRedundancyTrack_Object = MibScalar
hmSecRouterRedundancyTrack = _HmSecRouterRedundancyTrack_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 2),
    _HmSecRouterRedundancyTrack_Type()
)
hmSecRouterRedundancyTrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyTrack.setStatus("mandatory")
_HmSecRouterRedundancyInternalID_Type = Integer32
_HmSecRouterRedundancyInternalID_Object = MibScalar
hmSecRouterRedundancyInternalID = _HmSecRouterRedundancyInternalID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 3),
    _HmSecRouterRedundancyInternalID_Type()
)
hmSecRouterRedundancyInternalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyInternalID.setStatus("mandatory")
_HmSecRouterRedundancyExternalID_Type = Integer32
_HmSecRouterRedundancyExternalID_Object = MibScalar
hmSecRouterRedundancyExternalID = _HmSecRouterRedundancyExternalID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 4),
    _HmSecRouterRedundancyExternalID_Type()
)
hmSecRouterRedundancyExternalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyExternalID.setStatus("mandatory")
_HmSecRouterRedundancyPassword_Type = DisplayString
_HmSecRouterRedundancyPassword_Object = MibScalar
hmSecRouterRedundancyPassword = _HmSecRouterRedundancyPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 5),
    _HmSecRouterRedundancyPassword_Type()
)
hmSecRouterRedundancyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyPassword.setStatus("mandatory")
_HmSecRouterRedundancyPeerIntern_Type = IpAddress
_HmSecRouterRedundancyPeerIntern_Object = MibScalar
hmSecRouterRedundancyPeerIntern = _HmSecRouterRedundancyPeerIntern_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 6),
    _HmSecRouterRedundancyPeerIntern_Type()
)
hmSecRouterRedundancyPeerIntern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyPeerIntern.setStatus("mandatory")
_HmSecRouterRedundancyPeerExtern_Type = IpAddress
_HmSecRouterRedundancyPeerExtern_Object = MibScalar
hmSecRouterRedundancyPeerExtern = _HmSecRouterRedundancyPeerExtern_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 7),
    _HmSecRouterRedundancyPeerExtern_Type()
)
hmSecRouterRedundancyPeerExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyPeerExtern.setStatus("mandatory")
_HmSecRouterRedundancyPriority_Type = Integer32
_HmSecRouterRedundancyPriority_Object = MibScalar
hmSecRouterRedundancyPriority = _HmSecRouterRedundancyPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 8),
    _HmSecRouterRedundancyPriority_Type()
)
hmSecRouterRedundancyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyPriority.setStatus("mandatory")
_HmSecRouterRedundancyVirtIpInt_Type = IpAddress
_HmSecRouterRedundancyVirtIpInt_Object = MibScalar
hmSecRouterRedundancyVirtIpInt = _HmSecRouterRedundancyVirtIpInt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 9),
    _HmSecRouterRedundancyVirtIpInt_Type()
)
hmSecRouterRedundancyVirtIpInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyVirtIpInt.setStatus("mandatory")
_HmSecRouterRedundancyVirtIpExt_Type = IpAddress
_HmSecRouterRedundancyVirtIpExt_Object = MibScalar
hmSecRouterRedundancyVirtIpExt = _HmSecRouterRedundancyVirtIpExt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 10),
    _HmSecRouterRedundancyVirtIpExt_Type()
)
hmSecRouterRedundancyVirtIpExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyVirtIpExt.setStatus("mandatory")


class _HmSecRouterRedundancyWantState_Type(Integer32):
    """Custom type hmSecRouterRedundancyWantState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("backup", 2))
    )


_HmSecRouterRedundancyWantState_Type.__name__ = "Integer32"
_HmSecRouterRedundancyWantState_Object = MibScalar
hmSecRouterRedundancyWantState = _HmSecRouterRedundancyWantState_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 11),
    _HmSecRouterRedundancyWantState_Type()
)
hmSecRouterRedundancyWantState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyWantState.setStatus("mandatory")
_HmSecRouterRedExtHostCheckTable_Object = MibTable
hmSecRouterRedExtHostCheckTable = _HmSecRouterRedExtHostCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 12)
)
if mibBuilder.loadTexts:
    hmSecRouterRedExtHostCheckTable.setStatus("mandatory")
_HmSecRouterRedExtHostCheckEntry_Object = MibTableRow
hmSecRouterRedExtHostCheckEntry = _HmSecRouterRedExtHostCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 12, 1)
)
hmSecRouterRedExtHostCheckEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecRouterRedExtHostCheckIndex"),
)
if mibBuilder.loadTexts:
    hmSecRouterRedExtHostCheckEntry.setStatus("mandatory")


class _HmSecRouterRedExtHostCheckIndex_Type(Integer32):
    """Custom type hmSecRouterRedExtHostCheckIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecRouterRedExtHostCheckIndex_Type.__name__ = "Integer32"
_HmSecRouterRedExtHostCheckIndex_Object = MibTableColumn
hmSecRouterRedExtHostCheckIndex = _HmSecRouterRedExtHostCheckIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 12, 1, 1),
    _HmSecRouterRedExtHostCheckIndex_Type()
)
hmSecRouterRedExtHostCheckIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecRouterRedExtHostCheckIndex.setStatus("mandatory")
_HmSecRouterRedExtHostCheckIP_Type = IpAddress
_HmSecRouterRedExtHostCheckIP_Object = MibTableColumn
hmSecRouterRedExtHostCheckIP = _HmSecRouterRedExtHostCheckIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 12, 1, 2),
    _HmSecRouterRedExtHostCheckIP_Type()
)
hmSecRouterRedExtHostCheckIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedExtHostCheckIP.setStatus("mandatory")
_HmSecRouterRedExtHostCheckRowSt_Type = RowStatus
_HmSecRouterRedExtHostCheckRowSt_Object = MibTableColumn
hmSecRouterRedExtHostCheckRowSt = _HmSecRouterRedExtHostCheckRowSt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 12, 1, 3),
    _HmSecRouterRedExtHostCheckRowSt_Type()
)
hmSecRouterRedExtHostCheckRowSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedExtHostCheckRowSt.setStatus("mandatory")
_HmSecRouterRedIntHostCheckTable_Object = MibTable
hmSecRouterRedIntHostCheckTable = _HmSecRouterRedIntHostCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 13)
)
if mibBuilder.loadTexts:
    hmSecRouterRedIntHostCheckTable.setStatus("mandatory")
_HmSecRouterRedIntHostCheckEntry_Object = MibTableRow
hmSecRouterRedIntHostCheckEntry = _HmSecRouterRedIntHostCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 13, 1)
)
hmSecRouterRedIntHostCheckEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecRouterRedIntHostCheckIndex"),
)
if mibBuilder.loadTexts:
    hmSecRouterRedIntHostCheckEntry.setStatus("mandatory")


class _HmSecRouterRedIntHostCheckIndex_Type(Integer32):
    """Custom type hmSecRouterRedIntHostCheckIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecRouterRedIntHostCheckIndex_Type.__name__ = "Integer32"
_HmSecRouterRedIntHostCheckIndex_Object = MibTableColumn
hmSecRouterRedIntHostCheckIndex = _HmSecRouterRedIntHostCheckIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 13, 1, 1),
    _HmSecRouterRedIntHostCheckIndex_Type()
)
hmSecRouterRedIntHostCheckIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecRouterRedIntHostCheckIndex.setStatus("mandatory")
_HmSecRouterRedIntHostCheckIP_Type = IpAddress
_HmSecRouterRedIntHostCheckIP_Object = MibTableColumn
hmSecRouterRedIntHostCheckIP = _HmSecRouterRedIntHostCheckIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 13, 1, 2),
    _HmSecRouterRedIntHostCheckIP_Type()
)
hmSecRouterRedIntHostCheckIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedIntHostCheckIP.setStatus("mandatory")
_HmSecRouterRedIntHostCheckRowSt_Type = RowStatus
_HmSecRouterRedIntHostCheckRowSt_Object = MibTableColumn
hmSecRouterRedIntHostCheckRowSt = _HmSecRouterRedIntHostCheckRowSt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 13, 1, 3),
    _HmSecRouterRedIntHostCheckRowSt_Type()
)
hmSecRouterRedIntHostCheckRowSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecRouterRedIntHostCheckRowSt.setStatus("mandatory")


class _HmSecRouterRedundancyState_Type(Integer32):
    """Custom type hmSecRouterRedundancyState based on Integer32"""
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
        *(("backup", 1),
          ("master", 2),
          ("fault", 3),
          ("disabled", 4))
    )


_HmSecRouterRedundancyState_Type.__name__ = "Integer32"
_HmSecRouterRedundancyState_Object = MibScalar
hmSecRouterRedundancyState = _HmSecRouterRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 9, 2, 14),
    _HmSecRouterRedundancyState_Type()
)
hmSecRouterRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecRouterRedundancyState.setStatus("mandatory")
_HmSecInfo_ObjectIdentity = ObjectIdentity
hmSecInfo = _HmSecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10)
)
_HmSecHTTPSLastAccessIP_Type = IpAddress
_HmSecHTTPSLastAccessIP_Object = MibScalar
hmSecHTTPSLastAccessIP = _HmSecHTTPSLastAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 1),
    _HmSecHTTPSLastAccessIP_Type()
)
hmSecHTTPSLastAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecHTTPSLastAccessIP.setStatus("mandatory")
_HmSecShellLastAccessIP_Type = IpAddress
_HmSecShellLastAccessIP_Object = MibScalar
hmSecShellLastAccessIP = _HmSecShellLastAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 2),
    _HmSecShellLastAccessIP_Type()
)
hmSecShellLastAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecShellLastAccessIP.setStatus("mandatory")
_HmSecDHCPLastAccessMAC_Type = MacAddress
_HmSecDHCPLastAccessMAC_Object = MibScalar
hmSecDHCPLastAccessMAC = _HmSecDHCPLastAccessMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 3),
    _HmSecDHCPLastAccessMAC_Type()
)
hmSecDHCPLastAccessMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecDHCPLastAccessMAC.setStatus("mandatory")
_HmSecTrapRessources_ObjectIdentity = ObjectIdentity
hmSecTrapRessources = _HmSecTrapRessources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4)
)


class _HmSecTResDiscFull_Type(Integer32):
    """Custom type hmSecTResDiscFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("tight", 2),
          ("full", 3))
    )


_HmSecTResDiscFull_Type.__name__ = "Integer32"
_HmSecTResDiscFull_Object = MibScalar
hmSecTResDiscFull = _HmSecTResDiscFull_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 1),
    _HmSecTResDiscFull_Type()
)
hmSecTResDiscFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResDiscFull.setStatus("mandatory")
_HmSecTResCpuLoadHigh_Type = Integer32
_HmSecTResCpuLoadHigh_Object = MibScalar
hmSecTResCpuLoadHigh = _HmSecTResCpuLoadHigh_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 2),
    _HmSecTResCpuLoadHigh_Type()
)
hmSecTResCpuLoadHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResCpuLoadHigh.setStatus("mandatory")
_HmSecTResMemoryFull_Type = Integer32
_HmSecTResMemoryFull_Object = MibScalar
hmSecTResMemoryFull = _HmSecTResMemoryFull_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 3),
    _HmSecTResMemoryFull_Type()
)
hmSecTResMemoryFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResMemoryFull.setStatus("mandatory")
_HmSecTResColdstart_Type = Integer32
_HmSecTResColdstart_Object = MibScalar
hmSecTResColdstart = _HmSecTResColdstart_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 4),
    _HmSecTResColdstart_Type()
)
hmSecTResColdstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResColdstart.setStatus("mandatory")
_HmSecTResAV_ObjectIdentity = ObjectIdentity
hmSecTResAV = _HmSecTResAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 6)
)
_HmSecTResAvUpdateDone_Type = DisplayString
_HmSecTResAvUpdateDone_Object = MibScalar
hmSecTResAvUpdateDone = _HmSecTResAvUpdateDone_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 6, 1),
    _HmSecTResAvUpdateDone_Type()
)
hmSecTResAvUpdateDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResAvUpdateDone.setStatus("mandatory")
_HmSecTResAvUpdateError_Type = DisplayString
_HmSecTResAvUpdateError_Object = MibScalar
hmSecTResAvUpdateError = _HmSecTResAvUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 6, 2),
    _HmSecTResAvUpdateError_Type()
)
hmSecTResAvUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResAvUpdateError.setStatus("mandatory")
_HmSecTResAvVirusDetected_Type = DisplayString
_HmSecTResAvVirusDetected_Object = MibScalar
hmSecTResAvVirusDetected = _HmSecTResAvVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 6, 3),
    _HmSecTResAvVirusDetected_Type()
)
hmSecTResAvVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResAvVirusDetected.setStatus("mandatory")
_HmSecTResAvFileNotScanned_Type = DisplayString
_HmSecTResAvFileNotScanned_Object = MibScalar
hmSecTResAvFileNotScanned = _HmSecTResAvFileNotScanned_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 6, 4),
    _HmSecTResAvFileNotScanned_Type()
)
hmSecTResAvFileNotScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResAvFileNotScanned.setStatus("mandatory")
_HmSecTResAvFailed_Type = DisplayString
_HmSecTResAvFailed_Object = MibScalar
hmSecTResAvFailed = _HmSecTResAvFailed_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 6, 5),
    _HmSecTResAvFailed_Type()
)
hmSecTResAvFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResAvFailed.setStatus("mandatory")
_HmSecTResPlatformSpecific_ObjectIdentity = ObjectIdentity
hmSecTResPlatformSpecific = _HmSecTResPlatformSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7)
)
_HmSecTResIndustrial_ObjectIdentity = ObjectIdentity
hmSecTResIndustrial = _HmSecTResIndustrial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1)
)
_HmSecTResIndustrialPower_ObjectIdentity = ObjectIdentity
hmSecTResIndustrialPower = _HmSecTResIndustrialPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 1)
)
_HmSecPSTable_Object = MibTable
hmSecPSTable = _HmSecPSTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hmSecPSTable.setStatus("mandatory")
_HmSecPSEntry_Object = MibTableRow
hmSecPSEntry = _HmSecPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 1, 2, 1)
)
hmSecPSEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecPSSysID"),
    (0, "HmSecurityGateway-MIB", "hmSecPSID"),
)
if mibBuilder.loadTexts:
    hmSecPSEntry.setStatus("mandatory")


class _HmSecPSSysID_Type(Integer32):
    """Custom type hmSecPSSysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecPSSysID_Type.__name__ = "Integer32"
_HmSecPSSysID_Object = MibTableColumn
hmSecPSSysID = _HmSecPSSysID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 1, 2, 1, 1),
    _HmSecPSSysID_Type()
)
hmSecPSSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPSSysID.setStatus("mandatory")


class _HmSecPSID_Type(Integer32):
    """Custom type hmSecPSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecPSID_Type.__name__ = "Integer32"
_HmSecPSID_Object = MibTableColumn
hmSecPSID = _HmSecPSID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 1, 2, 1, 2),
    _HmSecPSID_Type()
)
hmSecPSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPSID.setStatus("mandatory")


class _HmSecPSState_Type(Integer32):
    """Custom type hmSecPSState based on Integer32"""
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
        *(("ok", 1),
          ("failed", 2),
          ("notInstalled", 3),
          ("unknown", 4))
    )


_HmSecPSState_Type.__name__ = "Integer32"
_HmSecPSState_Object = MibTableColumn
hmSecPSState = _HmSecPSState_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 1, 2, 1, 3),
    _HmSecPSState_Type()
)
hmSecPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecPSState.setStatus("mandatory")
_HmSecTResIndustrialTemperature_ObjectIdentity = ObjectIdentity
hmSecTResIndustrialTemperature = _HmSecTResIndustrialTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 2)
)
_HmSecTResIndustrialTempHiLimit_Type = Integer32
_HmSecTResIndustrialTempHiLimit_Object = MibScalar
hmSecTResIndustrialTempHiLimit = _HmSecTResIndustrialTempHiLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 2, 2),
    _HmSecTResIndustrialTempHiLimit_Type()
)
hmSecTResIndustrialTempHiLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecTResIndustrialTempHiLimit.setStatus("mandatory")
_HmSecTResIndustrialTempLowLimit_Type = Integer32
_HmSecTResIndustrialTempLowLimit_Object = MibScalar
hmSecTResIndustrialTempLowLimit = _HmSecTResIndustrialTempLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 2, 3),
    _HmSecTResIndustrialTempLowLimit_Type()
)
hmSecTResIndustrialTempLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecTResIndustrialTempLowLimit.setStatus("mandatory")
_HmSecTResSignalRelais_ObjectIdentity = ObjectIdentity
hmSecTResSignalRelais = _HmSecTResSignalRelais_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3)
)
_HmSecTResSignalRelaisState_Type = Integer32
_HmSecTResSignalRelaisState_Object = MibScalar
hmSecTResSignalRelaisState = _HmSecTResSignalRelaisState_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3, 1),
    _HmSecTResSignalRelaisState_Type()
)
hmSecTResSignalRelaisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResSignalRelaisState.setStatus("mandatory")
_HmSecTResSignalRelaisReason_Type = ObjectIdentifier
_HmSecTResSignalRelaisReason_Object = MibScalar
hmSecTResSignalRelaisReason = _HmSecTResSignalRelaisReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3, 2),
    _HmSecTResSignalRelaisReason_Type()
)
hmSecTResSignalRelaisReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResSignalRelaisReason.setStatus("mandatory")
_HmSecTResSignalRelaisReasonIdx_Type = Integer32
_HmSecTResSignalRelaisReasonIdx_Object = MibScalar
hmSecTResSignalRelaisReasonIdx = _HmSecTResSignalRelaisReasonIdx_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3, 3),
    _HmSecTResSignalRelaisReasonIdx_Type()
)
hmSecTResSignalRelaisReasonIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResSignalRelaisReasonIdx.setStatus("mandatory")


class _HmSecTResSignalRelaisPowerAlarm_Type(Integer32):
    """Custom type hmSecTResSignalRelaisPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecTResSignalRelaisPowerAlarm_Type.__name__ = "Integer32"
_HmSecTResSignalRelaisPowerAlarm_Object = MibScalar
hmSecTResSignalRelaisPowerAlarm = _HmSecTResSignalRelaisPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3, 4),
    _HmSecTResSignalRelaisPowerAlarm_Type()
)
hmSecTResSignalRelaisPowerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecTResSignalRelaisPowerAlarm.setStatus("mandatory")


class _HmSecTResSignalRelaisMode_Type(Integer32):
    """Custom type hmSecTResSignalRelaisMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("manual", 2))
    )


_HmSecTResSignalRelaisMode_Type.__name__ = "Integer32"
_HmSecTResSignalRelaisMode_Object = MibScalar
hmSecTResSignalRelaisMode = _HmSecTResSignalRelaisMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3, 5),
    _HmSecTResSignalRelaisMode_Type()
)
hmSecTResSignalRelaisMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecTResSignalRelaisMode.setStatus("mandatory")


class _HmSecTResSignalRelaisManualStat_Type(Integer32):
    """Custom type hmSecTResSignalRelaisManualStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HmSecTResSignalRelaisManualStat_Type.__name__ = "Integer32"
_HmSecTResSignalRelaisManualStat_Object = MibScalar
hmSecTResSignalRelaisManualStat = _HmSecTResSignalRelaisManualStat_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 3, 6),
    _HmSecTResSignalRelaisManualStat_Type()
)
hmSecTResSignalRelaisManualStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecTResSignalRelaisManualStat.setStatus("mandatory")


class _HmSecTResAutoConfigAdapterState_Type(Integer32):
    """Custom type hmSecTResAutoConfigAdapterState based on Integer32"""
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
        *(("notPresent", 1),
          ("removed", 2),
          ("ok", 3),
          ("notInSync", 4),
          ("outOfMemory", 5),
          ("wrongMachine", 6),
          ("checksumErr", 7),
          ("genericErr", 8))
    )


_HmSecTResAutoConfigAdapterState_Type.__name__ = "Integer32"
_HmSecTResAutoConfigAdapterState_Object = MibScalar
hmSecTResAutoConfigAdapterState = _HmSecTResAutoConfigAdapterState_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 4),
    _HmSecTResAutoConfigAdapterState_Type()
)
hmSecTResAutoConfigAdapterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResAutoConfigAdapterState.setStatus("mandatory")
_HmSecTResSignalLinkTable_ObjectIdentity = ObjectIdentity
hmSecTResSignalLinkTable = _HmSecTResSignalLinkTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 5)
)


class _HmSecTResSigLinkID_Type(Integer32):
    """Custom type hmSecTResSigLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmSecTResSigLinkID_Type.__name__ = "Integer32"
_HmSecTResSigLinkID_Object = MibScalar
hmSecTResSigLinkID = _HmSecTResSigLinkID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 5, 1),
    _HmSecTResSigLinkID_Type()
)
hmSecTResSigLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResSigLinkID.setStatus("mandatory")


class _HmSecTResSigLinkAlarm_Type(Integer32):
    """Custom type hmSecTResSigLinkAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HmSecTResSigLinkAlarm_Type.__name__ = "Integer32"
_HmSecTResSigLinkAlarm_Object = MibScalar
hmSecTResSigLinkAlarm = _HmSecTResSigLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 1, 5, 2),
    _HmSecTResSigLinkAlarm_Type()
)
hmSecTResSigLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecTResSigLinkAlarm.setStatus("mandatory")
_HmSecTResBladeCTRL_ObjectIdentity = ObjectIdentity
hmSecTResBladeCTRL = _HmSecTResBladeCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2)
)
_HmSecTResBladeInfo_ObjectIdentity = ObjectIdentity
hmSecTResBladeInfo = _HmSecTResBladeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 1)
)
_HmSecTResBladeRackID_Type = DisplayString
_HmSecTResBladeRackID_Object = MibScalar
hmSecTResBladeRackID = _HmSecTResBladeRackID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 1, 1),
    _HmSecTResBladeRackID_Type()
)
hmSecTResBladeRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeRackID.setStatus("mandatory")
_HmSecTResBladeSlotNr_Type = Integer32
_HmSecTResBladeSlotNr_Object = MibScalar
hmSecTResBladeSlotNr = _HmSecTResBladeSlotNr_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 1, 2),
    _HmSecTResBladeSlotNr_Type()
)
hmSecTResBladeSlotNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeSlotNr.setStatus("mandatory")


class _HmSecTResBladeCtrlPowerStatus_Type(Integer32):
    """Custom type hmSecTResBladeCtrlPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2),
          ("online", 3))
    )


_HmSecTResBladeCtrlPowerStatus_Type.__name__ = "Integer32"
_HmSecTResBladeCtrlPowerStatus_Object = MibScalar
hmSecTResBladeCtrlPowerStatus = _HmSecTResBladeCtrlPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 2),
    _HmSecTResBladeCtrlPowerStatus_Type()
)
hmSecTResBladeCtrlPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeCtrlPowerStatus.setStatus("mandatory")


class _HmSecTResBladeCtrlRunStatus_Type(Integer32):
    """Custom type hmSecTResBladeCtrlRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2),
          ("online", 3))
    )


_HmSecTResBladeCtrlRunStatus_Type.__name__ = "Integer32"
_HmSecTResBladeCtrlRunStatus_Object = MibScalar
hmSecTResBladeCtrlRunStatus = _HmSecTResBladeCtrlRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 3),
    _HmSecTResBladeCtrlRunStatus_Type()
)
hmSecTResBladeCtrlRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeCtrlRunStatus.setStatus("mandatory")
_HmSecTResBladeCtrlFailover_Type = DisplayString
_HmSecTResBladeCtrlFailover_Object = MibScalar
hmSecTResBladeCtrlFailover = _HmSecTResBladeCtrlFailover_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 4),
    _HmSecTResBladeCtrlFailover_Type()
)
hmSecTResBladeCtrlFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeCtrlFailover.setStatus("mandatory")
_HmSecTResBladeCtrlCfg_ObjectIdentity = ObjectIdentity
hmSecTResBladeCtrlCfg = _HmSecTResBladeCtrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 5)
)


class _HmSecTResBladeCtrlCfgBackup_Type(Integer32):
    """Custom type hmSecTResBladeCtrlCfgBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("downloaded", 3)
    )


_HmSecTResBladeCtrlCfgBackup_Type.__name__ = "Integer32"
_HmSecTResBladeCtrlCfgBackup_Object = MibScalar
hmSecTResBladeCtrlCfgBackup = _HmSecTResBladeCtrlCfgBackup_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 5, 1),
    _HmSecTResBladeCtrlCfgBackup_Type()
)
hmSecTResBladeCtrlCfgBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeCtrlCfgBackup.setStatus("mandatory")


class _HmSecTResBladeCtrlCfgRestored_Type(Integer32):
    """Custom type hmSecTResBladeCtrlCfgRestored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_HmSecTResBladeCtrlCfgRestored_Type.__name__ = "Integer32"
_HmSecTResBladeCtrlCfgRestored_Object = MibScalar
hmSecTResBladeCtrlCfgRestored = _HmSecTResBladeCtrlCfgRestored_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 7, 2, 5, 2),
    _HmSecTResBladeCtrlCfgRestored_Type()
)
hmSecTResBladeCtrlCfgRestored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResBladeCtrlCfgRestored.setStatus("mandatory")
_HmSecTResRedundancy_ObjectIdentity = ObjectIdentity
hmSecTResRedundancy = _HmSecTResRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 8)
)
_HmSecTResRedundacyReason_Type = DisplayString
_HmSecTResRedundacyReason_Object = MibScalar
hmSecTResRedundacyReason = _HmSecTResRedundacyReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 8, 1),
    _HmSecTResRedundacyReason_Type()
)
hmSecTResRedundacyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResRedundacyReason.setStatus("mandatory")
_HmSecTResRedundacyBackupDown_Type = DisplayString
_HmSecTResRedundacyBackupDown_Object = MibScalar
hmSecTResRedundacyBackupDown = _HmSecTResRedundacyBackupDown_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 4, 8, 2),
    _HmSecTResRedundacyBackupDown_Type()
)
hmSecTResRedundacyBackupDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecTResRedundacyBackupDown.setStatus("mandatory")
_HmSecTraps_ObjectIdentity = ObjectIdentity
hmSecTraps = _HmSecTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 5)
)
_HmSecTrapAV_ObjectIdentity = ObjectIdentity
hmSecTrapAV = _HmSecTrapAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 6)
)
_HmSecTrapPlatformSpecific_ObjectIdentity = ObjectIdentity
hmSecTrapPlatformSpecific = _HmSecTrapPlatformSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7)
)
_HmSecTrapIndustrial_ObjectIdentity = ObjectIdentity
hmSecTrapIndustrial = _HmSecTrapIndustrial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 1)
)
_HmSecTrapBladeCTRL_ObjectIdentity = ObjectIdentity
hmSecTrapBladeCTRL = _HmSecTrapBladeCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2)
)
_HmSecTrapBladeCtrlCfg_ObjectIdentity = ObjectIdentity
hmSecTrapBladeCtrlCfg = _HmSecTrapBladeCtrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2, 5)
)
_HmSecTrapRouterRedundancy_ObjectIdentity = ObjectIdentity
hmSecTrapRouterRedundancy = _HmSecTrapRouterRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 8)
)
_HmSecLogging_ObjectIdentity = ObjectIdentity
hmSecLogging = _HmSecLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 11)
)


class _HmSecLoggingRemoteActivate_Type(Integer32):
    """Custom type hmSecLoggingRemoteActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecLoggingRemoteActivate_Type.__name__ = "Integer32"
_HmSecLoggingRemoteActivate_Object = MibScalar
hmSecLoggingRemoteActivate = _HmSecLoggingRemoteActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 11, 1),
    _HmSecLoggingRemoteActivate_Type()
)
hmSecLoggingRemoteActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLoggingRemoteActivate.setStatus("mandatory")
_HmSecLoggingRemoteIP_Type = IpAddress
_HmSecLoggingRemoteIP_Object = MibScalar
hmSecLoggingRemoteIP = _HmSecLoggingRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 11, 2),
    _HmSecLoggingRemoteIP_Type()
)
hmSecLoggingRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLoggingRemoteIP.setStatus("mandatory")
_HmSecLoggingRemotePort_Type = DisplayString
_HmSecLoggingRemotePort_Object = MibScalar
hmSecLoggingRemotePort = _HmSecLoggingRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 11, 3),
    _HmSecLoggingRemotePort_Type()
)
hmSecLoggingRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecLoggingRemotePort.setStatus("mandatory")
_HmSecContFilt_ObjectIdentity = ObjectIdentity
hmSecContFilt = _HmSecContFilt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12)
)
_HmSecContFiltAVP_ObjectIdentity = ObjectIdentity
hmSecContFiltAVP = _HmSecContFiltAVP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1)
)


class _HmSecContFiltAVPSchedule_Type(Integer32):
    """Custom type hmSecContFiltAVPSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15,
              30,
              60,
              120,
              360,
              720,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("never", 1),
          ("onboot", 2),
          ("quarterhourly", 15),
          ("halfhourly", 30),
          ("hourly", 60),
          ("bihourly", 120),
          ("triplehourly", 360),
          ("sixhourly", 720),
          ("twicedayly", 1440))
    )


_HmSecContFiltAVPSchedule_Type.__name__ = "Integer32"
_HmSecContFiltAVPSchedule_Object = MibScalar
hmSecContFiltAVPSchedule = _HmSecContFiltAVPSchedule_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 1),
    _HmSecContFiltAVPSchedule_Type()
)
hmSecContFiltAVPSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPSchedule.setStatus("mandatory")
_HmSecContFiltAVPServerTable_Object = MibTable
hmSecContFiltAVPServerTable = _HmSecContFiltAVPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerTable.setStatus("mandatory")
_HmSecContFiltAVPServerEntry_Object = MibTableRow
hmSecContFiltAVPServerEntry = _HmSecContFiltAVPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1)
)
hmSecContFiltAVPServerEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecContFiltAVPServerIndex"),
)
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerEntry.setStatus("mandatory")


class _HmSecContFiltAVPServerIndex_Type(Integer32):
    """Custom type hmSecContFiltAVPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecContFiltAVPServerIndex_Type.__name__ = "Integer32"
_HmSecContFiltAVPServerIndex_Object = MibTableColumn
hmSecContFiltAVPServerIndex = _HmSecContFiltAVPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1, 1),
    _HmSecContFiltAVPServerIndex_Type()
)
hmSecContFiltAVPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerIndex.setStatus("mandatory")


class _HmSecContFiltAVPServerProtocol_Type(Integer32):
    """Custom type hmSecContFiltAVPServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("ftp", 2))
    )


_HmSecContFiltAVPServerProtocol_Type.__name__ = "Integer32"
_HmSecContFiltAVPServerProtocol_Object = MibTableColumn
hmSecContFiltAVPServerProtocol = _HmSecContFiltAVPServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1, 2),
    _HmSecContFiltAVPServerProtocol_Type()
)
hmSecContFiltAVPServerProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerProtocol.setStatus("mandatory")
_HmSecContFiltAVPServerURL_Type = DisplayString
_HmSecContFiltAVPServerURL_Object = MibTableColumn
hmSecContFiltAVPServerURL = _HmSecContFiltAVPServerURL_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1, 3),
    _HmSecContFiltAVPServerURL_Type()
)
hmSecContFiltAVPServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerURL.setStatus("mandatory")
_HmSecContFiltAVPServerLogin_Type = DisplayString
_HmSecContFiltAVPServerLogin_Object = MibTableColumn
hmSecContFiltAVPServerLogin = _HmSecContFiltAVPServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1, 4),
    _HmSecContFiltAVPServerLogin_Type()
)
hmSecContFiltAVPServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerLogin.setStatus("mandatory")
_HmSecContFiltAVPServerPassword_Type = DisplayString
_HmSecContFiltAVPServerPassword_Object = MibTableColumn
hmSecContFiltAVPServerPassword = _HmSecContFiltAVPServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1, 5),
    _HmSecContFiltAVPServerPassword_Type()
)
hmSecContFiltAVPServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerPassword.setStatus("mandatory")
_HmSecContFiltAVPServerRowStatus_Type = RowStatus
_HmSecContFiltAVPServerRowStatus_Object = MibTableColumn
hmSecContFiltAVPServerRowStatus = _HmSecContFiltAVPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 2, 1, 6),
    _HmSecContFiltAVPServerRowStatus_Type()
)
hmSecContFiltAVPServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPServerRowStatus.setStatus("mandatory")
_HmSecContFiltAVPHTTPProxy_ObjectIdentity = ObjectIdentity
hmSecContFiltAVPHTTPProxy = _HmSecContFiltAVPHTTPProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 3)
)
_HmSecContFiltAVPHTTPProxyLogin_Type = DisplayString
_HmSecContFiltAVPHTTPProxyLogin_Object = MibScalar
hmSecContFiltAVPHTTPProxyLogin = _HmSecContFiltAVPHTTPProxyLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 3, 1),
    _HmSecContFiltAVPHTTPProxyLogin_Type()
)
hmSecContFiltAVPHTTPProxyLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPHTTPProxyLogin.setStatus("mandatory")
_HmSecContFiltAVPHTTPProxyPasswd_Type = DisplayString
_HmSecContFiltAVPHTTPProxyPasswd_Object = MibScalar
hmSecContFiltAVPHTTPProxyPasswd = _HmSecContFiltAVPHTTPProxyPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 3, 2),
    _HmSecContFiltAVPHTTPProxyPasswd_Type()
)
hmSecContFiltAVPHTTPProxyPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPHTTPProxyPasswd.setStatus("mandatory")
_HmSecContFiltAVPHTTPProxyServer_Type = DisplayString
_HmSecContFiltAVPHTTPProxyServer_Object = MibScalar
hmSecContFiltAVPHTTPProxyServer = _HmSecContFiltAVPHTTPProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 3, 3),
    _HmSecContFiltAVPHTTPProxyServer_Type()
)
hmSecContFiltAVPHTTPProxyServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPHTTPProxyServer.setStatus("mandatory")
_HmSecContFiltAVPHTTPProxyPort_Type = DisplayString
_HmSecContFiltAVPHTTPProxyPort_Object = MibScalar
hmSecContFiltAVPHTTPProxyPort = _HmSecContFiltAVPHTTPProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 3, 4),
    _HmSecContFiltAVPHTTPProxyPort_Type()
)
hmSecContFiltAVPHTTPProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPHTTPProxyPort.setStatus("mandatory")
_HmSecContFiltAVPFTPProxy_ObjectIdentity = ObjectIdentity
hmSecContFiltAVPFTPProxy = _HmSecContFiltAVPFTPProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 4)
)
_HmSecContFiltAVPFTPProxyLogin_Type = DisplayString
_HmSecContFiltAVPFTPProxyLogin_Object = MibScalar
hmSecContFiltAVPFTPProxyLogin = _HmSecContFiltAVPFTPProxyLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 4, 1),
    _HmSecContFiltAVPFTPProxyLogin_Type()
)
hmSecContFiltAVPFTPProxyLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPFTPProxyLogin.setStatus("mandatory")
_HmSecContFiltAVPFTPProxyPasswd_Type = DisplayString
_HmSecContFiltAVPFTPProxyPasswd_Object = MibScalar
hmSecContFiltAVPFTPProxyPasswd = _HmSecContFiltAVPFTPProxyPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 4, 2),
    _HmSecContFiltAVPFTPProxyPasswd_Type()
)
hmSecContFiltAVPFTPProxyPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPFTPProxyPasswd.setStatus("mandatory")
_HmSecContFiltAVPFTPProxyServer_Type = DisplayString
_HmSecContFiltAVPFTPProxyServer_Object = MibScalar
hmSecContFiltAVPFTPProxyServer = _HmSecContFiltAVPFTPProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 4, 3),
    _HmSecContFiltAVPFTPProxyServer_Type()
)
hmSecContFiltAVPFTPProxyServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPFTPProxyServer.setStatus("mandatory")
_HmSecContFiltAVPFTPProxyPort_Type = DisplayString
_HmSecContFiltAVPFTPProxyPort_Object = MibScalar
hmSecContFiltAVPFTPProxyPort = _HmSecContFiltAVPFTPProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 4, 4),
    _HmSecContFiltAVPFTPProxyPort_Type()
)
hmSecContFiltAVPFTPProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPFTPProxyPort.setStatus("mandatory")


class _HmSecContFiltAVPLogLevel_Type(Integer32):
    """Custom type hmSecContFiltAVPLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmSecContFiltAVPLogLevel_Type.__name__ = "Integer32"
_HmSecContFiltAVPLogLevel_Object = MibScalar
hmSecContFiltAVPLogLevel = _HmSecContFiltAVPLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 5),
    _HmSecContFiltAVPLogLevel_Type()
)
hmSecContFiltAVPLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPLogLevel.setStatus("mandatory")
_HmSecContFiltAVPMaxConnections_Type = Integer32
_HmSecContFiltAVPMaxConnections_Object = MibScalar
hmSecContFiltAVPMaxConnections = _HmSecContFiltAVPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 6),
    _HmSecContFiltAVPMaxConnections_Type()
)
hmSecContFiltAVPMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPMaxConnections.setStatus("mandatory")
_HmSecContFiltAVPScanTimeout_Type = Integer32
_HmSecContFiltAVPScanTimeout_Object = MibScalar
hmSecContFiltAVPScanTimeout = _HmSecContFiltAVPScanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 7),
    _HmSecContFiltAVPScanTimeout_Type()
)
hmSecContFiltAVPScanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPScanTimeout.setStatus("mandatory")
_HmSecContFiltAVPpass_ObjectIdentity = ObjectIdentity
hmSecContFiltAVPpass = _HmSecContFiltAVPpass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 8)
)


class _HmSecContFiltAVPpassCorrupt_Type(Integer32):
    """Custom type hmSecContFiltAVPpassCorrupt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltAVPpassCorrupt_Type.__name__ = "Integer32"
_HmSecContFiltAVPpassCorrupt_Object = MibScalar
hmSecContFiltAVPpassCorrupt = _HmSecContFiltAVPpassCorrupt_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 8, 1),
    _HmSecContFiltAVPpassCorrupt_Type()
)
hmSecContFiltAVPpassCorrupt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPpassCorrupt.setStatus("mandatory")


class _HmSecContFiltAVPpassEncrypted_Type(Integer32):
    """Custom type hmSecContFiltAVPpassEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltAVPpassEncrypted_Type.__name__ = "Integer32"
_HmSecContFiltAVPpassEncrypted_Object = MibScalar
hmSecContFiltAVPpassEncrypted = _HmSecContFiltAVPpassEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 8, 2),
    _HmSecContFiltAVPpassEncrypted_Type()
)
hmSecContFiltAVPpassEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPpassEncrypted.setStatus("mandatory")


class _HmSecContFiltAVPpassSuspicious_Type(Integer32):
    """Custom type hmSecContFiltAVPpassSuspicious based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltAVPpassSuspicious_Type.__name__ = "Integer32"
_HmSecContFiltAVPpassSuspicious_Object = MibScalar
hmSecContFiltAVPpassSuspicious = _HmSecContFiltAVPpassSuspicious_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 8, 3),
    _HmSecContFiltAVPpassSuspicious_Type()
)
hmSecContFiltAVPpassSuspicious.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPpassSuspicious.setStatus("mandatory")


class _HmSecContFiltAVPpassWarnings_Type(Integer32):
    """Custom type hmSecContFiltAVPpassWarnings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltAVPpassWarnings_Type.__name__ = "Integer32"
_HmSecContFiltAVPpassWarnings_Object = MibScalar
hmSecContFiltAVPpassWarnings = _HmSecContFiltAVPpassWarnings_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 8, 4),
    _HmSecContFiltAVPpassWarnings_Type()
)
hmSecContFiltAVPpassWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltAVPpassWarnings.setStatus("mandatory")
_HmSecContFiltQuarantine_ObjectIdentity = ObjectIdentity
hmSecContFiltQuarantine = _HmSecContFiltQuarantine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 9)
)


class _HmSecContFiltQuarantineClean_Type(Integer32):
    """Custom type hmSecContFiltQuarantineClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltQuarantineClean_Type.__name__ = "Integer32"
_HmSecContFiltQuarantineClean_Object = MibScalar
hmSecContFiltQuarantineClean = _HmSecContFiltQuarantineClean_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 9, 1),
    _HmSecContFiltQuarantineClean_Type()
)
hmSecContFiltQuarantineClean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltQuarantineClean.setStatus("mandatory")


class _HmSecContFiltQuarantineError_Type(Integer32):
    """Custom type hmSecContFiltQuarantineError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltQuarantineError_Type.__name__ = "Integer32"
_HmSecContFiltQuarantineError_Object = MibScalar
hmSecContFiltQuarantineError = _HmSecContFiltQuarantineError_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 9, 2),
    _HmSecContFiltQuarantineError_Type()
)
hmSecContFiltQuarantineError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltQuarantineError.setStatus("mandatory")


class _HmSecContFiltQuarantineVirus_Type(Integer32):
    """Custom type hmSecContFiltQuarantineVirus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecContFiltQuarantineVirus_Type.__name__ = "Integer32"
_HmSecContFiltQuarantineVirus_Object = MibScalar
hmSecContFiltQuarantineVirus = _HmSecContFiltQuarantineVirus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 9, 3),
    _HmSecContFiltQuarantineVirus_Type()
)
hmSecContFiltQuarantineVirus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltQuarantineVirus.setStatus("mandatory")
_HmSecContFiltQuarantineSrvIP_Type = DisplayString
_HmSecContFiltQuarantineSrvIP_Object = MibScalar
hmSecContFiltQuarantineSrvIP = _HmSecContFiltQuarantineSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 9, 4),
    _HmSecContFiltQuarantineSrvIP_Type()
)
hmSecContFiltQuarantineSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltQuarantineSrvIP.setStatus("mandatory")
_HmSecContFiltQuarantineSrvPort_Type = DisplayString
_HmSecContFiltQuarantineSrvPort_Object = MibScalar
hmSecContFiltQuarantineSrvPort = _HmSecContFiltQuarantineSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 9, 5),
    _HmSecContFiltQuarantineSrvPort_Type()
)
hmSecContFiltQuarantineSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltQuarantineSrvPort.setStatus("mandatory")
_HmSecContFiltInfo_ObjectIdentity = ObjectIdentity
hmSecContFiltInfo = _HmSecContFiltInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 10)
)
_HmSecContFiltInfoFlashID_Type = DisplayString
_HmSecContFiltInfoFlashID_Object = MibScalar
hmSecContFiltInfoFlashID = _HmSecContFiltInfoFlashID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 1, 10, 1),
    _HmSecContFiltInfoFlashID_Type()
)
hmSecContFiltInfoFlashID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecContFiltInfoFlashID.setStatus("mandatory")
_HmSecContFiltHTTP_ObjectIdentity = ObjectIdentity
hmSecContFiltHTTP = _HmSecContFiltHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2)
)


class _HmSecContFiltHTTPEnable_Type(Integer32):
    """Custom type hmSecContFiltHTTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecContFiltHTTPEnable_Type.__name__ = "Integer32"
_HmSecContFiltHTTPEnable_Object = MibScalar
hmSecContFiltHTTPEnable = _HmSecContFiltHTTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 1),
    _HmSecContFiltHTTPEnable_Type()
)
hmSecContFiltHTTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPEnable.setStatus("mandatory")


class _HmSecContFiltHTTPVirusAction_Type(Integer32):
    """Custom type hmSecContFiltHTTPVirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("error", 1)
    )


_HmSecContFiltHTTPVirusAction_Type.__name__ = "Integer32"
_HmSecContFiltHTTPVirusAction_Object = MibScalar
hmSecContFiltHTTPVirusAction = _HmSecContFiltHTTPVirusAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 2),
    _HmSecContFiltHTTPVirusAction_Type()
)
hmSecContFiltHTTPVirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPVirusAction.setStatus("mandatory")


class _HmSecContFiltHTTPMaxSize_Type(Integer32):
    """Custom type hmSecContFiltHTTPMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000)
        )
    )
    namedValues = NamedValues(
        *(("dottwomeg", 200000),
          ("dotfivemeg", 500000),
          ("onemeg", 1000000),
          ("twomeg", 2000000),
          ("fourmeg", 4000000),
          ("fivemeg", 5000000),
          ("eightmeg", 8000000))
    )


_HmSecContFiltHTTPMaxSize_Type.__name__ = "Integer32"
_HmSecContFiltHTTPMaxSize_Object = MibScalar
hmSecContFiltHTTPMaxSize = _HmSecContFiltHTTPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 3),
    _HmSecContFiltHTTPMaxSize_Type()
)
hmSecContFiltHTTPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPMaxSize.setStatus("mandatory")


class _HmSecContFiltHTTPExceedAction_Type(Integer32):
    """Custom type hmSecContFiltHTTPExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_HmSecContFiltHTTPExceedAction_Type.__name__ = "Integer32"
_HmSecContFiltHTTPExceedAction_Object = MibScalar
hmSecContFiltHTTPExceedAction = _HmSecContFiltHTTPExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 4),
    _HmSecContFiltHTTPExceedAction_Type()
)
hmSecContFiltHTTPExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPExceedAction.setStatus("mandatory")
_HmSecContFiltHTTPSrvrTable_Object = MibTable
hmSecContFiltHTTPSrvrTable = _HmSecContFiltHTTPSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5)
)
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrTable.setStatus("mandatory")
_HmSecContFiltHTTPSrvrEntry_Object = MibTableRow
hmSecContFiltHTTPSrvrEntry = _HmSecContFiltHTTPSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1)
)
hmSecContFiltHTTPSrvrEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecContFiltHTTPSrvrIndex"),
)
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrEntry.setStatus("mandatory")


class _HmSecContFiltHTTPSrvrIndex_Type(Integer32):
    """Custom type hmSecContFiltHTTPSrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecContFiltHTTPSrvrIndex_Type.__name__ = "Integer32"
_HmSecContFiltHTTPSrvrIndex_Object = MibTableColumn
hmSecContFiltHTTPSrvrIndex = _HmSecContFiltHTTPSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1, 1),
    _HmSecContFiltHTTPSrvrIndex_Type()
)
hmSecContFiltHTTPSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrIndex.setStatus("mandatory")
_HmSecContFiltHTTPSrvrIP_Type = DisplayString
_HmSecContFiltHTTPSrvrIP_Object = MibTableColumn
hmSecContFiltHTTPSrvrIP = _HmSecContFiltHTTPSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1, 2),
    _HmSecContFiltHTTPSrvrIP_Type()
)
hmSecContFiltHTTPSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrIP.setStatus("mandatory")
_HmSecContFiltHTTPSrvrPort_Type = DisplayString
_HmSecContFiltHTTPSrvrPort_Object = MibTableColumn
hmSecContFiltHTTPSrvrPort = _HmSecContFiltHTTPSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1, 3),
    _HmSecContFiltHTTPSrvrPort_Type()
)
hmSecContFiltHTTPSrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrPort.setStatus("mandatory")


class _HmSecContFiltHTTPSrvrScanAction_Type(Integer32):
    """Custom type hmSecContFiltHTTPSrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scan", 1),
          ("noscan", 2))
    )


_HmSecContFiltHTTPSrvrScanAction_Type.__name__ = "Integer32"
_HmSecContFiltHTTPSrvrScanAction_Object = MibTableColumn
hmSecContFiltHTTPSrvrScanAction = _HmSecContFiltHTTPSrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1, 4),
    _HmSecContFiltHTTPSrvrScanAction_Type()
)
hmSecContFiltHTTPSrvrScanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrScanAction.setStatus("mandatory")
_HmSecContFiltHTTPSrvrRowStatus_Type = RowStatus
_HmSecContFiltHTTPSrvrRowStatus_Object = MibTableColumn
hmSecContFiltHTTPSrvrRowStatus = _HmSecContFiltHTTPSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1, 5),
    _HmSecContFiltHTTPSrvrRowStatus_Type()
)
hmSecContFiltHTTPSrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrRowStatus.setStatus("mandatory")
_HmSecContFiltHTTPSrvrComment_Type = DisplayString
_HmSecContFiltHTTPSrvrComment_Object = MibTableColumn
hmSecContFiltHTTPSrvrComment = _HmSecContFiltHTTPSrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 2, 5, 1, 6),
    _HmSecContFiltHTTPSrvrComment_Type()
)
hmSecContFiltHTTPSrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltHTTPSrvrComment.setStatus("mandatory")
_HmSecContFiltPOP3_ObjectIdentity = ObjectIdentity
hmSecContFiltPOP3 = _HmSecContFiltPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3)
)


class _HmSecContFiltPOP3Enable_Type(Integer32):
    """Custom type hmSecContFiltPOP3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecContFiltPOP3Enable_Type.__name__ = "Integer32"
_HmSecContFiltPOP3Enable_Object = MibScalar
hmSecContFiltPOP3Enable = _HmSecContFiltPOP3Enable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 1),
    _HmSecContFiltPOP3Enable_Type()
)
hmSecContFiltPOP3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3Enable.setStatus("mandatory")


class _HmSecContFiltPOP3VirusAction_Type(Integer32):
    """Custom type hmSecContFiltPOP3VirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("mail", 2))
    )


_HmSecContFiltPOP3VirusAction_Type.__name__ = "Integer32"
_HmSecContFiltPOP3VirusAction_Object = MibScalar
hmSecContFiltPOP3VirusAction = _HmSecContFiltPOP3VirusAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 2),
    _HmSecContFiltPOP3VirusAction_Type()
)
hmSecContFiltPOP3VirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3VirusAction.setStatus("mandatory")


class _HmSecContFiltPOP3MaxSize_Type(Integer32):
    """Custom type hmSecContFiltPOP3MaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000)
        )
    )
    namedValues = NamedValues(
        *(("dottwomeg", 200000),
          ("dotfivemeg", 500000),
          ("onemeg", 1000000),
          ("twomeg", 2000000),
          ("fourmeg", 4000000),
          ("fivemeg", 5000000),
          ("eightmeg", 8000000))
    )


_HmSecContFiltPOP3MaxSize_Type.__name__ = "Integer32"
_HmSecContFiltPOP3MaxSize_Object = MibScalar
hmSecContFiltPOP3MaxSize = _HmSecContFiltPOP3MaxSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 3),
    _HmSecContFiltPOP3MaxSize_Type()
)
hmSecContFiltPOP3MaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3MaxSize.setStatus("mandatory")


class _HmSecContFiltPOP3ExceedAction_Type(Integer32):
    """Custom type hmSecContFiltPOP3ExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_HmSecContFiltPOP3ExceedAction_Type.__name__ = "Integer32"
_HmSecContFiltPOP3ExceedAction_Object = MibScalar
hmSecContFiltPOP3ExceedAction = _HmSecContFiltPOP3ExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 4),
    _HmSecContFiltPOP3ExceedAction_Type()
)
hmSecContFiltPOP3ExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3ExceedAction.setStatus("mandatory")
_HmSecContFiltPOP3SrvrTable_Object = MibTable
hmSecContFiltPOP3SrvrTable = _HmSecContFiltPOP3SrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5)
)
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrTable.setStatus("mandatory")
_HmSecContFiltPOP3SrvrEntry_Object = MibTableRow
hmSecContFiltPOP3SrvrEntry = _HmSecContFiltPOP3SrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1)
)
hmSecContFiltPOP3SrvrEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecContFiltPOP3SrvrIndex"),
)
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrEntry.setStatus("mandatory")


class _HmSecContFiltPOP3SrvrIndex_Type(Integer32):
    """Custom type hmSecContFiltPOP3SrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecContFiltPOP3SrvrIndex_Type.__name__ = "Integer32"
_HmSecContFiltPOP3SrvrIndex_Object = MibTableColumn
hmSecContFiltPOP3SrvrIndex = _HmSecContFiltPOP3SrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1, 1),
    _HmSecContFiltPOP3SrvrIndex_Type()
)
hmSecContFiltPOP3SrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrIndex.setStatus("mandatory")
_HmSecContFiltPOP3SrvrIP_Type = DisplayString
_HmSecContFiltPOP3SrvrIP_Object = MibTableColumn
hmSecContFiltPOP3SrvrIP = _HmSecContFiltPOP3SrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1, 2),
    _HmSecContFiltPOP3SrvrIP_Type()
)
hmSecContFiltPOP3SrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrIP.setStatus("mandatory")
_HmSecContFiltPOP3SrvrPort_Type = DisplayString
_HmSecContFiltPOP3SrvrPort_Object = MibTableColumn
hmSecContFiltPOP3SrvrPort = _HmSecContFiltPOP3SrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1, 3),
    _HmSecContFiltPOP3SrvrPort_Type()
)
hmSecContFiltPOP3SrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrPort.setStatus("mandatory")


class _HmSecContFiltPOP3SrvrScanAction_Type(Integer32):
    """Custom type hmSecContFiltPOP3SrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scan", 1),
          ("noscan", 2))
    )


_HmSecContFiltPOP3SrvrScanAction_Type.__name__ = "Integer32"
_HmSecContFiltPOP3SrvrScanAction_Object = MibTableColumn
hmSecContFiltPOP3SrvrScanAction = _HmSecContFiltPOP3SrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1, 4),
    _HmSecContFiltPOP3SrvrScanAction_Type()
)
hmSecContFiltPOP3SrvrScanAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrScanAction.setStatus("mandatory")
_HmSecContFiltPOP3SrvrRowStatus_Type = RowStatus
_HmSecContFiltPOP3SrvrRowStatus_Object = MibTableColumn
hmSecContFiltPOP3SrvrRowStatus = _HmSecContFiltPOP3SrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1, 5),
    _HmSecContFiltPOP3SrvrRowStatus_Type()
)
hmSecContFiltPOP3SrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrRowStatus.setStatus("mandatory")
_HmSecContFiltPOP3SrvrComment_Type = DisplayString
_HmSecContFiltPOP3SrvrComment_Object = MibTableColumn
hmSecContFiltPOP3SrvrComment = _HmSecContFiltPOP3SrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 3, 5, 1, 6),
    _HmSecContFiltPOP3SrvrComment_Type()
)
hmSecContFiltPOP3SrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltPOP3SrvrComment.setStatus("mandatory")
_HmSecContFiltSMTP_ObjectIdentity = ObjectIdentity
hmSecContFiltSMTP = _HmSecContFiltSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4)
)


class _HmSecContFiltSMTPEnable_Type(Integer32):
    """Custom type hmSecContFiltSMTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecContFiltSMTPEnable_Type.__name__ = "Integer32"
_HmSecContFiltSMTPEnable_Object = MibScalar
hmSecContFiltSMTPEnable = _HmSecContFiltSMTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 1),
    _HmSecContFiltSMTPEnable_Type()
)
hmSecContFiltSMTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPEnable.setStatus("mandatory")


class _HmSecContFiltSMTPVirusAction_Type(Integer32):
    """Custom type hmSecContFiltSMTPVirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("error", 1)
    )


_HmSecContFiltSMTPVirusAction_Type.__name__ = "Integer32"
_HmSecContFiltSMTPVirusAction_Object = MibScalar
hmSecContFiltSMTPVirusAction = _HmSecContFiltSMTPVirusAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 2),
    _HmSecContFiltSMTPVirusAction_Type()
)
hmSecContFiltSMTPVirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPVirusAction.setStatus("mandatory")


class _HmSecContFiltSMTPMaxSize_Type(Integer32):
    """Custom type hmSecContFiltSMTPMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000)
        )
    )
    namedValues = NamedValues(
        *(("dottwomeg", 200000),
          ("dotfivemeg", 500000),
          ("onemeg", 1000000),
          ("twomeg", 2000000),
          ("fourmeg", 4000000),
          ("fivemeg", 5000000),
          ("eightmeg", 8000000))
    )


_HmSecContFiltSMTPMaxSize_Type.__name__ = "Integer32"
_HmSecContFiltSMTPMaxSize_Object = MibScalar
hmSecContFiltSMTPMaxSize = _HmSecContFiltSMTPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 3),
    _HmSecContFiltSMTPMaxSize_Type()
)
hmSecContFiltSMTPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPMaxSize.setStatus("mandatory")


class _HmSecContFiltSMTPExceedAction_Type(Integer32):
    """Custom type hmSecContFiltSMTPExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_HmSecContFiltSMTPExceedAction_Type.__name__ = "Integer32"
_HmSecContFiltSMTPExceedAction_Object = MibScalar
hmSecContFiltSMTPExceedAction = _HmSecContFiltSMTPExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 4),
    _HmSecContFiltSMTPExceedAction_Type()
)
hmSecContFiltSMTPExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPExceedAction.setStatus("mandatory")
_HmSecContFiltSMTPSrvrTable_Object = MibTable
hmSecContFiltSMTPSrvrTable = _HmSecContFiltSMTPSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5)
)
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrTable.setStatus("mandatory")
_HmSecContFiltSMTPSrvrEntry_Object = MibTableRow
hmSecContFiltSMTPSrvrEntry = _HmSecContFiltSMTPSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1)
)
hmSecContFiltSMTPSrvrEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecContFiltSMTPSrvrIndex"),
)
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrEntry.setStatus("mandatory")


class _HmSecContFiltSMTPSrvrIndex_Type(Integer32):
    """Custom type hmSecContFiltSMTPSrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecContFiltSMTPSrvrIndex_Type.__name__ = "Integer32"
_HmSecContFiltSMTPSrvrIndex_Object = MibTableColumn
hmSecContFiltSMTPSrvrIndex = _HmSecContFiltSMTPSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1, 1),
    _HmSecContFiltSMTPSrvrIndex_Type()
)
hmSecContFiltSMTPSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrIndex.setStatus("mandatory")
_HmSecContFiltSMTPSrvrIP_Type = DisplayString
_HmSecContFiltSMTPSrvrIP_Object = MibTableColumn
hmSecContFiltSMTPSrvrIP = _HmSecContFiltSMTPSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1, 2),
    _HmSecContFiltSMTPSrvrIP_Type()
)
hmSecContFiltSMTPSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrIP.setStatus("mandatory")
_HmSecContFiltSMTPSrvrPort_Type = DisplayString
_HmSecContFiltSMTPSrvrPort_Object = MibTableColumn
hmSecContFiltSMTPSrvrPort = _HmSecContFiltSMTPSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1, 3),
    _HmSecContFiltSMTPSrvrPort_Type()
)
hmSecContFiltSMTPSrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrPort.setStatus("mandatory")


class _HmSecContFiltSMTPSrvrScanAction_Type(Integer32):
    """Custom type hmSecContFiltSMTPSrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scan", 1),
          ("noscan", 2))
    )


_HmSecContFiltSMTPSrvrScanAction_Type.__name__ = "Integer32"
_HmSecContFiltSMTPSrvrScanAction_Object = MibTableColumn
hmSecContFiltSMTPSrvrScanAction = _HmSecContFiltSMTPSrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1, 4),
    _HmSecContFiltSMTPSrvrScanAction_Type()
)
hmSecContFiltSMTPSrvrScanAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrScanAction.setStatus("mandatory")
_HmSecContFiltSMTPSrvrRowStatus_Type = RowStatus
_HmSecContFiltSMTPSrvrRowStatus_Object = MibTableColumn
hmSecContFiltSMTPSrvrRowStatus = _HmSecContFiltSMTPSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1, 5),
    _HmSecContFiltSMTPSrvrRowStatus_Type()
)
hmSecContFiltSMTPSrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrRowStatus.setStatus("mandatory")
_HmSecContFiltSMTPSrvrComment_Type = DisplayString
_HmSecContFiltSMTPSrvrComment_Object = MibTableColumn
hmSecContFiltSMTPSrvrComment = _HmSecContFiltSMTPSrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 4, 5, 1, 6),
    _HmSecContFiltSMTPSrvrComment_Type()
)
hmSecContFiltSMTPSrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltSMTPSrvrComment.setStatus("mandatory")
_HmSecContFiltFTP_ObjectIdentity = ObjectIdentity
hmSecContFiltFTP = _HmSecContFiltFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5)
)


class _HmSecContFiltFTPEnable_Type(Integer32):
    """Custom type hmSecContFiltFTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmSecContFiltFTPEnable_Type.__name__ = "Integer32"
_HmSecContFiltFTPEnable_Object = MibScalar
hmSecContFiltFTPEnable = _HmSecContFiltFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 1),
    _HmSecContFiltFTPEnable_Type()
)
hmSecContFiltFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPEnable.setStatus("mandatory")


class _HmSecContFiltFTPVirusAction_Type(Integer32):
    """Custom type hmSecContFiltFTPVirusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("error", 1)
    )


_HmSecContFiltFTPVirusAction_Type.__name__ = "Integer32"
_HmSecContFiltFTPVirusAction_Object = MibScalar
hmSecContFiltFTPVirusAction = _HmSecContFiltFTPVirusAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 2),
    _HmSecContFiltFTPVirusAction_Type()
)
hmSecContFiltFTPVirusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPVirusAction.setStatus("mandatory")


class _HmSecContFiltFTPMaxSize_Type(Integer32):
    """Custom type hmSecContFiltFTPMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200000,
              500000,
              1000000,
              2000000,
              4000000,
              5000000,
              8000000)
        )
    )
    namedValues = NamedValues(
        *(("dottwomeg", 200000),
          ("dotfivemeg", 500000),
          ("onemeg", 1000000),
          ("twomeg", 2000000),
          ("fourmeg", 4000000),
          ("fivemeg", 5000000),
          ("eightmeg", 8000000))
    )


_HmSecContFiltFTPMaxSize_Type.__name__ = "Integer32"
_HmSecContFiltFTPMaxSize_Object = MibScalar
hmSecContFiltFTPMaxSize = _HmSecContFiltFTPMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 3),
    _HmSecContFiltFTPMaxSize_Type()
)
hmSecContFiltFTPMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPMaxSize.setStatus("mandatory")


class _HmSecContFiltFTPExceedAction_Type(Integer32):
    """Custom type hmSecContFiltFTPExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_HmSecContFiltFTPExceedAction_Type.__name__ = "Integer32"
_HmSecContFiltFTPExceedAction_Object = MibScalar
hmSecContFiltFTPExceedAction = _HmSecContFiltFTPExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 4),
    _HmSecContFiltFTPExceedAction_Type()
)
hmSecContFiltFTPExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPExceedAction.setStatus("mandatory")
_HmSecContFiltFTPSrvrTable_Object = MibTable
hmSecContFiltFTPSrvrTable = _HmSecContFiltFTPSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5)
)
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrTable.setStatus("mandatory")
_HmSecContFiltFTPSrvrEntry_Object = MibTableRow
hmSecContFiltFTPSrvrEntry = _HmSecContFiltFTPSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1)
)
hmSecContFiltFTPSrvrEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecContFiltFTPSrvrIndex"),
)
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrEntry.setStatus("mandatory")


class _HmSecContFiltFTPSrvrIndex_Type(Integer32):
    """Custom type hmSecContFiltFTPSrvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecContFiltFTPSrvrIndex_Type.__name__ = "Integer32"
_HmSecContFiltFTPSrvrIndex_Object = MibTableColumn
hmSecContFiltFTPSrvrIndex = _HmSecContFiltFTPSrvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1, 1),
    _HmSecContFiltFTPSrvrIndex_Type()
)
hmSecContFiltFTPSrvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrIndex.setStatus("mandatory")
_HmSecContFiltFTPSrvrIP_Type = DisplayString
_HmSecContFiltFTPSrvrIP_Object = MibTableColumn
hmSecContFiltFTPSrvrIP = _HmSecContFiltFTPSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1, 2),
    _HmSecContFiltFTPSrvrIP_Type()
)
hmSecContFiltFTPSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrIP.setStatus("mandatory")
_HmSecContFiltFTPSrvrPort_Type = DisplayString
_HmSecContFiltFTPSrvrPort_Object = MibTableColumn
hmSecContFiltFTPSrvrPort = _HmSecContFiltFTPSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1, 3),
    _HmSecContFiltFTPSrvrPort_Type()
)
hmSecContFiltFTPSrvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrPort.setStatus("mandatory")


class _HmSecContFiltFTPSrvrScanAction_Type(Integer32):
    """Custom type hmSecContFiltFTPSrvrScanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scan", 1),
          ("noscan", 2))
    )


_HmSecContFiltFTPSrvrScanAction_Type.__name__ = "Integer32"
_HmSecContFiltFTPSrvrScanAction_Object = MibTableColumn
hmSecContFiltFTPSrvrScanAction = _HmSecContFiltFTPSrvrScanAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1, 4),
    _HmSecContFiltFTPSrvrScanAction_Type()
)
hmSecContFiltFTPSrvrScanAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrScanAction.setStatus("mandatory")
_HmSecContFiltFTPSrvrRowStatus_Type = RowStatus
_HmSecContFiltFTPSrvrRowStatus_Object = MibTableColumn
hmSecContFiltFTPSrvrRowStatus = _HmSecContFiltFTPSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1, 5),
    _HmSecContFiltFTPSrvrRowStatus_Type()
)
hmSecContFiltFTPSrvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrRowStatus.setStatus("mandatory")
_HmSecContFiltFTPSrvrComment_Type = DisplayString
_HmSecContFiltFTPSrvrComment_Object = MibTableColumn
hmSecContFiltFTPSrvrComment = _HmSecContFiltFTPSrvrComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 12, 5, 5, 1, 6),
    _HmSecContFiltFTPSrvrComment_Type()
)
hmSecContFiltFTPSrvrComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecContFiltFTPSrvrComment.setStatus("mandatory")
_HmSecBlade_ObjectIdentity = ObjectIdentity
hmSecBlade = _HmSecBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 13)
)
_HmSecBladeRackID_Type = Integer32
_HmSecBladeRackID_Object = MibScalar
hmSecBladeRackID = _HmSecBladeRackID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 1),
    _HmSecBladeRackID_Type()
)
hmSecBladeRackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecBladeRackID.setStatus("mandatory")
_HmSecBladeSlotID_Type = Integer32
_HmSecBladeSlotID_Object = MibScalar
hmSecBladeSlotID = _HmSecBladeSlotID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 2),
    _HmSecBladeSlotID_Type()
)
hmSecBladeSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecBladeSlotID.setStatus("mandatory")
_HmSecBladeCtrlTable_Object = MibTable
hmSecBladeCtrlTable = _HmSecBladeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3)
)
if mibBuilder.loadTexts:
    hmSecBladeCtrlTable.setStatus("mandatory")
_HmSecBladeCtrlEntry_Object = MibTableRow
hmSecBladeCtrlEntry = _HmSecBladeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1)
)
hmSecBladeCtrlEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecBladeCtrlIndex"),
)
if mibBuilder.loadTexts:
    hmSecBladeCtrlEntry.setStatus("mandatory")


class _HmSecBladeCtrlIndex_Type(Integer32):
    """Custom type hmSecBladeCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecBladeCtrlIndex_Type.__name__ = "Integer32"
_HmSecBladeCtrlIndex_Object = MibTableColumn
hmSecBladeCtrlIndex = _HmSecBladeCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 1),
    _HmSecBladeCtrlIndex_Type()
)
hmSecBladeCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecBladeCtrlIndex.setStatus("mandatory")
_HmSecBladeCtrlDevice_Type = DisplayString
_HmSecBladeCtrlDevice_Object = MibTableColumn
hmSecBladeCtrlDevice = _HmSecBladeCtrlDevice_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 2),
    _HmSecBladeCtrlDevice_Type()
)
hmSecBladeCtrlDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlDevice.setStatus("mandatory")


class _HmSecBladeCtrlStatus_Type(Integer32):
    """Custom type hmSecBladeCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2),
          ("online", 3))
    )


_HmSecBladeCtrlStatus_Type.__name__ = "Integer32"
_HmSecBladeCtrlStatus_Object = MibTableColumn
hmSecBladeCtrlStatus = _HmSecBladeCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 3),
    _HmSecBladeCtrlStatus_Type()
)
hmSecBladeCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlStatus.setStatus("mandatory")
_HmSecBladeCtrlAVRRevision_Type = DisplayString
_HmSecBladeCtrlAVRRevision_Object = MibTableColumn
hmSecBladeCtrlAVRRevision = _HmSecBladeCtrlAVRRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 4),
    _HmSecBladeCtrlAVRRevision_Type()
)
hmSecBladeCtrlAVRRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlAVRRevision.setStatus("mandatory")
_HmSecBladeCtrlSlotID_Type = DisplayString
_HmSecBladeCtrlSlotID_Object = MibTableColumn
hmSecBladeCtrlSlotID = _HmSecBladeCtrlSlotID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 5),
    _HmSecBladeCtrlSlotID_Type()
)
hmSecBladeCtrlSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlSlotID.setStatus("mandatory")
_HmSecBladeCtrlProductID_Type = DisplayString
_HmSecBladeCtrlProductID_Object = MibTableColumn
hmSecBladeCtrlProductID = _HmSecBladeCtrlProductID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 6),
    _HmSecBladeCtrlProductID_Type()
)
hmSecBladeCtrlProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlProductID.setStatus("mandatory")
_HmSecBladeCtrlAssemblyID_Type = DisplayString
_HmSecBladeCtrlAssemblyID_Object = MibTableColumn
hmSecBladeCtrlAssemblyID = _HmSecBladeCtrlAssemblyID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 7),
    _HmSecBladeCtrlAssemblyID_Type()
)
hmSecBladeCtrlAssemblyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlAssemblyID.setStatus("mandatory")
_HmSecBladeCtrlSerial_Type = DisplayString
_HmSecBladeCtrlSerial_Object = MibTableColumn
hmSecBladeCtrlSerial = _HmSecBladeCtrlSerial_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 8),
    _HmSecBladeCtrlSerial_Type()
)
hmSecBladeCtrlSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlSerial.setStatus("mandatory")
_HmSecBladeCtrlFlashID_Type = DisplayString
_HmSecBladeCtrlFlashID_Object = MibTableColumn
hmSecBladeCtrlFlashID = _HmSecBladeCtrlFlashID_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 9),
    _HmSecBladeCtrlFlashID_Type()
)
hmSecBladeCtrlFlashID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlFlashID.setStatus("mandatory")
_HmSecBladeCtrlVersion_Type = DisplayString
_HmSecBladeCtrlVersion_Object = MibTableColumn
hmSecBladeCtrlVersion = _HmSecBladeCtrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 10),
    _HmSecBladeCtrlVersion_Type()
)
hmSecBladeCtrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladeCtrlVersion.setStatus("mandatory")


class _HmSecBladeCtrlBackup_Type(Integer32):
    """Custom type hmSecBladeCtrlBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecBladeCtrlBackup_Type.__name__ = "Integer32"
_HmSecBladeCtrlBackup_Object = MibTableColumn
hmSecBladeCtrlBackup = _HmSecBladeCtrlBackup_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 11),
    _HmSecBladeCtrlBackup_Type()
)
hmSecBladeCtrlBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecBladeCtrlBackup.setStatus("mandatory")


class _HmSecBladeCtrlReconfig_Type(Integer32):
    """Custom type hmSecBladeCtrlReconfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HmSecBladeCtrlReconfig_Type.__name__ = "Integer32"
_HmSecBladeCtrlReconfig_Object = MibScalar
hmSecBladeCtrlReconfig = _HmSecBladeCtrlReconfig_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 3, 1, 12),
    _HmSecBladeCtrlReconfig_Type()
)
hmSecBladeCtrlReconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecBladeCtrlReconfig.setStatus("mandatory")
_HmSecBladePwrTable_Object = MibTable
hmSecBladePwrTable = _HmSecBladePwrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 4)
)
if mibBuilder.loadTexts:
    hmSecBladePwrTable.setStatus("mandatory")
_HmSecBladePwrEntry_Object = MibTableRow
hmSecBladePwrEntry = _HmSecBladePwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 4, 1)
)
hmSecBladePwrEntry.setIndexNames(
    (0, "HmSecurityGateway-MIB", "hmSecBladePwrIndex"),
)
if mibBuilder.loadTexts:
    hmSecBladePwrEntry.setStatus("mandatory")


class _HmSecBladePwrIndex_Type(Integer32):
    """Custom type hmSecBladePwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSecBladePwrIndex_Type.__name__ = "Integer32"
_HmSecBladePwrIndex_Object = MibTableColumn
hmSecBladePwrIndex = _HmSecBladePwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 4, 1, 1),
    _HmSecBladePwrIndex_Type()
)
hmSecBladePwrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSecBladePwrIndex.setStatus("mandatory")


class _HmSecBladePwrStatus_Type(Integer32):
    """Custom type hmSecBladePwrStatus based on Integer32"""
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
        *(("absent", 1),
          ("fatal", 2),
          ("defect", 3),
          ("ok", 4))
    )


_HmSecBladePwrStatus_Type.__name__ = "Integer32"
_HmSecBladePwrStatus_Object = MibTableColumn
hmSecBladePwrStatus = _HmSecBladePwrStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 13, 4, 1, 2),
    _HmSecBladePwrStatus_Type()
)
hmSecBladePwrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSecBladePwrStatus.setStatus("mandatory")
_HmSecProfile_ObjectIdentity = ObjectIdentity
hmSecProfile = _HmSecProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 14)
)
_HmSecProfilePush_ObjectIdentity = ObjectIdentity
hmSecProfilePush = _HmSecProfilePush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 1)
)
_HmSecProfilePull_ObjectIdentity = ObjectIdentity
hmSecProfilePull = _HmSecProfilePull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2)
)


class _HmSecProfilePullSchedule_Type(Integer32):
    """Custom type hmSecProfilePullSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15,
              30,
              60,
              120,
              360,
              720,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("never", 1),
          ("onboot", 2),
          ("quarterhourly", 15),
          ("halfhourly", 30),
          ("hourly", 60),
          ("bihourly", 120),
          ("triplehourly", 360),
          ("sixhourly", 720),
          ("twicedayly", 1440))
    )


_HmSecProfilePullSchedule_Type.__name__ = "Integer32"
_HmSecProfilePullSchedule_Object = MibScalar
hmSecProfilePullSchedule = _HmSecProfilePullSchedule_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 1),
    _HmSecProfilePullSchedule_Type()
)
hmSecProfilePullSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullSchedule.setStatus("mandatory")
_HmSecProfilePullHTTPS_ObjectIdentity = ObjectIdentity
hmSecProfilePullHTTPS = _HmSecProfilePullHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2)
)
_HmSecProfilePullHTTPSCert_Type = DisplayString
_HmSecProfilePullHTTPSCert_Object = MibScalar
hmSecProfilePullHTTPSCert = _HmSecProfilePullHTTPSCert_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 1),
    _HmSecProfilePullHTTPSCert_Type()
)
hmSecProfilePullHTTPSCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSCert.setStatus("mandatory")
_HmSecProfilePullHTTPSServer_Type = DisplayString
_HmSecProfilePullHTTPSServer_Object = MibScalar
hmSecProfilePullHTTPSServer = _HmSecProfilePullHTTPSServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 2),
    _HmSecProfilePullHTTPSServer_Type()
)
hmSecProfilePullHTTPSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSServer.setStatus("mandatory")
_HmSecProfilePullHTTPSPort_Type = DisplayString
_HmSecProfilePullHTTPSPort_Object = MibScalar
hmSecProfilePullHTTPSPort = _HmSecProfilePullHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 3),
    _HmSecProfilePullHTTPSPort_Type()
)
hmSecProfilePullHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSPort.setStatus("mandatory")
_HmSecProfilePullHTTPSFile_Type = DisplayString
_HmSecProfilePullHTTPSFile_Object = MibScalar
hmSecProfilePullHTTPSFile = _HmSecProfilePullHTTPSFile_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 4),
    _HmSecProfilePullHTTPSFile_Type()
)
hmSecProfilePullHTTPSFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSFile.setStatus("mandatory")
_HmSecProfilePullHTTPSLogin_Type = DisplayString
_HmSecProfilePullHTTPSLogin_Object = MibScalar
hmSecProfilePullHTTPSLogin = _HmSecProfilePullHTTPSLogin_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 5),
    _HmSecProfilePullHTTPSLogin_Type()
)
hmSecProfilePullHTTPSLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSLogin.setStatus("mandatory")
_HmSecProfilePullHTTPSPasswd_Type = DisplayString
_HmSecProfilePullHTTPSPasswd_Object = MibScalar
hmSecProfilePullHTTPSPasswd = _HmSecProfilePullHTTPSPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 6),
    _HmSecProfilePullHTTPSPasswd_Type()
)
hmSecProfilePullHTTPSPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSPasswd.setStatus("mandatory")
_HmSecProfilePullHTTPSDirectory_Type = DisplayString
_HmSecProfilePullHTTPSDirectory_Object = MibScalar
hmSecProfilePullHTTPSDirectory = _HmSecProfilePullHTTPSDirectory_Object(
    (1, 3, 6, 1, 4, 1, 248, 51, 14, 2, 2, 7),
    _HmSecProfilePullHTTPSDirectory_Type()
)
hmSecProfilePullHTTPSDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSecProfilePullHTTPSDirectory.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hmSecHTTPSLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 0, 1)
)
hmSecHTTPSLoginTrap.setObjects(
    ("HmSecurityGateway-MIB", "hmSecHTTPSLastAccessIP")
)
if mibBuilder.loadTexts:
    hmSecHTTPSLoginTrap.setStatus(
        ""
    )

hmSecShellLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 0, 2)
)
hmSecShellLoginTrap.setObjects(
    ("HmSecurityGateway-MIB", "hmSecShellLastAccessIP")
)
if mibBuilder.loadTexts:
    hmSecShellLoginTrap.setStatus(
        ""
    )

hmSecDHCPNewClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 0, 3)
)
hmSecDHCPNewClientTrap.setObjects(
    ("HmSecurityGateway-MIB", "hmSecDHCPLastAccessMAC")
)
if mibBuilder.loadTexts:
    hmSecDHCPNewClientTrap.setStatus(
        ""
    )

hmSecTrapDiscFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 5, 0, 1)
)
hmSecTrapDiscFull.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResDiscFull")
)
if mibBuilder.loadTexts:
    hmSecTrapDiscFull.setStatus(
        ""
    )

hmSecTrapCpuLoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 5, 0, 2)
)
hmSecTrapCpuLoadHigh.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResCpuLoadHigh")
)
if mibBuilder.loadTexts:
    hmSecTrapCpuLoadHigh.setStatus(
        ""
    )

hmSecTrapMemoryFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 5, 0, 3)
)
hmSecTrapMemoryFull.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResMemoryFull")
)
if mibBuilder.loadTexts:
    hmSecTrapMemoryFull.setStatus(
        ""
    )

hmSecTrapColdstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 5, 0, 4)
)
hmSecTrapColdstart.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResColdstart")
)
if mibBuilder.loadTexts:
    hmSecTrapColdstart.setStatus(
        ""
    )

hmSecTrapAvUpdateDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 6, 0, 1)
)
hmSecTrapAvUpdateDone.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResAvUpdateDone")
)
if mibBuilder.loadTexts:
    hmSecTrapAvUpdateDone.setStatus(
        ""
    )

hmSecTrapAvUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 6, 0, 2)
)
hmSecTrapAvUpdateError.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResAvUpdateError")
)
if mibBuilder.loadTexts:
    hmSecTrapAvUpdateError.setStatus(
        ""
    )

hmSecTrapAvVirusDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 6, 0, 3)
)
hmSecTrapAvVirusDetected.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResAvVirusDetected")
)
if mibBuilder.loadTexts:
    hmSecTrapAvVirusDetected.setStatus(
        ""
    )

hmSecTrapAvFileNotScanned = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 6, 0, 4)
)
hmSecTrapAvFileNotScanned.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResAvFileNotScanned")
)
if mibBuilder.loadTexts:
    hmSecTrapAvFileNotScanned.setStatus(
        ""
    )

hmSecTrapAvFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 6, 0, 5)
)
hmSecTrapAvFailed.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResAvFailed")
)
if mibBuilder.loadTexts:
    hmSecTrapAvFailed.setStatus(
        ""
    )

hmSecTrapIndustrialTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 1, 0, 1)
)
hmSecTrapIndustrialTemperature.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecSystemTemperature"),
        ("HmSecurityGateway-MIB", "hmSecTResIndustrialTempHiLimit"),
        ("HmSecurityGateway-MIB", "hmSecTResIndustrialTempLowLimit"))
)
if mibBuilder.loadTexts:
    hmSecTrapIndustrialTemperature.setStatus(
        ""
    )

hmSecTrapIndustrialPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 1, 0, 2)
)
hmSecTrapIndustrialPowerStatus.setObjects(
    ("HmSecurityGateway-MIB", "hmSecPSState")
)
if mibBuilder.loadTexts:
    hmSecTrapIndustrialPowerStatus.setStatus(
        ""
    )

hmSecTrapSignalRelais = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 1, 0, 3)
)
hmSecTrapSignalRelais.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecTResSignalRelaisState"),
        ("HmSecurityGateway-MIB", "hmSecTResSignalRelaisReason"),
        ("HmSecurityGateway-MIB", "hmSecTResSignalRelaisReasonIdx"))
)
if mibBuilder.loadTexts:
    hmSecTrapSignalRelais.setStatus(
        ""
    )

hmSecTrapAutoConfigAdapterState = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 1, 0, 4)
)
hmSecTrapAutoConfigAdapterState.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResAutoConfigAdapterState")
)
if mibBuilder.loadTexts:
    hmSecTrapAutoConfigAdapterState.setStatus(
        ""
    )

hmSecTrapBladeCtrlPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2, 0, 2)
)
hmSecTrapBladeCtrlPowerStatus.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecTResBladeRackID"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeSlotNr"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeCtrlPowerStatus"))
)
if mibBuilder.loadTexts:
    hmSecTrapBladeCtrlPowerStatus.setStatus(
        ""
    )

hmSecTrapBladeCtrlRunStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2, 0, 3)
)
hmSecTrapBladeCtrlRunStatus.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecTResBladeRackID"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeSlotNr"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeCtrlRunStatus"))
)
if mibBuilder.loadTexts:
    hmSecTrapBladeCtrlRunStatus.setStatus(
        ""
    )

hmSecTrapBladeCtrlFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2, 0, 4)
)
hmSecTrapBladeCtrlFailover.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecTResBladeRackID"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeSlotNr"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeCtrlFailover"))
)
if mibBuilder.loadTexts:
    hmSecTrapBladeCtrlFailover.setStatus(
        ""
    )

hmSecTrapBladeCtrlCfgBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2, 5, 0, 1)
)
hmSecTrapBladeCtrlCfgBackup.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecTResBladeRackID"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeSlotNr"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeCtrlCfgBackup"))
)
if mibBuilder.loadTexts:
    hmSecTrapBladeCtrlCfgBackup.setStatus(
        ""
    )

hmSecTrapBladeCtrlCfgRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 7, 2, 5, 0, 2)
)
hmSecTrapBladeCtrlCfgRestored.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecTResBladeRackID"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeSlotNr"),
        ("HmSecurityGateway-MIB", "hmSecTResBladeCtrlCfgRestored"))
)
if mibBuilder.loadTexts:
    hmSecTrapBladeCtrlCfgRestored.setStatus(
        ""
    )

hmSecTrapRouterRedundancyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 8, 0, 1)
)
hmSecTrapRouterRedundancyStatusChange.setObjects(
      *(("HmSecurityGateway-MIB", "hmSecRouterRedundancyState"),
        ("HmSecurityGateway-MIB", "hmSecTResRedundacyReason"))
)
if mibBuilder.loadTexts:
    hmSecTrapRouterRedundancyStatusChange.setStatus(
        ""
    )

hmSecTrapRouterRedundancyBackupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 51, 10, 8, 0, 2)
)
hmSecTrapRouterRedundancyBackupDown.setObjects(
    ("HmSecurityGateway-MIB", "hmSecTResRedundacyBackupDown")
)
if mibBuilder.loadTexts:
    hmSecTrapRouterRedundancyBackupDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HmSecurityGateway-MIB",
    **{"hirschmann": hirschmann,
       "hmSecurityGateway": hmSecurityGateway,
       "hmSecHTTPSLoginTrap": hmSecHTTPSLoginTrap,
       "hmSecShellLoginTrap": hmSecShellLoginTrap,
       "hmSecDHCPNewClientTrap": hmSecDHCPNewClientTrap,
       "hmSecVPN": hmSecVPN,
       "hmSecVPNMachine": hmSecVPNMachine,
       "hmSecVPNMachineCert": hmSecVPNMachineCert,
       "hmSecVPNMachinePrivate": hmSecVPNMachinePrivate,
       "hmSecVPNConnectionTable": hmSecVPNConnectionTable,
       "hmSecVPNConnectionEntry": hmSecVPNConnectionEntry,
       "hmSecVPNconIndex": hmSecVPNconIndex,
       "hmSecVPNconName": hmSecVPNconName,
       "hmSecVPNconEnabled": hmSecVPNconEnabled,
       "hmSecVPNremGW": hmSecVPNremGW,
       "hmSecVPNconType": hmSecVPNconType,
       "hmSecVPNlocalNet": hmSecVPNlocalNet,
       "hmSecVPNlocalMask": hmSecVPNlocalMask,
       "hmSecVPNremoteNet": hmSecVPNremoteNet,
       "hmSecVPNremoteMask": hmSecVPNremoteMask,
       "hmSecVPNauthType": hmSecVPNauthType,
       "hmSecVPNpsk": hmSecVPNpsk,
       "hmSecVPNx509": hmSecVPNx509,
       "hmSecVPNikeDH": hmSecVPNikeDH,
       "hmSecVPNikeHash": hmSecVPNikeHash,
       "hmSecVPNipsecHash": hmSecVPNipsecHash,
       "hmSecVPNikeAlg": hmSecVPNikeAlg,
       "hmSecVPNipsecAlg": hmSecVPNipsecAlg,
       "hmSecVPNpfs": hmSecVPNpfs,
       "hmSecVPNconStartUp": hmSecVPNconStartUp,
       "hmSecVPNvirtIPMethod": hmSecVPNvirtIPMethod,
       "hmSecVPNvirtIP": hmSecVPNvirtIP,
       "hmSecVPNFWLogDefIn": hmSecVPNFWLogDefIn,
       "hmSecVPNFWLogDefOut": hmSecVPNFWLogDefOut,
       "hmSecVPNProtoAH": hmSecVPNProtoAH,
       "hmSecVPNProtoESP": hmSecVPNProtoESP,
       "hmSecVPNComp": hmSecVPNComp,
       "hmSecVPNLocalIDMode": hmSecVPNLocalIDMode,
       "hmSecVPNLocalID": hmSecVPNLocalID,
       "hmSecVPNRemoteIDMode": hmSecVPNRemoteIDMode,
       "hmSecVPNRemoteID": hmSecVPNRemoteID,
       "hmSecVPNIkeLifetime": hmSecVPNIkeLifetime,
       "hmSecVPNIpsecLifetime": hmSecVPNIpsecLifetime,
       "hmSecVPNRekeyMargin": hmSecVPNRekeyMargin,
       "hmSecVPNRekeyFuzz": hmSecVPNRekeyFuzz,
       "hmSecVPNKeyingTries": hmSecVPNKeyingTries,
       "hmSecVPNRekey": hmSecVPNRekey,
       "hmSecVPNDPDAction": hmSecVPNDPDAction,
       "hmSecVPNDPDDelay": hmSecVPNDPDDelay,
       "hmSecVPNDPDTimeout": hmSecVPNDPDTimeout,
       "hmSecVPNRowStatus": hmSecVPNRowStatus,
       "hmSecVPNAggressive": hmSecVPNAggressive,
       "hmSecVPNlocal": hmSecVPNlocal,
       "hmSecVPNremote": hmSecVPNremote,
       "hmSecVPNFW": hmSecVPNFW,
       "hmSecVPNFWINTable": hmSecVPNFWINTable,
       "hmSecVPNFWINEntry": hmSecVPNFWINEntry,
       "hmSecVPNFWINconIndex": hmSecVPNFWINconIndex,
       "hmSecVPNFWINruleIndex": hmSecVPNFWINruleIndex,
       "hmSecVPNFWINsourceIP": hmSecVPNFWINsourceIP,
       "hmSecVPNFWINdestinationIP": hmSecVPNFWINdestinationIP,
       "hmSecVPNFWINsport": hmSecVPNFWINsport,
       "hmSecVPNFWINdport": hmSecVPNFWINdport,
       "hmSecVPNFWINtarget": hmSecVPNFWINtarget,
       "hmSecVPNFWINproto": hmSecVPNFWINproto,
       "hmSecVPNFWINlog": hmSecVPNFWINlog,
       "hmSecVPNFWINRowStatus": hmSecVPNFWINRowStatus,
       "hmSecVPNFWINcomment": hmSecVPNFWINcomment,
       "hmSecVPNFWOUTTable": hmSecVPNFWOUTTable,
       "hmSecVPNFWOUTEntry": hmSecVPNFWOUTEntry,
       "hmSecVPNFWOUTconIndex": hmSecVPNFWOUTconIndex,
       "hmSecVPNFWOUTruleIndex": hmSecVPNFWOUTruleIndex,
       "hmSecVPNFWOUTsourceIP": hmSecVPNFWOUTsourceIP,
       "hmSecVPNFWOUTdestinationIP": hmSecVPNFWOUTdestinationIP,
       "hmSecVPNFWOUTsport": hmSecVPNFWOUTsport,
       "hmSecVPNFWOUTdport": hmSecVPNFWOUTdport,
       "hmSecVPNFWOUTtarget": hmSecVPNFWOUTtarget,
       "hmSecVPNFWOUTproto": hmSecVPNFWOUTproto,
       "hmSecVPNFWOUTlog": hmSecVPNFWOUTlog,
       "hmSecVPNFWOUTRowStatus": hmSecVPNFWOUTRowStatus,
       "hmSecVPNFWOUTcomment": hmSecVPNFWOUTcomment,
       "hmSecVPNDynDNS": hmSecVPNDynDNS,
       "hmSecVPNDynDNSRegister": hmSecVPNDynDNSRegister,
       "hmSecVPNDynDNSReg": hmSecVPNDynDNSReg,
       "hmSecVPNDynDNSRegInterval": hmSecVPNDynDNSRegInterval,
       "hmSecVPNDynDNSRegServer": hmSecVPNDynDNSRegServer,
       "hmSecVPNDynDNSRegLogin": hmSecVPNDynDNSRegLogin,
       "hmSecVPNDynDNSRegPasswd": hmSecVPNDynDNSRegPasswd,
       "hmSecVPNDynDNSRegProvider": hmSecVPNDynDNSRegProvider,
       "hmSecVPNDynDNSRegHostname": hmSecVPNDynDNSRegHostname,
       "hmSecVPNDynDNSCheck": hmSecVPNDynDNSCheck,
       "hmSecVPNDynDNSCheckDo": hmSecVPNDynDNSCheckDo,
       "hmSecVPNDynDNSCheckRefresh": hmSecVPNDynDNSCheckRefresh,
       "hmSecVPNL2TP": hmSecVPNL2TP,
       "hmSecVPNL2TPStart": hmSecVPNL2TPStart,
       "hmSecVPNL2TPLocalIP": hmSecVPNL2TPLocalIP,
       "hmSecVPNL2TPRemoteIPRangeStart": hmSecVPNL2TPRemoteIPRangeStart,
       "hmSecVPNL2TPRemoteIPRangeEnd": hmSecVPNL2TPRemoteIPRangeEnd,
       "hmSecVPNL2TPpppdOptTable": hmSecVPNL2TPpppdOptTable,
       "hmSecVPNL2TPpppdOptEntry": hmSecVPNL2TPpppdOptEntry,
       "hmSecVPNL2TPpppdOptIndex": hmSecVPNL2TPpppdOptIndex,
       "hmSecVPNL2TPpppdOptValue": hmSecVPNL2TPpppdOptValue,
       "hmSecVPNL2TPpppdOptRowStatus": hmSecVPNL2TPpppdOptRowStatus,
       "hmSecVPNSettings": hmSecVPNSettings,
       "hmSecVPNRequireUniqueIDs": hmSecVPNRequireUniqueIDs,
       "hmSecVPNNatTraversal": hmSecVPNNatTraversal,
       "hmSecVPNNatTPortfloating": hmSecVPNNatTPortfloating,
       "hmSecVPNNatTKeepAliveInterval": hmSecVPNNatTKeepAliveInterval,
       "hmSecVPNNatTKeepAliveForce": hmSecVPNNatTKeepAliveForce,
       "hmSecVPNIkeLog": hmSecVPNIkeLog,
       "hmSecVPNHideTos": hmSecVPNHideTos,
       "hmSecVPNmtu": hmSecVPNmtu,
       "hmSecVPNStrictCRLPolicy": hmSecVPNStrictCRLPolicy,
       "hmSecVPNNoCertReqSend": hmSecVPNNoCertReqSend,
       "hmSecFirewall": hmSecFirewall,
       "hmSecFirewallIncoming": hmSecFirewallIncoming,
       "hmSecFirewallIncomingTable": hmSecFirewallIncomingTable,
       "hmSecFirewallIncomingEntry": hmSecFirewallIncomingEntry,
       "hmSecFWINruleIndex": hmSecFWINruleIndex,
       "hmSecFWINsourceIP": hmSecFWINsourceIP,
       "hmSecFWINdestinationIP": hmSecFWINdestinationIP,
       "hmSecFWINsport": hmSecFWINsport,
       "hmSecFWINdport": hmSecFWINdport,
       "hmSecFWINtarget": hmSecFWINtarget,
       "hmSecFWINproto": hmSecFWINproto,
       "hmSecFWINlog": hmSecFWINlog,
       "hmSecFWINRowStatus": hmSecFWINRowStatus,
       "hmSecFWINcomment": hmSecFWINcomment,
       "hmSecFirewallINLogDefault": hmSecFirewallINLogDefault,
       "hmSecFirewallOutgoing": hmSecFirewallOutgoing,
       "hmSecFirewallOutgoingTable": hmSecFirewallOutgoingTable,
       "hmSecFirewallOutgoingEntry": hmSecFirewallOutgoingEntry,
       "hmSecFWOUTruleIndex": hmSecFWOUTruleIndex,
       "hmSecFWOUTsourceIP": hmSecFWOUTsourceIP,
       "hmSecFWOUTdestinationIP": hmSecFWOUTdestinationIP,
       "hmSecFWOUTsport": hmSecFWOUTsport,
       "hmSecFWOUTdport": hmSecFWOUTdport,
       "hmSecFWOUTtarget": hmSecFWOUTtarget,
       "hmSecFWOUTproto": hmSecFWOUTproto,
       "hmSecFWOUTlog": hmSecFWOUTlog,
       "hmSecFWOUTRowStatus": hmSecFWOUTRowStatus,
       "hmSecFWOUTcomment": hmSecFWOUTcomment,
       "hmSecFirewallOUTLogDefault": hmSecFirewallOUTLogDefault,
       "hmSecFirewallPortforwarding": hmSecFirewallPortforwarding,
       "hmSecFirewallPortforwardTable": hmSecFirewallPortforwardTable,
       "hmSecFirewallPortforwardEntry": hmSecFirewallPortforwardEntry,
       "hmSecFWPORTFORWruleIndex": hmSecFWPORTFORWruleIndex,
       "hmSecFWPORTFORWinIP": hmSecFWPORTFORWinIP,
       "hmSecFWPORTFORWoutIP": hmSecFWPORTFORWoutIP,
       "hmSecFWPORTFORWinport": hmSecFWPORTFORWinport,
       "hmSecFWPORTFORWoutport": hmSecFWPORTFORWoutport,
       "hmSecFWPORTFORWproto": hmSecFWPORTFORWproto,
       "hmSecFWPORTFORWlog": hmSecFWPORTFORWlog,
       "hmSecFWPORTFORWRowStatus": hmSecFWPORTFORWRowStatus,
       "hmSecFWPORTFORWsrcIP": hmSecFWPORTFORWsrcIP,
       "hmSecFWPORTFORWsrcport": hmSecFWPORTFORWsrcport,
       "hmSecFWPORTFORWcomment": hmSecFWPORTFORWcomment,
       "hmSecFirewallNAT": hmSecFirewallNAT,
       "hmSecFirewallNATRuleTable": hmSecFirewallNATRuleTable,
       "hmSecFirewallNATRuleEntry": hmSecFirewallNATRuleEntry,
       "hmSecFWNATruleIndex": hmSecFWNATruleIndex,
       "hmSecFWNATIP": hmSecFWNATIP,
       "hmSecFWNATRowStatus": hmSecFWNATRowStatus,
       "hmSecFWNATOutIP": hmSecFWNATOutIP,
       "hmSecFirewallExtended": hmSecFirewallExtended,
       "hmSecFirewallIPConntrackMax": hmSecFirewallIPConntrackMax,
       "hmSecFirewallIPSynfloodLimitInt": hmSecFirewallIPSynfloodLimitInt,
       "hmSecFirewallIPSynfloodLimitExt": hmSecFirewallIPSynfloodLimitExt,
       "hmSecFirewallICMPLimitInt": hmSecFirewallICMPLimitInt,
       "hmSecFirewallICMPLimitExt": hmSecFirewallICMPLimitExt,
       "hmSecFirewallEnableConntrackFTP": hmSecFirewallEnableConntrackFTP,
       "hmSecFirewallConntrackIRC": hmSecFirewallConntrackIRC,
       "hmSecFirewallConntrackPPTP": hmSecFirewallConntrackPPTP,
       "hmSecFirewallARPLimitInt": hmSecFirewallARPLimitInt,
       "hmSecFirewallARPLimitExt": hmSecFirewallARPLimitExt,
       "hmSecFirewallICMPPolicy": hmSecFirewallICMPPolicy,
       "hmSecFirewallConntrackH323": hmSecFirewallConntrackH323,
       "hmSecFirewallIpUncleanMatch": hmSecFirewallIpUncleanMatch,
       "hmSecFirewall11NAT": hmSecFirewall11NAT,
       "hmSecFirewall11NATRuleTable": hmSecFirewall11NATRuleTable,
       "hmSecFirewall11NATRuleEntry": hmSecFirewall11NATRuleEntry,
       "hmSecFW11NATruleIndex": hmSecFW11NATruleIndex,
       "hmSecFW11NATLocal": hmSecFW11NATLocal,
       "hmSecFW11NATRemote": hmSecFW11NATRemote,
       "hmSecFW11NATMask": hmSecFW11NATMask,
       "hmSecFW11NATLog": hmSecFW11NATLog,
       "hmSecFW11NATRowStatus": hmSecFW11NATRowStatus,
       "hmSecNetwork": hmSecNetwork,
       "hmSecNetworkMode": hmSecNetworkMode,
       "hmSecStealth": hmSecStealth,
       "hmSecStealthIPConfMode": hmSecStealthIPConfMode,
       "hmSecStealthIPConfStatic": hmSecStealthIPConfStatic,
       "hmSecStealthStaticIP": hmSecStealthStaticIP,
       "hmSecStealthStaticMAC": hmSecStealthStaticMAC,
       "hmSecStealthStaticActivate": hmSecStealthStaticActivate,
       "hmSecStealthManageIP": hmSecStealthManageIP,
       "hmSecStealthManageNetmask": hmSecStealthManageNetmask,
       "hmSecStealthManageGateway": hmSecStealthManageGateway,
       "hmSecStealthManageActivate": hmSecStealthManageActivate,
       "hmSecStealthHiDiscoveryRelay": hmSecStealthHiDiscoveryRelay,
       "hmSecStealthHiDiscoveryState": hmSecStealthHiDiscoveryState,
       "hmSecStealthL2Filter": hmSecStealthL2Filter,
       "hmSecL2FilterInternTable": hmSecL2FilterInternTable,
       "hmSecL2FilterInternEntry": hmSecL2FilterInternEntry,
       "hmSecL2FilterInternRuleIndex": hmSecL2FilterInternRuleIndex,
       "hmSecL2FilterInternRowStatus": hmSecL2FilterInternRowStatus,
       "hmSecL2FilterInternSrcMac": hmSecL2FilterInternSrcMac,
       "hmSecL2FilterInternDstMac": hmSecL2FilterInternDstMac,
       "hmSecL2FilterInternEthType": hmSecL2FilterInternEthType,
       "hmSecL2FilterInternTarget": hmSecL2FilterInternTarget,
       "hmSecL2FilterInternComment": hmSecL2FilterInternComment,
       "hmSecL2FilterExternTable": hmSecL2FilterExternTable,
       "hmSecL2FilterExternEntry": hmSecL2FilterExternEntry,
       "hmSecL2FilterExternRuleIndex": hmSecL2FilterExternRuleIndex,
       "hmSecL2FilterExternRowStatus": hmSecL2FilterExternRowStatus,
       "hmSecL2FilterExternSrcMac": hmSecL2FilterExternSrcMac,
       "hmSecL2FilterExternDstMac": hmSecL2FilterExternDstMac,
       "hmSecL2FilterExternEthType": hmSecL2FilterExternEthType,
       "hmSecL2FilterExternTarget": hmSecL2FilterExternTarget,
       "hmSecL2FilterExternComment": hmSecL2FilterExternComment,
       "hmSecStealthL2ForwardGVRP": hmSecStealthL2ForwardGVRP,
       "hmSecStealthL2ForwardSTP": hmSecStealthL2ForwardSTP,
       "hmSecStealthL2ForwardDHCP": hmSecStealthL2ForwardDHCP,
       "hmSecStealthInterface": hmSecStealthInterface,
       "hmSecStealthMTU": hmSecStealthMTU,
       "hmSecStealthVlanMTU": hmSecStealthVlanMTU,
       "hmSecStealthManageUseVLAN": hmSecStealthManageUseVLAN,
       "hmSecStealthManageVLanID": hmSecStealthManageVLanID,
       "hmSecRouter": hmSecRouter,
       "hmSecRouterLocal": hmSecRouterLocal,
       "hmSecRouterLocalIP": hmSecRouterLocalIP,
       "hmSecRouterLocalNetmask": hmSecRouterLocalNetmask,
       "hmSecRouterLocalActivate": hmSecRouterLocalActivate,
       "hmSecRouterLocalAliasesTable": hmSecRouterLocalAliasesTable,
       "hmSecRouterLocalAliasesEntry": hmSecRouterLocalAliasesEntry,
       "hmSecLocalAliasIndex": hmSecLocalAliasIndex,
       "hmSecLocalAliasIpAddress": hmSecLocalAliasIpAddress,
       "hmSecLocalAliasNetmask": hmSecLocalAliasNetmask,
       "hmSecLocalAliasRowStatus": hmSecLocalAliasRowStatus,
       "hmSecLocalAliasUseVLAN": hmSecLocalAliasUseVLAN,
       "hmSecLocalAliasVLANid": hmSecLocalAliasVLANid,
       "hmSecLocalRoutesTable": hmSecLocalRoutesTable,
       "hmSecLocalRoutesEntry": hmSecLocalRoutesEntry,
       "hmSecLocalRouteIndex": hmSecLocalRouteIndex,
       "hmSecLocalRouteNetwork": hmSecLocalRouteNetwork,
       "hmSecLocalRouteGateway": hmSecLocalRouteGateway,
       "hmSecLocalRouteRowStatus": hmSecLocalRouteRowStatus,
       "hmSecRouterLocalDevMTU": hmSecRouterLocalDevMTU,
       "hmSecRouterLocalUseVLAN": hmSecRouterLocalUseVLAN,
       "hmSecRouterLocalVlanId": hmSecRouterLocalVlanId,
       "hmSecRouterLocalDevVlanMTU": hmSecRouterLocalDevVlanMTU,
       "hmSecRouterExtern": hmSecRouterExtern,
       "hmSecRouterExternDHCP": hmSecRouterExternDHCP,
       "hmSecRouterExternStatic": hmSecRouterExternStatic,
       "hmSecRouterExternStaticIP": hmSecRouterExternStaticIP,
       "hmSecRouterExternStaticNetmask": hmSecRouterExternStaticNetmask,
       "hmSecRouterExternStaticGateway": hmSecRouterExternStaticGateway,
       "hmSecRouterExternActivate": hmSecRouterExternActivate,
       "hmSecRouterExternAliasesTable": hmSecRouterExternAliasesTable,
       "hmSecRouterExternAliasesEntry": hmSecRouterExternAliasesEntry,
       "hmSecExternAliasIndex": hmSecExternAliasIndex,
       "hmSecExternAliasIpAddress": hmSecExternAliasIpAddress,
       "hmSecExternAliasNetmask": hmSecExternAliasNetmask,
       "hmSecExternAliasRowStatus": hmSecExternAliasRowStatus,
       "hmSecExternAliasUseVLAN": hmSecExternAliasUseVLAN,
       "hmSecExternAliasVLANid": hmSecExternAliasVLANid,
       "hmSecExternRoutesTable": hmSecExternRoutesTable,
       "hmSecExternRoutesEntry": hmSecExternRoutesEntry,
       "hmSecExternRouteIndex": hmSecExternRouteIndex,
       "hmSecExternRouteNetwork": hmSecExternRouteNetwork,
       "hmSecExternRouteGateway": hmSecExternRouteGateway,
       "hmSecExternRouteRowStatus": hmSecExternRouteRowStatus,
       "hmSecRouterExternDevMTU": hmSecRouterExternDevMTU,
       "hmSecRouterExternUseVLAN": hmSecRouterExternUseVLAN,
       "hmSecRouterExternVlanId": hmSecRouterExternVlanId,
       "hmSecRouterExternDevVlanMTU": hmSecRouterExternDevVlanMTU,
       "hmSecRouterHiDiscovery": hmSecRouterHiDiscovery,
       "hmSecRouterHiDiscoveryIntern": hmSecRouterHiDiscoveryIntern,
       "hmSecRouterHiDiscoveryExtern": hmSecRouterHiDiscoveryExtern,
       "hmSecPPPOE": hmSecPPPOE,
       "hmSecPPPOELogin": hmSecPPPOELogin,
       "hmSecPPPOEPasswd": hmSecPPPOEPasswd,
       "hmSecPPPOEMSS": hmSecPPPOEMSS,
       "hmSecPPPOEServiceName": hmSecPPPOEServiceName,
       "hmSecPPPOEAccessConcentName": hmSecPPPOEAccessConcentName,
       "hmSecPPPOEHostUnique": hmSecPPPOEHostUnique,
       "hmSecPPPOEpppdOptionsTable": hmSecPPPOEpppdOptionsTable,
       "hmSecPPPOEpppdOptionsEntry": hmSecPPPOEpppdOptionsEntry,
       "hmSecPPPOEpppdOptionsIndex": hmSecPPPOEpppdOptionsIndex,
       "hmSecPPPOEpppdOptionsValue": hmSecPPPOEpppdOptionsValue,
       "hmSecPPPOEpppdOptionsRowStatus": hmSecPPPOEpppdOptionsRowStatus,
       "hmSecDHCP": hmSecDHCP,
       "hmSecDHCPInt": hmSecDHCPInt,
       "hmSecDHCPIntStart": hmSecDHCPIntStart,
       "hmSecDHCPIntPoolEnable": hmSecDHCPIntPoolEnable,
       "hmSecDHCPIntRangeStart": hmSecDHCPIntRangeStart,
       "hmSecDHCPIntRangeEnd": hmSecDHCPIntRangeEnd,
       "hmSecDHCPIntNetmask": hmSecDHCPIntNetmask,
       "hmSecDHCPIntGateway": hmSecDHCPIntGateway,
       "hmSecDHCPIntDnsServer": hmSecDHCPIntDnsServer,
       "hmSecDHCPIntStaticTable": hmSecDHCPIntStaticTable,
       "hmSecDHCPIntStaticEntry": hmSecDHCPIntStaticEntry,
       "hmSecDHCPIntStaticIndex": hmSecDHCPIntStaticIndex,
       "hmSecDHCPIntStaticMAC": hmSecDHCPIntStaticMAC,
       "hmSecDHCPIntStaticIP": hmSecDHCPIntStaticIP,
       "hmSecDHCPIntStaticRowStatus": hmSecDHCPIntStaticRowStatus,
       "hmSecDHCPIntBroadcast": hmSecDHCPIntBroadcast,
       "hmSecDHCPIntWINS": hmSecDHCPIntWINS,
       "hmSecDHCPIntLeaseTime": hmSecDHCPIntLeaseTime,
       "hmSecDHCPIntRelayServerTable": hmSecDHCPIntRelayServerTable,
       "hmSecDHCPIntRelayServerEntry": hmSecDHCPIntRelayServerEntry,
       "hmSecDHCPIntRelayServerIndex": hmSecDHCPIntRelayServerIndex,
       "hmSecDHCPIntRelayServerIP": hmSecDHCPIntRelayServerIP,
       "hmSecDHCPIntRelayRowStatus": hmSecDHCPIntRelayRowStatus,
       "hmSecDHCPIntRelayMaxHop": hmSecDHCPIntRelayMaxHop,
       "hmSecDHCPIntRelayAppend": hmSecDHCPIntRelayAppend,
       "hmSecDHCPIntRelayAppendLimit": hmSecDHCPIntRelayAppendLimit,
       "hmSecDHCPIntRelayCircuitInfo": hmSecDHCPIntRelayCircuitInfo,
       "hmSecDHCPIntRelayCircuitText": hmSecDHCPIntRelayCircuitText,
       "hmSecDHCPIntRelayRemoteInfo": hmSecDHCPIntRelayRemoteInfo,
       "hmSecDHCPIntRelayRemoteText": hmSecDHCPIntRelayRemoteText,
       "hmSecDHCPExt": hmSecDHCPExt,
       "hmSecDHCPExtStart": hmSecDHCPExtStart,
       "hmSecDHCPExtPoolEnable": hmSecDHCPExtPoolEnable,
       "hmSecDHCPExtRangeStart": hmSecDHCPExtRangeStart,
       "hmSecDHCPExtRangeEnd": hmSecDHCPExtRangeEnd,
       "hmSecDHCPExtNetmask": hmSecDHCPExtNetmask,
       "hmSecDHCPExtGateway": hmSecDHCPExtGateway,
       "hmSecDHCPExtDnsServer": hmSecDHCPExtDnsServer,
       "hmSecDHCPExtStaticTable": hmSecDHCPExtStaticTable,
       "hmSecDHCPExtStaticEntry": hmSecDHCPExtStaticEntry,
       "hmSecDHCPExtStaticIndex": hmSecDHCPExtStaticIndex,
       "hmSecDHCPExtStaticMAC": hmSecDHCPExtStaticMAC,
       "hmSecDHCPExtStaticIP": hmSecDHCPExtStaticIP,
       "hmSecDHCPExtStaticRowStatus": hmSecDHCPExtStaticRowStatus,
       "hmSecDHCPExtBroadcast": hmSecDHCPExtBroadcast,
       "hmSecDHCPExtWINS": hmSecDHCPExtWINS,
       "hmSecDHCPExtLeaseTime": hmSecDHCPExtLeaseTime,
       "hmSecDHCPExtRelayServerTable": hmSecDHCPExtRelayServerTable,
       "hmSecDHCPExtRelayServerEntry": hmSecDHCPExtRelayServerEntry,
       "hmSecDHCPExtRelayServerIndex": hmSecDHCPExtRelayServerIndex,
       "hmSecDHCPExtRelayServerIP": hmSecDHCPExtRelayServerIP,
       "hmSecDHCPExtRelayRowStatus": hmSecDHCPExtRelayRowStatus,
       "hmSecDHCPExtRelayMaxHop": hmSecDHCPExtRelayMaxHop,
       "hmSecDHCPExtRelayAppend": hmSecDHCPExtRelayAppend,
       "hmSecDHCPExtRelayAppendLimit": hmSecDHCPExtRelayAppendLimit,
       "hmSecDHCPExtRelayCircuitInfo": hmSecDHCPExtRelayCircuitInfo,
       "hmSecDHCPExtRelayCircuitText": hmSecDHCPExtRelayCircuitText,
       "hmSecDHCPExtRelayRemoteInfo": hmSecDHCPExtRelayRemoteInfo,
       "hmSecDHCPExtRelayRemoteText": hmSecDHCPExtRelayRemoteText,
       "hmSecDNS": hmSecDNS,
       "hmSecDNSSearchPath": hmSecDNSSearchPath,
       "hmSecDNSServerType": hmSecDNSServerType,
       "hmSecDNSUserDefinedServerTable": hmSecDNSUserDefinedServerTable,
       "hmSecDNSUserDefinedServerEntry": hmSecDNSUserDefinedServerEntry,
       "hmSecdnsServerIndex": hmSecdnsServerIndex,
       "hmSecdnsServerIP": hmSecdnsServerIP,
       "hmSecdnsServerRowStatus": hmSecdnsServerRowStatus,
       "hmSecDNSCacheEnabled": hmSecDNSCacheEnabled,
       "hmSecNetworkStatus": hmSecNetworkStatus,
       "hmSecNetworkStatMode": hmSecNetworkStatMode,
       "hmSecNetworkStatExtIP": hmSecNetworkStatExtIP,
       "hmSecNetworkStatGateway": hmSecNetworkStatGateway,
       "hmSecNetworkStatVPN": hmSecNetworkStatVPN,
       "hmSecNetworkStatDynIPReg": hmSecNetworkStatDynIPReg,
       "hmSecNetworkStatHTTPSRemAccess": hmSecNetworkStatHTTPSRemAccess,
       "hmSecNetworkStatSSHRemoteAccess": hmSecNetworkStatSSHRemoteAccess,
       "hmSecNetworkSoftwareVersion": hmSecNetworkSoftwareVersion,
       "hmSecNetworkStatUptime": hmSecNetworkStatUptime,
       "hmSecNetworkStatLanguage": hmSecNetworkStatLanguage,
       "hmSecHostname": hmSecHostname,
       "hmSecHostnameMode": hmSecHostnameMode,
       "hmSecPPTP": hmSecPPTP,
       "hmSecPPTPLogin": hmSecPPTPLogin,
       "hmSecPPTPassword": hmSecPPTPassword,
       "hmSecPPTPLocalIPMode": hmSecPPTPLocalIPMode,
       "hmSecPPTPLocalIP": hmSecPPTPLocalIP,
       "hmSecPPTPModemIP": hmSecPPTPModemIP,
       "hmSecPPTPpppdOptionsTable": hmSecPPTPpppdOptionsTable,
       "hmSecPPTPpppdOptionsEntry": hmSecPPTPpppdOptionsEntry,
       "hmSecPPTPpppdOptionsIndex": hmSecPPTPpppdOptionsIndex,
       "hmSecPPTPpppdOptionsValue": hmSecPPTPpppdOptionsValue,
       "hmSecPPTPpppdOptionsRowStatus": hmSecPPTPpppdOptionsRowStatus,
       "hmSecSerial": hmSecSerial,
       "hmSecSerialBaud": hmSecSerialBaud,
       "hmSecSerialHWHandshakeEnable": hmSecSerialHWHandshakeEnable,
       "hmSecSerialPPP": hmSecSerialPPP,
       "hmSecSerialPPPEnable": hmSecSerialPPPEnable,
       "hmSecSerialPPPLogin": hmSecSerialPPPLogin,
       "hmSecSerialPPPPasswd": hmSecSerialPPPPasswd,
       "hmSecSerialPPPLocalIP": hmSecSerialPPPLocalIP,
       "hmSecSerialPPPRemoteIP": hmSecSerialPPPRemoteIP,
       "hmSecSerialPPPFWIN": hmSecSerialPPPFWIN,
       "hmSecSerialPPPFWINTable": hmSecSerialPPPFWINTable,
       "hmSecSerialPPPFWINEntry": hmSecSerialPPPFWINEntry,
       "hmSecSerialPPPFWINruleIndex": hmSecSerialPPPFWINruleIndex,
       "hmSecSerialPPPFWINsourceIP": hmSecSerialPPPFWINsourceIP,
       "hmSecSerialPPPFWINdestinationIP": hmSecSerialPPPFWINdestinationIP,
       "hmSecSerialPPPFWINsport": hmSecSerialPPPFWINsport,
       "hmSecSerialPPPFWINdport": hmSecSerialPPPFWINdport,
       "hmSecSerialPPPFWINtarget": hmSecSerialPPPFWINtarget,
       "hmSecSerialPPPFWINproto": hmSecSerialPPPFWINproto,
       "hmSecSerialPPPFWINlog": hmSecSerialPPPFWINlog,
       "hmSecSerialPPPFWINRowStatus": hmSecSerialPPPFWINRowStatus,
       "hmSecSerialPPPFWINcomment": hmSecSerialPPPFWINcomment,
       "hmSecSerialPPPFWINLogDefault": hmSecSerialPPPFWINLogDefault,
       "hmSecSerialPPPFWOUT": hmSecSerialPPPFWOUT,
       "hmSecSerialPPPFWOUTTable": hmSecSerialPPPFWOUTTable,
       "hmSecSerialPPPFWOUTEntry": hmSecSerialPPPFWOUTEntry,
       "hmSecSerialPPPFWOUTruleIndex": hmSecSerialPPPFWOUTruleIndex,
       "hmSecSerialPPPFWOUTsourceIP": hmSecSerialPPPFWOUTsourceIP,
       "hmSecSerialPPPFWOUTtargetIP": hmSecSerialPPPFWOUTtargetIP,
       "hmSecSerialPPPFWOUTsport": hmSecSerialPPPFWOUTsport,
       "hmSecSerialPPPFWOUTdport": hmSecSerialPPPFWOUTdport,
       "hmSecSerialPPPFWOUTtarget": hmSecSerialPPPFWOUTtarget,
       "hmSecSerialPPPFWOUTproto": hmSecSerialPPPFWOUTproto,
       "hmSecSerialPPPFWOUTlog": hmSecSerialPPPFWOUTlog,
       "hmSecSerialPPPFWOUTRowStatus": hmSecSerialPPPFWOUTRowStatus,
       "hmSecSerialPPPFWOUTcomment": hmSecSerialPPPFWOUTcomment,
       "hmSecSerialPPPFWOUTLogDefault": hmSecSerialPPPFWOUTLogDefault,
       "hmSecArpTimeout": hmSecArpTimeout,
       "hmSecSystem": hmSecSystem,
       "hmSecPasswords": hmSecPasswords,
       "hmSecRootPassword": hmSecRootPassword,
       "hmSecAdminPassword": hmSecAdminPassword,
       "hmSecUserPassword": hmSecUserPassword,
       "hmSecUserPwdEnable": hmSecUserPwdEnable,
       "hmSecHTTPSRemoteAccess": hmSecHTTPSRemoteAccess,
       "hmSecHTTPSRemoteEnable": hmSecHTTPSRemoteEnable,
       "hmSecHTTPSRemotePort": hmSecHTTPSRemotePort,
       "hmSecHTTPSRemoteFWRuleTable": hmSecHTTPSRemoteFWRuleTable,
       "hmSecHTTPSRemoteFWRuleEntry": hmSecHTTPSRemoteFWRuleEntry,
       "hmSecHTTPSFWruleIndex": hmSecHTTPSFWruleIndex,
       "hmSecHTTPSFWsourceIP": hmSecHTTPSFWsourceIP,
       "hmSecHTTPSFWinterface": hmSecHTTPSFWinterface,
       "hmSecHTTPSFWtarget": hmSecHTTPSFWtarget,
       "hmSecHTTPSFWlog": hmSecHTTPSFWlog,
       "hmSecHTTPSFWRowStatus": hmSecHTTPSFWRowStatus,
       "hmSecHTTPSFWcomment": hmSecHTTPSFWcomment,
       "hmSecSSHRemoteAccess": hmSecSSHRemoteAccess,
       "hmSecSSHRemoteEnable": hmSecSSHRemoteEnable,
       "hmSecSSHRemotePort": hmSecSSHRemotePort,
       "hmSecSSHRemoteFWRuleTable": hmSecSSHRemoteFWRuleTable,
       "hmSecSSHRemoteFWRuleEntry": hmSecSSHRemoteFWRuleEntry,
       "hmSecSSHFWruleIndex": hmSecSSHFWruleIndex,
       "hmSecSSHFWsourceIP": hmSecSSHFWsourceIP,
       "hmSecSSHFWinterface": hmSecSSHFWinterface,
       "hmSecSSHFWtarget": hmSecSSHFWtarget,
       "hmSecSSHFWlog": hmSecSSHFWlog,
       "hmSecSSHFWRowStatus": hmSecSSHFWRowStatus,
       "hmSecSSHFWcomment": hmSecSSHFWcomment,
       "hmSecLanguage": hmSecLanguage,
       "hmSecHardwareInformation": hmSecHardwareInformation,
       "hmSecHardware": hmSecHardware,
       "hmSecCPU": hmSecCPU,
       "hmSecCPUFamily": hmSecCPUFamily,
       "hmSecCPUStepping": hmSecCPUStepping,
       "hmSecCPUSpeed": hmSecCPUSpeed,
       "hmSecSystemTemperature": hmSecSystemTemperature,
       "hmSecUptime": hmSecUptime,
       "hmSecUSMem": hmSecUSMem,
       "hmSecMAC1": hmSecMAC1,
       "hmSecMAC2": hmSecMAC2,
       "hmSecMAC3": hmSecMAC3,
       "hmSecSerialNumber": hmSecSerialNumber,
       "hmSecVerParSet": hmSecVerParSet,
       "hmSecProductName": hmSecProductName,
       "hmSecOEMName": hmSecOEMName,
       "hmSecOEMSerial": hmSecOEMSerial,
       "hmSecManufacturer": hmSecManufacturer,
       "hmSecManuDate": hmSecManuDate,
       "hmSecBootLoader": hmSecBootLoader,
       "hmSecHardwareVersion": hmSecHardwareVersion,
       "hmSecRescueSystem": hmSecRescueSystem,
       "hmSecProdSoft": hmSecProdSoft,
       "hmSecVersions": hmSecVersions,
       "hmSecVersion": hmSecVersion,
       "hmSecBaseVersion": hmSecBaseVersion,
       "hmSecUpdates": hmSecUpdates,
       "hmSecPackageVersionTable": hmSecPackageVersionTable,
       "hmSecPackageVersionEntry": hmSecPackageVersionEntry,
       "hmSecPkgIndex": hmSecPkgIndex,
       "hmSecPkgName": hmSecPkgName,
       "hmSecPkgVerNum": hmSecPkgVerNum,
       "hmSecPkgVerVersion": hmSecPkgVerVersion,
       "hmSecPkgVerFlavour": hmSecPkgVerFlavour,
       "hmSecAction": hmSecAction,
       "hmSecSNMP": hmSecSNMP,
       "hmSecSNMPenableV3": hmSecSNMPenableV3,
       "hmSecSNMPenableV1": hmSecSNMPenableV1,
       "hmSecSNMPport": hmSecSNMPport,
       "hmSecSNMPv1ROCommunity": hmSecSNMPv1ROCommunity,
       "hmSecSNMPv1RWCommunity": hmSecSNMPv1RWCommunity,
       "hmSecSNMPFWRuleTable": hmSecSNMPFWRuleTable,
       "hmSecSNMPFWRuleEntry": hmSecSNMPFWRuleEntry,
       "hmSecSNMPFWruleIndex": hmSecSNMPFWruleIndex,
       "hmSecSNMPFWsourceIP": hmSecSNMPFWsourceIP,
       "hmSecSNMPFWinterface": hmSecSNMPFWinterface,
       "hmSecSNMPFWtarget": hmSecSNMPFWtarget,
       "hmSecSNMPFWlog": hmSecSNMPFWlog,
       "hmSecSNMPFWRowStatus": hmSecSNMPFWRowStatus,
       "hmSecSNMPFWcomment": hmSecSNMPFWcomment,
       "hmSecSNMPTrapReceiverTable": hmSecSNMPTrapReceiverTable,
       "hmSecSNMPTrapReceiverEntry": hmSecSNMPTrapReceiverEntry,
       "hmSecSNMPTrapReceiverIndex": hmSecSNMPTrapReceiverIndex,
       "hmSecSNMPTrapReceiverCommunity": hmSecSNMPTrapReceiverCommunity,
       "hmSecSNMPTrapReceiverIPAddress": hmSecSNMPTrapReceiverIPAddress,
       "hmSecSNMPTrapReceiverName": hmSecSNMPTrapReceiverName,
       "hmSecSNMPTrapReceiverRowStatus": hmSecSNMPTrapReceiverRowStatus,
       "hmSecSNMPTrapConfigGroup": hmSecSNMPTrapConfigGroup,
       "hmSecSNMPAuthenticationTrapFlag": hmSecSNMPAuthenticationTrapFlag,
       "hmSecSNMPLinkUpDownTrapFlag": hmSecSNMPLinkUpDownTrapFlag,
       "hmSecSNMPColdStartTrapFlag": hmSecSNMPColdStartTrapFlag,
       "hmSecSNMPTrapFlag": hmSecSNMPTrapFlag,
       "hmSecSNMPChassisTrapFlag": hmSecSNMPChassisTrapFlag,
       "hmSecSNMPAgentTrapFlag": hmSecSNMPAgentTrapFlag,
       "hmSecSNMPAvFailTrapFlag": hmSecSNMPAvFailTrapFlag,
       "hmSecSNMPAvInfoTrapFlag": hmSecSNMPAvInfoTrapFlag,
       "hmSecSNMPBladeStateTrapFlag": hmSecSNMPBladeStateTrapFlag,
       "hmSecSNMPBladeConfigTrapFlag": hmSecSNMPBladeConfigTrapFlag,
       "hmSecSNMPRouterRedundancyStatusFlag": hmSecSNMPRouterRedundancyStatusFlag,
       "hmSecNTP": hmSecNTP,
       "hmSecNTPactivate": hmSecNTPactivate,
       "hmSecNTPtimestamp": hmSecNTPtimestamp,
       "hmSecNTPServerTable": hmSecNTPServerTable,
       "hmSecNTPServerEntry": hmSecNTPServerEntry,
       "hmSecNTPServerIndex": hmSecNTPServerIndex,
       "hmSecNTPServerHost": hmSecNTPServerHost,
       "hmSecNTPServerRowStatus": hmSecNTPServerRowStatus,
       "hmSecNTPTimezone": hmSecNTPTimezone,
       "hmSecNTPStatus": hmSecNTPStatus,
       "hmSecUpdate": hmSecUpdate,
       "hmSecUpdateServerTable": hmSecUpdateServerTable,
       "hmSecUpdateServerEntry": hmSecUpdateServerEntry,
       "hmSecUpdateServerIndex": hmSecUpdateServerIndex,
       "hmSecUpdateServer": hmSecUpdateServer,
       "hmSecUpdateServerRowStatus": hmSecUpdateServerRowStatus,
       "hmSecUpdateServerProto": hmSecUpdateServerProto,
       "hmSecUpdateServerHost": hmSecUpdateServerHost,
       "hmSecUpdateServerLogin": hmSecUpdateServerLogin,
       "hmSecUpdateServerPassword": hmSecUpdateServerPassword,
       "hmSecSNMPError": hmSecSNMPError,
       "hmSecRedundancy": hmSecRedundancy,
       "hmSecL2Redundancy": hmSecL2Redundancy,
       "hmSecL2RedundancyEnable": hmSecL2RedundancyEnable,
       "hmSecL2RedundancyPort": hmSecL2RedundancyPort,
       "hmSecRouterRedundancy": hmSecRouterRedundancy,
       "hmSecRouterRedundancyEnable": hmSecRouterRedundancyEnable,
       "hmSecRouterRedundancyTrack": hmSecRouterRedundancyTrack,
       "hmSecRouterRedundancyInternalID": hmSecRouterRedundancyInternalID,
       "hmSecRouterRedundancyExternalID": hmSecRouterRedundancyExternalID,
       "hmSecRouterRedundancyPassword": hmSecRouterRedundancyPassword,
       "hmSecRouterRedundancyPeerIntern": hmSecRouterRedundancyPeerIntern,
       "hmSecRouterRedundancyPeerExtern": hmSecRouterRedundancyPeerExtern,
       "hmSecRouterRedundancyPriority": hmSecRouterRedundancyPriority,
       "hmSecRouterRedundancyVirtIpInt": hmSecRouterRedundancyVirtIpInt,
       "hmSecRouterRedundancyVirtIpExt": hmSecRouterRedundancyVirtIpExt,
       "hmSecRouterRedundancyWantState": hmSecRouterRedundancyWantState,
       "hmSecRouterRedExtHostCheckTable": hmSecRouterRedExtHostCheckTable,
       "hmSecRouterRedExtHostCheckEntry": hmSecRouterRedExtHostCheckEntry,
       "hmSecRouterRedExtHostCheckIndex": hmSecRouterRedExtHostCheckIndex,
       "hmSecRouterRedExtHostCheckIP": hmSecRouterRedExtHostCheckIP,
       "hmSecRouterRedExtHostCheckRowSt": hmSecRouterRedExtHostCheckRowSt,
       "hmSecRouterRedIntHostCheckTable": hmSecRouterRedIntHostCheckTable,
       "hmSecRouterRedIntHostCheckEntry": hmSecRouterRedIntHostCheckEntry,
       "hmSecRouterRedIntHostCheckIndex": hmSecRouterRedIntHostCheckIndex,
       "hmSecRouterRedIntHostCheckIP": hmSecRouterRedIntHostCheckIP,
       "hmSecRouterRedIntHostCheckRowSt": hmSecRouterRedIntHostCheckRowSt,
       "hmSecRouterRedundancyState": hmSecRouterRedundancyState,
       "hmSecInfo": hmSecInfo,
       "hmSecHTTPSLastAccessIP": hmSecHTTPSLastAccessIP,
       "hmSecShellLastAccessIP": hmSecShellLastAccessIP,
       "hmSecDHCPLastAccessMAC": hmSecDHCPLastAccessMAC,
       "hmSecTrapRessources": hmSecTrapRessources,
       "hmSecTResDiscFull": hmSecTResDiscFull,
       "hmSecTResCpuLoadHigh": hmSecTResCpuLoadHigh,
       "hmSecTResMemoryFull": hmSecTResMemoryFull,
       "hmSecTResColdstart": hmSecTResColdstart,
       "hmSecTResAV": hmSecTResAV,
       "hmSecTResAvUpdateDone": hmSecTResAvUpdateDone,
       "hmSecTResAvUpdateError": hmSecTResAvUpdateError,
       "hmSecTResAvVirusDetected": hmSecTResAvVirusDetected,
       "hmSecTResAvFileNotScanned": hmSecTResAvFileNotScanned,
       "hmSecTResAvFailed": hmSecTResAvFailed,
       "hmSecTResPlatformSpecific": hmSecTResPlatformSpecific,
       "hmSecTResIndustrial": hmSecTResIndustrial,
       "hmSecTResIndustrialPower": hmSecTResIndustrialPower,
       "hmSecPSTable": hmSecPSTable,
       "hmSecPSEntry": hmSecPSEntry,
       "hmSecPSSysID": hmSecPSSysID,
       "hmSecPSID": hmSecPSID,
       "hmSecPSState": hmSecPSState,
       "hmSecTResIndustrialTemperature": hmSecTResIndustrialTemperature,
       "hmSecTResIndustrialTempHiLimit": hmSecTResIndustrialTempHiLimit,
       "hmSecTResIndustrialTempLowLimit": hmSecTResIndustrialTempLowLimit,
       "hmSecTResSignalRelais": hmSecTResSignalRelais,
       "hmSecTResSignalRelaisState": hmSecTResSignalRelaisState,
       "hmSecTResSignalRelaisReason": hmSecTResSignalRelaisReason,
       "hmSecTResSignalRelaisReasonIdx": hmSecTResSignalRelaisReasonIdx,
       "hmSecTResSignalRelaisPowerAlarm": hmSecTResSignalRelaisPowerAlarm,
       "hmSecTResSignalRelaisMode": hmSecTResSignalRelaisMode,
       "hmSecTResSignalRelaisManualStat": hmSecTResSignalRelaisManualStat,
       "hmSecTResAutoConfigAdapterState": hmSecTResAutoConfigAdapterState,
       "hmSecTResSignalLinkTable": hmSecTResSignalLinkTable,
       "hmSecTResSigLinkID": hmSecTResSigLinkID,
       "hmSecTResSigLinkAlarm": hmSecTResSigLinkAlarm,
       "hmSecTResBladeCTRL": hmSecTResBladeCTRL,
       "hmSecTResBladeInfo": hmSecTResBladeInfo,
       "hmSecTResBladeRackID": hmSecTResBladeRackID,
       "hmSecTResBladeSlotNr": hmSecTResBladeSlotNr,
       "hmSecTResBladeCtrlPowerStatus": hmSecTResBladeCtrlPowerStatus,
       "hmSecTResBladeCtrlRunStatus": hmSecTResBladeCtrlRunStatus,
       "hmSecTResBladeCtrlFailover": hmSecTResBladeCtrlFailover,
       "hmSecTResBladeCtrlCfg": hmSecTResBladeCtrlCfg,
       "hmSecTResBladeCtrlCfgBackup": hmSecTResBladeCtrlCfgBackup,
       "hmSecTResBladeCtrlCfgRestored": hmSecTResBladeCtrlCfgRestored,
       "hmSecTResRedundancy": hmSecTResRedundancy,
       "hmSecTResRedundacyReason": hmSecTResRedundacyReason,
       "hmSecTResRedundacyBackupDown": hmSecTResRedundacyBackupDown,
       "hmSecTraps": hmSecTraps,
       "hmSecTrapDiscFull": hmSecTrapDiscFull,
       "hmSecTrapCpuLoadHigh": hmSecTrapCpuLoadHigh,
       "hmSecTrapMemoryFull": hmSecTrapMemoryFull,
       "hmSecTrapColdstart": hmSecTrapColdstart,
       "hmSecTrapAV": hmSecTrapAV,
       "hmSecTrapAvUpdateDone": hmSecTrapAvUpdateDone,
       "hmSecTrapAvUpdateError": hmSecTrapAvUpdateError,
       "hmSecTrapAvVirusDetected": hmSecTrapAvVirusDetected,
       "hmSecTrapAvFileNotScanned": hmSecTrapAvFileNotScanned,
       "hmSecTrapAvFailed": hmSecTrapAvFailed,
       "hmSecTrapPlatformSpecific": hmSecTrapPlatformSpecific,
       "hmSecTrapIndustrial": hmSecTrapIndustrial,
       "hmSecTrapIndustrialTemperature": hmSecTrapIndustrialTemperature,
       "hmSecTrapIndustrialPowerStatus": hmSecTrapIndustrialPowerStatus,
       "hmSecTrapSignalRelais": hmSecTrapSignalRelais,
       "hmSecTrapAutoConfigAdapterState": hmSecTrapAutoConfigAdapterState,
       "hmSecTrapBladeCTRL": hmSecTrapBladeCTRL,
       "hmSecTrapBladeCtrlPowerStatus": hmSecTrapBladeCtrlPowerStatus,
       "hmSecTrapBladeCtrlRunStatus": hmSecTrapBladeCtrlRunStatus,
       "hmSecTrapBladeCtrlFailover": hmSecTrapBladeCtrlFailover,
       "hmSecTrapBladeCtrlCfg": hmSecTrapBladeCtrlCfg,
       "hmSecTrapBladeCtrlCfgBackup": hmSecTrapBladeCtrlCfgBackup,
       "hmSecTrapBladeCtrlCfgRestored": hmSecTrapBladeCtrlCfgRestored,
       "hmSecTrapRouterRedundancy": hmSecTrapRouterRedundancy,
       "hmSecTrapRouterRedundancyStatusChange": hmSecTrapRouterRedundancyStatusChange,
       "hmSecTrapRouterRedundancyBackupDown": hmSecTrapRouterRedundancyBackupDown,
       "hmSecLogging": hmSecLogging,
       "hmSecLoggingRemoteActivate": hmSecLoggingRemoteActivate,
       "hmSecLoggingRemoteIP": hmSecLoggingRemoteIP,
       "hmSecLoggingRemotePort": hmSecLoggingRemotePort,
       "hmSecContFilt": hmSecContFilt,
       "hmSecContFiltAVP": hmSecContFiltAVP,
       "hmSecContFiltAVPSchedule": hmSecContFiltAVPSchedule,
       "hmSecContFiltAVPServerTable": hmSecContFiltAVPServerTable,
       "hmSecContFiltAVPServerEntry": hmSecContFiltAVPServerEntry,
       "hmSecContFiltAVPServerIndex": hmSecContFiltAVPServerIndex,
       "hmSecContFiltAVPServerProtocol": hmSecContFiltAVPServerProtocol,
       "hmSecContFiltAVPServerURL": hmSecContFiltAVPServerURL,
       "hmSecContFiltAVPServerLogin": hmSecContFiltAVPServerLogin,
       "hmSecContFiltAVPServerPassword": hmSecContFiltAVPServerPassword,
       "hmSecContFiltAVPServerRowStatus": hmSecContFiltAVPServerRowStatus,
       "hmSecContFiltAVPHTTPProxy": hmSecContFiltAVPHTTPProxy,
       "hmSecContFiltAVPHTTPProxyLogin": hmSecContFiltAVPHTTPProxyLogin,
       "hmSecContFiltAVPHTTPProxyPasswd": hmSecContFiltAVPHTTPProxyPasswd,
       "hmSecContFiltAVPHTTPProxyServer": hmSecContFiltAVPHTTPProxyServer,
       "hmSecContFiltAVPHTTPProxyPort": hmSecContFiltAVPHTTPProxyPort,
       "hmSecContFiltAVPFTPProxy": hmSecContFiltAVPFTPProxy,
       "hmSecContFiltAVPFTPProxyLogin": hmSecContFiltAVPFTPProxyLogin,
       "hmSecContFiltAVPFTPProxyPasswd": hmSecContFiltAVPFTPProxyPasswd,
       "hmSecContFiltAVPFTPProxyServer": hmSecContFiltAVPFTPProxyServer,
       "hmSecContFiltAVPFTPProxyPort": hmSecContFiltAVPFTPProxyPort,
       "hmSecContFiltAVPLogLevel": hmSecContFiltAVPLogLevel,
       "hmSecContFiltAVPMaxConnections": hmSecContFiltAVPMaxConnections,
       "hmSecContFiltAVPScanTimeout": hmSecContFiltAVPScanTimeout,
       "hmSecContFiltAVPpass": hmSecContFiltAVPpass,
       "hmSecContFiltAVPpassCorrupt": hmSecContFiltAVPpassCorrupt,
       "hmSecContFiltAVPpassEncrypted": hmSecContFiltAVPpassEncrypted,
       "hmSecContFiltAVPpassSuspicious": hmSecContFiltAVPpassSuspicious,
       "hmSecContFiltAVPpassWarnings": hmSecContFiltAVPpassWarnings,
       "hmSecContFiltQuarantine": hmSecContFiltQuarantine,
       "hmSecContFiltQuarantineClean": hmSecContFiltQuarantineClean,
       "hmSecContFiltQuarantineError": hmSecContFiltQuarantineError,
       "hmSecContFiltQuarantineVirus": hmSecContFiltQuarantineVirus,
       "hmSecContFiltQuarantineSrvIP": hmSecContFiltQuarantineSrvIP,
       "hmSecContFiltQuarantineSrvPort": hmSecContFiltQuarantineSrvPort,
       "hmSecContFiltInfo": hmSecContFiltInfo,
       "hmSecContFiltInfoFlashID": hmSecContFiltInfoFlashID,
       "hmSecContFiltHTTP": hmSecContFiltHTTP,
       "hmSecContFiltHTTPEnable": hmSecContFiltHTTPEnable,
       "hmSecContFiltHTTPVirusAction": hmSecContFiltHTTPVirusAction,
       "hmSecContFiltHTTPMaxSize": hmSecContFiltHTTPMaxSize,
       "hmSecContFiltHTTPExceedAction": hmSecContFiltHTTPExceedAction,
       "hmSecContFiltHTTPSrvrTable": hmSecContFiltHTTPSrvrTable,
       "hmSecContFiltHTTPSrvrEntry": hmSecContFiltHTTPSrvrEntry,
       "hmSecContFiltHTTPSrvrIndex": hmSecContFiltHTTPSrvrIndex,
       "hmSecContFiltHTTPSrvrIP": hmSecContFiltHTTPSrvrIP,
       "hmSecContFiltHTTPSrvrPort": hmSecContFiltHTTPSrvrPort,
       "hmSecContFiltHTTPSrvrScanAction": hmSecContFiltHTTPSrvrScanAction,
       "hmSecContFiltHTTPSrvrRowStatus": hmSecContFiltHTTPSrvrRowStatus,
       "hmSecContFiltHTTPSrvrComment": hmSecContFiltHTTPSrvrComment,
       "hmSecContFiltPOP3": hmSecContFiltPOP3,
       "hmSecContFiltPOP3Enable": hmSecContFiltPOP3Enable,
       "hmSecContFiltPOP3VirusAction": hmSecContFiltPOP3VirusAction,
       "hmSecContFiltPOP3MaxSize": hmSecContFiltPOP3MaxSize,
       "hmSecContFiltPOP3ExceedAction": hmSecContFiltPOP3ExceedAction,
       "hmSecContFiltPOP3SrvrTable": hmSecContFiltPOP3SrvrTable,
       "hmSecContFiltPOP3SrvrEntry": hmSecContFiltPOP3SrvrEntry,
       "hmSecContFiltPOP3SrvrIndex": hmSecContFiltPOP3SrvrIndex,
       "hmSecContFiltPOP3SrvrIP": hmSecContFiltPOP3SrvrIP,
       "hmSecContFiltPOP3SrvrPort": hmSecContFiltPOP3SrvrPort,
       "hmSecContFiltPOP3SrvrScanAction": hmSecContFiltPOP3SrvrScanAction,
       "hmSecContFiltPOP3SrvrRowStatus": hmSecContFiltPOP3SrvrRowStatus,
       "hmSecContFiltPOP3SrvrComment": hmSecContFiltPOP3SrvrComment,
       "hmSecContFiltSMTP": hmSecContFiltSMTP,
       "hmSecContFiltSMTPEnable": hmSecContFiltSMTPEnable,
       "hmSecContFiltSMTPVirusAction": hmSecContFiltSMTPVirusAction,
       "hmSecContFiltSMTPMaxSize": hmSecContFiltSMTPMaxSize,
       "hmSecContFiltSMTPExceedAction": hmSecContFiltSMTPExceedAction,
       "hmSecContFiltSMTPSrvrTable": hmSecContFiltSMTPSrvrTable,
       "hmSecContFiltSMTPSrvrEntry": hmSecContFiltSMTPSrvrEntry,
       "hmSecContFiltSMTPSrvrIndex": hmSecContFiltSMTPSrvrIndex,
       "hmSecContFiltSMTPSrvrIP": hmSecContFiltSMTPSrvrIP,
       "hmSecContFiltSMTPSrvrPort": hmSecContFiltSMTPSrvrPort,
       "hmSecContFiltSMTPSrvrScanAction": hmSecContFiltSMTPSrvrScanAction,
       "hmSecContFiltSMTPSrvrRowStatus": hmSecContFiltSMTPSrvrRowStatus,
       "hmSecContFiltSMTPSrvrComment": hmSecContFiltSMTPSrvrComment,
       "hmSecContFiltFTP": hmSecContFiltFTP,
       "hmSecContFiltFTPEnable": hmSecContFiltFTPEnable,
       "hmSecContFiltFTPVirusAction": hmSecContFiltFTPVirusAction,
       "hmSecContFiltFTPMaxSize": hmSecContFiltFTPMaxSize,
       "hmSecContFiltFTPExceedAction": hmSecContFiltFTPExceedAction,
       "hmSecContFiltFTPSrvrTable": hmSecContFiltFTPSrvrTable,
       "hmSecContFiltFTPSrvrEntry": hmSecContFiltFTPSrvrEntry,
       "hmSecContFiltFTPSrvrIndex": hmSecContFiltFTPSrvrIndex,
       "hmSecContFiltFTPSrvrIP": hmSecContFiltFTPSrvrIP,
       "hmSecContFiltFTPSrvrPort": hmSecContFiltFTPSrvrPort,
       "hmSecContFiltFTPSrvrScanAction": hmSecContFiltFTPSrvrScanAction,
       "hmSecContFiltFTPSrvrRowStatus": hmSecContFiltFTPSrvrRowStatus,
       "hmSecContFiltFTPSrvrComment": hmSecContFiltFTPSrvrComment,
       "hmSecBlade": hmSecBlade,
       "hmSecBladeRackID": hmSecBladeRackID,
       "hmSecBladeSlotID": hmSecBladeSlotID,
       "hmSecBladeCtrlTable": hmSecBladeCtrlTable,
       "hmSecBladeCtrlEntry": hmSecBladeCtrlEntry,
       "hmSecBladeCtrlIndex": hmSecBladeCtrlIndex,
       "hmSecBladeCtrlDevice": hmSecBladeCtrlDevice,
       "hmSecBladeCtrlStatus": hmSecBladeCtrlStatus,
       "hmSecBladeCtrlAVRRevision": hmSecBladeCtrlAVRRevision,
       "hmSecBladeCtrlSlotID": hmSecBladeCtrlSlotID,
       "hmSecBladeCtrlProductID": hmSecBladeCtrlProductID,
       "hmSecBladeCtrlAssemblyID": hmSecBladeCtrlAssemblyID,
       "hmSecBladeCtrlSerial": hmSecBladeCtrlSerial,
       "hmSecBladeCtrlFlashID": hmSecBladeCtrlFlashID,
       "hmSecBladeCtrlVersion": hmSecBladeCtrlVersion,
       "hmSecBladeCtrlBackup": hmSecBladeCtrlBackup,
       "hmSecBladeCtrlReconfig": hmSecBladeCtrlReconfig,
       "hmSecBladePwrTable": hmSecBladePwrTable,
       "hmSecBladePwrEntry": hmSecBladePwrEntry,
       "hmSecBladePwrIndex": hmSecBladePwrIndex,
       "hmSecBladePwrStatus": hmSecBladePwrStatus,
       "hmSecProfile": hmSecProfile,
       "hmSecProfilePush": hmSecProfilePush,
       "hmSecProfilePull": hmSecProfilePull,
       "hmSecProfilePullSchedule": hmSecProfilePullSchedule,
       "hmSecProfilePullHTTPS": hmSecProfilePullHTTPS,
       "hmSecProfilePullHTTPSCert": hmSecProfilePullHTTPSCert,
       "hmSecProfilePullHTTPSServer": hmSecProfilePullHTTPSServer,
       "hmSecProfilePullHTTPSPort": hmSecProfilePullHTTPSPort,
       "hmSecProfilePullHTTPSFile": hmSecProfilePullHTTPSFile,
       "hmSecProfilePullHTTPSLogin": hmSecProfilePullHTTPSLogin,
       "hmSecProfilePullHTTPSPasswd": hmSecProfilePullHTTPSPasswd,
       "hmSecProfilePullHTTPSDirectory": hmSecProfilePullHTTPSDirectory}
)
