# SNMP MIB module (SMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SMC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:50 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

supermicro = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876)
)
if mibBuilder.loadTexts:
    supermicro.setRevisions(
        ("2014-09-16 17:29",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cmm_ObjectIdentity = ObjectIdentity
cmm = _Cmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1)
)
_NetMACAddr_Type = PhysAddress
_NetMACAddr_Object = MibScalar
netMACAddr = _NetMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 2),
    _NetMACAddr_Type()
)
netMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMACAddr.setStatus("current")


class _NetIPAutoConf_Type(Integer32):
    """Custom type netIPAutoConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dhcp", 1),
          ("bootp", 2))
    )


_NetIPAutoConf_Type.__name__ = "Integer32"
_NetIPAutoConf_Object = MibScalar
netIPAutoConf = _NetIPAutoConf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 3),
    _NetIPAutoConf_Type()
)
netIPAutoConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIPAutoConf.setStatus("current")


class _NetHostName_Type(OctetString):
    """Custom type netHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NetHostName_Type.__name__ = "OctetString"
_NetHostName_Object = MibScalar
netHostName = _NetHostName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 4),
    _NetHostName_Type()
)
netHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHostName.setStatus("current")
_NetIPAddr_Type = IpAddress
_NetIPAddr_Object = MibScalar
netIPAddr = _NetIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 5),
    _NetIPAddr_Type()
)
netIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIPAddr.setStatus("current")
_NetNetmask_Type = IpAddress
_NetNetmask_Object = MibScalar
netNetmask = _NetNetmask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 6),
    _NetNetmask_Type()
)
netNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netNetmask.setStatus("current")
_NetGateway_Type = IpAddress
_NetGateway_Object = MibScalar
netGateway = _NetGateway_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 7),
    _NetGateway_Type()
)
netGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netGateway.setStatus("current")
_NetDNS1_Type = IpAddress
_NetDNS1_Object = MibScalar
netDNS1 = _NetDNS1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 8),
    _NetDNS1_Type()
)
netDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDNS1.setStatus("current")
_NetDNS2_Type = IpAddress
_NetDNS2_Object = MibScalar
netDNS2 = _NetDNS2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 9),
    _NetDNS2_Type()
)
netDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDNS2.setStatus("current")
_NetPortHTTPS_Type = Integer32
_NetPortHTTPS_Object = MibScalar
netPortHTTPS = _NetPortHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 11),
    _NetPortHTTPS_Type()
)
netPortHTTPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPortHTTPS.setStatus("current")
_NetPortHTTP_Type = Integer32
_NetPortHTTP_Object = MibScalar
netPortHTTP = _NetPortHTTP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 12),
    _NetPortHTTP_Type()
)
netPortHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPortHTTP.setStatus("current")
_NetPortSSH_Type = Integer32
_NetPortSSH_Object = MibScalar
netPortSSH = _NetPortSSH_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 13),
    _NetPortSSH_Type()
)
netPortSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPortSSH.setStatus("current")


class _NetBandWidthLimit_Type(Integer32):
    """Custom type netBandWidthLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_NetBandWidthLimit_Type.__name__ = "Integer32"
_NetBandWidthLimit_Object = MibScalar
netBandWidthLimit = _NetBandWidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 14),
    _NetBandWidthLimit_Type()
)
netBandWidthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBandWidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    netBandWidthLimit.setUnits("kbit/s")


class _NetSSHAccess_Type(Integer32):
    """Custom type netSSHAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NetSSHAccess_Type.__name__ = "Integer32"
_NetSSHAccess_Object = MibScalar
netSSHAccess = _NetSSHAccess_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 15),
    _NetSSHAccess_Type()
)
netSSHAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSSHAccess.setStatus("current")


class _NetSetupProtocol_Type(Integer32):
    """Custom type netSetupProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NetSetupProtocol_Type.__name__ = "Integer32"
_NetSetupProtocol_Object = MibScalar
netSetupProtocol = _NetSetupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 16),
    _NetSetupProtocol_Type()
)
netSetupProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSetupProtocol.setStatus("current")


class _NetLANSpeed_Type(Integer32):
    """Custom type netLANSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 0),
          ("spd10M", 1),
          ("spd100M", 2))
    )


_NetLANSpeed_Type.__name__ = "Integer32"
_NetLANSpeed_Object = MibScalar
netLANSpeed = _NetLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 18),
    _NetLANSpeed_Type()
)
netLANSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLANSpeed.setStatus("current")


class _NetLANDuplexMode_Type(Integer32):
    """Custom type netLANDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 0),
          ("halfDuplex", 1),
          ("fullDeplex", 2))
    )


_NetLANDuplexMode_Type.__name__ = "Integer32"
_NetLANDuplexMode_Object = MibScalar
netLANDuplexMode = _NetLANDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 19),
    _NetLANDuplexMode_Type()
)
netLANDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLANDuplexMode.setStatus("current")


class _NetDDNSStatus_Type(Integer32):
    """Custom type netDDNSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NetDDNSStatus_Type.__name__ = "Integer32"
_NetDDNSStatus_Object = MibScalar
netDDNSStatus = _NetDDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 21),
    _NetDDNSStatus_Type()
)
netDDNSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSStatus.setStatus("current")
_NetDDNSServer_Type = OctetString
_NetDDNSServer_Object = MibScalar
netDDNSServer = _NetDDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 22),
    _NetDDNSServer_Type()
)
netDDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netDDNSServer.setStatus("current")


class _NetDDNSSystemMode_Type(Integer32):
    """Custom type netDDNSSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("custom", 1))
    )


_NetDDNSSystemMode_Type.__name__ = "Integer32"
_NetDDNSSystemMode_Object = MibScalar
netDDNSSystemMode = _NetDDNSSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 23),
    _NetDDNSSystemMode_Type()
)
netDDNSSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSSystemMode.setStatus("current")
_NetDDNSHostName_Type = OctetString
_NetDDNSHostName_Object = MibScalar
netDDNSHostName = _NetDDNSHostName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 24),
    _NetDDNSHostName_Type()
)
netDDNSHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSHostName.setStatus("current")
_NetDDNSUserName_Type = OctetString
_NetDDNSUserName_Object = MibScalar
netDDNSUserName = _NetDDNSUserName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 25),
    _NetDDNSUserName_Type()
)
netDDNSUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSUserName.setStatus("current")
_NetDDNSPassword_Type = OctetString
_NetDDNSPassword_Object = MibScalar
netDDNSPassword = _NetDDNSPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 26),
    _NetDDNSPassword_Type()
)
netDDNSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSPassword.setStatus("current")
_NetDDNSCheckTime_Type = OctetString
_NetDDNSCheckTime_Object = MibScalar
netDDNSCheckTime = _NetDDNSCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 27),
    _NetDDNSCheckTime_Type()
)
netDDNSCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSCheckTime.setStatus("current")


class _NetDDNSCheckInterval_Type(Integer32):
    """Custom type netDDNSCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("time24h", 0),
          ("time12h", 1),
          ("time6h", 2),
          ("time3h", 3),
          ("time2h", 4),
          ("time10min", 5),
          ("time1min", 6))
    )


_NetDDNSCheckInterval_Type.__name__ = "Integer32"
_NetDDNSCheckInterval_Object = MibScalar
netDDNSCheckInterval = _NetDDNSCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 28),
    _NetDDNSCheckInterval_Type()
)
netDDNSCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDDNSCheckInterval.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2)
)


class _SecForceWebHTTPS_Type(Integer32):
    """Custom type secForceWebHTTPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SecForceWebHTTPS_Type.__name__ = "Integer32"
_SecForceWebHTTPS_Object = MibScalar
secForceWebHTTPS = _SecForceWebHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 2),
    _SecForceWebHTTPS_Type()
)
secForceWebHTTPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secForceWebHTTPS.setStatus("current")


class _SecKVMEncryption_Type(Integer32):
    """Custom type secKVMEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("try", 1),
          ("force", 2))
    )


_SecKVMEncryption_Type.__name__ = "Integer32"
_SecKVMEncryption_Object = MibScalar
secKVMEncryption = _SecKVMEncryption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 3),
    _SecKVMEncryption_Type()
)
secKVMEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secKVMEncryption.setStatus("current")


class _SecIPFWStatus_Type(Integer32):
    """Custom type secIPFWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SecIPFWStatus_Type.__name__ = "Integer32"
_SecIPFWStatus_Object = MibScalar
secIPFWStatus = _SecIPFWStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 5),
    _SecIPFWStatus_Type()
)
secIPFWStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secIPFWStatus.setStatus("current")


class _SecIPFWDefaultPolicy_Type(Integer32):
    """Custom type secIPFWDefaultPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("drop", 1))
    )


_SecIPFWDefaultPolicy_Type.__name__ = "Integer32"
_SecIPFWDefaultPolicy_Object = MibScalar
secIPFWDefaultPolicy = _SecIPFWDefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 6),
    _SecIPFWDefaultPolicy_Type()
)
secIPFWDefaultPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secIPFWDefaultPolicy.setStatus("current")


class _SecLoginRetryCount_Type(Integer32):
    """Custom type secLoginRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1024),
    )


_SecLoginRetryCount_Type.__name__ = "Integer32"
_SecLoginRetryCount_Object = MibScalar
secLoginRetryCount = _SecLoginRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 8),
    _SecLoginRetryCount_Type()
)
secLoginRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secLoginRetryCount.setStatus("current")


class _SecLoginBlockTime_Type(Integer32):
    """Custom type secLoginBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10080),
    )


_SecLoginBlockTime_Type.__name__ = "Integer32"
_SecLoginBlockTime_Object = MibScalar
secLoginBlockTime = _SecLoginBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 9),
    _SecLoginBlockTime_Type()
)
secLoginBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secLoginBlockTime.setStatus("current")
if mibBuilder.loadTexts:
    secLoginBlockTime.setUnits("minute")


class _SecSMCRAKP_Type(Integer32):
    """Custom type secSMCRAKP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SecSMCRAKP_Type.__name__ = "Integer32"
_SecSMCRAKP_Object = MibScalar
secSMCRAKP = _SecSMCRAKP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 11),
    _SecSMCRAKP_Type()
)
secSMCRAKP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secSMCRAKP.setStatus("current")
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3)
)
_UserMgmtTable_Object = MibTable
userMgmtTable = _UserMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1)
)
if mibBuilder.loadTexts:
    userMgmtTable.setStatus("current")
_UserMgmtEntry_Object = MibTableRow
userMgmtEntry = _UserMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1)
)
userMgmtEntry.setIndexNames(
    (0, "SMC-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userMgmtEntry.setStatus("current")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIndex.setStatus("current")


class _UserPresence_Type(Integer32):
    """Custom type userPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_UserPresence_Type.__name__ = "Integer32"
_UserPresence_Object = MibTableColumn
userPresence = _UserPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 2),
    _UserPresence_Type()
)
userPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPresence.setStatus("current")


class _UserName_Type(OctetString):
    """Custom type userName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UserName_Type.__name__ = "OctetString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 3),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserFullName_Type(OctetString):
    """Custom type userFullName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UserFullName_Type.__name__ = "OctetString"
_UserFullName_Object = MibTableColumn
userFullName = _UserFullName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 4),
    _UserFullName_Type()
)
userFullName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userFullName.setStatus("current")


class _UserPassword_Type(OctetString):
    """Custom type userPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_UserPassword_Type.__name__ = "OctetString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 5),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")


class _UserEmail_Type(OctetString):
    """Custom type userEmail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UserEmail_Type.__name__ = "OctetString"
_UserEmail_Object = MibTableColumn
userEmail = _UserEmail_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 6),
    _UserEmail_Type()
)
userEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEmail.setStatus("current")


