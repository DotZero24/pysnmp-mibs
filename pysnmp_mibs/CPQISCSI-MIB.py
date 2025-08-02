_AC='cpqiScsiCxnAttrIndex'
_AB='cpqiScsiCxnAttrSessionIndex'
_AA='cpqiScsiCxnAttrNodeIndex'
_A9='cpqiScsiCxnAttrInstIndex'
_A8='cpqiScsiSsnCxnIndex'
_A7='cpqiScsiSsnCxnNodeIndex'
_A6='cpqiScsiSsnCxnInstIndex'
_A5='cpqiScsiSsnSessionIndex'
_A4='cpqiScsiSsnStatNodeIndex'
_A3='cpqiScsiSsnStatInstIndex'
_A2='cpqiScsiSsnIndex'
_A1='cpqiScsiSsnNodeIndex'
_A0='cpqiScsiSsnInstIndex'
_z='cpqiScsiIntrAuthIndex'
_y='cpqiScsiIntrAuthNodeIndex'
_x='cpqiScsiIntrAuthInstIndex'
_w='cpqiScsiIntrLogoutNodeIndex'
_v='cpqiScsiIntrLogoutInstIndex'
_u='cpqiScsiIntrLoginNodeIndex'
_t='cpqiScsiIntrLoginInstIndex'
_s='cpqiScsiIntrNodeIndex'
_r='cpqiScsiIntrInstIndex'
_q='cpqiScsiTgtAuthIndex'
_p='cpqiScsiTgtAuthNodeIndex'
_o='cpqiScsiTgtAuthInstIndex'
_n='cpqiScsiTgtLogoutNodeIndex'
_m='cpqiScsiTgtLogoutInstIndex'
_l='cpqiScsiTgtLoginNodeIndex'
_k='cpqiScsiTgtLoginInstIndex'
_j='cpqiScsiTgtNodeIndex'
_i='cpqiScsiTgtInstIndex'
_h='cpqiScsiNodeNodeIndex'
_g='cpqiScsiNodeInstIndex'
_f='DisplayString'
_e='NotificationType'
_d='cpqiScsiInstDescr'
_c='destroy'
_b='createAndWait'
_a='createAndGo'
_Z='notReady'
_Y='notInService'
_X='active'
_W='sysName'
_V='SNMPv2-MIB'
_U='cpqHoTrapFlags'
_T='CPQHOST-MIB'
_S='cpqiScsiPortalIndex'
_R='dns'
_Q='ipv6z'
_P='ipv4z'
_O='ipv6'
_N='ipv4'
_M='crc32c'
_L='noDigest'
_K='none'
_J='cpqiScsiInstIndex'
_I='other'
_H='OctetString'
_G='false'
_F='true'
_E='read-write'
_D='CPQISCSI-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_T,'compaq',_U)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_V,_W)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_e,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_e,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_f,'PhysAddress','TextualConvention')
_CpqiScsiModule_ObjectIdentity=ObjectIdentity
cpqiScsiModule=_CpqiScsiModule_ObjectIdentity((1,3,6,1,4,1,232,169))
_CpqiScsiMibRev_ObjectIdentity=ObjectIdentity
cpqiScsiMibRev=_CpqiScsiMibRev_ObjectIdentity((1,3,6,1,4,1,232,169,1))
class _CpqiScsiMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiMibRevMajor_Type.__name__=_C
_CpqiScsiMibRevMajor_Object=MibScalar
cpqiScsiMibRevMajor=_CpqiScsiMibRevMajor_Object((1,3,6,1,4,1,232,169,1,1),_CpqiScsiMibRevMajor_Type())
cpqiScsiMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiMibRevMajor.setStatus(_A)
class _CpqiScsiMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqiScsiMibRevMinor_Type.__name__=_C
_CpqiScsiMibRevMinor_Object=MibScalar
cpqiScsiMibRevMinor=_CpqiScsiMibRevMinor_Object((1,3,6,1,4,1,232,169,1,2),_CpqiScsiMibRevMinor_Type())
cpqiScsiMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiMibRevMinor.setStatus(_A)
class _CpqiScsiMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('ok',2),('degraded',3),('failed',4)))
_CpqiScsiMibCondition_Type.__name__=_C
_CpqiScsiMibCondition_Object=MibScalar
cpqiScsiMibCondition=_CpqiScsiMibCondition_Object((1,3,6,1,4,1,232,169,1,3),_CpqiScsiMibCondition_Type())
cpqiScsiMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiMibCondition.setStatus(_A)
_CpqiScsiObjects_ObjectIdentity=ObjectIdentity
cpqiScsiObjects=_CpqiScsiObjects_ObjectIdentity((1,3,6,1,4,1,232,169,2))
_CpqiScsiDescriptors_ObjectIdentity=ObjectIdentity
cpqiScsiDescriptors=_CpqiScsiDescriptors_ObjectIdentity((1,3,6,1,4,1,232,169,2,1))
_CpqiScsiInstance_ObjectIdentity=ObjectIdentity
cpqiScsiInstance=_CpqiScsiInstance_ObjectIdentity((1,3,6,1,4,1,232,169,2,2))
_CpqiScsiInstanceAttributesTable_Object=MibTable
cpqiScsiInstanceAttributesTable=_CpqiScsiInstanceAttributesTable_Object((1,3,6,1,4,1,232,169,2,2,1))
if mibBuilder.loadTexts:cpqiScsiInstanceAttributesTable.setStatus(_A)
_CpqiScsiInstanceAttributesEntry_Object=MibTableRow
cpqiScsiInstanceAttributesEntry=_CpqiScsiInstanceAttributesEntry_Object((1,3,6,1,4,1,232,169,2,2,1,1))
cpqiScsiInstanceAttributesEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cpqiScsiInstanceAttributesEntry.setStatus(_A)
_CpqiScsiInstIndex_Type=Gauge32
_CpqiScsiInstIndex_Object=MibTableColumn
cpqiScsiInstIndex=_CpqiScsiInstIndex_Object((1,3,6,1,4,1,232,169,2,2,1,1,1),_CpqiScsiInstIndex_Type())
cpqiScsiInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstIndex.setStatus(_A)
_CpqiScsiInstDescr_Type=DisplayString
_CpqiScsiInstDescr_Object=MibTableColumn
cpqiScsiInstDescr=_CpqiScsiInstDescr_Object((1,3,6,1,4,1,232,169,2,2,1,1,2),_CpqiScsiInstDescr_Type())
cpqiScsiInstDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstDescr.setStatus(_A)
class _CpqiScsiInstVersionMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqiScsiInstVersionMin_Type.__name__=_C
_CpqiScsiInstVersionMin_Object=MibTableColumn
cpqiScsiInstVersionMin=_CpqiScsiInstVersionMin_Object((1,3,6,1,4,1,232,169,2,2,1,1,3),_CpqiScsiInstVersionMin_Type())
cpqiScsiInstVersionMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstVersionMin.setStatus(_A)
class _CpqiScsiInstVersionMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqiScsiInstVersionMax_Type.__name__=_C
_CpqiScsiInstVersionMax_Object=MibTableColumn
cpqiScsiInstVersionMax=_CpqiScsiInstVersionMax_Object((1,3,6,1,4,1,232,169,2,2,1,1,4),_CpqiScsiInstVersionMax_Type())
cpqiScsiInstVersionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstVersionMax.setStatus(_A)
_CpqiScsiInstVendorID_Type=DisplayString
_CpqiScsiInstVendorID_Object=MibTableColumn
cpqiScsiInstVendorID=_CpqiScsiInstVendorID_Object((1,3,6,1,4,1,232,169,2,2,1,1,5),_CpqiScsiInstVendorID_Type())
cpqiScsiInstVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstVendorID.setStatus(_A)
_CpqiScsiInstVendorVersion_Type=DisplayString
_CpqiScsiInstVendorVersion_Object=MibTableColumn
cpqiScsiInstVendorVersion=_CpqiScsiInstVendorVersion_Object((1,3,6,1,4,1,232,169,2,2,1,1,6),_CpqiScsiInstVendorVersion_Type())
cpqiScsiInstVendorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstVendorVersion.setStatus(_A)
_CpqiScsiInstPortalNumber_Type=Gauge32
_CpqiScsiInstPortalNumber_Object=MibTableColumn
cpqiScsiInstPortalNumber=_CpqiScsiInstPortalNumber_Object((1,3,6,1,4,1,232,169,2,2,1,1,7),_CpqiScsiInstPortalNumber_Type())
cpqiScsiInstPortalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstPortalNumber.setStatus(_A)
_CpqiScsiInstNodeNumber_Type=Gauge32
_CpqiScsiInstNodeNumber_Object=MibTableColumn
cpqiScsiInstNodeNumber=_CpqiScsiInstNodeNumber_Object((1,3,6,1,4,1,232,169,2,2,1,1,8),_CpqiScsiInstNodeNumber_Type())
cpqiScsiInstNodeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstNodeNumber.setStatus(_A)
_CpqiScsiInstSessionNumber_Type=Gauge32
_CpqiScsiInstSessionNumber_Object=MibTableColumn
cpqiScsiInstSessionNumber=_CpqiScsiInstSessionNumber_Object((1,3,6,1,4,1,232,169,2,2,1,1,9),_CpqiScsiInstSessionNumber_Type())
cpqiScsiInstSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstSessionNumber.setStatus(_A)
_CpqiScsiInstSsnFailures_Type=Counter32
_CpqiScsiInstSsnFailures_Object=MibTableColumn
cpqiScsiInstSsnFailures=_CpqiScsiInstSsnFailures_Object((1,3,6,1,4,1,232,169,2,2,1,1,10),_CpqiScsiInstSsnFailures_Type())
cpqiScsiInstSsnFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstSsnFailures.setStatus(_A)
_CpqiScsiInstLastSsnFailureType_Type=ObjectIdentifier
_CpqiScsiInstLastSsnFailureType_Object=MibTableColumn
cpqiScsiInstLastSsnFailureType=_CpqiScsiInstLastSsnFailureType_Object((1,3,6,1,4,1,232,169,2,2,1,1,11),_CpqiScsiInstLastSsnFailureType_Type())
cpqiScsiInstLastSsnFailureType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstLastSsnFailureType.setStatus(_A)
_CpqiScsiInstLastSsnRmtNodeName_Type=DisplayString
_CpqiScsiInstLastSsnRmtNodeName_Object=MibTableColumn
cpqiScsiInstLastSsnRmtNodeName=_CpqiScsiInstLastSsnRmtNodeName_Object((1,3,6,1,4,1,232,169,2,2,1,1,12),_CpqiScsiInstLastSsnRmtNodeName_Type())
cpqiScsiInstLastSsnRmtNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstLastSsnRmtNodeName.setStatus(_A)
_CpqiScsiInstanceSsnErrorStatsTable_Object=MibTable
cpqiScsiInstanceSsnErrorStatsTable=_CpqiScsiInstanceSsnErrorStatsTable_Object((1,3,6,1,4,1,232,169,2,2,2))
if mibBuilder.loadTexts:cpqiScsiInstanceSsnErrorStatsTable.setStatus(_A)
_CpqiScsiInstanceSsnErrorStatsEntry_Object=MibTableRow
cpqiScsiInstanceSsnErrorStatsEntry=_CpqiScsiInstanceSsnErrorStatsEntry_Object((1,3,6,1,4,1,232,169,2,2,2,1))
cpqiScsiInstanceSsnErrorStatsEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cpqiScsiInstanceSsnErrorStatsEntry.setStatus(_A)
_CpqiScsiInstSsnInstIndex_Type=Gauge32
_CpqiScsiInstSsnInstIndex_Object=MibTableColumn
cpqiScsiInstSsnInstIndex=_CpqiScsiInstSsnInstIndex_Object((1,3,6,1,4,1,232,169,2,2,2,1,1),_CpqiScsiInstSsnInstIndex_Type())
cpqiScsiInstSsnInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstSsnInstIndex.setStatus(_A)
_CpqiScsiInstSsnDigestErrors_Type=Counter32
_CpqiScsiInstSsnDigestErrors_Object=MibTableColumn
cpqiScsiInstSsnDigestErrors=_CpqiScsiInstSsnDigestErrors_Object((1,3,6,1,4,1,232,169,2,2,2,1,2),_CpqiScsiInstSsnDigestErrors_Type())
cpqiScsiInstSsnDigestErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstSsnDigestErrors.setStatus(_A)
_CpqiScsiInstSsnCxnTimeoutErrors_Type=Counter32
_CpqiScsiInstSsnCxnTimeoutErrors_Object=MibTableColumn
cpqiScsiInstSsnCxnTimeoutErrors=_CpqiScsiInstSsnCxnTimeoutErrors_Object((1,3,6,1,4,1,232,169,2,2,2,1,3),_CpqiScsiInstSsnCxnTimeoutErrors_Type())
cpqiScsiInstSsnCxnTimeoutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstSsnCxnTimeoutErrors.setStatus(_A)
_CpqiScsiInstSsnFormatErrors_Type=Counter32
_CpqiScsiInstSsnFormatErrors_Object=MibTableColumn
cpqiScsiInstSsnFormatErrors=_CpqiScsiInstSsnFormatErrors_Object((1,3,6,1,4,1,232,169,2,2,2,1,4),_CpqiScsiInstSsnFormatErrors_Type())
cpqiScsiInstSsnFormatErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiInstSsnFormatErrors.setStatus(_A)
_CpqiScsiPortal_ObjectIdentity=ObjectIdentity
cpqiScsiPortal=_CpqiScsiPortal_ObjectIdentity((1,3,6,1,4,1,232,169,2,3))
_CpqiScsiPortalAttributesTable_Object=MibTable
cpqiScsiPortalAttributesTable=_CpqiScsiPortalAttributesTable_Object((1,3,6,1,4,1,232,169,2,3,1))
if mibBuilder.loadTexts:cpqiScsiPortalAttributesTable.setStatus(_A)
_CpqiScsiPortalAttributesEntry_Object=MibTableRow
cpqiScsiPortalAttributesEntry=_CpqiScsiPortalAttributesEntry_Object((1,3,6,1,4,1,232,169,2,3,1,1))
cpqiScsiPortalAttributesEntry.setIndexNames((0,_D,_J),(0,_D,_S))
if mibBuilder.loadTexts:cpqiScsiPortalAttributesEntry.setStatus(_A)
_CpqiScsiPortalInstIndex_Type=Gauge32
_CpqiScsiPortalInstIndex_Object=MibTableColumn
cpqiScsiPortalInstIndex=_CpqiScsiPortalInstIndex_Object((1,3,6,1,4,1,232,169,2,3,1,1,1),_CpqiScsiPortalInstIndex_Type())
cpqiScsiPortalInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiPortalInstIndex.setStatus(_A)
_CpqiScsiPortalIndex_Type=Gauge32
_CpqiScsiPortalIndex_Object=MibTableColumn
cpqiScsiPortalIndex=_CpqiScsiPortalIndex_Object((1,3,6,1,4,1,232,169,2,3,1,1,2),_CpqiScsiPortalIndex_Type())
cpqiScsiPortalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiPortalIndex.setStatus(_A)
class _CpqiScsiPortalRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_c,6)))
_CpqiScsiPortalRowStatus_Type.__name__=_C
_CpqiScsiPortalRowStatus_Object=MibTableColumn
cpqiScsiPortalRowStatus=_CpqiScsiPortalRowStatus_Object((1,3,6,1,4,1,232,169,2,3,1,1,3),_CpqiScsiPortalRowStatus_Type())
cpqiScsiPortalRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalRowStatus.setStatus(_A)
class _CpqiScsiPortalRoles_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_CpqiScsiPortalRoles_Type.__name__=_H
_CpqiScsiPortalRoles_Object=MibTableColumn
cpqiScsiPortalRoles=_CpqiScsiPortalRoles_Object((1,3,6,1,4,1,232,169,2,3,1,1,4),_CpqiScsiPortalRoles_Type())
cpqiScsiPortalRoles.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalRoles.setStatus(_A)
class _CpqiScsiPortalAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,16)))
_CpqiScsiPortalAddrType_Type.__name__=_C
_CpqiScsiPortalAddrType_Object=MibTableColumn
cpqiScsiPortalAddrType=_CpqiScsiPortalAddrType_Object((1,3,6,1,4,1,232,169,2,3,1,1,5),_CpqiScsiPortalAddrType_Type())
cpqiScsiPortalAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalAddrType.setStatus(_A)
class _CpqiScsiPortalAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqiScsiPortalAddr_Type.__name__=_H
_CpqiScsiPortalAddr_Object=MibTableColumn
cpqiScsiPortalAddr=_CpqiScsiPortalAddr_Object((1,3,6,1,4,1,232,169,2,3,1,1,6),_CpqiScsiPortalAddr_Type())
cpqiScsiPortalAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalAddr.setStatus(_A)
class _CpqiScsiPortalProtocol_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('icmp',1),('igmp',2),('ggp',3),('ip',4),('st',5),('tcp',6)))
_CpqiScsiPortalProtocol_Type.__name__=_C
_CpqiScsiPortalProtocol_Object=MibTableColumn
cpqiScsiPortalProtocol=_CpqiScsiPortalProtocol_Object((1,3,6,1,4,1,232,169,2,3,1,1,7),_CpqiScsiPortalProtocol_Type())
cpqiScsiPortalProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalProtocol.setStatus(_A)
class _CpqiScsiPortalMaxRecvDataSegLength_Type(Integer32):defaultValue=8192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiPortalMaxRecvDataSegLength_Type.__name__=_C
_CpqiScsiPortalMaxRecvDataSegLength_Object=MibTableColumn
cpqiScsiPortalMaxRecvDataSegLength=_CpqiScsiPortalMaxRecvDataSegLength_Object((1,3,6,1,4,1,232,169,2,3,1,1,8),_CpqiScsiPortalMaxRecvDataSegLength_Type())
cpqiScsiPortalMaxRecvDataSegLength.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalMaxRecvDataSegLength.setStatus(_A)
class _CpqiScsiPortalPrimaryHdrDigest_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_I,2),(_L,3),(_M,4)))
_CpqiScsiPortalPrimaryHdrDigest_Type.__name__=_C
_CpqiScsiPortalPrimaryHdrDigest_Object=MibTableColumn
cpqiScsiPortalPrimaryHdrDigest=_CpqiScsiPortalPrimaryHdrDigest_Object((1,3,6,1,4,1,232,169,2,3,1,1,9),_CpqiScsiPortalPrimaryHdrDigest_Type())
cpqiScsiPortalPrimaryHdrDigest.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalPrimaryHdrDigest.setStatus(_A)
class _CpqiScsiPortalPrimaryDataDigest_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_I,2),(_L,3),(_M,4)))
_CpqiScsiPortalPrimaryDataDigest_Type.__name__=_C
_CpqiScsiPortalPrimaryDataDigest_Object=MibTableColumn
cpqiScsiPortalPrimaryDataDigest=_CpqiScsiPortalPrimaryDataDigest_Object((1,3,6,1,4,1,232,169,2,3,1,1,10),_CpqiScsiPortalPrimaryDataDigest_Type())
cpqiScsiPortalPrimaryDataDigest.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalPrimaryDataDigest.setStatus(_A)
class _CpqiScsiPortalSecondaryHdrDigest_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_I,2),(_L,3),(_M,4)))
_CpqiScsiPortalSecondaryHdrDigest_Type.__name__=_C
_CpqiScsiPortalSecondaryHdrDigest_Object=MibTableColumn
cpqiScsiPortalSecondaryHdrDigest=_CpqiScsiPortalSecondaryHdrDigest_Object((1,3,6,1,4,1,232,169,2,3,1,1,11),_CpqiScsiPortalSecondaryHdrDigest_Type())
cpqiScsiPortalSecondaryHdrDigest.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalSecondaryHdrDigest.setStatus(_A)
class _CpqiScsiPortalSecondaryDataDigest_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_I,2),(_L,3),(_M,4)))
_CpqiScsiPortalSecondaryDataDigest_Type.__name__=_C
_CpqiScsiPortalSecondaryDataDigest_Object=MibTableColumn
cpqiScsiPortalSecondaryDataDigest=_CpqiScsiPortalSecondaryDataDigest_Object((1,3,6,1,4,1,232,169,2,3,1,1,12),_CpqiScsiPortalSecondaryDataDigest_Type())
cpqiScsiPortalSecondaryDataDigest.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalSecondaryDataDigest.setStatus(_A)
class _CpqiScsiPortalRecvMarker_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiPortalRecvMarker_Type.__name__=_C
_CpqiScsiPortalRecvMarker_Object=MibTableColumn
cpqiScsiPortalRecvMarker=_CpqiScsiPortalRecvMarker_Object((1,3,6,1,4,1,232,169,2,3,1,1,13),_CpqiScsiPortalRecvMarker_Type())
cpqiScsiPortalRecvMarker.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiPortalRecvMarker.setStatus(_A)
_CpqiScsiTargetPortal_ObjectIdentity=ObjectIdentity
cpqiScsiTargetPortal=_CpqiScsiTargetPortal_ObjectIdentity((1,3,6,1,4,1,232,169,2,4))
_CpqiScsiTgtPortalAttributesTable_Object=MibTable
cpqiScsiTgtPortalAttributesTable=_CpqiScsiTgtPortalAttributesTable_Object((1,3,6,1,4,1,232,169,2,4,1))
if mibBuilder.loadTexts:cpqiScsiTgtPortalAttributesTable.setStatus(_A)
_CpqiScsiTgtPortalAttributesEntry_Object=MibTableRow
cpqiScsiTgtPortalAttributesEntry=_CpqiScsiTgtPortalAttributesEntry_Object((1,3,6,1,4,1,232,169,2,4,1,1))
cpqiScsiTgtPortalAttributesEntry.setIndexNames((0,_D,_J),(0,_D,_S))
if mibBuilder.loadTexts:cpqiScsiTgtPortalAttributesEntry.setStatus(_A)
_CpqiScsiTgtPortalInstIndex_Type=Gauge32
_CpqiScsiTgtPortalInstIndex_Object=MibTableColumn
cpqiScsiTgtPortalInstIndex=_CpqiScsiTgtPortalInstIndex_Object((1,3,6,1,4,1,232,169,2,4,1,1,1),_CpqiScsiTgtPortalInstIndex_Type())
cpqiScsiTgtPortalInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtPortalInstIndex.setStatus(_A)
_CpqiScsiTgtPortalPortalIndex_Type=Gauge32
_CpqiScsiTgtPortalPortalIndex_Object=MibTableColumn
cpqiScsiTgtPortalPortalIndex=_CpqiScsiTgtPortalPortalIndex_Object((1,3,6,1,4,1,232,169,2,4,1,1,2),_CpqiScsiTgtPortalPortalIndex_Type())
cpqiScsiTgtPortalPortalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtPortalPortalIndex.setStatus(_A)
_CpqiScsiTgtPortalPort_Type=Gauge32
_CpqiScsiTgtPortalPort_Object=MibTableColumn
cpqiScsiTgtPortalPort=_CpqiScsiTgtPortalPort_Object((1,3,6,1,4,1,232,169,2,4,1,1,3),_CpqiScsiTgtPortalPort_Type())
cpqiScsiTgtPortalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiTgtPortalPort.setStatus(_A)
class _CpqiScsiTgtPortalTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiTgtPortalTag_Type.__name__=_C
_CpqiScsiTgtPortalTag_Object=MibTableColumn
cpqiScsiTgtPortalTag=_CpqiScsiTgtPortalTag_Object((1,3,6,1,4,1,232,169,2,4,1,1,4),_CpqiScsiTgtPortalTag_Type())
cpqiScsiTgtPortalTag.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiTgtPortalTag.setStatus(_A)
_CpqiScsiInitiatorPortal_ObjectIdentity=ObjectIdentity
cpqiScsiInitiatorPortal=_CpqiScsiInitiatorPortal_ObjectIdentity((1,3,6,1,4,1,232,169,2,5))
_CpqiScsiIntrPortalAttributesTable_Object=MibTable
cpqiScsiIntrPortalAttributesTable=_CpqiScsiIntrPortalAttributesTable_Object((1,3,6,1,4,1,232,169,2,5,1))
if mibBuilder.loadTexts:cpqiScsiIntrPortalAttributesTable.setStatus(_A)
_CpqiScsiIntrPortalAttributesEntry_Object=MibTableRow
cpqiScsiIntrPortalAttributesEntry=_CpqiScsiIntrPortalAttributesEntry_Object((1,3,6,1,4,1,232,169,2,5,1,1))
cpqiScsiIntrPortalAttributesEntry.setIndexNames((0,_D,_J),(0,_D,_S))
if mibBuilder.loadTexts:cpqiScsiIntrPortalAttributesEntry.setStatus(_A)
_CpqiScsiIntrPortalInstIndex_Type=Gauge32
_CpqiScsiIntrPortalInstIndex_Object=MibTableColumn
cpqiScsiIntrPortalInstIndex=_CpqiScsiIntrPortalInstIndex_Object((1,3,6,1,4,1,232,169,2,5,1,1,1),_CpqiScsiIntrPortalInstIndex_Type())
cpqiScsiIntrPortalInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrPortalInstIndex.setStatus(_A)
_CpqiScsiIntrPortalPortalIndex_Type=Gauge32
_CpqiScsiIntrPortalPortalIndex_Object=MibTableColumn
cpqiScsiIntrPortalPortalIndex=_CpqiScsiIntrPortalPortalIndex_Object((1,3,6,1,4,1,232,169,2,5,1,1,2),_CpqiScsiIntrPortalPortalIndex_Type())
cpqiScsiIntrPortalPortalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrPortalPortalIndex.setStatus(_A)
class _CpqiScsiIntrPortalTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiIntrPortalTag_Type.__name__=_C
_CpqiScsiIntrPortalTag_Object=MibTableColumn
cpqiScsiIntrPortalTag=_CpqiScsiIntrPortalTag_Object((1,3,6,1,4,1,232,169,2,5,1,1,3),_CpqiScsiIntrPortalTag_Type())
cpqiScsiIntrPortalTag.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiIntrPortalTag.setStatus(_A)
_CpqiScsiNode_ObjectIdentity=ObjectIdentity
cpqiScsiNode=_CpqiScsiNode_ObjectIdentity((1,3,6,1,4,1,232,169,2,6))
_CpqiScsiNodeAttributesTable_Object=MibTable
cpqiScsiNodeAttributesTable=_CpqiScsiNodeAttributesTable_Object((1,3,6,1,4,1,232,169,2,6,1))
if mibBuilder.loadTexts:cpqiScsiNodeAttributesTable.setStatus(_A)
_CpqiScsiNodeAttributesEntry_Object=MibTableRow
cpqiScsiNodeAttributesEntry=_CpqiScsiNodeAttributesEntry_Object((1,3,6,1,4,1,232,169,2,6,1,1))
cpqiScsiNodeAttributesEntry.setIndexNames((0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:cpqiScsiNodeAttributesEntry.setStatus(_A)
_CpqiScsiNodeInstIndex_Type=Gauge32
_CpqiScsiNodeInstIndex_Object=MibTableColumn
cpqiScsiNodeInstIndex=_CpqiScsiNodeInstIndex_Object((1,3,6,1,4,1,232,169,2,6,1,1,1),_CpqiScsiNodeInstIndex_Type())
cpqiScsiNodeInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeInstIndex.setStatus(_A)
_CpqiScsiNodeNodeIndex_Type=Gauge32
_CpqiScsiNodeNodeIndex_Object=MibTableColumn
cpqiScsiNodeNodeIndex=_CpqiScsiNodeNodeIndex_Object((1,3,6,1,4,1,232,169,2,6,1,1,2),_CpqiScsiNodeNodeIndex_Type())
cpqiScsiNodeNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeNodeIndex.setStatus(_A)
_CpqiScsiNodeName_Type=DisplayString
_CpqiScsiNodeName_Object=MibTableColumn
cpqiScsiNodeName=_CpqiScsiNodeName_Object((1,3,6,1,4,1,232,169,2,6,1,1,3),_CpqiScsiNodeName_Type())
cpqiScsiNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeName.setStatus(_A)
_CpqiScsiNodeAlias_Type=DisplayString
_CpqiScsiNodeAlias_Object=MibTableColumn
cpqiScsiNodeAlias=_CpqiScsiNodeAlias_Object((1,3,6,1,4,1,232,169,2,6,1,1,4),_CpqiScsiNodeAlias_Type())
cpqiScsiNodeAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeAlias.setStatus(_A)
class _CpqiScsiNodeRoles_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_CpqiScsiNodeRoles_Type.__name__=_H
_CpqiScsiNodeRoles_Object=MibTableColumn
cpqiScsiNodeRoles=_CpqiScsiNodeRoles_Object((1,3,6,1,4,1,232,169,2,6,1,1,5),_CpqiScsiNodeRoles_Type())
cpqiScsiNodeRoles.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeRoles.setStatus(_A)
_CpqiScsiNodeTransportType_Type=ObjectIdentifier
_CpqiScsiNodeTransportType_Object=MibTableColumn
cpqiScsiNodeTransportType=_CpqiScsiNodeTransportType_Object((1,3,6,1,4,1,232,169,2,6,1,1,6),_CpqiScsiNodeTransportType_Type())
cpqiScsiNodeTransportType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeTransportType.setStatus(_A)
class _CpqiScsiNodeInitialR2T_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiNodeInitialR2T_Type.__name__=_C
_CpqiScsiNodeInitialR2T_Object=MibTableColumn
cpqiScsiNodeInitialR2T=_CpqiScsiNodeInitialR2T_Object((1,3,6,1,4,1,232,169,2,6,1,1,7),_CpqiScsiNodeInitialR2T_Type())
cpqiScsiNodeInitialR2T.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiNodeInitialR2T.setStatus(_A)
class _CpqiScsiNodeImmediateData_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiNodeImmediateData_Type.__name__=_C
_CpqiScsiNodeImmediateData_Object=MibTableColumn
cpqiScsiNodeImmediateData=_CpqiScsiNodeImmediateData_Object((1,3,6,1,4,1,232,169,2,6,1,1,8),_CpqiScsiNodeImmediateData_Type())
cpqiScsiNodeImmediateData.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeImmediateData.setStatus(_A)
class _CpqiScsiNodeMaxOutstandingR2T_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiNodeMaxOutstandingR2T_Type.__name__=_C
_CpqiScsiNodeMaxOutstandingR2T_Object=MibTableColumn
cpqiScsiNodeMaxOutstandingR2T=_CpqiScsiNodeMaxOutstandingR2T_Object((1,3,6,1,4,1,232,169,2,6,1,1,9),_CpqiScsiNodeMaxOutstandingR2T_Type())
cpqiScsiNodeMaxOutstandingR2T.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeMaxOutstandingR2T.setStatus(_A)
class _CpqiScsiNodeFirstBurstLength_Type(Integer32):defaultValue=65536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiNodeFirstBurstLength_Type.__name__=_C
_CpqiScsiNodeFirstBurstLength_Object=MibTableColumn
cpqiScsiNodeFirstBurstLength=_CpqiScsiNodeFirstBurstLength_Object((1,3,6,1,4,1,232,169,2,6,1,1,10),_CpqiScsiNodeFirstBurstLength_Type())
cpqiScsiNodeFirstBurstLength.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeFirstBurstLength.setStatus(_A)
class _CpqiScsiNodeMaxBurstLength_Type(Integer32):defaultValue=262144;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiNodeMaxBurstLength_Type.__name__=_C
_CpqiScsiNodeMaxBurstLength_Object=MibTableColumn
cpqiScsiNodeMaxBurstLength=_CpqiScsiNodeMaxBurstLength_Object((1,3,6,1,4,1,232,169,2,6,1,1,11),_CpqiScsiNodeMaxBurstLength_Type())
cpqiScsiNodeMaxBurstLength.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeMaxBurstLength.setStatus(_A)
class _CpqiScsiNodeMaxConnections_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiNodeMaxConnections_Type.__name__=_C
_CpqiScsiNodeMaxConnections_Object=MibTableColumn
cpqiScsiNodeMaxConnections=_CpqiScsiNodeMaxConnections_Object((1,3,6,1,4,1,232,169,2,6,1,1,12),_CpqiScsiNodeMaxConnections_Type())
cpqiScsiNodeMaxConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeMaxConnections.setStatus(_A)
class _CpqiScsiNodeDataSequenceInOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiNodeDataSequenceInOrder_Type.__name__=_C
_CpqiScsiNodeDataSequenceInOrder_Object=MibTableColumn
cpqiScsiNodeDataSequenceInOrder=_CpqiScsiNodeDataSequenceInOrder_Object((1,3,6,1,4,1,232,169,2,6,1,1,13),_CpqiScsiNodeDataSequenceInOrder_Type())
cpqiScsiNodeDataSequenceInOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeDataSequenceInOrder.setStatus(_A)
class _CpqiScsiNodeDataPDUInOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiNodeDataPDUInOrder_Type.__name__=_C
_CpqiScsiNodeDataPDUInOrder_Object=MibTableColumn
cpqiScsiNodeDataPDUInOrder=_CpqiScsiNodeDataPDUInOrder_Object((1,3,6,1,4,1,232,169,2,6,1,1,14),_CpqiScsiNodeDataPDUInOrder_Type())
cpqiScsiNodeDataPDUInOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeDataPDUInOrder.setStatus(_A)
class _CpqiScsiNodeDefaultTime2Wait_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CpqiScsiNodeDefaultTime2Wait_Type.__name__=_C
_CpqiScsiNodeDefaultTime2Wait_Object=MibTableColumn
cpqiScsiNodeDefaultTime2Wait=_CpqiScsiNodeDefaultTime2Wait_Object((1,3,6,1,4,1,232,169,2,6,1,1,15),_CpqiScsiNodeDefaultTime2Wait_Type())
cpqiScsiNodeDefaultTime2Wait.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeDefaultTime2Wait.setStatus(_A)
class _CpqiScsiNodeDefaultTime2Retain_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CpqiScsiNodeDefaultTime2Retain_Type.__name__=_C
_CpqiScsiNodeDefaultTime2Retain_Object=MibTableColumn
cpqiScsiNodeDefaultTime2Retain=_CpqiScsiNodeDefaultTime2Retain_Object((1,3,6,1,4,1,232,169,2,6,1,1,16),_CpqiScsiNodeDefaultTime2Retain_Type())
cpqiScsiNodeDefaultTime2Retain.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeDefaultTime2Retain.setStatus(_A)
class _CpqiScsiNodeErrorRecoveryLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqiScsiNodeErrorRecoveryLevel_Type.__name__=_C
_CpqiScsiNodeErrorRecoveryLevel_Object=MibTableColumn
cpqiScsiNodeErrorRecoveryLevel=_CpqiScsiNodeErrorRecoveryLevel_Object((1,3,6,1,4,1,232,169,2,6,1,1,17),_CpqiScsiNodeErrorRecoveryLevel_Type())
cpqiScsiNodeErrorRecoveryLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiNodeErrorRecoveryLevel.setStatus(_A)
_CpqiScsiTarget_ObjectIdentity=ObjectIdentity
cpqiScsiTarget=_CpqiScsiTarget_ObjectIdentity((1,3,6,1,4,1,232,169,2,7))
_CpqiScsiTargetAttributesTable_Object=MibTable
cpqiScsiTargetAttributesTable=_CpqiScsiTargetAttributesTable_Object((1,3,6,1,4,1,232,169,2,7,1))
if mibBuilder.loadTexts:cpqiScsiTargetAttributesTable.setStatus(_A)
_CpqiScsiTargetAttributesEntry_Object=MibTableRow
cpqiScsiTargetAttributesEntry=_CpqiScsiTargetAttributesEntry_Object((1,3,6,1,4,1,232,169,2,7,1,1))
cpqiScsiTargetAttributesEntry.setIndexNames((0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:cpqiScsiTargetAttributesEntry.setStatus(_A)
_CpqiScsiTgtInstIndex_Type=Gauge32
_CpqiScsiTgtInstIndex_Object=MibTableColumn
cpqiScsiTgtInstIndex=_CpqiScsiTgtInstIndex_Object((1,3,6,1,4,1,232,169,2,7,1,1,1),_CpqiScsiTgtInstIndex_Type())
cpqiScsiTgtInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtInstIndex.setStatus(_A)
_CpqiScsiTgtNodeIndex_Type=Gauge32
_CpqiScsiTgtNodeIndex_Object=MibTableColumn
cpqiScsiTgtNodeIndex=_CpqiScsiTgtNodeIndex_Object((1,3,6,1,4,1,232,169,2,7,1,1,2),_CpqiScsiTgtNodeIndex_Type())
cpqiScsiTgtNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtNodeIndex.setStatus(_A)
_CpqiScsiTgtLoginFailures_Type=Counter32
_CpqiScsiTgtLoginFailures_Object=MibTableColumn
cpqiScsiTgtLoginFailures=_CpqiScsiTgtLoginFailures_Object((1,3,6,1,4,1,232,169,2,7,1,1,3),_CpqiScsiTgtLoginFailures_Type())
cpqiScsiTgtLoginFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginFailures.setStatus(_A)
_CpqiScsiTgtLastFailureTime_Type=TimeTicks
_CpqiScsiTgtLastFailureTime_Object=MibTableColumn
cpqiScsiTgtLastFailureTime=_CpqiScsiTgtLastFailureTime_Object((1,3,6,1,4,1,232,169,2,7,1,1,4),_CpqiScsiTgtLastFailureTime_Type())
cpqiScsiTgtLastFailureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLastFailureTime.setStatus(_A)
_CpqiScsiTgtLastFailureType_Type=ObjectIdentifier
_CpqiScsiTgtLastFailureType_Object=MibTableColumn
cpqiScsiTgtLastFailureType=_CpqiScsiTgtLastFailureType_Object((1,3,6,1,4,1,232,169,2,7,1,1,5),_CpqiScsiTgtLastFailureType_Type())
cpqiScsiTgtLastFailureType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLastFailureType.setStatus(_A)
_CpqiScsiTgtLastIntrFailureName_Type=DisplayString
_CpqiScsiTgtLastIntrFailureName_Object=MibTableColumn
cpqiScsiTgtLastIntrFailureName=_CpqiScsiTgtLastIntrFailureName_Object((1,3,6,1,4,1,232,169,2,7,1,1,6),_CpqiScsiTgtLastIntrFailureName_Type())
cpqiScsiTgtLastIntrFailureName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLastIntrFailureName.setStatus(_A)
class _CpqiScsiTgtLastIntrFailureAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,16)))
_CpqiScsiTgtLastIntrFailureAddrType_Type.__name__=_C
_CpqiScsiTgtLastIntrFailureAddrType_Object=MibTableColumn
cpqiScsiTgtLastIntrFailureAddrType=_CpqiScsiTgtLastIntrFailureAddrType_Object((1,3,6,1,4,1,232,169,2,7,1,1,7),_CpqiScsiTgtLastIntrFailureAddrType_Type())
cpqiScsiTgtLastIntrFailureAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLastIntrFailureAddrType.setStatus(_A)
class _CpqiScsiTgtLastIntrFailureAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqiScsiTgtLastIntrFailureAddr_Type.__name__=_H
_CpqiScsiTgtLastIntrFailureAddr_Object=MibTableColumn
cpqiScsiTgtLastIntrFailureAddr=_CpqiScsiTgtLastIntrFailureAddr_Object((1,3,6,1,4,1,232,169,2,7,1,1,8),_CpqiScsiTgtLastIntrFailureAddr_Type())
cpqiScsiTgtLastIntrFailureAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLastIntrFailureAddr.setStatus(_A)
_CpqiScsiTargetLoginStatsTable_Object=MibTable
cpqiScsiTargetLoginStatsTable=_CpqiScsiTargetLoginStatsTable_Object((1,3,6,1,4,1,232,169,2,7,2))
if mibBuilder.loadTexts:cpqiScsiTargetLoginStatsTable.setStatus(_A)
_CpqiScsiTargetLoginStatsEntry_Object=MibTableRow
cpqiScsiTargetLoginStatsEntry=_CpqiScsiTargetLoginStatsEntry_Object((1,3,6,1,4,1,232,169,2,7,2,1))
cpqiScsiTargetLoginStatsEntry.setIndexNames((0,_D,_k),(0,_D,_l))
if mibBuilder.loadTexts:cpqiScsiTargetLoginStatsEntry.setStatus(_A)
_CpqiScsiTgtLoginInstIndex_Type=Gauge32
_CpqiScsiTgtLoginInstIndex_Object=MibTableColumn
cpqiScsiTgtLoginInstIndex=_CpqiScsiTgtLoginInstIndex_Object((1,3,6,1,4,1,232,169,2,7,2,1,1),_CpqiScsiTgtLoginInstIndex_Type())
cpqiScsiTgtLoginInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginInstIndex.setStatus(_A)
_CpqiScsiTgtLoginNodeIndex_Type=Gauge32
_CpqiScsiTgtLoginNodeIndex_Object=MibTableColumn
cpqiScsiTgtLoginNodeIndex=_CpqiScsiTgtLoginNodeIndex_Object((1,3,6,1,4,1,232,169,2,7,2,1,2),_CpqiScsiTgtLoginNodeIndex_Type())
cpqiScsiTgtLoginNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginNodeIndex.setStatus(_A)
_CpqiScsiTgtLoginAccepts_Type=Counter32
_CpqiScsiTgtLoginAccepts_Object=MibTableColumn
cpqiScsiTgtLoginAccepts=_CpqiScsiTgtLoginAccepts_Object((1,3,6,1,4,1,232,169,2,7,2,1,3),_CpqiScsiTgtLoginAccepts_Type())
cpqiScsiTgtLoginAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginAccepts.setStatus(_A)
_CpqiScsiTgtLoginOtherFails_Type=Counter32
_CpqiScsiTgtLoginOtherFails_Object=MibTableColumn
cpqiScsiTgtLoginOtherFails=_CpqiScsiTgtLoginOtherFails_Object((1,3,6,1,4,1,232,169,2,7,2,1,4),_CpqiScsiTgtLoginOtherFails_Type())
cpqiScsiTgtLoginOtherFails.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginOtherFails.setStatus(_A)
_CpqiScsiTgtLoginRedirects_Type=Counter32
_CpqiScsiTgtLoginRedirects_Object=MibTableColumn
cpqiScsiTgtLoginRedirects=_CpqiScsiTgtLoginRedirects_Object((1,3,6,1,4,1,232,169,2,7,2,1,5),_CpqiScsiTgtLoginRedirects_Type())
cpqiScsiTgtLoginRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginRedirects.setStatus(_A)
_CpqiScsiTgtLoginAuthorizeFails_Type=Counter32
_CpqiScsiTgtLoginAuthorizeFails_Object=MibTableColumn
cpqiScsiTgtLoginAuthorizeFails=_CpqiScsiTgtLoginAuthorizeFails_Object((1,3,6,1,4,1,232,169,2,7,2,1,6),_CpqiScsiTgtLoginAuthorizeFails_Type())
cpqiScsiTgtLoginAuthorizeFails.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginAuthorizeFails.setStatus(_A)
_CpqiScsiTgtLoginAuthenticateFails_Type=Counter32
_CpqiScsiTgtLoginAuthenticateFails_Object=MibTableColumn
cpqiScsiTgtLoginAuthenticateFails=_CpqiScsiTgtLoginAuthenticateFails_Object((1,3,6,1,4,1,232,169,2,7,2,1,7),_CpqiScsiTgtLoginAuthenticateFails_Type())
cpqiScsiTgtLoginAuthenticateFails.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginAuthenticateFails.setStatus(_A)
_CpqiScsiTgtLoginNegotiateFails_Type=Counter32
_CpqiScsiTgtLoginNegotiateFails_Object=MibTableColumn
cpqiScsiTgtLoginNegotiateFails=_CpqiScsiTgtLoginNegotiateFails_Object((1,3,6,1,4,1,232,169,2,7,2,1,8),_CpqiScsiTgtLoginNegotiateFails_Type())
cpqiScsiTgtLoginNegotiateFails.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLoginNegotiateFails.setStatus(_A)
_CpqiScsiTargetLogoutStatsTable_Object=MibTable
cpqiScsiTargetLogoutStatsTable=_CpqiScsiTargetLogoutStatsTable_Object((1,3,6,1,4,1,232,169,2,7,3))
if mibBuilder.loadTexts:cpqiScsiTargetLogoutStatsTable.setStatus(_A)
_CpqiScsiTargetLogoutStatsEntry_Object=MibTableRow
cpqiScsiTargetLogoutStatsEntry=_CpqiScsiTargetLogoutStatsEntry_Object((1,3,6,1,4,1,232,169,2,7,3,1))
cpqiScsiTargetLogoutStatsEntry.setIndexNames((0,_D,_m),(0,_D,_n))
if mibBuilder.loadTexts:cpqiScsiTargetLogoutStatsEntry.setStatus(_A)
_CpqiScsiTgtLogoutInstIndex_Type=Gauge32
_CpqiScsiTgtLogoutInstIndex_Object=MibTableColumn
cpqiScsiTgtLogoutInstIndex=_CpqiScsiTgtLogoutInstIndex_Object((1,3,6,1,4,1,232,169,2,7,3,1,1),_CpqiScsiTgtLogoutInstIndex_Type())
cpqiScsiTgtLogoutInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLogoutInstIndex.setStatus(_A)
_CpqiScsiTgtLogoutNodeIndex_Type=Gauge32
_CpqiScsiTgtLogoutNodeIndex_Object=MibTableColumn
cpqiScsiTgtLogoutNodeIndex=_CpqiScsiTgtLogoutNodeIndex_Object((1,3,6,1,4,1,232,169,2,7,3,1,2),_CpqiScsiTgtLogoutNodeIndex_Type())
cpqiScsiTgtLogoutNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLogoutNodeIndex.setStatus(_A)
_CpqiScsiTgtLogoutNormals_Type=Counter32
_CpqiScsiTgtLogoutNormals_Object=MibTableColumn
cpqiScsiTgtLogoutNormals=_CpqiScsiTgtLogoutNormals_Object((1,3,6,1,4,1,232,169,2,7,3,1,3),_CpqiScsiTgtLogoutNormals_Type())
cpqiScsiTgtLogoutNormals.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLogoutNormals.setStatus(_A)
_CpqiScsiTgtLogoutOthers_Type=Counter32
_CpqiScsiTgtLogoutOthers_Object=MibTableColumn
cpqiScsiTgtLogoutOthers=_CpqiScsiTgtLogoutOthers_Object((1,3,6,1,4,1,232,169,2,7,3,1,4),_CpqiScsiTgtLogoutOthers_Type())
cpqiScsiTgtLogoutOthers.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtLogoutOthers.setStatus(_A)
_CpqiScsiTgtAuthorization_ObjectIdentity=ObjectIdentity
cpqiScsiTgtAuthorization=_CpqiScsiTgtAuthorization_ObjectIdentity((1,3,6,1,4,1,232,169,2,8))
_CpqiScsiTgtAuthAttributesTable_Object=MibTable
cpqiScsiTgtAuthAttributesTable=_CpqiScsiTgtAuthAttributesTable_Object((1,3,6,1,4,1,232,169,2,8,1))
if mibBuilder.loadTexts:cpqiScsiTgtAuthAttributesTable.setStatus(_A)
_CpqiScsiTgtAuthAttributesEntry_Object=MibTableRow
cpqiScsiTgtAuthAttributesEntry=_CpqiScsiTgtAuthAttributesEntry_Object((1,3,6,1,4,1,232,169,2,8,1,1))
cpqiScsiTgtAuthAttributesEntry.setIndexNames((0,_D,_o),(0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:cpqiScsiTgtAuthAttributesEntry.setStatus(_A)
_CpqiScsiTgtAuthInstIndex_Type=Gauge32
_CpqiScsiTgtAuthInstIndex_Object=MibTableColumn
cpqiScsiTgtAuthInstIndex=_CpqiScsiTgtAuthInstIndex_Object((1,3,6,1,4,1,232,169,2,8,1,1,1),_CpqiScsiTgtAuthInstIndex_Type())
cpqiScsiTgtAuthInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtAuthInstIndex.setStatus(_A)
_CpqiScsiTgtAuthNodeIndex_Type=Gauge32
_CpqiScsiTgtAuthNodeIndex_Object=MibTableColumn
cpqiScsiTgtAuthNodeIndex=_CpqiScsiTgtAuthNodeIndex_Object((1,3,6,1,4,1,232,169,2,8,1,1,2),_CpqiScsiTgtAuthNodeIndex_Type())
cpqiScsiTgtAuthNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtAuthNodeIndex.setStatus(_A)
_CpqiScsiTgtAuthIndex_Type=Gauge32
_CpqiScsiTgtAuthIndex_Object=MibTableColumn
cpqiScsiTgtAuthIndex=_CpqiScsiTgtAuthIndex_Object((1,3,6,1,4,1,232,169,2,8,1,1,3),_CpqiScsiTgtAuthIndex_Type())
cpqiScsiTgtAuthIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiTgtAuthIndex.setStatus(_A)
class _CpqiScsiTgtAuthRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_c,6)))
_CpqiScsiTgtAuthRowStatus_Type.__name__=_C
_CpqiScsiTgtAuthRowStatus_Object=MibTableColumn
cpqiScsiTgtAuthRowStatus=_CpqiScsiTgtAuthRowStatus_Object((1,3,6,1,4,1,232,169,2,8,1,1,4),_CpqiScsiTgtAuthRowStatus_Type())
cpqiScsiTgtAuthRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiTgtAuthRowStatus.setStatus(_A)
_CpqiScsiTgtAuthIdentity_Type=ObjectIdentifier
_CpqiScsiTgtAuthIdentity_Object=MibTableColumn
cpqiScsiTgtAuthIdentity=_CpqiScsiTgtAuthIdentity_Object((1,3,6,1,4,1,232,169,2,8,1,1,5),_CpqiScsiTgtAuthIdentity_Type())
cpqiScsiTgtAuthIdentity.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiTgtAuthIdentity.setStatus(_A)
_CpqiScsiInitiator_ObjectIdentity=ObjectIdentity
cpqiScsiInitiator=_CpqiScsiInitiator_ObjectIdentity((1,3,6,1,4,1,232,169,2,9))
_CpqiScsiInitiatorAttributesTable_Object=MibTable
cpqiScsiInitiatorAttributesTable=_CpqiScsiInitiatorAttributesTable_Object((1,3,6,1,4,1,232,169,2,9,1))
if mibBuilder.loadTexts:cpqiScsiInitiatorAttributesTable.setStatus(_A)
_CpqiScsiInitiatorAttributesEntry_Object=MibTableRow
cpqiScsiInitiatorAttributesEntry=_CpqiScsiInitiatorAttributesEntry_Object((1,3,6,1,4,1,232,169,2,9,1,1))
cpqiScsiInitiatorAttributesEntry.setIndexNames((0,_D,_r),(0,_D,_s))
if mibBuilder.loadTexts:cpqiScsiInitiatorAttributesEntry.setStatus(_A)
_CpqiScsiIntrInstIndex_Type=Gauge32
_CpqiScsiIntrInstIndex_Object=MibTableColumn
cpqiScsiIntrInstIndex=_CpqiScsiIntrInstIndex_Object((1,3,6,1,4,1,232,169,2,9,1,1,1),_CpqiScsiIntrInstIndex_Type())
cpqiScsiIntrInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrInstIndex.setStatus(_A)
_CpqiScsiIntrNodeIndex_Type=Gauge32
_CpqiScsiIntrNodeIndex_Object=MibTableColumn
cpqiScsiIntrNodeIndex=_CpqiScsiIntrNodeIndex_Object((1,3,6,1,4,1,232,169,2,9,1,1,2),_CpqiScsiIntrNodeIndex_Type())
cpqiScsiIntrNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrNodeIndex.setStatus(_A)
_CpqiScsiIntrLoginFailures_Type=Counter32
_CpqiScsiIntrLoginFailures_Object=MibTableColumn
cpqiScsiIntrLoginFailures=_CpqiScsiIntrLoginFailures_Object((1,3,6,1,4,1,232,169,2,9,1,1,3),_CpqiScsiIntrLoginFailures_Type())
cpqiScsiIntrLoginFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginFailures.setStatus(_A)
_CpqiScsiIntrLastFailureTime_Type=TimeTicks
_CpqiScsiIntrLastFailureTime_Object=MibTableColumn
cpqiScsiIntrLastFailureTime=_CpqiScsiIntrLastFailureTime_Object((1,3,6,1,4,1,232,169,2,9,1,1,4),_CpqiScsiIntrLastFailureTime_Type())
cpqiScsiIntrLastFailureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLastFailureTime.setStatus(_A)
_CpqiScsiIntrLastFailureType_Type=ObjectIdentifier
_CpqiScsiIntrLastFailureType_Object=MibTableColumn
cpqiScsiIntrLastFailureType=_CpqiScsiIntrLastFailureType_Object((1,3,6,1,4,1,232,169,2,9,1,1,5),_CpqiScsiIntrLastFailureType_Type())
cpqiScsiIntrLastFailureType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLastFailureType.setStatus(_A)
_CpqiScsiIntrLastTgtFailureName_Type=DisplayString
_CpqiScsiIntrLastTgtFailureName_Object=MibTableColumn
cpqiScsiIntrLastTgtFailureName=_CpqiScsiIntrLastTgtFailureName_Object((1,3,6,1,4,1,232,169,2,9,1,1,6),_CpqiScsiIntrLastTgtFailureName_Type())
cpqiScsiIntrLastTgtFailureName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLastTgtFailureName.setStatus(_A)
class _CpqiScsiIntrLastTgtFailureAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,16)))
_CpqiScsiIntrLastTgtFailureAddrType_Type.__name__=_C
_CpqiScsiIntrLastTgtFailureAddrType_Object=MibTableColumn
cpqiScsiIntrLastTgtFailureAddrType=_CpqiScsiIntrLastTgtFailureAddrType_Object((1,3,6,1,4,1,232,169,2,9,1,1,7),_CpqiScsiIntrLastTgtFailureAddrType_Type())
cpqiScsiIntrLastTgtFailureAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLastTgtFailureAddrType.setStatus(_A)
class _CpqiScsiIntrLastTgtFailureAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqiScsiIntrLastTgtFailureAddr_Type.__name__=_H
_CpqiScsiIntrLastTgtFailureAddr_Object=MibTableColumn
cpqiScsiIntrLastTgtFailureAddr=_CpqiScsiIntrLastTgtFailureAddr_Object((1,3,6,1,4,1,232,169,2,9,1,1,8),_CpqiScsiIntrLastTgtFailureAddr_Type())
cpqiScsiIntrLastTgtFailureAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLastTgtFailureAddr.setStatus(_A)
_CpqiScsiInitiatorLoginStatsTable_Object=MibTable
cpqiScsiInitiatorLoginStatsTable=_CpqiScsiInitiatorLoginStatsTable_Object((1,3,6,1,4,1,232,169,2,9,2))
if mibBuilder.loadTexts:cpqiScsiInitiatorLoginStatsTable.setStatus(_A)
_CpqiScsiInitiatorLoginStatsEntry_Object=MibTableRow
cpqiScsiInitiatorLoginStatsEntry=_CpqiScsiInitiatorLoginStatsEntry_Object((1,3,6,1,4,1,232,169,2,9,2,1))
cpqiScsiInitiatorLoginStatsEntry.setIndexNames((0,_D,_t),(0,_D,_u))
if mibBuilder.loadTexts:cpqiScsiInitiatorLoginStatsEntry.setStatus(_A)
_CpqiScsiIntrLoginInstIndex_Type=Gauge32
_CpqiScsiIntrLoginInstIndex_Object=MibTableColumn
cpqiScsiIntrLoginInstIndex=_CpqiScsiIntrLoginInstIndex_Object((1,3,6,1,4,1,232,169,2,9,2,1,1),_CpqiScsiIntrLoginInstIndex_Type())
cpqiScsiIntrLoginInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginInstIndex.setStatus(_A)
_CpqiScsiIntrLoginNodeIndex_Type=Gauge32
_CpqiScsiIntrLoginNodeIndex_Object=MibTableColumn
cpqiScsiIntrLoginNodeIndex=_CpqiScsiIntrLoginNodeIndex_Object((1,3,6,1,4,1,232,169,2,9,2,1,2),_CpqiScsiIntrLoginNodeIndex_Type())
cpqiScsiIntrLoginNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginNodeIndex.setStatus(_A)
_CpqiScsiIntrLoginAcceptRsps_Type=Counter32
_CpqiScsiIntrLoginAcceptRsps_Object=MibTableColumn
cpqiScsiIntrLoginAcceptRsps=_CpqiScsiIntrLoginAcceptRsps_Object((1,3,6,1,4,1,232,169,2,9,2,1,3),_CpqiScsiIntrLoginAcceptRsps_Type())
cpqiScsiIntrLoginAcceptRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginAcceptRsps.setStatus(_A)
_CpqiScsiIntrLoginOtherFailRsps_Type=Counter32
_CpqiScsiIntrLoginOtherFailRsps_Object=MibTableColumn
cpqiScsiIntrLoginOtherFailRsps=_CpqiScsiIntrLoginOtherFailRsps_Object((1,3,6,1,4,1,232,169,2,9,2,1,4),_CpqiScsiIntrLoginOtherFailRsps_Type())
cpqiScsiIntrLoginOtherFailRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginOtherFailRsps.setStatus(_A)
_CpqiScsiIntrLoginRedirectRsps_Type=Counter32
_CpqiScsiIntrLoginRedirectRsps_Object=MibTableColumn
cpqiScsiIntrLoginRedirectRsps=_CpqiScsiIntrLoginRedirectRsps_Object((1,3,6,1,4,1,232,169,2,9,2,1,5),_CpqiScsiIntrLoginRedirectRsps_Type())
cpqiScsiIntrLoginRedirectRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginRedirectRsps.setStatus(_A)
_CpqiScsiIntrLoginAuthFailRsps_Type=Counter32
_CpqiScsiIntrLoginAuthFailRsps_Object=MibTableColumn
cpqiScsiIntrLoginAuthFailRsps=_CpqiScsiIntrLoginAuthFailRsps_Object((1,3,6,1,4,1,232,169,2,9,2,1,6),_CpqiScsiIntrLoginAuthFailRsps_Type())
cpqiScsiIntrLoginAuthFailRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginAuthFailRsps.setStatus(_A)
_CpqiScsiIntrLoginAuthenticateFails_Type=Counter32
_CpqiScsiIntrLoginAuthenticateFails_Object=MibTableColumn
cpqiScsiIntrLoginAuthenticateFails=_CpqiScsiIntrLoginAuthenticateFails_Object((1,3,6,1,4,1,232,169,2,9,2,1,7),_CpqiScsiIntrLoginAuthenticateFails_Type())
cpqiScsiIntrLoginAuthenticateFails.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginAuthenticateFails.setStatus(_A)
_CpqiScsiIntrLoginNegotiateFails_Type=Counter32
_CpqiScsiIntrLoginNegotiateFails_Object=MibTableColumn
cpqiScsiIntrLoginNegotiateFails=_CpqiScsiIntrLoginNegotiateFails_Object((1,3,6,1,4,1,232,169,2,9,2,1,8),_CpqiScsiIntrLoginNegotiateFails_Type())
cpqiScsiIntrLoginNegotiateFails.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLoginNegotiateFails.setStatus(_A)
_CpqiScsiInitiatorLogoutStatsTable_Object=MibTable
cpqiScsiInitiatorLogoutStatsTable=_CpqiScsiInitiatorLogoutStatsTable_Object((1,3,6,1,4,1,232,169,2,9,3))
if mibBuilder.loadTexts:cpqiScsiInitiatorLogoutStatsTable.setStatus(_A)
_CpqiScsiInitiatorLogoutStatsEntry_Object=MibTableRow
cpqiScsiInitiatorLogoutStatsEntry=_CpqiScsiInitiatorLogoutStatsEntry_Object((1,3,6,1,4,1,232,169,2,9,3,1))
cpqiScsiInitiatorLogoutStatsEntry.setIndexNames((0,_D,_v),(0,_D,_w))
if mibBuilder.loadTexts:cpqiScsiInitiatorLogoutStatsEntry.setStatus(_A)
_CpqiScsiIntrLogoutInstIndex_Type=Gauge32
_CpqiScsiIntrLogoutInstIndex_Object=MibTableColumn
cpqiScsiIntrLogoutInstIndex=_CpqiScsiIntrLogoutInstIndex_Object((1,3,6,1,4,1,232,169,2,9,3,1,1),_CpqiScsiIntrLogoutInstIndex_Type())
cpqiScsiIntrLogoutInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLogoutInstIndex.setStatus(_A)
_CpqiScsiIntrLogoutNodeIndex_Type=Gauge32
_CpqiScsiIntrLogoutNodeIndex_Object=MibTableColumn
cpqiScsiIntrLogoutNodeIndex=_CpqiScsiIntrLogoutNodeIndex_Object((1,3,6,1,4,1,232,169,2,9,3,1,2),_CpqiScsiIntrLogoutNodeIndex_Type())
cpqiScsiIntrLogoutNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLogoutNodeIndex.setStatus(_A)
_CpqiScsiIntrLogoutNormals_Type=Counter32
_CpqiScsiIntrLogoutNormals_Object=MibTableColumn
cpqiScsiIntrLogoutNormals=_CpqiScsiIntrLogoutNormals_Object((1,3,6,1,4,1,232,169,2,9,3,1,3),_CpqiScsiIntrLogoutNormals_Type())
cpqiScsiIntrLogoutNormals.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLogoutNormals.setStatus(_A)
_CpqiScsiIntrLogoutOthers_Type=Counter32
_CpqiScsiIntrLogoutOthers_Object=MibTableColumn
cpqiScsiIntrLogoutOthers=_CpqiScsiIntrLogoutOthers_Object((1,3,6,1,4,1,232,169,2,9,3,1,4),_CpqiScsiIntrLogoutOthers_Type())
cpqiScsiIntrLogoutOthers.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrLogoutOthers.setStatus(_A)
_CpqiScsiIntrAuthorization_ObjectIdentity=ObjectIdentity
cpqiScsiIntrAuthorization=_CpqiScsiIntrAuthorization_ObjectIdentity((1,3,6,1,4,1,232,169,2,10))
_CpqiScsiIntrAuthAttributesTable_Object=MibTable
cpqiScsiIntrAuthAttributesTable=_CpqiScsiIntrAuthAttributesTable_Object((1,3,6,1,4,1,232,169,2,10,1))
if mibBuilder.loadTexts:cpqiScsiIntrAuthAttributesTable.setStatus(_A)
_CpqiScsiIntrAuthAttributesEntry_Object=MibTableRow
cpqiScsiIntrAuthAttributesEntry=_CpqiScsiIntrAuthAttributesEntry_Object((1,3,6,1,4,1,232,169,2,10,1,1))
cpqiScsiIntrAuthAttributesEntry.setIndexNames((0,_D,_x),(0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:cpqiScsiIntrAuthAttributesEntry.setStatus(_A)
_CpqiScsiIntrAuthInstIndex_Type=Gauge32
_CpqiScsiIntrAuthInstIndex_Object=MibTableColumn
cpqiScsiIntrAuthInstIndex=_CpqiScsiIntrAuthInstIndex_Object((1,3,6,1,4,1,232,169,2,10,1,1,1),_CpqiScsiIntrAuthInstIndex_Type())
cpqiScsiIntrAuthInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrAuthInstIndex.setStatus(_A)
_CpqiScsiIntrAuthNodeIndex_Type=Gauge32
_CpqiScsiIntrAuthNodeIndex_Object=MibTableColumn
cpqiScsiIntrAuthNodeIndex=_CpqiScsiIntrAuthNodeIndex_Object((1,3,6,1,4,1,232,169,2,10,1,1,2),_CpqiScsiIntrAuthNodeIndex_Type())
cpqiScsiIntrAuthNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrAuthNodeIndex.setStatus(_A)
_CpqiScsiIntrAuthIndex_Type=Gauge32
_CpqiScsiIntrAuthIndex_Object=MibTableColumn
cpqiScsiIntrAuthIndex=_CpqiScsiIntrAuthIndex_Object((1,3,6,1,4,1,232,169,2,10,1,1,3),_CpqiScsiIntrAuthIndex_Type())
cpqiScsiIntrAuthIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrAuthIndex.setStatus(_A)
class _CpqiScsiIntrAuthRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),(_c,6)))
_CpqiScsiIntrAuthRowStatus_Type.__name__=_C
_CpqiScsiIntrAuthRowStatus_Object=MibTableColumn
cpqiScsiIntrAuthRowStatus=_CpqiScsiIntrAuthRowStatus_Object((1,3,6,1,4,1,232,169,2,10,1,1,4),_CpqiScsiIntrAuthRowStatus_Type())
cpqiScsiIntrAuthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrAuthRowStatus.setStatus(_A)
_CpqiScsiIntrAuthIdentity_Type=ObjectIdentifier
_CpqiScsiIntrAuthIdentity_Object=MibTableColumn
cpqiScsiIntrAuthIdentity=_CpqiScsiIntrAuthIdentity_Object((1,3,6,1,4,1,232,169,2,10,1,1,5),_CpqiScsiIntrAuthIdentity_Type())
cpqiScsiIntrAuthIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiIntrAuthIdentity.setStatus(_A)
_CpqiScsiSession_ObjectIdentity=ObjectIdentity
cpqiScsiSession=_CpqiScsiSession_ObjectIdentity((1,3,6,1,4,1,232,169,2,11))
_CpqiScsiSessionAttributesTable_Object=MibTable
cpqiScsiSessionAttributesTable=_CpqiScsiSessionAttributesTable_Object((1,3,6,1,4,1,232,169,2,11,1))
if mibBuilder.loadTexts:cpqiScsiSessionAttributesTable.setStatus(_A)
_CpqiScsiSessionAttributesEntry_Object=MibTableRow
cpqiScsiSessionAttributesEntry=_CpqiScsiSessionAttributesEntry_Object((1,3,6,1,4,1,232,169,2,11,1,1))
cpqiScsiSessionAttributesEntry.setIndexNames((0,_D,_A0),(0,_D,_A1),(0,_D,_A2))
if mibBuilder.loadTexts:cpqiScsiSessionAttributesEntry.setStatus(_A)
_CpqiScsiSsnInstIndex_Type=Gauge32
_CpqiScsiSsnInstIndex_Object=MibTableColumn
cpqiScsiSsnInstIndex=_CpqiScsiSsnInstIndex_Object((1,3,6,1,4,1,232,169,2,11,1,1,1),_CpqiScsiSsnInstIndex_Type())
cpqiScsiSsnInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnInstIndex.setStatus(_A)
_CpqiScsiSsnNodeIndex_Type=Gauge32
_CpqiScsiSsnNodeIndex_Object=MibTableColumn
cpqiScsiSsnNodeIndex=_CpqiScsiSsnNodeIndex_Object((1,3,6,1,4,1,232,169,2,11,1,1,2),_CpqiScsiSsnNodeIndex_Type())
cpqiScsiSsnNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnNodeIndex.setStatus(_A)
_CpqiScsiSsnIndex_Type=Gauge32
_CpqiScsiSsnIndex_Object=MibTableColumn
cpqiScsiSsnIndex=_CpqiScsiSsnIndex_Object((1,3,6,1,4,1,232,169,2,11,1,1,3),_CpqiScsiSsnIndex_Type())
cpqiScsiSsnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnIndex.setStatus(_A)
class _CpqiScsiSsnDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inboundSession',1),('outboundSession',2)))
_CpqiScsiSsnDirection_Type.__name__=_C
_CpqiScsiSsnDirection_Object=MibTableColumn
cpqiScsiSsnDirection=_CpqiScsiSsnDirection_Object((1,3,6,1,4,1,232,169,2,11,1,1,4),_CpqiScsiSsnDirection_Type())
cpqiScsiSsnDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnDirection.setStatus(_A)
_CpqiScsiSsnInitiatorName_Type=DisplayString
_CpqiScsiSsnInitiatorName_Object=MibTableColumn
cpqiScsiSsnInitiatorName=_CpqiScsiSsnInitiatorName_Object((1,3,6,1,4,1,232,169,2,11,1,1,5),_CpqiScsiSsnInitiatorName_Type())
cpqiScsiSsnInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnInitiatorName.setStatus(_A)
_CpqiScsiSsnTargetName_Type=DisplayString
_CpqiScsiSsnTargetName_Object=MibTableColumn
cpqiScsiSsnTargetName=_CpqiScsiSsnTargetName_Object((1,3,6,1,4,1,232,169,2,11,1,1,6),_CpqiScsiSsnTargetName_Type())
cpqiScsiSsnTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnTargetName.setStatus(_A)
class _CpqiScsiSsnTSIH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiSsnTSIH_Type.__name__=_C
_CpqiScsiSsnTSIH_Object=MibTableColumn
cpqiScsiSsnTSIH=_CpqiScsiSsnTSIH_Object((1,3,6,1,4,1,232,169,2,11,1,1,7),_CpqiScsiSsnTSIH_Type())
cpqiScsiSsnTSIH.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnTSIH.setStatus(_A)
class _CpqiScsiSsnISID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CpqiScsiSsnISID_Type.__name__=_H
_CpqiScsiSsnISID_Object=MibTableColumn
cpqiScsiSsnISID=_CpqiScsiSsnISID_Object((1,3,6,1,4,1,232,169,2,11,1,1,8),_CpqiScsiSsnISID_Type())
cpqiScsiSsnISID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnISID.setStatus(_A)
_CpqiScsiSsnInitiatorAlias_Type=DisplayString
_CpqiScsiSsnInitiatorAlias_Object=MibTableColumn
cpqiScsiSsnInitiatorAlias=_CpqiScsiSsnInitiatorAlias_Object((1,3,6,1,4,1,232,169,2,11,1,1,9),_CpqiScsiSsnInitiatorAlias_Type())
cpqiScsiSsnInitiatorAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnInitiatorAlias.setStatus(_A)
_CpqiScsiSsnTargetAlias_Type=DisplayString
_CpqiScsiSsnTargetAlias_Object=MibTableColumn
cpqiScsiSsnTargetAlias=_CpqiScsiSsnTargetAlias_Object((1,3,6,1,4,1,232,169,2,11,1,1,10),_CpqiScsiSsnTargetAlias_Type())
cpqiScsiSsnTargetAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnTargetAlias.setStatus(_A)
class _CpqiScsiSsnInitialR2T_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiSsnInitialR2T_Type.__name__=_C
_CpqiScsiSsnInitialR2T_Object=MibTableColumn
cpqiScsiSsnInitialR2T=_CpqiScsiSsnInitialR2T_Object((1,3,6,1,4,1,232,169,2,11,1,1,11),_CpqiScsiSsnInitialR2T_Type())
cpqiScsiSsnInitialR2T.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnInitialR2T.setStatus(_A)
class _CpqiScsiSsnImmediateData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiSsnImmediateData_Type.__name__=_C
_CpqiScsiSsnImmediateData_Object=MibTableColumn
cpqiScsiSsnImmediateData=_CpqiScsiSsnImmediateData_Object((1,3,6,1,4,1,232,169,2,11,1,1,12),_CpqiScsiSsnImmediateData_Type())
cpqiScsiSsnImmediateData.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnImmediateData.setStatus(_A)
class _CpqiScsiSsnType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normalSession',1),('discoverySession',2)))
_CpqiScsiSsnType_Type.__name__=_C
_CpqiScsiSsnType_Object=MibTableColumn
cpqiScsiSsnType=_CpqiScsiSsnType_Object((1,3,6,1,4,1,232,169,2,11,1,1,13),_CpqiScsiSsnType_Type())
cpqiScsiSsnType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnType.setStatus(_A)
class _CpqiScsiSsnMaxOutstandingR2T_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiSsnMaxOutstandingR2T_Type.__name__=_C
_CpqiScsiSsnMaxOutstandingR2T_Object=MibTableColumn
cpqiScsiSsnMaxOutstandingR2T=_CpqiScsiSsnMaxOutstandingR2T_Object((1,3,6,1,4,1,232,169,2,11,1,1,14),_CpqiScsiSsnMaxOutstandingR2T_Type())
cpqiScsiSsnMaxOutstandingR2T.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnMaxOutstandingR2T.setStatus(_A)
class _CpqiScsiSsnFirstBurstLength_Type(Integer32):defaultValue=65536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiSsnFirstBurstLength_Type.__name__=_C
_CpqiScsiSsnFirstBurstLength_Object=MibTableColumn
cpqiScsiSsnFirstBurstLength=_CpqiScsiSsnFirstBurstLength_Object((1,3,6,1,4,1,232,169,2,11,1,1,15),_CpqiScsiSsnFirstBurstLength_Type())
cpqiScsiSsnFirstBurstLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnFirstBurstLength.setStatus(_A)
class _CpqiScsiSsnMaxBurstLength_Type(Integer32):defaultValue=262144;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiSsnMaxBurstLength_Type.__name__=_C
_CpqiScsiSsnMaxBurstLength_Object=MibTableColumn
cpqiScsiSsnMaxBurstLength=_CpqiScsiSsnMaxBurstLength_Object((1,3,6,1,4,1,232,169,2,11,1,1,16),_CpqiScsiSsnMaxBurstLength_Type())
cpqiScsiSsnMaxBurstLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnMaxBurstLength.setStatus(_A)
_CpqiScsiSsnConnectionNumber_Type=Gauge32
_CpqiScsiSsnConnectionNumber_Object=MibTableColumn
cpqiScsiSsnConnectionNumber=_CpqiScsiSsnConnectionNumber_Object((1,3,6,1,4,1,232,169,2,11,1,1,17),_CpqiScsiSsnConnectionNumber_Type())
cpqiScsiSsnConnectionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnConnectionNumber.setStatus(_A)
_CpqiScsiSsnAuthIdentity_Type=ObjectIdentifier
_CpqiScsiSsnAuthIdentity_Object=MibTableColumn
cpqiScsiSsnAuthIdentity=_CpqiScsiSsnAuthIdentity_Object((1,3,6,1,4,1,232,169,2,11,1,1,18),_CpqiScsiSsnAuthIdentity_Type())
cpqiScsiSsnAuthIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnAuthIdentity.setStatus(_A)
class _CpqiScsiSsnDataSequenceInOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiSsnDataSequenceInOrder_Type.__name__=_C
_CpqiScsiSsnDataSequenceInOrder_Object=MibTableColumn
cpqiScsiSsnDataSequenceInOrder=_CpqiScsiSsnDataSequenceInOrder_Object((1,3,6,1,4,1,232,169,2,11,1,1,19),_CpqiScsiSsnDataSequenceInOrder_Type())
cpqiScsiSsnDataSequenceInOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnDataSequenceInOrder.setStatus(_A)
class _CpqiScsiSsnDataPDUInOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiSsnDataPDUInOrder_Type.__name__=_C
_CpqiScsiSsnDataPDUInOrder_Object=MibTableColumn
cpqiScsiSsnDataPDUInOrder=_CpqiScsiSsnDataPDUInOrder_Object((1,3,6,1,4,1,232,169,2,11,1,1,20),_CpqiScsiSsnDataPDUInOrder_Type())
cpqiScsiSsnDataPDUInOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnDataPDUInOrder.setStatus(_A)
class _CpqiScsiSsnErrorRecoveryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqiScsiSsnErrorRecoveryLevel_Type.__name__=_C
_CpqiScsiSsnErrorRecoveryLevel_Object=MibTableColumn
cpqiScsiSsnErrorRecoveryLevel=_CpqiScsiSsnErrorRecoveryLevel_Object((1,3,6,1,4,1,232,169,2,11,1,1,21),_CpqiScsiSsnErrorRecoveryLevel_Type())
cpqiScsiSsnErrorRecoveryLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnErrorRecoveryLevel.setStatus(_A)
class _CpqiScsiSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqiScsiSessionId_Type.__name__=_f
_CpqiScsiSessionId_Object=MibTableColumn
cpqiScsiSessionId=_CpqiScsiSessionId_Object((1,3,6,1,4,1,232,169,2,11,1,1,22),_CpqiScsiSessionId_Type())
cpqiScsiSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSessionId.setStatus(_A)
_CpqiScsiSessionStatsTable_Object=MibTable
cpqiScsiSessionStatsTable=_CpqiScsiSessionStatsTable_Object((1,3,6,1,4,1,232,169,2,11,2))
if mibBuilder.loadTexts:cpqiScsiSessionStatsTable.setStatus(_A)
_CpqiScsiSessionStatsEntry_Object=MibTableRow
cpqiScsiSessionStatsEntry=_CpqiScsiSessionStatsEntry_Object((1,3,6,1,4,1,232,169,2,11,2,1))
cpqiScsiSessionStatsEntry.setIndexNames((0,_D,_A3),(0,_D,_A4),(0,_D,_A5))
if mibBuilder.loadTexts:cpqiScsiSessionStatsEntry.setStatus(_A)
_CpqiScsiSsnStatInstIndex_Type=Gauge32
_CpqiScsiSsnStatInstIndex_Object=MibTableColumn
cpqiScsiSsnStatInstIndex=_CpqiScsiSsnStatInstIndex_Object((1,3,6,1,4,1,232,169,2,11,2,1,1),_CpqiScsiSsnStatInstIndex_Type())
cpqiScsiSsnStatInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnStatInstIndex.setStatus(_A)
_CpqiScsiSsnStatNodeIndex_Type=Gauge32
_CpqiScsiSsnStatNodeIndex_Object=MibTableColumn
cpqiScsiSsnStatNodeIndex=_CpqiScsiSsnStatNodeIndex_Object((1,3,6,1,4,1,232,169,2,11,2,1,2),_CpqiScsiSsnStatNodeIndex_Type())
cpqiScsiSsnStatNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnStatNodeIndex.setStatus(_A)
_CpqiScsiSsnSessionIndex_Type=Gauge32
_CpqiScsiSsnSessionIndex_Object=MibTableColumn
cpqiScsiSsnSessionIndex=_CpqiScsiSsnSessionIndex_Object((1,3,6,1,4,1,232,169,2,11,2,1,3),_CpqiScsiSsnSessionIndex_Type())
cpqiScsiSsnSessionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnSessionIndex.setStatus(_A)
_CpqiScsiSsnCmdPDUs_Type=Counter32
_CpqiScsiSsnCmdPDUs_Object=MibTableColumn
cpqiScsiSsnCmdPDUs=_CpqiScsiSsnCmdPDUs_Object((1,3,6,1,4,1,232,169,2,11,2,1,4),_CpqiScsiSsnCmdPDUs_Type())
cpqiScsiSsnCmdPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnCmdPDUs.setStatus(_A)
_CpqiScsiSsnRspPDUs_Type=Counter32
_CpqiScsiSsnRspPDUs_Object=MibTableColumn
cpqiScsiSsnRspPDUs=_CpqiScsiSsnRspPDUs_Object((1,3,6,1,4,1,232,169,2,11,2,1,5),_CpqiScsiSsnRspPDUs_Type())
cpqiScsiSsnRspPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnRspPDUs.setStatus(_A)
_CpqiScsiSsnTxDataOctets_Type=Counter32
_CpqiScsiSsnTxDataOctets_Object=MibTableColumn
cpqiScsiSsnTxDataOctets=_CpqiScsiSsnTxDataOctets_Object((1,3,6,1,4,1,232,169,2,11,2,1,6),_CpqiScsiSsnTxDataOctets_Type())
cpqiScsiSsnTxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnTxDataOctets.setStatus(_A)
_CpqiScsiSsnRxDataOctets_Type=Counter32
_CpqiScsiSsnRxDataOctets_Object=MibTableColumn
cpqiScsiSsnRxDataOctets=_CpqiScsiSsnRxDataOctets_Object((1,3,6,1,4,1,232,169,2,11,2,1,7),_CpqiScsiSsnRxDataOctets_Type())
cpqiScsiSsnRxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnRxDataOctets.setStatus(_A)
_CpqiScsiSsnLCTxDataOctets_Type=Counter32
_CpqiScsiSsnLCTxDataOctets_Object=MibTableColumn
cpqiScsiSsnLCTxDataOctets=_CpqiScsiSsnLCTxDataOctets_Object((1,3,6,1,4,1,232,169,2,11,2,1,8),_CpqiScsiSsnLCTxDataOctets_Type())
cpqiScsiSsnLCTxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnLCTxDataOctets.setStatus(_A)
_CpqiScsiSsnLCRxDataOctets_Type=Counter32
_CpqiScsiSsnLCRxDataOctets_Object=MibTableColumn
cpqiScsiSsnLCRxDataOctets=_CpqiScsiSsnLCRxDataOctets_Object((1,3,6,1,4,1,232,169,2,11,2,1,9),_CpqiScsiSsnLCRxDataOctets_Type())
cpqiScsiSsnLCRxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnLCRxDataOctets.setStatus(_A)
_CpqiScsiSessionCxnErrorStatsTable_Object=MibTable
cpqiScsiSessionCxnErrorStatsTable=_CpqiScsiSessionCxnErrorStatsTable_Object((1,3,6,1,4,1,232,169,2,11,3))
if mibBuilder.loadTexts:cpqiScsiSessionCxnErrorStatsTable.setStatus(_A)
_CpqiScsiSessionCxnErrorStatsEntry_Object=MibTableRow
cpqiScsiSessionCxnErrorStatsEntry=_CpqiScsiSessionCxnErrorStatsEntry_Object((1,3,6,1,4,1,232,169,2,11,3,1))
cpqiScsiSessionCxnErrorStatsEntry.setIndexNames((0,_D,_A6),(0,_D,_A7),(0,_D,_A8))
if mibBuilder.loadTexts:cpqiScsiSessionCxnErrorStatsEntry.setStatus(_A)
_CpqiScsiSsnCxnInstIndex_Type=Gauge32
_CpqiScsiSsnCxnInstIndex_Object=MibTableColumn
cpqiScsiSsnCxnInstIndex=_CpqiScsiSsnCxnInstIndex_Object((1,3,6,1,4,1,232,169,2,11,3,1,1),_CpqiScsiSsnCxnInstIndex_Type())
cpqiScsiSsnCxnInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnCxnInstIndex.setStatus(_A)
_CpqiScsiSsnCxnNodeIndex_Type=Gauge32
_CpqiScsiSsnCxnNodeIndex_Object=MibTableColumn
cpqiScsiSsnCxnNodeIndex=_CpqiScsiSsnCxnNodeIndex_Object((1,3,6,1,4,1,232,169,2,11,3,1,2),_CpqiScsiSsnCxnNodeIndex_Type())
cpqiScsiSsnCxnNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnCxnNodeIndex.setStatus(_A)
_CpqiScsiSsnCxnIndex_Type=Gauge32
_CpqiScsiSsnCxnIndex_Object=MibTableColumn
cpqiScsiSsnCxnIndex=_CpqiScsiSsnCxnIndex_Object((1,3,6,1,4,1,232,169,2,11,3,1,3),_CpqiScsiSsnCxnIndex_Type())
cpqiScsiSsnCxnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnCxnIndex.setStatus(_A)
_CpqiScsiSsnCxnDigestErrors_Type=Counter32
_CpqiScsiSsnCxnDigestErrors_Object=MibTableColumn
cpqiScsiSsnCxnDigestErrors=_CpqiScsiSsnCxnDigestErrors_Object((1,3,6,1,4,1,232,169,2,11,3,1,4),_CpqiScsiSsnCxnDigestErrors_Type())
cpqiScsiSsnCxnDigestErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnCxnDigestErrors.setStatus(_A)
_CpqiScsiSsnCxnTimeoutErrors_Type=Counter32
_CpqiScsiSsnCxnTimeoutErrors_Object=MibTableColumn
cpqiScsiSsnCxnTimeoutErrors=_CpqiScsiSsnCxnTimeoutErrors_Object((1,3,6,1,4,1,232,169,2,11,3,1,5),_CpqiScsiSsnCxnTimeoutErrors_Type())
cpqiScsiSsnCxnTimeoutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiSsnCxnTimeoutErrors.setStatus(_A)
_CpqiScsiConnection_ObjectIdentity=ObjectIdentity
cpqiScsiConnection=_CpqiScsiConnection_ObjectIdentity((1,3,6,1,4,1,232,169,2,12))
_CpqiScsiConnectionAttributesTable_Object=MibTable
cpqiScsiConnectionAttributesTable=_CpqiScsiConnectionAttributesTable_Object((1,3,6,1,4,1,232,169,2,12,1))
if mibBuilder.loadTexts:cpqiScsiConnectionAttributesTable.setStatus(_A)
_CpqiScsiConnectionAttributesEntry_Object=MibTableRow
cpqiScsiConnectionAttributesEntry=_CpqiScsiConnectionAttributesEntry_Object((1,3,6,1,4,1,232,169,2,12,1,1))
cpqiScsiConnectionAttributesEntry.setIndexNames((0,_D,_A9),(0,_D,_AA),(0,_D,_AB),(0,_D,_AC))
if mibBuilder.loadTexts:cpqiScsiConnectionAttributesEntry.setStatus(_A)
_CpqiScsiCxnAttrInstIndex_Type=Gauge32
_CpqiScsiCxnAttrInstIndex_Object=MibTableColumn
cpqiScsiCxnAttrInstIndex=_CpqiScsiCxnAttrInstIndex_Object((1,3,6,1,4,1,232,169,2,12,1,1,1),_CpqiScsiCxnAttrInstIndex_Type())
cpqiScsiCxnAttrInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrInstIndex.setStatus(_A)
_CpqiScsiCxnAttrNodeIndex_Type=Gauge32
_CpqiScsiCxnAttrNodeIndex_Object=MibTableColumn
cpqiScsiCxnAttrNodeIndex=_CpqiScsiCxnAttrNodeIndex_Object((1,3,6,1,4,1,232,169,2,12,1,1,2),_CpqiScsiCxnAttrNodeIndex_Type())
cpqiScsiCxnAttrNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrNodeIndex.setStatus(_A)
_CpqiScsiCxnAttrSessionIndex_Type=Gauge32
_CpqiScsiCxnAttrSessionIndex_Object=MibTableColumn
cpqiScsiCxnAttrSessionIndex=_CpqiScsiCxnAttrSessionIndex_Object((1,3,6,1,4,1,232,169,2,12,1,1,3),_CpqiScsiCxnAttrSessionIndex_Type())
cpqiScsiCxnAttrSessionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrSessionIndex.setStatus(_A)
_CpqiScsiCxnAttrIndex_Type=Gauge32
_CpqiScsiCxnAttrIndex_Object=MibTableColumn
cpqiScsiCxnAttrIndex=_CpqiScsiCxnAttrIndex_Object((1,3,6,1,4,1,232,169,2,12,1,1,4),_CpqiScsiCxnAttrIndex_Type())
cpqiScsiCxnAttrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrIndex.setStatus(_A)
class _CpqiScsiCxnAttrCid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqiScsiCxnAttrCid_Type.__name__=_C
_CpqiScsiCxnAttrCid_Object=MibTableColumn
cpqiScsiCxnAttrCid=_CpqiScsiCxnAttrCid_Object((1,3,6,1,4,1,232,169,2,12,1,1,5),_CpqiScsiCxnAttrCid_Type())
cpqiScsiCxnAttrCid.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrCid.setStatus(_A)
class _CpqiScsiCxnAttrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('login',1),('full',2),('logout',3)))
_CpqiScsiCxnAttrState_Type.__name__=_C
_CpqiScsiCxnAttrState_Object=MibTableColumn
cpqiScsiCxnAttrState=_CpqiScsiCxnAttrState_Object((1,3,6,1,4,1,232,169,2,12,1,1,6),_CpqiScsiCxnAttrState_Type())
cpqiScsiCxnAttrState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrState.setStatus(_A)
class _CpqiScsiCxnAttrLocalAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,16)))
_CpqiScsiCxnAttrLocalAddrType_Type.__name__=_C
_CpqiScsiCxnAttrLocalAddrType_Object=MibTableColumn
cpqiScsiCxnAttrLocalAddrType=_CpqiScsiCxnAttrLocalAddrType_Object((1,3,6,1,4,1,232,169,2,12,1,1,7),_CpqiScsiCxnAttrLocalAddrType_Type())
cpqiScsiCxnAttrLocalAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrLocalAddrType.setStatus(_A)
class _CpqiScsiCxnAttrLocalAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqiScsiCxnAttrLocalAddr_Type.__name__=_H
_CpqiScsiCxnAttrLocalAddr_Object=MibTableColumn
cpqiScsiCxnAttrLocalAddr=_CpqiScsiCxnAttrLocalAddr_Object((1,3,6,1,4,1,232,169,2,12,1,1,8),_CpqiScsiCxnAttrLocalAddr_Type())
cpqiScsiCxnAttrLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrLocalAddr.setStatus(_A)
class _CpqiScsiCxnAttrProtocol_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('icmp',1),('igmp',2),('ggp',3),('ip',4),('st',5),('tcp',6)))
_CpqiScsiCxnAttrProtocol_Type.__name__=_C
_CpqiScsiCxnAttrProtocol_Object=MibTableColumn
cpqiScsiCxnAttrProtocol=_CpqiScsiCxnAttrProtocol_Object((1,3,6,1,4,1,232,169,2,12,1,1,9),_CpqiScsiCxnAttrProtocol_Type())
cpqiScsiCxnAttrProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqiScsiCxnAttrProtocol.setStatus(_A)
_CpqiScsiCxnAttrLocalPort_Type=Gauge32
_CpqiScsiCxnAttrLocalPort_Object=MibTableColumn
cpqiScsiCxnAttrLocalPort=_CpqiScsiCxnAttrLocalPort_Object((1,3,6,1,4,1,232,169,2,12,1,1,10),_CpqiScsiCxnAttrLocalPort_Type())
cpqiScsiCxnAttrLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrLocalPort.setStatus(_A)
class _CpqiScsiCxnAttrRemoteAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,16)))
_CpqiScsiCxnAttrRemoteAddrType_Type.__name__=_C
_CpqiScsiCxnAttrRemoteAddrType_Object=MibTableColumn
cpqiScsiCxnAttrRemoteAddrType=_CpqiScsiCxnAttrRemoteAddrType_Object((1,3,6,1,4,1,232,169,2,12,1,1,11),_CpqiScsiCxnAttrRemoteAddrType_Type())
cpqiScsiCxnAttrRemoteAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrRemoteAddrType.setStatus(_A)
class _CpqiScsiCxnAttrRemoteAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqiScsiCxnAttrRemoteAddr_Type.__name__=_H
_CpqiScsiCxnAttrRemoteAddr_Object=MibTableColumn
cpqiScsiCxnAttrRemoteAddr=_CpqiScsiCxnAttrRemoteAddr_Object((1,3,6,1,4,1,232,169,2,12,1,1,12),_CpqiScsiCxnAttrRemoteAddr_Type())
cpqiScsiCxnAttrRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrRemoteAddr.setStatus(_A)
_CpqiScsiCxnAttrRemotePort_Type=Gauge32
_CpqiScsiCxnAttrRemotePort_Object=MibTableColumn
cpqiScsiCxnAttrRemotePort=_CpqiScsiCxnAttrRemotePort_Object((1,3,6,1,4,1,232,169,2,12,1,1,13),_CpqiScsiCxnAttrRemotePort_Type())
cpqiScsiCxnAttrRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrRemotePort.setStatus(_A)
class _CpqiScsiCxnAttrMaxRecvDataSegLength_Type(Integer32):defaultValue=8192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiCxnAttrMaxRecvDataSegLength_Type.__name__=_C
_CpqiScsiCxnAttrMaxRecvDataSegLength_Object=MibTableColumn
cpqiScsiCxnAttrMaxRecvDataSegLength=_CpqiScsiCxnAttrMaxRecvDataSegLength_Object((1,3,6,1,4,1,232,169,2,12,1,1,14),_CpqiScsiCxnAttrMaxRecvDataSegLength_Type())
cpqiScsiCxnAttrMaxRecvDataSegLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrMaxRecvDataSegLength.setStatus(_A)
class _CpqiScsiCxnAttrMaxXmitDataSegLength_Type(Integer32):defaultValue=8192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,16777215))
_CpqiScsiCxnAttrMaxXmitDataSegLength_Type.__name__=_C
_CpqiScsiCxnAttrMaxXmitDataSegLength_Object=MibTableColumn
cpqiScsiCxnAttrMaxXmitDataSegLength=_CpqiScsiCxnAttrMaxXmitDataSegLength_Object((1,3,6,1,4,1,232,169,2,12,1,1,15),_CpqiScsiCxnAttrMaxXmitDataSegLength_Type())
cpqiScsiCxnAttrMaxXmitDataSegLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrMaxXmitDataSegLength.setStatus(_A)
class _CpqiScsiCxnAttrHeaderIntegrity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_I,2),(_L,3),(_M,4)))
_CpqiScsiCxnAttrHeaderIntegrity_Type.__name__=_C
_CpqiScsiCxnAttrHeaderIntegrity_Object=MibTableColumn
cpqiScsiCxnAttrHeaderIntegrity=_CpqiScsiCxnAttrHeaderIntegrity_Object((1,3,6,1,4,1,232,169,2,12,1,1,16),_CpqiScsiCxnAttrHeaderIntegrity_Type())
cpqiScsiCxnAttrHeaderIntegrity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrHeaderIntegrity.setStatus(_A)
class _CpqiScsiCxnAttrDataIntegrity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_I,2),(_L,3),(_M,4)))
_CpqiScsiCxnAttrDataIntegrity_Type.__name__=_C
_CpqiScsiCxnAttrDataIntegrity_Object=MibTableColumn
cpqiScsiCxnAttrDataIntegrity=_CpqiScsiCxnAttrDataIntegrity_Object((1,3,6,1,4,1,232,169,2,12,1,1,17),_CpqiScsiCxnAttrDataIntegrity_Type())
cpqiScsiCxnAttrDataIntegrity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrDataIntegrity.setStatus(_A)
class _CpqiScsiCxnAttrRecvMarker_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiCxnAttrRecvMarker_Type.__name__=_C
_CpqiScsiCxnAttrRecvMarker_Object=MibTableColumn
cpqiScsiCxnAttrRecvMarker=_CpqiScsiCxnAttrRecvMarker_Object((1,3,6,1,4,1,232,169,2,12,1,1,18),_CpqiScsiCxnAttrRecvMarker_Type())
cpqiScsiCxnAttrRecvMarker.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrRecvMarker.setStatus(_A)
class _CpqiScsiCxnAttrSendMarker_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpqiScsiCxnAttrSendMarker_Type.__name__=_C
_CpqiScsiCxnAttrSendMarker_Object=MibTableColumn
cpqiScsiCxnAttrSendMarker=_CpqiScsiCxnAttrSendMarker_Object((1,3,6,1,4,1,232,169,2,12,1,1,19),_CpqiScsiCxnAttrSendMarker_Type())
cpqiScsiCxnAttrSendMarker.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrSendMarker.setStatus(_A)
class _CpqiScsiCxnAttrVersionActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqiScsiCxnAttrVersionActive_Type.__name__=_C
_CpqiScsiCxnAttrVersionActive_Object=MibTableColumn
cpqiScsiCxnAttrVersionActive=_CpqiScsiCxnAttrVersionActive_Object((1,3,6,1,4,1,232,169,2,12,1,1,20),_CpqiScsiCxnAttrVersionActive_Type())
cpqiScsiCxnAttrVersionActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqiScsiCxnAttrVersionActive.setStatus(_A)
cpqiScsiLinkUp=NotificationType((1,3,6,1,4,1,232,0,169001))
cpqiScsiLinkUp.setObjects(*((_V,_W),(_T,_U),(_D,_d)))
if mibBuilder.loadTexts:cpqiScsiLinkUp.setStatus('')
cpqiScsiLinkDown=NotificationType((1,3,6,1,4,1,232,0,169002))
cpqiScsiLinkDown.setObjects(*((_V,_W),(_T,_U),(_D,_d)))
if mibBuilder.loadTexts:cpqiScsiLinkDown.setStatus('')
mibBuilder.exportSymbols(_D,**{'cpqiScsiLinkUp':cpqiScsiLinkUp,'cpqiScsiLinkDown':cpqiScsiLinkDown,'cpqiScsiModule':cpqiScsiModule,'cpqiScsiMibRev':cpqiScsiMibRev,'cpqiScsiMibRevMajor':cpqiScsiMibRevMajor,'cpqiScsiMibRevMinor':cpqiScsiMibRevMinor,'cpqiScsiMibCondition':cpqiScsiMibCondition,'cpqiScsiObjects':cpqiScsiObjects,'cpqiScsiDescriptors':cpqiScsiDescriptors,'cpqiScsiInstance':cpqiScsiInstance,'cpqiScsiInstanceAttributesTable':cpqiScsiInstanceAttributesTable,'cpqiScsiInstanceAttributesEntry':cpqiScsiInstanceAttributesEntry,_J:cpqiScsiInstIndex,_d:cpqiScsiInstDescr,'cpqiScsiInstVersionMin':cpqiScsiInstVersionMin,'cpqiScsiInstVersionMax':cpqiScsiInstVersionMax,'cpqiScsiInstVendorID':cpqiScsiInstVendorID,'cpqiScsiInstVendorVersion':cpqiScsiInstVendorVersion,'cpqiScsiInstPortalNumber':cpqiScsiInstPortalNumber,'cpqiScsiInstNodeNumber':cpqiScsiInstNodeNumber,'cpqiScsiInstSessionNumber':cpqiScsiInstSessionNumber,'cpqiScsiInstSsnFailures':cpqiScsiInstSsnFailures,'cpqiScsiInstLastSsnFailureType':cpqiScsiInstLastSsnFailureType,'cpqiScsiInstLastSsnRmtNodeName':cpqiScsiInstLastSsnRmtNodeName,'cpqiScsiInstanceSsnErrorStatsTable':cpqiScsiInstanceSsnErrorStatsTable,'cpqiScsiInstanceSsnErrorStatsEntry':cpqiScsiInstanceSsnErrorStatsEntry,'cpqiScsiInstSsnInstIndex':cpqiScsiInstSsnInstIndex,'cpqiScsiInstSsnDigestErrors':cpqiScsiInstSsnDigestErrors,'cpqiScsiInstSsnCxnTimeoutErrors':cpqiScsiInstSsnCxnTimeoutErrors,'cpqiScsiInstSsnFormatErrors':cpqiScsiInstSsnFormatErrors,'cpqiScsiPortal':cpqiScsiPortal,'cpqiScsiPortalAttributesTable':cpqiScsiPortalAttributesTable,'cpqiScsiPortalAttributesEntry':cpqiScsiPortalAttributesEntry,'cpqiScsiPortalInstIndex':cpqiScsiPortalInstIndex,_S:cpqiScsiPortalIndex,'cpqiScsiPortalRowStatus':cpqiScsiPortalRowStatus,'cpqiScsiPortalRoles':cpqiScsiPortalRoles,'cpqiScsiPortalAddrType':cpqiScsiPortalAddrType,'cpqiScsiPortalAddr':cpqiScsiPortalAddr,'cpqiScsiPortalProtocol':cpqiScsiPortalProtocol,'cpqiScsiPortalMaxRecvDataSegLength':cpqiScsiPortalMaxRecvDataSegLength,'cpqiScsiPortalPrimaryHdrDigest':cpqiScsiPortalPrimaryHdrDigest,'cpqiScsiPortalPrimaryDataDigest':cpqiScsiPortalPrimaryDataDigest,'cpqiScsiPortalSecondaryHdrDigest':cpqiScsiPortalSecondaryHdrDigest,'cpqiScsiPortalSecondaryDataDigest':cpqiScsiPortalSecondaryDataDigest,'cpqiScsiPortalRecvMarker':cpqiScsiPortalRecvMarker,'cpqiScsiTargetPortal':cpqiScsiTargetPortal,'cpqiScsiTgtPortalAttributesTable':cpqiScsiTgtPortalAttributesTable,'cpqiScsiTgtPortalAttributesEntry':cpqiScsiTgtPortalAttributesEntry,'cpqiScsiTgtPortalInstIndex':cpqiScsiTgtPortalInstIndex,'cpqiScsiTgtPortalPortalIndex':cpqiScsiTgtPortalPortalIndex,'cpqiScsiTgtPortalPort':cpqiScsiTgtPortalPort,'cpqiScsiTgtPortalTag':cpqiScsiTgtPortalTag,'cpqiScsiInitiatorPortal':cpqiScsiInitiatorPortal,'cpqiScsiIntrPortalAttributesTable':cpqiScsiIntrPortalAttributesTable,'cpqiScsiIntrPortalAttributesEntry':cpqiScsiIntrPortalAttributesEntry,'cpqiScsiIntrPortalInstIndex':cpqiScsiIntrPortalInstIndex,'cpqiScsiIntrPortalPortalIndex':cpqiScsiIntrPortalPortalIndex,'cpqiScsiIntrPortalTag':cpqiScsiIntrPortalTag,'cpqiScsiNode':cpqiScsiNode,'cpqiScsiNodeAttributesTable':cpqiScsiNodeAttributesTable,'cpqiScsiNodeAttributesEntry':cpqiScsiNodeAttributesEntry,_g:cpqiScsiNodeInstIndex,_h:cpqiScsiNodeNodeIndex,'cpqiScsiNodeName':cpqiScsiNodeName,'cpqiScsiNodeAlias':cpqiScsiNodeAlias,'cpqiScsiNodeRoles':cpqiScsiNodeRoles,'cpqiScsiNodeTransportType':cpqiScsiNodeTransportType,'cpqiScsiNodeInitialR2T':cpqiScsiNodeInitialR2T,'cpqiScsiNodeImmediateData':cpqiScsiNodeImmediateData,'cpqiScsiNodeMaxOutstandingR2T':cpqiScsiNodeMaxOutstandingR2T,'cpqiScsiNodeFirstBurstLength':cpqiScsiNodeFirstBurstLength,'cpqiScsiNodeMaxBurstLength':cpqiScsiNodeMaxBurstLength,'cpqiScsiNodeMaxConnections':cpqiScsiNodeMaxConnections,'cpqiScsiNodeDataSequenceInOrder':cpqiScsiNodeDataSequenceInOrder,'cpqiScsiNodeDataPDUInOrder':cpqiScsiNodeDataPDUInOrder,'cpqiScsiNodeDefaultTime2Wait':cpqiScsiNodeDefaultTime2Wait,'cpqiScsiNodeDefaultTime2Retain':cpqiScsiNodeDefaultTime2Retain,'cpqiScsiNodeErrorRecoveryLevel':cpqiScsiNodeErrorRecoveryLevel,'cpqiScsiTarget':cpqiScsiTarget,'cpqiScsiTargetAttributesTable':cpqiScsiTargetAttributesTable,'cpqiScsiTargetAttributesEntry':cpqiScsiTargetAttributesEntry,_i:cpqiScsiTgtInstIndex,_j:cpqiScsiTgtNodeIndex,'cpqiScsiTgtLoginFailures':cpqiScsiTgtLoginFailures,'cpqiScsiTgtLastFailureTime':cpqiScsiTgtLastFailureTime,'cpqiScsiTgtLastFailureType':cpqiScsiTgtLastFailureType,'cpqiScsiTgtLastIntrFailureName':cpqiScsiTgtLastIntrFailureName,'cpqiScsiTgtLastIntrFailureAddrType':cpqiScsiTgtLastIntrFailureAddrType,'cpqiScsiTgtLastIntrFailureAddr':cpqiScsiTgtLastIntrFailureAddr,'cpqiScsiTargetLoginStatsTable':cpqiScsiTargetLoginStatsTable,'cpqiScsiTargetLoginStatsEntry':cpqiScsiTargetLoginStatsEntry,_k:cpqiScsiTgtLoginInstIndex,_l:cpqiScsiTgtLoginNodeIndex,'cpqiScsiTgtLoginAccepts':cpqiScsiTgtLoginAccepts,'cpqiScsiTgtLoginOtherFails':cpqiScsiTgtLoginOtherFails,'cpqiScsiTgtLoginRedirects':cpqiScsiTgtLoginRedirects,'cpqiScsiTgtLoginAuthorizeFails':cpqiScsiTgtLoginAuthorizeFails,'cpqiScsiTgtLoginAuthenticateFails':cpqiScsiTgtLoginAuthenticateFails,'cpqiScsiTgtLoginNegotiateFails':cpqiScsiTgtLoginNegotiateFails,'cpqiScsiTargetLogoutStatsTable':cpqiScsiTargetLogoutStatsTable,'cpqiScsiTargetLogoutStatsEntry':cpqiScsiTargetLogoutStatsEntry,_m:cpqiScsiTgtLogoutInstIndex,_n:cpqiScsiTgtLogoutNodeIndex,'cpqiScsiTgtLogoutNormals':cpqiScsiTgtLogoutNormals,'cpqiScsiTgtLogoutOthers':cpqiScsiTgtLogoutOthers,'cpqiScsiTgtAuthorization':cpqiScsiTgtAuthorization,'cpqiScsiTgtAuthAttributesTable':cpqiScsiTgtAuthAttributesTable,'cpqiScsiTgtAuthAttributesEntry':cpqiScsiTgtAuthAttributesEntry,_o:cpqiScsiTgtAuthInstIndex,_p:cpqiScsiTgtAuthNodeIndex,_q:cpqiScsiTgtAuthIndex,'cpqiScsiTgtAuthRowStatus':cpqiScsiTgtAuthRowStatus,'cpqiScsiTgtAuthIdentity':cpqiScsiTgtAuthIdentity,'cpqiScsiInitiator':cpqiScsiInitiator,'cpqiScsiInitiatorAttributesTable':cpqiScsiInitiatorAttributesTable,'cpqiScsiInitiatorAttributesEntry':cpqiScsiInitiatorAttributesEntry,_r:cpqiScsiIntrInstIndex,_s:cpqiScsiIntrNodeIndex,'cpqiScsiIntrLoginFailures':cpqiScsiIntrLoginFailures,'cpqiScsiIntrLastFailureTime':cpqiScsiIntrLastFailureTime,'cpqiScsiIntrLastFailureType':cpqiScsiIntrLastFailureType,'cpqiScsiIntrLastTgtFailureName':cpqiScsiIntrLastTgtFailureName,'cpqiScsiIntrLastTgtFailureAddrType':cpqiScsiIntrLastTgtFailureAddrType,'cpqiScsiIntrLastTgtFailureAddr':cpqiScsiIntrLastTgtFailureAddr,'cpqiScsiInitiatorLoginStatsTable':cpqiScsiInitiatorLoginStatsTable,'cpqiScsiInitiatorLoginStatsEntry':cpqiScsiInitiatorLoginStatsEntry,_t:cpqiScsiIntrLoginInstIndex,_u:cpqiScsiIntrLoginNodeIndex,'cpqiScsiIntrLoginAcceptRsps':cpqiScsiIntrLoginAcceptRsps,'cpqiScsiIntrLoginOtherFailRsps':cpqiScsiIntrLoginOtherFailRsps,'cpqiScsiIntrLoginRedirectRsps':cpqiScsiIntrLoginRedirectRsps,'cpqiScsiIntrLoginAuthFailRsps':cpqiScsiIntrLoginAuthFailRsps,'cpqiScsiIntrLoginAuthenticateFails':cpqiScsiIntrLoginAuthenticateFails,'cpqiScsiIntrLoginNegotiateFails':cpqiScsiIntrLoginNegotiateFails,'cpqiScsiInitiatorLogoutStatsTable':cpqiScsiInitiatorLogoutStatsTable,'cpqiScsiInitiatorLogoutStatsEntry':cpqiScsiInitiatorLogoutStatsEntry,_v:cpqiScsiIntrLogoutInstIndex,_w:cpqiScsiIntrLogoutNodeIndex,'cpqiScsiIntrLogoutNormals':cpqiScsiIntrLogoutNormals,'cpqiScsiIntrLogoutOthers':cpqiScsiIntrLogoutOthers,'cpqiScsiIntrAuthorization':cpqiScsiIntrAuthorization,'cpqiScsiIntrAuthAttributesTable':cpqiScsiIntrAuthAttributesTable,'cpqiScsiIntrAuthAttributesEntry':cpqiScsiIntrAuthAttributesEntry,_x:cpqiScsiIntrAuthInstIndex,_y:cpqiScsiIntrAuthNodeIndex,_z:cpqiScsiIntrAuthIndex,'cpqiScsiIntrAuthRowStatus':cpqiScsiIntrAuthRowStatus,'cpqiScsiIntrAuthIdentity':cpqiScsiIntrAuthIdentity,'cpqiScsiSession':cpqiScsiSession,'cpqiScsiSessionAttributesTable':cpqiScsiSessionAttributesTable,'cpqiScsiSessionAttributesEntry':cpqiScsiSessionAttributesEntry,_A0:cpqiScsiSsnInstIndex,_A1:cpqiScsiSsnNodeIndex,_A2:cpqiScsiSsnIndex,'cpqiScsiSsnDirection':cpqiScsiSsnDirection,'cpqiScsiSsnInitiatorName':cpqiScsiSsnInitiatorName,'cpqiScsiSsnTargetName':cpqiScsiSsnTargetName,'cpqiScsiSsnTSIH':cpqiScsiSsnTSIH,'cpqiScsiSsnISID':cpqiScsiSsnISID,'cpqiScsiSsnInitiatorAlias':cpqiScsiSsnInitiatorAlias,'cpqiScsiSsnTargetAlias':cpqiScsiSsnTargetAlias,'cpqiScsiSsnInitialR2T':cpqiScsiSsnInitialR2T,'cpqiScsiSsnImmediateData':cpqiScsiSsnImmediateData,'cpqiScsiSsnType':cpqiScsiSsnType,'cpqiScsiSsnMaxOutstandingR2T':cpqiScsiSsnMaxOutstandingR2T,'cpqiScsiSsnFirstBurstLength':cpqiScsiSsnFirstBurstLength,'cpqiScsiSsnMaxBurstLength':cpqiScsiSsnMaxBurstLength,'cpqiScsiSsnConnectionNumber':cpqiScsiSsnConnectionNumber,'cpqiScsiSsnAuthIdentity':cpqiScsiSsnAuthIdentity,'cpqiScsiSsnDataSequenceInOrder':cpqiScsiSsnDataSequenceInOrder,'cpqiScsiSsnDataPDUInOrder':cpqiScsiSsnDataPDUInOrder,'cpqiScsiSsnErrorRecoveryLevel':cpqiScsiSsnErrorRecoveryLevel,'cpqiScsiSessionId':cpqiScsiSessionId,'cpqiScsiSessionStatsTable':cpqiScsiSessionStatsTable,'cpqiScsiSessionStatsEntry':cpqiScsiSessionStatsEntry,_A3:cpqiScsiSsnStatInstIndex,_A4:cpqiScsiSsnStatNodeIndex,_A5:cpqiScsiSsnSessionIndex,'cpqiScsiSsnCmdPDUs':cpqiScsiSsnCmdPDUs,'cpqiScsiSsnRspPDUs':cpqiScsiSsnRspPDUs,'cpqiScsiSsnTxDataOctets':cpqiScsiSsnTxDataOctets,'cpqiScsiSsnRxDataOctets':cpqiScsiSsnRxDataOctets,'cpqiScsiSsnLCTxDataOctets':cpqiScsiSsnLCTxDataOctets,'cpqiScsiSsnLCRxDataOctets':cpqiScsiSsnLCRxDataOctets,'cpqiScsiSessionCxnErrorStatsTable':cpqiScsiSessionCxnErrorStatsTable,'cpqiScsiSessionCxnErrorStatsEntry':cpqiScsiSessionCxnErrorStatsEntry,_A6:cpqiScsiSsnCxnInstIndex,_A7:cpqiScsiSsnCxnNodeIndex,_A8:cpqiScsiSsnCxnIndex,'cpqiScsiSsnCxnDigestErrors':cpqiScsiSsnCxnDigestErrors,'cpqiScsiSsnCxnTimeoutErrors':cpqiScsiSsnCxnTimeoutErrors,'cpqiScsiConnection':cpqiScsiConnection,'cpqiScsiConnectionAttributesTable':cpqiScsiConnectionAttributesTable,'cpqiScsiConnectionAttributesEntry':cpqiScsiConnectionAttributesEntry,_A9:cpqiScsiCxnAttrInstIndex,_AA:cpqiScsiCxnAttrNodeIndex,_AB:cpqiScsiCxnAttrSessionIndex,_AC:cpqiScsiCxnAttrIndex,'cpqiScsiCxnAttrCid':cpqiScsiCxnAttrCid,'cpqiScsiCxnAttrState':cpqiScsiCxnAttrState,'cpqiScsiCxnAttrLocalAddrType':cpqiScsiCxnAttrLocalAddrType,'cpqiScsiCxnAttrLocalAddr':cpqiScsiCxnAttrLocalAddr,'cpqiScsiCxnAttrProtocol':cpqiScsiCxnAttrProtocol,'cpqiScsiCxnAttrLocalPort':cpqiScsiCxnAttrLocalPort,'cpqiScsiCxnAttrRemoteAddrType':cpqiScsiCxnAttrRemoteAddrType,'cpqiScsiCxnAttrRemoteAddr':cpqiScsiCxnAttrRemoteAddr,'cpqiScsiCxnAttrRemotePort':cpqiScsiCxnAttrRemotePort,'cpqiScsiCxnAttrMaxRecvDataSegLength':cpqiScsiCxnAttrMaxRecvDataSegLength,'cpqiScsiCxnAttrMaxXmitDataSegLength':cpqiScsiCxnAttrMaxXmitDataSegLength,'cpqiScsiCxnAttrHeaderIntegrity':cpqiScsiCxnAttrHeaderIntegrity,'cpqiScsiCxnAttrDataIntegrity':cpqiScsiCxnAttrDataIntegrity,'cpqiScsiCxnAttrRecvMarker':cpqiScsiCxnAttrRecvMarker,'cpqiScsiCxnAttrSendMarker':cpqiScsiCxnAttrSendMarker,'cpqiScsiCxnAttrVersionActive':cpqiScsiCxnAttrVersionActive})