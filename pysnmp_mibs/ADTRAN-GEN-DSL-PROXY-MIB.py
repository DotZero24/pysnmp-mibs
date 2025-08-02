_d='adGenDslProxyLoopbackStatus'
_c='adGenDslProxySetLoopback'
_b='adGenDslProxyNumRepeaters'
_a='adGenDslProxySystemType'
_Z='adGenDslProxySystemLastError'
_Y='adGenDslProxySystemValid'
_X='adGenDslProxyFrameGroundLastTime'
_W='adGenDslProxyFrameGroundInitiate'
_V='adGenDslProxySpliceDetectLastTime'
_U='adGenDslProxySpliceDetectStatus'
_T='adGenDslProxySpliceDetectInitiate'
_S='adGenDslProxyLoopbackStatusLastTime'
_R='adGenDslProxyLoopbackStatusStatus'
_Q='adGenDslProxyLoopbackStatusInitiate'
_P='adGenDslProxySystemTypeLastTime'
_O='adGenDslProxySystemTypeStatus'
_N='adGenDslProxySystemTypeInitiate'
_M='bilateral'
_L='customer'
_K='network'
_J='adEShdslInvIndex'
_I='ADTRAN-SHDSL-MIB'
_H='adGenDslProxyFrameGroundStatus'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='ADTRAN-GEN-DSL-PROXY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenDslProxy,adGenDslProxyID=mibBuilder.importSymbols('ADTRAN-SHARED-SHDSL-MIB','adGenDslProxy','adGenDslProxyID')
adEShdslInvIndex,=mibBuilder.importSymbols(_I,_J)
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenDslProxyMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,59,4,1))
if mibBuilder.loadTexts:adGenDslProxyMIB.setRevisions(('2009-06-08 00:00',))
class AdGenDslProxyInitiate(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiate',1))
class AdGenDslProxyStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('neverActivated',1),('inProgress',2),('resultsValid',3),('error',4)))
class AdGenDslProxyLastTime(TimeTicks):0
_AdGenDslProxyCommands_ObjectIdentity=ObjectIdentity
adGenDslProxyCommands=_AdGenDslProxyCommands_ObjectIdentity((1,3,6,1,4,1,664,5,59,4,1))
_AdGenDslProxyCommandTable_Object=MibTable
adGenDslProxyCommandTable=_AdGenDslProxyCommandTable_Object((1,3,6,1,4,1,664,5,59,4,1,1))
if mibBuilder.loadTexts:adGenDslProxyCommandTable.setStatus(_A)
_AdGenDslProxyCommandEntry_Object=MibTableRow
adGenDslProxyCommandEntry=_AdGenDslProxyCommandEntry_Object((1,3,6,1,4,1,664,5,59,4,1,1,1))
adGenDslProxyCommandEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDslProxyCommandEntry.setStatus(_A)
_AdGenDslProxySystemTypeInitiate_Type=AdGenDslProxyInitiate
_AdGenDslProxySystemTypeInitiate_Object=MibTableColumn
adGenDslProxySystemTypeInitiate=_AdGenDslProxySystemTypeInitiate_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,1),_AdGenDslProxySystemTypeInitiate_Type())
adGenDslProxySystemTypeInitiate.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDslProxySystemTypeInitiate.setStatus(_A)
_AdGenDslProxySystemTypeStatus_Type=AdGenDslProxyStatus
_AdGenDslProxySystemTypeStatus_Object=MibTableColumn
adGenDslProxySystemTypeStatus=_AdGenDslProxySystemTypeStatus_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,2),_AdGenDslProxySystemTypeStatus_Type())
adGenDslProxySystemTypeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySystemTypeStatus.setStatus(_A)
_AdGenDslProxySystemTypeLastTime_Type=AdGenDslProxyLastTime
_AdGenDslProxySystemTypeLastTime_Object=MibTableColumn
adGenDslProxySystemTypeLastTime=_AdGenDslProxySystemTypeLastTime_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,3),_AdGenDslProxySystemTypeLastTime_Type())
adGenDslProxySystemTypeLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySystemTypeLastTime.setStatus(_A)
_AdGenDslProxyLoopbackStatusInitiate_Type=AdGenDslProxyInitiate
_AdGenDslProxyLoopbackStatusInitiate_Object=MibTableColumn
adGenDslProxyLoopbackStatusInitiate=_AdGenDslProxyLoopbackStatusInitiate_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,4),_AdGenDslProxyLoopbackStatusInitiate_Type())
adGenDslProxyLoopbackStatusInitiate.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDslProxyLoopbackStatusInitiate.setStatus(_A)
_AdGenDslProxyLoopbackStatusStatus_Type=AdGenDslProxyStatus
_AdGenDslProxyLoopbackStatusStatus_Object=MibTableColumn
adGenDslProxyLoopbackStatusStatus=_AdGenDslProxyLoopbackStatusStatus_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,5),_AdGenDslProxyLoopbackStatusStatus_Type())
adGenDslProxyLoopbackStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyLoopbackStatusStatus.setStatus(_A)
_AdGenDslProxyLoopbackStatusLastTime_Type=AdGenDslProxyLastTime
_AdGenDslProxyLoopbackStatusLastTime_Object=MibTableColumn
adGenDslProxyLoopbackStatusLastTime=_AdGenDslProxyLoopbackStatusLastTime_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,6),_AdGenDslProxyLoopbackStatusLastTime_Type())
adGenDslProxyLoopbackStatusLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyLoopbackStatusLastTime.setStatus(_A)
_AdGenDslProxySpliceDetectInitiate_Type=AdGenDslProxyInitiate
_AdGenDslProxySpliceDetectInitiate_Object=MibTableColumn
adGenDslProxySpliceDetectInitiate=_AdGenDslProxySpliceDetectInitiate_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,7),_AdGenDslProxySpliceDetectInitiate_Type())
adGenDslProxySpliceDetectInitiate.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDslProxySpliceDetectInitiate.setStatus(_A)
_AdGenDslProxySpliceDetectStatus_Type=AdGenDslProxyStatus
_AdGenDslProxySpliceDetectStatus_Object=MibTableColumn
adGenDslProxySpliceDetectStatus=_AdGenDslProxySpliceDetectStatus_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,8),_AdGenDslProxySpliceDetectStatus_Type())
adGenDslProxySpliceDetectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySpliceDetectStatus.setStatus(_A)
_AdGenDslProxySpliceDetectLastTime_Type=AdGenDslProxyLastTime
_AdGenDslProxySpliceDetectLastTime_Object=MibTableColumn
adGenDslProxySpliceDetectLastTime=_AdGenDslProxySpliceDetectLastTime_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,9),_AdGenDslProxySpliceDetectLastTime_Type())
adGenDslProxySpliceDetectLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySpliceDetectLastTime.setStatus(_A)
_AdGenDslProxyFrameGroundInitiate_Type=AdGenDslProxyInitiate
_AdGenDslProxyFrameGroundInitiate_Object=MibTableColumn
adGenDslProxyFrameGroundInitiate=_AdGenDslProxyFrameGroundInitiate_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,10),_AdGenDslProxyFrameGroundInitiate_Type())
adGenDslProxyFrameGroundInitiate.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDslProxyFrameGroundInitiate.setStatus(_A)
_AdGenDslProxyFrameGroundStatus_Type=AdGenDslProxyStatus
_AdGenDslProxyFrameGroundStatus_Object=MibTableColumn
adGenDslProxyFrameGroundStatus=_AdGenDslProxyFrameGroundStatus_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,11),_AdGenDslProxyFrameGroundStatus_Type())
adGenDslProxyFrameGroundStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyFrameGroundStatus.setStatus(_A)
_AdGenDslProxyFrameGroundLastTime_Type=AdGenDslProxyLastTime
_AdGenDslProxyFrameGroundLastTime_Object=MibTableColumn
adGenDslProxyFrameGroundLastTime=_AdGenDslProxyFrameGroundLastTime_Object((1,3,6,1,4,1,664,5,59,4,1,1,1,12),_AdGenDslProxyFrameGroundLastTime_Type())
adGenDslProxyFrameGroundLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyFrameGroundLastTime.setStatus(_A)
_AdGenDslProxyResults_ObjectIdentity=ObjectIdentity
adGenDslProxyResults=_AdGenDslProxyResults_ObjectIdentity((1,3,6,1,4,1,664,5,59,4,2))
_AdGenDslProxySystemTable_Object=MibTable
adGenDslProxySystemTable=_AdGenDslProxySystemTable_Object((1,3,6,1,4,1,664,5,59,4,2,1))
if mibBuilder.loadTexts:adGenDslProxySystemTable.setStatus(_A)
_AdGenDslProxySystemEntry_Object=MibTableRow
adGenDslProxySystemEntry=_AdGenDslProxySystemEntry_Object((1,3,6,1,4,1,664,5,59,4,2,1,1))
adGenDslProxySystemEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDslProxySystemEntry.setStatus(_A)
class _AdGenDslProxySystemValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('valid',2),('invalid',3)))
_AdGenDslProxySystemValid_Type.__name__=_D
_AdGenDslProxySystemValid_Object=MibTableColumn
adGenDslProxySystemValid=_AdGenDslProxySystemValid_Object((1,3,6,1,4,1,664,5,59,4,2,1,1,1),_AdGenDslProxySystemValid_Type())
adGenDslProxySystemValid.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySystemValid.setStatus(_A)
_AdGenDslProxySystemLastError_Type=DisplayString
_AdGenDslProxySystemLastError_Object=MibTableColumn
adGenDslProxySystemLastError=_AdGenDslProxySystemLastError_Object((1,3,6,1,4,1,664,5,59,4,2,1,1,2),_AdGenDslProxySystemLastError_Type())
adGenDslProxySystemLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySystemLastError.setStatus(_A)
class _AdGenDslProxySystemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoWire',1),('fourWire',2)))
_AdGenDslProxySystemType_Type.__name__=_D
_AdGenDslProxySystemType_Object=MibTableColumn
adGenDslProxySystemType=_AdGenDslProxySystemType_Object((1,3,6,1,4,1,664,5,59,4,2,1,1,3),_AdGenDslProxySystemType_Type())
adGenDslProxySystemType.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxySystemType.setStatus(_A)
_AdGenDslProxyNumRepeaters_Type=Integer32
_AdGenDslProxyNumRepeaters_Object=MibTableColumn
adGenDslProxyNumRepeaters=_AdGenDslProxyNumRepeaters_Object((1,3,6,1,4,1,664,5,59,4,2,1,1,4),_AdGenDslProxyNumRepeaters_Type())
adGenDslProxyNumRepeaters.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyNumRepeaters.setStatus(_A)
_AdGenDslProxyLoopbackTable_Object=MibTable
adGenDslProxyLoopbackTable=_AdGenDslProxyLoopbackTable_Object((1,3,6,1,4,1,664,5,59,4,2,2))
if mibBuilder.loadTexts:adGenDslProxyLoopbackTable.setStatus(_A)
_AdGenDslProxyLoopbackEntry_Object=MibTableRow
adGenDslProxyLoopbackEntry=_AdGenDslProxyLoopbackEntry_Object((1,3,6,1,4,1,664,5,59,4,2,2,1))
adGenDslProxyLoopbackEntry.setIndexNames((0,_E,_F),(0,_I,_J))
if mibBuilder.loadTexts:adGenDslProxyLoopbackEntry.setStatus(_A)
class _AdGenDslProxySetLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_K,2),(_L,3),(_M,4)))
_AdGenDslProxySetLoopback_Type.__name__=_D
_AdGenDslProxySetLoopback_Object=MibTableColumn
adGenDslProxySetLoopback=_AdGenDslProxySetLoopback_Object((1,3,6,1,4,1,664,5,59,4,2,2,1,1),_AdGenDslProxySetLoopback_Type())
adGenDslProxySetLoopback.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDslProxySetLoopback.setStatus(_A)
class _AdGenDslProxyLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_K,2),(_L,3),(_M,4)))
_AdGenDslProxyLoopbackStatus_Type.__name__=_D
_AdGenDslProxyLoopbackStatus_Object=MibTableColumn
adGenDslProxyLoopbackStatus=_AdGenDslProxyLoopbackStatus_Object((1,3,6,1,4,1,664,5,59,4,2,2,1,2),_AdGenDslProxyLoopbackStatus_Type())
adGenDslProxyLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyLoopbackStatus.setStatus(_A)
_AdGenDslProxyFrameGroundTable_Object=MibTable
adGenDslProxyFrameGroundTable=_AdGenDslProxyFrameGroundTable_Object((1,3,6,1,4,1,664,5,59,4,2,3))
if mibBuilder.loadTexts:adGenDslProxyFrameGroundTable.setStatus(_A)
_AdGenDslProxyFrameGroundEntry_Object=MibTableRow
adGenDslProxyFrameGroundEntry=_AdGenDslProxyFrameGroundEntry_Object((1,3,6,1,4,1,664,5,59,4,2,3,1))
adGenDslProxyFrameGroundEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDslProxyFrameGroundEntry.setStatus(_A)
class _AdGenDslProxyFrameGroundResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('goodGround',1),('badGround',2)))
_AdGenDslProxyFrameGroundResult_Type.__name__=_D
_AdGenDslProxyFrameGroundResult_Object=MibTableColumn
adGenDslProxyFrameGroundResult=_AdGenDslProxyFrameGroundResult_Object((1,3,6,1,4,1,664,5,59,4,2,3,1,1),_AdGenDslProxyFrameGroundResult_Type())
adGenDslProxyFrameGroundResult.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenDslProxyFrameGroundResult.setStatus(_A)
_AdGenDslProxyMibConformance_ObjectIdentity=ObjectIdentity
adGenDslProxyMibConformance=_AdGenDslProxyMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,59,4,10))
_AdGenDslProxyMibGroups_ObjectIdentity=ObjectIdentity
adGenDslProxyMibGroups=_AdGenDslProxyMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,59,4,10,1))
adGenDslProxyCommandGroup=ObjectGroup((1,3,6,1,4,1,664,5,59,4,10,1,1))
adGenDslProxyCommandGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_H),(_B,_X)))
if mibBuilder.loadTexts:adGenDslProxyCommandGroup.setStatus(_A)
adGenDslProxySystemGroup=ObjectGroup((1,3,6,1,4,1,664,5,59,4,10,1,2))
adGenDslProxySystemGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:adGenDslProxySystemGroup.setStatus(_A)
adGenDslProxyLoopbackGroup=ObjectGroup((1,3,6,1,4,1,664,5,59,4,10,1,3))
adGenDslProxyLoopbackGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:adGenDslProxyLoopbackGroup.setStatus(_A)
adGenDslProxyFrameGroundGroup=ObjectGroup((1,3,6,1,4,1,664,5,59,4,10,1,4))
adGenDslProxyFrameGroundGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:adGenDslProxyFrameGroundGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AdGenDslProxyInitiate':AdGenDslProxyInitiate,'AdGenDslProxyStatus':AdGenDslProxyStatus,'AdGenDslProxyLastTime':AdGenDslProxyLastTime,'adGenDslProxyCommands':adGenDslProxyCommands,'adGenDslProxyCommandTable':adGenDslProxyCommandTable,'adGenDslProxyCommandEntry':adGenDslProxyCommandEntry,_N:adGenDslProxySystemTypeInitiate,_O:adGenDslProxySystemTypeStatus,_P:adGenDslProxySystemTypeLastTime,_Q:adGenDslProxyLoopbackStatusInitiate,_R:adGenDslProxyLoopbackStatusStatus,_S:adGenDslProxyLoopbackStatusLastTime,_T:adGenDslProxySpliceDetectInitiate,_U:adGenDslProxySpliceDetectStatus,_V:adGenDslProxySpliceDetectLastTime,_W:adGenDslProxyFrameGroundInitiate,_H:adGenDslProxyFrameGroundStatus,_X:adGenDslProxyFrameGroundLastTime,'adGenDslProxyResults':adGenDslProxyResults,'adGenDslProxySystemTable':adGenDslProxySystemTable,'adGenDslProxySystemEntry':adGenDslProxySystemEntry,_Y:adGenDslProxySystemValid,_Z:adGenDslProxySystemLastError,_a:adGenDslProxySystemType,_b:adGenDslProxyNumRepeaters,'adGenDslProxyLoopbackTable':adGenDslProxyLoopbackTable,'adGenDslProxyLoopbackEntry':adGenDslProxyLoopbackEntry,_c:adGenDslProxySetLoopback,_d:adGenDslProxyLoopbackStatus,'adGenDslProxyFrameGroundTable':adGenDslProxyFrameGroundTable,'adGenDslProxyFrameGroundEntry':adGenDslProxyFrameGroundEntry,'adGenDslProxyFrameGroundResult':adGenDslProxyFrameGroundResult,'adGenDslProxyMibConformance':adGenDslProxyMibConformance,'adGenDslProxyMibGroups':adGenDslProxyMibGroups,'adGenDslProxyCommandGroup':adGenDslProxyCommandGroup,'adGenDslProxySystemGroup':adGenDslProxySystemGroup,'adGenDslProxyLoopbackGroup':adGenDslProxyLoopbackGroup,'adGenDslProxyFrameGroundGroup':adGenDslProxyFrameGroundGroup,'adGenDslProxyMIB':adGenDslProxyMIB})