class _UserMobile_Type(OctetString):
    """Custom type userMobile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UserMobile_Type.__name__ = "OctetString"
_UserMobile_Object = MibTableColumn
userMobile = _UserMobile_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 7),
    _UserMobile_Type()
)
userMobile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userMobile.setStatus("current")


class _UserPriv_Type(Integer32):
    """Custom type userPriv based on Integer32"""
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
        *(("noaccess", 0),
          ("user", 1),
          ("operator", 2),
          ("administrator", 3),
          ("oem", 4))
    )


_UserPriv_Type.__name__ = "Integer32"
_UserPriv_Object = MibTableColumn
userPriv = _UserPriv_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 3, 1, 1, 8),
    _UserPriv_Type()
)
userPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPriv.setStatus("current")
_Blades_ObjectIdentity = ObjectIdentity
blades = _Blades_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4)
)
_BladeTable_Object = MibTable
bladeTable = _BladeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bladeTable.setStatus("current")
_BladeEntry_Object = MibTableRow
bladeEntry = _BladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1)
)
bladeEntry.setIndexNames(
    (0, "SMC-MIB", "bladeIndex"),
)
if mibBuilder.loadTexts:
    bladeEntry.setStatus("current")


class _BladeIndex_Type(Integer32):
    """Custom type bladeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BladeIndex_Type.__name__ = "Integer32"
_BladeIndex_Object = MibTableColumn
bladeIndex = _BladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 1),
    _BladeIndex_Type()
)
bladeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bladeIndex.setStatus("current")


class _BladeSlotID_Type(Integer32):
    """Custom type bladeSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BladeSlotID_Type.__name__ = "Integer32"
_BladeSlotID_Object = MibTableColumn
bladeSlotID = _BladeSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 2),
    _BladeSlotID_Type()
)
bladeSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSlotID.setStatus("current")


class _BladePresence_Type(Integer32):
    """Custom type bladePresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_BladePresence_Type.__name__ = "Integer32"
_BladePresence_Object = MibTableColumn
bladePresence = _BladePresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 3),
    _BladePresence_Type()
)
bladePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePresence.setStatus("current")
_BladeName_Type = OctetString
_BladeName_Object = MibTableColumn
bladeName = _BladeName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 4),
    _BladeName_Type()
)
bladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeName.setStatus("current")
_BladeModel_Type = OctetString
_BladeModel_Object = MibTableColumn
bladeModel = _BladeModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 5),
    _BladeModel_Type()
)
bladeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeModel.setStatus("current")


class _BladePowerStatus_Type(Integer32):
    """Custom type bladePowerStatus based on Integer32"""
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
        *(("powerOff", 0),
          ("powerOn", 1),
          ("powerReset", 2),
          ("powerGracefulShutdown", 3))
    )


_BladePowerStatus_Type.__name__ = "Integer32"
_BladePowerStatus_Object = MibTableColumn
bladePowerStatus = _BladePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 6),
    _BladePowerStatus_Type()
)
bladePowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePowerStatus.setStatus("current")
_BladePowerWatt_Type = Integer32
_BladePowerWatt_Object = MibTableColumn
bladePowerWatt = _BladePowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 7),
    _BladePowerWatt_Type()
)
bladePowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePowerWatt.setStatus("current")
if mibBuilder.loadTexts:
    bladePowerWatt.setUnits("W")


class _BladePowerControl_Type(Integer32):
    """Custom type bladePowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerCtrl0per", 0),
          ("powerCtrl50per", 1),
          ("powerCtrlFull", 2))
    )


_BladePowerControl_Type.__name__ = "Integer32"
_BladePowerControl_Object = MibTableColumn
bladePowerControl = _BladePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 8),
    _BladePowerControl_Type()
)
bladePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePowerControl.setStatus("current")


class _BladeACLostPolicy_Type(Integer32):
    """Custom type bladeACLostPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 0),
          ("powerOn", 1),
          ("lastState", 2))
    )


_BladeACLostPolicy_Type.__name__ = "Integer32"
_BladeACLostPolicy_Object = MibTableColumn
bladeACLostPolicy = _BladeACLostPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 9),
    _BladeACLostPolicy_Type()
)
bladeACLostPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeACLostPolicy.setStatus("current")


class _BladeKVMStatus_Type(Integer32):
    """Custom type bladeKVMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deselected", 0),
          ("selected", 1))
    )


_BladeKVMStatus_Type.__name__ = "Integer32"
_BladeKVMStatus_Object = MibTableColumn
bladeKVMStatus = _BladeKVMStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 10),
    _BladeKVMStatus_Type()
)
bladeKVMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeKVMStatus.setStatus("current")


class _BladeUID_Type(Integer32):
    """Custom type bladeUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_BladeUID_Type.__name__ = "Integer32"
_BladeUID_Object = MibTableColumn
bladeUID = _BladeUID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 11),
    _BladeUID_Type()
)
bladeUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeUID.setStatus("current")


class _BladeError_Type(Integer32):
    """Custom type bladeError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_BladeError_Type.__name__ = "Integer32"
_BladeError_Object = MibTableColumn
bladeError = _BladeError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 12),
    _BladeError_Type()
)
bladeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeError.setStatus("current")
_BladeMgmtIPAddr_Type = IpAddress
_BladeMgmtIPAddr_Object = MibTableColumn
bladeMgmtIPAddr = _BladeMgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 13),
    _BladeMgmtIPAddr_Type()
)
bladeMgmtIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMgmtIPAddr.setStatus("current")
_BladeSN_Type = OctetString
_BladeSN_Object = MibTableColumn
bladeSN = _BladeSN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 14),
    _BladeSN_Type()
)
bladeSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSN.setStatus("current")
_BladeBMCVersion_Type = OctetString
_BladeBMCVersion_Object = MibTableColumn
bladeBMCVersion = _BladeBMCVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 15),
    _BladeBMCVersion_Type()
)
bladeBMCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBMCVersion.setStatus("current")
_BladeBIOSVersion_Type = OctetString
_BladeBIOSVersion_Object = MibTableColumn
bladeBIOSVersion = _BladeBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 4, 1, 1, 16),
    _BladeBIOSVersion_Type()
)
bladeBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBIOSVersion.setStatus("current")
_Switches_ObjectIdentity = ObjectIdentity
switches = _Switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5)
)
_SwitchGBTable_Object = MibTable
switchGBTable = _SwitchGBTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1)
)
if mibBuilder.loadTexts:
    switchGBTable.setStatus("current")
_SwitchGBEntry_Object = MibTableRow
switchGBEntry = _SwitchGBEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1)
)
switchGBEntry.setIndexNames(
    (0, "SMC-MIB", "switchGBIndex"),
)
if mibBuilder.loadTexts:
    switchGBEntry.setStatus("current")


class _SwitchGBIndex_Type(Integer32):
    """Custom type switchGBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchGBIndex_Type.__name__ = "Integer32"
_SwitchGBIndex_Object = MibTableColumn
switchGBIndex = _SwitchGBIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 1),
    _SwitchGBIndex_Type()
)
switchGBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchGBIndex.setStatus("current")
_SwitchGBSlotID_Type = Integer32
_SwitchGBSlotID_Object = MibTableColumn
switchGBSlotID = _SwitchGBSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 2),
    _SwitchGBSlotID_Type()
)
switchGBSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBSlotID.setStatus("current")


class _SwitchGBPresence_Type(Integer32):
    """Custom type switchGBPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_SwitchGBPresence_Type.__name__ = "Integer32"
_SwitchGBPresence_Object = MibTableColumn
switchGBPresence = _SwitchGBPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 3),
    _SwitchGBPresence_Type()
)
switchGBPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBPresence.setStatus("current")
_SwitchGBName_Type = OctetString
_SwitchGBName_Object = MibTableColumn
switchGBName = _SwitchGBName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 4),
    _SwitchGBName_Type()
)
switchGBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBName.setStatus("current")


class _SwitchGBModel_Type(OctetString):
    """Custom type switchGBModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwitchGBModel_Type.__name__ = "OctetString"
_SwitchGBModel_Object = MibTableColumn
switchGBModel = _SwitchGBModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 5),
    _SwitchGBModel_Type()
)
switchGBModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBModel.setStatus("current")


class _SwitchGBPowerStatus_Type(Integer32):
    """Custom type switchGBPowerStatus based on Integer32"""
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
        *(("powerOff", 0),
          ("powerOn", 1),
          ("restart", 2),
          ("reset", 3),
          ("resetFactoryDefaults", 4))
    )


_SwitchGBPowerStatus_Type.__name__ = "Integer32"
_SwitchGBPowerStatus_Object = MibTableColumn
switchGBPowerStatus = _SwitchGBPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 6),
    _SwitchGBPowerStatus_Type()
)
switchGBPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchGBPowerStatus.setStatus("current")
_SwitchGBTemperature_Type = Integer32
_SwitchGBTemperature_Object = MibTableColumn
switchGBTemperature = _SwitchGBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 7),
    _SwitchGBTemperature_Type()
)
switchGBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBTemperature.setStatus("current")
if mibBuilder.loadTexts:
    switchGBTemperature.setUnits("C")


class _SwitchGBError_Type(Integer32):
    """Custom type switchGBError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_SwitchGBError_Type.__name__ = "Integer32"
_SwitchGBError_Object = MibTableColumn
switchGBError = _SwitchGBError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 8),
    _SwitchGBError_Type()
)
switchGBError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBError.setStatus("current")


class _SwitchGBInitialized_Type(Integer32):
    """Custom type switchGBInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ok", 1))
    )


_SwitchGBInitialized_Type.__name__ = "Integer32"
_SwitchGBInitialized_Object = MibTableColumn
switchGBInitialized = _SwitchGBInitialized_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 9),
    _SwitchGBInitialized_Type()
)
switchGBInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGBInitialized.setStatus("current")
_SwitchGB2V5_Type = OctetString
_SwitchGB2V5_Object = MibTableColumn
switchGB2V5 = _SwitchGB2V5_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 10),
    _SwitchGB2V5_Type()
)
switchGB2V5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGB2V5.setStatus("current")
if mibBuilder.loadTexts:
    switchGB2V5.setUnits("V")
_SwitchGB1V25_Type = OctetString
_SwitchGB1V25_Object = MibTableColumn
switchGB1V25 = _SwitchGB1V25_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 1, 1, 11),
    _SwitchGB1V25_Type()
)
switchGB1V25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchGB1V25.setStatus("current")
if mibBuilder.loadTexts:
    switchGB1V25.setUnits("V")
_Switch10GBTable_Object = MibTable
switch10GBTable = _Switch10GBTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2)
)
if mibBuilder.loadTexts:
    switch10GBTable.setStatus("current")
_Switch10GBEntry_Object = MibTableRow
switch10GBEntry = _Switch10GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1)
)
switch10GBEntry.setIndexNames(
    (0, "SMC-MIB", "switch10GBIndex"),
)
if mibBuilder.loadTexts:
    switch10GBEntry.setStatus("current")


class _Switch10GBIndex_Type(Integer32):
    """Custom type switch10GBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Switch10GBIndex_Type.__name__ = "Integer32"
_Switch10GBIndex_Object = MibTableColumn
switch10GBIndex = _Switch10GBIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 1),
    _Switch10GBIndex_Type()
)
switch10GBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switch10GBIndex.setStatus("current")
_Switch10GBSlotID_Type = Integer32
_Switch10GBSlotID_Object = MibTableColumn
switch10GBSlotID = _Switch10GBSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 2),
    _Switch10GBSlotID_Type()
)
switch10GBSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBSlotID.setStatus("current")


class _Switch10GBPresence_Type(Integer32):
    """Custom type switch10GBPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_Switch10GBPresence_Type.__name__ = "Integer32"
_Switch10GBPresence_Object = MibTableColumn
switch10GBPresence = _Switch10GBPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 3),
    _Switch10GBPresence_Type()
)
switch10GBPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBPresence.setStatus("current")
_Switch10GBName_Type = OctetString
_Switch10GBName_Object = MibTableColumn
switch10GBName = _Switch10GBName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 4),
    _Switch10GBName_Type()
)
switch10GBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBName.setStatus("current")


