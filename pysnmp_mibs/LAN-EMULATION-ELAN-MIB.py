_g='lecsErrLogIndex'
_f='lecsVccVci'
_e='lecsVccVpi'
_d='lecsVccIfIndex'
_c='lecsTlvIndex'
_b='lecsTlvTag'
_a='lecsTlvSelectorIndex'
_Z='AtmLaneMask'
_Y='IfIndexOrZero'
_X='elanLecElanName'
_W='elanLecFrameSize'
_V='elanLecRdBridgeNum'
_U='elanLecRdSegId'
_T='elanLecMacAddress'
_S='elanLecAtmMask'
_R='elanLecAtmAddress'
_Q='elanPolicyIndex'
_P='elanPolicySelectorIndex'
_O='LecDataFrameSize'
_N='LecDataFrameFormat'
_M='Integer'
_L='AtmLaneAddress'
_K='DisplayString'
_J='OctetString'
_I='lecsConfIndex'
_H='elanLesIndex'
_G='elanConfIndex'
_F='Integer32'
_E='not-accessible'
_D='read-only'
_C='read-write'
_B='LAN-EMULATION-ELAN-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1',_M,_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
LecDataFrameFormat,LecDataFrameSize,VciInteger,VpiInteger,atmfLanEmulation=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB',_N,_O,'VciInteger','VpiInteger','atmfLanEmulation')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
class Integer(Integer32):0
class RowStatus(Integer32):0
class AutonomousType(ObjectIdentifier):0
class TIMESTAMP(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class AtmLaneAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class IfIndexOrZero(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class ElanLocalIndex(Integer32):0
class AtmLaneMask(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
class TlvSelectorIndexType(Integer32):0
class PolicySelectorIndexType(Integer32):0
class LecsErrLogIndexType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ElanMIB_ObjectIdentity=ObjectIdentity
elanMIB=_ElanMIB_ObjectIdentity((1,3,6,1,4,1,353,5,3,2))
_ElanAdminGroup_ObjectIdentity=ObjectIdentity
elanAdminGroup=_ElanAdminGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1))
_ElanAdminPolicyVal_ObjectIdentity=ObjectIdentity
elanAdminPolicyVal=_ElanAdminPolicyVal_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1))
_ByAtmAddr_ObjectIdentity=ObjectIdentity
byAtmAddr=_ByAtmAddr_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1,1))
_ByMacAddr_ObjectIdentity=ObjectIdentity
byMacAddr=_ByMacAddr_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1,2))
_ByRouteDescriptor_ObjectIdentity=ObjectIdentity
byRouteDescriptor=_ByRouteDescriptor_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1,3))
_ByLanType_ObjectIdentity=ObjectIdentity
byLanType=_ByLanType_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1,4))
_ByPktSize_ObjectIdentity=ObjectIdentity
byPktSize=_ByPktSize_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1,5))
_ByElanName_ObjectIdentity=ObjectIdentity
byElanName=_ByElanName_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,1,1,6))
_ElanConfGroup_ObjectIdentity=ObjectIdentity
elanConfGroup=_ElanConfGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,2))
_ElanConfNextId_Type=ElanLocalIndex
_ElanConfNextId_Object=MibScalar
elanConfNextId=_ElanConfNextId_Object((1,3,6,1,4,1,353,5,3,2,2,1),_ElanConfNextId_Type())
elanConfNextId.setMaxAccess(_D)
if mibBuilder.loadTexts:elanConfNextId.setStatus(_A)
_ElanConfTable_Object=MibTable
elanConfTable=_ElanConfTable_Object((1,3,6,1,4,1,353,5,3,2,2,2))
if mibBuilder.loadTexts:elanConfTable.setStatus(_A)
_ElanConfEntry_Object=MibTableRow
elanConfEntry=_ElanConfEntry_Object((1,3,6,1,4,1,353,5,3,2,2,2,1))
elanConfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:elanConfEntry.setStatus(_A)
_ElanConfIndex_Type=ElanLocalIndex
_ElanConfIndex_Object=MibTableColumn
elanConfIndex=_ElanConfIndex_Object((1,3,6,1,4,1,353,5,3,2,2,2,1,1),_ElanConfIndex_Type())
elanConfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:elanConfIndex.setStatus(_A)
class _ElanConfName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ElanConfName_Type.__name__=_K
_ElanConfName_Object=MibTableColumn
elanConfName=_ElanConfName_Object((1,3,6,1,4,1,353,5,3,2,2,2,1,2),_ElanConfName_Type())
elanConfName.setMaxAccess(_C)
if mibBuilder.loadTexts:elanConfName.setStatus(_A)
_ElanConfTlvIndex_Type=TlvSelectorIndexType
_ElanConfTlvIndex_Object=MibTableColumn
elanConfTlvIndex=_ElanConfTlvIndex_Object((1,3,6,1,4,1,353,5,3,2,2,2,1,3),_ElanConfTlvIndex_Type())
elanConfTlvIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:elanConfTlvIndex.setStatus(_A)
class _ElanConfLanType_Type(LecDataFrameFormat):defaultValue=1
_ElanConfLanType_Type.__name__=_N
_ElanConfLanType_Object=MibTableColumn
elanConfLanType=_ElanConfLanType_Object((1,3,6,1,4,1,353,5,3,2,2,2,1,4),_ElanConfLanType_Type())
elanConfLanType.setMaxAccess(_C)
if mibBuilder.loadTexts:elanConfLanType.setStatus(_A)
class _ElanConfMaxFrameSize_Type(LecDataFrameSize):defaultValue=1
_ElanConfMaxFrameSize_Type.__name__=_O
_ElanConfMaxFrameSize_Object=MibTableColumn
elanConfMaxFrameSize=_ElanConfMaxFrameSize_Object((1,3,6,1,4,1,353,5,3,2,2,2,1,5),_ElanConfMaxFrameSize_Type())
elanConfMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:elanConfMaxFrameSize.setStatus(_A)
_ElanConfRowStatus_Type=RowStatus
_ElanConfRowStatus_Object=MibTableColumn
elanConfRowStatus=_ElanConfRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,2,1,6),_ElanConfRowStatus_Type())
elanConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanConfRowStatus.setStatus(_A)
_ElanLesTable_Object=MibTable
elanLesTable=_ElanLesTable_Object((1,3,6,1,4,1,353,5,3,2,2,3))
if mibBuilder.loadTexts:elanLesTable.setStatus(_A)
_ElanLesEntry_Object=MibTableRow
elanLesEntry=_ElanLesEntry_Object((1,3,6,1,4,1,353,5,3,2,2,3,1))
elanLesEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:elanLesEntry.setStatus(_A)
_ElanLesIndex_Type=Integer32
_ElanLesIndex_Object=MibTableColumn
elanLesIndex=_ElanLesIndex_Object((1,3,6,1,4,1,353,5,3,2,2,3,1,1),_ElanLesIndex_Type())
elanLesIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLesIndex.setStatus(_A)
class _ElanLesAtmAddress_Type(AtmLaneAddress):defaultValue=OctetString('')
_ElanLesAtmAddress_Type.__name__=_L
_ElanLesAtmAddress_Object=MibTableColumn
elanLesAtmAddress=_ElanLesAtmAddress_Object((1,3,6,1,4,1,353,5,3,2,2,3,1,2),_ElanLesAtmAddress_Type())
elanLesAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLesAtmAddress.setStatus(_A)
_ElanLesRowStatus_Type=RowStatus
_ElanLesRowStatus_Object=MibTableColumn
elanLesRowStatus=_ElanLesRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,3,1,3),_ElanLesRowStatus_Type())
elanLesRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLesRowStatus.setStatus(_A)
_ElanPolicyTable_Object=MibTable
elanPolicyTable=_ElanPolicyTable_Object((1,3,6,1,4,1,353,5,3,2,2,4))
if mibBuilder.loadTexts:elanPolicyTable.setStatus(_A)
_ElanPolicyEntry_Object=MibTableRow
elanPolicyEntry=_ElanPolicyEntry_Object((1,3,6,1,4,1,353,5,3,2,2,4,1))
elanPolicyEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:elanPolicyEntry.setStatus(_A)
_ElanPolicySelectorIndex_Type=PolicySelectorIndexType
_ElanPolicySelectorIndex_Object=MibTableColumn
elanPolicySelectorIndex=_ElanPolicySelectorIndex_Object((1,3,6,1,4,1,353,5,3,2,2,4,1,1),_ElanPolicySelectorIndex_Type())
elanPolicySelectorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:elanPolicySelectorIndex.setStatus(_A)
class _ElanPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65000))
_ElanPolicyIndex_Type.__name__=_F
_ElanPolicyIndex_Object=MibTableColumn
elanPolicyIndex=_ElanPolicyIndex_Object((1,3,6,1,4,1,353,5,3,2,2,4,1,2),_ElanPolicyIndex_Type())
elanPolicyIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:elanPolicyIndex.setStatus(_A)
class _ElanPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65000))
_ElanPolicyPriority_Type.__name__=_F
_ElanPolicyPriority_Object=MibTableColumn
elanPolicyPriority=_ElanPolicyPriority_Object((1,3,6,1,4,1,353,5,3,2,2,4,1,3),_ElanPolicyPriority_Type())
elanPolicyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:elanPolicyPriority.setStatus(_A)
_ElanPolicyType_Type=AutonomousType
_ElanPolicyType_Object=MibTableColumn
elanPolicyType=_ElanPolicyType_Object((1,3,6,1,4,1,353,5,3,2,2,4,1,4),_ElanPolicyType_Type())
elanPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:elanPolicyType.setStatus(_A)
_ElanPolicyRowStatus_Type=RowStatus
_ElanPolicyRowStatus_Object=MibTableColumn
elanPolicyRowStatus=_ElanPolicyRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,4,1,5),_ElanPolicyRowStatus_Type())
elanPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanPolicyRowStatus.setStatus(_A)
_ElanLecAtmAddrTable_Object=MibTable
elanLecAtmAddrTable=_ElanLecAtmAddrTable_Object((1,3,6,1,4,1,353,5,3,2,2,5))
if mibBuilder.loadTexts:elanLecAtmAddrTable.setStatus(_A)
_ElanLecAtmAddrEntry_Object=MibTableRow
elanLecAtmAddrEntry=_ElanLecAtmAddrEntry_Object((1,3,6,1,4,1,353,5,3,2,2,5,1))
elanLecAtmAddrEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:elanLecAtmAddrEntry.setStatus(_A)
_ElanLecAtmAddress_Type=AtmLaneAddress
_ElanLecAtmAddress_Object=MibTableColumn
elanLecAtmAddress=_ElanLecAtmAddress_Object((1,3,6,1,4,1,353,5,3,2,2,5,1,1),_ElanLecAtmAddress_Type())
elanLecAtmAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecAtmAddress.setStatus(_A)
_ElanLecAtmMask_Type=AtmLaneAddress
_ElanLecAtmMask_Object=MibTableColumn
elanLecAtmMask=_ElanLecAtmMask_Object((1,3,6,1,4,1,353,5,3,2,2,5,1,2),_ElanLecAtmMask_Type())
elanLecAtmMask.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecAtmMask.setStatus(_A)
_ElanLecAtmRowStatus_Type=RowStatus
_ElanLecAtmRowStatus_Object=MibTableColumn
elanLecAtmRowStatus=_ElanLecAtmRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,5,1,4),_ElanLecAtmRowStatus_Type())
elanLecAtmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLecAtmRowStatus.setStatus(_A)
_ElanLecMacAddrTable_Object=MibTable
elanLecMacAddrTable=_ElanLecMacAddrTable_Object((1,3,6,1,4,1,353,5,3,2,2,6))
if mibBuilder.loadTexts:elanLecMacAddrTable.setStatus(_A)
_ElanLecMacAddrEntry_Object=MibTableRow
elanLecMacAddrEntry=_ElanLecMacAddrEntry_Object((1,3,6,1,4,1,353,5,3,2,2,6,1))
elanLecMacAddrEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_T))
if mibBuilder.loadTexts:elanLecMacAddrEntry.setStatus(_A)
_ElanLecMacAddress_Type=MacAddress
_ElanLecMacAddress_Object=MibTableColumn
elanLecMacAddress=_ElanLecMacAddress_Object((1,3,6,1,4,1,353,5,3,2,2,6,1,1),_ElanLecMacAddress_Type())
elanLecMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecMacAddress.setStatus(_A)
_ElanLecMacRowStatus_Type=RowStatus
_ElanLecMacRowStatus_Object=MibTableColumn
elanLecMacRowStatus=_ElanLecMacRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,6,1,2),_ElanLecMacRowStatus_Type())
elanLecMacRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLecMacRowStatus.setStatus(_A)
_ElanLecRdTable_Object=MibTable
elanLecRdTable=_ElanLecRdTable_Object((1,3,6,1,4,1,353,5,3,2,2,7))
if mibBuilder.loadTexts:elanLecRdTable.setStatus(_A)
_ElanLecRdEntry_Object=MibTableRow
elanLecRdEntry=_ElanLecRdEntry_Object((1,3,6,1,4,1,353,5,3,2,2,7,1))
elanLecRdEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:elanLecRdEntry.setStatus(_A)
class _ElanLecRdSegId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ElanLecRdSegId_Type.__name__=_F
_ElanLecRdSegId_Object=MibTableColumn
elanLecRdSegId=_ElanLecRdSegId_Object((1,3,6,1,4,1,353,5,3,2,2,7,1,1),_ElanLecRdSegId_Type())
elanLecRdSegId.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecRdSegId.setStatus(_A)
class _ElanLecRdBridgeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ElanLecRdBridgeNum_Type.__name__=_F
_ElanLecRdBridgeNum_Object=MibTableColumn
elanLecRdBridgeNum=_ElanLecRdBridgeNum_Object((1,3,6,1,4,1,353,5,3,2,2,7,1,2),_ElanLecRdBridgeNum_Type())
elanLecRdBridgeNum.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecRdBridgeNum.setStatus(_A)
_ElanLecRdRowStatus_Type=RowStatus
_ElanLecRdRowStatus_Object=MibTableColumn
elanLecRdRowStatus=_ElanLecRdRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,7,1,4),_ElanLecRdRowStatus_Type())
elanLecRdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLecRdRowStatus.setStatus(_A)
_ElanLecPktSizeTable_Object=MibTable
elanLecPktSizeTable=_ElanLecPktSizeTable_Object((1,3,6,1,4,1,353,5,3,2,2,8))
if mibBuilder.loadTexts:elanLecPktSizeTable.setStatus(_A)
_ElanLecPktSizeEntry_Object=MibTableRow
elanLecPktSizeEntry=_ElanLecPktSizeEntry_Object((1,3,6,1,4,1,353,5,3,2,2,8,1))
elanLecPktSizeEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_W))
if mibBuilder.loadTexts:elanLecPktSizeEntry.setStatus(_A)
_ElanLecFrameSize_Type=LecDataFrameSize
_ElanLecFrameSize_Object=MibTableColumn
elanLecFrameSize=_ElanLecFrameSize_Object((1,3,6,1,4,1,353,5,3,2,2,8,1,1),_ElanLecFrameSize_Type())
elanLecFrameSize.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecFrameSize.setStatus(_A)
_ElanLecPktSizeRowStatus_Type=RowStatus
_ElanLecPktSizeRowStatus_Object=MibTableColumn
elanLecPktSizeRowStatus=_ElanLecPktSizeRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,8,1,2),_ElanLecPktSizeRowStatus_Type())
elanLecPktSizeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLecPktSizeRowStatus.setStatus(_A)
_ElanLecNameTable_Object=MibTable
elanLecNameTable=_ElanLecNameTable_Object((1,3,6,1,4,1,353,5,3,2,2,9))
if mibBuilder.loadTexts:elanLecNameTable.setStatus(_A)
_ElanLecNameEntry_Object=MibTableRow
elanLecNameEntry=_ElanLecNameEntry_Object((1,3,6,1,4,1,353,5,3,2,2,9,1))
elanLecNameEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_X))
if mibBuilder.loadTexts:elanLecNameEntry.setStatus(_A)
class _ElanLecElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ElanLecElanName_Type.__name__=_K
_ElanLecElanName_Object=MibTableColumn
elanLecElanName=_ElanLecElanName_Object((1,3,6,1,4,1,353,5,3,2,2,9,1,1),_ElanLecElanName_Type())
elanLecElanName.setMaxAccess(_E)
if mibBuilder.loadTexts:elanLecElanName.setStatus(_A)
_ElanLecNameRowStatus_Type=RowStatus
_ElanLecNameRowStatus_Object=MibTableColumn
elanLecNameRowStatus=_ElanLecNameRowStatus_Object((1,3,6,1,4,1,353,5,3,2,2,9,1,2),_ElanLecNameRowStatus_Type())
elanLecNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:elanLecNameRowStatus.setStatus(_A)
_ElanLecsGroup_ObjectIdentity=ObjectIdentity
elanLecsGroup=_ElanLecsGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,3))
_ElanLecsConfGroup_ObjectIdentity=ObjectIdentity
elanLecsConfGroup=_ElanLecsConfGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,3,1))
_LecsConfNextId_Type=ElanLocalIndex
_LecsConfNextId_Object=MibScalar
lecsConfNextId=_LecsConfNextId_Object((1,3,6,1,4,1,353,5,3,2,3,1,1),_LecsConfNextId_Type())
lecsConfNextId.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsConfNextId.setStatus(_A)
_LecsConfTable_Object=MibTable
lecsConfTable=_LecsConfTable_Object((1,3,6,1,4,1,353,5,3,2,3,1,2))
if mibBuilder.loadTexts:lecsConfTable.setStatus(_A)
_LecsConfEntry_Object=MibTableRow
lecsConfEntry=_LecsConfEntry_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1))
lecsConfEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:lecsConfEntry.setStatus(_A)
_LecsConfIndex_Type=Integer32
_LecsConfIndex_Object=MibTableColumn
lecsConfIndex=_LecsConfIndex_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,1),_LecsConfIndex_Type())
lecsConfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsConfIndex.setStatus(_A)
class _LecsAtmIfIndex_Type(IfIndexOrZero):defaultValue=0
_LecsAtmIfIndex_Type.__name__=_Y
_LecsAtmIfIndex_Object=MibTableColumn
lecsAtmIfIndex=_LecsAtmIfIndex_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,2),_LecsAtmIfIndex_Type())
lecsAtmIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmIfIndex.setStatus(_A)
class _LecsAtmAddrSpec_Type(AtmLaneAddress):defaultHexValue='4700790000000000000000000000A03E00000100'
_LecsAtmAddrSpec_Type.__name__=_L
_LecsAtmAddrSpec_Object=MibTableColumn
lecsAtmAddrSpec=_LecsAtmAddrSpec_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,3),_LecsAtmAddrSpec_Type())
lecsAtmAddrSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrSpec.setStatus(_A)
class _LecsAtmAddrMask_Type(AtmLaneMask):defaultHexValue='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
_LecsAtmAddrMask_Type.__name__=_Z
_LecsAtmAddrMask_Object=MibTableColumn
lecsAtmAddrMask=_LecsAtmAddrMask_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,4),_LecsAtmAddrMask_Type())
lecsAtmAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrMask.setStatus(_A)
_LecsAtmAddrActual_Type=AtmLaneAddress
_LecsAtmAddrActual_Object=MibTableColumn
lecsAtmAddrActual=_LecsAtmAddrActual_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,5),_LecsAtmAddrActual_Type())
lecsAtmAddrActual.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsAtmAddrActual.setStatus(_A)
_LecsPolicySelIndex_Type=PolicySelectorIndexType
_LecsPolicySelIndex_Object=MibTableColumn
lecsPolicySelIndex=_LecsPolicySelIndex_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,6),_LecsPolicySelIndex_Type())
lecsPolicySelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsPolicySelIndex.setStatus(_A)
_LecsLastInitialized_Type=TIMESTAMP
_LecsLastInitialized_Object=MibTableColumn
lecsLastInitialized=_LecsLastInitialized_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,7),_LecsLastInitialized_Type())
lecsLastInitialized.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsLastInitialized.setStatus(_A)
class _LecsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('up',2),('down',3)))
_LecsOperStatus_Type.__name__=_F
_LecsOperStatus_Object=MibTableColumn
lecsOperStatus=_LecsOperStatus_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,8),_LecsOperStatus_Type())
lecsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsOperStatus.setStatus(_A)
class _LecsAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_LecsAdminStatus_Type.__name__=_F
_LecsAdminStatus_Object=MibTableColumn
lecsAdminStatus=_LecsAdminStatus_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,9),_LecsAdminStatus_Type())
lecsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAdminStatus.setStatus(_A)
_LecsRowStatus_Type=RowStatus
_LecsRowStatus_Object=MibTableColumn
lecsRowStatus=_LecsRowStatus_Object((1,3,6,1,4,1,353,5,3,2,3,1,2,1,10),_LecsRowStatus_Type())
lecsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsRowStatus.setStatus(_A)
_LecsElanTable_Object=MibTable
lecsElanTable=_LecsElanTable_Object((1,3,6,1,4,1,353,5,3,2,3,1,3))
if mibBuilder.loadTexts:lecsElanTable.setStatus(_A)
_LecsElanEntry_Object=MibTableRow
lecsElanEntry=_LecsElanEntry_Object((1,3,6,1,4,1,353,5,3,2,3,1,3,1))
lecsElanEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:lecsElanEntry.setStatus(_A)
_LecsElanRowStatus_Type=RowStatus
_LecsElanRowStatus_Object=MibTableColumn
lecsElanRowStatus=_LecsElanRowStatus_Object((1,3,6,1,4,1,353,5,3,2,3,1,3,1,1),_LecsElanRowStatus_Type())
lecsElanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsElanRowStatus.setStatus(_A)
_LecsTlvTable_Object=MibTable
lecsTlvTable=_LecsTlvTable_Object((1,3,6,1,4,1,353,5,3,2,3,1,4))
if mibBuilder.loadTexts:lecsTlvTable.setStatus(_A)
_LecsTlvEntry_Object=MibTableRow
lecsTlvEntry=_LecsTlvEntry_Object((1,3,6,1,4,1,353,5,3,2,3,1,4,1))
lecsTlvEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:lecsTlvEntry.setStatus(_A)
_LecsTlvSelectorIndex_Type=TlvSelectorIndexType
_LecsTlvSelectorIndex_Object=MibTableColumn
lecsTlvSelectorIndex=_LecsTlvSelectorIndex_Object((1,3,6,1,4,1,353,5,3,2,3,1,4,1,1),_LecsTlvSelectorIndex_Type())
lecsTlvSelectorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsTlvSelectorIndex.setStatus(_A)
class _LecsTlvTag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_LecsTlvTag_Type.__name__=_J
_LecsTlvTag_Object=MibTableColumn
lecsTlvTag=_LecsTlvTag_Object((1,3,6,1,4,1,353,5,3,2,3,1,4,1,2),_LecsTlvTag_Type())
lecsTlvTag.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsTlvTag.setStatus(_A)
class _LecsTlvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LecsTlvIndex_Type.__name__=_F
_LecsTlvIndex_Object=MibTableColumn
lecsTlvIndex=_LecsTlvIndex_Object((1,3,6,1,4,1,353,5,3,2,3,1,4,1,3),_LecsTlvIndex_Type())
lecsTlvIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsTlvIndex.setStatus(_A)
class _LecsTlvVal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_LecsTlvVal_Type.__name__=_J
_LecsTlvVal_Object=MibTableColumn
lecsTlvVal=_LecsTlvVal_Object((1,3,6,1,4,1,353,5,3,2,3,1,4,1,4),_LecsTlvVal_Type())
lecsTlvVal.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsTlvVal.setStatus(_A)
_LecsTlvRowStatus_Type=RowStatus
_LecsTlvRowStatus_Object=MibTableColumn
lecsTlvRowStatus=_LecsTlvRowStatus_Object((1,3,6,1,4,1,353,5,3,2,3,1,4,1,5),_LecsTlvRowStatus_Type())
lecsTlvRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsTlvRowStatus.setStatus(_A)
_LecsVccTable_Object=MibTable
lecsVccTable=_LecsVccTable_Object((1,3,6,1,4,1,353,5,3,2,3,1,5))
if mibBuilder.loadTexts:lecsVccTable.setStatus(_A)
_LecsVccEntry_Object=MibTableRow
lecsVccEntry=_LecsVccEntry_Object((1,3,6,1,4,1,353,5,3,2,3,1,5,1))
lecsVccEntry.setIndexNames((0,_B,_I),(0,_B,_d),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:lecsVccEntry.setStatus(_A)
_LecsVccIfIndex_Type=IfIndexOrZero
_LecsVccIfIndex_Object=MibTableColumn
lecsVccIfIndex=_LecsVccIfIndex_Object((1,3,6,1,4,1,353,5,3,2,3,1,5,1,1),_LecsVccIfIndex_Type())
lecsVccIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsVccIfIndex.setStatus(_A)
_LecsVccVpi_Type=VpiInteger
_LecsVccVpi_Object=MibTableColumn
lecsVccVpi=_LecsVccVpi_Object((1,3,6,1,4,1,353,5,3,2,3,1,5,1,2),_LecsVccVpi_Type())
lecsVccVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsVccVpi.setStatus(_A)
_LecsVccVci_Type=VciInteger
_LecsVccVci_Object=MibTableColumn
lecsVccVci=_LecsVccVci_Object((1,3,6,1,4,1,353,5,3,2,3,1,5,1,3),_LecsVccVci_Type())
lecsVccVci.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsVccVci.setStatus(_A)
_LecsVccRowStatus_Type=RowStatus
_LecsVccRowStatus_Object=MibTableColumn
lecsVccRowStatus=_LecsVccRowStatus_Object((1,3,6,1,4,1,353,5,3,2,3,1,5,1,4),_LecsVccRowStatus_Type())
lecsVccRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsVccRowStatus.setStatus(_A)
_ElanLecsFaultGroup_ObjectIdentity=ObjectIdentity
elanLecsFaultGroup=_ElanLecsFaultGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,3,2))
_LecsErrCtlTable_Object=MibTable
lecsErrCtlTable=_LecsErrCtlTable_Object((1,3,6,1,4,1,353,5,3,2,3,2,1))
if mibBuilder.loadTexts:lecsErrCtlTable.setStatus(_A)
_LecsErrCtlEntry_Object=MibTableRow
lecsErrCtlEntry=_LecsErrCtlEntry_Object((1,3,6,1,4,1,353,5,3,2,3,2,1,1))
lecsErrCtlEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:lecsErrCtlEntry.setStatus(_A)
class _LecsErrCtlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_LecsErrCtlAdminStatus_Type.__name__=_F
_LecsErrCtlAdminStatus_Object=MibTableColumn
lecsErrCtlAdminStatus=_LecsErrCtlAdminStatus_Object((1,3,6,1,4,1,353,5,3,2,3,2,1,1,1),_LecsErrCtlAdminStatus_Type())
lecsErrCtlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsErrCtlAdminStatus.setStatus(_A)
class _LecsErrCtlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('active',2),('outOfRes',3),('failed',4),('disabled',5)))
_LecsErrCtlOperStatus_Type.__name__=_F
_LecsErrCtlOperStatus_Object=MibTableColumn
lecsErrCtlOperStatus=_LecsErrCtlOperStatus_Object((1,3,6,1,4,1,353,5,3,2,3,2,1,1,2),_LecsErrCtlOperStatus_Type())
lecsErrCtlOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsErrCtlOperStatus.setStatus(_A)
class _LecsErrCtlClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('clear',2)))
_LecsErrCtlClearLog_Type.__name__=_F
_LecsErrCtlClearLog_Object=MibTableColumn
lecsErrCtlClearLog=_LecsErrCtlClearLog_Object((1,3,6,1,4,1,353,5,3,2,3,2,1,1,3),_LecsErrCtlClearLog_Type())
lecsErrCtlClearLog.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsErrCtlClearLog.setStatus(_A)
class _LecsErrCtlMaxEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LecsErrCtlMaxEntries_Type.__name__=_F
_LecsErrCtlMaxEntries_Object=MibTableColumn
lecsErrCtlMaxEntries=_LecsErrCtlMaxEntries_Object((1,3,6,1,4,1,353,5,3,2,3,2,1,1,4),_LecsErrCtlMaxEntries_Type())
lecsErrCtlMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsErrCtlMaxEntries.setStatus(_A)
_LecsErrCtlLastEntry_Type=LecsErrLogIndexType
_LecsErrCtlLastEntry_Object=MibTableColumn
lecsErrCtlLastEntry=_LecsErrCtlLastEntry_Object((1,3,6,1,4,1,353,5,3,2,3,2,1,1,5),_LecsErrCtlLastEntry_Type())
lecsErrCtlLastEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsErrCtlLastEntry.setStatus(_A)
_LecsErrLogTable_Object=MibTable
lecsErrLogTable=_LecsErrLogTable_Object((1,3,6,1,4,1,353,5,3,2,3,2,2))
if mibBuilder.loadTexts:lecsErrLogTable.setStatus(_A)
_LecsErrLogEntry_Object=MibTableRow
lecsErrLogEntry=_LecsErrLogEntry_Object((1,3,6,1,4,1,353,5,3,2,3,2,2,1))
lecsErrLogEntry.setIndexNames((0,_B,_I),(0,_B,_g))
if mibBuilder.loadTexts:lecsErrLogEntry.setStatus(_A)
_LecsErrLogIndex_Type=LecsErrLogIndexType
_LecsErrLogIndex_Object=MibTableColumn
lecsErrLogIndex=_LecsErrLogIndex_Object((1,3,6,1,4,1,353,5,3,2,3,2,2,1,1),_LecsErrLogIndex_Type())
lecsErrLogIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lecsErrLogIndex.setStatus(_A)
_LecsErrLogAtmAddr_Type=AtmLaneAddress
_LecsErrLogAtmAddr_Object=MibTableColumn
lecsErrLogAtmAddr=_LecsErrLogAtmAddr_Object((1,3,6,1,4,1,353,5,3,2,3,2,2,1,2),_LecsErrLogAtmAddr_Type())
lecsErrLogAtmAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsErrLogAtmAddr.setStatus(_A)
class _LecsErrLogErrCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,22))
_LecsErrLogErrCode_Type.__name__=_F
_LecsErrLogErrCode_Object=MibTableColumn
lecsErrLogErrCode=_LecsErrLogErrCode_Object((1,3,6,1,4,1,353,5,3,2,3,2,2,1,3),_LecsErrLogErrCode_Type())
lecsErrLogErrCode.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsErrLogErrCode.setStatus(_A)
_LecsErrLogTime_Type=TIMESTAMP
_LecsErrLogTime_Object=MibTableColumn
lecsErrLogTime=_LecsErrLogTime_Object((1,3,6,1,4,1,353,5,3,2,3,2,2,1,4),_LecsErrLogTime_Type())
lecsErrLogTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsErrLogTime.setStatus(_A)
_ElanLecsStatGroup_ObjectIdentity=ObjectIdentity
elanLecsStatGroup=_ElanLecsStatGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,2,3,3))
_LecsStatsTable_Object=MibTable
lecsStatsTable=_LecsStatsTable_Object((1,3,6,1,4,1,353,5,3,2,3,3,1))
if mibBuilder.loadTexts:lecsStatsTable.setStatus(_A)
_LecsStatsEntry_Object=MibTableRow
lecsStatsEntry=_LecsStatsEntry_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1))
lecsStatsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:lecsStatsEntry.setStatus(_A)
_LecsStatSuccessful_Type=Counter32
_LecsStatSuccessful_Object=MibTableColumn
lecsStatSuccessful=_LecsStatSuccessful_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,1),_LecsStatSuccessful_Type())
lecsStatSuccessful.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatSuccessful.setStatus(_A)
_LecsStatInBadFrames_Type=Counter32
_LecsStatInBadFrames_Object=MibTableColumn
lecsStatInBadFrames=_LecsStatInBadFrames_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,2),_LecsStatInBadFrames_Type())
lecsStatInBadFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInBadFrames.setStatus(_A)
_LecsStatInvalidParam_Type=Counter32
_LecsStatInvalidParam_Object=MibTableColumn
lecsStatInvalidParam=_LecsStatInvalidParam_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,3),_LecsStatInvalidParam_Type())
lecsStatInvalidParam.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInvalidParam.setStatus(_A)
_LecsStatInsufRes_Type=Counter32
_LecsStatInsufRes_Object=MibTableColumn
lecsStatInsufRes=_LecsStatInsufRes_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,4),_LecsStatInsufRes_Type())
lecsStatInsufRes.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInsufRes.setStatus(_A)
_LecsStatAccDenied_Type=Counter32
_LecsStatAccDenied_Object=MibTableColumn
lecsStatAccDenied=_LecsStatAccDenied_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,5),_LecsStatAccDenied_Type())
lecsStatAccDenied.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatAccDenied.setStatus(_A)
_LecsStatInvalidReq_Type=Counter32
_LecsStatInvalidReq_Object=MibTableColumn
lecsStatInvalidReq=_LecsStatInvalidReq_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,6),_LecsStatInvalidReq_Type())
lecsStatInvalidReq.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInvalidReq.setStatus(_A)
_LecsStatInvalidDest_Type=Counter32
_LecsStatInvalidDest_Object=MibTableColumn
lecsStatInvalidDest=_LecsStatInvalidDest_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,7),_LecsStatInvalidDest_Type())
lecsStatInvalidDest.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInvalidDest.setStatus(_A)
_LecsStatInvalidAddr_Type=Counter32
_LecsStatInvalidAddr_Object=MibTableColumn
lecsStatInvalidAddr=_LecsStatInvalidAddr_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,8),_LecsStatInvalidAddr_Type())
lecsStatInvalidAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInvalidAddr.setStatus(_A)
_LecsStatNoConf_Type=Counter32
_LecsStatNoConf_Object=MibTableColumn
lecsStatNoConf=_LecsStatNoConf_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,9),_LecsStatNoConf_Type())
lecsStatNoConf.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatNoConf.setStatus(_A)
_LecsStatConfError_Type=Counter32
_LecsStatConfError_Object=MibTableColumn
lecsStatConfError=_LecsStatConfError_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,10),_LecsStatConfError_Type())
lecsStatConfError.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatConfError.setStatus(_A)
_LecsStatInsufInfo_Type=Counter32
_LecsStatInsufInfo_Object=MibTableColumn
lecsStatInsufInfo=_LecsStatInsufInfo_Object((1,3,6,1,4,1,353,5,3,2,3,3,1,1,11),_LecsStatInsufInfo_Type())
lecsStatInsufInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsStatInsufInfo.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:Integer,'RowStatus':RowStatus,'AutonomousType':AutonomousType,'TIMESTAMP':TIMESTAMP,_L:AtmLaneAddress,'MacAddress':MacAddress,_Y:IfIndexOrZero,'ElanLocalIndex':ElanLocalIndex,_Z:AtmLaneMask,'TlvSelectorIndexType':TlvSelectorIndexType,'PolicySelectorIndexType':PolicySelectorIndexType,'LecsErrLogIndexType':LecsErrLogIndexType,'elanMIB':elanMIB,'elanAdminGroup':elanAdminGroup,'elanAdminPolicyVal':elanAdminPolicyVal,'byAtmAddr':byAtmAddr,'byMacAddr':byMacAddr,'byRouteDescriptor':byRouteDescriptor,'byLanType':byLanType,'byPktSize':byPktSize,'byElanName':byElanName,'elanConfGroup':elanConfGroup,'elanConfNextId':elanConfNextId,'elanConfTable':elanConfTable,'elanConfEntry':elanConfEntry,_G:elanConfIndex,'elanConfName':elanConfName,'elanConfTlvIndex':elanConfTlvIndex,'elanConfLanType':elanConfLanType,'elanConfMaxFrameSize':elanConfMaxFrameSize,'elanConfRowStatus':elanConfRowStatus,'elanLesTable':elanLesTable,'elanLesEntry':elanLesEntry,_H:elanLesIndex,'elanLesAtmAddress':elanLesAtmAddress,'elanLesRowStatus':elanLesRowStatus,'elanPolicyTable':elanPolicyTable,'elanPolicyEntry':elanPolicyEntry,_P:elanPolicySelectorIndex,_Q:elanPolicyIndex,'elanPolicyPriority':elanPolicyPriority,'elanPolicyType':elanPolicyType,'elanPolicyRowStatus':elanPolicyRowStatus,'elanLecAtmAddrTable':elanLecAtmAddrTable,'elanLecAtmAddrEntry':elanLecAtmAddrEntry,_R:elanLecAtmAddress,_S:elanLecAtmMask,'elanLecAtmRowStatus':elanLecAtmRowStatus,'elanLecMacAddrTable':elanLecMacAddrTable,'elanLecMacAddrEntry':elanLecMacAddrEntry,_T:elanLecMacAddress,'elanLecMacRowStatus':elanLecMacRowStatus,'elanLecRdTable':elanLecRdTable,'elanLecRdEntry':elanLecRdEntry,_U:elanLecRdSegId,_V:elanLecRdBridgeNum,'elanLecRdRowStatus':elanLecRdRowStatus,'elanLecPktSizeTable':elanLecPktSizeTable,'elanLecPktSizeEntry':elanLecPktSizeEntry,_W:elanLecFrameSize,'elanLecPktSizeRowStatus':elanLecPktSizeRowStatus,'elanLecNameTable':elanLecNameTable,'elanLecNameEntry':elanLecNameEntry,_X:elanLecElanName,'elanLecNameRowStatus':elanLecNameRowStatus,'elanLecsGroup':elanLecsGroup,'elanLecsConfGroup':elanLecsConfGroup,'lecsConfNextId':lecsConfNextId,'lecsConfTable':lecsConfTable,'lecsConfEntry':lecsConfEntry,_I:lecsConfIndex,'lecsAtmIfIndex':lecsAtmIfIndex,'lecsAtmAddrSpec':lecsAtmAddrSpec,'lecsAtmAddrMask':lecsAtmAddrMask,'lecsAtmAddrActual':lecsAtmAddrActual,'lecsPolicySelIndex':lecsPolicySelIndex,'lecsLastInitialized':lecsLastInitialized,'lecsOperStatus':lecsOperStatus,'lecsAdminStatus':lecsAdminStatus,'lecsRowStatus':lecsRowStatus,'lecsElanTable':lecsElanTable,'lecsElanEntry':lecsElanEntry,'lecsElanRowStatus':lecsElanRowStatus,'lecsTlvTable':lecsTlvTable,'lecsTlvEntry':lecsTlvEntry,_a:lecsTlvSelectorIndex,_b:lecsTlvTag,_c:lecsTlvIndex,'lecsTlvVal':lecsTlvVal,'lecsTlvRowStatus':lecsTlvRowStatus,'lecsVccTable':lecsVccTable,'lecsVccEntry':lecsVccEntry,_d:lecsVccIfIndex,_e:lecsVccVpi,_f:lecsVccVci,'lecsVccRowStatus':lecsVccRowStatus,'elanLecsFaultGroup':elanLecsFaultGroup,'lecsErrCtlTable':lecsErrCtlTable,'lecsErrCtlEntry':lecsErrCtlEntry,'lecsErrCtlAdminStatus':lecsErrCtlAdminStatus,'lecsErrCtlOperStatus':lecsErrCtlOperStatus,'lecsErrCtlClearLog':lecsErrCtlClearLog,'lecsErrCtlMaxEntries':lecsErrCtlMaxEntries,'lecsErrCtlLastEntry':lecsErrCtlLastEntry,'lecsErrLogTable':lecsErrLogTable,'lecsErrLogEntry':lecsErrLogEntry,_g:lecsErrLogIndex,'lecsErrLogAtmAddr':lecsErrLogAtmAddr,'lecsErrLogErrCode':lecsErrLogErrCode,'lecsErrLogTime':lecsErrLogTime,'elanLecsStatGroup':elanLecsStatGroup,'lecsStatsTable':lecsStatsTable,'lecsStatsEntry':lecsStatsEntry,'lecsStatSuccessful':lecsStatSuccessful,'lecsStatInBadFrames':lecsStatInBadFrames,'lecsStatInvalidParam':lecsStatInvalidParam,'lecsStatInsufRes':lecsStatInsufRes,'lecsStatAccDenied':lecsStatAccDenied,'lecsStatInvalidReq':lecsStatInvalidReq,'lecsStatInvalidDest':lecsStatInvalidDest,'lecsStatInvalidAddr':lecsStatInvalidAddr,'lecsStatNoConf':lecsStatNoConf,'lecsStatConfError':lecsStatConfError,'lecsStatInsufInfo':lecsStatInsufInfo})