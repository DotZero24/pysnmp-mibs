_b='ignore'
_a='unknown'
_Z='ipSifPolicyChkDestPort'
_Y='ipSifPolicyChkProtocol'
_X='ipSifAliasServiceGroupId'
_W='ipSifAliasAddressGroupId'
_V='ipSifExpectIndex'
_U='ipSifRejectIndex'
_T='medium'
_S='low-latency'
_R='default'
_Q='reject'
_P='ipSifAliasOrder'
_O='ipSifAliasServiceAlias'
_N='address'
_M='interface'
_L='ipSifAliasAddressAlias'
_K='access'
_J='DisplayString'
_I='disable'
_H='enable'
_G='deny'
_F='delete'
_E='BIANCA-BRICK-SIF-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_IpSifAliasAddressTable_Object=MibTable
ipSifAliasAddressTable=_IpSifAliasAddressTable_Object((1,3,6,1,4,1,272,4,5,28))
if mibBuilder.loadTexts:ipSifAliasAddressTable.setStatus(_A)
_IpSifAliasAddressEntry_Object=MibTableRow
ipSifAliasAddressEntry=_IpSifAliasAddressEntry_Object((1,3,6,1,4,1,272,4,5,28,1))
ipSifAliasAddressEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:ipSifAliasAddressEntry.setStatus(_A)
class _IpSifAliasAddressIndex_Type(Integer32):defaultValue=0
_IpSifAliasAddressIndex_Type.__name__=_C
_IpSifAliasAddressIndex_Object=MibTableColumn
ipSifAliasAddressIndex=_IpSifAliasAddressIndex_Object((1,3,6,1,4,1,272,4,5,28,1,1),_IpSifAliasAddressIndex_Type())
ipSifAliasAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifAliasAddressIndex.setStatus(_A)
class _IpSifAliasAddressAlias_Type(DisplayString):defaultValue=OctetString('')
_IpSifAliasAddressAlias_Type.__name__=_J
_IpSifAliasAddressAlias_Object=MibTableColumn
ipSifAliasAddressAlias=_IpSifAliasAddressAlias_Object((1,3,6,1,4,1,272,4,5,28,1,2),_IpSifAliasAddressAlias_Type())
ipSifAliasAddressAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressAlias.setStatus(_A)
_IpSifAliasAddressAddress_Type=IpAddress
_IpSifAliasAddressAddress_Object=MibTableColumn
ipSifAliasAddressAddress=_IpSifAliasAddressAddress_Object((1,3,6,1,4,1,272,4,5,28,1,3),_IpSifAliasAddressAddress_Type())
ipSifAliasAddressAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressAddress.setStatus(_A)
_IpSifAliasAddressMask_Type=IpAddress
_IpSifAliasAddressMask_Object=MibTableColumn
ipSifAliasAddressMask=_IpSifAliasAddressMask_Object((1,3,6,1,4,1,272,4,5,28,1,4),_IpSifAliasAddressMask_Type())
ipSifAliasAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressMask.setStatus(_A)
class _IpSifAliasAddressInterface_Type(Integer32):defaultValue=0
_IpSifAliasAddressInterface_Type.__name__=_C
_IpSifAliasAddressInterface_Object=MibTableColumn
ipSifAliasAddressInterface=_IpSifAliasAddressInterface_Object((1,3,6,1,4,1,272,4,5,28,1,5),_IpSifAliasAddressInterface_Type())
ipSifAliasAddressInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressInterface.setStatus(_A)
class _IpSifAliasAddressMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),('range',3),(_F,4)))
_IpSifAliasAddressMode_Type.__name__=_C
_IpSifAliasAddressMode_Object=MibTableColumn
ipSifAliasAddressMode=_IpSifAliasAddressMode_Object((1,3,6,1,4,1,272,4,5,28,1,6),_IpSifAliasAddressMode_Type())
ipSifAliasAddressMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressMode.setStatus(_A)
class _IpSifAliasAddressRange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpSifAliasAddressRange_Type.__name__=_C
_IpSifAliasAddressRange_Object=MibTableColumn
ipSifAliasAddressRange=_IpSifAliasAddressRange_Object((1,3,6,1,4,1,272,4,5,28,1,7),_IpSifAliasAddressRange_Type())
ipSifAliasAddressRange.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressRange.setStatus(_A)
_IpSifAliasAddressGroup_Type=Integer32
_IpSifAliasAddressGroup_Object=MibTableColumn
ipSifAliasAddressGroup=_IpSifAliasAddressGroup_Object((1,3,6,1,4,1,272,4,5,28,1,8),_IpSifAliasAddressGroup_Type())
ipSifAliasAddressGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressGroup.setStatus(_A)
_IpSifAliasServiceTable_Object=MibTable
ipSifAliasServiceTable=_IpSifAliasServiceTable_Object((1,3,6,1,4,1,272,4,5,29))
if mibBuilder.loadTexts:ipSifAliasServiceTable.setStatus(_A)
_IpSifAliasServiceEntry_Object=MibTableRow
ipSifAliasServiceEntry=_IpSifAliasServiceEntry_Object((1,3,6,1,4,1,272,4,5,29,1))
ipSifAliasServiceEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:ipSifAliasServiceEntry.setStatus(_A)
class _IpSifAliasServiceIndex_Type(Integer32):defaultValue=0
_IpSifAliasServiceIndex_Type.__name__=_C
_IpSifAliasServiceIndex_Object=MibTableColumn
ipSifAliasServiceIndex=_IpSifAliasServiceIndex_Object((1,3,6,1,4,1,272,4,5,29,1,1),_IpSifAliasServiceIndex_Type())
ipSifAliasServiceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifAliasServiceIndex.setStatus(_A)
class _IpSifAliasServiceAlias_Type(DisplayString):defaultValue=OctetString('')
_IpSifAliasServiceAlias_Type.__name__=_J
_IpSifAliasServiceAlias_Object=MibTableColumn
ipSifAliasServiceAlias=_IpSifAliasServiceAlias_Object((1,3,6,1,4,1,272,4,5,29,1,2),_IpSifAliasServiceAlias_Type())
ipSifAliasServiceAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceAlias.setStatus(_A)
class _IpSifAliasServiceProtocol_Type(Integer32):defaultValue=254;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,8,9,12,16,17,20,22,27,41,46,47,50,51,56,57,65,80,88,89,94,103,111,112,115,250,251,252,253,254,255,256)));namedValues=NamedValues(*(('icmp',1),('igmp',2),('ggp',3),('ip',4),('tcp',6),('egp',8),('igp',9),('pup',12),('chaos',16),('udp',17),('hmp',20),('xns-idp',22),('rdp',27),('ipv6',41),('rsvp',46),('gre',47),('esp',50),('ah',51),('tlsp',56),('skip',57),('kryptolan',65),('iso-ip',80),('igrp',88),('ospf',89),('ipip',94),('pim',103),('ipx-in-ip',111),('vrrp',112),('l2tp',115),('local',250),('internet',251),('netmeeting',252),('udptcp',253),('any',254),(_F,255),('dont-verify',256)))
_IpSifAliasServiceProtocol_Type.__name__=_C
_IpSifAliasServiceProtocol_Object=MibTableColumn
ipSifAliasServiceProtocol=_IpSifAliasServiceProtocol_Object((1,3,6,1,4,1,272,4,5,29,1,3),_IpSifAliasServiceProtocol_Type())
ipSifAliasServiceProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceProtocol.setStatus(_A)
class _IpSifAliasServicePort_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_IpSifAliasServicePort_Type.__name__=_C
_IpSifAliasServicePort_Object=MibTableColumn
ipSifAliasServicePort=_IpSifAliasServicePort_Object((1,3,6,1,4,1,272,4,5,29,1,4),_IpSifAliasServicePort_Type())
ipSifAliasServicePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServicePort.setStatus(_A)
class _IpSifAliasServiceRange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_IpSifAliasServiceRange_Type.__name__=_C
_IpSifAliasServiceRange_Object=MibTableColumn
ipSifAliasServiceRange=_IpSifAliasServiceRange_Object((1,3,6,1,4,1,272,4,5,29,1,5),_IpSifAliasServiceRange_Type())
ipSifAliasServiceRange.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceRange.setStatus(_A)
class _IpSifAliasServiceType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('predefined',1),('custom',2)))
_IpSifAliasServiceType_Type.__name__=_C
_IpSifAliasServiceType_Object=MibTableColumn
ipSifAliasServiceType=_IpSifAliasServiceType_Object((1,3,6,1,4,1,272,4,5,29,1,6),_IpSifAliasServiceType_Type())
ipSifAliasServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifAliasServiceType.setStatus(_A)
_IpSifAliasServiceGroup_Type=Integer32
_IpSifAliasServiceGroup_Object=MibTableColumn
ipSifAliasServiceGroup=_IpSifAliasServiceGroup_Object((1,3,6,1,4,1,272,4,5,29,1,7),_IpSifAliasServiceGroup_Type())
ipSifAliasServiceGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceGroup.setStatus(_A)
class _IpSifAliasServiceSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpSifAliasServiceSourcePort_Type.__name__=_C
_IpSifAliasServiceSourcePort_Object=MibTableColumn
ipSifAliasServiceSourcePort=_IpSifAliasServiceSourcePort_Object((1,3,6,1,4,1,272,4,5,29,1,8),_IpSifAliasServiceSourcePort_Type())
ipSifAliasServiceSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceSourcePort.setStatus(_A)
class _IpSifAliasServiceSourceRange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_IpSifAliasServiceSourceRange_Type.__name__=_C
_IpSifAliasServiceSourceRange_Object=MibTableColumn
ipSifAliasServiceSourceRange=_IpSifAliasServiceSourceRange_Object((1,3,6,1,4,1,272,4,5,29,1,9),_IpSifAliasServiceSourceRange_Type())
ipSifAliasServiceSourceRange.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceSourceRange.setStatus(_A)
class _IpSifAliasServiceIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_IpSifAliasServiceIcmpType_Type.__name__=_C
_IpSifAliasServiceIcmpType_Object=MibTableColumn
ipSifAliasServiceIcmpType=_IpSifAliasServiceIcmpType_Object((1,3,6,1,4,1,272,4,5,29,1,10),_IpSifAliasServiceIcmpType_Type())
ipSifAliasServiceIcmpType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceIcmpType.setStatus(_A)
class _IpSifAliasServiceIcmpCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_IpSifAliasServiceIcmpCode_Type.__name__=_C
_IpSifAliasServiceIcmpCode_Object=MibTableColumn
ipSifAliasServiceIcmpCode=_IpSifAliasServiceIcmpCode_Object((1,3,6,1,4,1,272,4,5,29,1,11),_IpSifAliasServiceIcmpCode_Type())
ipSifAliasServiceIcmpCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceIcmpCode.setStatus(_A)
_IpSifAliasTable_Object=MibTable
ipSifAliasTable=_IpSifAliasTable_Object((1,3,6,1,4,1,272,4,5,30))
if mibBuilder.loadTexts:ipSifAliasTable.setStatus(_A)
_IpSifAliasEntry_Object=MibTableRow
ipSifAliasEntry=_IpSifAliasEntry_Object((1,3,6,1,4,1,272,4,5,30,1))
ipSifAliasEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:ipSifAliasEntry.setStatus(_A)
_IpSifAliasOrder_Type=Integer32
_IpSifAliasOrder_Object=MibTableColumn
ipSifAliasOrder=_IpSifAliasOrder_Object((1,3,6,1,4,1,272,4,5,30,1,1),_IpSifAliasOrder_Type())
ipSifAliasOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasOrder.setStatus(_A)
_IpSifAliasSource_Type=Integer32
_IpSifAliasSource_Object=MibTableColumn
ipSifAliasSource=_IpSifAliasSource_Object((1,3,6,1,4,1,272,4,5,30,1,2),_IpSifAliasSource_Type())
ipSifAliasSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasSource.setStatus(_A)
_IpSifAliasDestination_Type=Integer32
_IpSifAliasDestination_Object=MibTableColumn
ipSifAliasDestination=_IpSifAliasDestination_Object((1,3,6,1,4,1,272,4,5,30,1,3),_IpSifAliasDestination_Type())
ipSifAliasDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasDestination.setStatus(_A)
_IpSifAliasService_Type=Integer32
_IpSifAliasService_Object=MibTableColumn
ipSifAliasService=_IpSifAliasService_Object((1,3,6,1,4,1,272,4,5,30,1,4),_IpSifAliasService_Type())
ipSifAliasService.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasService.setStatus(_A)
class _IpSifAliasAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_K,1),(_G,2),(_Q,3),(_F,255)))
_IpSifAliasAction_Type.__name__=_C
_IpSifAliasAction_Object=MibTableColumn
ipSifAliasAction=_IpSifAliasAction_Object((1,3,6,1,4,1,272,4,5,30,1,5),_IpSifAliasAction_Type())
ipSifAliasAction.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAction.setStatus(_A)
class _IpSifAliasStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IpSifAliasStatus_Type.__name__=_C
_IpSifAliasStatus_Object=MibTableColumn
ipSifAliasStatus=_IpSifAliasStatus_Object((1,3,6,1,4,1,272,4,5,30,1,6),_IpSifAliasStatus_Type())
ipSifAliasStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasStatus.setStatus(_A)
class _IpSifAliasPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),('high',3),(_T,4),('low',5)))
_IpSifAliasPriority_Type.__name__=_C
_IpSifAliasPriority_Object=MibTableColumn
ipSifAliasPriority=_IpSifAliasPriority_Object((1,3,6,1,4,1,272,4,5,30,1,7),_IpSifAliasPriority_Type())
ipSifAliasPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasPriority.setStatus(_A)
class _IpSifAliasClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpSifAliasClassId_Type.__name__=_C
_IpSifAliasClassId_Object=MibTableColumn
ipSifAliasClassId=_IpSifAliasClassId_Object((1,3,6,1,4,1,272,4,5,30,1,8),_IpSifAliasClassId_Type())
ipSifAliasClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasClassId.setStatus(_A)
_IpSifRejectTable_Object=MibTable
ipSifRejectTable=_IpSifRejectTable_Object((1,3,6,1,4,1,272,4,5,31))
if mibBuilder.loadTexts:ipSifRejectTable.setStatus(_A)
_IpSifRejectEntry_Object=MibTableRow
ipSifRejectEntry=_IpSifRejectEntry_Object((1,3,6,1,4,1,272,4,5,31,1))
ipSifRejectEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:ipSifRejectEntry.setStatus(_A)
_IpSifRejectIndex_Type=Integer32
_IpSifRejectIndex_Object=MibTableColumn
ipSifRejectIndex=_IpSifRejectIndex_Object((1,3,6,1,4,1,272,4,5,31,1,1),_IpSifRejectIndex_Type())
ipSifRejectIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectIndex.setStatus(_A)
_IpSifRejectSource_Type=IpAddress
_IpSifRejectSource_Object=MibTableColumn
ipSifRejectSource=_IpSifRejectSource_Object((1,3,6,1,4,1,272,4,5,31,1,2),_IpSifRejectSource_Type())
ipSifRejectSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectSource.setStatus(_A)
_IpSifRejectDestination_Type=IpAddress
_IpSifRejectDestination_Object=MibTableColumn
ipSifRejectDestination=_IpSifRejectDestination_Object((1,3,6,1,4,1,272,4,5,31,1,3),_IpSifRejectDestination_Type())
ipSifRejectDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectDestination.setStatus(_A)
_IpSifRejectRejects_Type=Integer32
_IpSifRejectRejects_Object=MibTableColumn
ipSifRejectRejects=_IpSifRejectRejects_Object((1,3,6,1,4,1,272,4,5,31,1,4),_IpSifRejectRejects_Type())
ipSifRejectRejects.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectRejects.setStatus(_A)
_IpSifRejectSilence_Type=Integer32
_IpSifRejectSilence_Object=MibTableColumn
ipSifRejectSilence=_IpSifRejectSilence_Object((1,3,6,1,4,1,272,4,5,31,1,5),_IpSifRejectSilence_Type())
ipSifRejectSilence.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectSilence.setStatus(_A)
class _IpSifRejectProtocol_Type(Integer32):defaultValue=0
_IpSifRejectProtocol_Type.__name__=_C
_IpSifRejectProtocol_Object=MibTableColumn
ipSifRejectProtocol=_IpSifRejectProtocol_Object((1,3,6,1,4,1,272,4,5,31,1,6),_IpSifRejectProtocol_Type())
ipSifRejectProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectProtocol.setStatus(_A)
class _IpSifRejectPortLo_Type(Integer32):defaultValue=0
_IpSifRejectPortLo_Type.__name__=_C
_IpSifRejectPortLo_Object=MibTableColumn
ipSifRejectPortLo=_IpSifRejectPortLo_Object((1,3,6,1,4,1,272,4,5,31,1,7),_IpSifRejectPortLo_Type())
ipSifRejectPortLo.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectPortLo.setStatus(_A)
class _IpSifRejectPortHigh_Type(Integer32):defaultValue=0
_IpSifRejectPortHigh_Type.__name__=_C
_IpSifRejectPortHigh_Object=MibTableColumn
ipSifRejectPortHigh=_IpSifRejectPortHigh_Object((1,3,6,1,4,1,272,4,5,31,1,8),_IpSifRejectPortHigh_Type())
ipSifRejectPortHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifRejectPortHigh.setStatus(_A)
_IpSifExpectTable_Object=MibTable
ipSifExpectTable=_IpSifExpectTable_Object((1,3,6,1,4,1,272,4,5,35))
if mibBuilder.loadTexts:ipSifExpectTable.setStatus(_A)
_IpSifExpectEntry_Object=MibTableRow
ipSifExpectEntry=_IpSifExpectEntry_Object((1,3,6,1,4,1,272,4,5,35,1))
ipSifExpectEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:ipSifExpectEntry.setStatus(_A)
_IpSifExpectIndex_Type=Integer32
_IpSifExpectIndex_Object=MibTableColumn
ipSifExpectIndex=_IpSifExpectIndex_Object((1,3,6,1,4,1,272,4,5,35,1,1),_IpSifExpectIndex_Type())
ipSifExpectIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectIndex.setStatus(_A)
_IpSifExpectSource_Type=IpAddress
_IpSifExpectSource_Object=MibTableColumn
ipSifExpectSource=_IpSifExpectSource_Object((1,3,6,1,4,1,272,4,5,35,1,2),_IpSifExpectSource_Type())
ipSifExpectSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectSource.setStatus(_A)
_IpSifExpectDestination_Type=IpAddress
_IpSifExpectDestination_Object=MibTableColumn
ipSifExpectDestination=_IpSifExpectDestination_Object((1,3,6,1,4,1,272,4,5,35,1,3),_IpSifExpectDestination_Type())
ipSifExpectDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectDestination.setStatus(_A)
class _IpSifExpectProtocol_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,6,17,255)));namedValues=NamedValues(*(('igmp',2),('ip',4),('tcp',6),('udp',17),(_F,255)))
_IpSifExpectProtocol_Type.__name__=_C
_IpSifExpectProtocol_Object=MibTableColumn
ipSifExpectProtocol=_IpSifExpectProtocol_Object((1,3,6,1,4,1,272,4,5,35,1,4),_IpSifExpectProtocol_Type())
ipSifExpectProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifExpectProtocol.setStatus(_A)
class _IpSifExpectSourcePort_Type(Integer32):defaultValue=0
_IpSifExpectSourcePort_Type.__name__=_C
_IpSifExpectSourcePort_Object=MibTableColumn
ipSifExpectSourcePort=_IpSifExpectSourcePort_Object((1,3,6,1,4,1,272,4,5,35,1,5),_IpSifExpectSourcePort_Type())
ipSifExpectSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectSourcePort.setStatus(_A)
class _IpSifExpectDestPort_Type(Integer32):defaultValue=0
_IpSifExpectDestPort_Type.__name__=_C
_IpSifExpectDestPort_Object=MibTableColumn
ipSifExpectDestPort=_IpSifExpectDestPort_Object((1,3,6,1,4,1,272,4,5,35,1,6),_IpSifExpectDestPort_Type())
ipSifExpectDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectDestPort.setStatus(_A)
class _IpSifExpectPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),('high',3),(_T,4),('low',5)))
_IpSifExpectPriority_Type.__name__=_C
_IpSifExpectPriority_Object=MibTableColumn
ipSifExpectPriority=_IpSifExpectPriority_Object((1,3,6,1,4,1,272,4,5,35,1,7),_IpSifExpectPriority_Type())
ipSifExpectPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectPriority.setStatus(_A)
class _IpSifExpectClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpSifExpectClassId_Type.__name__=_C
_IpSifExpectClassId_Object=MibTableColumn
ipSifExpectClassId=_IpSifExpectClassId_Object((1,3,6,1,4,1,272,4,5,35,1,8),_IpSifExpectClassId_Type())
ipSifExpectClassId.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectClassId.setStatus(_A)
class _IpSifExpectIfIndex_Type(Integer32):defaultValue=0
_IpSifExpectIfIndex_Type.__name__=_C
_IpSifExpectIfIndex_Object=MibTableColumn
ipSifExpectIfIndex=_IpSifExpectIfIndex_Object((1,3,6,1,4,1,272,4,5,35,1,9),_IpSifExpectIfIndex_Type())
ipSifExpectIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifExpectIfIndex.setStatus(_A)
_IpSif_ObjectIdentity=ObjectIdentity
ipSif=_IpSif_ObjectIdentity((1,3,6,1,4,1,272,4,5,37))
class _IpSifAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpSifAdminStatus_Type.__name__=_C
_IpSifAdminStatus_Object=MibScalar
ipSifAdminStatus=_IpSifAdminStatus_Object((1,3,6,1,4,1,272,4,5,37,1),_IpSifAdminStatus_Type())
ipSifAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAdminStatus.setStatus(_A)
class _IpSifLocalFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpSifLocalFilter_Type.__name__=_C
_IpSifLocalFilter_Object=MibScalar
ipSifLocalFilter=_IpSifLocalFilter_Object((1,3,6,1,4,1,272,4,5,37,2),_IpSifLocalFilter_Type())
ipSifLocalFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifLocalFilter.setStatus(_A)
class _IpSifInterfaceFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpSifInterfaceFilter_Type.__name__=_C
_IpSifInterfaceFilter_Object=MibScalar
ipSifInterfaceFilter=_IpSifInterfaceFilter_Object((1,3,6,1,4,1,272,4,5,37,3),_IpSifInterfaceFilter_Type())
ipSifInterfaceFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifInterfaceFilter.setStatus(_A)
class _IpSifSysloglevel_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('accept',2),('verbose',3),('none',4)))
_IpSifSysloglevel_Type.__name__=_C
_IpSifSysloglevel_Object=MibScalar
ipSifSysloglevel=_IpSifSysloglevel_Object((1,3,6,1,4,1,272,4,5,37,4),_IpSifSysloglevel_Type())
ipSifSysloglevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifSysloglevel.setStatus(_A)
class _IpSifUdpTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_IpSifUdpTimeout_Type.__name__=_C
_IpSifUdpTimeout_Object=MibScalar
ipSifUdpTimeout=_IpSifUdpTimeout_Object((1,3,6,1,4,1,272,4,5,37,5),_IpSifUdpTimeout_Type())
ipSifUdpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifUdpTimeout.setStatus(_A)
class _IpSifTcpTimeout_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_IpSifTcpTimeout_Type.__name__=_C
_IpSifTcpTimeout_Object=MibScalar
ipSifTcpTimeout=_IpSifTcpTimeout_Object((1,3,6,1,4,1,272,4,5,37,6),_IpSifTcpTimeout_Type())
ipSifTcpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifTcpTimeout.setStatus(_A)
class _IpSifPPTPTimeout_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_IpSifPPTPTimeout_Type.__name__=_C
_IpSifPPTPTimeout_Object=MibScalar
ipSifPPTPTimeout=_IpSifPPTPTimeout_Object((1,3,6,1,4,1,272,4,5,37,7),_IpSifPPTPTimeout_Type())
ipSifPPTPTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPPTPTimeout.setStatus(_A)
class _IpSifDefaultTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_IpSifDefaultTimeout_Type.__name__=_C
_IpSifDefaultTimeout_Object=MibScalar
ipSifDefaultTimeout=_IpSifDefaultTimeout_Object((1,3,6,1,4,1,272,4,5,37,8),_IpSifDefaultTimeout_Type())
ipSifDefaultTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifDefaultTimeout.setStatus(_A)
class _IpSifMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_IpSifMaxSessions_Type.__name__=_C
_IpSifMaxSessions_Object=MibScalar
ipSifMaxSessions=_IpSifMaxSessions_Object((1,3,6,1,4,1,272,4,5,37,9),_IpSifMaxSessions_Type())
ipSifMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifMaxSessions.setStatus(_A)
class _IpSifMaxRejectEntries_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_IpSifMaxRejectEntries_Type.__name__=_C
_IpSifMaxRejectEntries_Object=MibScalar
ipSifMaxRejectEntries=_IpSifMaxRejectEntries_Object((1,3,6,1,4,1,272,4,5,37,14),_IpSifMaxRejectEntries_Type())
ipSifMaxRejectEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifMaxRejectEntries.setStatus(_A)
class _IpSifMaxRejectTtl_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_IpSifMaxRejectTtl_Type.__name__=_C
_IpSifMaxRejectTtl_Object=MibScalar
ipSifMaxRejectTtl=_IpSifMaxRejectTtl_Object((1,3,6,1,4,1,272,4,5,37,15),_IpSifMaxRejectTtl_Type())
ipSifMaxRejectTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifMaxRejectTtl.setStatus(_A)
class _IpSifInterfaceAliasAutoCreate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpSifInterfaceAliasAutoCreate_Type.__name__=_C
_IpSifInterfaceAliasAutoCreate_Object=MibScalar
ipSifInterfaceAliasAutoCreate=_IpSifInterfaceAliasAutoCreate_Object((1,3,6,1,4,1,272,4,5,37,16),_IpSifInterfaceAliasAutoCreate_Type())
ipSifInterfaceAliasAutoCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifInterfaceAliasAutoCreate.setStatus(_A)
_IpSifStat_ObjectIdentity=ObjectIdentity
ipSifStat=_IpSifStat_ObjectIdentity((1,3,6,1,4,1,272,4,5,46))
_IpSifStatCurrSessions_Type=Counter32
_IpSifStatCurrSessions_Object=MibScalar
ipSifStatCurrSessions=_IpSifStatCurrSessions_Object((1,3,6,1,4,1,272,4,5,46,1),_IpSifStatCurrSessions_Type())
ipSifStatCurrSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatCurrSessions.setStatus(_A)
_IpSifStatCurrUdpSessions_Type=Counter32
_IpSifStatCurrUdpSessions_Object=MibScalar
ipSifStatCurrUdpSessions=_IpSifStatCurrUdpSessions_Object((1,3,6,1,4,1,272,4,5,46,2),_IpSifStatCurrUdpSessions_Type())
ipSifStatCurrUdpSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatCurrUdpSessions.setStatus(_A)
_IpSifStatCurrTcpSessions_Type=Counter32
_IpSifStatCurrTcpSessions_Object=MibScalar
ipSifStatCurrTcpSessions=_IpSifStatCurrTcpSessions_Object((1,3,6,1,4,1,272,4,5,46,3),_IpSifStatCurrTcpSessions_Type())
ipSifStatCurrTcpSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatCurrTcpSessions.setStatus(_A)
_IpSifStatCurrOtherSessions_Type=Counter32
_IpSifStatCurrOtherSessions_Object=MibScalar
ipSifStatCurrOtherSessions=_IpSifStatCurrOtherSessions_Object((1,3,6,1,4,1,272,4,5,46,4),_IpSifStatCurrOtherSessions_Type())
ipSifStatCurrOtherSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatCurrOtherSessions.setStatus(_A)
_IpSifStatCurrExpectedSessions_Type=Counter32
_IpSifStatCurrExpectedSessions_Object=MibScalar
ipSifStatCurrExpectedSessions=_IpSifStatCurrExpectedSessions_Object((1,3,6,1,4,1,272,4,5,46,5),_IpSifStatCurrExpectedSessions_Type())
ipSifStatCurrExpectedSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatCurrExpectedSessions.setStatus(_A)
_IpSifStatTotalUdpSessions_Type=Counter32
_IpSifStatTotalUdpSessions_Object=MibScalar
ipSifStatTotalUdpSessions=_IpSifStatTotalUdpSessions_Object((1,3,6,1,4,1,272,4,5,46,6),_IpSifStatTotalUdpSessions_Type())
ipSifStatTotalUdpSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatTotalUdpSessions.setStatus(_A)
_IpSifStatTotalTcpSessions_Type=Counter32
_IpSifStatTotalTcpSessions_Object=MibScalar
ipSifStatTotalTcpSessions=_IpSifStatTotalTcpSessions_Object((1,3,6,1,4,1,272,4,5,46,7),_IpSifStatTotalTcpSessions_Type())
ipSifStatTotalTcpSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatTotalTcpSessions.setStatus(_A)
_IpSifStatTotalOtherSessions_Type=Counter32
_IpSifStatTotalOtherSessions_Object=MibScalar
ipSifStatTotalOtherSessions=_IpSifStatTotalOtherSessions_Object((1,3,6,1,4,1,272,4,5,46,8),_IpSifStatTotalOtherSessions_Type())
ipSifStatTotalOtherSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatTotalOtherSessions.setStatus(_A)
_IpSifStatTotalExpectedSessions_Type=Counter32
_IpSifStatTotalExpectedSessions_Object=MibScalar
ipSifStatTotalExpectedSessions=_IpSifStatTotalExpectedSessions_Object((1,3,6,1,4,1,272,4,5,46,9),_IpSifStatTotalExpectedSessions_Type())
ipSifStatTotalExpectedSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifStatTotalExpectedSessions.setStatus(_A)
_IpSifAliasAddressGroupTable_Object=MibTable
ipSifAliasAddressGroupTable=_IpSifAliasAddressGroupTable_Object((1,3,6,1,4,1,272,4,5,47))
if mibBuilder.loadTexts:ipSifAliasAddressGroupTable.setStatus(_A)
_IpSifAliasAddressGroupEntry_Object=MibTableRow
ipSifAliasAddressGroupEntry=_IpSifAliasAddressGroupEntry_Object((1,3,6,1,4,1,272,4,5,47,1))
ipSifAliasAddressGroupEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:ipSifAliasAddressGroupEntry.setStatus(_A)
_IpSifAliasAddressGroupId_Type=Integer32
_IpSifAliasAddressGroupId_Object=MibTableColumn
ipSifAliasAddressGroupId=_IpSifAliasAddressGroupId_Object((1,3,6,1,4,1,272,4,5,47,1,1),_IpSifAliasAddressGroupId_Type())
ipSifAliasAddressGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressGroupId.setStatus(_A)
_IpSifAliasAddressGroupAlias_Type=DisplayString
_IpSifAliasAddressGroupAlias_Object=MibTableColumn
ipSifAliasAddressGroupAlias=_IpSifAliasAddressGroupAlias_Object((1,3,6,1,4,1,272,4,5,47,1,2),_IpSifAliasAddressGroupAlias_Type())
ipSifAliasAddressGroupAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressGroupAlias.setStatus(_A)
_IpSifAliasAddressGroupIndex_Type=Integer32
_IpSifAliasAddressGroupIndex_Object=MibTableColumn
ipSifAliasAddressGroupIndex=_IpSifAliasAddressGroupIndex_Object((1,3,6,1,4,1,272,4,5,47,1,3),_IpSifAliasAddressGroupIndex_Type())
ipSifAliasAddressGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifAliasAddressGroupIndex.setStatus(_A)
class _IpSifAliasAddressGroupMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_F,3)))
_IpSifAliasAddressGroupMode_Type.__name__=_C
_IpSifAliasAddressGroupMode_Object=MibTableColumn
ipSifAliasAddressGroupMode=_IpSifAliasAddressGroupMode_Object((1,3,6,1,4,1,272,4,5,47,1,4),_IpSifAliasAddressGroupMode_Type())
ipSifAliasAddressGroupMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasAddressGroupMode.setStatus(_A)
_IpSifAliasServiceGroupTable_Object=MibTable
ipSifAliasServiceGroupTable=_IpSifAliasServiceGroupTable_Object((1,3,6,1,4,1,272,4,5,48))
if mibBuilder.loadTexts:ipSifAliasServiceGroupTable.setStatus(_A)
_IpSifAliasServiceGroupEntry_Object=MibTableRow
ipSifAliasServiceGroupEntry=_IpSifAliasServiceGroupEntry_Object((1,3,6,1,4,1,272,4,5,48,1))
ipSifAliasServiceGroupEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:ipSifAliasServiceGroupEntry.setStatus(_A)
_IpSifAliasServiceGroupId_Type=Integer32
_IpSifAliasServiceGroupId_Object=MibTableColumn
ipSifAliasServiceGroupId=_IpSifAliasServiceGroupId_Object((1,3,6,1,4,1,272,4,5,48,1,1),_IpSifAliasServiceGroupId_Type())
ipSifAliasServiceGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceGroupId.setStatus(_A)
_IpSifAliasServiceGroupAlias_Type=DisplayString
_IpSifAliasServiceGroupAlias_Object=MibTableColumn
ipSifAliasServiceGroupAlias=_IpSifAliasServiceGroupAlias_Object((1,3,6,1,4,1,272,4,5,48,1,2),_IpSifAliasServiceGroupAlias_Type())
ipSifAliasServiceGroupAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceGroupAlias.setStatus(_A)
_IpSifAliasServiceGroupIndex_Type=Integer32
_IpSifAliasServiceGroupIndex_Object=MibTableColumn
ipSifAliasServiceGroupIndex=_IpSifAliasServiceGroupIndex_Object((1,3,6,1,4,1,272,4,5,48,1,3),_IpSifAliasServiceGroupIndex_Type())
ipSifAliasServiceGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifAliasServiceGroupIndex.setStatus(_A)
class _IpSifAliasServiceGroupMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('service',1),(_F,2)))
_IpSifAliasServiceGroupMode_Type.__name__=_C
_IpSifAliasServiceGroupMode_Object=MibTableColumn
ipSifAliasServiceGroupMode=_IpSifAliasServiceGroupMode_Object((1,3,6,1,4,1,272,4,5,48,1,4),_IpSifAliasServiceGroupMode_Type())
ipSifAliasServiceGroupMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifAliasServiceGroupMode.setStatus(_A)
_IpSifPolicyChkTable_Object=MibTable
ipSifPolicyChkTable=_IpSifPolicyChkTable_Object((1,3,6,1,4,1,272,4,5,49))
if mibBuilder.loadTexts:ipSifPolicyChkTable.setStatus(_A)
_IpSifPolicyChkEntry_Object=MibTableRow
ipSifPolicyChkEntry=_IpSifPolicyChkEntry_Object((1,3,6,1,4,1,272,4,5,49,1))
ipSifPolicyChkEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:ipSifPolicyChkEntry.setStatus(_A)
_IpSifPolicyChkSourceIfIndex_Type=Integer32
_IpSifPolicyChkSourceIfIndex_Object=MibTableColumn
ipSifPolicyChkSourceIfIndex=_IpSifPolicyChkSourceIfIndex_Object((1,3,6,1,4,1,272,4,5,49,1,1),_IpSifPolicyChkSourceIfIndex_Type())
ipSifPolicyChkSourceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkSourceIfIndex.setStatus(_A)
_IpSifPolicyChkDestIfIndex_Type=Integer32
_IpSifPolicyChkDestIfIndex_Object=MibTableColumn
ipSifPolicyChkDestIfIndex=_IpSifPolicyChkDestIfIndex_Object((1,3,6,1,4,1,272,4,5,49,1,2),_IpSifPolicyChkDestIfIndex_Type())
ipSifPolicyChkDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkDestIfIndex.setStatus(_A)
_IpSifPolicyChkSource_Type=IpAddress
_IpSifPolicyChkSource_Object=MibTableColumn
ipSifPolicyChkSource=_IpSifPolicyChkSource_Object((1,3,6,1,4,1,272,4,5,49,1,3),_IpSifPolicyChkSource_Type())
ipSifPolicyChkSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkSource.setStatus(_A)
_IpSifPolicyChkDestination_Type=IpAddress
_IpSifPolicyChkDestination_Object=MibTableColumn
ipSifPolicyChkDestination=_IpSifPolicyChkDestination_Object((1,3,6,1,4,1,272,4,5,49,1,4),_IpSifPolicyChkDestination_Type())
ipSifPolicyChkDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkDestination.setStatus(_A)
_IpSifPolicyChkProtocol_Type=Integer32
_IpSifPolicyChkProtocol_Object=MibTableColumn
ipSifPolicyChkProtocol=_IpSifPolicyChkProtocol_Object((1,3,6,1,4,1,272,4,5,49,1,5),_IpSifPolicyChkProtocol_Type())
ipSifPolicyChkProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkProtocol.setStatus(_A)
_IpSifPolicyChkDestPort_Type=Integer32
_IpSifPolicyChkDestPort_Object=MibTableColumn
ipSifPolicyChkDestPort=_IpSifPolicyChkDestPort_Object((1,3,6,1,4,1,272,4,5,49,1,6),_IpSifPolicyChkDestPort_Type())
ipSifPolicyChkDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkDestPort.setStatus(_A)
class _IpSifPolicyChkRule_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_G,2),(_Q,3),(_a,4)))
_IpSifPolicyChkRule_Type.__name__=_C
_IpSifPolicyChkRule_Object=MibTableColumn
ipSifPolicyChkRule=_IpSifPolicyChkRule_Object((1,3,6,1,4,1,272,4,5,49,1,7),_IpSifPolicyChkRule_Type())
ipSifPolicyChkRule.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifPolicyChkRule.setStatus(_A)
_IpSifPolicyChkRuleOrder_Type=Integer32
_IpSifPolicyChkRuleOrder_Object=MibTableColumn
ipSifPolicyChkRuleOrder=_IpSifPolicyChkRuleOrder_Object((1,3,6,1,4,1,272,4,5,49,1,8),_IpSifPolicyChkRuleOrder_Type())
ipSifPolicyChkRuleOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifPolicyChkRuleOrder.setStatus(_A)
class _IpSifPolicyChkResult_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_G,2),(_a,3)))
_IpSifPolicyChkResult_Type.__name__=_C
_IpSifPolicyChkResult_Object=MibTableColumn
ipSifPolicyChkResult=_IpSifPolicyChkResult_Object((1,3,6,1,4,1,272,4,5,49,1,9),_IpSifPolicyChkResult_Type())
ipSifPolicyChkResult.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifPolicyChkResult.setStatus(_A)
class _IpSifPolicyChkState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initial',1),('trigger',2),('running',3),('done',4)))
_IpSifPolicyChkState_Type.__name__=_C
_IpSifPolicyChkState_Object=MibTableColumn
ipSifPolicyChkState=_IpSifPolicyChkState_Object((1,3,6,1,4,1,272,4,5,49,1,10),_IpSifPolicyChkState_Type())
ipSifPolicyChkState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkState.setStatus(_A)
class _IpSifPolicyChkAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('check',1),(_b,2)))
_IpSifPolicyChkAdminStatus_Type.__name__=_C
_IpSifPolicyChkAdminStatus_Object=MibTableColumn
ipSifPolicyChkAdminStatus=_IpSifPolicyChkAdminStatus_Object((1,3,6,1,4,1,272,4,5,49,1,11),_IpSifPolicyChkAdminStatus_Type())
ipSifPolicyChkAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkAdminStatus.setStatus(_A)
class _IpSifPolicyChkOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('check',1),(_b,2)))
_IpSifPolicyChkOperStatus_Type.__name__=_C
_IpSifPolicyChkOperStatus_Object=MibTableColumn
ipSifPolicyChkOperStatus=_IpSifPolicyChkOperStatus_Object((1,3,6,1,4,1,272,4,5,49,1,12),_IpSifPolicyChkOperStatus_Type())
ipSifPolicyChkOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipSifPolicyChkOperStatus.setStatus(_A)
class _IpSifPolicyChkCurrOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_IpSifPolicyChkCurrOperStatus_Type.__name__=_C
_IpSifPolicyChkCurrOperStatus_Object=MibTableColumn
ipSifPolicyChkCurrOperStatus=_IpSifPolicyChkCurrOperStatus_Object((1,3,6,1,4,1,272,4,5,49,1,13),_IpSifPolicyChkCurrOperStatus_Type())
ipSifPolicyChkCurrOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipSifPolicyChkCurrOperStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'ipSifAliasAddressTable':ipSifAliasAddressTable,'ipSifAliasAddressEntry':ipSifAliasAddressEntry,'ipSifAliasAddressIndex':ipSifAliasAddressIndex,_L:ipSifAliasAddressAlias,'ipSifAliasAddressAddress':ipSifAliasAddressAddress,'ipSifAliasAddressMask':ipSifAliasAddressMask,'ipSifAliasAddressInterface':ipSifAliasAddressInterface,'ipSifAliasAddressMode':ipSifAliasAddressMode,'ipSifAliasAddressRange':ipSifAliasAddressRange,'ipSifAliasAddressGroup':ipSifAliasAddressGroup,'ipSifAliasServiceTable':ipSifAliasServiceTable,'ipSifAliasServiceEntry':ipSifAliasServiceEntry,'ipSifAliasServiceIndex':ipSifAliasServiceIndex,_O:ipSifAliasServiceAlias,'ipSifAliasServiceProtocol':ipSifAliasServiceProtocol,'ipSifAliasServicePort':ipSifAliasServicePort,'ipSifAliasServiceRange':ipSifAliasServiceRange,'ipSifAliasServiceType':ipSifAliasServiceType,'ipSifAliasServiceGroup':ipSifAliasServiceGroup,'ipSifAliasServiceSourcePort':ipSifAliasServiceSourcePort,'ipSifAliasServiceSourceRange':ipSifAliasServiceSourceRange,'ipSifAliasServiceIcmpType':ipSifAliasServiceIcmpType,'ipSifAliasServiceIcmpCode':ipSifAliasServiceIcmpCode,'ipSifAliasTable':ipSifAliasTable,'ipSifAliasEntry':ipSifAliasEntry,_P:ipSifAliasOrder,'ipSifAliasSource':ipSifAliasSource,'ipSifAliasDestination':ipSifAliasDestination,'ipSifAliasService':ipSifAliasService,'ipSifAliasAction':ipSifAliasAction,'ipSifAliasStatus':ipSifAliasStatus,'ipSifAliasPriority':ipSifAliasPriority,'ipSifAliasClassId':ipSifAliasClassId,'ipSifRejectTable':ipSifRejectTable,'ipSifRejectEntry':ipSifRejectEntry,_U:ipSifRejectIndex,'ipSifRejectSource':ipSifRejectSource,'ipSifRejectDestination':ipSifRejectDestination,'ipSifRejectRejects':ipSifRejectRejects,'ipSifRejectSilence':ipSifRejectSilence,'ipSifRejectProtocol':ipSifRejectProtocol,'ipSifRejectPortLo':ipSifRejectPortLo,'ipSifRejectPortHigh':ipSifRejectPortHigh,'ipSifExpectTable':ipSifExpectTable,'ipSifExpectEntry':ipSifExpectEntry,_V:ipSifExpectIndex,'ipSifExpectSource':ipSifExpectSource,'ipSifExpectDestination':ipSifExpectDestination,'ipSifExpectProtocol':ipSifExpectProtocol,'ipSifExpectSourcePort':ipSifExpectSourcePort,'ipSifExpectDestPort':ipSifExpectDestPort,'ipSifExpectPriority':ipSifExpectPriority,'ipSifExpectClassId':ipSifExpectClassId,'ipSifExpectIfIndex':ipSifExpectIfIndex,'ipSif':ipSif,'ipSifAdminStatus':ipSifAdminStatus,'ipSifLocalFilter':ipSifLocalFilter,'ipSifInterfaceFilter':ipSifInterfaceFilter,'ipSifSysloglevel':ipSifSysloglevel,'ipSifUdpTimeout':ipSifUdpTimeout,'ipSifTcpTimeout':ipSifTcpTimeout,'ipSifPPTPTimeout':ipSifPPTPTimeout,'ipSifDefaultTimeout':ipSifDefaultTimeout,'ipSifMaxSessions':ipSifMaxSessions,'ipSifMaxRejectEntries':ipSifMaxRejectEntries,'ipSifMaxRejectTtl':ipSifMaxRejectTtl,'ipSifInterfaceAliasAutoCreate':ipSifInterfaceAliasAutoCreate,'ipSifStat':ipSifStat,'ipSifStatCurrSessions':ipSifStatCurrSessions,'ipSifStatCurrUdpSessions':ipSifStatCurrUdpSessions,'ipSifStatCurrTcpSessions':ipSifStatCurrTcpSessions,'ipSifStatCurrOtherSessions':ipSifStatCurrOtherSessions,'ipSifStatCurrExpectedSessions':ipSifStatCurrExpectedSessions,'ipSifStatTotalUdpSessions':ipSifStatTotalUdpSessions,'ipSifStatTotalTcpSessions':ipSifStatTotalTcpSessions,'ipSifStatTotalOtherSessions':ipSifStatTotalOtherSessions,'ipSifStatTotalExpectedSessions':ipSifStatTotalExpectedSessions,'ipSifAliasAddressGroupTable':ipSifAliasAddressGroupTable,'ipSifAliasAddressGroupEntry':ipSifAliasAddressGroupEntry,_W:ipSifAliasAddressGroupId,'ipSifAliasAddressGroupAlias':ipSifAliasAddressGroupAlias,'ipSifAliasAddressGroupIndex':ipSifAliasAddressGroupIndex,'ipSifAliasAddressGroupMode':ipSifAliasAddressGroupMode,'ipSifAliasServiceGroupTable':ipSifAliasServiceGroupTable,'ipSifAliasServiceGroupEntry':ipSifAliasServiceGroupEntry,_X:ipSifAliasServiceGroupId,'ipSifAliasServiceGroupAlias':ipSifAliasServiceGroupAlias,'ipSifAliasServiceGroupIndex':ipSifAliasServiceGroupIndex,'ipSifAliasServiceGroupMode':ipSifAliasServiceGroupMode,'ipSifPolicyChkTable':ipSifPolicyChkTable,'ipSifPolicyChkEntry':ipSifPolicyChkEntry,'ipSifPolicyChkSourceIfIndex':ipSifPolicyChkSourceIfIndex,'ipSifPolicyChkDestIfIndex':ipSifPolicyChkDestIfIndex,'ipSifPolicyChkSource':ipSifPolicyChkSource,'ipSifPolicyChkDestination':ipSifPolicyChkDestination,_Y:ipSifPolicyChkProtocol,_Z:ipSifPolicyChkDestPort,'ipSifPolicyChkRule':ipSifPolicyChkRule,'ipSifPolicyChkRuleOrder':ipSifPolicyChkRuleOrder,'ipSifPolicyChkResult':ipSifPolicyChkResult,'ipSifPolicyChkState':ipSifPolicyChkState,'ipSifPolicyChkAdminStatus':ipSifPolicyChkAdminStatus,'ipSifPolicyChkOperStatus':ipSifPolicyChkOperStatus,'ipSifPolicyChkCurrOperStatus':ipSifPolicyChkCurrOperStatus})