class _Switch10GBModel_Type(OctetString):
    """Custom type switch10GBModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Switch10GBModel_Type.__name__ = "OctetString"
_Switch10GBModel_Object = MibTableColumn
switch10GBModel = _Switch10GBModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 5),
    _Switch10GBModel_Type()
)
switch10GBModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBModel.setStatus("current")


class _Switch10GBPowerStatus_Type(Integer32):
    """Custom type switch10GBPowerStatus based on Integer32"""
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
        *(("powerOff", 0),
          ("powerOn", 1),
          ("restart", 2),
          ("reset", 3),
          ("resetFactoryDefaults", 4))
    )


_Switch10GBPowerStatus_Type.__name__ = "Integer32"
_Switch10GBPowerStatus_Object = MibTableColumn
switch10GBPowerStatus = _Switch10GBPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 6),
    _Switch10GBPowerStatus_Type()
)
switch10GBPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switch10GBPowerStatus.setStatus("current")
_Switch10GBTemperature_Type = Integer32
_Switch10GBTemperature_Object = MibTableColumn
switch10GBTemperature = _Switch10GBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 7),
    _Switch10GBTemperature_Type()
)
switch10GBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBTemperature.setStatus("current")
if mibBuilder.loadTexts:
    switch10GBTemperature.setUnits("C")


class _Switch10GBError_Type(Integer32):
    """Custom type switch10GBError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_Switch10GBError_Type.__name__ = "Integer32"
_Switch10GBError_Object = MibTableColumn
switch10GBError = _Switch10GBError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 8),
    _Switch10GBError_Type()
)
switch10GBError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBError.setStatus("current")


class _Switch10GBInitialized_Type(Integer32):
    """Custom type switch10GBInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ok", 1))
    )


_Switch10GBInitialized_Type.__name__ = "Integer32"
_Switch10GBInitialized_Object = MibTableColumn
switch10GBInitialized = _Switch10GBInitialized_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 9),
    _Switch10GBInitialized_Type()
)
switch10GBInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GBInitialized.setStatus("current")
_Switch10GB3V3_Type = OctetString
_Switch10GB3V3_Object = MibTableColumn
switch10GB3V3 = _Switch10GB3V3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 10),
    _Switch10GB3V3_Type()
)
switch10GB3V3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GB3V3.setStatus("current")
if mibBuilder.loadTexts:
    switch10GB3V3.setUnits("V")
_Switch10GB1V25_Type = OctetString
_Switch10GB1V25_Object = MibTableColumn
switch10GB1V25 = _Switch10GB1V25_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 2, 1, 11),
    _Switch10GB1V25_Type()
)
switch10GB1V25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch10GB1V25.setStatus("current")
if mibBuilder.loadTexts:
    switch10GB1V25.setUnits("V")
_Passthru10GBTable_Object = MibTable
passthru10GBTable = _Passthru10GBTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3)
)
if mibBuilder.loadTexts:
    passthru10GBTable.setStatus("current")
_Passthru10GBEntry_Object = MibTableRow
passthru10GBEntry = _Passthru10GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1)
)
passthru10GBEntry.setIndexNames(
    (0, "SMC-MIB", "passthru10GBIndex"),
)
if mibBuilder.loadTexts:
    passthru10GBEntry.setStatus("current")


class _Passthru10GBIndex_Type(Integer32):
    """Custom type passthru10GBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Passthru10GBIndex_Type.__name__ = "Integer32"
_Passthru10GBIndex_Object = MibTableColumn
passthru10GBIndex = _Passthru10GBIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 1),
    _Passthru10GBIndex_Type()
)
passthru10GBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    passthru10GBIndex.setStatus("current")
_Passthru10GBSlotID_Type = Integer32
_Passthru10GBSlotID_Object = MibTableColumn
passthru10GBSlotID = _Passthru10GBSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 2),
    _Passthru10GBSlotID_Type()
)
passthru10GBSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBSlotID.setStatus("current")


class _Passthru10GBPresence_Type(Integer32):
    """Custom type passthru10GBPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_Passthru10GBPresence_Type.__name__ = "Integer32"
_Passthru10GBPresence_Object = MibTableColumn
passthru10GBPresence = _Passthru10GBPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 3),
    _Passthru10GBPresence_Type()
)
passthru10GBPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBPresence.setStatus("current")
_Passthru10GBName_Type = OctetString
_Passthru10GBName_Object = MibTableColumn
passthru10GBName = _Passthru10GBName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 4),
    _Passthru10GBName_Type()
)
passthru10GBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBName.setStatus("current")


class _Passthru10GBModel_Type(OctetString):
    """Custom type passthru10GBModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Passthru10GBModel_Type.__name__ = "OctetString"
_Passthru10GBModel_Object = MibTableColumn
passthru10GBModel = _Passthru10GBModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 5),
    _Passthru10GBModel_Type()
)
passthru10GBModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBModel.setStatus("current")


class _Passthru10GBPowerStatus_Type(Integer32):
    """Custom type passthru10GBPowerStatus based on Integer32"""
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
        *(("powerOff", 0),
          ("powerOn", 1),
          ("restart", 2),
          ("reset", 3),
          ("resetFactoryDefaults", 4))
    )


_Passthru10GBPowerStatus_Type.__name__ = "Integer32"
_Passthru10GBPowerStatus_Object = MibTableColumn
passthru10GBPowerStatus = _Passthru10GBPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 6),
    _Passthru10GBPowerStatus_Type()
)
passthru10GBPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passthru10GBPowerStatus.setStatus("current")
_Passthru10GBTemperature_Type = Integer32
_Passthru10GBTemperature_Object = MibTableColumn
passthru10GBTemperature = _Passthru10GBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 7),
    _Passthru10GBTemperature_Type()
)
passthru10GBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBTemperature.setStatus("current")
if mibBuilder.loadTexts:
    passthru10GBTemperature.setUnits("C")


class _Passthru10GBError_Type(Integer32):
    """Custom type passthru10GBError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_Passthru10GBError_Type.__name__ = "Integer32"
_Passthru10GBError_Object = MibTableColumn
passthru10GBError = _Passthru10GBError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 8),
    _Passthru10GBError_Type()
)
passthru10GBError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBError.setStatus("current")


class _Passthru10GBInitialized_Type(Integer32):
    """Custom type passthru10GBInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ok", 1))
    )


_Passthru10GBInitialized_Type.__name__ = "Integer32"
_Passthru10GBInitialized_Object = MibTableColumn
passthru10GBInitialized = _Passthru10GBInitialized_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 9),
    _Passthru10GBInitialized_Type()
)
passthru10GBInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GBInitialized.setStatus("current")
_Passthru10GB3V3_Type = OctetString
_Passthru10GB3V3_Object = MibTableColumn
passthru10GB3V3 = _Passthru10GB3V3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 10),
    _Passthru10GB3V3_Type()
)
passthru10GB3V3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GB3V3.setStatus("current")
if mibBuilder.loadTexts:
    passthru10GB3V3.setUnits("V")
_Passthru10GB1V25_Type = OctetString
_Passthru10GB1V25_Object = MibTableColumn
passthru10GB1V25 = _Passthru10GB1V25_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 3, 1, 11),
    _Passthru10GB1V25_Type()
)
passthru10GB1V25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthru10GB1V25.setStatus("current")
if mibBuilder.loadTexts:
    passthru10GB1V25.setUnits("V")
_SwitchIBTable_Object = MibTable
switchIBTable = _SwitchIBTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4)
)
if mibBuilder.loadTexts:
    switchIBTable.setStatus("current")
_SwitchIBEntry_Object = MibTableRow
switchIBEntry = _SwitchIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1)
)
switchIBEntry.setIndexNames(
    (0, "SMC-MIB", "switchIBIndex"),
)
if mibBuilder.loadTexts:
    switchIBEntry.setStatus("current")


class _SwitchIBIndex_Type(Integer32):
    """Custom type switchIBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchIBIndex_Type.__name__ = "Integer32"
_SwitchIBIndex_Object = MibTableColumn
switchIBIndex = _SwitchIBIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 1),
    _SwitchIBIndex_Type()
)
switchIBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchIBIndex.setStatus("current")
_SwitchIBSlotID_Type = Integer32
_SwitchIBSlotID_Object = MibTableColumn
switchIBSlotID = _SwitchIBSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 2),
    _SwitchIBSlotID_Type()
)
switchIBSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBSlotID.setStatus("current")


class _SwitchIBPresence_Type(Integer32):
    """Custom type switchIBPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_SwitchIBPresence_Type.__name__ = "Integer32"
_SwitchIBPresence_Object = MibTableColumn
switchIBPresence = _SwitchIBPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 3),
    _SwitchIBPresence_Type()
)
switchIBPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBPresence.setStatus("current")
_SwitchIBName_Type = OctetString
_SwitchIBName_Object = MibTableColumn
switchIBName = _SwitchIBName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 4),
    _SwitchIBName_Type()
)
switchIBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBName.setStatus("current")


class _SwitchIBModel_Type(OctetString):
    """Custom type switchIBModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwitchIBModel_Type.__name__ = "OctetString"
_SwitchIBModel_Object = MibTableColumn
switchIBModel = _SwitchIBModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 5),
    _SwitchIBModel_Type()
)
switchIBModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBModel.setStatus("current")


class _SwitchIBPowerStatus_Type(Integer32):
    """Custom type switchIBPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 0),
          ("powerOn", 1),
          ("reset", 2))
    )


_SwitchIBPowerStatus_Type.__name__ = "Integer32"
_SwitchIBPowerStatus_Object = MibTableColumn
switchIBPowerStatus = _SwitchIBPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 6),
    _SwitchIBPowerStatus_Type()
)
switchIBPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIBPowerStatus.setStatus("current")
_SwitchIBTemperature_Type = Integer32
_SwitchIBTemperature_Object = MibTableColumn
switchIBTemperature = _SwitchIBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 7),
    _SwitchIBTemperature_Type()
)
switchIBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBTemperature.setStatus("current")
if mibBuilder.loadTexts:
    switchIBTemperature.setUnits("C")


class _SwitchIBInitialized_Type(Integer32):
    """Custom type switchIBInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ok", 1))
    )


_SwitchIBInitialized_Type.__name__ = "Integer32"
_SwitchIBInitialized_Object = MibTableColumn
switchIBInitialized = _SwitchIBInitialized_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 8),
    _SwitchIBInitialized_Type()
)
switchIBInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBInitialized.setStatus("current")
_SwitchIB3V3Aux_Type = OctetString
_SwitchIB3V3Aux_Object = MibTableColumn
switchIB3V3Aux = _SwitchIB3V3Aux_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 9),
    _SwitchIB3V3Aux_Type()
)
switchIB3V3Aux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIB3V3Aux.setStatus("current")
if mibBuilder.loadTexts:
    switchIB3V3Aux.setUnits("V")
_SwitchIB3V3_Type = OctetString
_SwitchIB3V3_Object = MibTableColumn
switchIB3V3 = _SwitchIB3V3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 10),
    _SwitchIB3V3_Type()
)
switchIB3V3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIB3V3.setStatus("current")
if mibBuilder.loadTexts:
    switchIB3V3.setUnits("V")
_SwitchIB1V8_Type = OctetString
_SwitchIB1V8_Object = MibTableColumn
switchIB1V8 = _SwitchIB1V8_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 11),
    _SwitchIB1V8_Type()
)
switchIB1V8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIB1V8.setStatus("current")
if mibBuilder.loadTexts:
    switchIB1V8.setUnits("V")
_SwitchIB1V2_Type = OctetString
_SwitchIB1V2_Object = MibTableColumn
switchIB1V2 = _SwitchIB1V2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 12),
    _SwitchIB1V2_Type()
)
switchIB1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIB1V2.setStatus("current")
if mibBuilder.loadTexts:
    switchIB1V2.setUnits("V")
_SwitchIBVVdd_Type = OctetString
_SwitchIBVVdd_Object = MibTableColumn
switchIBVVdd = _SwitchIBVVdd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 4, 1, 13),
    _SwitchIBVVdd_Type()
)
switchIBVVdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBVVdd.setStatus("current")
if mibBuilder.loadTexts:
    switchIBVVdd.setUnits("V")
_SwitchIBQDRTable_Object = MibTable
switchIBQDRTable = _SwitchIBQDRTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5)
)
if mibBuilder.loadTexts:
    switchIBQDRTable.setStatus("current")
_SwitchIBQDREntry_Object = MibTableRow
switchIBQDREntry = _SwitchIBQDREntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1)
)
switchIBQDREntry.setIndexNames(
    (0, "SMC-MIB", "switchIBQDRIndex"),
)
if mibBuilder.loadTexts:
    switchIBQDREntry.setStatus("current")


class _SwitchIBQDRIndex_Type(Integer32):
    """Custom type switchIBQDRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchIBQDRIndex_Type.__name__ = "Integer32"
