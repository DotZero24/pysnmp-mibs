_b='hpnsaEISAPortInitEntryIndex'
_a='hpnsaEISAPortInitFunctIndex'
_Z='hpnsaEISAPortInitSlotIndex'
_Y='hpnsaEISAPortEntryIndex'
_X='hpnsaEISAPortFunctIndex'
_W='hpnsaEISAPortSlotIndex'
_V='hpnsaEISADmaAllocIndex'
_U='hpnsaEISADmaFunctIndex'
_T='hpnsaEISADmaSlotIndex'
_S='hpnsaEISAIntAllocIndex'
_R='hpnsaEISAIntFunctIndex'
_Q='hpnsaEISAIntSlotIndex'
_P='hpnsaEISAMemAllocIndex'
_O='hpnsaEISAMemFunctIndex'
_N='hpnsaEISAMemSlotIndex'
_M='hpnsaEISAFunctIndex'
_L='hpnsaEISAFunctSlotIndex'
_K='virtual'
_J='hpnsaEISASlotIndex'
_I='hpnsaEISAAgentIndex'
_H='shared'
_G='notShared'
_F='OctetString'
_E='DisplayString'
_D='HPNSAEISA-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaEISA_ObjectIdentity=ObjectIdentity
hpnsaEISA=_HpnsaEISA_ObjectIdentity((1,3,6,1,4,1,11,2,23,9))
_HpnsaEISAMibRev_ObjectIdentity=ObjectIdentity
hpnsaEISAMibRev=_HpnsaEISAMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,9,1))
class _HpnsaEISAMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaEISAMibRevMajor_Type.__name__=_C
_HpnsaEISAMibRevMajor_Object=MibScalar
hpnsaEISAMibRevMajor=_HpnsaEISAMibRevMajor_Object((1,3,6,1,4,1,11,2,23,9,1,1),_HpnsaEISAMibRevMajor_Type())
hpnsaEISAMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMibRevMajor.setStatus(_A)
class _HpnsaEISAMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEISAMibRevMinor_Type.__name__=_C
_HpnsaEISAMibRevMinor_Object=MibScalar
hpnsaEISAMibRevMinor=_HpnsaEISAMibRevMinor_Object((1,3,6,1,4,1,11,2,23,9,1,2),_HpnsaEISAMibRevMinor_Type())
hpnsaEISAMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMibRevMinor.setStatus(_A)
_HpnsaEISAAgent_ObjectIdentity=ObjectIdentity
hpnsaEISAAgent=_HpnsaEISAAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,9,2))
_HpnsaEISAAgentTable_Object=MibTable
hpnsaEISAAgentTable=_HpnsaEISAAgentTable_Object((1,3,6,1,4,1,11,2,23,9,2,1))
if mibBuilder.loadTexts:hpnsaEISAAgentTable.setStatus(_A)
_HpnsaEISAAgentEntry_Object=MibTableRow
hpnsaEISAAgentEntry=_HpnsaEISAAgentEntry_Object((1,3,6,1,4,1,11,2,23,9,2,1,1))
hpnsaEISAAgentEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hpnsaEISAAgentEntry.setStatus(_A)
class _HpnsaEISAAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAAgentIndex_Type.__name__=_C
_HpnsaEISAAgentIndex_Object=MibTableColumn
hpnsaEISAAgentIndex=_HpnsaEISAAgentIndex_Object((1,3,6,1,4,1,11,2,23,9,2,1,1,1),_HpnsaEISAAgentIndex_Type())
hpnsaEISAAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAAgentIndex.setStatus(_A)
class _HpnsaEISAAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEISAAgentName_Type.__name__=_E
_HpnsaEISAAgentName_Object=MibTableColumn
hpnsaEISAAgentName=_HpnsaEISAAgentName_Object((1,3,6,1,4,1,11,2,23,9,2,1,1,2),_HpnsaEISAAgentName_Type())
hpnsaEISAAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAAgentName.setStatus(_A)
class _HpnsaEISAAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnsaEISAAgentVersion_Type.__name__=_E
_HpnsaEISAAgentVersion_Object=MibTableColumn
hpnsaEISAAgentVersion=_HpnsaEISAAgentVersion_Object((1,3,6,1,4,1,11,2,23,9,2,1,1,3),_HpnsaEISAAgentVersion_Type())
hpnsaEISAAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAAgentVersion.setStatus(_A)
class _HpnsaEISAAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEISAAgentDate_Type.__name__=_F
_HpnsaEISAAgentDate_Object=MibTableColumn
hpnsaEISAAgentDate=_HpnsaEISAAgentDate_Object((1,3,6,1,4,1,11,2,23,9,2,1,1,4),_HpnsaEISAAgentDate_Type())
hpnsaEISAAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAAgentDate.setStatus(_A)
_HpnsaEISACfgUtil_ObjectIdentity=ObjectIdentity
hpnsaEISACfgUtil=_HpnsaEISACfgUtil_ObjectIdentity((1,3,6,1,4,1,11,2,23,9,3))
class _HpnsaEISACfgUtilRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaEISACfgUtilRevMajor_Type.__name__=_C
_HpnsaEISACfgUtilRevMajor_Object=MibScalar
hpnsaEISACfgUtilRevMajor=_HpnsaEISACfgUtilRevMajor_Object((1,3,6,1,4,1,11,2,23,9,3,1),_HpnsaEISACfgUtilRevMajor_Type())
hpnsaEISACfgUtilRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISACfgUtilRevMajor.setStatus(_A)
class _HpnsaEISACfgUtilRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEISACfgUtilRevMinor_Type.__name__=_C
_HpnsaEISACfgUtilRevMinor_Object=MibScalar
hpnsaEISACfgUtilRevMinor=_HpnsaEISACfgUtilRevMinor_Object((1,3,6,1,4,1,11,2,23,9,3,2),_HpnsaEISACfgUtilRevMinor_Type())
hpnsaEISACfgUtilRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISACfgUtilRevMinor.setStatus(_A)
_HpnsaEISASlotInfo_ObjectIdentity=ObjectIdentity
hpnsaEISASlotInfo=_HpnsaEISASlotInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,9,4))
_HpnsaEISABoardTable_Object=MibTable
hpnsaEISABoardTable=_HpnsaEISABoardTable_Object((1,3,6,1,4,1,11,2,23,9,4,1))
if mibBuilder.loadTexts:hpnsaEISABoardTable.setStatus(_A)
_HpnsaEISABoardEntry_Object=MibTableRow
hpnsaEISABoardEntry=_HpnsaEISABoardEntry_Object((1,3,6,1,4,1,11,2,23,9,4,1,1))
hpnsaEISABoardEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnsaEISABoardEntry.setStatus(_A)
_HpnsaEISASlotIndex_Type=Integer32
_HpnsaEISASlotIndex_Object=MibTableColumn
hpnsaEISASlotIndex=_HpnsaEISASlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,1),_HpnsaEISASlotIndex_Type())
hpnsaEISASlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISASlotIndex.setStatus(_A)
class _HpnsaEISASlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('expansion',0),('embedded',1),(_K,2),('reserved',3)))
_HpnsaEISASlotType_Type.__name__=_C
_HpnsaEISASlotType_Object=MibTableColumn
hpnsaEISASlotType=_HpnsaEISASlotType_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,2),_HpnsaEISASlotType_Type())
hpnsaEISASlotType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISASlotType.setStatus(_A)
_HpnsaEISACfgRevMajor_Type=Integer32
_HpnsaEISACfgRevMajor_Object=MibTableColumn
hpnsaEISACfgRevMajor=_HpnsaEISACfgRevMajor_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,3),_HpnsaEISACfgRevMajor_Type())
hpnsaEISACfgRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISACfgRevMajor.setStatus(_A)
_HpnsaEISACfgRevMinor_Type=Integer32
_HpnsaEISACfgRevMinor_Object=MibTableColumn
hpnsaEISACfgRevMinor=_HpnsaEISACfgRevMinor_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,4),_HpnsaEISACfgRevMinor_Type())
hpnsaEISACfgRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISACfgRevMinor.setStatus(_A)
class _HpnsaEISABoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_HpnsaEISABoardID_Type.__name__=_E
_HpnsaEISABoardID_Object=MibTableColumn
hpnsaEISABoardID=_HpnsaEISABoardID_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,5),_HpnsaEISABoardID_Type())
hpnsaEISABoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISABoardID.setStatus(_A)
_HpnsaEISABoardDupCfg_Type=Integer32
_HpnsaEISABoardDupCfg_Object=MibTableColumn
hpnsaEISABoardDupCfg=_HpnsaEISABoardDupCfg_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,6),_HpnsaEISABoardDupCfg_Type())
hpnsaEISABoardDupCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISABoardDupCfg.setStatus(_A)
_HpnsaEISANumFunctions_Type=Integer32
_HpnsaEISANumFunctions_Object=MibTableColumn
hpnsaEISANumFunctions=_HpnsaEISANumFunctions_Object((1,3,6,1,4,1,11,2,23,9,4,1,1,7),_HpnsaEISANumFunctions_Type())
hpnsaEISANumFunctions.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISANumFunctions.setStatus(_A)
_HpnsaEISAFunctTable_Object=MibTable
hpnsaEISAFunctTable=_HpnsaEISAFunctTable_Object((1,3,6,1,4,1,11,2,23,9,4,2))
if mibBuilder.loadTexts:hpnsaEISAFunctTable.setStatus(_A)
_HpnsaEISAFunctEntry_Object=MibTableRow
hpnsaEISAFunctEntry=_HpnsaEISAFunctEntry_Object((1,3,6,1,4,1,11,2,23,9,4,2,1))
hpnsaEISAFunctEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:hpnsaEISAFunctEntry.setStatus(_A)
class _HpnsaEISAFunctSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAFunctSlotIndex_Type.__name__=_C
_HpnsaEISAFunctSlotIndex_Object=MibTableColumn
hpnsaEISAFunctSlotIndex=_HpnsaEISAFunctSlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,2,1,1),_HpnsaEISAFunctSlotIndex_Type())
hpnsaEISAFunctSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAFunctSlotIndex.setStatus(_A)
class _HpnsaEISAFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAFunctIndex_Type.__name__=_C
_HpnsaEISAFunctIndex_Object=MibTableColumn
hpnsaEISAFunctIndex=_HpnsaEISAFunctIndex_Object((1,3,6,1,4,1,11,2,23,9,4,2,1,2),_HpnsaEISAFunctIndex_Type())
hpnsaEISAFunctIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAFunctIndex.setStatus(_A)
class _HpnsaEISAFunctStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('disabled',2),('enabled',3)))
_HpnsaEISAFunctStatus_Type.__name__=_C
_HpnsaEISAFunctStatus_Object=MibTableColumn
hpnsaEISAFunctStatus=_HpnsaEISAFunctStatus_Object((1,3,6,1,4,1,11,2,23,9,4,2,1,3),_HpnsaEISAFunctStatus_Type())
hpnsaEISAFunctStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAFunctStatus.setStatus(_A)
class _HpnsaEISAFunctType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_HpnsaEISAFunctType_Type.__name__=_E
_HpnsaEISAFunctType_Object=MibTableColumn
hpnsaEISAFunctType=_HpnsaEISAFunctType_Object((1,3,6,1,4,1,11,2,23,9,4,2,1,4),_HpnsaEISAFunctType_Type())
hpnsaEISAFunctType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAFunctType.setStatus(_A)
_HpnsaEISAMemTable_Object=MibTable
hpnsaEISAMemTable=_HpnsaEISAMemTable_Object((1,3,6,1,4,1,11,2,23,9,4,3))
if mibBuilder.loadTexts:hpnsaEISAMemTable.setStatus(_A)
_HpnsaEISAMemEntry_Object=MibTableRow
hpnsaEISAMemEntry=_HpnsaEISAMemEntry_Object((1,3,6,1,4,1,11,2,23,9,4,3,1))
hpnsaEISAMemEntry.setIndexNames((0,_D,_N),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:hpnsaEISAMemEntry.setStatus(_A)
class _HpnsaEISAMemSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAMemSlotIndex_Type.__name__=_C
_HpnsaEISAMemSlotIndex_Object=MibTableColumn
hpnsaEISAMemSlotIndex=_HpnsaEISAMemSlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,1),_HpnsaEISAMemSlotIndex_Type())
hpnsaEISAMemSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemSlotIndex.setStatus(_A)
class _HpnsaEISAMemFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAMemFunctIndex_Type.__name__=_C
_HpnsaEISAMemFunctIndex_Object=MibTableColumn
hpnsaEISAMemFunctIndex=_HpnsaEISAMemFunctIndex_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,2),_HpnsaEISAMemFunctIndex_Type())
hpnsaEISAMemFunctIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemFunctIndex.setStatus(_A)
class _HpnsaEISAMemAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAMemAllocIndex_Type.__name__=_C
_HpnsaEISAMemAllocIndex_Object=MibTableColumn
hpnsaEISAMemAllocIndex=_HpnsaEISAMemAllocIndex_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,3),_HpnsaEISAMemAllocIndex_Type())
hpnsaEISAMemAllocIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemAllocIndex.setStatus(_A)
_HpnsaEISAMemStartAddr_Type=Integer32
_HpnsaEISAMemStartAddr_Object=MibTableColumn
hpnsaEISAMemStartAddr=_HpnsaEISAMemStartAddr_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,4),_HpnsaEISAMemStartAddr_Type())
hpnsaEISAMemStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemStartAddr.setStatus(_A)
_HpnsaEISAMemSize_Type=Integer32
_HpnsaEISAMemSize_Object=MibTableColumn
hpnsaEISAMemSize=_HpnsaEISAMemSize_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,5),_HpnsaEISAMemSize_Type())
hpnsaEISAMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemSize.setStatus(_A)
class _HpnsaEISAMemShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nonshareable',0),('shareable',1)))
_HpnsaEISAMemShare_Type.__name__=_C
_HpnsaEISAMemShare_Object=MibTableColumn
hpnsaEISAMemShare=_HpnsaEISAMemShare_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,6),_HpnsaEISAMemShare_Type())
hpnsaEISAMemShare.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemShare.setStatus(_A)
class _HpnsaEISAMemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('systemBaseOrExtended',1),('expanded',2),(_K,3)))
_HpnsaEISAMemType_Type.__name__=_C
_HpnsaEISAMemType_Object=MibTableColumn
hpnsaEISAMemType=_HpnsaEISAMemType_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,7),_HpnsaEISAMemType_Type())
hpnsaEISAMemType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemType.setStatus(_A)
class _HpnsaEISAMemCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notCached',1),('writeThroughCached',2),('writeBackCached',3)))
_HpnsaEISAMemCache_Type.__name__=_C
_HpnsaEISAMemCache_Object=MibTableColumn
hpnsaEISAMemCache=_HpnsaEISAMemCache_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,8),_HpnsaEISAMemCache_Type())
hpnsaEISAMemCache.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemCache.setStatus(_A)
class _HpnsaEISAMemAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_HpnsaEISAMemAccess_Type.__name__=_C
_HpnsaEISAMemAccess_Object=MibTableColumn
hpnsaEISAMemAccess=_HpnsaEISAMemAccess_Object((1,3,6,1,4,1,11,2,23,9,4,3,1,9),_HpnsaEISAMemAccess_Type())
hpnsaEISAMemAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAMemAccess.setStatus(_A)
_HpnsaEISAIntTable_Object=MibTable
hpnsaEISAIntTable=_HpnsaEISAIntTable_Object((1,3,6,1,4,1,11,2,23,9,4,4))
if mibBuilder.loadTexts:hpnsaEISAIntTable.setStatus(_A)
_HpnsaEISAIntEntry_Object=MibTableRow
hpnsaEISAIntEntry=_HpnsaEISAIntEntry_Object((1,3,6,1,4,1,11,2,23,9,4,4,1))
hpnsaEISAIntEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:hpnsaEISAIntEntry.setStatus(_A)
class _HpnsaEISAIntSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAIntSlotIndex_Type.__name__=_C
_HpnsaEISAIntSlotIndex_Object=MibTableColumn
hpnsaEISAIntSlotIndex=_HpnsaEISAIntSlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,4,1,1),_HpnsaEISAIntSlotIndex_Type())
hpnsaEISAIntSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAIntSlotIndex.setStatus(_A)
class _HpnsaEISAIntFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAIntFunctIndex_Type.__name__=_C
_HpnsaEISAIntFunctIndex_Object=MibTableColumn
hpnsaEISAIntFunctIndex=_HpnsaEISAIntFunctIndex_Object((1,3,6,1,4,1,11,2,23,9,4,4,1,2),_HpnsaEISAIntFunctIndex_Type())
hpnsaEISAIntFunctIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAIntFunctIndex.setStatus(_A)
class _HpnsaEISAIntAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISAIntAllocIndex_Type.__name__=_C
_HpnsaEISAIntAllocIndex_Object=MibTableColumn
hpnsaEISAIntAllocIndex=_HpnsaEISAIntAllocIndex_Object((1,3,6,1,4,1,11,2,23,9,4,4,1,3),_HpnsaEISAIntAllocIndex_Type())
hpnsaEISAIntAllocIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAIntAllocIndex.setStatus(_A)
class _HpnsaEISAIntNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEISAIntNum_Type.__name__=_C
_HpnsaEISAIntNum_Object=MibTableColumn
hpnsaEISAIntNum=_HpnsaEISAIntNum_Object((1,3,6,1,4,1,11,2,23,9,4,4,1,4),_HpnsaEISAIntNum_Type())
hpnsaEISAIntNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAIntNum.setStatus(_A)
class _HpnsaEISAIntShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnsaEISAIntShare_Type.__name__=_C
_HpnsaEISAIntShare_Object=MibTableColumn
hpnsaEISAIntShare=_HpnsaEISAIntShare_Object((1,3,6,1,4,1,11,2,23,9,4,4,1,5),_HpnsaEISAIntShare_Type())
hpnsaEISAIntShare.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAIntShare.setStatus(_A)
class _HpnsaEISAIntTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('edgeTriggered',0),('levelTriggered',1)))
_HpnsaEISAIntTrigger_Type.__name__=_C
_HpnsaEISAIntTrigger_Object=MibTableColumn
hpnsaEISAIntTrigger=_HpnsaEISAIntTrigger_Object((1,3,6,1,4,1,11,2,23,9,4,4,1,6),_HpnsaEISAIntTrigger_Type())
hpnsaEISAIntTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAIntTrigger.setStatus(_A)
_HpnsaEISADmaTable_Object=MibTable
hpnsaEISADmaTable=_HpnsaEISADmaTable_Object((1,3,6,1,4,1,11,2,23,9,4,5))
if mibBuilder.loadTexts:hpnsaEISADmaTable.setStatus(_A)
_HpnsaEISADmaEntry_Object=MibTableRow
hpnsaEISADmaEntry=_HpnsaEISADmaEntry_Object((1,3,6,1,4,1,11,2,23,9,4,5,1))
hpnsaEISADmaEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:hpnsaEISADmaEntry.setStatus(_A)
class _HpnsaEISADmaSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISADmaSlotIndex_Type.__name__=_C
_HpnsaEISADmaSlotIndex_Object=MibTableColumn
hpnsaEISADmaSlotIndex=_HpnsaEISADmaSlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,1),_HpnsaEISADmaSlotIndex_Type())
hpnsaEISADmaSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaSlotIndex.setStatus(_A)
class _HpnsaEISADmaFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISADmaFunctIndex_Type.__name__=_C
_HpnsaEISADmaFunctIndex_Object=MibTableColumn
hpnsaEISADmaFunctIndex=_HpnsaEISADmaFunctIndex_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,2),_HpnsaEISADmaFunctIndex_Type())
hpnsaEISADmaFunctIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaFunctIndex.setStatus(_A)
class _HpnsaEISADmaAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEISADmaAllocIndex_Type.__name__=_C
_HpnsaEISADmaAllocIndex_Object=MibTableColumn
hpnsaEISADmaAllocIndex=_HpnsaEISADmaAllocIndex_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,3),_HpnsaEISADmaAllocIndex_Type())
hpnsaEISADmaAllocIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaAllocIndex.setStatus(_A)
class _HpnsaEISADmaChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEISADmaChannelNum_Type.__name__=_C
_HpnsaEISADmaChannelNum_Object=MibTableColumn
hpnsaEISADmaChannelNum=_HpnsaEISADmaChannelNum_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,4),_HpnsaEISADmaChannelNum_Type())
hpnsaEISADmaChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaChannelNum.setStatus(_A)
class _HpnsaEISADmaShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnsaEISADmaShare_Type.__name__=_C
_HpnsaEISADmaShare_Object=MibTableColumn
hpnsaEISADmaShare=_HpnsaEISADmaShare_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,5),_HpnsaEISADmaShare_Type())
hpnsaEISADmaShare.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaShare.setStatus(_A)
class _HpnsaEISADmaTiming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('defaultISACompat',0),('typeA',1),('typeB',2),('burstC',3)))
_HpnsaEISADmaTiming_Type.__name__=_C
_HpnsaEISADmaTiming_Object=MibTableColumn
hpnsaEISADmaTiming=_HpnsaEISADmaTiming_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,6),_HpnsaEISADmaTiming_Type())
hpnsaEISADmaTiming.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaTiming.setStatus(_A)
class _HpnsaEISADmaXferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('eightBit',0),('sixteenBit',1),('thirtyTwoBit',2)))
_HpnsaEISADmaXferSize_Type.__name__=_C
_HpnsaEISADmaXferSize_Object=MibTableColumn
hpnsaEISADmaXferSize=_HpnsaEISADmaXferSize_Object((1,3,6,1,4,1,11,2,23,9,4,5,1,7),_HpnsaEISADmaXferSize_Type())
hpnsaEISADmaXferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISADmaXferSize.setStatus(_A)
_HpnsaEISAPortTable_Object=MibTable
hpnsaEISAPortTable=_HpnsaEISAPortTable_Object((1,3,6,1,4,1,11,2,23,9,4,6))
if mibBuilder.loadTexts:hpnsaEISAPortTable.setStatus(_A)
_HpnsaEISAPortEntry_Object=MibTableRow
hpnsaEISAPortEntry=_HpnsaEISAPortEntry_Object((1,3,6,1,4,1,11,2,23,9,4,6,1))
hpnsaEISAPortEntry.setIndexNames((0,_D,_W),(0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:hpnsaEISAPortEntry.setStatus(_A)
_HpnsaEISAPortSlotIndex_Type=Integer32
_HpnsaEISAPortSlotIndex_Object=MibTableColumn
hpnsaEISAPortSlotIndex=_HpnsaEISAPortSlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,6,1,1),_HpnsaEISAPortSlotIndex_Type())
hpnsaEISAPortSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortSlotIndex.setStatus(_A)
_HpnsaEISAPortFunctIndex_Type=Integer32
_HpnsaEISAPortFunctIndex_Object=MibTableColumn
hpnsaEISAPortFunctIndex=_HpnsaEISAPortFunctIndex_Object((1,3,6,1,4,1,11,2,23,9,4,6,1,2),_HpnsaEISAPortFunctIndex_Type())
hpnsaEISAPortFunctIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortFunctIndex.setStatus(_A)
_HpnsaEISAPortEntryIndex_Type=Integer32
_HpnsaEISAPortEntryIndex_Object=MibTableColumn
hpnsaEISAPortEntryIndex=_HpnsaEISAPortEntryIndex_Object((1,3,6,1,4,1,11,2,23,9,4,6,1,3),_HpnsaEISAPortEntryIndex_Type())
hpnsaEISAPortEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortEntryIndex.setStatus(_A)
_HpnsaEISAPortAddress_Type=Integer32
_HpnsaEISAPortAddress_Object=MibTableColumn
hpnsaEISAPortAddress=_HpnsaEISAPortAddress_Object((1,3,6,1,4,1,11,2,23,9,4,6,1,4),_HpnsaEISAPortAddress_Type())
hpnsaEISAPortAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortAddress.setStatus(_A)
_HpnsaEISAPortSize_Type=Integer32
_HpnsaEISAPortSize_Object=MibTableColumn
hpnsaEISAPortSize=_HpnsaEISAPortSize_Object((1,3,6,1,4,1,11,2,23,9,4,6,1,5),_HpnsaEISAPortSize_Type())
hpnsaEISAPortSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortSize.setStatus(_A)
class _HpnsaEISAPortShared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_HpnsaEISAPortShared_Type.__name__=_C
_HpnsaEISAPortShared_Object=MibTableColumn
hpnsaEISAPortShared=_HpnsaEISAPortShared_Object((1,3,6,1,4,1,11,2,23,9,4,6,1,6),_HpnsaEISAPortShared_Type())
hpnsaEISAPortShared.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortShared.setStatus(_A)
_HpnsaEISAPortInitTable_Object=MibTable
hpnsaEISAPortInitTable=_HpnsaEISAPortInitTable_Object((1,3,6,1,4,1,11,2,23,9,4,7))
if mibBuilder.loadTexts:hpnsaEISAPortInitTable.setStatus(_A)
_HpnsaEISAPortInitEntry_Object=MibTableRow
hpnsaEISAPortInitEntry=_HpnsaEISAPortInitEntry_Object((1,3,6,1,4,1,11,2,23,9,4,7,1))
hpnsaEISAPortInitEntry.setIndexNames((0,_D,_Z),(0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:hpnsaEISAPortInitEntry.setStatus(_A)
_HpnsaEISAPortInitSlotIndex_Type=Integer32
_HpnsaEISAPortInitSlotIndex_Object=MibTableColumn
hpnsaEISAPortInitSlotIndex=_HpnsaEISAPortInitSlotIndex_Object((1,3,6,1,4,1,11,2,23,9,4,7,1,1),_HpnsaEISAPortInitSlotIndex_Type())
hpnsaEISAPortInitSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortInitSlotIndex.setStatus(_A)
_HpnsaEISAPortInitFunctIndex_Type=Integer32
_HpnsaEISAPortInitFunctIndex_Object=MibTableColumn
hpnsaEISAPortInitFunctIndex=_HpnsaEISAPortInitFunctIndex_Object((1,3,6,1,4,1,11,2,23,9,4,7,1,2),_HpnsaEISAPortInitFunctIndex_Type())
hpnsaEISAPortInitFunctIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortInitFunctIndex.setStatus(_A)
_HpnsaEISAPortInitEntryIndex_Type=Integer32
_HpnsaEISAPortInitEntryIndex_Object=MibTableColumn
hpnsaEISAPortInitEntryIndex=_HpnsaEISAPortInitEntryIndex_Object((1,3,6,1,4,1,11,2,23,9,4,7,1,3),_HpnsaEISAPortInitEntryIndex_Type())
hpnsaEISAPortInitEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortInitEntryIndex.setStatus(_A)
class _HpnsaEISAPortInitData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_HpnsaEISAPortInitData_Type.__name__=_F
_HpnsaEISAPortInitData_Object=MibTableColumn
hpnsaEISAPortInitData=_HpnsaEISAPortInitData_Object((1,3,6,1,4,1,11,2,23,9,4,7,1,4),_HpnsaEISAPortInitData_Type())
hpnsaEISAPortInitData.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEISAPortInitData.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaEISA':hpnsaEISA,'hpnsaEISAMibRev':hpnsaEISAMibRev,'hpnsaEISAMibRevMajor':hpnsaEISAMibRevMajor,'hpnsaEISAMibRevMinor':hpnsaEISAMibRevMinor,'hpnsaEISAAgent':hpnsaEISAAgent,'hpnsaEISAAgentTable':hpnsaEISAAgentTable,'hpnsaEISAAgentEntry':hpnsaEISAAgentEntry,_I:hpnsaEISAAgentIndex,'hpnsaEISAAgentName':hpnsaEISAAgentName,'hpnsaEISAAgentVersion':hpnsaEISAAgentVersion,'hpnsaEISAAgentDate':hpnsaEISAAgentDate,'hpnsaEISACfgUtil':hpnsaEISACfgUtil,'hpnsaEISACfgUtilRevMajor':hpnsaEISACfgUtilRevMajor,'hpnsaEISACfgUtilRevMinor':hpnsaEISACfgUtilRevMinor,'hpnsaEISASlotInfo':hpnsaEISASlotInfo,'hpnsaEISABoardTable':hpnsaEISABoardTable,'hpnsaEISABoardEntry':hpnsaEISABoardEntry,_J:hpnsaEISASlotIndex,'hpnsaEISASlotType':hpnsaEISASlotType,'hpnsaEISACfgRevMajor':hpnsaEISACfgRevMajor,'hpnsaEISACfgRevMinor':hpnsaEISACfgRevMinor,'hpnsaEISABoardID':hpnsaEISABoardID,'hpnsaEISABoardDupCfg':hpnsaEISABoardDupCfg,'hpnsaEISANumFunctions':hpnsaEISANumFunctions,'hpnsaEISAFunctTable':hpnsaEISAFunctTable,'hpnsaEISAFunctEntry':hpnsaEISAFunctEntry,_L:hpnsaEISAFunctSlotIndex,_M:hpnsaEISAFunctIndex,'hpnsaEISAFunctStatus':hpnsaEISAFunctStatus,'hpnsaEISAFunctType':hpnsaEISAFunctType,'hpnsaEISAMemTable':hpnsaEISAMemTable,'hpnsaEISAMemEntry':hpnsaEISAMemEntry,_N:hpnsaEISAMemSlotIndex,_O:hpnsaEISAMemFunctIndex,_P:hpnsaEISAMemAllocIndex,'hpnsaEISAMemStartAddr':hpnsaEISAMemStartAddr,'hpnsaEISAMemSize':hpnsaEISAMemSize,'hpnsaEISAMemShare':hpnsaEISAMemShare,'hpnsaEISAMemType':hpnsaEISAMemType,'hpnsaEISAMemCache':hpnsaEISAMemCache,'hpnsaEISAMemAccess':hpnsaEISAMemAccess,'hpnsaEISAIntTable':hpnsaEISAIntTable,'hpnsaEISAIntEntry':hpnsaEISAIntEntry,_Q:hpnsaEISAIntSlotIndex,_R:hpnsaEISAIntFunctIndex,_S:hpnsaEISAIntAllocIndex,'hpnsaEISAIntNum':hpnsaEISAIntNum,'hpnsaEISAIntShare':hpnsaEISAIntShare,'hpnsaEISAIntTrigger':hpnsaEISAIntTrigger,'hpnsaEISADmaTable':hpnsaEISADmaTable,'hpnsaEISADmaEntry':hpnsaEISADmaEntry,_T:hpnsaEISADmaSlotIndex,_U:hpnsaEISADmaFunctIndex,_V:hpnsaEISADmaAllocIndex,'hpnsaEISADmaChannelNum':hpnsaEISADmaChannelNum,'hpnsaEISADmaShare':hpnsaEISADmaShare,'hpnsaEISADmaTiming':hpnsaEISADmaTiming,'hpnsaEISADmaXferSize':hpnsaEISADmaXferSize,'hpnsaEISAPortTable':hpnsaEISAPortTable,'hpnsaEISAPortEntry':hpnsaEISAPortEntry,_W:hpnsaEISAPortSlotIndex,_X:hpnsaEISAPortFunctIndex,_Y:hpnsaEISAPortEntryIndex,'hpnsaEISAPortAddress':hpnsaEISAPortAddress,'hpnsaEISAPortSize':hpnsaEISAPortSize,'hpnsaEISAPortShared':hpnsaEISAPortShared,'hpnsaEISAPortInitTable':hpnsaEISAPortInitTable,'hpnsaEISAPortInitEntry':hpnsaEISAPortInitEntry,_Z:hpnsaEISAPortInitSlotIndex,_a:hpnsaEISAPortInitFunctIndex,_b:hpnsaEISAPortInitEntryIndex,'hpnsaEISAPortInitData':hpnsaEISAPortInitData})