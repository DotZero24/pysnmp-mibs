# SNMP MIB module (HUAWEI-SECURITY-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-IPSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:25:26 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

hwIpsec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26)
)
if mibBuilder.loadTexts:
    hwIpsec.setRevisions(
        ("2022-06-13 15:40",
         "2021-10-07 14:49",
         "2021-10-07 14:49",
         "2021-06-18 12:10",
         "2021-05-12 10:00",
         "2021-03-23 10:00",
         "2020-08-28 15:00",
         "2020-07-16 15:00",
         "2020-04-15 15:00",
         "2020-04-14 15:00",
         "2018-08-08 15:00",
         "2018-07-24 15:00",
         "2018-05-21 15:00",
         "2018-03-21 15:00",
         "2018-01-17 15:00",
         "2017-11-21 15:00",
         "2017-09-29 15:00",
         "2017-05-10 15:00",
         "2016-12-06 15:00",
         "2016-10-25 15:00",
         "2016-06-23 15:00",
         "2015-07-13 15:00",
         "2015-05-28 15:00",
         "2015-05-05 19:00",
         "2015-04-28 19:00",
         "2009-10-10 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwIPSecGlobalStats_ObjectIdentity = ObjectIdentity
hwIPSecGlobalStats = _HwIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1)
)
_HwIPSecGlobalTotal_Type = Gauge32
_HwIPSecGlobalTotal_Object = MibScalar
hwIPSecGlobalTotal = _HwIPSecGlobalTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 1),
    _HwIPSecGlobalTotal_Type()
)
hwIPSecGlobalTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalTotal.setStatus("current")
_HwIPSecGlobalPacketInput_Type = Counter64
_HwIPSecGlobalPacketInput_Object = MibScalar
hwIPSecGlobalPacketInput = _HwIPSecGlobalPacketInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 2),
    _HwIPSecGlobalPacketInput_Type()
)
hwIPSecGlobalPacketInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalPacketInput.setStatus("current")
_HwIPSecGlobalPacketOutput_Type = Counter64
_HwIPSecGlobalPacketOutput_Object = MibScalar
hwIPSecGlobalPacketOutput = _HwIPSecGlobalPacketOutput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 3),
    _HwIPSecGlobalPacketOutput_Type()
)
hwIPSecGlobalPacketOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalPacketOutput.setStatus("current")
_HwIPSecGlobalByteInput_Type = Counter64
_HwIPSecGlobalByteInput_Object = MibScalar
hwIPSecGlobalByteInput = _HwIPSecGlobalByteInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 4),
    _HwIPSecGlobalByteInput_Type()
)
hwIPSecGlobalByteInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalByteInput.setStatus("current")
_HwIPSecGlobalByteOutput_Type = Counter64
_HwIPSecGlobalByteOutput_Object = MibScalar
hwIPSecGlobalByteOutput = _HwIPSecGlobalByteOutput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 5),
    _HwIPSecGlobalByteOutput_Type()
)
hwIPSecGlobalByteOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalByteOutput.setStatus("current")
_HwIPSecGlobalDroppedPacketInput_Type = Counter64
_HwIPSecGlobalDroppedPacketInput_Object = MibScalar
hwIPSecGlobalDroppedPacketInput = _HwIPSecGlobalDroppedPacketInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 6),
    _HwIPSecGlobalDroppedPacketInput_Type()
)
hwIPSecGlobalDroppedPacketInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalDroppedPacketInput.setStatus("current")
_HwIPSecGlobalDroppedPacketOutput_Type = Counter64
_HwIPSecGlobalDroppedPacketOutput_Object = MibScalar
hwIPSecGlobalDroppedPacketOutput = _HwIPSecGlobalDroppedPacketOutput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 7),
    _HwIPSecGlobalDroppedPacketOutput_Type()
)
hwIPSecGlobalDroppedPacketOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalDroppedPacketOutput.setStatus("current")
_HwIPSecGlobalEncIntactPacket_Type = Counter64
_HwIPSecGlobalEncIntactPacket_Object = MibScalar
hwIPSecGlobalEncIntactPacket = _HwIPSecGlobalEncIntactPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 8),
    _HwIPSecGlobalEncIntactPacket_Type()
)
hwIPSecGlobalEncIntactPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalEncIntactPacket.setStatus("current")
_HwIPSecGlobalEncPacketFirstSlice_Type = Counter64
_HwIPSecGlobalEncPacketFirstSlice_Object = MibScalar
hwIPSecGlobalEncPacketFirstSlice = _HwIPSecGlobalEncPacketFirstSlice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 9),
    _HwIPSecGlobalEncPacketFirstSlice_Type()
)
hwIPSecGlobalEncPacketFirstSlice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalEncPacketFirstSlice.setStatus("current")
_HwIPSecGlobalEncPacketAfterSlice_Type = Counter64
_HwIPSecGlobalEncPacketAfterSlice_Object = MibScalar
hwIPSecGlobalEncPacketAfterSlice = _HwIPSecGlobalEncPacketAfterSlice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 10),
    _HwIPSecGlobalEncPacketAfterSlice_Type()
)
hwIPSecGlobalEncPacketAfterSlice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalEncPacketAfterSlice.setStatus("current")
_HwIPSecGlobalDecPacketReassFirstSlice_Type = Counter64
_HwIPSecGlobalDecPacketReassFirstSlice_Object = MibScalar
hwIPSecGlobalDecPacketReassFirstSlice = _HwIPSecGlobalDecPacketReassFirstSlice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 11),
    _HwIPSecGlobalDecPacketReassFirstSlice_Type()
)
hwIPSecGlobalDecPacketReassFirstSlice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalDecPacketReassFirstSlice.setStatus("current")
_HwIPSecGlobalDecPacketReassAfterSlice_Type = Counter64
_HwIPSecGlobalDecPacketReassAfterSlice_Object = MibScalar
hwIPSecGlobalDecPacketReassAfterSlice = _HwIPSecGlobalDecPacketReassAfterSlice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 12),
    _HwIPSecGlobalDecPacketReassAfterSlice_Type()
)
hwIPSecGlobalDecPacketReassAfterSlice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalDecPacketReassAfterSlice.setStatus("current")
_HwIPSecGlobalDecPacketReassLenErr_Type = Counter64
_HwIPSecGlobalDecPacketReassLenErr_Object = MibScalar
hwIPSecGlobalDecPacketReassLenErr = _HwIPSecGlobalDecPacketReassLenErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 13),
    _HwIPSecGlobalDecPacketReassLenErr_Type()
)
hwIPSecGlobalDecPacketReassLenErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalDecPacketReassLenErr.setStatus("current")
_HwIPSecGlobalPacketHeaderWrong_Type = Counter64
_HwIPSecGlobalPacketHeaderWrong_Object = MibScalar
hwIPSecGlobalPacketHeaderWrong = _HwIPSecGlobalPacketHeaderWrong_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 14),
    _HwIPSecGlobalPacketHeaderWrong_Type()
)
hwIPSecGlobalPacketHeaderWrong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalPacketHeaderWrong.setStatus("current")
_HwIPSecGlobalMemoryApplyFail_Type = Counter64
_HwIPSecGlobalMemoryApplyFail_Object = MibScalar
hwIPSecGlobalMemoryApplyFail = _HwIPSecGlobalMemoryApplyFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 15),
    _HwIPSecGlobalMemoryApplyFail_Type()
)
hwIPSecGlobalMemoryApplyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalMemoryApplyFail.setStatus("current")
_HwIPSecGlobalCannotFindSA_Type = Counter64
_HwIPSecGlobalCannotFindSA_Object = MibScalar
hwIPSecGlobalCannotFindSA = _HwIPSecGlobalCannotFindSA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 16),
    _HwIPSecGlobalCannotFindSA_Type()
)
hwIPSecGlobalCannotFindSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalCannotFindSA.setStatus("current")
_HwIPSecGlobalWrongSA_Type = Counter64
_HwIPSecGlobalWrongSA_Object = MibScalar
hwIPSecGlobalWrongSA = _HwIPSecGlobalWrongSA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 17),
    _HwIPSecGlobalWrongSA_Type()
)
hwIPSecGlobalWrongSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalWrongSA.setStatus("current")
_HwIPSecGlobalBadAuthentication_Type = Counter64
_HwIPSecGlobalBadAuthentication_Object = MibScalar
hwIPSecGlobalBadAuthentication = _HwIPSecGlobalBadAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 18),
    _HwIPSecGlobalBadAuthentication_Type()
)
hwIPSecGlobalBadAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalBadAuthentication.setStatus("current")
_HwIPSecGlobalReplay_Type = Counter64
_HwIPSecGlobalReplay_Object = MibScalar
hwIPSecGlobalReplay = _HwIPSecGlobalReplay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 19),
    _HwIPSecGlobalReplay_Type()
)
hwIPSecGlobalReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalReplay.setStatus("current")
_HwIPSecGlobalPreRecheckErr_Type = Counter64
_HwIPSecGlobalPreRecheckErr_Object = MibScalar
hwIPSecGlobalPreRecheckErr = _HwIPSecGlobalPreRecheckErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 20),
    _HwIPSecGlobalPreRecheckErr_Type()
)
hwIPSecGlobalPreRecheckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalPreRecheckErr.setStatus("current")
_HwIPSecGlobalPostRecheckErr_Type = Counter64
_HwIPSecGlobalPostRecheckErr_Object = MibScalar
hwIPSecGlobalPostRecheckErr = _HwIPSecGlobalPostRecheckErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 21),
    _HwIPSecGlobalPostRecheckErr_Type()
)
hwIPSecGlobalPostRecheckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalPostRecheckErr.setStatus("current")
_HwIPSecGlobalExceedByteLimit_Type = Counter64
_HwIPSecGlobalExceedByteLimit_Object = MibScalar
hwIPSecGlobalExceedByteLimit = _HwIPSecGlobalExceedByteLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 22),
    _HwIPSecGlobalExceedByteLimit_Type()
)
hwIPSecGlobalExceedByteLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalExceedByteLimit.setStatus("current")
_HwIPSecGlobalExceedPacketLimit_Type = Counter64
_HwIPSecGlobalExceedPacketLimit_Object = MibScalar
hwIPSecGlobalExceedPacketLimit = _HwIPSecGlobalExceedPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 23),
    _HwIPSecGlobalExceedPacketLimit_Type()
)
hwIPSecGlobalExceedPacketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalExceedPacketLimit.setStatus("current")
_HwIPSecGlobalProcessIpv4Err_Type = Counter64
_HwIPSecGlobalProcessIpv4Err_Object = MibScalar
hwIPSecGlobalProcessIpv4Err = _HwIPSecGlobalProcessIpv4Err_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 24),
    _HwIPSecGlobalProcessIpv4Err_Type()
)
hwIPSecGlobalProcessIpv4Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalProcessIpv4Err.setStatus("current")
_HwIPSecGlobalFibSearchErr_Type = Counter64
_HwIPSecGlobalFibSearchErr_Object = MibScalar
hwIPSecGlobalFibSearchErr = _HwIPSecGlobalFibSearchErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 25),
    _HwIPSecGlobalFibSearchErr_Type()
)
hwIPSecGlobalFibSearchErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalFibSearchErr.setStatus("current")
_HwIPSecGlobalIKEInboundOK_Type = Counter64
_HwIPSecGlobalIKEInboundOK_Object = MibScalar
hwIPSecGlobalIKEInboundOK = _HwIPSecGlobalIKEInboundOK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 26),
    _HwIPSecGlobalIKEInboundOK_Type()
)
hwIPSecGlobalIKEInboundOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalIKEInboundOK.setStatus("current")
_HwIPSecGlobalIKEInboundErr_Type = Counter64
_HwIPSecGlobalIKEInboundErr_Object = MibScalar
hwIPSecGlobalIKEInboundErr = _HwIPSecGlobalIKEInboundErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 27),
    _HwIPSecGlobalIKEInboundErr_Type()
)
hwIPSecGlobalIKEInboundErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalIKEInboundErr.setStatus("current")
_HwIPSecGlobalIKEOutboundOK_Type = Counter64
_HwIPSecGlobalIKEOutboundOK_Object = MibScalar
hwIPSecGlobalIKEOutboundOK = _HwIPSecGlobalIKEOutboundOK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 28),
    _HwIPSecGlobalIKEOutboundOK_Type()
)
hwIPSecGlobalIKEOutboundOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalIKEOutboundOK.setStatus("current")
_HwIPSecGlobalIKEOutboundErr_Type = Counter64
_HwIPSecGlobalIKEOutboundErr_Object = MibScalar
hwIPSecGlobalIKEOutboundErr = _HwIPSecGlobalIKEOutboundErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 29),
    _HwIPSecGlobalIKEOutboundErr_Type()
)
hwIPSecGlobalIKEOutboundErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalIKEOutboundErr.setStatus("current")
_HwIPSecGlobalSoftExpr_Type = Counter64
_HwIPSecGlobalSoftExpr_Object = MibScalar
hwIPSecGlobalSoftExpr = _HwIPSecGlobalSoftExpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 30),
    _HwIPSecGlobalSoftExpr_Type()
)
hwIPSecGlobalSoftExpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalSoftExpr.setStatus("current")
_HwIPSecGlobalHardExpr_Type = Counter64
_HwIPSecGlobalHardExpr_Object = MibScalar
hwIPSecGlobalHardExpr = _HwIPSecGlobalHardExpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 31),
    _HwIPSecGlobalHardExpr_Type()
)
hwIPSecGlobalHardExpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalHardExpr.setStatus("current")
_HwIPSecGlobalDPDOper_Type = Counter64
_HwIPSecGlobalDPDOper_Object = MibScalar
hwIPSecGlobalDPDOper = _HwIPSecGlobalDPDOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 32),
    _HwIPSecGlobalDPDOper_Type()
)
hwIPSecGlobalDPDOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalDPDOper.setStatus("current")
_HwIPSecGlobalModpCnt_Type = Counter64
_HwIPSecGlobalModpCnt_Object = MibScalar
hwIPSecGlobalModpCnt = _HwIPSecGlobalModpCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 33),
    _HwIPSecGlobalModpCnt_Type()
)
hwIPSecGlobalModpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalModpCnt.setStatus("current")
_HwIPSecGlobalSaeSucc_Type = Counter64
_HwIPSecGlobalSaeSucc_Object = MibScalar
hwIPSecGlobalSaeSucc = _HwIPSecGlobalSaeSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 34),
    _HwIPSecGlobalSaeSucc_Type()
)
hwIPSecGlobalSaeSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalSaeSucc.setStatus("current")
_HwIPSecGlobalSoftwareSucc_Type = Counter64
_HwIPSecGlobalSoftwareSucc_Object = MibScalar
hwIPSecGlobalSoftwareSucc = _HwIPSecGlobalSoftwareSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 35),
    _HwIPSecGlobalSoftwareSucc_Type()
)
hwIPSecGlobalSoftwareSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalSoftwareSucc.setStatus("current")
_HwIPSecGlobalConnectionRate_Type = Gauge32
_HwIPSecGlobalConnectionRate_Object = MibScalar
hwIPSecGlobalConnectionRate = _HwIPSecGlobalConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 36),
    _HwIPSecGlobalConnectionRate_Type()
)
hwIPSecGlobalConnectionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalConnectionRate.setStatus("current")
_HwIPSecGlobalTotalPhase1Num_Type = Gauge32
_HwIPSecGlobalTotalPhase1Num_Object = MibScalar
hwIPSecGlobalTotalPhase1Num = _HwIPSecGlobalTotalPhase1Num_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 37),
    _HwIPSecGlobalTotalPhase1Num_Type()
)
hwIPSecGlobalTotalPhase1Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalTotalPhase1Num.setStatus("current")
_HwIPSecGlobalBytesPerSecondIn_Type = Counter64
_HwIPSecGlobalBytesPerSecondIn_Object = MibScalar
hwIPSecGlobalBytesPerSecondIn = _HwIPSecGlobalBytesPerSecondIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 38),
    _HwIPSecGlobalBytesPerSecondIn_Type()
)
hwIPSecGlobalBytesPerSecondIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalBytesPerSecondIn.setStatus("current")
_HwIPSecGlobalBytesPerSecondOut_Type = Counter64
_HwIPSecGlobalBytesPerSecondOut_Object = MibScalar
hwIPSecGlobalBytesPerSecondOut = _HwIPSecGlobalBytesPerSecondOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 1, 39),
    _HwIPSecGlobalBytesPerSecondOut_Type()
)
hwIPSecGlobalBytesPerSecondOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecGlobalBytesPerSecondOut.setStatus("current")
_HwIPSecTunnelConfigTable_Object = MibTable
hwIPSecTunnelConfigTable = _HwIPSecTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2)
)
if mibBuilder.loadTexts:
    hwIPSecTunnelConfigTable.setStatus("current")