_SwitchIBQDRIndex_Object = MibTableColumn
switchIBQDRIndex = _SwitchIBQDRIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 1),
    _SwitchIBQDRIndex_Type()
)
switchIBQDRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchIBQDRIndex.setStatus("current")
_SwitchIBQDRSlotID_Type = Integer32
_SwitchIBQDRSlotID_Object = MibTableColumn
switchIBQDRSlotID = _SwitchIBQDRSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 2),
    _SwitchIBQDRSlotID_Type()
)
switchIBQDRSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRSlotID.setStatus("current")


class _SwitchIBQDRPresence_Type(Integer32):
    """Custom type switchIBQDRPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_SwitchIBQDRPresence_Type.__name__ = "Integer32"
_SwitchIBQDRPresence_Object = MibTableColumn
switchIBQDRPresence = _SwitchIBQDRPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 3),
    _SwitchIBQDRPresence_Type()
)
switchIBQDRPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRPresence.setStatus("current")
_SwitchIBQDRName_Type = OctetString
_SwitchIBQDRName_Object = MibTableColumn
switchIBQDRName = _SwitchIBQDRName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 4),
    _SwitchIBQDRName_Type()
)
switchIBQDRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRName.setStatus("current")


class _SwitchIBQDRModel_Type(OctetString):
    """Custom type switchIBQDRModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwitchIBQDRModel_Type.__name__ = "OctetString"
_SwitchIBQDRModel_Object = MibTableColumn
switchIBQDRModel = _SwitchIBQDRModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 5),
    _SwitchIBQDRModel_Type()
)
switchIBQDRModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRModel.setStatus("current")


class _SwitchIBQDRPowerStatus_Type(Integer32):
    """Custom type switchIBQDRPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 0),
          ("powerOn", 1),
          ("reset", 2))
    )


_SwitchIBQDRPowerStatus_Type.__name__ = "Integer32"
_SwitchIBQDRPowerStatus_Object = MibTableColumn
switchIBQDRPowerStatus = _SwitchIBQDRPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 6),
    _SwitchIBQDRPowerStatus_Type()
)
switchIBQDRPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIBQDRPowerStatus.setStatus("current")
_SwitchIBQDRTemperature_Type = Integer32
_SwitchIBQDRTemperature_Object = MibTableColumn
switchIBQDRTemperature = _SwitchIBQDRTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 7),
    _SwitchIBQDRTemperature_Type()
)
switchIBQDRTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRTemperature.setStatus("current")
if mibBuilder.loadTexts:
    switchIBQDRTemperature.setUnits("C")


class _SwitchIBQDRInitialized_Type(Integer32):
    """Custom type switchIBQDRInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ok", 1))
    )


_SwitchIBQDRInitialized_Type.__name__ = "Integer32"
_SwitchIBQDRInitialized_Object = MibTableColumn
switchIBQDRInitialized = _SwitchIBQDRInitialized_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 8),
    _SwitchIBQDRInitialized_Type()
)
switchIBQDRInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRInitialized.setStatus("current")


class _SwitchIBQDRError_Type(Integer32):
    """Custom type switchIBQDRError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_SwitchIBQDRError_Type.__name__ = "Integer32"
_SwitchIBQDRError_Object = MibTableColumn
switchIBQDRError = _SwitchIBQDRError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 9),
    _SwitchIBQDRError_Type()
)
switchIBQDRError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDRError.setStatus("current")
_SwitchIBQDR3V3_Type = OctetString
_SwitchIBQDR3V3_Object = MibTableColumn
switchIBQDR3V3 = _SwitchIBQDR3V3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 10),
    _SwitchIBQDR3V3_Type()
)
switchIBQDR3V3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDR3V3.setStatus("current")
if mibBuilder.loadTexts:
    switchIBQDR3V3.setUnits("V")
_SwitchIBQDR1V25_Type = OctetString
_SwitchIBQDR1V25_Object = MibTableColumn
switchIBQDR1V25 = _SwitchIBQDR1V25_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 5, 1, 11),
    _SwitchIBQDR1V25_Type()
)
switchIBQDR1V25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBQDR1V25.setStatus("current")
if mibBuilder.loadTexts:
    switchIBQDR1V25.setUnits("V")
_SwitchIBFDRTable_Object = MibTable
switchIBFDRTable = _SwitchIBFDRTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6)
)
if mibBuilder.loadTexts:
    switchIBFDRTable.setStatus("current")
_SwitchIBFDREntry_Object = MibTableRow
switchIBFDREntry = _SwitchIBFDREntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1)
)
switchIBFDREntry.setIndexNames(
    (0, "SMC-MIB", "switchIBFDRIndex"),
)
if mibBuilder.loadTexts:
    switchIBFDREntry.setStatus("current")


class _SwitchIBFDRIndex_Type(Integer32):
    """Custom type switchIBFDRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchIBFDRIndex_Type.__name__ = "Integer32"
_SwitchIBFDRIndex_Object = MibTableColumn
switchIBFDRIndex = _SwitchIBFDRIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 1),
    _SwitchIBFDRIndex_Type()
)
switchIBFDRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchIBFDRIndex.setStatus("current")
_SwitchIBFDRSlotID_Type = Integer32
_SwitchIBFDRSlotID_Object = MibTableColumn
switchIBFDRSlotID = _SwitchIBFDRSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 2),
    _SwitchIBFDRSlotID_Type()
)
switchIBFDRSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRSlotID.setStatus("current")


class _SwitchIBFDRPresence_Type(Integer32):
    """Custom type switchIBFDRPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_SwitchIBFDRPresence_Type.__name__ = "Integer32"
_SwitchIBFDRPresence_Object = MibTableColumn
switchIBFDRPresence = _SwitchIBFDRPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 3),
    _SwitchIBFDRPresence_Type()
)
switchIBFDRPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRPresence.setStatus("current")
_SwitchIBFDRName_Type = OctetString
_SwitchIBFDRName_Object = MibTableColumn
switchIBFDRName = _SwitchIBFDRName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 4),
    _SwitchIBFDRName_Type()
)
switchIBFDRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRName.setStatus("current")


class _SwitchIBFDRModel_Type(OctetString):
    """Custom type switchIBFDRModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwitchIBFDRModel_Type.__name__ = "OctetString"
_SwitchIBFDRModel_Object = MibTableColumn
switchIBFDRModel = _SwitchIBFDRModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 5),
    _SwitchIBFDRModel_Type()
)
switchIBFDRModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRModel.setStatus("current")


class _SwitchIBFDRPowerStatus_Type(Integer32):
    """Custom type switchIBFDRPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 0),
          ("powerOn", 1),
          ("reset", 2))
    )


_SwitchIBFDRPowerStatus_Type.__name__ = "Integer32"
_SwitchIBFDRPowerStatus_Object = MibTableColumn
switchIBFDRPowerStatus = _SwitchIBFDRPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 6),
    _SwitchIBFDRPowerStatus_Type()
)
switchIBFDRPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIBFDRPowerStatus.setStatus("current")
_SwitchIBFDRTemp1_Type = Integer32
_SwitchIBFDRTemp1_Object = MibTableColumn
switchIBFDRTemp1 = _SwitchIBFDRTemp1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 7),
    _SwitchIBFDRTemp1_Type()
)
switchIBFDRTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRTemp1.setStatus("current")
if mibBuilder.loadTexts:
    switchIBFDRTemp1.setUnits("C")
_SwitchIBFDRTemp2_Type = Integer32
_SwitchIBFDRTemp2_Object = MibTableColumn
switchIBFDRTemp2 = _SwitchIBFDRTemp2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 8),
    _SwitchIBFDRTemp2_Type()
)
switchIBFDRTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRTemp2.setStatus("current")
if mibBuilder.loadTexts:
    switchIBFDRTemp2.setUnits("C")


class _SwitchIBFDRInitialized_Type(Integer32):
    """Custom type switchIBFDRInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ok", 1))
    )


_SwitchIBFDRInitialized_Type.__name__ = "Integer32"
_SwitchIBFDRInitialized_Object = MibTableColumn
switchIBFDRInitialized = _SwitchIBFDRInitialized_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 9),
    _SwitchIBFDRInitialized_Type()
)
switchIBFDRInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRInitialized.setStatus("current")


class _SwitchIBFDRError_Type(Integer32):
    """Custom type switchIBFDRError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("error", 1))
    )


_SwitchIBFDRError_Type.__name__ = "Integer32"
_SwitchIBFDRError_Object = MibTableColumn
switchIBFDRError = _SwitchIBFDRError_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 10),
    _SwitchIBFDRError_Type()
)
switchIBFDRError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDRError.setStatus("current")
_SwitchIBFDR3V3_Type = OctetString
_SwitchIBFDR3V3_Object = MibTableColumn
switchIBFDR3V3 = _SwitchIBFDR3V3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 11),
    _SwitchIBFDR3V3_Type()
)
switchIBFDR3V3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDR3V3.setStatus("current")
if mibBuilder.loadTexts:
    switchIBFDR3V3.setUnits("V")
_SwitchIBFDR1V2_Type = OctetString
_SwitchIBFDR1V2_Object = MibTableColumn
switchIBFDR1V2 = _SwitchIBFDR1V2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 12),
    _SwitchIBFDR1V2_Type()
)
switchIBFDR1V2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDR1V2.setStatus("current")
if mibBuilder.loadTexts:
    switchIBFDR1V2.setUnits("V")
_SwitchIBFDR0V9_Type = OctetString
_SwitchIBFDR0V9_Object = MibTableColumn
switchIBFDR0V9 = _SwitchIBFDR0V9_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 5, 6, 1, 13),
    _SwitchIBFDR0V9_Type()
)
switchIBFDR0V9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIBFDR0V9.setStatus("current")
if mibBuilder.loadTexts:
    switchIBFDR0V9.setUnits("V")
_PowerSupplies_ObjectIdentity = ObjectIdentity
powerSupplies = _PowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6)
)
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1)
)
psuEntry.setIndexNames(
    (0, "SMC-MIB", "psuIndex"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")


class _PsuIndex_Type(Integer32):
    """Custom type psuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PsuIndex_Type.__name__ = "Integer32"
_PsuIndex_Object = MibTableColumn
psuIndex = _PsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 1),
    _PsuIndex_Type()
)
psuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psuIndex.setStatus("current")
_PsuSlotID_Type = Integer32
_PsuSlotID_Object = MibTableColumn
psuSlotID = _PsuSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 2),
    _PsuSlotID_Type()
)
psuSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuSlotID.setStatus("current")


class _PsuPresence_Type(Integer32):
    """Custom type psuPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_PsuPresence_Type.__name__ = "Integer32"
_PsuPresence_Object = MibTableColumn
psuPresence = _PsuPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 3),
    _PsuPresence_Type()
)
psuPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuPresence.setStatus("current")
_PsuName_Type = OctetString
_PsuName_Object = MibTableColumn
psuName = _PsuName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 4),
    _PsuName_Type()
)
psuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuName.setStatus("current")


class _PsuModel_Type(OctetString):
    """Custom type psuModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PsuModel_Type.__name__ = "OctetString"
_PsuModel_Object = MibTableColumn
psuModel = _PsuModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 5),
    _PsuModel_Type()
)
psuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuModel.setStatus("current")


