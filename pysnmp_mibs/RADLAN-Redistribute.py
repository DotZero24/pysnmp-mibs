_V='rlRedistRoutMapName'
_U='rlRedistMatchType'
_T='rlRedistSrcProcessId'
_S='rlRedistDstProcessId'
_R='rlRedistSrcProtocol'
_Q='rlRedistDstProtocol'
_P='rlRedistProtocolIsIsL2'
_O='rlRedistProtocolIsIsL1'
_N='rlRedistProtocolMobile'
_M='rlRedistProtocolIsIs'
_L='rlRedistProtocolEigrp'
_K='rlRedistProtocolBgp'
_J='rlRedistProtocolOspfv3'
_I='rlRedistProtocolOspfv2'
_H='rlRedistProtocolRip'
_G='DisplayString'
_F='TruthValue'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='RADLAN-Redistribute'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipSpec,=mibBuilder.importSymbols('RADLAN-IP','ipSpec')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_F)
class RlRedistSrcProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,101,102)));namedValues=NamedValues(*(('rlRedistProtocolConnected',1),('rlRedistProtocolStatic',2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),('rlRedistProtocolAll',10),(_O,101),(_P,102)))
class RlRedistDstProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,100,101,102)));namedValues=NamedValues(*((_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),('rlRedistProtocolBgpMulticast',100),(_O,101),(_P,102)))
class RlRedistMatchType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,100,101)));namedValues=NamedValues(*(('rlRedistMatchTypeNone',0),('rlRedistMatchTypeInternal',1),('rlRedistMatchTypeExternalOne',2),('rlRedistMatchTypeExternalTwo',3),('rlRedistMatchTypeIsIsInternal',100),('rlRedistMatchTypeIsIsExternal',101)))
class RlRedistMetricType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,100,101)));namedValues=NamedValues(*(('rlRedistMetricTypeNone',0),('rlRedistMetricTypeExternalOne',1),('rlRedistMetricTypeExternalTwo',2),('rlRedistMetricTypeIsIsInternal',100),('rlRedistMetricTypeIsIsExternal',101)))
_RlRedistribute_ObjectIdentity=ObjectIdentity
rlRedistribute=_RlRedistribute_ObjectIdentity((1,3,6,1,4,1,89,26,27))
_RlRedistTable_Object=MibTable
rlRedistTable=_RlRedistTable_Object((1,3,6,1,4,1,89,26,27,1))
if mibBuilder.loadTexts:rlRedistTable.setStatus(_A)
_RlRedistEntry_Object=MibTableRow
rlRedistEntry=_RlRedistEntry_Object((1,3,6,1,4,1,89,26,27,1,1))
rlRedistEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:rlRedistEntry.setStatus(_A)
_RlRedistDstProtocol_Type=RlRedistDstProtocol
_RlRedistDstProtocol_Object=MibTableColumn
rlRedistDstProtocol=_RlRedistDstProtocol_Object((1,3,6,1,4,1,89,26,27,1,1,1),_RlRedistDstProtocol_Type())
rlRedistDstProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:rlRedistDstProtocol.setStatus(_A)
_RlRedistSrcProtocol_Type=RlRedistSrcProtocol
_RlRedistSrcProtocol_Object=MibTableColumn
rlRedistSrcProtocol=_RlRedistSrcProtocol_Object((1,3,6,1,4,1,89,26,27,1,1,2),_RlRedistSrcProtocol_Type())
rlRedistSrcProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:rlRedistSrcProtocol.setStatus(_A)
class _RlRedistDstProcessId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlRedistDstProcessId_Type.__name__=_E
_RlRedistDstProcessId_Object=MibTableColumn
rlRedistDstProcessId=_RlRedistDstProcessId_Object((1,3,6,1,4,1,89,26,27,1,1,3),_RlRedistDstProcessId_Type())
rlRedistDstProcessId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlRedistDstProcessId.setStatus(_A)
class _RlRedistSrcProcessId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlRedistSrcProcessId_Type.__name__=_E
_RlRedistSrcProcessId_Object=MibTableColumn
rlRedistSrcProcessId=_RlRedistSrcProcessId_Object((1,3,6,1,4,1,89,26,27,1,1,4),_RlRedistSrcProcessId_Type())
rlRedistSrcProcessId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlRedistSrcProcessId.setStatus(_A)
_RlRedistMatchType_Type=RlRedistMatchType
_RlRedistMatchType_Object=MibTableColumn
rlRedistMatchType=_RlRedistMatchType_Object((1,3,6,1,4,1,89,26,27,1,1,5),_RlRedistMatchType_Type())
rlRedistMatchType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlRedistMatchType.setStatus(_A)
class _RlRedistRoutMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlRedistRoutMapName_Type.__name__=_G
_RlRedistRoutMapName_Object=MibTableColumn
rlRedistRoutMapName=_RlRedistRoutMapName_Object((1,3,6,1,4,1,89,26,27,1,1,6),_RlRedistRoutMapName_Type())
rlRedistRoutMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlRedistRoutMapName.setStatus(_A)
class _RlRedistAsNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlRedistAsNumber_Type.__name__=_E
_RlRedistAsNumber_Object=MibTableColumn
rlRedistAsNumber=_RlRedistAsNumber_Object((1,3,6,1,4,1,89,26,27,1,1,7),_RlRedistAsNumber_Type())
rlRedistAsNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistAsNumber.setStatus(_A)
class _RlRedistMetricTransparent_Type(TruthValue):defaultValue=1
_RlRedistMetricTransparent_Type.__name__=_F
_RlRedistMetricTransparent_Object=MibTableColumn
rlRedistMetricTransparent=_RlRedistMetricTransparent_Object((1,3,6,1,4,1,89,26,27,1,1,8),_RlRedistMetricTransparent_Type())
rlRedistMetricTransparent.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistMetricTransparent.setStatus(_A)
class _RlRedistMetricValue_Type(Integer32):defaultValue=0
_RlRedistMetricValue_Type.__name__=_E
_RlRedistMetricValue_Object=MibTableColumn
rlRedistMetricValue=_RlRedistMetricValue_Object((1,3,6,1,4,1,89,26,27,1,1,9),_RlRedistMetricValue_Type())
rlRedistMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistMetricValue.setStatus(_A)
_RlRedistMetricType_Type=RlRedistMetricType
_RlRedistMetricType_Object=MibTableColumn
rlRedistMetricType=_RlRedistMetricType_Object((1,3,6,1,4,1,89,26,27,1,1,10),_RlRedistMetricType_Type())
rlRedistMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistMetricType.setStatus(_A)
class _RlRedistSubnets_Type(TruthValue):defaultValue=2
_RlRedistSubnets_Type.__name__=_F
_RlRedistSubnets_Object=MibTableColumn
rlRedistSubnets=_RlRedistSubnets_Object((1,3,6,1,4,1,89,26,27,1,1,11),_RlRedistSubnets_Type())
rlRedistSubnets.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistSubnets.setStatus(_A)
class _RlRedistOnlyNSSA_Type(TruthValue):defaultValue=2
_RlRedistOnlyNSSA_Type.__name__=_F
_RlRedistOnlyNSSA_Object=MibTableColumn
rlRedistOnlyNSSA=_RlRedistOnlyNSSA_Object((1,3,6,1,4,1,89,26,27,1,1,12),_RlRedistOnlyNSSA_Type())
rlRedistOnlyNSSA.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistOnlyNSSA.setStatus(_A)
_RlRedistRowStatus_Type=RowStatus
_RlRedistRowStatus_Object=MibTableColumn
rlRedistRowStatus=_RlRedistRowStatus_Object((1,3,6,1,4,1,89,26,27,1,1,13),_RlRedistRowStatus_Type())
rlRedistRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rlRedistRowStatus.setStatus(_A)
_RlRedistFilterListName_Type=DisplayString
_RlRedistFilterListName_Object=MibTableColumn
rlRedistFilterListName=_RlRedistFilterListName_Object((1,3,6,1,4,1,89,26,27,1,1,14),_RlRedistFilterListName_Type())
rlRedistFilterListName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRedistFilterListName.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RlRedistSrcProtocol':RlRedistSrcProtocol,'RlRedistDstProtocol':RlRedistDstProtocol,'RlRedistMatchType':RlRedistMatchType,'RlRedistMetricType':RlRedistMetricType,'rlRedistribute':rlRedistribute,'rlRedistTable':rlRedistTable,'rlRedistEntry':rlRedistEntry,_Q:rlRedistDstProtocol,_R:rlRedistSrcProtocol,_S:rlRedistDstProcessId,_T:rlRedistSrcProcessId,_U:rlRedistMatchType,_V:rlRedistRoutMapName,'rlRedistAsNumber':rlRedistAsNumber,'rlRedistMetricTransparent':rlRedistMetricTransparent,'rlRedistMetricValue':rlRedistMetricValue,'rlRedistMetricType':rlRedistMetricType,'rlRedistSubnets':rlRedistSubnets,'rlRedistOnlyNSSA':rlRedistOnlyNSSA,'rlRedistRowStatus':rlRedistRowStatus,'rlRedistFilterListName':rlRedistFilterListName})