_HwIPSecTunnelConfigEntry_Object = MibTableRow
hwIPSecTunnelConfigEntry = _HwIPSecTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1)
)
hwIPSecTunnelConfigEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIfIndex"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyNum"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelIndex"),
)
if mibBuilder.loadTexts:
    hwIPSecTunnelConfigEntry.setStatus("current")
_HwIPSecIfIndex_Type = Gauge32
_HwIPSecIfIndex_Object = MibTableColumn
hwIPSecIfIndex = _HwIPSecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 1),
    _HwIPSecIfIndex_Type()
)
hwIPSecIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecIfIndex.setStatus("current")
_HwIPSecTunnelPolicyNum_Type = Gauge32
_HwIPSecTunnelPolicyNum_Object = MibTableColumn
hwIPSecTunnelPolicyNum = _HwIPSecTunnelPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 2),
    _HwIPSecTunnelPolicyNum_Type()
)
hwIPSecTunnelPolicyNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTunnelPolicyNum.setStatus("current")
_HwIPSecTunnelIndex_Type = Gauge32
_HwIPSecTunnelIndex_Object = MibTableColumn
hwIPSecTunnelIndex = _HwIPSecTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 3),
    _HwIPSecTunnelIndex_Type()
)
hwIPSecTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTunnelIndex.setStatus("current")
_HwIPSecTunnelRuleId_Type = Gauge32
_HwIPSecTunnelRuleId_Object = MibTableColumn
hwIPSecTunnelRuleId = _HwIPSecTunnelRuleId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 4),
    _HwIPSecTunnelRuleId_Type()
)
hwIPSecTunnelRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRuleId.setStatus("current")


class _HwIPSecTunnelDstIP_Type(OctetString):
    """Custom type hwIPSecTunnelDstIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelDstIP_Type.__name__ = "OctetString"
_HwIPSecTunnelDstIP_Object = MibTableColumn
hwIPSecTunnelDstIP = _HwIPSecTunnelDstIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 5),
    _HwIPSecTunnelDstIP_Type()
)
hwIPSecTunnelDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelDstIP.setStatus("current")


class _HwIPSecTunnelInsideIP_Type(OctetString):
    """Custom type hwIPSecTunnelInsideIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelInsideIP_Type.__name__ = "OctetString"
_HwIPSecTunnelInsideIP_Object = MibTableColumn
hwIPSecTunnelInsideIP = _HwIPSecTunnelInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 6),
    _HwIPSecTunnelInsideIP_Type()
)
hwIPSecTunnelInsideIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelInsideIP.setStatus("current")
_HwIPSecTunnelRemotePort_Type = Gauge32
_HwIPSecTunnelRemotePort_Object = MibTableColumn
hwIPSecTunnelRemotePort = _HwIPSecTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 7),
    _HwIPSecTunnelRemotePort_Type()
)
hwIPSecTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRemotePort.setStatus("current")
_HwIPSecTunnelCpuID_Type = Gauge32
_HwIPSecTunnelCpuID_Object = MibTableColumn
hwIPSecTunnelCpuID = _HwIPSecTunnelCpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 8),
    _HwIPSecTunnelCpuID_Type()
)
hwIPSecTunnelCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelCpuID.setStatus("current")


class _HwIPSecTunnelEncapMode_Type(Integer32):
    """Custom type hwIPSecTunnelEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 0),
          ("transport", 1))
    )


_HwIPSecTunnelEncapMode_Type.__name__ = "Integer32"
_HwIPSecTunnelEncapMode_Object = MibTableColumn
hwIPSecTunnelEncapMode = _HwIPSecTunnelEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 9),
    _HwIPSecTunnelEncapMode_Type()
)
hwIPSecTunnelEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelEncapMode.setStatus("current")


class _HwIPSecTunnelNatTraver_Type(Integer32):
    """Custom type hwIPSecTunnelNatTraver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noNatTraversal", 0),
          ("natTraversal", 1))
    )


_HwIPSecTunnelNatTraver_Type.__name__ = "Integer32"
_HwIPSecTunnelNatTraver_Object = MibTableColumn
hwIPSecTunnelNatTraver = _HwIPSecTunnelNatTraver_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 10),
    _HwIPSecTunnelNatTraver_Type()
)
hwIPSecTunnelNatTraver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelNatTraver.setStatus("current")


class _HwIPSecTunnelFromIKEV2_Type(Integer32):
    """Custom type hwIPSecTunnelFromIKEV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noIkev2", 0),
          ("ikev2", 1))
    )


_HwIPSecTunnelFromIKEV2_Type.__name__ = "Integer32"
_HwIPSecTunnelFromIKEV2_Object = MibTableColumn
hwIPSecTunnelFromIKEV2 = _HwIPSecTunnelFromIKEV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 11),
    _HwIPSecTunnelFromIKEV2_Type()
)
hwIPSecTunnelFromIKEV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFromIKEV2.setStatus("current")
_HwIPSecTunnelEncryptMode_Type = Gauge32
_HwIPSecTunnelEncryptMode_Object = MibTableColumn
hwIPSecTunnelEncryptMode = _HwIPSecTunnelEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 12),
    _HwIPSecTunnelEncryptMode_Type()
)
hwIPSecTunnelEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelEncryptMode.setStatus("current")
_HwIPSecTunnelESPDigestMode_Type = Gauge32
_HwIPSecTunnelESPDigestMode_Object = MibTableColumn
hwIPSecTunnelESPDigestMode = _HwIPSecTunnelESPDigestMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 13),
    _HwIPSecTunnelESPDigestMode_Type()
)
hwIPSecTunnelESPDigestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelESPDigestMode.setStatus("current")
_HwIPSecTunnelAHDigestMode_Type = Gauge32
_HwIPSecTunnelAHDigestMode_Object = MibTableColumn
hwIPSecTunnelAHDigestMode = _HwIPSecTunnelAHDigestMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 14),
    _HwIPSecTunnelAHDigestMode_Type()
)
hwIPSecTunnelAHDigestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelAHDigestMode.setStatus("current")
_HwIPSecTunnelProto_Type = Gauge32
_HwIPSecTunnelProto_Object = MibTableColumn
hwIPSecTunnelProto = _HwIPSecTunnelProto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 15),
    _HwIPSecTunnelProto_Type()
)
hwIPSecTunnelProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelProto.setStatus("current")
_HwIPSecTunnelOutPortIndex_Type = Gauge32
_HwIPSecTunnelOutPortIndex_Object = MibTableColumn
hwIPSecTunnelOutPortIndex = _HwIPSecTunnelOutPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 16),
    _HwIPSecTunnelOutPortIndex_Type()
)
hwIPSecTunnelOutPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelOutPortIndex.setStatus("current")
_HwIPSecTunnelSrcPort_Type = Gauge32
_HwIPSecTunnelSrcPort_Object = MibTableColumn
hwIPSecTunnelSrcPort = _HwIPSecTunnelSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 17),
    _HwIPSecTunnelSrcPort_Type()
)
hwIPSecTunnelSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSrcPort.setStatus("current")
_HwIPSecTunnelDstPort_Type = Gauge32
_HwIPSecTunnelDstPort_Object = MibTableColumn
hwIPSecTunnelDstPort = _HwIPSecTunnelDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 18),
    _HwIPSecTunnelDstPort_Type()
)
hwIPSecTunnelDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelDstPort.setStatus("current")
_HwIPSecTunnelVrfIndex_Type = Gauge32
_HwIPSecTunnelVrfIndex_Object = MibTableColumn
hwIPSecTunnelVrfIndex = _HwIPSecTunnelVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 19),
    _HwIPSecTunnelVrfIndex_Type()
)
hwIPSecTunnelVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelVrfIndex.setStatus("current")
_HwIPSecTunnelIfVrfIndex_Type = Gauge32
_HwIPSecTunnelIfVrfIndex_Object = MibTableColumn
hwIPSecTunnelIfVrfIndex = _HwIPSecTunnelIfVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 20),
    _HwIPSecTunnelIfVrfIndex_Type()
)
hwIPSecTunnelIfVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelIfVrfIndex.setStatus("current")


class _HwIPSecTunnelSrcIP_Type(OctetString):
    """Custom type hwIPSecTunnelSrcIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelSrcIP_Type.__name__ = "OctetString"