class _PsuPowerStatus_Type(Integer32):
    """Custom type psuPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 0),
          ("powerOn", 1),
          ("powerFailure", 2))
    )


_PsuPowerStatus_Type.__name__ = "Integer32"
_PsuPowerStatus_Object = MibTableColumn
psuPowerStatus = _PsuPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 6),
    _PsuPowerStatus_Type()
)
psuPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psuPowerStatus.setStatus("current")
_PsuTemperature_Type = OctetString
_PsuTemperature_Object = MibTableColumn
psuTemperature = _PsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 7),
    _PsuTemperature_Type()
)
psuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuTemperature.setStatus("current")
_PsuFAN1Speed_Type = Integer32
_PsuFAN1Speed_Object = MibTableColumn
psuFAN1Speed = _PsuFAN1Speed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 8),
    _PsuFAN1Speed_Type()
)
psuFAN1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuFAN1Speed.setStatus("current")
if mibBuilder.loadTexts:
    psuFAN1Speed.setUnits("RPM")
_PsuFAN2Speed_Type = Integer32
_PsuFAN2Speed_Object = MibTableColumn
psuFAN2Speed = _PsuFAN2Speed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 9),
    _PsuFAN2Speed_Type()
)
psuFAN2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuFAN2Speed.setStatus("current")
if mibBuilder.loadTexts:
    psuFAN2Speed.setUnits("RPM")
_PsuFAN3Speed_Type = Integer32
_PsuFAN3Speed_Object = MibTableColumn
psuFAN3Speed = _PsuFAN3Speed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 10),
    _PsuFAN3Speed_Type()
)
psuFAN3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuFAN3Speed.setStatus("current")
if mibBuilder.loadTexts:
    psuFAN3Speed.setUnits("RPM")
_PsuFAN4Speed_Type = Integer32
_PsuFAN4Speed_Object = MibTableColumn
psuFAN4Speed = _PsuFAN4Speed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 11),
    _PsuFAN4Speed_Type()
)
psuFAN4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuFAN4Speed.setStatus("current")
if mibBuilder.loadTexts:
    psuFAN4Speed.setUnits("RPM")
_PsuACInVoltage_Type = Integer32
_PsuACInVoltage_Object = MibTableColumn
psuACInVoltage = _PsuACInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 12),
    _PsuACInVoltage_Type()
)
psuACInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuACInVoltage.setStatus("current")
if mibBuilder.loadTexts:
    psuACInVoltage.setUnits("V")
_PsuMaxWatt_Type = Integer32
_PsuMaxWatt_Object = MibTableColumn
psuMaxWatt = _PsuMaxWatt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 13),
    _PsuMaxWatt_Type()
)
psuMaxWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuMaxWatt.setStatus("current")
if mibBuilder.loadTexts:
    psuMaxWatt.setUnits("W")
_PsuACInCurrent_Type = OctetString
_PsuACInCurrent_Object = MibTableColumn
psuACInCurrent = _PsuACInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 14),
    _PsuACInCurrent_Type()
)
psuACInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuACInCurrent.setStatus("current")
if mibBuilder.loadTexts:
    psuACInCurrent.setUnits("A")
_PsuDCOutCurrent_Type = OctetString
_PsuDCOutCurrent_Object = MibTableColumn
psuDCOutCurrent = _PsuDCOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 15),
    _PsuDCOutCurrent_Type()
)
psuDCOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuDCOutCurrent.setStatus("current")
if mibBuilder.loadTexts:
    psuDCOutCurrent.setUnits("A")
_PsuCurrentPwrUsage_Type = OctetString
_PsuCurrentPwrUsage_Object = MibTableColumn
psuCurrentPwrUsage = _PsuCurrentPwrUsage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 16),
    _PsuCurrentPwrUsage_Type()
)
psuCurrentPwrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuCurrentPwrUsage.setStatus("current")
if mibBuilder.loadTexts:
    psuCurrentPwrUsage.setUnits("%")
_PsuFWVersion_Type = OctetString
_PsuFWVersion_Object = MibTableColumn
psuFWVersion = _PsuFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 17),
    _PsuFWVersion_Type()
)
psuFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuFWVersion.setStatus("current")
_PsuFRUVersion_Type = OctetString
_PsuFRUVersion_Object = MibTableColumn
psuFRUVersion = _PsuFRUVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 1, 1, 18),
    _PsuFRUVersion_Type()
)
psuFRUVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuFRUVersion.setStatus("current")
_PwrTotalPower_Type = Integer32
_PwrTotalPower_Object = MibScalar
pwrTotalPower = _PwrTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 3),
    _PwrTotalPower_Type()
)
pwrTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrTotalPower.setStatus("current")
_PwrBladeReserved_Type = Integer32
_PwrBladeReserved_Object = MibScalar
pwrBladeReserved = _PwrBladeReserved_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 4),
    _PwrBladeReserved_Type()
)
pwrBladeReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrBladeReserved.setStatus("current")
_PwrPeripheralReserved_Type = Integer32
_PwrPeripheralReserved_Object = MibScalar
pwrPeripheralReserved = _PwrPeripheralReserved_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 5),
    _PwrPeripheralReserved_Type()
)
pwrPeripheralReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrPeripheralReserved.setStatus("current")
_PwrAvailablePower_Type = Integer32
_PwrAvailablePower_Object = MibScalar
pwrAvailablePower = _PwrAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 6),
    _PwrAvailablePower_Type()
)
pwrAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrAvailablePower.setStatus("current")
_PwrCurrentMaxTemp_Type = OctetString
_PwrCurrentMaxTemp_Object = MibScalar
pwrCurrentMaxTemp = _PwrCurrentMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 7),
    _PwrCurrentMaxTemp_Type()
)
pwrCurrentMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrCurrentMaxTemp.setStatus("current")
_PwrCurrentMaxTempModule_Type = OctetString
_PwrCurrentMaxTempModule_Object = MibScalar
pwrCurrentMaxTempModule = _PwrCurrentMaxTempModule_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 8),
    _PwrCurrentMaxTempModule_Type()
)
pwrCurrentMaxTempModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrCurrentMaxTempModule.setStatus("current")


class _PwrRedundancy_Type(Integer32):
    """Custom type pwrRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pwrRedundancyDisabled", 0),
          ("pwrRedundancyEnabled", 1))
    )


_PwrRedundancy_Type.__name__ = "Integer32"
_PwrRedundancy_Object = MibScalar
pwrRedundancy = _PwrRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 10),
    _PwrRedundancy_Type()
)
pwrRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrRedundancy.setStatus("current")


class _PwrPSUFanCtrl_Type(Integer32):
    """Custom type pwrPSUFanCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("userCtrl", 0),
          ("autoCtrl", 1))
    )


_PwrPSUFanCtrl_Type.__name__ = "Integer32"
_PwrPSUFanCtrl_Object = MibScalar
pwrPSUFanCtrl = _PwrPSUFanCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 12),
    _PwrPSUFanCtrl_Type()
)
pwrPSUFanCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrPSUFanCtrl.setStatus("current")


class _PwrPSUFanSpdCtrl_Type(Integer32):
    """Custom type pwrPSUFanSpdCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PwrPSUFanSpdCtrl_Type.__name__ = "Integer32"
_PwrPSUFanSpdCtrl_Object = MibScalar
pwrPSUFanSpdCtrl = _PwrPSUFanSpdCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 13),
    _PwrPSUFanSpdCtrl_Type()
)
pwrPSUFanSpdCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrPSUFanSpdCtrl.setStatus("current")
_Cmms_ObjectIdentity = ObjectIdentity
cmms = _Cmms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7)
)
_CmmTable_Object = MibTable
cmmTable = _CmmTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cmmTable.setStatus("current")
_CmmEntry_Object = MibTableRow
cmmEntry = _CmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1)
)
cmmEntry.setIndexNames(
    (0, "SMC-MIB", "cmmIndex"),
)
if mibBuilder.loadTexts:
    cmmEntry.setStatus("current")


class _CmmIndex_Type(Integer32):
    """Custom type cmmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmmIndex_Type.__name__ = "Integer32"
_CmmIndex_Object = MibTableColumn
cmmIndex = _CmmIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 1),
    _CmmIndex_Type()
)
cmmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmIndex.setStatus("current")
_CmmSlot_Type = Integer32
_CmmSlot_Object = MibTableColumn
cmmSlot = _CmmSlot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 2),
    _CmmSlot_Type()
)
cmmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSlot.setStatus("current")


class _CmmPresence_Type(Integer32):
    """Custom type cmmPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_CmmPresence_Type.__name__ = "Integer32"
_CmmPresence_Object = MibTableColumn
cmmPresence = _CmmPresence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 3),
    _CmmPresence_Type()
)
cmmPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPresence.setStatus("current")
_CmmName_Type = OctetString
_CmmName_Object = MibTableColumn
cmmName = _CmmName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 4),
    _CmmName_Type()
)
cmmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmName.setStatus("current")


class _CmmRole_Type(Integer32):
    """Custom type cmmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_CmmRole_Type.__name__ = "Integer32"
_CmmRole_Object = MibTableColumn
cmmRole = _CmmRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 5),
    _CmmRole_Type()
)
cmmRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmRole.setStatus("current")
_CmmIPAddr_Type = IpAddress
_CmmIPAddr_Object = MibTableColumn
cmmIPAddr = _CmmIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 6),
    _CmmIPAddr_Type()
)
cmmIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIPAddr.setStatus("current")


class _CmmStatus_Type(Integer32):
    """Custom type cmmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_CmmStatus_Type.__name__ = "Integer32"
_CmmStatus_Object = MibTableColumn
cmmStatus = _CmmStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 7),
    _CmmStatus_Type()
)
cmmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStatus.setStatus("current")
_CmmFWVersion_Type = OctetString
_CmmFWVersion_Object = MibTableColumn
cmmFWVersion = _CmmFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 8),
    _CmmFWVersion_Type()
)
cmmFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFWVersion.setStatus("current")
_CmmFWTag_Type = OctetString
_CmmFWTag_Object = MibTableColumn
cmmFWTag = _CmmFWTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 1, 1, 9),
    _CmmFWTag_Type()
)
cmmFWTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFWTag.setStatus("current")


class _CmmOperationMode_Type(Integer32):
    """Custom type cmmOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enterprise", 0),
          ("office", 1))
    )


_CmmOperationMode_Type.__name__ = "Integer32"
_CmmOperationMode_Object = MibScalar
cmmOperationMode = _CmmOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 2),
    _CmmOperationMode_Type()
)
cmmOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOperationMode.setStatus("current")
_CmmDateTime_Type = OctetString
_CmmDateTime_Object = MibScalar
cmmDateTime = _CmmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 3),
    _CmmDateTime_Type()
)
cmmDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmDateTime.setStatus("current")


class _CmmNTPStatus_Type(Integer32):
    """Custom type cmmNTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("userDefined", 0),
          ("ntpSync", 1))
    )


_CmmNTPStatus_Type.__name__ = "Integer32"
_CmmNTPStatus_Object = MibScalar
cmmNTPStatus = _CmmNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 4),
    _CmmNTPStatus_Type()
)
cmmNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmNTPStatus.setStatus("current")
_CmmNTPServer1_Type = IpAddress
_CmmNTPServer1_Object = MibScalar
cmmNTPServer1 = _CmmNTPServer1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 5),
    _CmmNTPServer1_Type()
)
cmmNTPServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmNTPServer1.setStatus("current")
_CmmNTPServer2_Type = IpAddress
_CmmNTPServer2_Object = MibScalar
cmmNTPServer2 = _CmmNTPServer2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 6),
    _CmmNTPServer2_Type()
)
cmmNTPServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmNTPServer2.setStatus("current")


class _CmmUTCOffset_Type(Integer32):
    """Custom type cmmUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-11, 12),
    )


_CmmUTCOffset_Type.__name__ = "Integer32"
_CmmUTCOffset_Object = MibScalar
cmmUTCOffset = _CmmUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 7, 7),
    _CmmUTCOffset_Type()
)
cmmUTCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmUTCOffset.setStatus("current")
_Fru_ObjectIdentity = ObjectIdentity
fru = _Fru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8)
)
_FruTable_Object = MibTable
fruTable = _FruTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1)
)
if mibBuilder.loadTexts:
    fruTable.setStatus("obsolete")
_FruEntry_Object = MibTableRow
fruEntry = _FruEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1)
)
fruEntry.setIndexNames(
    (0, "SMC-MIB", "fruTableIndex"),
)
if mibBuilder.loadTexts:
    fruEntry.setStatus("obsolete")


class _FruTableIndex_Type(Integer32):
    """Custom type fruTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FruTableIndex_Type.__name__ = "Integer32"
