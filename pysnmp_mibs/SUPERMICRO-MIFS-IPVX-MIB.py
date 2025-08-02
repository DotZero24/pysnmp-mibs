_S='fsMIIpvxTraceHopCount'
_R='fsMIIpvxTraceAddr'
_Q='fsMIIpvxTraceAddrType'
_P='fsMIIpvxTraceConfigDest'
_O='fsMIIpvxTraceConfigAddrType'
_N='fsMIIpvxTraceConfigIndex'
_M='fsMIIpvxAddrPrefixLen'
_L='fsMIIpvxAddrPrefix'
_K='fsMIIpvxAddrPrefixAddrType'
_J='fsMIIpvxAddrPrefixIfIndex'
_I='TruthValue'
_H='read-create'
_G='InetAddress'
_F='read-write'
_E='read-only'
_D='not-accessible'
_C='SUPERMICRO-MIFS-IPVX-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
fsMIFsIpvx=ModuleIdentity((1,3,6,1,4,1,10876,101,2,34))
if mibBuilder.loadTexts:fsMIFsIpvx.setRevisions(('2012-09-05 00:00',))
_FsMIIpvxAddrPrefixTable_Object=MibTable
fsMIIpvxAddrPrefixTable=_FsMIIpvxAddrPrefixTable_Object((1,3,6,1,4,1,10876,101,2,34,1))
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixTable.setStatus(_A)
_FsMIIpvxAddrPrefixEntry_Object=MibTableRow
fsMIIpvxAddrPrefixEntry=_FsMIIpvxAddrPrefixEntry_Object((1,3,6,1,4,1,10876,101,2,34,1,1))
fsMIIpvxAddrPrefixEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixEntry.setStatus(_A)
_FsMIIpvxAddrPrefixIfIndex_Type=InterfaceIndex
_FsMIIpvxAddrPrefixIfIndex_Object=MibTableColumn
fsMIIpvxAddrPrefixIfIndex=_FsMIIpvxAddrPrefixIfIndex_Object((1,3,6,1,4,1,10876,101,2,34,1,1,1),_FsMIIpvxAddrPrefixIfIndex_Type())
fsMIIpvxAddrPrefixIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixIfIndex.setStatus(_A)
_FsMIIpvxAddrPrefixAddrType_Type=InetAddressType
_FsMIIpvxAddrPrefixAddrType_Object=MibTableColumn
fsMIIpvxAddrPrefixAddrType=_FsMIIpvxAddrPrefixAddrType_Object((1,3,6,1,4,1,10876,101,2,34,1,1,2),_FsMIIpvxAddrPrefixAddrType_Type())
fsMIIpvxAddrPrefixAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixAddrType.setStatus(_A)
class _FsMIIpvxAddrPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpvxAddrPrefix_Type.__name__=_G
_FsMIIpvxAddrPrefix_Object=MibTableColumn
fsMIIpvxAddrPrefix=_FsMIIpvxAddrPrefix_Object((1,3,6,1,4,1,10876,101,2,34,1,1,3),_FsMIIpvxAddrPrefix_Type())
fsMIIpvxAddrPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefix.setStatus(_A)
_FsMIIpvxAddrPrefixLen_Type=InetAddressPrefixLength
_FsMIIpvxAddrPrefixLen_Object=MibTableColumn
fsMIIpvxAddrPrefixLen=_FsMIIpvxAddrPrefixLen_Object((1,3,6,1,4,1,10876,101,2,34,1,1,4),_FsMIIpvxAddrPrefixLen_Type())
fsMIIpvxAddrPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixLen.setStatus(_A)
_FsMIIpvxAddrPrefixContextId_Type=Integer32
_FsMIIpvxAddrPrefixContextId_Object=MibTableColumn
fsMIIpvxAddrPrefixContextId=_FsMIIpvxAddrPrefixContextId_Object((1,3,6,1,4,1,10876,101,2,34,1,1,5),_FsMIIpvxAddrPrefixContextId_Type())
fsMIIpvxAddrPrefixContextId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixContextId.setStatus(_A)
_FsMIIpvxAddrPrefixProfileIndex_Type=Unsigned32
_FsMIIpvxAddrPrefixProfileIndex_Object=MibTableColumn
fsMIIpvxAddrPrefixProfileIndex=_FsMIIpvxAddrPrefixProfileIndex_Object((1,3,6,1,4,1,10876,101,2,34,1,1,6),_FsMIIpvxAddrPrefixProfileIndex_Type())
fsMIIpvxAddrPrefixProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixProfileIndex.setStatus(_A)
class _FsMIIpvxAddrPrefixSecAddrFlag_Type(TruthValue):defaultValue=1
_FsMIIpvxAddrPrefixSecAddrFlag_Type.__name__=_I
_FsMIIpvxAddrPrefixSecAddrFlag_Object=MibTableColumn
fsMIIpvxAddrPrefixSecAddrFlag=_FsMIIpvxAddrPrefixSecAddrFlag_Object((1,3,6,1,4,1,10876,101,2,34,1,1,7),_FsMIIpvxAddrPrefixSecAddrFlag_Type())
fsMIIpvxAddrPrefixSecAddrFlag.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixSecAddrFlag.setStatus(_A)
_FsMIIpvxAddrPrefixRowStatus_Type=RowStatus
_FsMIIpvxAddrPrefixRowStatus_Object=MibTableColumn
fsMIIpvxAddrPrefixRowStatus=_FsMIIpvxAddrPrefixRowStatus_Object((1,3,6,1,4,1,10876,101,2,34,1,1,8),_FsMIIpvxAddrPrefixRowStatus_Type())
fsMIIpvxAddrPrefixRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIIpvxAddrPrefixRowStatus.setStatus(_A)
_FsMIIpvxTraceConfigTable_Object=MibTable
fsMIIpvxTraceConfigTable=_FsMIIpvxTraceConfigTable_Object((1,3,6,1,4,1,10876,101,2,34,2))
if mibBuilder.loadTexts:fsMIIpvxTraceConfigTable.setStatus(_A)
_FsMIIpvxTraceConfigEntry_Object=MibTableRow
fsMIIpvxTraceConfigEntry=_FsMIIpvxTraceConfigEntry_Object((1,3,6,1,4,1,10876,101,2,34,2,1))
fsMIIpvxTraceConfigEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:fsMIIpvxTraceConfigEntry.setStatus(_A)
class _FsMIIpvxTraceConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsMIIpvxTraceConfigIndex_Type.__name__=_B
_FsMIIpvxTraceConfigIndex_Object=MibTableColumn
fsMIIpvxTraceConfigIndex=_FsMIIpvxTraceConfigIndex_Object((1,3,6,1,4,1,10876,101,2,34,2,1,1),_FsMIIpvxTraceConfigIndex_Type())
fsMIIpvxTraceConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigIndex.setStatus(_A)
_FsMIIpvxTraceConfigAddrType_Type=InetAddressType
_FsMIIpvxTraceConfigAddrType_Object=MibTableColumn
fsMIIpvxTraceConfigAddrType=_FsMIIpvxTraceConfigAddrType_Object((1,3,6,1,4,1,10876,101,2,34,2,1,2),_FsMIIpvxTraceConfigAddrType_Type())
fsMIIpvxTraceConfigAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigAddrType.setStatus(_A)
class _FsMIIpvxTraceConfigDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpvxTraceConfigDest_Type.__name__=_G
_FsMIIpvxTraceConfigDest_Object=MibTableColumn
fsMIIpvxTraceConfigDest=_FsMIIpvxTraceConfigDest_Object((1,3,6,1,4,1,10876,101,2,34,2,1,3),_FsMIIpvxTraceConfigDest_Type())
fsMIIpvxTraceConfigDest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigDest.setStatus(_A)
class _FsMIIpvxTraceConfigAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FsMIIpvxTraceConfigAdminStatus_Type.__name__=_B
_FsMIIpvxTraceConfigAdminStatus_Object=MibTableColumn
fsMIIpvxTraceConfigAdminStatus=_FsMIIpvxTraceConfigAdminStatus_Object((1,3,6,1,4,1,10876,101,2,34,2,1,4),_FsMIIpvxTraceConfigAdminStatus_Type())
fsMIIpvxTraceConfigAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigAdminStatus.setStatus(_A)
class _FsMIIpvxTraceConfigMaxTTL_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_FsMIIpvxTraceConfigMaxTTL_Type.__name__=_B
_FsMIIpvxTraceConfigMaxTTL_Object=MibTableColumn
fsMIIpvxTraceConfigMaxTTL=_FsMIIpvxTraceConfigMaxTTL_Object((1,3,6,1,4,1,10876,101,2,34,2,1,5),_FsMIIpvxTraceConfigMaxTTL_Type())
fsMIIpvxTraceConfigMaxTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigMaxTTL.setStatus(_A)
class _FsMIIpvxTraceConfigMinTTL_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_FsMIIpvxTraceConfigMinTTL_Type.__name__=_B
_FsMIIpvxTraceConfigMinTTL_Object=MibTableColumn
fsMIIpvxTraceConfigMinTTL=_FsMIIpvxTraceConfigMinTTL_Object((1,3,6,1,4,1,10876,101,2,34,2,1,6),_FsMIIpvxTraceConfigMinTTL_Type())
fsMIIpvxTraceConfigMinTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigMinTTL.setStatus(_A)
class _FsMIIpvxTraceConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inprogress',1),('notinprogress',2)))
_FsMIIpvxTraceConfigOperStatus_Type.__name__=_B
_FsMIIpvxTraceConfigOperStatus_Object=MibTableColumn
fsMIIpvxTraceConfigOperStatus=_FsMIIpvxTraceConfigOperStatus_Object((1,3,6,1,4,1,10876,101,2,34,2,1,7),_FsMIIpvxTraceConfigOperStatus_Type())
fsMIIpvxTraceConfigOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigOperStatus.setStatus(_A)
class _FsMIIpvxTraceConfigTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIIpvxTraceConfigTimeout_Type.__name__=_B
_FsMIIpvxTraceConfigTimeout_Object=MibTableColumn
fsMIIpvxTraceConfigTimeout=_FsMIIpvxTraceConfigTimeout_Object((1,3,6,1,4,1,10876,101,2,34,2,1,8),_FsMIIpvxTraceConfigTimeout_Type())
fsMIIpvxTraceConfigTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigTimeout.setStatus(_A)
class _FsMIIpvxTraceConfigMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIIpvxTraceConfigMtu_Type.__name__=_B
_FsMIIpvxTraceConfigMtu_Object=MibTableColumn
fsMIIpvxTraceConfigMtu=_FsMIIpvxTraceConfigMtu_Object((1,3,6,1,4,1,10876,101,2,34,2,1,9),_FsMIIpvxTraceConfigMtu_Type())
fsMIIpvxTraceConfigMtu.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigMtu.setStatus(_A)
class _FsMIIpvxTraceConfigCxtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpvxTraceConfigCxtId_Type.__name__=_B
_FsMIIpvxTraceConfigCxtId_Object=MibTableColumn
fsMIIpvxTraceConfigCxtId=_FsMIIpvxTraceConfigCxtId_Object((1,3,6,1,4,1,10876,101,2,34,2,1,10),_FsMIIpvxTraceConfigCxtId_Type())
fsMIIpvxTraceConfigCxtId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpvxTraceConfigCxtId.setStatus(_A)
_FsMIIpvxTraceTable_Object=MibTable
fsMIIpvxTraceTable=_FsMIIpvxTraceTable_Object((1,3,6,1,4,1,10876,101,2,34,3))
if mibBuilder.loadTexts:fsMIIpvxTraceTable.setStatus(_A)
_FsMIIpvxTraceEntry_Object=MibTableRow
fsMIIpvxTraceEntry=_FsMIIpvxTraceEntry_Object((1,3,6,1,4,1,10876,101,2,34,3,1))
fsMIIpvxTraceEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:fsMIIpvxTraceEntry.setStatus(_A)
class _FsMIIpvxTraceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsMIIpvxTraceIndex_Type.__name__=_B
_FsMIIpvxTraceIndex_Object=MibTableColumn
fsMIIpvxTraceIndex=_FsMIIpvxTraceIndex_Object((1,3,6,1,4,1,10876,101,2,34,3,1,1),_FsMIIpvxTraceIndex_Type())
fsMIIpvxTraceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceIndex.setStatus(_A)
_FsMIIpvxTraceAddrType_Type=InetAddressType
_FsMIIpvxTraceAddrType_Object=MibTableColumn
fsMIIpvxTraceAddrType=_FsMIIpvxTraceAddrType_Object((1,3,6,1,4,1,10876,101,2,34,3,1,2),_FsMIIpvxTraceAddrType_Type())
fsMIIpvxTraceAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceAddrType.setStatus(_A)
class _FsMIIpvxTraceAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpvxTraceAddr_Type.__name__=_G
_FsMIIpvxTraceAddr_Object=MibTableColumn
fsMIIpvxTraceAddr=_FsMIIpvxTraceAddr_Object((1,3,6,1,4,1,10876,101,2,34,3,1,3),_FsMIIpvxTraceAddr_Type())
fsMIIpvxTraceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceAddr.setStatus(_A)
class _FsMIIpvxTraceHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIIpvxTraceHopCount_Type.__name__=_B
_FsMIIpvxTraceHopCount_Object=MibTableColumn
fsMIIpvxTraceHopCount=_FsMIIpvxTraceHopCount_Object((1,3,6,1,4,1,10876,101,2,34,3,1,4),_FsMIIpvxTraceHopCount_Type())
fsMIIpvxTraceHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpvxTraceHopCount.setStatus(_A)
class _FsMIIpvxTraceIntermHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpvxTraceIntermHop_Type.__name__=_G
_FsMIIpvxTraceIntermHop_Object=MibTableColumn
fsMIIpvxTraceIntermHop=_FsMIIpvxTraceIntermHop_Object((1,3,6,1,4,1,10876,101,2,34,3,1,5),_FsMIIpvxTraceIntermHop_Type())
fsMIIpvxTraceIntermHop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxTraceIntermHop.setStatus(_A)
class _FsMIIpvxTraceReachTime1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIIpvxTraceReachTime1_Type.__name__=_B
_FsMIIpvxTraceReachTime1_Object=MibTableColumn
fsMIIpvxTraceReachTime1=_FsMIIpvxTraceReachTime1_Object((1,3,6,1,4,1,10876,101,2,34,3,1,6),_FsMIIpvxTraceReachTime1_Type())
fsMIIpvxTraceReachTime1.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxTraceReachTime1.setStatus(_A)
class _FsMIIpvxTraceReachTime2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIIpvxTraceReachTime2_Type.__name__=_B
_FsMIIpvxTraceReachTime2_Object=MibTableColumn
fsMIIpvxTraceReachTime2=_FsMIIpvxTraceReachTime2_Object((1,3,6,1,4,1,10876,101,2,34,3,1,7),_FsMIIpvxTraceReachTime2_Type())
fsMIIpvxTraceReachTime2.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxTraceReachTime2.setStatus(_A)
class _FsMIIpvxTraceReachTime3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIIpvxTraceReachTime3_Type.__name__=_B
_FsMIIpvxTraceReachTime3_Object=MibTableColumn
fsMIIpvxTraceReachTime3=_FsMIIpvxTraceReachTime3_Object((1,3,6,1,4,1,10876,101,2,34,3,1,8),_FsMIIpvxTraceReachTime3_Type())
fsMIIpvxTraceReachTime3.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxTraceReachTime3.setStatus(_A)
class _FsMIIpvxTraceCxtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpvxTraceCxtId_Type.__name__=_B
_FsMIIpvxTraceCxtId_Object=MibTableColumn
fsMIIpvxTraceCxtId=_FsMIIpvxTraceCxtId_Object((1,3,6,1,4,1,10876,101,2,34,3,1,9),_FsMIIpvxTraceCxtId_Type())
fsMIIpvxTraceCxtId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIIpvxTraceCxtId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsMIFsIpvx':fsMIFsIpvx,'fsMIIpvxAddrPrefixTable':fsMIIpvxAddrPrefixTable,'fsMIIpvxAddrPrefixEntry':fsMIIpvxAddrPrefixEntry,_J:fsMIIpvxAddrPrefixIfIndex,_K:fsMIIpvxAddrPrefixAddrType,_L:fsMIIpvxAddrPrefix,_M:fsMIIpvxAddrPrefixLen,'fsMIIpvxAddrPrefixContextId':fsMIIpvxAddrPrefixContextId,'fsMIIpvxAddrPrefixProfileIndex':fsMIIpvxAddrPrefixProfileIndex,'fsMIIpvxAddrPrefixSecAddrFlag':fsMIIpvxAddrPrefixSecAddrFlag,'fsMIIpvxAddrPrefixRowStatus':fsMIIpvxAddrPrefixRowStatus,'fsMIIpvxTraceConfigTable':fsMIIpvxTraceConfigTable,'fsMIIpvxTraceConfigEntry':fsMIIpvxTraceConfigEntry,_N:fsMIIpvxTraceConfigIndex,_O:fsMIIpvxTraceConfigAddrType,_P:fsMIIpvxTraceConfigDest,'fsMIIpvxTraceConfigAdminStatus':fsMIIpvxTraceConfigAdminStatus,'fsMIIpvxTraceConfigMaxTTL':fsMIIpvxTraceConfigMaxTTL,'fsMIIpvxTraceConfigMinTTL':fsMIIpvxTraceConfigMinTTL,'fsMIIpvxTraceConfigOperStatus':fsMIIpvxTraceConfigOperStatus,'fsMIIpvxTraceConfigTimeout':fsMIIpvxTraceConfigTimeout,'fsMIIpvxTraceConfigMtu':fsMIIpvxTraceConfigMtu,'fsMIIpvxTraceConfigCxtId':fsMIIpvxTraceConfigCxtId,'fsMIIpvxTraceTable':fsMIIpvxTraceTable,'fsMIIpvxTraceEntry':fsMIIpvxTraceEntry,'fsMIIpvxTraceIndex':fsMIIpvxTraceIndex,_Q:fsMIIpvxTraceAddrType,_R:fsMIIpvxTraceAddr,_S:fsMIIpvxTraceHopCount,'fsMIIpvxTraceIntermHop':fsMIIpvxTraceIntermHop,'fsMIIpvxTraceReachTime1':fsMIIpvxTraceReachTime1,'fsMIIpvxTraceReachTime2':fsMIIpvxTraceReachTime2,'fsMIIpvxTraceReachTime3':fsMIIpvxTraceReachTime3,'fsMIIpvxTraceCxtId':fsMIIpvxTraceCxtId})