_HwIPSecTunnelSrcIP_Object = MibTableColumn
hwIPSecTunnelSrcIP = _HwIPSecTunnelSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 21),
    _HwIPSecTunnelSrcIP_Type()
)
hwIPSecTunnelSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSrcIP.setStatus("current")
_HwIPSecTunnelSpeedLimitIn_Type = Gauge32
_HwIPSecTunnelSpeedLimitIn_Object = MibTableColumn
hwIPSecTunnelSpeedLimitIn = _HwIPSecTunnelSpeedLimitIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 22),
    _HwIPSecTunnelSpeedLimitIn_Type()
)
hwIPSecTunnelSpeedLimitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSpeedLimitIn.setStatus("current")
_HwIPSecTunnelSpeedLimitOut_Type = Gauge32
_HwIPSecTunnelSpeedLimitOut_Object = MibTableColumn
hwIPSecTunnelSpeedLimitOut = _HwIPSecTunnelSpeedLimitOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 23),
    _HwIPSecTunnelSpeedLimitOut_Type()
)
hwIPSecTunnelSpeedLimitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSpeedLimitOut.setStatus("current")


class _HwIPSecTunnelInitiator_Type(Integer32):
    """Custom type hwIPSecTunnelInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("responder", 0),
          ("ikev2Initiator", 1),
          ("ikev1Initiator", 2))
    )


_HwIPSecTunnelInitiator_Type.__name__ = "Integer32"
_HwIPSecTunnelInitiator_Object = MibTableColumn
hwIPSecTunnelInitiator = _HwIPSecTunnelInitiator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 24),
    _HwIPSecTunnelInitiator_Type()
)
hwIPSecTunnelInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelInitiator.setStatus("current")


class _HwIPSecTunnelLifeSize_Type(Gauge32):
    """Custom type hwIPSecTunnelLifeSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_HwIPSecTunnelLifeSize_Type.__name__ = "Gauge32"
_HwIPSecTunnelLifeSize_Object = MibTableColumn
hwIPSecTunnelLifeSize = _HwIPSecTunnelLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 25),
    _HwIPSecTunnelLifeSize_Type()
)
hwIPSecTunnelLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelLifeSize.setStatus("current")


class _HwIPSecTunnelLifeTime_Type(Gauge32):
    """Custom type hwIPSecTunnelLifeTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_HwIPSecTunnelLifeTime_Type.__name__ = "Gauge32"
_HwIPSecTunnelLifeTime_Object = MibTableColumn
hwIPSecTunnelLifeTime = _HwIPSecTunnelLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 26),
    _HwIPSecTunnelLifeTime_Type()
)
hwIPSecTunnelLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelLifeTime.setStatus("current")


class _HwIPSecTunnelPolicyName_Type(OctetString):
    """Custom type hwIPSecTunnelPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIPSecTunnelPolicyName_Type.__name__ = "OctetString"
_HwIPSecTunnelPolicyName_Object = MibTableColumn
hwIPSecTunnelPolicyName = _HwIPSecTunnelPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 27),
    _HwIPSecTunnelPolicyName_Type()
)
hwIPSecTunnelPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPolicyName.setStatus("current")


class _HwIPSecTunnelSaStatus_Type(Integer32):
    """Custom type hwIPSecTunnelSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("free", 0),
          ("ocuppied", 1))
    )


_HwIPSecTunnelSaStatus_Type.__name__ = "Integer32"
_HwIPSecTunnelSaStatus_Object = MibTableColumn
hwIPSecTunnelSaStatus = _HwIPSecTunnelSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 28),
    _HwIPSecTunnelSaStatus_Type()
)
hwIPSecTunnelSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSaStatus.setStatus("current")
_HwIPSecTunnelSlotID_Type = Gauge32
_HwIPSecTunnelSlotID_Object = MibTableColumn
hwIPSecTunnelSlotID = _HwIPSecTunnelSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 29),
    _HwIPSecTunnelSlotID_Type()
)
hwIPSecTunnelSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSlotID.setStatus("current")


class _HwIPSecTunnelFlowInfo_Type(OctetString):
    """Custom type hwIPSecTunnelFlowInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIPSecTunnelFlowInfo_Type.__name__ = "OctetString"
_HwIPSecTunnelFlowInfo_Object = MibTableColumn
hwIPSecTunnelFlowInfo = _HwIPSecTunnelFlowInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 30),
    _HwIPSecTunnelFlowInfo_Type()
)
hwIPSecTunnelFlowInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFlowInfo.setStatus("current")


class _HwIPSecTunnelPolicyAlias_Type(OctetString):
    """Custom type hwIPSecTunnelPolicyAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelPolicyAlias_Type.__name__ = "OctetString"
_HwIPSecTunnelPolicyAlias_Object = MibTableColumn
hwIPSecTunnelPolicyAlias = _HwIPSecTunnelPolicyAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 31),
    _HwIPSecTunnelPolicyAlias_Type()
)
hwIPSecTunnelPolicyAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPolicyAlias.setStatus("current")


class _HwIPSecTunnelDstIPv6_Type(OctetString):
    """Custom type hwIPSecTunnelDstIPv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelDstIPv6_Type.__name__ = "OctetString"
_HwIPSecTunnelDstIPv6_Object = MibTableColumn
hwIPSecTunnelDstIPv6 = _HwIPSecTunnelDstIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 32),
    _HwIPSecTunnelDstIPv6_Type()
)
hwIPSecTunnelDstIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelDstIPv6.setStatus("current")


class _HwIPSecTunnelInsideIPv6_Type(OctetString):
    """Custom type hwIPSecTunnelInsideIPv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelInsideIPv6_Type.__name__ = "OctetString"
_HwIPSecTunnelInsideIPv6_Object = MibTableColumn
hwIPSecTunnelInsideIPv6 = _HwIPSecTunnelInsideIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 33),
    _HwIPSecTunnelInsideIPv6_Type()
)
hwIPSecTunnelInsideIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelInsideIPv6.setStatus("current")


class _HwIPSecTunnelSrcIPv6_Type(OctetString):
    """Custom type hwIPSecTunnelSrcIPv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelSrcIPv6_Type.__name__ = "OctetString"
_HwIPSecTunnelSrcIPv6_Object = MibTableColumn
hwIPSecTunnelSrcIPv6 = _HwIPSecTunnelSrcIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 2, 1, 34),
    _HwIPSecTunnelSrcIPv6_Type()
)
hwIPSecTunnelSrcIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSrcIPv6.setStatus("current")
_HwIPSecTunnelStatsTable_Object = MibTable
hwIPSecTunnelStatsTable = _HwIPSecTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3)
)
if mibBuilder.loadTexts:
    hwIPSecTunnelStatsTable.setStatus("current")
_HwIPSecTunnelStatsEntry_Object = MibTableRow
hwIPSecTunnelStatsEntry = _HwIPSecTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1)
)
hwIPSecTunnelStatsEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIfIndex"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyNum"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelIndex"),
)
if mibBuilder.loadTexts:
    hwIPSecTunnelStatsEntry.setStatus("current")