_FruTableIndex_Object = MibTableColumn
fruTableIndex = _FruTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 1),
    _FruTableIndex_Type()
)
fruTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fruTableIndex.setStatus("obsolete")


class _FruDeviceType_Type(Integer32):
    """Custom type fruDeviceType based on Integer32"""
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
        *(("cmm", 0),
          ("middlePlane", 1),
          ("switch", 2),
          ("powerSupply", 3),
          ("blade", 4))
    )


_FruDeviceType_Type.__name__ = "Integer32"
_FruDeviceType_Object = MibTableColumn
fruDeviceType = _FruDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 2),
    _FruDeviceType_Type()
)
fruDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDeviceType.setStatus("obsolete")
_FruDeviceSlot_Type = Unsigned32
_FruDeviceSlot_Object = MibTableColumn
fruDeviceSlot = _FruDeviceSlot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 3),
    _FruDeviceSlot_Type()
)
fruDeviceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDeviceSlot.setStatus("obsolete")
_FruDevID_Type = Unsigned32
_FruDevID_Object = MibTableColumn
fruDevID = _FruDevID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 4),
    _FruDevID_Type()
)
fruDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDevID.setStatus("obsolete")


class _FruChassisType_Type(Integer32):
    """Custom type fruChassisType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("other", 1),
          ("unknown", 2),
          ("desktop", 3),
          ("lowProfileDesktop", 4),
          ("pizzaBox", 5),
          ("miniTower", 6),
          ("tower", 7),
          ("portable", 8),
          ("laptop", 9),
          ("notebook", 10),
          ("handHeld", 11),
          ("dockingStation", 12),
          ("allInOne", 13),
          ("subNotebook", 14),
          ("spaceSaving", 15),
          ("lunchBox", 16),
          ("mainServerChassis", 17),
          ("expansionChassis", 18),
          ("subChassis", 19),
          ("busExpansionChassis", 20),
          ("peripheralChassis", 21),
          ("raidChassis", 22),
          ("rackMountChassis", 23))
    )


_FruChassisType_Type.__name__ = "Integer32"
_FruChassisType_Object = MibTableColumn
fruChassisType = _FruChassisType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 5),
    _FruChassisType_Type()
)
fruChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruChassisType.setStatus("obsolete")
_FruChassisTypeCode_Type = Unsigned32
_FruChassisTypeCode_Object = MibTableColumn
fruChassisTypeCode = _FruChassisTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 6),
    _FruChassisTypeCode_Type()
)
fruChassisTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruChassisTypeCode.setStatus("obsolete")
_FruChassisPN_Type = OctetString
_FruChassisPN_Object = MibTableColumn
fruChassisPN = _FruChassisPN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 7),
    _FruChassisPN_Type()
)
fruChassisPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruChassisPN.setStatus("obsolete")
_FruChassisSN_Type = OctetString
_FruChassisSN_Object = MibTableColumn
fruChassisSN = _FruChassisSN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 8),
    _FruChassisSN_Type()
)
fruChassisSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruChassisSN.setStatus("obsolete")


class _FruBoardLang_Type(Integer32):
    """Custom type fruBoardLang based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("english", 0)
    )


_FruBoardLang_Type.__name__ = "Integer32"
_FruBoardLang_Object = MibTableColumn
fruBoardLang = _FruBoardLang_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 9),
    _FruBoardLang_Type()
)
fruBoardLang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardLang.setStatus("obsolete")
_FruBoardLangCode_Type = Unsigned32
_FruBoardLangCode_Object = MibTableColumn
fruBoardLangCode = _FruBoardLangCode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 10),
    _FruBoardLangCode_Type()
)
fruBoardLangCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardLangCode.setStatus("obsolete")
_FruBoardMfgDatetime_Type = OctetString
_FruBoardMfgDatetime_Object = MibTableColumn
fruBoardMfgDatetime = _FruBoardMfgDatetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 11),
    _FruBoardMfgDatetime_Type()
)
fruBoardMfgDatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardMfgDatetime.setStatus("obsolete")
_FruBoardMfgName_Type = OctetString
_FruBoardMfgName_Object = MibTableColumn
fruBoardMfgName = _FruBoardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 12),
    _FruBoardMfgName_Type()
)
fruBoardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardMfgName.setStatus("obsolete")
_FruBoardProdName_Type = OctetString
_FruBoardProdName_Object = MibTableColumn
fruBoardProdName = _FruBoardProdName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 13),
    _FruBoardProdName_Type()
)
fruBoardProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardProdName.setStatus("obsolete")
_FruBoardSN_Type = OctetString
_FruBoardSN_Object = MibTableColumn
fruBoardSN = _FruBoardSN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 14),
    _FruBoardSN_Type()
)
fruBoardSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardSN.setStatus("obsolete")
_FruBoardPN_Type = OctetString
_FruBoardPN_Object = MibTableColumn
fruBoardPN = _FruBoardPN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 15),
    _FruBoardPN_Type()
)
fruBoardPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBoardPN.setStatus("obsolete")


class _FruProdLang_Type(Integer32):
    """Custom type fruProdLang based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("english", 0)
    )


_FruProdLang_Type.__name__ = "Integer32"
_FruProdLang_Object = MibTableColumn
fruProdLang = _FruProdLang_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 16),
    _FruProdLang_Type()
)
fruProdLang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdLang.setStatus("obsolete")
_FruProdLangCode_Type = Unsigned32
_FruProdLangCode_Object = MibTableColumn
fruProdLangCode = _FruProdLangCode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 17),
    _FruProdLangCode_Type()
)
fruProdLangCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdLangCode.setStatus("obsolete")
_FruProdMfgName_Type = OctetString
_FruProdMfgName_Object = MibTableColumn
fruProdMfgName = _FruProdMfgName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 18),
    _FruProdMfgName_Type()
)
fruProdMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdMfgName.setStatus("obsolete")
_FruProdProdName_Type = OctetString
_FruProdProdName_Object = MibTableColumn
fruProdProdName = _FruProdProdName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 19),
    _FruProdProdName_Type()
)
fruProdProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdProdName.setStatus("obsolete")
_FruProdPN_Type = OctetString
_FruProdPN_Object = MibTableColumn
fruProdPN = _FruProdPN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 20),
    _FruProdPN_Type()
)
fruProdPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdPN.setStatus("obsolete")
_FruProdVersion_Type = OctetString
_FruProdVersion_Object = MibTableColumn
fruProdVersion = _FruProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 21),
    _FruProdVersion_Type()
)
fruProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdVersion.setStatus("obsolete")
_FruProdSN_Type = OctetString
_FruProdSN_Object = MibTableColumn
fruProdSN = _FruProdSN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 22),
    _FruProdSN_Type()
)
fruProdSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdSN.setStatus("obsolete")
_FruProdAssetTag_Type = OctetString
_FruProdAssetTag_Object = MibTableColumn
fruProdAssetTag = _FruProdAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 8, 1, 1, 23),
    _FruProdAssetTag_Type()
)
fruProdAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruProdAssetTag.setStatus("obsolete")
_VirtualMedias_ObjectIdentity = ObjectIdentity
virtualMedias = _VirtualMedias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9)
)
_FloppyActiveImage1_Type = OctetString
_FloppyActiveImage1_Object = MibScalar
floppyActiveImage1 = _FloppyActiveImage1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 1),
    _FloppyActiveImage1_Type()
)
floppyActiveImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floppyActiveImage1.setStatus("obsolete")
_FloppyActiveImage2_Type = OctetString
_FloppyActiveImage2_Object = MibScalar
floppyActiveImage2 = _FloppyActiveImage2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 2),
    _FloppyActiveImage2_Type()
)
floppyActiveImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floppyActiveImage2.setStatus("obsolete")
_CdromActiveImage1_Type = OctetString
_CdromActiveImage1_Object = MibScalar
cdromActiveImage1 = _CdromActiveImage1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 3),
    _CdromActiveImage1_Type()
)
cdromActiveImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdromActiveImage1.setStatus("obsolete")
_CdromActiveImage2_Type = OctetString
_CdromActiveImage2_Object = MibScalar
cdromActiveImage2 = _CdromActiveImage2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 4),
    _CdromActiveImage2_Type()
)
cdromActiveImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdromActiveImage2.setStatus("obsolete")
_DrvRedirActiveImage1_Type = OctetString
_DrvRedirActiveImage1_Object = MibScalar
drvRedirActiveImage1 = _DrvRedirActiveImage1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 5),
    _DrvRedirActiveImage1_Type()
)
drvRedirActiveImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drvRedirActiveImage1.setStatus("obsolete")
_DrvRedirActiveImage2_Type = OctetString
_DrvRedirActiveImage2_Object = MibScalar
drvRedirActiveImage2 = _DrvRedirActiveImage2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 6),
    _DrvRedirActiveImage2_Type()
)
drvRedirActiveImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drvRedirActiveImage2.setStatus("obsolete")


class _DrvRedirStatus_Type(Integer32):
    """Custom type drvRedirStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DrvRedirStatus_Type.__name__ = "Integer32"
_DrvRedirStatus_Object = MibScalar
drvRedirStatus = _DrvRedirStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 7),
    _DrvRedirStatus_Type()
)
drvRedirStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drvRedirStatus.setStatus("current")


class _DrvRedirAccessType_Type(Integer32):
    """Custom type drvRedirAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("readwrite", 1))
    )


_DrvRedirAccessType_Type.__name__ = "Integer32"
_DrvRedirAccessType_Object = MibScalar
drvRedirAccessType = _DrvRedirAccessType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 8),
    _DrvRedirAccessType_Type()
)
drvRedirAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drvRedirAccessType.setStatus("current")


class _UsbEnableWithoutImage_Type(Integer32):
    """Custom type usbEnableWithoutImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UsbEnableWithoutImage_Type.__name__ = "Integer32"
_UsbEnableWithoutImage_Object = MibScalar
usbEnableWithoutImage = _UsbEnableWithoutImage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 9, 9),
    _UsbEnableWithoutImage_Type()
)
usbEnableWithoutImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbEnableWithoutImage.setStatus("current")
_KvmSettings_ObjectIdentity = ObjectIdentity
kvmSettings = _KvmSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 10)
)


class _KeyboardModel_Type(Integer32):
    """Custom type keyboardModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generic104KeyPC", 0),
          ("generic109KeyPC", 1),
          ("appleMacintosh", 2))
    )


_KeyboardModel_Type.__name__ = "Integer32"
_KeyboardModel_Object = MibScalar
keyboardModel = _KeyboardModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 10, 1),
    _KeyboardModel_Type()
)
keyboardModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyboardModel.setStatus("current")


class _KeyReleaseTimeoutStatus_Type(Integer32):
    """Custom type keyReleaseTimeoutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_KeyReleaseTimeoutStatus_Type.__name__ = "Integer32"
_KeyReleaseTimeoutStatus_Object = MibScalar
keyReleaseTimeoutStatus = _KeyReleaseTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 10, 2),
    _KeyReleaseTimeoutStatus_Type()
)
keyReleaseTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyReleaseTimeoutStatus.setStatus("current")


class _KeyReleaseTimeoutInterval_Type(Integer32):
    """Custom type keyReleaseTimeoutInterval based on Integer32"""
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
        *(("time25", 0),
          ("time50", 1),
          ("time100", 2),
          ("time200", 3))
    )


_KeyReleaseTimeoutInterval_Type.__name__ = "Integer32"
_KeyReleaseTimeoutInterval_Object = MibScalar
keyReleaseTimeoutInterval = _KeyReleaseTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 10, 3),
    _KeyReleaseTimeoutInterval_Type()
)
keyReleaseTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyReleaseTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    keyReleaseTimeoutInterval.setUnits("msec")


