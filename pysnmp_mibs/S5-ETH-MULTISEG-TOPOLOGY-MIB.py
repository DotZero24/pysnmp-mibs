_b='s5EnMsTopPortIfIndex'
_a='s5EnMsTopSrcMacAddr'
_Z='standby'
_Y='active'
_X='heartbeat'
_W='topChanged'
_V='read-write'
_U='s5EnMsTopBdgIpAddr'
_T='s5EnMsTopBdgPortNum'
_S='s5EnMsTopBdgSlotNum'
_R='s5EnMsTopNmmEnhancedSegId'
_Q='s5EnMsTopNmmEnhancedIpAddr'
_P='s5EnMsTopNmmEnhancedSubPort'
_O='s5EnMsTopNmmEnhancedPort'
_N='s5EnMsTopNmmEnhancedSlot'
_M='s5EnMsTopNmmSegId'
_L='s5EnMsTopNmmIpAddr'
_K='s5EnMsTopNmmPort'
_J='s5EnMsTopNmmSlot'
_I='other'
_H='OctetString'
_G='not-accessible'
_F='mandatory'
_E='current'
_D='S5-ETH-MULTISEG-TOPOLOGY-MIB'
_C='deprecated'
_B='Integer32'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
s5EnMsTop,=mibBuilder.importSymbols('S5-ROOT-MIB','s5EnMsTop')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
SnpxBackplaneType,SnpxChassisType=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','SnpxBackplaneType','SnpxChassisType')
s5EthMultisegTopologyMib=ModuleIdentity((1,3,6,1,4,1,45,1,6,13,0))
if mibBuilder.loadTexts:s5EthMultisegTopologyMib.setRevisions(('2009-08-18 00:00','2006-09-13 00:00','2006-09-12 00:00','2004-07-20 00:00'))
_S5EnMsTopInfo_ObjectIdentity=ObjectIdentity
s5EnMsTopInfo=_S5EnMsTopInfo_ObjectIdentity((1,3,6,1,4,1,45,1,6,13,1))
_S5EnMsTopIpAddr_Type=IpAddress
_S5EnMsTopIpAddr_Object=MibScalar
s5EnMsTopIpAddr=_S5EnMsTopIpAddr_Object((1,3,6,1,4,1,45,1,6,13,1,1),_S5EnMsTopIpAddr_Type())
s5EnMsTopIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopIpAddr.setStatus(_E)
class _S5EnMsTopStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('topOn',1),('topOff',2)))
_S5EnMsTopStatus_Type.__name__=_B
_S5EnMsTopStatus_Object=MibScalar
s5EnMsTopStatus=_S5EnMsTopStatus_Object((1,3,6,1,4,1,45,1,6,13,1,2),_S5EnMsTopStatus_Type())
s5EnMsTopStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:s5EnMsTopStatus.setStatus(_E)
_S5EnMsTopNmmLstChg_Type=TimeTicks
_S5EnMsTopNmmLstChg_Object=MibScalar
s5EnMsTopNmmLstChg=_S5EnMsTopNmmLstChg_Object((1,3,6,1,4,1,45,1,6,13,1,3),_S5EnMsTopNmmLstChg_Type())
s5EnMsTopNmmLstChg.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmLstChg.setStatus(_E)
_S5EnMsTopBdgLstChg_Type=TimeTicks
_S5EnMsTopBdgLstChg_Object=MibScalar
s5EnMsTopBdgLstChg=_S5EnMsTopBdgLstChg_Object((1,3,6,1,4,1,45,1,6,13,1,4),_S5EnMsTopBdgLstChg_Type())
s5EnMsTopBdgLstChg.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgLstChg.setStatus(_C)
class _S5EnMsTopNmmMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5EnMsTopNmmMaxNum_Type.__name__=_B
_S5EnMsTopNmmMaxNum_Object=MibScalar
s5EnMsTopNmmMaxNum=_S5EnMsTopNmmMaxNum_Object((1,3,6,1,4,1,45,1,6,13,1,5),_S5EnMsTopNmmMaxNum_Type())
s5EnMsTopNmmMaxNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmMaxNum.setStatus(_E)
class _S5EnMsTopNmmCurNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5EnMsTopNmmCurNum_Type.__name__=_B
_S5EnMsTopNmmCurNum_Object=MibScalar
s5EnMsTopNmmCurNum=_S5EnMsTopNmmCurNum_Object((1,3,6,1,4,1,45,1,6,13,1,6),_S5EnMsTopNmmCurNum_Type())
s5EnMsTopNmmCurNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmCurNum.setStatus(_E)
class _S5EnMsTopBdgMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5EnMsTopBdgMaxNum_Type.__name__=_B
_S5EnMsTopBdgMaxNum_Object=MibScalar
s5EnMsTopBdgMaxNum=_S5EnMsTopBdgMaxNum_Object((1,3,6,1,4,1,45,1,6,13,1,7),_S5EnMsTopBdgMaxNum_Type())
s5EnMsTopBdgMaxNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgMaxNum.setStatus(_C)
class _S5EnMsTopBdgCurNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5EnMsTopBdgCurNum_Type.__name__=_B
_S5EnMsTopBdgCurNum_Object=MibScalar
s5EnMsTopBdgCurNum=_S5EnMsTopBdgCurNum_Object((1,3,6,1,4,1,45,1,6,13,1,8),_S5EnMsTopBdgCurNum_Type())
s5EnMsTopBdgCurNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgCurNum.setStatus(_C)
_S5EnMsTopNmm_ObjectIdentity=ObjectIdentity
s5EnMsTopNmm=_S5EnMsTopNmm_ObjectIdentity((1,3,6,1,4,1,45,1,6,13,2))
_S5EnMsTopNmmTable_Object=MibTable
s5EnMsTopNmmTable=_S5EnMsTopNmmTable_Object((1,3,6,1,4,1,45,1,6,13,2,1))
if mibBuilder.loadTexts:s5EnMsTopNmmTable.setStatus(_E)
_S5EnMsTopNmmEntry_Object=MibTableRow
s5EnMsTopNmmEntry=_S5EnMsTopNmmEntry_Object((1,3,6,1,4,1,45,1,6,13,2,1,1))
s5EnMsTopNmmEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:s5EnMsTopNmmEntry.setStatus(_E)
class _S5EnMsTopNmmSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopNmmSlot_Type.__name__=_B
_S5EnMsTopNmmSlot_Object=MibTableColumn
s5EnMsTopNmmSlot=_S5EnMsTopNmmSlot_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,1),_S5EnMsTopNmmSlot_Type())
s5EnMsTopNmmSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmSlot.setStatus(_E)
class _S5EnMsTopNmmPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopNmmPort_Type.__name__=_B
_S5EnMsTopNmmPort_Object=MibTableColumn
s5EnMsTopNmmPort=_S5EnMsTopNmmPort_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,2),_S5EnMsTopNmmPort_Type())
s5EnMsTopNmmPort.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmPort.setStatus(_E)
_S5EnMsTopNmmIpAddr_Type=IpAddress
_S5EnMsTopNmmIpAddr_Object=MibTableColumn
s5EnMsTopNmmIpAddr=_S5EnMsTopNmmIpAddr_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,3),_S5EnMsTopNmmIpAddr_Type())
s5EnMsTopNmmIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmIpAddr.setStatus(_E)
class _S5EnMsTopNmmSegId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_S5EnMsTopNmmSegId_Type.__name__=_B
_S5EnMsTopNmmSegId_Object=MibTableColumn
s5EnMsTopNmmSegId=_S5EnMsTopNmmSegId_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,4),_S5EnMsTopNmmSegId_Type())
s5EnMsTopNmmSegId.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmSegId.setStatus(_E)
_S5EnMsTopNmmMacAddr_Type=MacAddress
_S5EnMsTopNmmMacAddr_Object=MibTableColumn
s5EnMsTopNmmMacAddr=_S5EnMsTopNmmMacAddr_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,5),_S5EnMsTopNmmMacAddr_Type())
s5EnMsTopNmmMacAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmMacAddr.setStatus(_E)
_S5EnMsTopNmmChassisType_Type=SnpxChassisType
_S5EnMsTopNmmChassisType_Object=MibTableColumn
s5EnMsTopNmmChassisType=_S5EnMsTopNmmChassisType_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,6),_S5EnMsTopNmmChassisType_Type())
s5EnMsTopNmmChassisType.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmChassisType.setStatus(_E)
_S5EnMsTopNmmBkplType_Type=SnpxBackplaneType
_S5EnMsTopNmmBkplType_Object=MibTableColumn
s5EnMsTopNmmBkplType=_S5EnMsTopNmmBkplType_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,7),_S5EnMsTopNmmBkplType_Type())
s5EnMsTopNmmBkplType.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmBkplType.setStatus(_E)
class _S5EnMsTopNmmLocalSeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_S5EnMsTopNmmLocalSeg_Type.__name__=_B
_S5EnMsTopNmmLocalSeg_Object=MibTableColumn
s5EnMsTopNmmLocalSeg=_S5EnMsTopNmmLocalSeg_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,8),_S5EnMsTopNmmLocalSeg_Type())
s5EnMsTopNmmLocalSeg.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmLocalSeg.setStatus(_E)
class _S5EnMsTopNmmCurState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),('new',3)))
_S5EnMsTopNmmCurState_Type.__name__=_B
_S5EnMsTopNmmCurState_Object=MibTableColumn
s5EnMsTopNmmCurState=_S5EnMsTopNmmCurState_Object((1,3,6,1,4,1,45,1,6,13,2,1,1,9),_S5EnMsTopNmmCurState_Type())
s5EnMsTopNmmCurState.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmCurState.setStatus(_E)
class _S5EnMsTopNmmEosSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_S5EnMsTopNmmEosSize_Type.__name__=_B
_S5EnMsTopNmmEosSize_Object=MibScalar
s5EnMsTopNmmEosSize=_S5EnMsTopNmmEosSize_Object((1,3,6,1,4,1,45,1,6,13,2,2),_S5EnMsTopNmmEosSize_Type())
s5EnMsTopNmmEosSize.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEosSize.setStatus(_E)
_S5EnMsTopNmmEosTable_Object=MibTable
s5EnMsTopNmmEosTable=_S5EnMsTopNmmEosTable_Object((1,3,6,1,4,1,45,1,6,13,2,3))
if mibBuilder.loadTexts:s5EnMsTopNmmEosTable.setStatus(_E)
_S5EnMsTopNmmEosEntry_Object=MibTableRow
s5EnMsTopNmmEosEntry=_S5EnMsTopNmmEosEntry_Object((1,3,6,1,4,1,45,1,6,13,2,3,1))
s5EnMsTopNmmEosEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:s5EnMsTopNmmEosEntry.setStatus(_E)
class _S5EnMsTopNmmEos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1400))
_S5EnMsTopNmmEos_Type.__name__=_H
_S5EnMsTopNmmEos_Object=MibTableColumn
s5EnMsTopNmmEos=_S5EnMsTopNmmEos_Object((1,3,6,1,4,1,45,1,6,13,2,3,1,1),_S5EnMsTopNmmEos_Type())
s5EnMsTopNmmEos.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEos.setStatus(_E)
_S5EnMsTopNmmEnhancedTable_Object=MibTable
s5EnMsTopNmmEnhancedTable=_S5EnMsTopNmmEnhancedTable_Object((1,3,6,1,4,1,45,1,6,13,2,4))
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedTable.setStatus(_F)
_S5EnMsTopNmmEnhancedEntry_Object=MibTableRow
s5EnMsTopNmmEnhancedEntry=_S5EnMsTopNmmEnhancedEntry_Object((1,3,6,1,4,1,45,1,6,13,2,4,1))
s5EnMsTopNmmEnhancedEntry.setIndexNames((0,_D,_N),(0,_D,_O),(0,_D,_P),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedEntry.setStatus(_F)
class _S5EnMsTopNmmEnhancedSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopNmmEnhancedSlot_Type.__name__=_B
_S5EnMsTopNmmEnhancedSlot_Object=MibTableColumn
s5EnMsTopNmmEnhancedSlot=_S5EnMsTopNmmEnhancedSlot_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,1),_S5EnMsTopNmmEnhancedSlot_Type())
s5EnMsTopNmmEnhancedSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedSlot.setStatus(_F)
class _S5EnMsTopNmmEnhancedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopNmmEnhancedPort_Type.__name__=_B
_S5EnMsTopNmmEnhancedPort_Object=MibTableColumn
s5EnMsTopNmmEnhancedPort=_S5EnMsTopNmmEnhancedPort_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,2),_S5EnMsTopNmmEnhancedPort_Type())
s5EnMsTopNmmEnhancedPort.setMaxAccess(_G)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedPort.setStatus(_F)
class _S5EnMsTopNmmEnhancedSubPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_S5EnMsTopNmmEnhancedSubPort_Type.__name__=_B
_S5EnMsTopNmmEnhancedSubPort_Object=MibTableColumn
s5EnMsTopNmmEnhancedSubPort=_S5EnMsTopNmmEnhancedSubPort_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,3),_S5EnMsTopNmmEnhancedSubPort_Type())
s5EnMsTopNmmEnhancedSubPort.setMaxAccess(_G)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedSubPort.setStatus(_F)
_S5EnMsTopNmmEnhancedIpAddr_Type=IpAddress
_S5EnMsTopNmmEnhancedIpAddr_Object=MibTableColumn
s5EnMsTopNmmEnhancedIpAddr=_S5EnMsTopNmmEnhancedIpAddr_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,4),_S5EnMsTopNmmEnhancedIpAddr_Type())
s5EnMsTopNmmEnhancedIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedIpAddr.setStatus(_F)
class _S5EnMsTopNmmEnhancedSegId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_S5EnMsTopNmmEnhancedSegId_Type.__name__=_B
_S5EnMsTopNmmEnhancedSegId_Object=MibTableColumn
s5EnMsTopNmmEnhancedSegId=_S5EnMsTopNmmEnhancedSegId_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,5),_S5EnMsTopNmmEnhancedSegId_Type())
s5EnMsTopNmmEnhancedSegId.setMaxAccess(_G)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedSegId.setStatus(_F)
_S5EnMsTopNmmEnhancedMacAddr_Type=MacAddress
_S5EnMsTopNmmEnhancedMacAddr_Object=MibTableColumn
s5EnMsTopNmmEnhancedMacAddr=_S5EnMsTopNmmEnhancedMacAddr_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,6),_S5EnMsTopNmmEnhancedMacAddr_Type())
s5EnMsTopNmmEnhancedMacAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedMacAddr.setStatus(_F)
_S5EnMsTopNmmEnhancedChassisType_Type=SnpxChassisType
_S5EnMsTopNmmEnhancedChassisType_Object=MibTableColumn
s5EnMsTopNmmEnhancedChassisType=_S5EnMsTopNmmEnhancedChassisType_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,7),_S5EnMsTopNmmEnhancedChassisType_Type())
s5EnMsTopNmmEnhancedChassisType.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedChassisType.setStatus(_F)
_S5EnMsTopNmmEnhancedBkplType_Type=SnpxBackplaneType
_S5EnMsTopNmmEnhancedBkplType_Object=MibTableColumn
s5EnMsTopNmmEnhancedBkplType=_S5EnMsTopNmmEnhancedBkplType_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,8),_S5EnMsTopNmmEnhancedBkplType_Type())
s5EnMsTopNmmEnhancedBkplType.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedBkplType.setStatus(_F)
class _S5EnMsTopNmmEnhancedLocalSeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_S5EnMsTopNmmEnhancedLocalSeg_Type.__name__=_B
_S5EnMsTopNmmEnhancedLocalSeg_Object=MibTableColumn
s5EnMsTopNmmEnhancedLocalSeg=_S5EnMsTopNmmEnhancedLocalSeg_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,9),_S5EnMsTopNmmEnhancedLocalSeg_Type())
s5EnMsTopNmmEnhancedLocalSeg.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedLocalSeg.setStatus(_F)
class _S5EnMsTopNmmEnhancedCurState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),('new',3)))
_S5EnMsTopNmmEnhancedCurState_Type.__name__=_B
_S5EnMsTopNmmEnhancedCurState_Object=MibTableColumn
s5EnMsTopNmmEnhancedCurState=_S5EnMsTopNmmEnhancedCurState_Object((1,3,6,1,4,1,45,1,6,13,2,4,1,10),_S5EnMsTopNmmEnhancedCurState_Type())
s5EnMsTopNmmEnhancedCurState.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedCurState.setStatus(_F)
_S5EnMsTopNmmEnhancedEosTable_Object=MibTable
s5EnMsTopNmmEnhancedEosTable=_S5EnMsTopNmmEnhancedEosTable_Object((1,3,6,1,4,1,45,1,6,13,2,5))
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedEosTable.setStatus(_F)
_S5EnMsTopNmmEnhancedEosEntry_Object=MibTableRow
s5EnMsTopNmmEnhancedEosEntry=_S5EnMsTopNmmEnhancedEosEntry_Object((1,3,6,1,4,1,45,1,6,13,2,5,1))
s5EnMsTopNmmEnhancedEosEntry.setIndexNames((0,_D,_N),(0,_D,_O),(0,_D,_P),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedEosEntry.setStatus(_F)
class _S5EnMsTopNmmEnhancedEos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1400))
_S5EnMsTopNmmEnhancedEos_Type.__name__=_H
_S5EnMsTopNmmEnhancedEos_Object=MibTableColumn
s5EnMsTopNmmEnhancedEos=_S5EnMsTopNmmEnhancedEos_Object((1,3,6,1,4,1,45,1,6,13,2,5,1,1),_S5EnMsTopNmmEnhancedEos_Type())
s5EnMsTopNmmEnhancedEos.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopNmmEnhancedEos.setStatus(_F)
_S5EnMsTopBdg_ObjectIdentity=ObjectIdentity
s5EnMsTopBdg=_S5EnMsTopBdg_ObjectIdentity((1,3,6,1,4,1,45,1,6,13,3))
_S5EnMsTopBdgTable_Object=MibTable
s5EnMsTopBdgTable=_S5EnMsTopBdgTable_Object((1,3,6,1,4,1,45,1,6,13,3,1))
if mibBuilder.loadTexts:s5EnMsTopBdgTable.setStatus(_C)
_S5EnMsTopBdgEntry_Object=MibTableRow
s5EnMsTopBdgEntry=_S5EnMsTopBdgEntry_Object((1,3,6,1,4,1,45,1,6,13,3,1,1))
s5EnMsTopBdgEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:s5EnMsTopBdgEntry.setStatus(_C)
class _S5EnMsTopBdgSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopBdgSlotNum_Type.__name__=_B
_S5EnMsTopBdgSlotNum_Object=MibTableColumn
s5EnMsTopBdgSlotNum=_S5EnMsTopBdgSlotNum_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,1),_S5EnMsTopBdgSlotNum_Type())
s5EnMsTopBdgSlotNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgSlotNum.setStatus(_C)
class _S5EnMsTopBdgPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopBdgPortNum_Type.__name__=_B
_S5EnMsTopBdgPortNum_Object=MibTableColumn
s5EnMsTopBdgPortNum=_S5EnMsTopBdgPortNum_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,2),_S5EnMsTopBdgPortNum_Type())
s5EnMsTopBdgPortNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgPortNum.setStatus(_C)
_S5EnMsTopBdgIpAddr_Type=IpAddress
_S5EnMsTopBdgIpAddr_Object=MibTableColumn
s5EnMsTopBdgIpAddr=_S5EnMsTopBdgIpAddr_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,3),_S5EnMsTopBdgIpAddr_Type())
s5EnMsTopBdgIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgIpAddr.setStatus(_C)
class _S5EnMsTopBdgNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5EnMsTopBdgNumber_Type.__name__=_B
_S5EnMsTopBdgNumber_Object=MibTableColumn
s5EnMsTopBdgNumber=_S5EnMsTopBdgNumber_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,4),_S5EnMsTopBdgNumber_Type())
s5EnMsTopBdgNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgNumber.setStatus(_C)
_S5EnMsTopBdgMacAddr_Type=MacAddress
_S5EnMsTopBdgMacAddr_Object=MibTableColumn
s5EnMsTopBdgMacAddr=_S5EnMsTopBdgMacAddr_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,5),_S5EnMsTopBdgMacAddr_Type())
s5EnMsTopBdgMacAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgMacAddr.setStatus(_C)
class _S5EnMsTopBdgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('localSyn',2),('remoteSyn',3),('kalpana',4)))
_S5EnMsTopBdgType_Type.__name__=_B
_S5EnMsTopBdgType_Object=MibTableColumn
s5EnMsTopBdgType=_S5EnMsTopBdgType_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,6),_S5EnMsTopBdgType_Type())
s5EnMsTopBdgType.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgType.setStatus(_C)
_S5EnMsTopBdgNumPorts_Type=Integer32
_S5EnMsTopBdgNumPorts_Object=MibTableColumn
s5EnMsTopBdgNumPorts=_S5EnMsTopBdgNumPorts_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,7),_S5EnMsTopBdgNumPorts_Type())
s5EnMsTopBdgNumPorts.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgNumPorts.setStatus(_C)
class _S5EnMsTopBdgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_Y,2),(_Z,3)))
_S5EnMsTopBdgStatus_Type.__name__=_B
_S5EnMsTopBdgStatus_Object=MibTableColumn
s5EnMsTopBdgStatus=_S5EnMsTopBdgStatus_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,8),_S5EnMsTopBdgStatus_Type())
s5EnMsTopBdgStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgStatus.setStatus(_C)
class _S5EnMsTopBdgHelloPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_S5EnMsTopBdgHelloPortNum_Type.__name__=_B
_S5EnMsTopBdgHelloPortNum_Object=MibTableColumn
s5EnMsTopBdgHelloPortNum=_S5EnMsTopBdgHelloPortNum_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,9),_S5EnMsTopBdgHelloPortNum_Type())
s5EnMsTopBdgHelloPortNum.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgHelloPortNum.setStatus(_C)
class _S5EnMsTopBdgHelloPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('eth',2),('tok4',3),('tok16',4),('fddi',5),('t1',6)))
_S5EnMsTopBdgHelloPortType_Type.__name__=_B
_S5EnMsTopBdgHelloPortType_Object=MibTableColumn
s5EnMsTopBdgHelloPortType=_S5EnMsTopBdgHelloPortType_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,10),_S5EnMsTopBdgHelloPortType_Type())
s5EnMsTopBdgHelloPortType.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgHelloPortType.setStatus(_C)
class _S5EnMsTopBdgHelloPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_Y,2),(_Z,3)))
_S5EnMsTopBdgHelloPortStatus_Type.__name__=_B
_S5EnMsTopBdgHelloPortStatus_Object=MibTableColumn
s5EnMsTopBdgHelloPortStatus=_S5EnMsTopBdgHelloPortStatus_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,11),_S5EnMsTopBdgHelloPortStatus_Type())
s5EnMsTopBdgHelloPortStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgHelloPortStatus.setStatus(_C)
_S5EnMsTopBdgCompBdgMac1_Type=MacAddress
_S5EnMsTopBdgCompBdgMac1_Object=MibTableColumn
s5EnMsTopBdgCompBdgMac1=_S5EnMsTopBdgCompBdgMac1_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,12),_S5EnMsTopBdgCompBdgMac1_Type())
s5EnMsTopBdgCompBdgMac1.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgCompBdgMac1.setStatus(_C)
_S5EnMsTopBdgCompBdgMac2_Type=MacAddress
_S5EnMsTopBdgCompBdgMac2_Object=MibTableColumn
s5EnMsTopBdgCompBdgMac2=_S5EnMsTopBdgCompBdgMac2_Object((1,3,6,1,4,1,45,1,6,13,3,1,1,13),_S5EnMsTopBdgCompBdgMac2_Type())
s5EnMsTopBdgCompBdgMac2.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgCompBdgMac2.setStatus(_C)
class _S5EnMsTopBdgEosSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_S5EnMsTopBdgEosSize_Type.__name__=_B
_S5EnMsTopBdgEosSize_Object=MibScalar
s5EnMsTopBdgEosSize=_S5EnMsTopBdgEosSize_Object((1,3,6,1,4,1,45,1,6,13,3,2),_S5EnMsTopBdgEosSize_Type())
s5EnMsTopBdgEosSize.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgEosSize.setStatus(_C)
_S5EnMsTopBdgEosTable_Object=MibTable
s5EnMsTopBdgEosTable=_S5EnMsTopBdgEosTable_Object((1,3,6,1,4,1,45,1,6,13,3,3))
if mibBuilder.loadTexts:s5EnMsTopBdgEosTable.setStatus(_C)
_S5EnMsTopBdgEosEntry_Object=MibTableRow
s5EnMsTopBdgEosEntry=_S5EnMsTopBdgEosEntry_Object((1,3,6,1,4,1,45,1,6,13,3,3,1))
s5EnMsTopBdgEosEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:s5EnMsTopBdgEosEntry.setStatus(_C)
class _S5EnMsTopBdgEos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1400))
_S5EnMsTopBdgEos_Type.__name__=_H
_S5EnMsTopBdgEos_Object=MibTableColumn
s5EnMsTopBdgEos=_S5EnMsTopBdgEos_Object((1,3,6,1,4,1,45,1,6,13,3,3,1,1),_S5EnMsTopBdgEos_Type())
s5EnMsTopBdgEos.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopBdgEos.setStatus(_C)
_S5EnMsTopSrcMac_ObjectIdentity=ObjectIdentity
s5EnMsTopSrcMac=_S5EnMsTopSrcMac_ObjectIdentity((1,3,6,1,4,1,45,1,6,13,4))
_S5EnMsTopSrcMacAddrTable_Object=MibTable
s5EnMsTopSrcMacAddrTable=_S5EnMsTopSrcMacAddrTable_Object((1,3,6,1,4,1,45,1,6,13,4,1))
if mibBuilder.loadTexts:s5EnMsTopSrcMacAddrTable.setStatus(_C)
_S5EnMsTopSrcMacAddrEntry_Object=MibTableRow
s5EnMsTopSrcMacAddrEntry=_S5EnMsTopSrcMacAddrEntry_Object((1,3,6,1,4,1,45,1,6,13,4,1,1))
s5EnMsTopSrcMacAddrEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:s5EnMsTopSrcMacAddrEntry.setStatus(_C)
_S5EnMsTopSrcMacAddr_Type=MacAddress
_S5EnMsTopSrcMacAddr_Object=MibTableColumn
s5EnMsTopSrcMacAddr=_S5EnMsTopSrcMacAddr_Object((1,3,6,1,4,1,45,1,6,13,4,1,1,1),_S5EnMsTopSrcMacAddr_Type())
s5EnMsTopSrcMacAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopSrcMacAddr.setStatus(_C)
class _S5EnMsTopSrcMacSegId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_S5EnMsTopSrcMacSegId_Type.__name__=_B
_S5EnMsTopSrcMacSegId_Object=MibTableColumn
s5EnMsTopSrcMacSegId=_S5EnMsTopSrcMacSegId_Object((1,3,6,1,4,1,45,1,6,13,4,1,1,2),_S5EnMsTopSrcMacSegId_Type())
s5EnMsTopSrcMacSegId.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopSrcMacSegId.setStatus(_C)
_S5EnMsTopSrcMacAddrLstChg_Type=TimeTicks
_S5EnMsTopSrcMacAddrLstChg_Object=MibScalar
s5EnMsTopSrcMacAddrLstChg=_S5EnMsTopSrcMacAddrLstChg_Object((1,3,6,1,4,1,45,1,6,13,4,2),_S5EnMsTopSrcMacAddrLstChg_Type())
s5EnMsTopSrcMacAddrLstChg.setMaxAccess(_A)
if mibBuilder.loadTexts:s5EnMsTopSrcMacAddrLstChg.setStatus(_C)
_S5EnMsTopPort_ObjectIdentity=ObjectIdentity
s5EnMsTopPort=_S5EnMsTopPort_ObjectIdentity((1,3,6,1,4,1,45,1,6,13,5))
_S5EnMsTopPortTable_Object=MibTable
s5EnMsTopPortTable=_S5EnMsTopPortTable_Object((1,3,6,1,4,1,45,1,6,13,5,1))
if mibBuilder.loadTexts:s5EnMsTopPortTable.setStatus(_E)
_S5EnMsTopPortEntry_Object=MibTableRow
s5EnMsTopPortEntry=_S5EnMsTopPortEntry_Object((1,3,6,1,4,1,45,1,6,13,5,1,1))
s5EnMsTopPortEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:s5EnMsTopPortEntry.setStatus(_E)
_S5EnMsTopPortIfIndex_Type=InterfaceIndex
_S5EnMsTopPortIfIndex_Object=MibTableColumn
s5EnMsTopPortIfIndex=_S5EnMsTopPortIfIndex_Object((1,3,6,1,4,1,45,1,6,13,5,1,1,1),_S5EnMsTopPortIfIndex_Type())
s5EnMsTopPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:s5EnMsTopPortIfIndex.setStatus(_E)
class _S5EnMsTopPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('topActive',1),('topPassthru',2)))
_S5EnMsTopPortState_Type.__name__=_B
_S5EnMsTopPortState_Object=MibTableColumn
s5EnMsTopPortState=_S5EnMsTopPortState_Object((1,3,6,1,4,1,45,1,6,13,5,1,1,2),_S5EnMsTopPortState_Type())
s5EnMsTopPortState.setMaxAccess(_V)
if mibBuilder.loadTexts:s5EnMsTopPortState.setStatus(_E)
mibBuilder.exportSymbols(_D,**{'s5EthMultisegTopologyMib':s5EthMultisegTopologyMib,'s5EnMsTopInfo':s5EnMsTopInfo,'s5EnMsTopIpAddr':s5EnMsTopIpAddr,'s5EnMsTopStatus':s5EnMsTopStatus,'s5EnMsTopNmmLstChg':s5EnMsTopNmmLstChg,'s5EnMsTopBdgLstChg':s5EnMsTopBdgLstChg,'s5EnMsTopNmmMaxNum':s5EnMsTopNmmMaxNum,'s5EnMsTopNmmCurNum':s5EnMsTopNmmCurNum,'s5EnMsTopBdgMaxNum':s5EnMsTopBdgMaxNum,'s5EnMsTopBdgCurNum':s5EnMsTopBdgCurNum,'s5EnMsTopNmm':s5EnMsTopNmm,'s5EnMsTopNmmTable':s5EnMsTopNmmTable,'s5EnMsTopNmmEntry':s5EnMsTopNmmEntry,_J:s5EnMsTopNmmSlot,_K:s5EnMsTopNmmPort,_L:s5EnMsTopNmmIpAddr,_M:s5EnMsTopNmmSegId,'s5EnMsTopNmmMacAddr':s5EnMsTopNmmMacAddr,'s5EnMsTopNmmChassisType':s5EnMsTopNmmChassisType,'s5EnMsTopNmmBkplType':s5EnMsTopNmmBkplType,'s5EnMsTopNmmLocalSeg':s5EnMsTopNmmLocalSeg,'s5EnMsTopNmmCurState':s5EnMsTopNmmCurState,'s5EnMsTopNmmEosSize':s5EnMsTopNmmEosSize,'s5EnMsTopNmmEosTable':s5EnMsTopNmmEosTable,'s5EnMsTopNmmEosEntry':s5EnMsTopNmmEosEntry,'s5EnMsTopNmmEos':s5EnMsTopNmmEos,'s5EnMsTopNmmEnhancedTable':s5EnMsTopNmmEnhancedTable,'s5EnMsTopNmmEnhancedEntry':s5EnMsTopNmmEnhancedEntry,_N:s5EnMsTopNmmEnhancedSlot,_O:s5EnMsTopNmmEnhancedPort,_P:s5EnMsTopNmmEnhancedSubPort,_Q:s5EnMsTopNmmEnhancedIpAddr,_R:s5EnMsTopNmmEnhancedSegId,'s5EnMsTopNmmEnhancedMacAddr':s5EnMsTopNmmEnhancedMacAddr,'s5EnMsTopNmmEnhancedChassisType':s5EnMsTopNmmEnhancedChassisType,'s5EnMsTopNmmEnhancedBkplType':s5EnMsTopNmmEnhancedBkplType,'s5EnMsTopNmmEnhancedLocalSeg':s5EnMsTopNmmEnhancedLocalSeg,'s5EnMsTopNmmEnhancedCurState':s5EnMsTopNmmEnhancedCurState,'s5EnMsTopNmmEnhancedEosTable':s5EnMsTopNmmEnhancedEosTable,'s5EnMsTopNmmEnhancedEosEntry':s5EnMsTopNmmEnhancedEosEntry,'s5EnMsTopNmmEnhancedEos':s5EnMsTopNmmEnhancedEos,'s5EnMsTopBdg':s5EnMsTopBdg,'s5EnMsTopBdgTable':s5EnMsTopBdgTable,'s5EnMsTopBdgEntry':s5EnMsTopBdgEntry,_S:s5EnMsTopBdgSlotNum,_T:s5EnMsTopBdgPortNum,_U:s5EnMsTopBdgIpAddr,'s5EnMsTopBdgNumber':s5EnMsTopBdgNumber,'s5EnMsTopBdgMacAddr':s5EnMsTopBdgMacAddr,'s5EnMsTopBdgType':s5EnMsTopBdgType,'s5EnMsTopBdgNumPorts':s5EnMsTopBdgNumPorts,'s5EnMsTopBdgStatus':s5EnMsTopBdgStatus,'s5EnMsTopBdgHelloPortNum':s5EnMsTopBdgHelloPortNum,'s5EnMsTopBdgHelloPortType':s5EnMsTopBdgHelloPortType,'s5EnMsTopBdgHelloPortStatus':s5EnMsTopBdgHelloPortStatus,'s5EnMsTopBdgCompBdgMac1':s5EnMsTopBdgCompBdgMac1,'s5EnMsTopBdgCompBdgMac2':s5EnMsTopBdgCompBdgMac2,'s5EnMsTopBdgEosSize':s5EnMsTopBdgEosSize,'s5EnMsTopBdgEosTable':s5EnMsTopBdgEosTable,'s5EnMsTopBdgEosEntry':s5EnMsTopBdgEosEntry,'s5EnMsTopBdgEos':s5EnMsTopBdgEos,'s5EnMsTopSrcMac':s5EnMsTopSrcMac,'s5EnMsTopSrcMacAddrTable':s5EnMsTopSrcMacAddrTable,'s5EnMsTopSrcMacAddrEntry':s5EnMsTopSrcMacAddrEntry,_a:s5EnMsTopSrcMacAddr,'s5EnMsTopSrcMacSegId':s5EnMsTopSrcMacSegId,'s5EnMsTopSrcMacAddrLstChg':s5EnMsTopSrcMacAddrLstChg,'s5EnMsTopPort':s5EnMsTopPort,'s5EnMsTopPortTable':s5EnMsTopPortTable,'s5EnMsTopPortEntry':s5EnMsTopPortEntry,_b:s5EnMsTopPortIfIndex,'s5EnMsTopPortState':s5EnMsTopPortState})