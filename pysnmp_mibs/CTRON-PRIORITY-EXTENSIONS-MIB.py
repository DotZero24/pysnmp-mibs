_Z='ctPriorityExtPortInterfaceNum'
_Y='ctPriorityExtPortSlotNum'
_X='ctPriorityExtPktTypeVlanId'
_W='ctPriorityExtPktType'
_V='delete'
_U='ctPriorityExtMACVlanId'
_T='ctPriorityExtMACPktType'
_S='ctPriorityExtAddrType'
_R='ctPriorityExtMACAddr'
_Q='ctPriorityExtInterfaceNum'
_P='ctPriorityExtSlotNum'
_O='priority7'
_N='priority6'
_M='priority5'
_L='priority4'
_K='priority3'
_J='priority2'
_I='priority1'
_H='priority0'
_G='disable'
_F='enable'
_E='read-write'
_D='Integer32'
_C='CTRON-PRIORITY-EXTENSIONS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctPriorityExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctPriorityExt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtPriorityExtTxQueue_ObjectIdentity=ObjectIdentity
ctPriorityExtTxQueue=_CtPriorityExtTxQueue_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,1))
_CtPriorityExtTXQueueTable_Object=MibTable
ctPriorityExtTXQueueTable=_CtPriorityExtTXQueueTable_Object((1,3,6,1,4,1,52,4,1,2,14,1,1))
if mibBuilder.loadTexts:ctPriorityExtTXQueueTable.setStatus(_A)
_CtPriorityExtTXQueueEntry_Object=MibTableRow
ctPriorityExtTXQueueEntry=_CtPriorityExtTXQueueEntry_Object((1,3,6,1,4,1,52,4,1,2,14,1,1,1))
ctPriorityExtTXQueueEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:ctPriorityExtTXQueueEntry.setStatus(_A)
_CtPriorityExtSlotNum_Type=Integer32
_CtPriorityExtSlotNum_Object=MibTableColumn
ctPriorityExtSlotNum=_CtPriorityExtSlotNum_Object((1,3,6,1,4,1,52,4,1,2,14,1,1,1,1),_CtPriorityExtSlotNum_Type())
ctPriorityExtSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtSlotNum.setStatus(_A)
_CtPriorityExtInterfaceNum_Type=Integer32
_CtPriorityExtInterfaceNum_Object=MibTableColumn
ctPriorityExtInterfaceNum=_CtPriorityExtInterfaceNum_Object((1,3,6,1,4,1,52,4,1,2,14,1,1,1,2),_CtPriorityExtInterfaceNum_Type())
ctPriorityExtInterfaceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtInterfaceNum.setStatus(_A)
class _CtPriorityExtNumTXQueues_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CtPriorityExtNumTXQueues_Type.__name__=_D
_CtPriorityExtNumTXQueues_Object=MibTableColumn
ctPriorityExtNumTXQueues=_CtPriorityExtNumTXQueues_Object((1,3,6,1,4,1,52,4,1,2,14,1,1,1,3),_CtPriorityExtNumTXQueues_Type())
ctPriorityExtNumTXQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtNumTXQueues.setStatus(_A)
_CtPriorityExtMACConfig_ObjectIdentity=ObjectIdentity
ctPriorityExtMACConfig=_CtPriorityExtMACConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,2))
class _CtPriorityExtMACStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtPriorityExtMACStatus_Type.__name__=_D
_CtPriorityExtMACStatus_Object=MibScalar
ctPriorityExtMACStatus=_CtPriorityExtMACStatus_Object((1,3,6,1,4,1,52,4,1,2,14,2,1),_CtPriorityExtMACStatus_Type())
ctPriorityExtMACStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtMACStatus.setStatus(_A)
_CtPriorityExtNumMACEntries_Type=Integer32
_CtPriorityExtNumMACEntries_Object=MibScalar
ctPriorityExtNumMACEntries=_CtPriorityExtNumMACEntries_Object((1,3,6,1,4,1,52,4,1,2,14,2,2),_CtPriorityExtNumMACEntries_Type())
ctPriorityExtNumMACEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtNumMACEntries.setStatus(_A)
_CtPriorityExtMaxNumMACEntries_Type=Integer32
_CtPriorityExtMaxNumMACEntries_Object=MibScalar
ctPriorityExtMaxNumMACEntries=_CtPriorityExtMaxNumMACEntries_Object((1,3,6,1,4,1,52,4,1,2,14,2,3),_CtPriorityExtMaxNumMACEntries_Type())
ctPriorityExtMaxNumMACEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtMaxNumMACEntries.setStatus(_A)
_CtPriorityExtMaxNumPktTypesPerMACEntry_Type=Integer32
_CtPriorityExtMaxNumPktTypesPerMACEntry_Object=MibScalar
ctPriorityExtMaxNumPktTypesPerMACEntry=_CtPriorityExtMaxNumPktTypesPerMACEntry_Object((1,3,6,1,4,1,52,4,1,2,14,2,4),_CtPriorityExtMaxNumPktTypesPerMACEntry_Type())
ctPriorityExtMaxNumPktTypesPerMACEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtMaxNumPktTypesPerMACEntry.setStatus(_A)
_CtPriorityExtMACTable_Object=MibTable
ctPriorityExtMACTable=_CtPriorityExtMACTable_Object((1,3,6,1,4,1,52,4,1,2,14,2,5))
if mibBuilder.loadTexts:ctPriorityExtMACTable.setStatus(_A)
_CtPriorityExtMACEntry_Object=MibTableRow
ctPriorityExtMACEntry=_CtPriorityExtMACEntry_Object((1,3,6,1,4,1,52,4,1,2,14,2,5,1))
ctPriorityExtMACEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:ctPriorityExtMACEntry.setStatus(_A)
_CtPriorityExtMACAddr_Type=PhysAddress
_CtPriorityExtMACAddr_Object=MibTableColumn
ctPriorityExtMACAddr=_CtPriorityExtMACAddr_Object((1,3,6,1,4,1,52,4,1,2,14,2,5,1,1),_CtPriorityExtMACAddr_Type())
ctPriorityExtMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtMACAddr.setStatus(_A)
class _CtPriorityExtAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('destAddr',1),('srcAddr',2),('destOrSource',3)))
_CtPriorityExtAddrType_Type.__name__=_D
_CtPriorityExtAddrType_Object=MibTableColumn
ctPriorityExtAddrType=_CtPriorityExtAddrType_Object((1,3,6,1,4,1,52,4,1,2,14,2,5,1,2),_CtPriorityExtAddrType_Type())
ctPriorityExtAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtAddrType.setStatus(_A)
_CtPriorityExtMACPktType_Type=Integer32
_CtPriorityExtMACPktType_Object=MibTableColumn
ctPriorityExtMACPktType=_CtPriorityExtMACPktType_Object((1,3,6,1,4,1,52,4,1,2,14,2,5,1,3),_CtPriorityExtMACPktType_Type())
ctPriorityExtMACPktType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtMACPktType.setStatus(_A)
_CtPriorityExtMACVlanId_Type=Integer32
_CtPriorityExtMACVlanId_Object=MibTableColumn
ctPriorityExtMACVlanId=_CtPriorityExtMACVlanId_Object((1,3,6,1,4,1,52,4,1,2,14,2,5,1,4),_CtPriorityExtMACVlanId_Type())
ctPriorityExtMACVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtMACVlanId.setStatus(_A)
class _CtPriorityExtMACPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,100)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_V,100)))
_CtPriorityExtMACPriority_Type.__name__=_D
_CtPriorityExtMACPriority_Object=MibTableColumn
ctPriorityExtMACPriority=_CtPriorityExtMACPriority_Object((1,3,6,1,4,1,52,4,1,2,14,2,5,1,5),_CtPriorityExtMACPriority_Type())
ctPriorityExtMACPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtMACPriority.setStatus(_A)
_CtPriorityExtPktTypeConfig_ObjectIdentity=ObjectIdentity
ctPriorityExtPktTypeConfig=_CtPriorityExtPktTypeConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,3))
class _CtPriorityExtPktTypeStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtPriorityExtPktTypeStatus_Type.__name__=_D
_CtPriorityExtPktTypeStatus_Object=MibScalar
ctPriorityExtPktTypeStatus=_CtPriorityExtPktTypeStatus_Object((1,3,6,1,4,1,52,4,1,2,14,3,1),_CtPriorityExtPktTypeStatus_Type())
ctPriorityExtPktTypeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtPktTypeStatus.setStatus(_A)
_CtPriorityExtNumPktTypeEntries_Type=Integer32
_CtPriorityExtNumPktTypeEntries_Object=MibScalar
ctPriorityExtNumPktTypeEntries=_CtPriorityExtNumPktTypeEntries_Object((1,3,6,1,4,1,52,4,1,2,14,3,2),_CtPriorityExtNumPktTypeEntries_Type())
ctPriorityExtNumPktTypeEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtNumPktTypeEntries.setStatus(_A)
_CtPriorityExtMaxNumPktTypeEntries_Type=Integer32
_CtPriorityExtMaxNumPktTypeEntries_Object=MibScalar
ctPriorityExtMaxNumPktTypeEntries=_CtPriorityExtMaxNumPktTypeEntries_Object((1,3,6,1,4,1,52,4,1,2,14,3,3),_CtPriorityExtMaxNumPktTypeEntries_Type())
ctPriorityExtMaxNumPktTypeEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtMaxNumPktTypeEntries.setStatus(_A)
_CtPriorityExtPktTypeTable_Object=MibTable
ctPriorityExtPktTypeTable=_CtPriorityExtPktTypeTable_Object((1,3,6,1,4,1,52,4,1,2,14,3,4))
if mibBuilder.loadTexts:ctPriorityExtPktTypeTable.setStatus(_A)
_CtPriorityExtPktTypeEntry_Object=MibTableRow
ctPriorityExtPktTypeEntry=_CtPriorityExtPktTypeEntry_Object((1,3,6,1,4,1,52,4,1,2,14,3,4,1))
ctPriorityExtPktTypeEntry.setIndexNames((0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:ctPriorityExtPktTypeEntry.setStatus(_A)
_CtPriorityExtPktType_Type=Integer32
_CtPriorityExtPktType_Object=MibTableColumn
ctPriorityExtPktType=_CtPriorityExtPktType_Object((1,3,6,1,4,1,52,4,1,2,14,3,4,1,1),_CtPriorityExtPktType_Type())
ctPriorityExtPktType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtPktType.setStatus(_A)
_CtPriorityExtPktTypeVlanId_Type=Integer32
_CtPriorityExtPktTypeVlanId_Object=MibTableColumn
ctPriorityExtPktTypeVlanId=_CtPriorityExtPktTypeVlanId_Object((1,3,6,1,4,1,52,4,1,2,14,3,4,1,2),_CtPriorityExtPktTypeVlanId_Type())
ctPriorityExtPktTypeVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtPktTypeVlanId.setStatus(_A)
class _CtPriorityExtPktTypePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,100)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_V,100)))
_CtPriorityExtPktTypePriority_Type.__name__=_D
_CtPriorityExtPktTypePriority_Object=MibTableColumn
ctPriorityExtPktTypePriority=_CtPriorityExtPktTypePriority_Object((1,3,6,1,4,1,52,4,1,2,14,3,4,1,3),_CtPriorityExtPktTypePriority_Type())
ctPriorityExtPktTypePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtPktTypePriority.setStatus(_A)
_CtPriorityExtPortConfig_ObjectIdentity=ObjectIdentity
ctPriorityExtPortConfig=_CtPriorityExtPortConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,4))
class _CtPriorityExtPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtPriorityExtPortStatus_Type.__name__=_D
_CtPriorityExtPortStatus_Object=MibScalar
ctPriorityExtPortStatus=_CtPriorityExtPortStatus_Object((1,3,6,1,4,1,52,4,1,2,14,4,1),_CtPriorityExtPortStatus_Type())
ctPriorityExtPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtPortStatus.setStatus(_A)
_CtPriorityExtPortTable_Object=MibTable
ctPriorityExtPortTable=_CtPriorityExtPortTable_Object((1,3,6,1,4,1,52,4,1,2,14,4,2))
if mibBuilder.loadTexts:ctPriorityExtPortTable.setStatus(_A)
_CtPriorityExtPortEntry_Object=MibTableRow
ctPriorityExtPortEntry=_CtPriorityExtPortEntry_Object((1,3,6,1,4,1,52,4,1,2,14,4,2,1))
ctPriorityExtPortEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:ctPriorityExtPortEntry.setStatus(_A)
_CtPriorityExtPortSlotNum_Type=Integer32
_CtPriorityExtPortSlotNum_Object=MibTableColumn
ctPriorityExtPortSlotNum=_CtPriorityExtPortSlotNum_Object((1,3,6,1,4,1,52,4,1,2,14,4,2,1,1),_CtPriorityExtPortSlotNum_Type())
ctPriorityExtPortSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtPortSlotNum.setStatus(_A)
_CtPriorityExtPortInterfaceNum_Type=Integer32
_CtPriorityExtPortInterfaceNum_Object=MibTableColumn
ctPriorityExtPortInterfaceNum=_CtPriorityExtPortInterfaceNum_Object((1,3,6,1,4,1,52,4,1,2,14,4,2,1,2),_CtPriorityExtPortInterfaceNum_Type())
ctPriorityExtPortInterfaceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPriorityExtPortInterfaceNum.setStatus(_A)
class _CtPriorityExtPortPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8)))
_CtPriorityExtPortPriority_Type.__name__=_D
_CtPriorityExtPortPriority_Object=MibTableColumn
ctPriorityExtPortPriority=_CtPriorityExtPortPriority_Object((1,3,6,1,4,1,52,4,1,2,14,4,2,1,3),_CtPriorityExtPortPriority_Type())
ctPriorityExtPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtPortPriority.setStatus(_A)
class _CtPriorityExtFwdInboundPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtPriorityExtFwdInboundPriority_Type.__name__=_D
_CtPriorityExtFwdInboundPriority_Object=MibTableColumn
ctPriorityExtFwdInboundPriority=_CtPriorityExtFwdInboundPriority_Object((1,3,6,1,4,1,52,4,1,2,14,4,2,1,4),_CtPriorityExtFwdInboundPriority_Type())
ctPriorityExtFwdInboundPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ctPriorityExtFwdInboundPriority.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctPriorityExtTxQueue':ctPriorityExtTxQueue,'ctPriorityExtTXQueueTable':ctPriorityExtTXQueueTable,'ctPriorityExtTXQueueEntry':ctPriorityExtTXQueueEntry,_P:ctPriorityExtSlotNum,_Q:ctPriorityExtInterfaceNum,'ctPriorityExtNumTXQueues':ctPriorityExtNumTXQueues,'ctPriorityExtMACConfig':ctPriorityExtMACConfig,'ctPriorityExtMACStatus':ctPriorityExtMACStatus,'ctPriorityExtNumMACEntries':ctPriorityExtNumMACEntries,'ctPriorityExtMaxNumMACEntries':ctPriorityExtMaxNumMACEntries,'ctPriorityExtMaxNumPktTypesPerMACEntry':ctPriorityExtMaxNumPktTypesPerMACEntry,'ctPriorityExtMACTable':ctPriorityExtMACTable,'ctPriorityExtMACEntry':ctPriorityExtMACEntry,_R:ctPriorityExtMACAddr,_S:ctPriorityExtAddrType,_T:ctPriorityExtMACPktType,_U:ctPriorityExtMACVlanId,'ctPriorityExtMACPriority':ctPriorityExtMACPriority,'ctPriorityExtPktTypeConfig':ctPriorityExtPktTypeConfig,'ctPriorityExtPktTypeStatus':ctPriorityExtPktTypeStatus,'ctPriorityExtNumPktTypeEntries':ctPriorityExtNumPktTypeEntries,'ctPriorityExtMaxNumPktTypeEntries':ctPriorityExtMaxNumPktTypeEntries,'ctPriorityExtPktTypeTable':ctPriorityExtPktTypeTable,'ctPriorityExtPktTypeEntry':ctPriorityExtPktTypeEntry,_W:ctPriorityExtPktType,_X:ctPriorityExtPktTypeVlanId,'ctPriorityExtPktTypePriority':ctPriorityExtPktTypePriority,'ctPriorityExtPortConfig':ctPriorityExtPortConfig,'ctPriorityExtPortStatus':ctPriorityExtPortStatus,'ctPriorityExtPortTable':ctPriorityExtPortTable,'ctPriorityExtPortEntry':ctPriorityExtPortEntry,_Y:ctPriorityExtPortSlotNum,_Z:ctPriorityExtPortInterfaceNum,'ctPriorityExtPortPriority':ctPriorityExtPortPriority,'ctPriorityExtFwdInboundPriority':ctPriorityExtFwdInboundPriority})