class _MouseType_Type(Integer32):
    """Custom type mouseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("relative", 0),
          ("absolute", 1))
    )


_MouseType_Type.__name__ = "Integer32"
_MouseType_Object = MibScalar
mouseType = _MouseType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 10, 4),
    _MouseType_Type()
)
mouseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mouseType.setStatus("current")


class _MouseSpeed_Type(Integer32):
    """Custom type mouseSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("scale1v025", 1),
          ("scale1v050", 2),
          ("scale1v100", 3),
          ("scale1v200", 4),
          ("scale1v400", 5))
    )


_MouseSpeed_Type.__name__ = "Integer32"
_MouseSpeed_Object = MibScalar
mouseSpeed = _MouseSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 10, 5),
    _MouseSpeed_Type()
)
mouseSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mouseSpeed.setStatus("current")
_EventLogging_ObjectIdentity = ObjectIdentity
eventLogging = _EventLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11)
)


class _EvtListLogStatus_Type(Integer32):
    """Custom type evtListLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EvtListLogStatus_Type.__name__ = "Integer32"
_EvtListLogStatus_Object = MibScalar
evtListLogStatus = _EvtListLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 2),
    _EvtListLogStatus_Type()
)
evtListLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtListLogStatus.setStatus("current")
_EvtListEntryPerPage_Type = Integer32
_EvtListEntryPerPage_Object = MibScalar
evtListEntryPerPage = _EvtListEntryPerPage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 3),
    _EvtListEntryPerPage_Type()
)
evtListEntryPerPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtListEntryPerPage.setStatus("current")


class _EvtListClearLog_Type(Integer32):
    """Custom type evtListClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("clear", 0)
    )


_EvtListClearLog_Type.__name__ = "Integer32"
_EvtListClearLog_Object = MibScalar
evtListClearLog = _EvtListClearLog_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 4),
    _EvtListClearLog_Type()
)
evtListClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtListClearLog.setStatus("current")


class _EvtNFSLogStatus_Type(Integer32):
    """Custom type evtNFSLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EvtNFSLogStatus_Type.__name__ = "Integer32"
_EvtNFSLogStatus_Object = MibScalar
evtNFSLogStatus = _EvtNFSLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 5),
    _EvtNFSLogStatus_Type()
)
evtNFSLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtNFSLogStatus.setStatus("current")
_EvtNFSServer_Type = OctetString
_EvtNFSServer_Object = MibScalar
evtNFSServer = _EvtNFSServer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 6),
    _EvtNFSServer_Type()
)
evtNFSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtNFSServer.setStatus("current")
_EvtNFSShare_Type = OctetString
_EvtNFSShare_Object = MibScalar
evtNFSShare = _EvtNFSShare_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 7),
    _EvtNFSShare_Type()
)
evtNFSShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtNFSShare.setStatus("current")
_EvtNFSLogFile_Type = OctetString
_EvtNFSLogFile_Object = MibScalar
evtNFSLogFile = _EvtNFSLogFile_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 8),
    _EvtNFSLogFile_Type()
)
evtNFSLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtNFSLogFile.setStatus("current")


class _EvtSMTPLogStatus_Type(Integer32):
    """Custom type evtSMTPLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EvtSMTPLogStatus_Type.__name__ = "Integer32"
_EvtSMTPLogStatus_Object = MibScalar
evtSMTPLogStatus = _EvtSMTPLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 9),
    _EvtSMTPLogStatus_Type()
)
evtSMTPLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSMTPLogStatus.setStatus("current")
_EvtSMTPServer_Type = OctetString
_EvtSMTPServer_Object = MibScalar
evtSMTPServer = _EvtSMTPServer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 10),
    _EvtSMTPServer_Type()
)
evtSMTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSMTPServer.setStatus("current")
_EvtSMTPRecvEmail_Type = OctetString
_EvtSMTPRecvEmail_Object = MibScalar
evtSMTPRecvEmail = _EvtSMTPRecvEmail_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 11),
    _EvtSMTPRecvEmail_Type()
)
evtSMTPRecvEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSMTPRecvEmail.setStatus("current")
_EvtSMTPSendEmail_Type = OctetString
_EvtSMTPSendEmail_Object = MibScalar
evtSMTPSendEmail = _EvtSMTPSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 12),
    _EvtSMTPSendEmail_Type()
)
evtSMTPSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSMTPSendEmail.setStatus("current")