_HwIPSecTunnelSaIDIn_Type = Gauge32
_HwIPSecTunnelSaIDIn_Object = MibTableColumn
hwIPSecTunnelSaIDIn = _HwIPSecTunnelSaIDIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 1),
    _HwIPSecTunnelSaIDIn_Type()
)
hwIPSecTunnelSaIDIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSaIDIn.setStatus("current")
_HwIPSecTunnelSaIDOut_Type = Gauge32
_HwIPSecTunnelSaIDOut_Object = MibTableColumn
hwIPSecTunnelSaIDOut = _HwIPSecTunnelSaIDOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 2),
    _HwIPSecTunnelSaIDOut_Type()
)
hwIPSecTunnelSaIDOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSaIDOut.setStatus("current")
_HwIPSecTunnelFlowSoftExpireIn_Type = Gauge32
_HwIPSecTunnelFlowSoftExpireIn_Object = MibTableColumn
hwIPSecTunnelFlowSoftExpireIn = _HwIPSecTunnelFlowSoftExpireIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 3),
    _HwIPSecTunnelFlowSoftExpireIn_Type()
)
hwIPSecTunnelFlowSoftExpireIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFlowSoftExpireIn.setStatus("current")
_HwIPSecTunnelFlowSoftExpireOut_Type = Gauge32
_HwIPSecTunnelFlowSoftExpireOut_Object = MibTableColumn
hwIPSecTunnelFlowSoftExpireOut = _HwIPSecTunnelFlowSoftExpireOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 4),
    _HwIPSecTunnelFlowSoftExpireOut_Type()
)
hwIPSecTunnelFlowSoftExpireOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFlowSoftExpireOut.setStatus("current")
_HwIPSecTunnelFlowHardExpireIn_Type = Gauge32
_HwIPSecTunnelFlowHardExpireIn_Object = MibTableColumn
hwIPSecTunnelFlowHardExpireIn = _HwIPSecTunnelFlowHardExpireIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 5),
    _HwIPSecTunnelFlowHardExpireIn_Type()
)
hwIPSecTunnelFlowHardExpireIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFlowHardExpireIn.setStatus("current")
_HwIPSecTunnelFlowHardExpireOut_Type = Gauge32
_HwIPSecTunnelFlowHardExpireOut_Object = MibTableColumn
hwIPSecTunnelFlowHardExpireOut = _HwIPSecTunnelFlowHardExpireOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 6),
    _HwIPSecTunnelFlowHardExpireOut_Type()
)
hwIPSecTunnelFlowHardExpireOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFlowHardExpireOut.setStatus("current")
_HwIPSecTunnelRemainTime_Type = Gauge32
_HwIPSecTunnelRemainTime_Object = MibTableColumn
hwIPSecTunnelRemainTime = _HwIPSecTunnelRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 7),
    _HwIPSecTunnelRemainTime_Type()
)
hwIPSecTunnelRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRemainTime.setStatus("current")
_HwIPSecTunnelRemainSize_Type = Gauge32
_HwIPSecTunnelRemainSize_Object = MibTableColumn
hwIPSecTunnelRemainSize = _HwIPSecTunnelRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 8),
    _HwIPSecTunnelRemainSize_Type()
)
hwIPSecTunnelRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRemainSize.setStatus("current")
_HwIPSecTunnelSpiIn_Type = Gauge32
_HwIPSecTunnelSpiIn_Object = MibTableColumn
hwIPSecTunnelSpiIn = _HwIPSecTunnelSpiIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 9),
    _HwIPSecTunnelSpiIn_Type()
)
hwIPSecTunnelSpiIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSpiIn.setStatus("current")
_HwIPSecTunnelSpiOut_Type = Gauge32
_HwIPSecTunnelSpiOut_Object = MibTableColumn
hwIPSecTunnelSpiOut = _HwIPSecTunnelSpiOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 10),
    _HwIPSecTunnelSpiOut_Type()
)
hwIPSecTunnelSpiOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSpiOut.setStatus("current")
_HwIPSecTunnelInSideSpiIn_Type = Gauge32
_HwIPSecTunnelInSideSpiIn_Object = MibTableColumn
hwIPSecTunnelInSideSpiIn = _HwIPSecTunnelInSideSpiIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 11),
    _HwIPSecTunnelInSideSpiIn_Type()
)
hwIPSecTunnelInSideSpiIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelInSideSpiIn.setStatus("current")
_HwIPSecTunnelInSideSpiOut_Type = Gauge32
_HwIPSecTunnelInSideSpiOut_Object = MibTableColumn
hwIPSecTunnelInSideSpiOut = _HwIPSecTunnelInSideSpiOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 12),
    _HwIPSecTunnelInSideSpiOut_Type()
)
hwIPSecTunnelInSideSpiOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelInSideSpiOut.setStatus("current")
_HwIPSecTunnelESPSequenceNumberIn_Type = Gauge32
_HwIPSecTunnelESPSequenceNumberIn_Object = MibTableColumn
hwIPSecTunnelESPSequenceNumberIn = _HwIPSecTunnelESPSequenceNumberIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 13),
    _HwIPSecTunnelESPSequenceNumberIn_Type()
)
hwIPSecTunnelESPSequenceNumberIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelESPSequenceNumberIn.setStatus("current")
_HwIPSecTunnelESPSequenceNumberOut_Type = Gauge32
_HwIPSecTunnelESPSequenceNumberOut_Object = MibTableColumn
hwIPSecTunnelESPSequenceNumberOut = _HwIPSecTunnelESPSequenceNumberOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 14),
    _HwIPSecTunnelESPSequenceNumberOut_Type()
)
hwIPSecTunnelESPSequenceNumberOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelESPSequenceNumberOut.setStatus("current")
_HwIPSecTunnellAHSequenceNumberIn_Type = Gauge32
_HwIPSecTunnellAHSequenceNumberIn_Object = MibTableColumn
hwIPSecTunnellAHSequenceNumberIn = _HwIPSecTunnellAHSequenceNumberIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 15),
    _HwIPSecTunnellAHSequenceNumberIn_Type()
)
hwIPSecTunnellAHSequenceNumberIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnellAHSequenceNumberIn.setStatus("current")
_HwIPSecTunnellAHSequenceNumberOut_Type = Gauge32
_HwIPSecTunnellAHSequenceNumberOut_Object = MibTableColumn
hwIPSecTunnellAHSequenceNumberOut = _HwIPSecTunnellAHSequenceNumberOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 16),
    _HwIPSecTunnellAHSequenceNumberOut_Type()
)
hwIPSecTunnellAHSequenceNumberOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnellAHSequenceNumberOut.setStatus("current")
_HwIPSecTunnelMemApplyFail_Type = Counter64
_HwIPSecTunnelMemApplyFail_Object = MibTableColumn
hwIPSecTunnelMemApplyFail = _HwIPSecTunnelMemApplyFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 17),
    _HwIPSecTunnelMemApplyFail_Type()
)
hwIPSecTunnelMemApplyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelMemApplyFail.setStatus("current")
_HwIPSecTunnelBadAuth_Type = Counter64
_HwIPSecTunnelBadAuth_Object = MibTableColumn
hwIPSecTunnelBadAuth = _HwIPSecTunnelBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 18),
    _HwIPSecTunnelBadAuth_Type()
)
hwIPSecTunnelBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelBadAuth.setStatus("current")
_HwIPSecTunnelReplay_Type = Counter64
_HwIPSecTunnelReplay_Object = MibTableColumn
hwIPSecTunnelReplay = _HwIPSecTunnelReplay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 19),
    _HwIPSecTunnelReplay_Type()
)
hwIPSecTunnelReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelReplay.setStatus("current")
_HwIPSecTunnelAfterReCheckErr_Type = Counter64
_HwIPSecTunnelAfterReCheckErr_Object = MibTableColumn
hwIPSecTunnelAfterReCheckErr = _HwIPSecTunnelAfterReCheckErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 20),
    _HwIPSecTunnelAfterReCheckErr_Type()
)
hwIPSecTunnelAfterReCheckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelAfterReCheckErr.setStatus("current")
_HwIPSecTunnelPktDropByteLimitIn_Type = Counter64
_HwIPSecTunnelPktDropByteLimitIn_Object = MibTableColumn
hwIPSecTunnelPktDropByteLimitIn = _HwIPSecTunnelPktDropByteLimitIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 21),
    _HwIPSecTunnelPktDropByteLimitIn_Type()
)
hwIPSecTunnelPktDropByteLimitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPktDropByteLimitIn.setStatus("current")
_HwIPSecTunnelPktDropByteLimitOut_Type = Counter64
_HwIPSecTunnelPktDropByteLimitOut_Object = MibTableColumn
hwIPSecTunnelPktDropByteLimitOut = _HwIPSecTunnelPktDropByteLimitOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 22),
    _HwIPSecTunnelPktDropByteLimitOut_Type()
)
hwIPSecTunnelPktDropByteLimitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPktDropByteLimitOut.setStatus("current")
_HwIPSecTunnelFIBSearchErr_Type = Counter64
_HwIPSecTunnelFIBSearchErr_Object = MibTableColumn
hwIPSecTunnelFIBSearchErr = _HwIPSecTunnelFIBSearchErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 23),
    _HwIPSecTunnelFIBSearchErr_Type()
)
hwIPSecTunnelFIBSearchErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelFIBSearchErr.setStatus("current")
_HwIPSecTunnelBytesPerSecondIn_Type = Gauge32
_HwIPSecTunnelBytesPerSecondIn_Object = MibTableColumn
hwIPSecTunnelBytesPerSecondIn = _HwIPSecTunnelBytesPerSecondIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 24),
    _HwIPSecTunnelBytesPerSecondIn_Type()
)
hwIPSecTunnelBytesPerSecondIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelBytesPerSecondIn.setStatus("current")
_HwIPSecTunnelBytesPerSecondOut_Type = Gauge32
_HwIPSecTunnelBytesPerSecondOut_Object = MibTableColumn
hwIPSecTunnelBytesPerSecondOut = _HwIPSecTunnelBytesPerSecondOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 25),
    _HwIPSecTunnelBytesPerSecondOut_Type()
)
hwIPSecTunnelBytesPerSecondOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelBytesPerSecondOut.setStatus("current")
_HwIPSecTunnelPacketsPerSecondIn_Type = Gauge32
_HwIPSecTunnelPacketsPerSecondIn_Object = MibTableColumn
hwIPSecTunnelPacketsPerSecondIn = _HwIPSecTunnelPacketsPerSecondIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 26),
    _HwIPSecTunnelPacketsPerSecondIn_Type()
)
hwIPSecTunnelPacketsPerSecondIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPacketsPerSecondIn.setStatus("current")
_HwIPSecTunnelPacketsPerSecondOut_Type = Gauge32
_HwIPSecTunnelPacketsPerSecondOut_Object = MibTableColumn
hwIPSecTunnelPacketsPerSecondOut = _HwIPSecTunnelPacketsPerSecondOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 27),
    _HwIPSecTunnelPacketsPerSecondOut_Type()
)
hwIPSecTunnelPacketsPerSecondOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPacketsPerSecondOut.setStatus("current")
_HwIPSecTunnelErrPacketsPerSecondIn_Type = Gauge32
_HwIPSecTunnelErrPacketsPerSecondIn_Object = MibTableColumn
hwIPSecTunnelErrPacketsPerSecondIn = _HwIPSecTunnelErrPacketsPerSecondIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 28),
    _HwIPSecTunnelErrPacketsPerSecondIn_Type()
)
hwIPSecTunnelErrPacketsPerSecondIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelErrPacketsPerSecondIn.setStatus("current")
_HwIPSecTunnelErrPacketsPerSecondOut_Type = Gauge32
_HwIPSecTunnelErrPacketsPerSecondOut_Object = MibTableColumn
hwIPSecTunnelErrPacketsPerSecondOut = _HwIPSecTunnelErrPacketsPerSecondOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 29),
    _HwIPSecTunnelErrPacketsPerSecondOut_Type()
)
hwIPSecTunnelErrPacketsPerSecondOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelErrPacketsPerSecondOut.setStatus("current")
_HwIPSecTunnelErrPacketsIn_Type = Gauge32
_HwIPSecTunnelErrPacketsIn_Object = MibTableColumn
hwIPSecTunnelErrPacketsIn = _HwIPSecTunnelErrPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 30),
    _HwIPSecTunnelErrPacketsIn_Type()
)
hwIPSecTunnelErrPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelErrPacketsIn.setStatus("current")
_HwIPSecTunnelErrPacketsOut_Type = Gauge32
_HwIPSecTunnelErrPacketsOut_Object = MibTableColumn
hwIPSecTunnelErrPacketsOut = _HwIPSecTunnelErrPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 3, 1, 31),
    _HwIPSecTunnelErrPacketsOut_Type()
)
hwIPSecTunnelErrPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelErrPacketsOut.setStatus("current")
_HwIPSecSaStatisticTable_Object = MibTable
hwIPSecSaStatisticTable = _HwIPSecSaStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4)
)
if mibBuilder.loadTexts:
    hwIPSecSaStatisticTable.setStatus("current")
_HwIPSecSaStatisticEntry_Object = MibTableRow
hwIPSecSaStatisticEntry = _HwIPSecSaStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1)
)
hwIPSecSaStatisticEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIfIndex"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyNum"),
)
if mibBuilder.loadTexts:
    hwIPSecSaStatisticEntry.setStatus("current")


