_J='ipForwardNextHop'
_I='ipForwardPolicy'
_H='ipForwardProto'
_G='ipForwardDest'
_F='IpAddress'
_E='RFC1354-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ip,=mibBuilder.importSymbols('IP-MIB','ip')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_F,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_IpForward_ObjectIdentity=ObjectIdentity
ipForward=_IpForward_ObjectIdentity((1,3,6,1,2,1,4,24))
_IpForwardNumber_Type=Gauge32
_IpForwardNumber_Object=MibScalar
ipForwardNumber=_IpForwardNumber_Object((1,3,6,1,2,1,4,24,1),_IpForwardNumber_Type())
ipForwardNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ipForwardNumber.setStatus(_A)
_IpForwardTable_Object=MibTable
ipForwardTable=_IpForwardTable_Object((1,3,6,1,2,1,4,24,2))
if mibBuilder.loadTexts:ipForwardTable.setStatus(_A)
_IpForwardEntry_Object=MibTableRow
ipForwardEntry=_IpForwardEntry_Object((1,3,6,1,2,1,4,24,2,1))
ipForwardEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:ipForwardEntry.setStatus(_A)
_IpForwardDest_Type=IpAddress
_IpForwardDest_Object=MibTableColumn
ipForwardDest=_IpForwardDest_Object((1,3,6,1,2,1,4,24,2,1,1),_IpForwardDest_Type())
ipForwardDest.setMaxAccess(_D)
if mibBuilder.loadTexts:ipForwardDest.setStatus(_A)
class _IpForwardMask_Type(IpAddress):defaultHexValue='00000000'
_IpForwardMask_Type.__name__=_F
_IpForwardMask_Object=MibTableColumn
ipForwardMask=_IpForwardMask_Object((1,3,6,1,2,1,4,24,2,1,2),_IpForwardMask_Type())
ipForwardMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardMask.setStatus(_A)
_IpForwardPolicy_Type=Integer32
_IpForwardPolicy_Object=MibTableColumn
ipForwardPolicy=_IpForwardPolicy_Object((1,3,6,1,2,1,4,24,2,1,3),_IpForwardPolicy_Type())
ipForwardPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:ipForwardPolicy.setStatus(_A)
_IpForwardNextHop_Type=IpAddress
_IpForwardNextHop_Object=MibTableColumn
ipForwardNextHop=_IpForwardNextHop_Object((1,3,6,1,2,1,4,24,2,1,4),_IpForwardNextHop_Type())
ipForwardNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:ipForwardNextHop.setStatus(_A)
class _IpForwardIfIndex_Type(Integer32):defaultValue=0
_IpForwardIfIndex_Type.__name__=_B
_IpForwardIfIndex_Object=MibTableColumn
ipForwardIfIndex=_IpForwardIfIndex_Object((1,3,6,1,2,1,4,24,2,1,5),_IpForwardIfIndex_Type())
ipForwardIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardIfIndex.setStatus(_A)
class _IpForwardType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('invalid',2),('local',3),('remote',4)))
_IpForwardType_Type.__name__=_B
_IpForwardType_Object=MibTableColumn
ipForwardType=_IpForwardType_Object((1,3,6,1,2,1,4,24,2,1,6),_IpForwardType_Type())
ipForwardType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardType.setStatus(_A)
class _IpForwardProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15)))
_IpForwardProto_Type.__name__=_B
_IpForwardProto_Object=MibTableColumn
ipForwardProto=_IpForwardProto_Object((1,3,6,1,2,1,4,24,2,1,7),_IpForwardProto_Type())
ipForwardProto.setMaxAccess(_D)
if mibBuilder.loadTexts:ipForwardProto.setStatus(_A)
class _IpForwardAge_Type(Integer32):defaultValue=0
_IpForwardAge_Type.__name__=_B
_IpForwardAge_Object=MibTableColumn
ipForwardAge=_IpForwardAge_Object((1,3,6,1,2,1,4,24,2,1,8),_IpForwardAge_Type())
ipForwardAge.setMaxAccess(_D)
if mibBuilder.loadTexts:ipForwardAge.setStatus(_A)
_IpForwardInfo_Type=ObjectIdentifier
_IpForwardInfo_Object=MibTableColumn
ipForwardInfo=_IpForwardInfo_Object((1,3,6,1,2,1,4,24,2,1,9),_IpForwardInfo_Type())
ipForwardInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardInfo.setStatus(_A)
class _IpForwardNextHopAS_Type(Integer32):defaultValue=0
_IpForwardNextHopAS_Type.__name__=_B
_IpForwardNextHopAS_Object=MibTableColumn
ipForwardNextHopAS=_IpForwardNextHopAS_Object((1,3,6,1,2,1,4,24,2,1,10),_IpForwardNextHopAS_Type())
ipForwardNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardNextHopAS.setStatus(_A)
class _IpForwardMetric1_Type(Integer32):defaultValue=-1
_IpForwardMetric1_Type.__name__=_B
_IpForwardMetric1_Object=MibTableColumn
ipForwardMetric1=_IpForwardMetric1_Object((1,3,6,1,2,1,4,24,2,1,11),_IpForwardMetric1_Type())
ipForwardMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardMetric1.setStatus(_A)
class _IpForwardMetric2_Type(Integer32):defaultValue=-1
_IpForwardMetric2_Type.__name__=_B
_IpForwardMetric2_Object=MibTableColumn
ipForwardMetric2=_IpForwardMetric2_Object((1,3,6,1,2,1,4,24,2,1,12),_IpForwardMetric2_Type())
ipForwardMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardMetric2.setStatus(_A)
class _IpForwardMetric3_Type(Integer32):defaultValue=-1
_IpForwardMetric3_Type.__name__=_B
_IpForwardMetric3_Object=MibTableColumn
ipForwardMetric3=_IpForwardMetric3_Object((1,3,6,1,2,1,4,24,2,1,13),_IpForwardMetric3_Type())
ipForwardMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardMetric3.setStatus(_A)
class _IpForwardMetric4_Type(Integer32):defaultValue=-1
_IpForwardMetric4_Type.__name__=_B
_IpForwardMetric4_Object=MibTableColumn
ipForwardMetric4=_IpForwardMetric4_Object((1,3,6,1,2,1,4,24,2,1,14),_IpForwardMetric4_Type())
ipForwardMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardMetric4.setStatus(_A)
class _IpForwardMetric5_Type(Integer32):defaultValue=-1
_IpForwardMetric5_Type.__name__=_B
_IpForwardMetric5_Object=MibTableColumn
ipForwardMetric5=_IpForwardMetric5_Object((1,3,6,1,2,1,4,24,2,1,15),_IpForwardMetric5_Type())
ipForwardMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwardMetric5.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ipForward':ipForward,'ipForwardNumber':ipForwardNumber,'ipForwardTable':ipForwardTable,'ipForwardEntry':ipForwardEntry,_G:ipForwardDest,'ipForwardMask':ipForwardMask,_I:ipForwardPolicy,_J:ipForwardNextHop,'ipForwardIfIndex':ipForwardIfIndex,'ipForwardType':ipForwardType,_H:ipForwardProto,'ipForwardAge':ipForwardAge,'ipForwardInfo':ipForwardInfo,'ipForwardNextHopAS':ipForwardNextHopAS,'ipForwardMetric1':ipForwardMetric1,'ipForwardMetric2':ipForwardMetric2,'ipForwardMetric3':ipForwardMetric3,'ipForwardMetric4':ipForwardMetric4,'ipForwardMetric5':ipForwardMetric5})