class _EvtSNMPLogStatus_Type(Integer32):
    """Custom type evtSNMPLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EvtSNMPLogStatus_Type.__name__ = "Integer32"
_EvtSNMPLogStatus_Object = MibScalar
evtSNMPLogStatus = _EvtSNMPLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 13),
    _EvtSNMPLogStatus_Type()
)
evtSNMPLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSNMPLogStatus.setStatus("current")
_EvtSNMPDestIP_Type = OctetString
_EvtSNMPDestIP_Object = MibScalar
evtSNMPDestIP = _EvtSNMPDestIP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 14),
    _EvtSNMPDestIP_Type()
)
evtSNMPDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSNMPDestIP.setStatus("current")
_EvtSNMPCommunity_Type = OctetString
_EvtSNMPCommunity_Object = MibScalar
evtSNMPCommunity = _EvtSNMPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 15),
    _EvtSNMPCommunity_Type()
)
evtSNMPCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtSNMPCommunity.setStatus("current")

# Managed Objects groups

netGrpBasicSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 1)
)
netGrpBasicSettings.setObjects(
      *(("SMC-MIB", "netMACAddr"),
        ("SMC-MIB", "netIPAutoConf"),
        ("SMC-MIB", "netHostName"),
        ("SMC-MIB", "netIPAddr"),
        ("SMC-MIB", "netNetmask"),
        ("SMC-MIB", "netGateway"),
        ("SMC-MIB", "netDNS1"),
        ("SMC-MIB", "netDNS2"))
)
if mibBuilder.loadTexts:
    netGrpBasicSettings.setStatus("current")

netGrpMiscSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 10)
)
netGrpMiscSettings.setObjects(
      *(("SMC-MIB", "netPortHTTPS"),
        ("SMC-MIB", "netPortHTTP"),
        ("SMC-MIB", "netPortSSH"),
        ("SMC-MIB", "netBandWidthLimit"),
        ("SMC-MIB", "netSSHAccess"),
        ("SMC-MIB", "netSetupProtocol"))
)
if mibBuilder.loadTexts:
    netGrpMiscSettings.setStatus("current")

netGrpLANSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 17)
)
netGrpLANSettings.setObjects(
      *(("SMC-MIB", "netLANSpeed"),
        ("SMC-MIB", "netLANDuplexMode"))
)
if mibBuilder.loadTexts:
    netGrpLANSettings.setStatus("current")

netGrpDDNSSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 1, 20)
)
netGrpDDNSSettings.setObjects(
      *(("SMC-MIB", "netDDNSStatus"),
        ("SMC-MIB", "netDDNSServer"),
        ("SMC-MIB", "netDDNSSystemMode"),
        ("SMC-MIB", "netDDNSHostName"),
        ("SMC-MIB", "netDDNSUserName"),
        ("SMC-MIB", "netDDNSPassword"),
        ("SMC-MIB", "netDDNSCheckTime"),
        ("SMC-MIB", "netDDNSCheckInterval"))
)
if mibBuilder.loadTexts:
    netGrpDDNSSettings.setStatus("current")

secGrpEncryptionSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 1)
)
secGrpEncryptionSettings.setObjects(
      *(("SMC-MIB", "secForceWebHTTPS"),
        ("SMC-MIB", "secKVMEncryption"))
)
if mibBuilder.loadTexts:
    secGrpEncryptionSettings.setStatus("current")

secGrpIPAccessControl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 4)
)
secGrpIPAccessControl.setObjects(
      *(("SMC-MIB", "secIPFWStatus"),
        ("SMC-MIB", "secIPFWDefaultPolicy"))
)
if mibBuilder.loadTexts:
    secGrpIPAccessControl.setStatus("current")

secGrpLoginFailBlocking = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 7)
)
secGrpLoginFailBlocking.setObjects(
      *(("SMC-MIB", "secLoginRetryCount"),
        ("SMC-MIB", "secLoginBlockTime"))
)
if mibBuilder.loadTexts:
    secGrpLoginFailBlocking.setStatus("current")

secIPMISettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 2, 10)
)
secIPMISettings.setObjects(
    ("SMC-MIB", "secSMCRAKP")
)
if mibBuilder.loadTexts:
    secIPMISettings.setStatus("current")

pwrGrpConsumption = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 2)
)
pwrGrpConsumption.setObjects(
      *(("SMC-MIB", "pwrTotalPower"),
        ("SMC-MIB", "pwrBladeReserved"),
        ("SMC-MIB", "pwrPeripheralReserved"),
        ("SMC-MIB", "pwrAvailablePower"),
        ("SMC-MIB", "pwrCurrentMaxTemp"),
        ("SMC-MIB", "pwrCurrentMaxTempModule"))
)
if mibBuilder.loadTexts:
    pwrGrpConsumption.setStatus("current")

pwrGrpPSURedundancy = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 9)
)
pwrGrpPSURedundancy.setObjects(
    ("SMC-MIB", "pwrRedundancy")
)
if mibBuilder.loadTexts:
    pwrGrpPSURedundancy.setStatus("current")

pwrGrpPSUFanCtrl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 6, 11)
)
pwrGrpPSUFanCtrl.setObjects(
      *(("SMC-MIB", "pwrPSUFanCtrl"),
        ("SMC-MIB", "pwrPSUFanSpdCtrl"))
)
if mibBuilder.loadTexts:
    pwrGrpPSUFanCtrl.setStatus("current")

evtGrpLogTargetSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 1, 11, 1)
)
evtGrpLogTargetSettings.setObjects(
      *(("SMC-MIB", "evtListLogStatus"),
        ("SMC-MIB", "evtListEntryPerPage"),
        ("SMC-MIB", "evtListClearLog"),
        ("SMC-MIB", "evtNFSLogStatus"),
        ("SMC-MIB", "evtNFSServer"),
        ("SMC-MIB", "evtNFSShare"),
        ("SMC-MIB", "evtNFSLogFile"),
        ("SMC-MIB", "evtSMTPLogStatus"),
        ("SMC-MIB", "evtSMTPServer"),
        ("SMC-MIB", "evtSMTPRecvEmail"),
        ("SMC-MIB", "evtSMTPSendEmail"),
        ("SMC-MIB", "evtSNMPLogStatus"),
        ("SMC-MIB", "evtSNMPDestIP"),
        ("SMC-MIB", "evtSNMPCommunity"))
)
if mibBuilder.loadTexts:
    evtGrpLogTargetSettings.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMC-MIB",
    **{"supermicro": supermicro,
       "cmm": cmm,
       "network": network,
       "netGrpBasicSettings": netGrpBasicSettings,
       "netMACAddr": netMACAddr,
       "netIPAutoConf": netIPAutoConf,
       "netHostName": netHostName,
       "netIPAddr": netIPAddr,
       "netNetmask": netNetmask,
       "netGateway": netGateway,
       "netDNS1": netDNS1,
       "netDNS2": netDNS2,
       "netGrpMiscSettings": netGrpMiscSettings,
       "netPortHTTPS": netPortHTTPS,
       "netPortHTTP": netPortHTTP,
       "netPortSSH": netPortSSH,
       "netBandWidthLimit": netBandWidthLimit,
       "netSSHAccess": netSSHAccess,
       "netSetupProtocol": netSetupProtocol,
       "netGrpLANSettings": netGrpLANSettings,
       "netLANSpeed": netLANSpeed,
       "netLANDuplexMode": netLANDuplexMode,
       "netGrpDDNSSettings": netGrpDDNSSettings,
       "netDDNSStatus": netDDNSStatus,
       "netDDNSServer": netDDNSServer,
       "netDDNSSystemMode": netDDNSSystemMode,
       "netDDNSHostName": netDDNSHostName,
       "netDDNSUserName": netDDNSUserName,
       "netDDNSPassword": netDDNSPassword,
       "netDDNSCheckTime": netDDNSCheckTime,
       "netDDNSCheckInterval": netDDNSCheckInterval,
       "security": security,
       "secGrpEncryptionSettings": secGrpEncryptionSettings,
       "secForceWebHTTPS": secForceWebHTTPS,
       "secKVMEncryption": secKVMEncryption,
       "secGrpIPAccessControl": secGrpIPAccessControl,
       "secIPFWStatus": secIPFWStatus,
       "secIPFWDefaultPolicy": secIPFWDefaultPolicy,
       "secGrpLoginFailBlocking": secGrpLoginFailBlocking,
       "secLoginRetryCount": secLoginRetryCount,
       "secLoginBlockTime": secLoginBlockTime,
       "secIPMISettings": secIPMISettings,
       "secSMCRAKP": secSMCRAKP,
       "users": users,
       "userMgmtTable": userMgmtTable,
       "userMgmtEntry": userMgmtEntry,
       "userIndex": userIndex,
       "userPresence": userPresence,
       "userName": userName,
       "userFullName": userFullName,
       "userPassword": userPassword,
       "userEmail": userEmail,
       "userMobile": userMobile,
       "userPriv": userPriv,
       "blades": blades,
       "bladeTable": bladeTable,
       "bladeEntry": bladeEntry,
       "bladeIndex": bladeIndex,
       "bladeSlotID": bladeSlotID,
       "bladePresence": bladePresence,
       "bladeName": bladeName,
       "bladeModel": bladeModel,
       "bladePowerStatus": bladePowerStatus,
       "bladePowerWatt": bladePowerWatt,
       "bladePowerControl": bladePowerControl,
       "bladeACLostPolicy": bladeACLostPolicy,
       "bladeKVMStatus": bladeKVMStatus,
       "bladeUID": bladeUID,
       "bladeError": bladeError,
       "bladeMgmtIPAddr": bladeMgmtIPAddr,
       "bladeSN": bladeSN,
       "bladeBMCVersion": bladeBMCVersion,
       "bladeBIOSVersion": bladeBIOSVersion,
       "switches": switches,
       "switchGBTable": switchGBTable,
       "switchGBEntry": switchGBEntry,
       "switchGBIndex": switchGBIndex,
       "switchGBSlotID": switchGBSlotID,
       "switchGBPresence": switchGBPresence,
       "switchGBName": switchGBName,
       "switchGBModel": switchGBModel,
       "switchGBPowerStatus": switchGBPowerStatus,
       "switchGBTemperature": switchGBTemperature,
       "switchGBError": switchGBError,
       "switchGBInitialized": switchGBInitialized,
       "switchGB2V5": switchGB2V5,
       "switchGB1V25": switchGB1V25,
       "switch10GBTable": switch10GBTable,
       "switch10GBEntry": switch10GBEntry,
       "switch10GBIndex": switch10GBIndex,
       "switch10GBSlotID": switch10GBSlotID,
       "switch10GBPresence": switch10GBPresence,
       "switch10GBName": switch10GBName,
       "switch10GBModel": switch10GBModel,
       "switch10GBPowerStatus": switch10GBPowerStatus,
       "switch10GBTemperature": switch10GBTemperature,
       "switch10GBError": switch10GBError,
       "switch10GBInitialized": switch10GBInitialized,
       "switch10GB3V3": switch10GB3V3,
       "switch10GB1V25": switch10GB1V25,
       "passthru10GBTable": passthru10GBTable,
       "passthru10GBEntry": passthru10GBEntry,
       "passthru10GBIndex": passthru10GBIndex,
       "passthru10GBSlotID": passthru10GBSlotID,
       "passthru10GBPresence": passthru10GBPresence,
       "passthru10GBName": passthru10GBName,
       "passthru10GBModel": passthru10GBModel,
       "passthru10GBPowerStatus": passthru10GBPowerStatus,
       "passthru10GBTemperature": passthru10GBTemperature,
       "passthru10GBError": passthru10GBError,
       "passthru10GBInitialized": passthru10GBInitialized,
       "passthru10GB3V3": passthru10GB3V3,
       "passthru10GB1V25": passthru10GB1V25,
       "switchIBTable": switchIBTable,
       "switchIBEntry": switchIBEntry,
       "switchIBIndex": switchIBIndex,
       "switchIBSlotID": switchIBSlotID,
       "switchIBPresence": switchIBPresence,
       "switchIBName": switchIBName,
       "switchIBModel": switchIBModel,
       "switchIBPowerStatus": switchIBPowerStatus,
       "switchIBTemperature": switchIBTemperature,
       "switchIBInitialized": switchIBInitialized,
       "switchIB3V3Aux": switchIB3V3Aux,
       "switchIB3V3": switchIB3V3,
       "switchIB1V8": switchIB1V8,
       "switchIB1V2": switchIB1V2,
       "switchIBVVdd": switchIBVVdd,
       "switchIBQDRTable": switchIBQDRTable,
       "switchIBQDREntry": switchIBQDREntry,
       "switchIBQDRIndex": switchIBQDRIndex,
       "switchIBQDRSlotID": switchIBQDRSlotID,
       "switchIBQDRPresence": switchIBQDRPresence,
       "switchIBQDRName": switchIBQDRName,
       "switchIBQDRModel": switchIBQDRModel,
       "switchIBQDRPowerStatus": switchIBQDRPowerStatus,
       "switchIBQDRTemperature": switchIBQDRTemperature,
       "switchIBQDRInitialized": switchIBQDRInitialized,
       "switchIBQDRError": switchIBQDRError,
       "switchIBQDR3V3": switchIBQDR3V3,
       "switchIBQDR1V25": switchIBQDR1V25,
       "switchIBFDRTable": switchIBFDRTable,
       "switchIBFDREntry": switchIBFDREntry,
       "switchIBFDRIndex": switchIBFDRIndex,
       "switchIBFDRSlotID": switchIBFDRSlotID,
       "switchIBFDRPresence": switchIBFDRPresence,
       "switchIBFDRName": switchIBFDRName,
       "switchIBFDRModel": switchIBFDRModel,
       "switchIBFDRPowerStatus": switchIBFDRPowerStatus,
       "switchIBFDRTemp1": switchIBFDRTemp1,
       "switchIBFDRTemp2": switchIBFDRTemp2,
       "switchIBFDRInitialized": switchIBFDRInitialized,
       "switchIBFDRError": switchIBFDRError,
       "switchIBFDR3V3": switchIBFDR3V3,
       "switchIBFDR1V2": switchIBFDR1V2,
       "switchIBFDR0V9": switchIBFDR0V9,
       "powerSupplies": powerSupplies,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuIndex": psuIndex,
       "psuSlotID": psuSlotID,
       "psuPresence": psuPresence,
       "psuName": psuName,
       "psuModel": psuModel,
       "psuPowerStatus": psuPowerStatus,
       "psuTemperature": psuTemperature,
       "psuFAN1Speed": psuFAN1Speed,
       "psuFAN2Speed": psuFAN2Speed,
       "psuFAN3Speed": psuFAN3Speed,
       "psuFAN4Speed": psuFAN4Speed,
       "psuACInVoltage": psuACInVoltage,
       "psuMaxWatt": psuMaxWatt,
       "psuACInCurrent": psuACInCurrent,
       "psuDCOutCurrent": psuDCOutCurrent,
       "psuCurrentPwrUsage": psuCurrentPwrUsage,
       "psuFWVersion": psuFWVersion,
       "psuFRUVersion": psuFRUVersion,
       "pwrGrpConsumption": pwrGrpConsumption,
       "pwrTotalPower": pwrTotalPower,
       "pwrBladeReserved": pwrBladeReserved,
       "pwrPeripheralReserved": pwrPeripheralReserved,
       "pwrAvailablePower": pwrAvailablePower,
       "pwrCurrentMaxTemp": pwrCurrentMaxTemp,
       "pwrCurrentMaxTempModule": pwrCurrentMaxTempModule,
       "pwrGrpPSURedundancy": pwrGrpPSURedundancy,
       "pwrRedundancy": pwrRedundancy,
       "pwrGrpPSUFanCtrl": pwrGrpPSUFanCtrl,
       "pwrPSUFanCtrl": pwrPSUFanCtrl,
       "pwrPSUFanSpdCtrl": pwrPSUFanSpdCtrl,
       "cmms": cmms,
       "cmmTable": cmmTable,
       "cmmEntry": cmmEntry,
       "cmmIndex": cmmIndex,
       "cmmSlot": cmmSlot,
       "cmmPresence": cmmPresence,
       "cmmName": cmmName,
       "cmmRole": cmmRole,
       "cmmIPAddr": cmmIPAddr,
       "cmmStatus": cmmStatus,
       "cmmFWVersion": cmmFWVersion,
       "cmmFWTag": cmmFWTag,
       "cmmOperationMode": cmmOperationMode,
       "cmmDateTime": cmmDateTime,
       "cmmNTPStatus": cmmNTPStatus,
       "cmmNTPServer1": cmmNTPServer1,
       "cmmNTPServer2": cmmNTPServer2,
       "cmmUTCOffset": cmmUTCOffset,
       "fru": fru,
       "fruTable": fruTable,
       "fruEntry": fruEntry,
       "fruTableIndex": fruTableIndex,
       "fruDeviceType": fruDeviceType,
       "fruDeviceSlot": fruDeviceSlot,
       "fruDevID": fruDevID,
       "fruChassisType": fruChassisType,
       "fruChassisTypeCode": fruChassisTypeCode,
       "fruChassisPN": fruChassisPN,
       "fruChassisSN": fruChassisSN,
       "fruBoardLang": fruBoardLang,
       "fruBoardLangCode": fruBoardLangCode,
       "fruBoardMfgDatetime": fruBoardMfgDatetime,
       "fruBoardMfgName": fruBoardMfgName,
       "fruBoardProdName": fruBoardProdName,
       "fruBoardSN": fruBoardSN,
       "fruBoardPN": fruBoardPN,
       "fruProdLang": fruProdLang,
       "fruProdLangCode": fruProdLangCode,
       "fruProdMfgName": fruProdMfgName,
       "fruProdProdName": fruProdProdName,
       "fruProdPN": fruProdPN,
       "fruProdVersion": fruProdVersion,
       "fruProdSN": fruProdSN,
       "fruProdAssetTag": fruProdAssetTag,
       "virtualMedias": virtualMedias,
       "floppyActiveImage1": floppyActiveImage1,
       "floppyActiveImage2": floppyActiveImage2,
       "cdromActiveImage1": cdromActiveImage1,
       "cdromActiveImage2": cdromActiveImage2,
       "drvRedirActiveImage1": drvRedirActiveImage1,
       "drvRedirActiveImage2": drvRedirActiveImage2,
       "drvRedirStatus": drvRedirStatus,
       "drvRedirAccessType": drvRedirAccessType,
       "usbEnableWithoutImage": usbEnableWithoutImage,
       "kvmSettings": kvmSettings,
       "keyboardModel": keyboardModel,
       "keyReleaseTimeoutStatus": keyReleaseTimeoutStatus,
       "keyReleaseTimeoutInterval": keyReleaseTimeoutInterval,
       "mouseType": mouseType,
       "mouseSpeed": mouseSpeed,
       "eventLogging": eventLogging,
       "evtGrpLogTargetSettings": evtGrpLogTargetSettings,
       "evtListLogStatus": evtListLogStatus,
       "evtListEntryPerPage": evtListEntryPerPage,
       "evtListClearLog": evtListClearLog,
       "evtNFSLogStatus": evtNFSLogStatus,
       "evtNFSServer": evtNFSServer,
       "evtNFSShare": evtNFSShare,
       "evtNFSLogFile": evtNFSLogFile,
       "evtSMTPLogStatus": evtSMTPLogStatus,
       "evtSMTPServer": evtSMTPServer,
       "evtSMTPRecvEmail": evtSMTPRecvEmail,
       "evtSMTPSendEmail": evtSMTPSendEmail,
       "evtSNMPLogStatus": evtSNMPLogStatus,
       "evtSNMPDestIP": evtSNMPDestIP,
       "evtSNMPCommunity": evtSNMPCommunity}
)