class _HwIPSecSaStatisticTunnelPolicyName_Type(OctetString):
    """Custom type hwIPSecSaStatisticTunnelPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIPSecSaStatisticTunnelPolicyName_Type.__name__ = "OctetString"
_HwIPSecSaStatisticTunnelPolicyName_Object = MibTableColumn
hwIPSecSaStatisticTunnelPolicyName = _HwIPSecSaStatisticTunnelPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 1),
    _HwIPSecSaStatisticTunnelPolicyName_Type()
)
hwIPSecSaStatisticTunnelPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecSaStatisticTunnelPolicyName.setStatus("current")
_HwIPSecSaStatisticSaInCnt_Type = Gauge32
_HwIPSecSaStatisticSaInCnt_Object = MibTableColumn
hwIPSecSaStatisticSaInCnt = _HwIPSecSaStatisticSaInCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 2),
    _HwIPSecSaStatisticSaInCnt_Type()
)
hwIPSecSaStatisticSaInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecSaStatisticSaInCnt.setStatus("current")
_HwIPSecSaStatisticSaOutCnt_Type = Gauge32
_HwIPSecSaStatisticSaOutCnt_Object = MibTableColumn
hwIPSecSaStatisticSaOutCnt = _HwIPSecSaStatisticSaOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 3),
    _HwIPSecSaStatisticSaOutCnt_Type()
)
hwIPSecSaStatisticSaOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecSaStatisticSaOutCnt.setStatus("current")
_HwIPSecTunnelByteInput_Type = Counter64
_HwIPSecTunnelByteInput_Object = MibTableColumn
hwIPSecTunnelByteInput = _HwIPSecTunnelByteInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 4),
    _HwIPSecTunnelByteInput_Type()
)
hwIPSecTunnelByteInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelByteInput.setStatus("current")
_HwIPSecTunnelByteOutput_Type = Counter64
_HwIPSecTunnelByteOutput_Object = MibTableColumn
hwIPSecTunnelByteOutput = _HwIPSecTunnelByteOutput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 5),
    _HwIPSecTunnelByteOutput_Type()
)
hwIPSecTunnelByteOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelByteOutput.setStatus("current")
_HwIPSecTunnelPacketInput_Type = Counter64
_HwIPSecTunnelPacketInput_Object = MibTableColumn
hwIPSecTunnelPacketInput = _HwIPSecTunnelPacketInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 6),
    _HwIPSecTunnelPacketInput_Type()
)
hwIPSecTunnelPacketInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPacketInput.setStatus("current")
_HwIPSecTunnelPacketOutput_Type = Counter64
_HwIPSecTunnelPacketOutput_Object = MibTableColumn
hwIPSecTunnelPacketOutput = _HwIPSecTunnelPacketOutput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 7),
    _HwIPSecTunnelPacketOutput_Type()
)
hwIPSecTunnelPacketOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelPacketOutput.setStatus("current")
_HwIPSecTunnelDroppedPacketInput_Type = Counter64
_HwIPSecTunnelDroppedPacketInput_Object = MibTableColumn
hwIPSecTunnelDroppedPacketInput = _HwIPSecTunnelDroppedPacketInput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 8),
    _HwIPSecTunnelDroppedPacketInput_Type()
)
hwIPSecTunnelDroppedPacketInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelDroppedPacketInput.setStatus("current")
_HwIPSecTunnelDroppedPacketOutput_Type = Counter64
_HwIPSecTunnelDroppedPacketOutput_Object = MibTableColumn
hwIPSecTunnelDroppedPacketOutput = _HwIPSecTunnelDroppedPacketOutput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 9),
    _HwIPSecTunnelDroppedPacketOutput_Type()
)
hwIPSecTunnelDroppedPacketOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelDroppedPacketOutput.setStatus("current")
_HwIPSecTunnelDialUserCount_Type = Gauge32
_HwIPSecTunnelDialUserCount_Object = MibTableColumn
hwIPSecTunnelDialUserCount = _HwIPSecTunnelDialUserCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 10),
    _HwIPSecTunnelDialUserCount_Type()
)
hwIPSecTunnelDialUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelDialUserCount.setStatus("current")


class _HwIPSecSaStatisticTunnelPolicyAlias_Type(OctetString):
    """Custom type hwIPSecSaStatisticTunnelPolicyAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecSaStatisticTunnelPolicyAlias_Type.__name__ = "OctetString"
_HwIPSecSaStatisticTunnelPolicyAlias_Object = MibTableColumn
hwIPSecSaStatisticTunnelPolicyAlias = _HwIPSecSaStatisticTunnelPolicyAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 4, 1, 11),
    _HwIPSecSaStatisticTunnelPolicyAlias_Type()
)
hwIPSecSaStatisticTunnelPolicyAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecSaStatisticTunnelPolicyAlias.setStatus("current")
_HwIPSecTrapObject_ObjectIdentity = ObjectIdentity
hwIPSecTrapObject = _HwIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5)
)
_HwIPSecTrapTunnelPolicyNum_Type = Gauge32
_HwIPSecTrapTunnelPolicyNum_Object = MibScalar
hwIPSecTrapTunnelPolicyNum = _HwIPSecTrapTunnelPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 1),
    _HwIPSecTrapTunnelPolicyNum_Type()
)
hwIPSecTrapTunnelPolicyNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelPolicyNum.setStatus("current")
_HwIPSecTrapIfIndex_Type = Gauge32
_HwIPSecTrapIfIndex_Object = MibScalar
hwIPSecTrapIfIndex = _HwIPSecTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 2),
    _HwIPSecTrapIfIndex_Type()
)
hwIPSecTrapIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapIfIndex.setStatus("current")


class _HwIPSecTrapTunnelPolicyName_Type(OctetString):
    """Custom type hwIPSecTrapTunnelPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIPSecTrapTunnelPolicyName_Type.__name__ = "OctetString"
_HwIPSecTrapTunnelPolicyName_Object = MibScalar
hwIPSecTrapTunnelPolicyName = _HwIPSecTrapTunnelPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 3),
    _HwIPSecTrapTunnelPolicyName_Type()
)
hwIPSecTrapTunnelPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelPolicyName.setStatus("current")


class _HwIPSecTrapAuthenticationMethod_Type(OctetString):
    """Custom type hwIPSecTrapAuthenticationMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTrapAuthenticationMethod_Type.__name__ = "OctetString"
_HwIPSecTrapAuthenticationMethod_Object = MibScalar
hwIPSecTrapAuthenticationMethod = _HwIPSecTrapAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 4),
    _HwIPSecTrapAuthenticationMethod_Type()
)
hwIPSecTrapAuthenticationMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapAuthenticationMethod.setStatus("current")


class _HwIPSecTrapAuthenticationID_Type(OctetString):
    """Custom type hwIPSecTrapAuthenticationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIPSecTrapAuthenticationID_Type.__name__ = "OctetString"
_HwIPSecTrapAuthenticationID_Object = MibScalar
hwIPSecTrapAuthenticationID = _HwIPSecTrapAuthenticationID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 5),
    _HwIPSecTrapAuthenticationID_Type()
)
hwIPSecTrapAuthenticationID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapAuthenticationID.setStatus("current")


class _HwIPSecTrapAuthenticationIDType_Type(OctetString):
    """Custom type hwIPSecTrapAuthenticationIDType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPSecTrapAuthenticationIDType_Type.__name__ = "OctetString"
_HwIPSecTrapAuthenticationIDType_Object = MibScalar
hwIPSecTrapAuthenticationIDType = _HwIPSecTrapAuthenticationIDType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 6),
    _HwIPSecTrapAuthenticationIDType_Type()
)
hwIPSecTrapAuthenticationIDType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapAuthenticationIDType.setStatus("current")


class _HwIPSecTrapTunnelDstIP_Type(OctetString):
    """Custom type hwIPSecTrapTunnelDstIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTrapTunnelDstIP_Type.__name__ = "OctetString"
_HwIPSecTrapTunnelDstIP_Object = MibScalar
hwIPSecTrapTunnelDstIP = _HwIPSecTrapTunnelDstIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 7),
    _HwIPSecTrapTunnelDstIP_Type()
)
hwIPSecTrapTunnelDstIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelDstIP.setStatus("current")


class _HwIPSecTrapTunnelSrcIP_Type(OctetString):
    """Custom type hwIPSecTrapTunnelSrcIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTrapTunnelSrcIP_Type.__name__ = "OctetString"
_HwIPSecTrapTunnelSrcIP_Object = MibScalar
hwIPSecTrapTunnelSrcIP = _HwIPSecTrapTunnelSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 8),
    _HwIPSecTrapTunnelSrcIP_Type()
)
hwIPSecTrapTunnelSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelSrcIP.setStatus("current")
_HwIPSecTrapTunnelRemotePort_Type = Gauge32
_HwIPSecTrapTunnelRemotePort_Object = MibScalar
hwIPSecTrapTunnelRemotePort = _HwIPSecTrapTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 9),
    _HwIPSecTrapTunnelRemotePort_Type()
)
hwIPSecTrapTunnelRemotePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelRemotePort.setStatus("current")


class _HwIPSecReason_Type(OctetString):
    """Custom type hwIPSecReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecReason_Type.__name__ = "OctetString"
_HwIPSecReason_Object = MibScalar
hwIPSecReason = _HwIPSecReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 10),
    _HwIPSecReason_Type()
)
hwIPSecReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecReason.setStatus("current")
_HwIPSecReasonCode_Type = Gauge32
_HwIPSecReasonCode_Object = MibScalar
hwIPSecReasonCode = _HwIPSecReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 11),
    _HwIPSecReasonCode_Type()
)
hwIPSecReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecReasonCode.setStatus("current")


class _HwIPSecTrapTunnelOfflineReason_Type(OctetString):
    """Custom type hwIPSecTrapTunnelOfflineReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTrapTunnelOfflineReason_Type.__name__ = "OctetString"
_HwIPSecTrapTunnelOfflineReason_Object = MibScalar
hwIPSecTrapTunnelOfflineReason = _HwIPSecTrapTunnelOfflineReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 12),
    _HwIPSecTrapTunnelOfflineReason_Type()
)
hwIPSecTrapTunnelOfflineReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelOfflineReason.setStatus("current")


class _HwIPSecVsysName_Type(OctetString):
    """Custom type hwIPSecVsysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPSecVsysName_Type.__name__ = "OctetString"
_HwIPSecVsysName_Object = MibScalar
hwIPSecVsysName = _HwIPSecVsysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 13),
    _HwIPSecVsysName_Type()
)
hwIPSecVsysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecVsysName.setStatus("current")


class _HwIPSecTrapIfName_Type(OctetString):
    """Custom type hwIPSecTrapIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwIPSecTrapIfName_Type.__name__ = "OctetString"
_HwIPSecTrapIfName_Object = MibScalar
hwIPSecTrapIfName = _HwIPSecTrapIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 14),
    _HwIPSecTrapIfName_Type()
)
hwIPSecTrapIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapIfName.setStatus("current")


class _HwIPSecInitiator_Type(OctetString):
    """Custom type hwIPSecInitiator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HwIPSecInitiator_Type.__name__ = "OctetString"
_HwIPSecInitiator_Object = MibScalar
hwIPSecInitiator = _HwIPSecInitiator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 15),
    _HwIPSecInitiator_Type()
)
hwIPSecInitiator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecInitiator.setStatus("current")
_HwIPSecTrapTunnelDstIPMask_Type = Gauge32
_HwIPSecTrapTunnelDstIPMask_Object = MibScalar
hwIPSecTrapTunnelDstIPMask = _HwIPSecTrapTunnelDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 16),
    _HwIPSecTrapTunnelDstIPMask_Type()
)
hwIPSecTrapTunnelDstIPMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapTunnelDstIPMask.setStatus("current")


class _HwIPSecTrapRouteNextHope_Type(OctetString):
    """Custom type hwIPSecTrapRouteNextHope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTrapRouteNextHope_Type.__name__ = "OctetString"
_HwIPSecTrapRouteNextHope_Object = MibScalar
hwIPSecTrapRouteNextHope = _HwIPSecTrapRouteNextHope_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 17),
    _HwIPSecTrapRouteNextHope_Type()
)
hwIPSecTrapRouteNextHope.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapRouteNextHope.setStatus("current")
_HwIPSecTrapOprPri_Type = Gauge32
_HwIPSecTrapOprPri_Object = MibScalar
hwIPSecTrapOprPri = _HwIPSecTrapOprPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 18),
    _HwIPSecTrapOprPri_Type()
)
hwIPSecTrapOprPri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTrapOprPri.setStatus("current")


