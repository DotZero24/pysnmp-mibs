_H='hpGlobalMemSlotIndex'
_G='hpLocalMemSlotIndex'
_F='hpPktBufSlotIndex'
_E='hpMsgBufSlotIndex'
_D='NETSWITCH-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpOpSystem_ObjectIdentity=ObjectIdentity
hpOpSystem=_HpOpSystem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1))
_HpBuf_ObjectIdentity=ObjectIdentity
hpBuf=_HpBuf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1,1))
_HpMsgBuf_ObjectIdentity=ObjectIdentity
hpMsgBuf=_HpMsgBuf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1))
_HpMsgBufTable_Object=MibTable
hpMsgBufTable=_HpMsgBufTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1))
if mibBuilder.loadTexts:hpMsgBufTable.setStatus(_A)
_HpMsgBufEntry_Object=MibTableRow
hpMsgBufEntry=_HpMsgBufEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1))
hpMsgBufEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpMsgBufEntry.setStatus(_A)
class _HpMsgBufSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpMsgBufSlotIndex_Type.__name__=_C
_HpMsgBufSlotIndex_Object=MibTableColumn
hpMsgBufSlotIndex=_HpMsgBufSlotIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,1),_HpMsgBufSlotIndex_Type())
hpMsgBufSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufSlotIndex.setStatus(_A)
_HpMsgBufCorrupted_Type=Counter32
_HpMsgBufCorrupted_Object=MibTableColumn
hpMsgBufCorrupted=_HpMsgBufCorrupted_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,2),_HpMsgBufCorrupted_Type())
hpMsgBufCorrupted.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufCorrupted.setStatus(_A)
_HpMsgBufFree_Type=Integer32
_HpMsgBufFree_Object=MibTableColumn
hpMsgBufFree=_HpMsgBufFree_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,3),_HpMsgBufFree_Type())
hpMsgBufFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufFree.setStatus(_A)
_HpMsgBufInit_Type=Integer32
_HpMsgBufInit_Object=MibTableColumn
hpMsgBufInit=_HpMsgBufInit_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,4),_HpMsgBufInit_Type())
hpMsgBufInit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufInit.setStatus(_A)
_HpMsgBufMin_Type=Integer32
_HpMsgBufMin_Object=MibTableColumn
hpMsgBufMin=_HpMsgBufMin_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,5),_HpMsgBufMin_Type())
hpMsgBufMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufMin.setStatus(_A)
_HpMsgBufMiss_Type=Counter32
_HpMsgBufMiss_Object=MibTableColumn
hpMsgBufMiss=_HpMsgBufMiss_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,6),_HpMsgBufMiss_Type())
hpMsgBufMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufMiss.setStatus(_A)
_HpMsgBufSize_Type=Integer32
_HpMsgBufSize_Object=MibTableColumn
hpMsgBufSize=_HpMsgBufSize_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,1,1,1,7),_HpMsgBufSize_Type())
hpMsgBufSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpMsgBufSize.setStatus(_A)
_HpPktBuf_ObjectIdentity=ObjectIdentity
hpPktBuf=_HpPktBuf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2))
_HpPktBufTable_Object=MibTable
hpPktBufTable=_HpPktBufTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1))
if mibBuilder.loadTexts:hpPktBufTable.setStatus(_A)
_HpPktBufEntry_Object=MibTableRow
hpPktBufEntry=_HpPktBufEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1))
hpPktBufEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpPktBufEntry.setStatus(_A)
class _HpPktBufSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpPktBufSlotIndex_Type.__name__=_C
_HpPktBufSlotIndex_Object=MibTableColumn
hpPktBufSlotIndex=_HpPktBufSlotIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,1),_HpPktBufSlotIndex_Type())
hpPktBufSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufSlotIndex.setStatus(_A)
_HpPktBufCorrupted_Type=Counter32
_HpPktBufCorrupted_Object=MibTableColumn
hpPktBufCorrupted=_HpPktBufCorrupted_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,2),_HpPktBufCorrupted_Type())
hpPktBufCorrupted.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufCorrupted.setStatus(_A)
_HpPktBufFree_Type=Integer32
_HpPktBufFree_Object=MibTableColumn
hpPktBufFree=_HpPktBufFree_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,3),_HpPktBufFree_Type())
hpPktBufFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufFree.setStatus(_A)
_HpPktBufInit_Type=Integer32
_HpPktBufInit_Object=MibTableColumn
hpPktBufInit=_HpPktBufInit_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,4),_HpPktBufInit_Type())
hpPktBufInit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufInit.setStatus(_A)
_HpPktBufMin_Type=Integer32
_HpPktBufMin_Object=MibTableColumn
hpPktBufMin=_HpPktBufMin_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,5),_HpPktBufMin_Type())
hpPktBufMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufMin.setStatus(_A)
_HpPktBufMiss_Type=Counter32
_HpPktBufMiss_Object=MibTableColumn
hpPktBufMiss=_HpPktBufMiss_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,6),_HpPktBufMiss_Type())
hpPktBufMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufMiss.setStatus(_A)
_HpPktBufSize_Type=Integer32
_HpPktBufSize_Object=MibTableColumn
hpPktBufSize=_HpPktBufSize_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,1,2,1,1,7),_HpPktBufSize_Type())
hpPktBufSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPktBufSize.setStatus(_A)
_HpMem_ObjectIdentity=ObjectIdentity
hpMem=_HpMem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1,2))
_HpLocalMem_ObjectIdentity=ObjectIdentity
hpLocalMem=_HpLocalMem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1))
_HpLocalMemTable_Object=MibTable
hpLocalMemTable=_HpLocalMemTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1))
if mibBuilder.loadTexts:hpLocalMemTable.setStatus(_A)
_HpLocalMemEntry_Object=MibTableRow
hpLocalMemEntry=_HpLocalMemEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1))
hpLocalMemEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpLocalMemEntry.setStatus(_A)
class _HpLocalMemSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpLocalMemSlotIndex_Type.__name__=_C
_HpLocalMemSlotIndex_Object=MibTableColumn
hpLocalMemSlotIndex=_HpLocalMemSlotIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,1),_HpLocalMemSlotIndex_Type())
hpLocalMemSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemSlotIndex.setStatus(_A)
_HpLocalMemSlabCnt_Type=Counter32
_HpLocalMemSlabCnt_Object=MibTableColumn
hpLocalMemSlabCnt=_HpLocalMemSlabCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,2),_HpLocalMemSlabCnt_Type())
hpLocalMemSlabCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemSlabCnt.setStatus(_A)
_HpLocalMemFreeSegCnt_Type=Counter32
_HpLocalMemFreeSegCnt_Object=MibTableColumn
hpLocalMemFreeSegCnt=_HpLocalMemFreeSegCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,3),_HpLocalMemFreeSegCnt_Type())
hpLocalMemFreeSegCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemFreeSegCnt.setStatus(_A)
_HpLocalMemAllocSegCnt_Type=Counter32
_HpLocalMemAllocSegCnt_Object=MibTableColumn
hpLocalMemAllocSegCnt=_HpLocalMemAllocSegCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,4),_HpLocalMemAllocSegCnt_Type())
hpLocalMemAllocSegCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemAllocSegCnt.setStatus(_A)
_HpLocalMemTotalBytes_Type=Integer32
_HpLocalMemTotalBytes_Object=MibTableColumn
hpLocalMemTotalBytes=_HpLocalMemTotalBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,5),_HpLocalMemTotalBytes_Type())
hpLocalMemTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemTotalBytes.setStatus(_A)
_HpLocalMemFreeBytes_Type=Integer32
_HpLocalMemFreeBytes_Object=MibTableColumn
hpLocalMemFreeBytes=_HpLocalMemFreeBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,6),_HpLocalMemFreeBytes_Type())
hpLocalMemFreeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemFreeBytes.setStatus(_A)
_HpLocalMemAllocBytes_Type=Integer32
_HpLocalMemAllocBytes_Object=MibTableColumn
hpLocalMemAllocBytes=_HpLocalMemAllocBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,1,1,1,7),_HpLocalMemAllocBytes_Type())
hpLocalMemAllocBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLocalMemAllocBytes.setStatus(_A)
_HpGlobalMem_ObjectIdentity=ObjectIdentity
hpGlobalMem=_HpGlobalMem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2))
_HpGlobalMemTable_Object=MibTable
hpGlobalMemTable=_HpGlobalMemTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1))
if mibBuilder.loadTexts:hpGlobalMemTable.setStatus(_A)
_HpGlobalMemEntry_Object=MibTableRow
hpGlobalMemEntry=_HpGlobalMemEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1))
hpGlobalMemEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpGlobalMemEntry.setStatus(_A)
class _HpGlobalMemSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpGlobalMemSlotIndex_Type.__name__=_C
_HpGlobalMemSlotIndex_Object=MibTableColumn
hpGlobalMemSlotIndex=_HpGlobalMemSlotIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,1),_HpGlobalMemSlotIndex_Type())
hpGlobalMemSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemSlotIndex.setStatus(_A)
_HpGlobalMemSlabCnt_Type=Counter32
_HpGlobalMemSlabCnt_Object=MibTableColumn
hpGlobalMemSlabCnt=_HpGlobalMemSlabCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,2),_HpGlobalMemSlabCnt_Type())
hpGlobalMemSlabCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemSlabCnt.setStatus(_A)
_HpGlobalMemFreeSegCnt_Type=Counter32
_HpGlobalMemFreeSegCnt_Object=MibTableColumn
hpGlobalMemFreeSegCnt=_HpGlobalMemFreeSegCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,3),_HpGlobalMemFreeSegCnt_Type())
hpGlobalMemFreeSegCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemFreeSegCnt.setStatus(_A)
_HpGlobalMemAllocSegCnt_Type=Counter32
_HpGlobalMemAllocSegCnt_Object=MibTableColumn
hpGlobalMemAllocSegCnt=_HpGlobalMemAllocSegCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,4),_HpGlobalMemAllocSegCnt_Type())
hpGlobalMemAllocSegCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemAllocSegCnt.setStatus(_A)
_HpGlobalMemTotalBytes_Type=Integer32
_HpGlobalMemTotalBytes_Object=MibTableColumn
hpGlobalMemTotalBytes=_HpGlobalMemTotalBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,5),_HpGlobalMemTotalBytes_Type())
hpGlobalMemTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemTotalBytes.setStatus(_A)
_HpGlobalMemFreeBytes_Type=Integer32
_HpGlobalMemFreeBytes_Object=MibTableColumn
hpGlobalMemFreeBytes=_HpGlobalMemFreeBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,6),_HpGlobalMemFreeBytes_Type())
hpGlobalMemFreeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemFreeBytes.setStatus(_A)
_HpGlobalMemAllocBytes_Type=Integer32
_HpGlobalMemAllocBytes_Object=MibTableColumn
hpGlobalMemAllocBytes=_HpGlobalMemAllocBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,2,2,1,1,7),_HpGlobalMemAllocBytes_Type())
hpGlobalMemAllocBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGlobalMemAllocBytes.setStatus(_A)
_HpSwitchOsVersion_Type=DisplayString
_HpSwitchOsVersion_Object=MibScalar
hpSwitchOsVersion=_HpSwitchOsVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,3),_HpSwitchOsVersion_Type())
hpSwitchOsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchOsVersion.setStatus(_A)
_HpSwitchRomVersion_Type=DisplayString
_HpSwitchRomVersion_Object=MibScalar
hpSwitchRomVersion=_HpSwitchRomVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,4),_HpSwitchRomVersion_Type())
hpSwitchRomVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchRomVersion.setStatus(_A)
class _HpSwitchSmartCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('fddi',2),('atm',3),('fddiAndATM',4),('other',5)))
_HpSwitchSmartCardType_Type.__name__=_C
_HpSwitchSmartCardType_Object=MibScalar
hpSwitchSmartCardType=_HpSwitchSmartCardType_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,5),_HpSwitchSmartCardType_Type())
hpSwitchSmartCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchSmartCardType.setStatus(_A)
_HpSwitchBaseMACAddress_Type=MacAddress
_HpSwitchBaseMACAddress_Object=MibScalar
hpSwitchBaseMACAddress=_HpSwitchBaseMACAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,1,6),_HpSwitchBaseMACAddress_Type())
hpSwitchBaseMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchBaseMACAddress.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'hpOpSystem':hpOpSystem,'hpBuf':hpBuf,'hpMsgBuf':hpMsgBuf,'hpMsgBufTable':hpMsgBufTable,'hpMsgBufEntry':hpMsgBufEntry,_E:hpMsgBufSlotIndex,'hpMsgBufCorrupted':hpMsgBufCorrupted,'hpMsgBufFree':hpMsgBufFree,'hpMsgBufInit':hpMsgBufInit,'hpMsgBufMin':hpMsgBufMin,'hpMsgBufMiss':hpMsgBufMiss,'hpMsgBufSize':hpMsgBufSize,'hpPktBuf':hpPktBuf,'hpPktBufTable':hpPktBufTable,'hpPktBufEntry':hpPktBufEntry,_F:hpPktBufSlotIndex,'hpPktBufCorrupted':hpPktBufCorrupted,'hpPktBufFree':hpPktBufFree,'hpPktBufInit':hpPktBufInit,'hpPktBufMin':hpPktBufMin,'hpPktBufMiss':hpPktBufMiss,'hpPktBufSize':hpPktBufSize,'hpMem':hpMem,'hpLocalMem':hpLocalMem,'hpLocalMemTable':hpLocalMemTable,'hpLocalMemEntry':hpLocalMemEntry,_G:hpLocalMemSlotIndex,'hpLocalMemSlabCnt':hpLocalMemSlabCnt,'hpLocalMemFreeSegCnt':hpLocalMemFreeSegCnt,'hpLocalMemAllocSegCnt':hpLocalMemAllocSegCnt,'hpLocalMemTotalBytes':hpLocalMemTotalBytes,'hpLocalMemFreeBytes':hpLocalMemFreeBytes,'hpLocalMemAllocBytes':hpLocalMemAllocBytes,'hpGlobalMem':hpGlobalMem,'hpGlobalMemTable':hpGlobalMemTable,'hpGlobalMemEntry':hpGlobalMemEntry,_H:hpGlobalMemSlotIndex,'hpGlobalMemSlabCnt':hpGlobalMemSlabCnt,'hpGlobalMemFreeSegCnt':hpGlobalMemFreeSegCnt,'hpGlobalMemAllocSegCnt':hpGlobalMemAllocSegCnt,'hpGlobalMemTotalBytes':hpGlobalMemTotalBytes,'hpGlobalMemFreeBytes':hpGlobalMemFreeBytes,'hpGlobalMemAllocBytes':hpGlobalMemAllocBytes,'hpSwitchOsVersion':hpSwitchOsVersion,'hpSwitchRomVersion':hpSwitchRomVersion,'hpSwitchSmartCardType':hpSwitchSmartCardType,'hpSwitchBaseMACAddress':hpSwitchBaseMACAddress})