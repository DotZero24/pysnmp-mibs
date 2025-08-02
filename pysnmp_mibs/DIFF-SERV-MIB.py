_S='diffServQueueNumber'
_R='packets'
_Q='diffServActionNumber'
_P='diffServTBMeterNumber'
_O='diffServClassifierNumber'
_N='diffServMFClassifierIndex'
_M='diffServAggregateDSCP'
_L='Unsigned32'
_K='bytes'
_J='diffServInterfaceDirection'
_I='RowPointer'
_H='ifIndex'
_G='IF-MIB'
_F='read-only'
_E='DIFF-SERV-MIB'
_D='Integer32'
_C='read-write'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rlExperience,=mibBuilder.importSymbols('Dell-MIB','rlExperience')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso','mib-2','zeroDotZero')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_I,'RowStatus','TextualConvention','TestAndIncr')
diffServMib=ModuleIdentity((1,3,6,1,4,1,89,51,1))
if mibBuilder.loadTexts:diffServMib.setRevisions(('1999-07-19 01:00',))
class Dscp(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class MFClassifierL4Port(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiffServObjects_ObjectIdentity=ObjectIdentity
diffServObjects=_DiffServObjects_ObjectIdentity((1,3,6,1,4,1,89,51,1,1))
_DiffServMFClassifierUnique_Type=TestAndIncr
_DiffServMFClassifierUnique_Object=MibScalar
diffServMFClassifierUnique=_DiffServMFClassifierUnique_Object((1,3,6,1,4,1,89,51,1,1,1),_DiffServMFClassifierUnique_Type())
diffServMFClassifierUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServMFClassifierUnique.setStatus(_A)
_DiffServClassifierUnique_Type=TestAndIncr
_DiffServClassifierUnique_Object=MibScalar
diffServClassifierUnique=_DiffServClassifierUnique_Object((1,3,6,1,4,1,89,51,1,1,2),_DiffServClassifierUnique_Type())
diffServClassifierUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServClassifierUnique.setStatus(_A)
_DiffServTBMeterUnique_Type=TestAndIncr
_DiffServTBMeterUnique_Object=MibScalar
diffServTBMeterUnique=_DiffServTBMeterUnique_Object((1,3,6,1,4,1,89,51,1,1,3),_DiffServTBMeterUnique_Type())
diffServTBMeterUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServTBMeterUnique.setStatus(_A)
_DiffServActionUnique_Type=TestAndIncr
_DiffServActionUnique_Object=MibScalar
diffServActionUnique=_DiffServActionUnique_Object((1,3,6,1,4,1,89,51,1,1,4),_DiffServActionUnique_Type())
diffServActionUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServActionUnique.setStatus(_A)
_DiffServQueueUnique_Type=TestAndIncr
_DiffServQueueUnique_Object=MibScalar
diffServQueueUnique=_DiffServQueueUnique_Object((1,3,6,1,4,1,89,51,1,1,5),_DiffServQueueUnique_Type())
diffServQueueUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServQueueUnique.setStatus(_A)
_DiffServTables_ObjectIdentity=ObjectIdentity
diffServTables=_DiffServTables_ObjectIdentity((1,3,6,1,4,1,89,51,1,2))
_DiffServAggregateTable_Object=MibTable
diffServAggregateTable=_DiffServAggregateTable_Object((1,3,6,1,4,1,89,51,1,2,1))
if mibBuilder.loadTexts:diffServAggregateTable.setStatus(_A)
_DiffServAggregateEntry_Object=MibTableRow
diffServAggregateEntry=_DiffServAggregateEntry_Object((1,3,6,1,4,1,89,51,1,2,1,1))
diffServAggregateEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:diffServAggregateEntry.setStatus(_A)
_DiffServAggregateDSCP_Type=Dscp
_DiffServAggregateDSCP_Object=MibTableColumn
diffServAggregateDSCP=_DiffServAggregateDSCP_Object((1,3,6,1,4,1,89,51,1,2,1,1,1),_DiffServAggregateDSCP_Type())
diffServAggregateDSCP.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServAggregateDSCP.setStatus(_A)
_DiffServMFClassifierTable_Object=MibTable
diffServMFClassifierTable=_DiffServMFClassifierTable_Object((1,3,6,1,4,1,89,51,1,2,2))
if mibBuilder.loadTexts:diffServMFClassifierTable.setStatus(_A)
_DiffServMFClassifierEntry_Object=MibTableRow
diffServMFClassifierEntry=_DiffServMFClassifierEntry_Object((1,3,6,1,4,1,89,51,1,2,2,1))
diffServMFClassifierEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:diffServMFClassifierEntry.setStatus(_A)
class _DiffServMFClassifierIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DiffServMFClassifierIndex_Type.__name__=_D
_DiffServMFClassifierIndex_Object=MibTableColumn
diffServMFClassifierIndex=_DiffServMFClassifierIndex_Object((1,3,6,1,4,1,89,51,1,2,2,1,1),_DiffServMFClassifierIndex_Type())
diffServMFClassifierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServMFClassifierIndex.setStatus(_A)
_DiffServMFClassifierAddrType_Type=InetAddressType
_DiffServMFClassifierAddrType_Object=MibTableColumn
diffServMFClassifierAddrType=_DiffServMFClassifierAddrType_Object((1,3,6,1,4,1,89,51,1,2,2,1,2),_DiffServMFClassifierAddrType_Type())
diffServMFClassifierAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierAddrType.setStatus(_A)
_DiffServMFClassifierDstAddr_Type=InetAddress
_DiffServMFClassifierDstAddr_Object=MibTableColumn
diffServMFClassifierDstAddr=_DiffServMFClassifierDstAddr_Object((1,3,6,1,4,1,89,51,1,2,2,1,3),_DiffServMFClassifierDstAddr_Type())
diffServMFClassifierDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierDstAddr.setStatus(_A)
_DiffServMFClassifierDstAddrMask_Type=InetAddress
_DiffServMFClassifierDstAddrMask_Object=MibTableColumn
diffServMFClassifierDstAddrMask=_DiffServMFClassifierDstAddrMask_Object((1,3,6,1,4,1,89,51,1,2,2,1,4),_DiffServMFClassifierDstAddrMask_Type())
diffServMFClassifierDstAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierDstAddrMask.setStatus(_A)
_DiffServMFClassifierSrcAddr_Type=InetAddress
_DiffServMFClassifierSrcAddr_Object=MibTableColumn
diffServMFClassifierSrcAddr=_DiffServMFClassifierSrcAddr_Object((1,3,6,1,4,1,89,51,1,2,2,1,5),_DiffServMFClassifierSrcAddr_Type())
diffServMFClassifierSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierSrcAddr.setStatus(_A)
_DiffServMFClassifierSrcAddrMask_Type=InetAddress
_DiffServMFClassifierSrcAddrMask_Object=MibTableColumn
diffServMFClassifierSrcAddrMask=_DiffServMFClassifierSrcAddrMask_Object((1,3,6,1,4,1,89,51,1,2,2,1,6),_DiffServMFClassifierSrcAddrMask_Type())
diffServMFClassifierSrcAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierSrcAddrMask.setStatus(_A)
class _DiffServMFClassifierDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_DiffServMFClassifierDscp_Type.__name__=_D
_DiffServMFClassifierDscp_Object=MibTableColumn
diffServMFClassifierDscp=_DiffServMFClassifierDscp_Object((1,3,6,1,4,1,89,51,1,2,2,1,7),_DiffServMFClassifierDscp_Type())
diffServMFClassifierDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierDscp.setStatus(_A)
class _DiffServMFClassifierProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DiffServMFClassifierProtocol_Type.__name__=_D
_DiffServMFClassifierProtocol_Object=MibTableColumn
diffServMFClassifierProtocol=_DiffServMFClassifierProtocol_Object((1,3,6,1,4,1,89,51,1,2,2,1,8),_DiffServMFClassifierProtocol_Type())
diffServMFClassifierProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierProtocol.setStatus(_A)
_DiffServMFClassifierDstL4PortMin_Type=MFClassifierL4Port
_DiffServMFClassifierDstL4PortMin_Object=MibTableColumn
diffServMFClassifierDstL4PortMin=_DiffServMFClassifierDstL4PortMin_Object((1,3,6,1,4,1,89,51,1,2,2,1,9),_DiffServMFClassifierDstL4PortMin_Type())
diffServMFClassifierDstL4PortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierDstL4PortMin.setStatus(_A)
_DiffServMFClassifierDstL4PortMax_Type=MFClassifierL4Port
_DiffServMFClassifierDstL4PortMax_Object=MibTableColumn
diffServMFClassifierDstL4PortMax=_DiffServMFClassifierDstL4PortMax_Object((1,3,6,1,4,1,89,51,1,2,2,1,10),_DiffServMFClassifierDstL4PortMax_Type())
diffServMFClassifierDstL4PortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierDstL4PortMax.setStatus(_A)
_DiffServMFClassifierSrcL4PortMin_Type=MFClassifierL4Port
_DiffServMFClassifierSrcL4PortMin_Object=MibTableColumn
diffServMFClassifierSrcL4PortMin=_DiffServMFClassifierSrcL4PortMin_Object((1,3,6,1,4,1,89,51,1,2,2,1,11),_DiffServMFClassifierSrcL4PortMin_Type())
diffServMFClassifierSrcL4PortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierSrcL4PortMin.setStatus(_A)
_DiffServMFClassifierSrcL4PortMax_Type=MFClassifierL4Port
_DiffServMFClassifierSrcL4PortMax_Object=MibTableColumn
diffServMFClassifierSrcL4PortMax=_DiffServMFClassifierSrcL4PortMax_Object((1,3,6,1,4,1,89,51,1,2,2,1,12),_DiffServMFClassifierSrcL4PortMax_Type())
diffServMFClassifierSrcL4PortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierSrcL4PortMax.setStatus(_A)
_DiffServMFClassifierStatus_Type=RowStatus
_DiffServMFClassifierStatus_Object=MibTableColumn
diffServMFClassifierStatus=_DiffServMFClassifierStatus_Object((1,3,6,1,4,1,89,51,1,2,2,1,13),_DiffServMFClassifierStatus_Type())
diffServMFClassifierStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServMFClassifierStatus.setStatus(_A)
_DiffServClassifierTable_Object=MibTable
diffServClassifierTable=_DiffServClassifierTable_Object((1,3,6,1,4,1,89,51,1,2,3))
if mibBuilder.loadTexts:diffServClassifierTable.setStatus(_A)
_DiffServClassifierEntry_Object=MibTableRow
diffServClassifierEntry=_DiffServClassifierEntry_Object((1,3,6,1,4,1,89,51,1,2,3,1))
diffServClassifierEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_O))
if mibBuilder.loadTexts:diffServClassifierEntry.setStatus(_A)
class _DiffServInterfaceDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_DiffServInterfaceDirection_Type.__name__=_D
_DiffServInterfaceDirection_Object=MibTableColumn
diffServInterfaceDirection=_DiffServInterfaceDirection_Object((1,3,6,1,4,1,89,51,1,2,3,1,1),_DiffServInterfaceDirection_Type())
diffServInterfaceDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServInterfaceDirection.setStatus(_A)
class _DiffServClassifierNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DiffServClassifierNumber_Type.__name__=_D
_DiffServClassifierNumber_Object=MibTableColumn
diffServClassifierNumber=_DiffServClassifierNumber_Object((1,3,6,1,4,1,89,51,1,2,3,1,2),_DiffServClassifierNumber_Type())
diffServClassifierNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServClassifierNumber.setStatus(_A)
class _DiffServClassifierMatchObject_Type(RowPointer):defaultValue=0,0
_DiffServClassifierMatchObject_Type.__name__=_I
_DiffServClassifierMatchObject_Object=MibTableColumn
diffServClassifierMatchObject=_DiffServClassifierMatchObject_Object((1,3,6,1,4,1,89,51,1,2,3,1,3),_DiffServClassifierMatchObject_Type())
diffServClassifierMatchObject.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServClassifierMatchObject.setStatus(_A)
_DiffServClassifierNext_Type=RowPointer
_DiffServClassifierNext_Object=MibTableColumn
diffServClassifierNext=_DiffServClassifierNext_Object((1,3,6,1,4,1,89,51,1,2,3,1,4),_DiffServClassifierNext_Type())
diffServClassifierNext.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServClassifierNext.setStatus(_A)
class _DiffServClassifierSequence_Type(Unsigned32):defaultValue=0
_DiffServClassifierSequence_Type.__name__=_L
_DiffServClassifierSequence_Object=MibTableColumn
diffServClassifierSequence=_DiffServClassifierSequence_Object((1,3,6,1,4,1,89,51,1,2,3,1,5),_DiffServClassifierSequence_Type())
diffServClassifierSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServClassifierSequence.setStatus(_A)
class _DiffServClassifierConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('other',0),('mib',1),('pib',2),('bgp',3)))
_DiffServClassifierConfigType_Type.__name__=_D
_DiffServClassifierConfigType_Object=MibTableColumn
diffServClassifierConfigType=_DiffServClassifierConfigType_Object((1,3,6,1,4,1,89,51,1,2,3,1,6),_DiffServClassifierConfigType_Type())
diffServClassifierConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServClassifierConfigType.setStatus(_A)
_DiffServClassifierConfigTypeInfo_Type=OctetString
_DiffServClassifierConfigTypeInfo_Object=MibTableColumn
diffServClassifierConfigTypeInfo=_DiffServClassifierConfigTypeInfo_Object((1,3,6,1,4,1,89,51,1,2,3,1,7),_DiffServClassifierConfigTypeInfo_Type())
diffServClassifierConfigTypeInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServClassifierConfigTypeInfo.setStatus(_A)
_DiffServClassifierStatus_Type=RowStatus
_DiffServClassifierStatus_Object=MibTableColumn
diffServClassifierStatus=_DiffServClassifierStatus_Object((1,3,6,1,4,1,89,51,1,2,3,1,8),_DiffServClassifierStatus_Type())
diffServClassifierStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServClassifierStatus.setStatus(_A)
_DiffServTBMeterTable_Object=MibTable
diffServTBMeterTable=_DiffServTBMeterTable_Object((1,3,6,1,4,1,89,51,1,2,4))
if mibBuilder.loadTexts:diffServTBMeterTable.setStatus(_A)
_DiffServTBMeterEntry_Object=MibTableRow
diffServTBMeterEntry=_DiffServTBMeterEntry_Object((1,3,6,1,4,1,89,51,1,2,4,1))
diffServTBMeterEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_P))
if mibBuilder.loadTexts:diffServTBMeterEntry.setStatus(_A)
class _DiffServTBMeterNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DiffServTBMeterNumber_Type.__name__=_D
_DiffServTBMeterNumber_Object=MibTableColumn
diffServTBMeterNumber=_DiffServTBMeterNumber_Object((1,3,6,1,4,1,89,51,1,2,4,1,1),_DiffServTBMeterNumber_Type())
diffServTBMeterNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:diffServTBMeterNumber.setStatus(_A)
_DiffServTBMeterInterval_Type=Unsigned32
_DiffServTBMeterInterval_Object=MibTableColumn
diffServTBMeterInterval=_DiffServTBMeterInterval_Object((1,3,6,1,4,1,89,51,1,2,4,1,2),_DiffServTBMeterInterval_Type())
diffServTBMeterInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServTBMeterInterval.setStatus(_A)
if mibBuilder.loadTexts:diffServTBMeterInterval.setUnits('microseconds')
_DiffServTBMeterBurstSize_Type=Unsigned32
_DiffServTBMeterBurstSize_Object=MibTableColumn
diffServTBMeterBurstSize=_DiffServTBMeterBurstSize_Object((1,3,6,1,4,1,89,51,1,2,4,1,3),_DiffServTBMeterBurstSize_Type())
diffServTBMeterBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServTBMeterBurstSize.setStatus(_A)
if mibBuilder.loadTexts:diffServTBMeterBurstSize.setUnits(_K)
_DiffServTBMeterFailNext_Type=RowPointer
_DiffServTBMeterFailNext_Object=MibTableColumn
diffServTBMeterFailNext=_DiffServTBMeterFailNext_Object((1,3,6,1,4,1,89,51,1,2,4,1,4),_DiffServTBMeterFailNext_Type())
diffServTBMeterFailNext.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServTBMeterFailNext.setStatus(_A)
class _DiffServTBMeterSucceedNext_Type(RowPointer):defaultValue=0,0
_DiffServTBMeterSucceedNext_Type.__name__=_I
_DiffServTBMeterSucceedNext_Object=MibTableColumn
diffServTBMeterSucceedNext=_DiffServTBMeterSucceedNext_Object((1,3,6,1,4,1,89,51,1,2,4,1,5),_DiffServTBMeterSucceedNext_Type())
diffServTBMeterSucceedNext.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServTBMeterSucceedNext.setStatus(_A)
_DiffServTBMeterStatus_Type=RowStatus
_DiffServTBMeterStatus_Object=MibTableColumn
diffServTBMeterStatus=_DiffServTBMeterStatus_Object((1,3,6,1,4,1,89,51,1,2,4,1,6),_DiffServTBMeterStatus_Type())
diffServTBMeterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServTBMeterStatus.setStatus(_A)
_DiffServActionTable_Object=MibTable
diffServActionTable=_DiffServActionTable_Object((1,3,6,1,4,1,89,51,1,2,5))
if mibBuilder.loadTexts:diffServActionTable.setStatus(_A)
_DiffServActionEntry_Object=MibTableRow
diffServActionEntry=_DiffServActionEntry_Object((1,3,6,1,4,1,89,51,1,2,5,1))
diffServActionEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_Q))
if mibBuilder.loadTexts:diffServActionEntry.setStatus(_A)
class _DiffServActionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DiffServActionNumber_Type.__name__=_D
_DiffServActionNumber_Object=MibTableColumn
diffServActionNumber=_DiffServActionNumber_Object((1,3,6,1,4,1,89,51,1,2,5,1,1),_DiffServActionNumber_Type())
diffServActionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServActionNumber.setStatus(_A)
class _DiffServActionNext_Type(RowPointer):defaultValue=0,0
_DiffServActionNext_Type.__name__=_I
_DiffServActionNext_Object=MibTableColumn
diffServActionNext=_DiffServActionNext_Object((1,3,6,1,4,1,89,51,1,2,5,1,2),_DiffServActionNext_Type())
diffServActionNext.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServActionNext.setStatus(_A)
_DiffServActionDSCP_Type=Dscp
_DiffServActionDSCP_Object=MibTableColumn
diffServActionDSCP=_DiffServActionDSCP_Object((1,3,6,1,4,1,89,51,1,2,5,1,3),_DiffServActionDSCP_Type())
diffServActionDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServActionDSCP.setStatus(_A)
_DiffServActionMinThreshold_Type=Unsigned32
_DiffServActionMinThreshold_Object=MibTableColumn
diffServActionMinThreshold=_DiffServActionMinThreshold_Object((1,3,6,1,4,1,89,51,1,2,5,1,4),_DiffServActionMinThreshold_Type())
diffServActionMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServActionMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:diffServActionMinThreshold.setUnits(_R)
_DiffServActionMaxThreshold_Type=Unsigned32
_DiffServActionMaxThreshold_Object=MibTableColumn
diffServActionMaxThreshold=_DiffServActionMaxThreshold_Object((1,3,6,1,4,1,89,51,1,2,5,1,5),_DiffServActionMaxThreshold_Type())
diffServActionMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServActionMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:diffServActionMaxThreshold.setUnits(_R)
class _DiffServActionDropPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('alwaysDrop',2),('tailDrop',3),('randomDrop',4)))
_DiffServActionDropPolicy_Type.__name__=_D
_DiffServActionDropPolicy_Object=MibTableColumn
diffServActionDropPolicy=_DiffServActionDropPolicy_Object((1,3,6,1,4,1,89,51,1,2,5,1,6),_DiffServActionDropPolicy_Type())
diffServActionDropPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServActionDropPolicy.setStatus(_A)
_DiffServActionHCConformingPackets_Type=Counter64
_DiffServActionHCConformingPackets_Object=MibTableColumn
diffServActionHCConformingPackets=_DiffServActionHCConformingPackets_Object((1,3,6,1,4,1,89,51,1,2,5,1,7),_DiffServActionHCConformingPackets_Type())
diffServActionHCConformingPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionHCConformingPackets.setStatus(_A)
if mibBuilder.loadTexts:diffServActionHCConformingPackets.setUnits(_K)
_DiffServActionConformingPackets_Type=Counter32
_DiffServActionConformingPackets_Object=MibTableColumn
diffServActionConformingPackets=_DiffServActionConformingPackets_Object((1,3,6,1,4,1,89,51,1,2,5,1,8),_DiffServActionConformingPackets_Type())
diffServActionConformingPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionConformingPackets.setStatus(_A)
if mibBuilder.loadTexts:diffServActionConformingPackets.setUnits(_K)
_DiffServActionHCConformingOctets_Type=Counter64
_DiffServActionHCConformingOctets_Object=MibTableColumn
diffServActionHCConformingOctets=_DiffServActionHCConformingOctets_Object((1,3,6,1,4,1,89,51,1,2,5,1,9),_DiffServActionHCConformingOctets_Type())
diffServActionHCConformingOctets.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionHCConformingOctets.setStatus(_A)
if mibBuilder.loadTexts:diffServActionHCConformingOctets.setUnits(_K)
_DiffServActionConformingOctets_Type=Counter32
_DiffServActionConformingOctets_Object=MibTableColumn
diffServActionConformingOctets=_DiffServActionConformingOctets_Object((1,3,6,1,4,1,89,51,1,2,5,1,10),_DiffServActionConformingOctets_Type())
diffServActionConformingOctets.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionConformingOctets.setStatus(_A)
if mibBuilder.loadTexts:diffServActionConformingOctets.setUnits(_K)
_DiffServActionTailDrops_Type=Counter32
_DiffServActionTailDrops_Object=MibTableColumn
diffServActionTailDrops=_DiffServActionTailDrops_Object((1,3,6,1,4,1,89,51,1,2,5,1,11),_DiffServActionTailDrops_Type())
diffServActionTailDrops.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionTailDrops.setStatus(_A)
_DiffServActionHCTailDrops_Type=Counter64
_DiffServActionHCTailDrops_Object=MibTableColumn
diffServActionHCTailDrops=_DiffServActionHCTailDrops_Object((1,3,6,1,4,1,89,51,1,2,5,1,12),_DiffServActionHCTailDrops_Type())
diffServActionHCTailDrops.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionHCTailDrops.setStatus(_A)
_DiffServActionRandomDrops_Type=Counter32
_DiffServActionRandomDrops_Object=MibTableColumn
diffServActionRandomDrops=_DiffServActionRandomDrops_Object((1,3,6,1,4,1,89,51,1,2,5,1,13),_DiffServActionRandomDrops_Type())
diffServActionRandomDrops.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionRandomDrops.setStatus(_A)
_DiffServActionHCRandomDrops_Type=Counter64
_DiffServActionHCRandomDrops_Object=MibTableColumn
diffServActionHCRandomDrops=_DiffServActionHCRandomDrops_Object((1,3,6,1,4,1,89,51,1,2,5,1,14),_DiffServActionHCRandomDrops_Type())
diffServActionHCRandomDrops.setMaxAccess(_F)
if mibBuilder.loadTexts:diffServActionHCRandomDrops.setStatus(_A)
_DiffServActionStatus_Type=RowStatus
_DiffServActionStatus_Object=MibTableColumn
diffServActionStatus=_DiffServActionStatus_Object((1,3,6,1,4,1,89,51,1,2,5,1,15),_DiffServActionStatus_Type())
diffServActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServActionStatus.setStatus(_A)
_DiffServQueueTable_Object=MibTable
diffServQueueTable=_DiffServQueueTable_Object((1,3,6,1,4,1,89,51,1,2,6))
if mibBuilder.loadTexts:diffServQueueTable.setStatus(_A)
_DiffServQueueEntry_Object=MibTableRow
diffServQueueEntry=_DiffServQueueEntry_Object((1,3,6,1,4,1,89,51,1,2,6,1))
diffServQueueEntry.setIndexNames((0,_G,_H),(0,_E,_J),(0,_E,_S))
if mibBuilder.loadTexts:diffServQueueEntry.setStatus(_A)
class _DiffServQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DiffServQueueNumber_Type.__name__=_D
_DiffServQueueNumber_Object=MibTableColumn
diffServQueueNumber=_DiffServQueueNumber_Object((1,3,6,1,4,1,89,51,1,2,6,1,1),_DiffServQueueNumber_Type())
diffServQueueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:diffServQueueNumber.setStatus(_A)
_DiffServQueueMinimumRate_Type=Unsigned32
_DiffServQueueMinimumRate_Object=MibTableColumn
diffServQueueMinimumRate=_DiffServQueueMinimumRate_Object((1,3,6,1,4,1,89,51,1,2,6,1,2),_DiffServQueueMinimumRate_Type())
diffServQueueMinimumRate.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServQueueMinimumRate.setStatus(_A)
if mibBuilder.loadTexts:diffServQueueMinimumRate.setUnits('KBPS')
_DiffServQueueMaximumRate_Type=Unsigned32
_DiffServQueueMaximumRate_Object=MibTableColumn
diffServQueueMaximumRate=_DiffServQueueMaximumRate_Object((1,3,6,1,4,1,89,51,1,2,6,1,3),_DiffServQueueMaximumRate_Type())
diffServQueueMaximumRate.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServQueueMaximumRate.setStatus(_A)
if mibBuilder.loadTexts:diffServQueueMaximumRate.setUnits('KBPS')
_DiffServQueuePriority_Type=Unsigned32
_DiffServQueuePriority_Object=MibTableColumn
diffServQueuePriority=_DiffServQueuePriority_Object((1,3,6,1,4,1,89,51,1,2,6,1,4),_DiffServQueuePriority_Type())
diffServQueuePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServQueuePriority.setStatus(_A)
class _DiffServQueueNextTCB_Type(RowPointer):defaultValue=0,0
_DiffServQueueNextTCB_Type.__name__=_I
_DiffServQueueNextTCB_Object=MibTableColumn
diffServQueueNextTCB=_DiffServQueueNextTCB_Object((1,3,6,1,4,1,89,51,1,2,6,1,5),_DiffServQueueNextTCB_Type())
diffServQueueNextTCB.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServQueueNextTCB.setStatus(_A)
_DiffServQueueOccupancyWeight_Type=Unsigned32
_DiffServQueueOccupancyWeight_Object=MibTableColumn
diffServQueueOccupancyWeight=_DiffServQueueOccupancyWeight_Object((1,3,6,1,4,1,89,51,1,2,6,1,6),_DiffServQueueOccupancyWeight_Type())
diffServQueueOccupancyWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServQueueOccupancyWeight.setStatus(_A)
_DiffServQueueStatus_Type=RowStatus
_DiffServQueueStatus_Object=MibTableColumn
diffServQueueStatus=_DiffServQueueStatus_Object((1,3,6,1,4,1,89,51,1,2,6,1,7),_DiffServQueueStatus_Type())
diffServQueueStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServQueueStatus.setStatus(_A)
_DiffServMIBConformance_ObjectIdentity=ObjectIdentity
diffServMIBConformance=_DiffServMIBConformance_ObjectIdentity((1,3,6,1,4,1,89,51,1,3))
mibBuilder.exportSymbols(_E,**{'Dscp':Dscp,'MFClassifierL4Port':MFClassifierL4Port,'diffServMib':diffServMib,'diffServObjects':diffServObjects,'diffServMFClassifierUnique':diffServMFClassifierUnique,'diffServClassifierUnique':diffServClassifierUnique,'diffServTBMeterUnique':diffServTBMeterUnique,'diffServActionUnique':diffServActionUnique,'diffServQueueUnique':diffServQueueUnique,'diffServTables':diffServTables,'diffServAggregateTable':diffServAggregateTable,'diffServAggregateEntry':diffServAggregateEntry,_M:diffServAggregateDSCP,'diffServMFClassifierTable':diffServMFClassifierTable,'diffServMFClassifierEntry':diffServMFClassifierEntry,_N:diffServMFClassifierIndex,'diffServMFClassifierAddrType':diffServMFClassifierAddrType,'diffServMFClassifierDstAddr':diffServMFClassifierDstAddr,'diffServMFClassifierDstAddrMask':diffServMFClassifierDstAddrMask,'diffServMFClassifierSrcAddr':diffServMFClassifierSrcAddr,'diffServMFClassifierSrcAddrMask':diffServMFClassifierSrcAddrMask,'diffServMFClassifierDscp':diffServMFClassifierDscp,'diffServMFClassifierProtocol':diffServMFClassifierProtocol,'diffServMFClassifierDstL4PortMin':diffServMFClassifierDstL4PortMin,'diffServMFClassifierDstL4PortMax':diffServMFClassifierDstL4PortMax,'diffServMFClassifierSrcL4PortMin':diffServMFClassifierSrcL4PortMin,'diffServMFClassifierSrcL4PortMax':diffServMFClassifierSrcL4PortMax,'diffServMFClassifierStatus':diffServMFClassifierStatus,'diffServClassifierTable':diffServClassifierTable,'diffServClassifierEntry':diffServClassifierEntry,_J:diffServInterfaceDirection,_O:diffServClassifierNumber,'diffServClassifierMatchObject':diffServClassifierMatchObject,'diffServClassifierNext':diffServClassifierNext,'diffServClassifierSequence':diffServClassifierSequence,'diffServClassifierConfigType':diffServClassifierConfigType,'diffServClassifierConfigTypeInfo':diffServClassifierConfigTypeInfo,'diffServClassifierStatus':diffServClassifierStatus,'diffServTBMeterTable':diffServTBMeterTable,'diffServTBMeterEntry':diffServTBMeterEntry,_P:diffServTBMeterNumber,'diffServTBMeterInterval':diffServTBMeterInterval,'diffServTBMeterBurstSize':diffServTBMeterBurstSize,'diffServTBMeterFailNext':diffServTBMeterFailNext,'diffServTBMeterSucceedNext':diffServTBMeterSucceedNext,'diffServTBMeterStatus':diffServTBMeterStatus,'diffServActionTable':diffServActionTable,'diffServActionEntry':diffServActionEntry,_Q:diffServActionNumber,'diffServActionNext':diffServActionNext,'diffServActionDSCP':diffServActionDSCP,'diffServActionMinThreshold':diffServActionMinThreshold,'diffServActionMaxThreshold':diffServActionMaxThreshold,'diffServActionDropPolicy':diffServActionDropPolicy,'diffServActionHCConformingPackets':diffServActionHCConformingPackets,'diffServActionConformingPackets':diffServActionConformingPackets,'diffServActionHCConformingOctets':diffServActionHCConformingOctets,'diffServActionConformingOctets':diffServActionConformingOctets,'diffServActionTailDrops':diffServActionTailDrops,'diffServActionHCTailDrops':diffServActionHCTailDrops,'diffServActionRandomDrops':diffServActionRandomDrops,'diffServActionHCRandomDrops':diffServActionHCRandomDrops,'diffServActionStatus':diffServActionStatus,'diffServQueueTable':diffServQueueTable,'diffServQueueEntry':diffServQueueEntry,_S:diffServQueueNumber,'diffServQueueMinimumRate':diffServQueueMinimumRate,'diffServQueueMaximumRate':diffServQueueMaximumRate,'diffServQueuePriority':diffServQueuePriority,'diffServQueueNextTCB':diffServQueueNextTCB,'diffServQueueOccupancyWeight':diffServQueueOccupancyWeight,'diffServQueueStatus':diffServQueueStatus,'diffServMIBConformance':diffServMIBConformance})