class _HwIPSecTunnelVpnName_Type(OctetString):
    """Custom type hwIPSecTunnelVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPSecTunnelVpnName_Type.__name__ = "OctetString"
_HwIPSecTunnelVpnName_Object = MibScalar
hwIPSecTunnelVpnName = _HwIPSecTunnelVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 19),
    _HwIPSecTunnelVpnName_Type()
)
hwIPSecTunnelVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTunnelVpnName.setStatus("current")


class _HwIPSecTunnelFlowVpnName_Type(OctetString):
    """Custom type hwIPSecTunnelFlowVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPSecTunnelFlowVpnName_Type.__name__ = "OctetString"
_HwIPSecTunnelFlowVpnName_Object = MibScalar
hwIPSecTunnelFlowVpnName = _HwIPSecTunnelFlowVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 20),
    _HwIPSecTunnelFlowVpnName_Type()
)
hwIPSecTunnelFlowVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTunnelFlowVpnName.setStatus("current")
_HwIPSecTunnelStatus_Type = Gauge32
_HwIPSecTunnelStatus_Object = MibScalar
hwIPSecTunnelStatus = _HwIPSecTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 21),
    _HwIPSecTunnelStatus_Type()
)
hwIPSecTunnelStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTunnelStatus.setStatus("current")


class _HwIPSecTunnelStatusChangeReason_Type(OctetString):
    """Custom type hwIPSecTunnelStatusChangeReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPSecTunnelStatusChangeReason_Type.__name__ = "OctetString"
_HwIPSecTunnelStatusChangeReason_Object = MibScalar
hwIPSecTunnelStatusChangeReason = _HwIPSecTunnelStatusChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 5, 22),
    _HwIPSecTunnelStatusChangeReason_Type()
)
hwIPSecTunnelStatusChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecTunnelStatusChangeReason.setStatus("current")
_HwIPSecNotifications_ObjectIdentity = ObjectIdentity
hwIPSecNotifications = _HwIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6)
)
_HwIPSecMibConformance_ObjectIdentity = ObjectIdentity
hwIPSecMibConformance = _HwIPSecMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7)
)
_HwIPSecMibCompliances_ObjectIdentity = ObjectIdentity
hwIPSecMibCompliances = _HwIPSecMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 1)
)
_HwIPSecMibGroups_ObjectIdentity = ObjectIdentity
hwIPSecMibGroups = _HwIPSecMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2)
)
_HwIPSecGdoiStatsTable_Object = MibTable
hwIPSecGdoiStatsTable = _HwIPSecGdoiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8)
)
if mibBuilder.loadTexts:
    hwIPSecGdoiStatsTable.setStatus("current")
_HwIPSecGdoiStatsEntry_Object = MibTableRow
hwIPSecGdoiStatsEntry = _HwIPSecGdoiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1)
)
hwIPSecGdoiStatsEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGdoiGroupID"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGdoiRemoteAddress"),
)
if mibBuilder.loadTexts:
    hwIPSecGdoiStatsEntry.setStatus("current")
_HwIPSecGdoiGroupID_Type = Gauge32
_HwIPSecGdoiGroupID_Object = MibTableColumn
hwIPSecGdoiGroupID = _HwIPSecGdoiGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 1),
    _HwIPSecGdoiGroupID_Type()
)
hwIPSecGdoiGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecGdoiGroupID.setStatus("current")
_HwIPSecGdoiRemoteAddress_Type = IpAddress
_HwIPSecGdoiRemoteAddress_Object = MibTableColumn
hwIPSecGdoiRemoteAddress = _HwIPSecGdoiRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 2),
    _HwIPSecGdoiRemoteAddress_Type()
)
hwIPSecGdoiRemoteAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPSecGdoiRemoteAddress.setStatus("current")
_HwIPSecTunnelSendPacket_Type = Counter64
_HwIPSecTunnelSendPacket_Object = MibTableColumn
hwIPSecTunnelSendPacket = _HwIPSecTunnelSendPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 3),
    _HwIPSecTunnelSendPacket_Type()
)
hwIPSecTunnelSendPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSendPacket.setStatus("current")
_HwIPSecTunnelSendSize_Type = Counter64
_HwIPSecTunnelSendSize_Object = MibTableColumn
hwIPSecTunnelSendSize = _HwIPSecTunnelSendSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 4),
    _HwIPSecTunnelSendSize_Type()
)
hwIPSecTunnelSendSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSendSize.setStatus("current")
_HwIPSecTunnelSendErrorPacket_Type = Counter64
_HwIPSecTunnelSendErrorPacket_Object = MibTableColumn
hwIPSecTunnelSendErrorPacket = _HwIPSecTunnelSendErrorPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 5),
    _HwIPSecTunnelSendErrorPacket_Type()
)
hwIPSecTunnelSendErrorPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSendErrorPacket.setStatus("current")
_HwIPSecTunnelSendErrorSize_Type = Counter64
_HwIPSecTunnelSendErrorSize_Object = MibTableColumn
hwIPSecTunnelSendErrorSize = _HwIPSecTunnelSendErrorSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 6),
    _HwIPSecTunnelSendErrorSize_Type()
)
hwIPSecTunnelSendErrorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelSendErrorSize.setStatus("current")
_HwIPSecTunnelRecvPacket_Type = Counter64
_HwIPSecTunnelRecvPacket_Object = MibTableColumn
hwIPSecTunnelRecvPacket = _HwIPSecTunnelRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 7),
    _HwIPSecTunnelRecvPacket_Type()
)
hwIPSecTunnelRecvPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRecvPacket.setStatus("current")
_HwIPSecTunnelRecvSize_Type = Counter64
_HwIPSecTunnelRecvSize_Object = MibTableColumn
hwIPSecTunnelRecvSize = _HwIPSecTunnelRecvSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 8),
    _HwIPSecTunnelRecvSize_Type()
)
hwIPSecTunnelRecvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRecvSize.setStatus("current")
_HwIPSecTunnelRecvErrorPacket_Type = Counter64
_HwIPSecTunnelRecvErrorPacket_Object = MibTableColumn
hwIPSecTunnelRecvErrorPacket = _HwIPSecTunnelRecvErrorPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 9),
    _HwIPSecTunnelRecvErrorPacket_Type()
)
hwIPSecTunnelRecvErrorPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRecvErrorPacket.setStatus("current")
_HwIPSecTunnelRecvErrorSize_Type = Counter64
_HwIPSecTunnelRecvErrorSize_Object = MibTableColumn
hwIPSecTunnelRecvErrorSize = _HwIPSecTunnelRecvErrorSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 8, 1, 10),
    _HwIPSecTunnelRecvErrorSize_Type()
)
hwIPSecTunnelRecvErrorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTunnelRecvErrorSize.setStatus("current")
_HwIPSecTEKSAStatusTable_Object = MibTable
hwIPSecTEKSAStatusTable = _HwIPSecTEKSAStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 9)
)
if mibBuilder.loadTexts:
    hwIPSecTEKSAStatusTable.setStatus("current")
_HwIPSecTEKSAStatusEntry_Object = MibTableRow
hwIPSecTEKSAStatusEntry = _HwIPSecTEKSAStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 9, 1)
)
hwIPSecTEKSAStatusEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGdoiGroupID"),
    (0, "HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGdoiRemoteAddress"),
)
if mibBuilder.loadTexts:
    hwIPSecTEKSAStatusEntry.setStatus("current")


class _HwIPSecTEKSAStatus_Type(Integer32):
    """Custom type hwIPSecTEKSAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("teksa", 0),
          ("noteksa", 1))
    )


_HwIPSecTEKSAStatus_Type.__name__ = "Integer32"
_HwIPSecTEKSAStatus_Object = MibTableColumn
hwIPSecTEKSAStatus = _HwIPSecTEKSAStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 9, 1, 1),
    _HwIPSecTEKSAStatus_Type()
)
hwIPSecTEKSAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSecTEKSAStatus.setStatus("current")

# Managed Objects groups

hwIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 1)
)
hwIPSecGlobalStatsGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalTotal"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalPacketInput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalPacketOutput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalByteInput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalByteOutput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalDroppedPacketInput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalDroppedPacketOutput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalEncIntactPacket"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalEncPacketFirstSlice"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalEncPacketAfterSlice"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalDecPacketReassFirstSlice"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalDecPacketReassAfterSlice"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalDecPacketReassLenErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalPacketHeaderWrong"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalMemoryApplyFail"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalCannotFindSA"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalWrongSA"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalBadAuthentication"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalReplay"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalPreRecheckErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalPostRecheckErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalExceedByteLimit"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalExceedPacketLimit"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalProcessIpv4Err"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalFibSearchErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalIKEInboundOK"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalIKEInboundErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalIKEOutboundOK"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalIKEOutboundErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalSoftExpr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalHardExpr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalDPDOper"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalModpCnt"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalSaeSucc"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalSoftwareSucc"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalConnectionRate"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalTotalPhase1Num"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalBytesPerSecondIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalBytesPerSecondOut"))
)
if mibBuilder.loadTexts:
    hwIPSecGlobalStatsGroup.setStatus("current")

hwIPSecTunnelConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 2)
)
hwIPSecTunnelConfigTableGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRuleId"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInsideIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRemotePort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelCpuID"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelEncapMode"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelNatTraver"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFromIKEV2"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelEncryptMode"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelESPDigestMode"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelAHDigestMode"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelProto"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelOutPortIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSrcPort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDstPort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelVrfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelIfVrfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSrcIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSpeedLimitIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSpeedLimitOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInitiator"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelLifeSize"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelLifeTime"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSaStatus"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSlotID"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowInfo"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyAlias"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDstIPv6"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInsideIPv6"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSrcIPv6"))
)
if mibBuilder.loadTexts:
    hwIPSecTunnelConfigTableGroup.setStatus("current")

hwIPSecTunnelStatsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 3)
)
hwIPSecTunnelStatsTableGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSaIDIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSaIDOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowSoftExpireIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowSoftExpireOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowHardExpireIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowHardExpireOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRemainTime"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRemainSize"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSpiIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSpiOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInSideSpiIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInSideSpiOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelESPSequenceNumberIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelESPSequenceNumberOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnellAHSequenceNumberIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnellAHSequenceNumberOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelMemApplyFail"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelBadAuth"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelReplay"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelAfterReCheckErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPktDropByteLimitIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPktDropByteLimitOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFIBSearchErr"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelBytesPerSecondIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelBytesPerSecondOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPacketsPerSecondIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPacketsPerSecondOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelErrPacketsPerSecondIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelErrPacketsPerSecondOut"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelErrPacketsIn"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelErrPacketsOut"))
)
if mibBuilder.loadTexts:
    hwIPSecTunnelStatsTableGroup.setStatus("current")

hwIPSecSaStatisticTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 4)
)
hwIPSecSaStatisticTableGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecSaStatisticTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecSaStatisticSaInCnt"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecSaStatisticSaOutCnt"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelByteInput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelByteOutput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPacketInput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPacketOutput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDroppedPacketInput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDroppedPacketOutput"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDialUserCount"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecSaStatisticTunnelPolicyAlias"))
)
if mibBuilder.loadTexts:
    hwIPSecSaStatisticTableGroup.setStatus("current")

hwIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 5)
)
hwIPSecTrapObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyName"))
)
if mibBuilder.loadTexts:
    hwIPSecTrapObjectGroup.setStatus("current")

hwIPSecGdoiStatsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 7)
)
hwIPSecGdoiStatsTableGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSendPacket"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSendSize"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSendErrorPacket"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSendErrorSize"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRecvPacket"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRecvSize"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRecvErrorPacket"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRecvErrorSize"))
)
if mibBuilder.loadTexts:
    hwIPSecGdoiStatsTableGroup.setStatus("current")


