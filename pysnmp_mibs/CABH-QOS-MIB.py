_Y='cabhPriorityQosGroup'
_X='cabhPriorityQosPsIfAttribIfNumQueues'
_W='cabhPriorityQosPsIfAttribIfNumPriorities'
_V='cabhPriorityQosBpDestIpPortPriority'
_U='cabhPriorityQosBpDestPort'
_T='cabhPriorityQosBpDestIpAddr'
_S='cabhPriorityQosBpDestIpAddrType'
_R='cabhPriorityQosBpDefaultCHPriority'
_Q='cabhPriorityQosBpApplicationId'
_P='cabhPriorityQosSetToFactory'
_O='cabhPriorityQosMasterRowStatus'
_N='cabhPriorityQosMasterDefaultCHPriority'
_M='cabhPriorityQosBpDestIndex'
_L='read-create'
_K='not-accessible'
_J='ifIndex'
_I='IF-MIB'
_H='cabhPriorityQosBpIndex'
_G='cabhPriorityQosBpIpAddr'
_F='cabhPriorityQosBpIpAddrType'
_E='cabhPriorityQosMasterApplicationId'
_D='Unsigned32'
_C='read-only'
_B='CABH-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjCableHome,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjCableHome')
ifIndex,=mibBuilder.importSymbols(_I,_J)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cabhQosMib=ModuleIdentity((1,3,6,1,4,1,4491,2,4,6))
if mibBuilder.loadTexts:cabhQosMib.setRevisions(('2003-03-01 00:00',))
_CabhQosMibObjects_ObjectIdentity=ObjectIdentity
cabhQosMibObjects=_CabhQosMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,1))
_CabhPriorityQosMibObjects_ObjectIdentity=ObjectIdentity
cabhPriorityQosMibObjects=_CabhPriorityQosMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,1,1))
_CabhPriorityQosBase_ObjectIdentity=ObjectIdentity
cabhPriorityQosBase=_CabhPriorityQosBase_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,1,1,1))
_CabhPriorityQosMasterTable_Object=MibTable
cabhPriorityQosMasterTable=_CabhPriorityQosMasterTable_Object((1,3,6,1,4,1,4491,2,4,6,1,1,1,1))
if mibBuilder.loadTexts:cabhPriorityQosMasterTable.setStatus(_A)
_CabhPriorityQosMasterEntry_Object=MibTableRow
cabhPriorityQosMasterEntry=_CabhPriorityQosMasterEntry_Object((1,3,6,1,4,1,4491,2,4,6,1,1,1,1,1))
cabhPriorityQosMasterEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cabhPriorityQosMasterEntry.setStatus(_A)
class _CabhPriorityQosMasterApplicationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhPriorityQosMasterApplicationId_Type.__name__=_D
_CabhPriorityQosMasterApplicationId_Object=MibTableColumn
cabhPriorityQosMasterApplicationId=_CabhPriorityQosMasterApplicationId_Object((1,3,6,1,4,1,4491,2,4,6,1,1,1,1,1,1),_CabhPriorityQosMasterApplicationId_Type())
cabhPriorityQosMasterApplicationId.setMaxAccess(_K)
if mibBuilder.loadTexts:cabhPriorityQosMasterApplicationId.setStatus(_A)
class _CabhPriorityQosMasterDefaultCHPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CabhPriorityQosMasterDefaultCHPriority_Type.__name__=_D
_CabhPriorityQosMasterDefaultCHPriority_Object=MibTableColumn
cabhPriorityQosMasterDefaultCHPriority=_CabhPriorityQosMasterDefaultCHPriority_Object((1,3,6,1,4,1,4491,2,4,6,1,1,1,1,1,2),_CabhPriorityQosMasterDefaultCHPriority_Type())
cabhPriorityQosMasterDefaultCHPriority.setMaxAccess(_L)
if mibBuilder.loadTexts:cabhPriorityQosMasterDefaultCHPriority.setStatus(_A)
_CabhPriorityQosMasterRowStatus_Type=RowStatus
_CabhPriorityQosMasterRowStatus_Object=MibTableColumn
cabhPriorityQosMasterRowStatus=_CabhPriorityQosMasterRowStatus_Object((1,3,6,1,4,1,4491,2,4,6,1,1,1,1,1,3),_CabhPriorityQosMasterRowStatus_Type())
cabhPriorityQosMasterRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:cabhPriorityQosMasterRowStatus.setStatus(_A)
_CabhPriorityQosSetToFactory_Type=TruthValue
_CabhPriorityQosSetToFactory_Object=MibScalar
cabhPriorityQosSetToFactory=_CabhPriorityQosSetToFactory_Object((1,3,6,1,4,1,4491,2,4,6,1,1,1,2),_CabhPriorityQosSetToFactory_Type())
cabhPriorityQosSetToFactory.setMaxAccess('read-write')
if mibBuilder.loadTexts:cabhPriorityQosSetToFactory.setStatus(_A)
_CabhPriorityQosBp_ObjectIdentity=ObjectIdentity
cabhPriorityQosBp=_CabhPriorityQosBp_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,1,1,2))
_CabhPriorityQosBpTable_Object=MibTable
cabhPriorityQosBpTable=_CabhPriorityQosBpTable_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1))
if mibBuilder.loadTexts:cabhPriorityQosBpTable.setStatus(_A)
_CabhPriorityQosBpEntry_Object=MibTableRow
cabhPriorityQosBpEntry=_CabhPriorityQosBpEntry_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1,1))
cabhPriorityQosBpEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cabhPriorityQosBpEntry.setStatus(_A)
_CabhPriorityQosBpIpAddrType_Type=InetAddressType
_CabhPriorityQosBpIpAddrType_Object=MibTableColumn
cabhPriorityQosBpIpAddrType=_CabhPriorityQosBpIpAddrType_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1,1,1),_CabhPriorityQosBpIpAddrType_Type())
cabhPriorityQosBpIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpIpAddrType.setStatus(_A)
_CabhPriorityQosBpIpAddr_Type=InetAddress
_CabhPriorityQosBpIpAddr_Object=MibTableColumn
cabhPriorityQosBpIpAddr=_CabhPriorityQosBpIpAddr_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1,1,2),_CabhPriorityQosBpIpAddr_Type())
cabhPriorityQosBpIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpIpAddr.setStatus(_A)
class _CabhPriorityQosBpApplicationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhPriorityQosBpApplicationId_Type.__name__=_D
_CabhPriorityQosBpApplicationId_Object=MibTableColumn
cabhPriorityQosBpApplicationId=_CabhPriorityQosBpApplicationId_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1,1,3),_CabhPriorityQosBpApplicationId_Type())
cabhPriorityQosBpApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpApplicationId.setStatus(_A)
class _CabhPriorityQosBpDefaultCHPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CabhPriorityQosBpDefaultCHPriority_Type.__name__=_D
_CabhPriorityQosBpDefaultCHPriority_Object=MibTableColumn
cabhPriorityQosBpDefaultCHPriority=_CabhPriorityQosBpDefaultCHPriority_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1,1,4),_CabhPriorityQosBpDefaultCHPriority_Type())
cabhPriorityQosBpDefaultCHPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpDefaultCHPriority.setStatus(_A)
class _CabhPriorityQosBpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhPriorityQosBpIndex_Type.__name__=_D
_CabhPriorityQosBpIndex_Object=MibTableColumn
cabhPriorityQosBpIndex=_CabhPriorityQosBpIndex_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,1,1,5),_CabhPriorityQosBpIndex_Type())
cabhPriorityQosBpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpIndex.setStatus(_A)
_CabhPriorityQosBpDestTable_Object=MibTable
cabhPriorityQosBpDestTable=_CabhPriorityQosBpDestTable_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2))
if mibBuilder.loadTexts:cabhPriorityQosBpDestTable.setStatus(_A)
_CabhPriorityQosBpDestEntry_Object=MibTableRow
cabhPriorityQosBpDestEntry=_CabhPriorityQosBpDestEntry_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2,1))
cabhPriorityQosBpDestEntry.setIndexNames((0,_B,_H),(0,_B,_M))
if mibBuilder.loadTexts:cabhPriorityQosBpDestEntry.setStatus(_A)
class _CabhPriorityQosBpDestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CabhPriorityQosBpDestIndex_Type.__name__=_D
_CabhPriorityQosBpDestIndex_Object=MibTableColumn
cabhPriorityQosBpDestIndex=_CabhPriorityQosBpDestIndex_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2,1,1),_CabhPriorityQosBpDestIndex_Type())
cabhPriorityQosBpDestIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cabhPriorityQosBpDestIndex.setStatus(_A)
_CabhPriorityQosBpDestIpAddrType_Type=InetAddressType
_CabhPriorityQosBpDestIpAddrType_Object=MibTableColumn
cabhPriorityQosBpDestIpAddrType=_CabhPriorityQosBpDestIpAddrType_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2,1,2),_CabhPriorityQosBpDestIpAddrType_Type())
cabhPriorityQosBpDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpDestIpAddrType.setStatus(_A)
_CabhPriorityQosBpDestIpAddr_Type=InetAddress
_CabhPriorityQosBpDestIpAddr_Object=MibTableColumn
cabhPriorityQosBpDestIpAddr=_CabhPriorityQosBpDestIpAddr_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2,1,3),_CabhPriorityQosBpDestIpAddr_Type())
cabhPriorityQosBpDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpDestIpAddr.setStatus(_A)
_CabhPriorityQosBpDestPort_Type=InetPortNumber
_CabhPriorityQosBpDestPort_Object=MibTableColumn
cabhPriorityQosBpDestPort=_CabhPriorityQosBpDestPort_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2,1,4),_CabhPriorityQosBpDestPort_Type())
cabhPriorityQosBpDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpDestPort.setStatus(_A)
class _CabhPriorityQosBpDestIpPortPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CabhPriorityQosBpDestIpPortPriority_Type.__name__=_D
_CabhPriorityQosBpDestIpPortPriority_Object=MibTableColumn
cabhPriorityQosBpDestIpPortPriority=_CabhPriorityQosBpDestIpPortPriority_Object((1,3,6,1,4,1,4491,2,4,6,1,1,2,2,1,5),_CabhPriorityQosBpDestIpPortPriority_Type())
cabhPriorityQosBpDestIpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosBpDestIpPortPriority.setStatus(_A)
_CabhPriorityQosPs_ObjectIdentity=ObjectIdentity
cabhPriorityQosPs=_CabhPriorityQosPs_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,1,1,3))
_CabhPriorityQosPsIfAttribTable_Object=MibTable
cabhPriorityQosPsIfAttribTable=_CabhPriorityQosPsIfAttribTable_Object((1,3,6,1,4,1,4491,2,4,6,1,1,3,1))
if mibBuilder.loadTexts:cabhPriorityQosPsIfAttribTable.setStatus(_A)
_CabhPriorityQosPsIfAttribEntry_Object=MibTableRow
cabhPriorityQosPsIfAttribEntry=_CabhPriorityQosPsIfAttribEntry_Object((1,3,6,1,4,1,4491,2,4,6,1,1,3,1,1))
cabhPriorityQosPsIfAttribEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cabhPriorityQosPsIfAttribEntry.setStatus(_A)
class _CabhPriorityQosPsIfAttribIfNumPriorities_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CabhPriorityQosPsIfAttribIfNumPriorities_Type.__name__=_D
_CabhPriorityQosPsIfAttribIfNumPriorities_Object=MibTableColumn
cabhPriorityQosPsIfAttribIfNumPriorities=_CabhPriorityQosPsIfAttribIfNumPriorities_Object((1,3,6,1,4,1,4491,2,4,6,1,1,3,1,1,1),_CabhPriorityQosPsIfAttribIfNumPriorities_Type())
cabhPriorityQosPsIfAttribIfNumPriorities.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosPsIfAttribIfNumPriorities.setStatus(_A)
class _CabhPriorityQosPsIfAttribIfNumQueues_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CabhPriorityQosPsIfAttribIfNumQueues_Type.__name__=_D
_CabhPriorityQosPsIfAttribIfNumQueues_Object=MibTableColumn
cabhPriorityQosPsIfAttribIfNumQueues=_CabhPriorityQosPsIfAttribIfNumQueues_Object((1,3,6,1,4,1,4491,2,4,6,1,1,3,1,1,2),_CabhPriorityQosPsIfAttribIfNumQueues_Type())
cabhPriorityQosPsIfAttribIfNumQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhPriorityQosPsIfAttribIfNumQueues.setStatus(_A)
_CabhQosNotification_ObjectIdentity=ObjectIdentity
cabhQosNotification=_CabhQosNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,2))
_CabhPriorityQosNotification_ObjectIdentity=ObjectIdentity
cabhPriorityQosNotification=_CabhPriorityQosNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,2,1))
_CabhQosConformance_ObjectIdentity=ObjectIdentity
cabhQosConformance=_CabhQosConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,3))
_CabhPriorityQosConformance_ObjectIdentity=ObjectIdentity
cabhPriorityQosConformance=_CabhPriorityQosConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,3,1))
_CabhPriorityQosGroups_ObjectIdentity=ObjectIdentity
cabhPriorityQosGroups=_CabhPriorityQosGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,3,1,1))
_CabhPriorityQosCompliances_ObjectIdentity=ObjectIdentity
cabhPriorityQosCompliances=_CabhPriorityQosCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,4,6,3,1,2))
cabhPriorityQosGroup=ObjectGroup((1,3,6,1,4,1,4491,2,4,6,3,1,1,1))
cabhPriorityQosGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_F),(_B,_G),(_B,_Q),(_B,_R),(_B,_H),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cabhPriorityQosGroup.setStatus(_A)
cabhPriorityQosCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,4,6,3,1,2,1))
cabhPriorityQosCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:cabhPriorityQosCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cabhQosMib':cabhQosMib,'cabhQosMibObjects':cabhQosMibObjects,'cabhPriorityQosMibObjects':cabhPriorityQosMibObjects,'cabhPriorityQosBase':cabhPriorityQosBase,'cabhPriorityQosMasterTable':cabhPriorityQosMasterTable,'cabhPriorityQosMasterEntry':cabhPriorityQosMasterEntry,_E:cabhPriorityQosMasterApplicationId,_N:cabhPriorityQosMasterDefaultCHPriority,_O:cabhPriorityQosMasterRowStatus,_P:cabhPriorityQosSetToFactory,'cabhPriorityQosBp':cabhPriorityQosBp,'cabhPriorityQosBpTable':cabhPriorityQosBpTable,'cabhPriorityQosBpEntry':cabhPriorityQosBpEntry,_F:cabhPriorityQosBpIpAddrType,_G:cabhPriorityQosBpIpAddr,_Q:cabhPriorityQosBpApplicationId,_R:cabhPriorityQosBpDefaultCHPriority,_H:cabhPriorityQosBpIndex,'cabhPriorityQosBpDestTable':cabhPriorityQosBpDestTable,'cabhPriorityQosBpDestEntry':cabhPriorityQosBpDestEntry,_M:cabhPriorityQosBpDestIndex,_S:cabhPriorityQosBpDestIpAddrType,_T:cabhPriorityQosBpDestIpAddr,_U:cabhPriorityQosBpDestPort,_V:cabhPriorityQosBpDestIpPortPriority,'cabhPriorityQosPs':cabhPriorityQosPs,'cabhPriorityQosPsIfAttribTable':cabhPriorityQosPsIfAttribTable,'cabhPriorityQosPsIfAttribEntry':cabhPriorityQosPsIfAttribEntry,_W:cabhPriorityQosPsIfAttribIfNumPriorities,_X:cabhPriorityQosPsIfAttribIfNumQueues,'cabhQosNotification':cabhQosNotification,'cabhPriorityQosNotification':cabhPriorityQosNotification,'cabhQosConformance':cabhQosConformance,'cabhPriorityQosConformance':cabhPriorityQosConformance,'cabhPriorityQosGroups':cabhPriorityQosGroups,_Y:cabhPriorityQosGroup,'cabhPriorityQosCompliances':cabhPriorityQosCompliances,'cabhPriorityQosCompliance':cabhPriorityQosCompliance})