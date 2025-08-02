_q='tnOspfv3MultiAreaConfigGroup'
_p='tnOspfMultiAreaConfigGroup'
_o='tnOspfPortGroup'
_n='tnOspfAreaGroup'
_m='tnOspfv3MultiAreaConfigRowStatus'
_l='tnOspfv3MultiAreaConfigVirtualLinkIp'
_k='tnOspfv3MultiAreaConfigDefaultCost'
_j='tnOspfv3MultiAreaConfigNssaTranslate'
_i='tnOspfv3MultiAreaConfigWavekeyOpaqueLsa'
_h='tnOspfv3MultiAreaConfigDnsOpaqueLsa'
_g='tnOspfv3MultiAreaConfigType'
_f='tnOspfv3MultiAreaId'
_e='tnOspfMultiAreaConfigRowStatus'
_d='tnOspfMultiAreaConfigVirtualLinkIp'
_c='tnOspfMultiAreaConfigDefaultCost'
_b='tnOspfMultiAreaConfigNssaTranslate'
_a='tnOspfMultiAreaConfigWavekeyOpaqueLsa'
_Z='tnOspfMultiAreaConfigDnsOpaqueLsa'
_Y='tnOspfMultiAreaConfigType'
_X='tnOspfMultiAreaId'
_W='tnOspfv3PortTopologyId'
_V='tnOspfPortTopologyId'
_U='tnOspfv3MultiAreaTopologyId'
_T='00000000'
_S='notApplicable'
_R='always'
_Q='candidate'
_P='nssaTotallyStub'
_O='totallyStub'
_N='normal'
_M='ifIndex'
_L='IF-MIB'
_K='not-accessible'
_J='tnOspfAreaId'
_I='RowStatus'
_H='IpAddress'
_G='no'
_F='yes'
_E='tnOspfAreaTopologyId'
_D='Integer32'
_C='read-create'
_B='TROPIC-OSPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_L,_M)
AreaID,=mibBuilder.importSymbols('OSPF-MIB','AreaID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_H,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_I,'TextualConvention')
tnOspfMIB,tnProtocolModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnOspfMIB','tnProtocolModules')
tnOspfMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,4,3))
if mibBuilder.loadTexts:tnOspfMibModule.setRevisions(('2021-08-20 12:00','2021-07-23 12:00','2018-02-23 12:00','2016-11-16 12:00','2015-04-03 12:00','2012-06-13 12:00','2011-09-28 12:00','2011-08-31 12:00','2011-04-15 12:00','2009-01-09 12:00','2008-12-18 12:00','2008-07-24 12:00','2008-06-09 12:00','2008-03-28 12:00','2008-03-06 12:00'))
class TnTopologyId(TextualConvention,Unsigned32):status=_A
_TnOspfConf_ObjectIdentity=ObjectIdentity
tnOspfConf=_TnOspfConf_ObjectIdentity((1,3,6,1,4,1,7483,2,5,1,1))
_TnOspfGroups_ObjectIdentity=ObjectIdentity
tnOspfGroups=_TnOspfGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,5,1,1,1))
_TnOspfCompliances_ObjectIdentity=ObjectIdentity
tnOspfCompliances=_TnOspfCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,5,1,1,2))
_TnOspfObjs_ObjectIdentity=ObjectIdentity
tnOspfObjs=_TnOspfObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,5,1,2))
_TnOspfAreaTable_Object=MibTable
tnOspfAreaTable=_TnOspfAreaTable_Object((1,3,6,1,4,1,7483,2,5,1,2,2))
if mibBuilder.loadTexts:tnOspfAreaTable.setStatus(_A)
_TnOspfAreaEntry_Object=MibTableRow
tnOspfAreaEntry=_TnOspfAreaEntry_Object((1,3,6,1,4,1,7483,2,5,1,2,2,1))
tnOspfAreaEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:tnOspfAreaEntry.setStatus(_A)
_TnOspfAreaTopologyId_Type=TnTopologyId
_TnOspfAreaTopologyId_Object=MibTableColumn
tnOspfAreaTopologyId=_TnOspfAreaTopologyId_Object((1,3,6,1,4,1,7483,2,5,1,2,2,1,1),_TnOspfAreaTopologyId_Type())
tnOspfAreaTopologyId.setMaxAccess(_K)
if mibBuilder.loadTexts:tnOspfAreaTopologyId.setStatus(_A)
_TnOspfAreaId_Type=AreaID
_TnOspfAreaId_Object=MibTableColumn
tnOspfAreaId=_TnOspfAreaId_Object((1,3,6,1,4,1,7483,2,5,1,2,2,1,2),_TnOspfAreaId_Type())
tnOspfAreaId.setMaxAccess(_K)
if mibBuilder.loadTexts:tnOspfAreaId.setStatus(_A)
_TnOspfPortTable_Object=MibTable
tnOspfPortTable=_TnOspfPortTable_Object((1,3,6,1,4,1,7483,2,5,1,2,21))
if mibBuilder.loadTexts:tnOspfPortTable.setStatus(_A)
_TnOspfPortEntry_Object=MibTableRow
tnOspfPortEntry=_TnOspfPortEntry_Object((1,3,6,1,4,1,7483,2,5,1,2,21,1))
tnOspfPortEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:tnOspfPortEntry.setStatus(_A)
_TnOspfPortTopologyId_Type=TnTopologyId
_TnOspfPortTopologyId_Object=MibTableColumn
tnOspfPortTopologyId=_TnOspfPortTopologyId_Object((1,3,6,1,4,1,7483,2,5,1,2,21,1,1),_TnOspfPortTopologyId_Type())
tnOspfPortTopologyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfPortTopologyId.setStatus(_A)
_TnOspfv3PortTopologyId_Type=TnTopologyId
_TnOspfv3PortTopologyId_Object=MibTableColumn
tnOspfv3PortTopologyId=_TnOspfv3PortTopologyId_Object((1,3,6,1,4,1,7483,2,5,1,2,21,1,2),_TnOspfv3PortTopologyId_Type())
tnOspfv3PortTopologyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3PortTopologyId.setStatus(_A)
_TnOspfMultiAreaConfigTable_Object=MibTable
tnOspfMultiAreaConfigTable=_TnOspfMultiAreaConfigTable_Object((1,3,6,1,4,1,7483,2,5,1,2,22))
if mibBuilder.loadTexts:tnOspfMultiAreaConfigTable.setStatus(_A)
_TnOspfMultiAreaConfigEntry_Object=MibTableRow
tnOspfMultiAreaConfigEntry=_TnOspfMultiAreaConfigEntry_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1))
tnOspfMultiAreaConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:tnOspfMultiAreaConfigEntry.setStatus(_A)
_TnOspfMultiAreaId_Type=AreaID
_TnOspfMultiAreaId_Object=MibTableColumn
tnOspfMultiAreaId=_TnOspfMultiAreaId_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,1),_TnOspfMultiAreaId_Type())
tnOspfMultiAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaId.setStatus(_A)
class _TnOspfMultiAreaConfigType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('stub',2),(_O,3),('nssa',4),(_P,5)))
_TnOspfMultiAreaConfigType_Type.__name__=_D
_TnOspfMultiAreaConfigType_Object=MibTableColumn
tnOspfMultiAreaConfigType=_TnOspfMultiAreaConfigType_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,2),_TnOspfMultiAreaConfigType_Type())
tnOspfMultiAreaConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigType.setStatus(_A)
class _TnOspfMultiAreaConfigDnsOpaqueLsa_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TnOspfMultiAreaConfigDnsOpaqueLsa_Type.__name__=_D
_TnOspfMultiAreaConfigDnsOpaqueLsa_Object=MibTableColumn
tnOspfMultiAreaConfigDnsOpaqueLsa=_TnOspfMultiAreaConfigDnsOpaqueLsa_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,3),_TnOspfMultiAreaConfigDnsOpaqueLsa_Type())
tnOspfMultiAreaConfigDnsOpaqueLsa.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigDnsOpaqueLsa.setStatus(_A)
class _TnOspfMultiAreaConfigWavekeyOpaqueLsa_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TnOspfMultiAreaConfigWavekeyOpaqueLsa_Type.__name__=_D
_TnOspfMultiAreaConfigWavekeyOpaqueLsa_Object=MibTableColumn
tnOspfMultiAreaConfigWavekeyOpaqueLsa=_TnOspfMultiAreaConfigWavekeyOpaqueLsa_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,4),_TnOspfMultiAreaConfigWavekeyOpaqueLsa_Type())
tnOspfMultiAreaConfigWavekeyOpaqueLsa.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigWavekeyOpaqueLsa.setStatus(_A)
class _TnOspfMultiAreaConfigNssaTranslate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),('never',3),(_S,4)))
_TnOspfMultiAreaConfigNssaTranslate_Type.__name__=_D
_TnOspfMultiAreaConfigNssaTranslate_Object=MibTableColumn
tnOspfMultiAreaConfigNssaTranslate=_TnOspfMultiAreaConfigNssaTranslate_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,5),_TnOspfMultiAreaConfigNssaTranslate_Type())
tnOspfMultiAreaConfigNssaTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigNssaTranslate.setStatus(_A)
class _TnOspfMultiAreaConfigDefaultCost_Type(Integer32):defaultValue=10
_TnOspfMultiAreaConfigDefaultCost_Type.__name__=_D
_TnOspfMultiAreaConfigDefaultCost_Object=MibTableColumn
tnOspfMultiAreaConfigDefaultCost=_TnOspfMultiAreaConfigDefaultCost_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,6),_TnOspfMultiAreaConfigDefaultCost_Type())
tnOspfMultiAreaConfigDefaultCost.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigDefaultCost.setStatus(_A)
class _TnOspfMultiAreaConfigVirtualLinkIp_Type(IpAddress):defaultHexValue=_T
_TnOspfMultiAreaConfigVirtualLinkIp_Type.__name__=_H
_TnOspfMultiAreaConfigVirtualLinkIp_Object=MibTableColumn
tnOspfMultiAreaConfigVirtualLinkIp=_TnOspfMultiAreaConfigVirtualLinkIp_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,7),_TnOspfMultiAreaConfigVirtualLinkIp_Type())
tnOspfMultiAreaConfigVirtualLinkIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigVirtualLinkIp.setStatus(_A)
class _TnOspfMultiAreaConfigRowStatus_Type(RowStatus):defaultValue=6
_TnOspfMultiAreaConfigRowStatus_Type.__name__=_I
_TnOspfMultiAreaConfigRowStatus_Object=MibTableColumn
tnOspfMultiAreaConfigRowStatus=_TnOspfMultiAreaConfigRowStatus_Object((1,3,6,1,4,1,7483,2,5,1,2,22,1,8),_TnOspfMultiAreaConfigRowStatus_Type())
tnOspfMultiAreaConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfMultiAreaConfigRowStatus.setStatus(_A)
_TnOspfv3MultiAreaConfigTable_Object=MibTable
tnOspfv3MultiAreaConfigTable=_TnOspfv3MultiAreaConfigTable_Object((1,3,6,1,4,1,7483,2,5,1,2,23))
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigTable.setStatus(_A)
_TnOspfv3MultiAreaConfigEntry_Object=MibTableRow
tnOspfv3MultiAreaConfigEntry=_TnOspfv3MultiAreaConfigEntry_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1))
tnOspfv3MultiAreaConfigEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigEntry.setStatus(_A)
_TnOspfv3MultiAreaTopologyId_Type=TnTopologyId
_TnOspfv3MultiAreaTopologyId_Object=MibTableColumn
tnOspfv3MultiAreaTopologyId=_TnOspfv3MultiAreaTopologyId_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,1),_TnOspfv3MultiAreaTopologyId_Type())
tnOspfv3MultiAreaTopologyId.setMaxAccess(_K)
if mibBuilder.loadTexts:tnOspfv3MultiAreaTopologyId.setStatus(_A)
_TnOspfv3MultiAreaId_Type=AreaID
_TnOspfv3MultiAreaId_Object=MibTableColumn
tnOspfv3MultiAreaId=_TnOspfv3MultiAreaId_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,2),_TnOspfv3MultiAreaId_Type())
tnOspfv3MultiAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaId.setStatus(_A)
class _TnOspfv3MultiAreaConfigType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('stub',2),(_O,3),('nssa',4),(_P,5)))
_TnOspfv3MultiAreaConfigType_Type.__name__=_D
_TnOspfv3MultiAreaConfigType_Object=MibTableColumn
tnOspfv3MultiAreaConfigType=_TnOspfv3MultiAreaConfigType_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,3),_TnOspfv3MultiAreaConfigType_Type())
tnOspfv3MultiAreaConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigType.setStatus(_A)
class _TnOspfv3MultiAreaConfigDnsOpaqueLsa_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TnOspfv3MultiAreaConfigDnsOpaqueLsa_Type.__name__=_D
_TnOspfv3MultiAreaConfigDnsOpaqueLsa_Object=MibTableColumn
tnOspfv3MultiAreaConfigDnsOpaqueLsa=_TnOspfv3MultiAreaConfigDnsOpaqueLsa_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,4),_TnOspfv3MultiAreaConfigDnsOpaqueLsa_Type())
tnOspfv3MultiAreaConfigDnsOpaqueLsa.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigDnsOpaqueLsa.setStatus(_A)
class _TnOspfv3MultiAreaConfigWavekeyOpaqueLsa_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TnOspfv3MultiAreaConfigWavekeyOpaqueLsa_Type.__name__=_D
_TnOspfv3MultiAreaConfigWavekeyOpaqueLsa_Object=MibTableColumn
tnOspfv3MultiAreaConfigWavekeyOpaqueLsa=_TnOspfv3MultiAreaConfigWavekeyOpaqueLsa_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,5),_TnOspfv3MultiAreaConfigWavekeyOpaqueLsa_Type())
tnOspfv3MultiAreaConfigWavekeyOpaqueLsa.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigWavekeyOpaqueLsa.setStatus(_A)
class _TnOspfv3MultiAreaConfigNssaTranslate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),('never',3),(_S,4)))
_TnOspfv3MultiAreaConfigNssaTranslate_Type.__name__=_D
_TnOspfv3MultiAreaConfigNssaTranslate_Object=MibTableColumn
tnOspfv3MultiAreaConfigNssaTranslate=_TnOspfv3MultiAreaConfigNssaTranslate_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,6),_TnOspfv3MultiAreaConfigNssaTranslate_Type())
tnOspfv3MultiAreaConfigNssaTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigNssaTranslate.setStatus(_A)
class _TnOspfv3MultiAreaConfigDefaultCost_Type(Integer32):defaultValue=10
_TnOspfv3MultiAreaConfigDefaultCost_Type.__name__=_D
_TnOspfv3MultiAreaConfigDefaultCost_Object=MibTableColumn
tnOspfv3MultiAreaConfigDefaultCost=_TnOspfv3MultiAreaConfigDefaultCost_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,7),_TnOspfv3MultiAreaConfigDefaultCost_Type())
tnOspfv3MultiAreaConfigDefaultCost.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigDefaultCost.setStatus(_A)
class _TnOspfv3MultiAreaConfigVirtualLinkIp_Type(IpAddress):defaultHexValue=_T
_TnOspfv3MultiAreaConfigVirtualLinkIp_Type.__name__=_H
_TnOspfv3MultiAreaConfigVirtualLinkIp_Object=MibTableColumn
tnOspfv3MultiAreaConfigVirtualLinkIp=_TnOspfv3MultiAreaConfigVirtualLinkIp_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,8),_TnOspfv3MultiAreaConfigVirtualLinkIp_Type())
tnOspfv3MultiAreaConfigVirtualLinkIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigVirtualLinkIp.setStatus(_A)
class _TnOspfv3MultiAreaConfigRowStatus_Type(RowStatus):defaultValue=6
_TnOspfv3MultiAreaConfigRowStatus_Type.__name__=_I
_TnOspfv3MultiAreaConfigRowStatus_Object=MibTableColumn
tnOspfv3MultiAreaConfigRowStatus=_TnOspfv3MultiAreaConfigRowStatus_Object((1,3,6,1,4,1,7483,2,5,1,2,23,1,9),_TnOspfv3MultiAreaConfigRowStatus_Type())
tnOspfv3MultiAreaConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigRowStatus.setStatus(_A)
tnOspfAreaGroup=ObjectGroup((1,3,6,1,4,1,7483,2,5,1,1,1,2))
tnOspfAreaGroup.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:tnOspfAreaGroup.setStatus(_A)
tnOspfPortGroup=ObjectGroup((1,3,6,1,4,1,7483,2,5,1,1,1,21))
tnOspfPortGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:tnOspfPortGroup.setStatus(_A)
tnOspfMultiAreaConfigGroup=ObjectGroup((1,3,6,1,4,1,7483,2,5,1,1,1,22))
tnOspfMultiAreaConfigGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:tnOspfMultiAreaConfigGroup.setStatus(_A)
tnOspfv3MultiAreaConfigGroup=ObjectGroup((1,3,6,1,4,1,7483,2,5,1,1,1,23))
tnOspfv3MultiAreaConfigGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:tnOspfv3MultiAreaConfigGroup.setStatus(_A)
tnOspfCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,5,1,1,2,1))
tnOspfCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:tnOspfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TnTopologyId':TnTopologyId,'tnOspfMibModule':tnOspfMibModule,'tnOspfConf':tnOspfConf,'tnOspfGroups':tnOspfGroups,_n:tnOspfAreaGroup,_o:tnOspfPortGroup,_p:tnOspfMultiAreaConfigGroup,_q:tnOspfv3MultiAreaConfigGroup,'tnOspfCompliances':tnOspfCompliances,'tnOspfCompliance':tnOspfCompliance,'tnOspfObjs':tnOspfObjs,'tnOspfAreaTable':tnOspfAreaTable,'tnOspfAreaEntry':tnOspfAreaEntry,_E:tnOspfAreaTopologyId,_J:tnOspfAreaId,'tnOspfPortTable':tnOspfPortTable,'tnOspfPortEntry':tnOspfPortEntry,_V:tnOspfPortTopologyId,_W:tnOspfv3PortTopologyId,'tnOspfMultiAreaConfigTable':tnOspfMultiAreaConfigTable,'tnOspfMultiAreaConfigEntry':tnOspfMultiAreaConfigEntry,_X:tnOspfMultiAreaId,_Y:tnOspfMultiAreaConfigType,_Z:tnOspfMultiAreaConfigDnsOpaqueLsa,_a:tnOspfMultiAreaConfigWavekeyOpaqueLsa,_b:tnOspfMultiAreaConfigNssaTranslate,_c:tnOspfMultiAreaConfigDefaultCost,_d:tnOspfMultiAreaConfigVirtualLinkIp,_e:tnOspfMultiAreaConfigRowStatus,'tnOspfv3MultiAreaConfigTable':tnOspfv3MultiAreaConfigTable,'tnOspfv3MultiAreaConfigEntry':tnOspfv3MultiAreaConfigEntry,_U:tnOspfv3MultiAreaTopologyId,_f:tnOspfv3MultiAreaId,_g:tnOspfv3MultiAreaConfigType,_h:tnOspfv3MultiAreaConfigDnsOpaqueLsa,_i:tnOspfv3MultiAreaConfigWavekeyOpaqueLsa,_j:tnOspfv3MultiAreaConfigNssaTranslate,_k:tnOspfv3MultiAreaConfigDefaultCost,_l:tnOspfv3MultiAreaConfigVirtualLinkIp,_m:tnOspfv3MultiAreaConfigRowStatus})