# Notification objects

hwIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 1)
)
hwIPSecTunnelStart.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRuleId"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInsideIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRemotePort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelCpuID"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSrcIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowInfo"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelLifeSize"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelLifeTime"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSlotID"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecInitiator"))
)
if mibBuilder.loadTexts:
    hwIPSecTunnelStart.setStatus(
        "current"
    )

hwIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 2)
)
hwIPSecTunnelStop.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRuleId"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelInsideIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelRemotePort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelCpuID"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSrcIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowInfo"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelOfflineReason"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSlotID"))
)
if mibBuilder.loadTexts:
    hwIPSecTunnelStop.setStatus(
        "current"
    )

hwIPSecPolicyAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 3)
)
hwIPSecPolicyAdd.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"))
)
if mibBuilder.loadTexts:
    hwIPSecPolicyAdd.setStatus(
        "current"
    )

hwIPSecPolicyDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 4)
)
hwIPSecPolicyDel.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"))
)
if mibBuilder.loadTexts:
    hwIPSecPolicyDel.setStatus(
        "current"
    )

hwIPSecPolicyAttach = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 5)
)
hwIPSecPolicyAttach.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"))
)
if mibBuilder.loadTexts:
    hwIPSecPolicyAttach.setStatus(
        "current"
    )

hwIPSecPolicyDetach = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 6)
)
hwIPSecPolicyDetach.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"))
)
if mibBuilder.loadTexts:
    hwIPSecPolicyDetach.setStatus(
        "current"
    )

hwIPSecIKEReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 7)
)
hwIPSecIKEReset.setObjects(
    ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName")
)
if mibBuilder.loadTexts:
    hwIPSecIKEReset.setStatus(
        "current"
    )

hwIPSecIPSecReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 8)
)
hwIPSecIPSecReset.setObjects(
    ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName")
)
if mibBuilder.loadTexts:
    hwIPSecIPSecReset.setStatus(
        "current"
    )

hwIPSecTunnelReachMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 9)
)
if mibBuilder.loadTexts:
    hwIPSecTunnelReachMax.setStatus(
        "current"
    )

hwIPSecTunnelReachMaxAtOnce = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 10)
)
if mibBuilder.loadTexts:
    hwIPSecTunnelReachMaxAtOnce.setStatus(
        "current"
    )

hwIKEPeerReachMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 11)
)
if mibBuilder.loadTexts:
    hwIKEPeerReachMax.setStatus(
        "current"
    )

hwIKEPeerReachMaxAtOnce = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 12)
)
if mibBuilder.loadTexts:
    hwIKEPeerReachMaxAtOnce.setStatus(
        "current"
    )

hwIKESaPhase1Establish = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 13)
)
hwIKESaPhase1Establish.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelRemotePort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelSrcIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapAuthenticationMethod"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapAuthenticationID"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapAuthenticationIDType"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecInitiator"))
)
if mibBuilder.loadTexts:
    hwIKESaPhase1Establish.setStatus(
        "current"
    )

hwIPSecNegoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 14)
)
hwIPSecNegoFail.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecReason"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecReasonCode"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelRemotePort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"))
)
if mibBuilder.loadTexts:
    hwIPSecNegoFail.setStatus(
        "current"
    )

hwIPSecTunnelHaveReachMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 15)
)
if mibBuilder.loadTexts:
    hwIPSecTunnelHaveReachMax.setStatus(
        "current"
    )

hwIPSecOPRRouteMissed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 16)
)
hwIPSecOPRRouteMissed.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelDstIPMask"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapRouteNextHope"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfIndex"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapOprPri"))
)
if mibBuilder.loadTexts:
    hwIPSecOPRRouteMissed.setStatus(
        "current"
    )

hwIPSecLowSecurityLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 17)
)
if mibBuilder.loadTexts:
    hwIPSecLowSecurityLevel.setStatus(
        "current"
    )

hwIPSecWeakEncr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 18)
)
hwIPSecWeakEncr.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"))
)
if mibBuilder.loadTexts:
    hwIPSecWeakEncr.setStatus(
        "current"
    )

hwIPSecTunnelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 6, 19)
)
hwIPSecTunnelStatusChange.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecVsysName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapIfName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyNum"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelPolicyAlias"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelVpnName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowVpnName"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelDstIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelDstPort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapTunnelSrcIP"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelSrcPort"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelFlowInfo"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelStatusChangeReason"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelStatus"))
)
if mibBuilder.loadTexts:
    hwIPSecTunnelStatusChange.setStatus(
        "current"
    )


# Notifications groups

hwIPSecNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 2, 6)
)
hwIPSecNotificationsGroup.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelStart"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelStop"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecPolicyAdd"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecPolicyDel"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecPolicyAttach"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecPolicyDetach"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIKEReset"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecIPSecReset"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelReachMax"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelReachMaxAtOnce"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIKEPeerReachMax"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIKEPeerReachMaxAtOnce"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIKESaPhase1Establish"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecNegoFail"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelStatusChange"))
)
if mibBuilder.loadTexts:
    hwIPSecNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIPSecMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 26, 7, 1, 1)
)
hwIPSecMibCompliance.setObjects(
      *(("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecGlobalStatsGroup"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelConfigTableGroup"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTunnelStatsTableGroup"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecSaStatisticTableGroup"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecTrapObjectGroup"),
        ("HUAWEI-SECURITY-IPSEC-MIB", "hwIPSecNotificationsGroup"))
)
if mibBuilder.loadTexts:
    hwIPSecMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-IPSEC-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwIpsec": hwIpsec,
       "hwIPSecGlobalStats": hwIPSecGlobalStats,
       "hwIPSecGlobalTotal": hwIPSecGlobalTotal,
       "hwIPSecGlobalPacketInput": hwIPSecGlobalPacketInput,
       "hwIPSecGlobalPacketOutput": hwIPSecGlobalPacketOutput,
       "hwIPSecGlobalByteInput": hwIPSecGlobalByteInput,
       "hwIPSecGlobalByteOutput": hwIPSecGlobalByteOutput,
       "hwIPSecGlobalDroppedPacketInput": hwIPSecGlobalDroppedPacketInput,
       "hwIPSecGlobalDroppedPacketOutput": hwIPSecGlobalDroppedPacketOutput,
       "hwIPSecGlobalEncIntactPacket": hwIPSecGlobalEncIntactPacket,
       "hwIPSecGlobalEncPacketFirstSlice": hwIPSecGlobalEncPacketFirstSlice,
       "hwIPSecGlobalEncPacketAfterSlice": hwIPSecGlobalEncPacketAfterSlice,
       "hwIPSecGlobalDecPacketReassFirstSlice": hwIPSecGlobalDecPacketReassFirstSlice,
       "hwIPSecGlobalDecPacketReassAfterSlice": hwIPSecGlobalDecPacketReassAfterSlice,
       "hwIPSecGlobalDecPacketReassLenErr": hwIPSecGlobalDecPacketReassLenErr,
       "hwIPSecGlobalPacketHeaderWrong": hwIPSecGlobalPacketHeaderWrong,
       "hwIPSecGlobalMemoryApplyFail": hwIPSecGlobalMemoryApplyFail,
       "hwIPSecGlobalCannotFindSA": hwIPSecGlobalCannotFindSA,
       "hwIPSecGlobalWrongSA": hwIPSecGlobalWrongSA,
       "hwIPSecGlobalBadAuthentication": hwIPSecGlobalBadAuthentication,
       "hwIPSecGlobalReplay": hwIPSecGlobalReplay,
       "hwIPSecGlobalPreRecheckErr": hwIPSecGlobalPreRecheckErr,
       "hwIPSecGlobalPostRecheckErr": hwIPSecGlobalPostRecheckErr,
       "hwIPSecGlobalExceedByteLimit": hwIPSecGlobalExceedByteLimit,
       "hwIPSecGlobalExceedPacketLimit": hwIPSecGlobalExceedPacketLimit,
       "hwIPSecGlobalProcessIpv4Err": hwIPSecGlobalProcessIpv4Err,
       "hwIPSecGlobalFibSearchErr": hwIPSecGlobalFibSearchErr,
       "hwIPSecGlobalIKEInboundOK": hwIPSecGlobalIKEInboundOK,
       "hwIPSecGlobalIKEInboundErr": hwIPSecGlobalIKEInboundErr,
       "hwIPSecGlobalIKEOutboundOK": hwIPSecGlobalIKEOutboundOK,
       "hwIPSecGlobalIKEOutboundErr": hwIPSecGlobalIKEOutboundErr,
       "hwIPSecGlobalSoftExpr": hwIPSecGlobalSoftExpr,
       "hwIPSecGlobalHardExpr": hwIPSecGlobalHardExpr,
       "hwIPSecGlobalDPDOper": hwIPSecGlobalDPDOper,
       "hwIPSecGlobalModpCnt": hwIPSecGlobalModpCnt,
       "hwIPSecGlobalSaeSucc": hwIPSecGlobalSaeSucc,
       "hwIPSecGlobalSoftwareSucc": hwIPSecGlobalSoftwareSucc,
       "hwIPSecGlobalConnectionRate": hwIPSecGlobalConnectionRate,
       "hwIPSecGlobalTotalPhase1Num": hwIPSecGlobalTotalPhase1Num,
       "hwIPSecGlobalBytesPerSecondIn": hwIPSecGlobalBytesPerSecondIn,
       "hwIPSecGlobalBytesPerSecondOut": hwIPSecGlobalBytesPerSecondOut,
       "hwIPSecTunnelConfigTable": hwIPSecTunnelConfigTable,
       "hwIPSecTunnelConfigEntry": hwIPSecTunnelConfigEntry,
       "hwIPSecIfIndex": hwIPSecIfIndex,
       "hwIPSecTunnelPolicyNum": hwIPSecTunnelPolicyNum,
       "hwIPSecTunnelIndex": hwIPSecTunnelIndex,
       "hwIPSecTunnelRuleId": hwIPSecTunnelRuleId,
       "hwIPSecTunnelDstIP": hwIPSecTunnelDstIP,
       "hwIPSecTunnelInsideIP": hwIPSecTunnelInsideIP,
       "hwIPSecTunnelRemotePort": hwIPSecTunnelRemotePort,
       "hwIPSecTunnelCpuID": hwIPSecTunnelCpuID,
       "hwIPSecTunnelEncapMode": hwIPSecTunnelEncapMode,
       "hwIPSecTunnelNatTraver": hwIPSecTunnelNatTraver,
       "hwIPSecTunnelFromIKEV2": hwIPSecTunnelFromIKEV2,
       "hwIPSecTunnelEncryptMode": hwIPSecTunnelEncryptMode,
       "hwIPSecTunnelESPDigestMode": hwIPSecTunnelESPDigestMode,
       "hwIPSecTunnelAHDigestMode": hwIPSecTunnelAHDigestMode,
       "hwIPSecTunnelProto": hwIPSecTunnelProto,
       "hwIPSecTunnelOutPortIndex": hwIPSecTunnelOutPortIndex,
       "hwIPSecTunnelSrcPort": hwIPSecTunnelSrcPort,
       "hwIPSecTunnelDstPort": hwIPSecTunnelDstPort,
       "hwIPSecTunnelVrfIndex": hwIPSecTunnelVrfIndex,
       "hwIPSecTunnelIfVrfIndex": hwIPSecTunnelIfVrfIndex,
       "hwIPSecTunnelSrcIP": hwIPSecTunnelSrcIP,
       "hwIPSecTunnelSpeedLimitIn": hwIPSecTunnelSpeedLimitIn,
       "hwIPSecTunnelSpeedLimitOut": hwIPSecTunnelSpeedLimitOut,
       "hwIPSecTunnelInitiator": hwIPSecTunnelInitiator,
       "hwIPSecTunnelLifeSize": hwIPSecTunnelLifeSize,
       "hwIPSecTunnelLifeTime": hwIPSecTunnelLifeTime,
       "hwIPSecTunnelPolicyName": hwIPSecTunnelPolicyName,
       "hwIPSecTunnelSaStatus": hwIPSecTunnelSaStatus,
       "hwIPSecTunnelSlotID": hwIPSecTunnelSlotID,
       "hwIPSecTunnelFlowInfo": hwIPSecTunnelFlowInfo,
       "hwIPSecTunnelPolicyAlias": hwIPSecTunnelPolicyAlias,
       "hwIPSecTunnelDstIPv6": hwIPSecTunnelDstIPv6,
       "hwIPSecTunnelInsideIPv6": hwIPSecTunnelInsideIPv6,
       "hwIPSecTunnelSrcIPv6": hwIPSecTunnelSrcIPv6,
       "hwIPSecTunnelStatsTable": hwIPSecTunnelStatsTable,
       "hwIPSecTunnelStatsEntry": hwIPSecTunnelStatsEntry,
       "hwIPSecTunnelSaIDIn": hwIPSecTunnelSaIDIn,
       "hwIPSecTunnelSaIDOut": hwIPSecTunnelSaIDOut,
       "hwIPSecTunnelFlowSoftExpireIn": hwIPSecTunnelFlowSoftExpireIn,
       "hwIPSecTunnelFlowSoftExpireOut": hwIPSecTunnelFlowSoftExpireOut,
       "hwIPSecTunnelFlowHardExpireIn": hwIPSecTunnelFlowHardExpireIn,
       "hwIPSecTunnelFlowHardExpireOut": hwIPSecTunnelFlowHardExpireOut,
       "hwIPSecTunnelRemainTime": hwIPSecTunnelRemainTime,
       "hwIPSecTunnelRemainSize": hwIPSecTunnelRemainSize,
       "hwIPSecTunnelSpiIn": hwIPSecTunnelSpiIn,
       "hwIPSecTunnelSpiOut": hwIPSecTunnelSpiOut,
       "hwIPSecTunnelInSideSpiIn": hwIPSecTunnelInSideSpiIn,
       "hwIPSecTunnelInSideSpiOut": hwIPSecTunnelInSideSpiOut,
       "hwIPSecTunnelESPSequenceNumberIn": hwIPSecTunnelESPSequenceNumberIn,
       "hwIPSecTunnelESPSequenceNumberOut": hwIPSecTunnelESPSequenceNumberOut,
       "hwIPSecTunnellAHSequenceNumberIn": hwIPSecTunnellAHSequenceNumberIn,
       "hwIPSecTunnellAHSequenceNumberOut": hwIPSecTunnellAHSequenceNumberOut,
       "hwIPSecTunnelMemApplyFail": hwIPSecTunnelMemApplyFail,
       "hwIPSecTunnelBadAuth": hwIPSecTunnelBadAuth,
       "hwIPSecTunnelReplay": hwIPSecTunnelReplay,
       "hwIPSecTunnelAfterReCheckErr": hwIPSecTunnelAfterReCheckErr,
       "hwIPSecTunnelPktDropByteLimitIn": hwIPSecTunnelPktDropByteLimitIn,
       "hwIPSecTunnelPktDropByteLimitOut": hwIPSecTunnelPktDropByteLimitOut,
       "hwIPSecTunnelFIBSearchErr": hwIPSecTunnelFIBSearchErr,
       "hwIPSecTunnelBytesPerSecondIn": hwIPSecTunnelBytesPerSecondIn,
       "hwIPSecTunnelBytesPerSecondOut": hwIPSecTunnelBytesPerSecondOut,
       "hwIPSecTunnelPacketsPerSecondIn": hwIPSecTunnelPacketsPerSecondIn,
       "hwIPSecTunnelPacketsPerSecondOut": hwIPSecTunnelPacketsPerSecondOut,
       "hwIPSecTunnelErrPacketsPerSecondIn": hwIPSecTunnelErrPacketsPerSecondIn,
       "hwIPSecTunnelErrPacketsPerSecondOut": hwIPSecTunnelErrPacketsPerSecondOut,
       "hwIPSecTunnelErrPacketsIn": hwIPSecTunnelErrPacketsIn,
       "hwIPSecTunnelErrPacketsOut": hwIPSecTunnelErrPacketsOut,
       "hwIPSecSaStatisticTable": hwIPSecSaStatisticTable,
       "hwIPSecSaStatisticEntry": hwIPSecSaStatisticEntry,
       "hwIPSecSaStatisticTunnelPolicyName": hwIPSecSaStatisticTunnelPolicyName,
       "hwIPSecSaStatisticSaInCnt": hwIPSecSaStatisticSaInCnt,
       "hwIPSecSaStatisticSaOutCnt": hwIPSecSaStatisticSaOutCnt,
       "hwIPSecTunnelByteInput": hwIPSecTunnelByteInput,
       "hwIPSecTunnelByteOutput": hwIPSecTunnelByteOutput,
       "hwIPSecTunnelPacketInput": hwIPSecTunnelPacketInput,
       "hwIPSecTunnelPacketOutput": hwIPSecTunnelPacketOutput,
       "hwIPSecTunnelDroppedPacketInput": hwIPSecTunnelDroppedPacketInput,
       "hwIPSecTunnelDroppedPacketOutput": hwIPSecTunnelDroppedPacketOutput,
       "hwIPSecTunnelDialUserCount": hwIPSecTunnelDialUserCount,
       "hwIPSecSaStatisticTunnelPolicyAlias": hwIPSecSaStatisticTunnelPolicyAlias,
       "hwIPSecTrapObject": hwIPSecTrapObject,
       "hwIPSecTrapTunnelPolicyNum": hwIPSecTrapTunnelPolicyNum,
       "hwIPSecTrapIfIndex": hwIPSecTrapIfIndex,
       "hwIPSecTrapTunnelPolicyName": hwIPSecTrapTunnelPolicyName,
       "hwIPSecTrapAuthenticationMethod": hwIPSecTrapAuthenticationMethod,
       "hwIPSecTrapAuthenticationID": hwIPSecTrapAuthenticationID,
       "hwIPSecTrapAuthenticationIDType": hwIPSecTrapAuthenticationIDType,
       "hwIPSecTrapTunnelDstIP": hwIPSecTrapTunnelDstIP,
       "hwIPSecTrapTunnelSrcIP": hwIPSecTrapTunnelSrcIP,
       "hwIPSecTrapTunnelRemotePort": hwIPSecTrapTunnelRemotePort,
       "hwIPSecReason": hwIPSecReason,
       "hwIPSecReasonCode": hwIPSecReasonCode,
       "hwIPSecTrapTunnelOfflineReason": hwIPSecTrapTunnelOfflineReason,
       "hwIPSecVsysName": hwIPSecVsysName,
       "hwIPSecTrapIfName": hwIPSecTrapIfName,
       "hwIPSecInitiator": hwIPSecInitiator,
       "hwIPSecTrapTunnelDstIPMask": hwIPSecTrapTunnelDstIPMask,
       "hwIPSecTrapRouteNextHope": hwIPSecTrapRouteNextHope,
       "hwIPSecTrapOprPri": hwIPSecTrapOprPri,
       "hwIPSecTunnelVpnName": hwIPSecTunnelVpnName,
       "hwIPSecTunnelFlowVpnName": hwIPSecTunnelFlowVpnName,
       "hwIPSecTunnelStatus": hwIPSecTunnelStatus,
       "hwIPSecTunnelStatusChangeReason": hwIPSecTunnelStatusChangeReason,
       "hwIPSecNotifications": hwIPSecNotifications,
       "hwIPSecTunnelStart": hwIPSecTunnelStart,
       "hwIPSecTunnelStop": hwIPSecTunnelStop,
       "hwIPSecPolicyAdd": hwIPSecPolicyAdd,
       "hwIPSecPolicyDel": hwIPSecPolicyDel,
       "hwIPSecPolicyAttach": hwIPSecPolicyAttach,
       "hwIPSecPolicyDetach": hwIPSecPolicyDetach,
       "hwIPSecIKEReset": hwIPSecIKEReset,
       "hwIPSecIPSecReset": hwIPSecIPSecReset,
       "hwIPSecTunnelReachMax": hwIPSecTunnelReachMax,
       "hwIPSecTunnelReachMaxAtOnce": hwIPSecTunnelReachMaxAtOnce,
       "hwIKEPeerReachMax": hwIKEPeerReachMax,
       "hwIKEPeerReachMaxAtOnce": hwIKEPeerReachMaxAtOnce,
       "hwIKESaPhase1Establish": hwIKESaPhase1Establish,
       "hwIPSecNegoFail": hwIPSecNegoFail,
       "hwIPSecTunnelHaveReachMax": hwIPSecTunnelHaveReachMax,
       "hwIPSecOPRRouteMissed": hwIPSecOPRRouteMissed,
       "hwIPSecLowSecurityLevel": hwIPSecLowSecurityLevel,
       "hwIPSecWeakEncr": hwIPSecWeakEncr,
       "hwIPSecTunnelStatusChange": hwIPSecTunnelStatusChange,
       "hwIPSecMibConformance": hwIPSecMibConformance,
       "hwIPSecMibCompliances": hwIPSecMibCompliances,
       "hwIPSecMibCompliance": hwIPSecMibCompliance,
       "hwIPSecMibGroups": hwIPSecMibGroups,
       "hwIPSecGlobalStatsGroup": hwIPSecGlobalStatsGroup,
       "hwIPSecTunnelConfigTableGroup": hwIPSecTunnelConfigTableGroup,
       "hwIPSecTunnelStatsTableGroup": hwIPSecTunnelStatsTableGroup,
       "hwIPSecSaStatisticTableGroup": hwIPSecSaStatisticTableGroup,
       "hwIPSecTrapObjectGroup": hwIPSecTrapObjectGroup,
       "hwIPSecNotificationsGroup": hwIPSecNotificationsGroup,
       "hwIPSecGdoiStatsTableGroup": hwIPSecGdoiStatsTableGroup,
       "hwIPSecGdoiStatsTable": hwIPSecGdoiStatsTable,
       "hwIPSecGdoiStatsEntry": hwIPSecGdoiStatsEntry,
       "hwIPSecGdoiGroupID": hwIPSecGdoiGroupID,
       "hwIPSecGdoiRemoteAddress": hwIPSecGdoiRemoteAddress,
       "hwIPSecTunnelSendPacket": hwIPSecTunnelSendPacket,
       "hwIPSecTunnelSendSize": hwIPSecTunnelSendSize,
       "hwIPSecTunnelSendErrorPacket": hwIPSecTunnelSendErrorPacket,
       "hwIPSecTunnelSendErrorSize": hwIPSecTunnelSendErrorSize,
       "hwIPSecTunnelRecvPacket": hwIPSecTunnelRecvPacket,
       "hwIPSecTunnelRecvSize": hwIPSecTunnelRecvSize,
       "hwIPSecTunnelRecvErrorPacket": hwIPSecTunnelRecvErrorPacket,
       "hwIPSecTunnelRecvErrorSize": hwIPSecTunnelRecvErrorSize,
       "hwIPSecTEKSAStatusTable": hwIPSecTEKSAStatusTable,
       "hwIPSecTEKSAStatusEntry": hwIPSecTEKSAStatusEntry,
       "hwIPSecTEKSAStatus": hwIPSecTEKSAStatus}
)
