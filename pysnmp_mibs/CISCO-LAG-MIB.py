_o='clagAggPortListInterfaceIndexGroup'
_n='clagAggPortListInterfaceIndexList'
_m='clagAggChannelIfMinLink'
_l='clagAggHashDistMethodGlobalConfig'
_k='clagAggChannelIfHashDistOperMethod'
_j='clagAggChannelIfHashDistAdminMethod'
_i='clagAggChannelIfMaxBundle'
_h='clagAggChannelIfFastSwitchOver'
_g='clagAggPortRate'
_f='clagAggMaxAggregators'
_e='clagAggPortListPorts'
_d='clagAggDistributionMplsProtocol'
_c='clagAggDistributionAddressMode'
_b='clagAggDistributionProtocol'
_a='clagAggPortAdminStatus'
_Z='clagAggProtocolType'
_Y='clagAggPortListEntry'
_X='clagAggPortEntry'
_W='Unsigned32'
_V='OctetString'
_U='clagAggChannelIfMinLinkGroup'
_T='clagAggHashDistGlobalGroup'
_S='clagAggChannelIfHashDistMethodGroup'
_R='clagAggChannelIfLacpGroup'
_Q='clagAggRateGroup'
_P='fixed'
_O='adaptive'
_N='ifIndex'
_M='IF-MIB'
_L='clagAggMaxAggregatorsGroup'
_K='read-only'
_J='clagAggPortListGroup'
_I='deprecated'
_H='Integer32'
_G='clagAggDistributionMplsGroup'
_F='clagAggDistributionGroup'
_E='clagAggPortGroup'
_D='clagAggProtocolGroup'
_C='read-write'
_B='current'
_A='CISCO-LAG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoInterfaceIndexList,=mibBuilder.importSymbols('CISCO-TC','CiscoInterfaceIndexList')
dot3adAggPortEntry,dot3adAggPortListEntry=mibBuilder.importSymbols('IEEE8023-LAG-MIB','dot3adAggPortEntry','dot3adAggPortListEntry')
ifIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoLagMIB=ModuleIdentity((1,3,6,1,4,1,9,9,225))
if mibBuilder.loadTexts:ciscoLagMIB.setRevisions(('2014-01-14 00:00','2010-10-20 00:00','2009-11-19 00:00','2008-01-08 00:00','2006-06-21 00:00','2004-06-11 00:00','2002-12-13 00:00','2002-01-02 00:00','2001-10-23 00:00'))
class ClagDistributionProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ip',1),('mac',2),('port',3),('vlanIpPort',4),('vlanIp',5),('ipPort',6)))
class ClagDistributionAddressMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('source',1),('destination',2),('both',3)))
class ClagDistributionMplsProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('label',1),('labelIp',2)))
class ClagAggregationProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lacp',1),('pagp',2)))
class ClagPortAdminStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('on',2),('active',3),('passive',4)))
_ClagMIBObjects_ObjectIdentity=ObjectIdentity
clagMIBObjects=_ClagMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,225,1))
_ClagGlobalConfigObjects_ObjectIdentity=ObjectIdentity
clagGlobalConfigObjects=_ClagGlobalConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,225,1,1))
_ClagAggDistributionProtocol_Type=ClagDistributionProtocol
_ClagAggDistributionProtocol_Object=MibScalar
clagAggDistributionProtocol=_ClagAggDistributionProtocol_Object((1,3,6,1,4,1,9,9,225,1,1,1),_ClagAggDistributionProtocol_Type())
clagAggDistributionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggDistributionProtocol.setStatus(_B)
_ClagAggDistributionAddressMode_Type=ClagDistributionAddressMode
_ClagAggDistributionAddressMode_Object=MibScalar
clagAggDistributionAddressMode=_ClagAggDistributionAddressMode_Object((1,3,6,1,4,1,9,9,225,1,1,2),_ClagAggDistributionAddressMode_Type())
clagAggDistributionAddressMode.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggDistributionAddressMode.setStatus(_B)
_ClagAggDistributionMplsProtocol_Type=ClagDistributionMplsProtocol
_ClagAggDistributionMplsProtocol_Object=MibScalar
clagAggDistributionMplsProtocol=_ClagAggDistributionMplsProtocol_Object((1,3,6,1,4,1,9,9,225,1,1,3),_ClagAggDistributionMplsProtocol_Type())
clagAggDistributionMplsProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggDistributionMplsProtocol.setStatus(_B)
_ClagAggMaxAggregators_Type=Unsigned32
_ClagAggMaxAggregators_Object=MibScalar
clagAggMaxAggregators=_ClagAggMaxAggregators_Object((1,3,6,1,4,1,9,9,225,1,1,4),_ClagAggMaxAggregators_Type())
clagAggMaxAggregators.setMaxAccess(_K)
if mibBuilder.loadTexts:clagAggMaxAggregators.setStatus(_B)
class _ClagAggHashDistMethodGlobalConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ClagAggHashDistMethodGlobalConfig_Type.__name__=_H
_ClagAggHashDistMethodGlobalConfig_Object=MibScalar
clagAggHashDistMethodGlobalConfig=_ClagAggHashDistMethodGlobalConfig_Object((1,3,6,1,4,1,9,9,225,1,1,5),_ClagAggHashDistMethodGlobalConfig_Type())
clagAggHashDistMethodGlobalConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggHashDistMethodGlobalConfig.setStatus(_B)
_ClagAgg_ObjectIdentity=ObjectIdentity
clagAgg=_ClagAgg_ObjectIdentity((1,3,6,1,4,1,9,9,225,1,2))
_ClagAggProtocolTable_Object=MibTable
clagAggProtocolTable=_ClagAggProtocolTable_Object((1,3,6,1,4,1,9,9,225,1,2,1))
if mibBuilder.loadTexts:clagAggProtocolTable.setStatus(_B)
_ClagAggProtocolEntry_Object=MibTableRow
clagAggProtocolEntry=_ClagAggProtocolEntry_Object((1,3,6,1,4,1,9,9,225,1,2,1,1))
clagAggProtocolEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:clagAggProtocolEntry.setStatus(_B)
_ClagAggProtocolType_Type=ClagAggregationProtocol
_ClagAggProtocolType_Object=MibTableColumn
clagAggProtocolType=_ClagAggProtocolType_Object((1,3,6,1,4,1,9,9,225,1,2,1,1,1),_ClagAggProtocolType_Type())
clagAggProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggProtocolType.setStatus(_B)
_ClagAggPort_ObjectIdentity=ObjectIdentity
clagAggPort=_ClagAggPort_ObjectIdentity((1,3,6,1,4,1,9,9,225,1,3))
_ClagAggPortTable_Object=MibTable
clagAggPortTable=_ClagAggPortTable_Object((1,3,6,1,4,1,9,9,225,1,3,1))
if mibBuilder.loadTexts:clagAggPortTable.setStatus(_B)
_ClagAggPortEntry_Object=MibTableRow
clagAggPortEntry=_ClagAggPortEntry_Object((1,3,6,1,4,1,9,9,225,1,3,1,1))
if mibBuilder.loadTexts:clagAggPortEntry.setStatus(_B)
_ClagAggPortAdminStatus_Type=ClagPortAdminStatus
_ClagAggPortAdminStatus_Object=MibTableColumn
clagAggPortAdminStatus=_ClagAggPortAdminStatus_Object((1,3,6,1,4,1,9,9,225,1,3,1,1,1),_ClagAggPortAdminStatus_Type())
clagAggPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggPortAdminStatus.setStatus(_B)
class _ClagAggPortRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('normal',2)))
_ClagAggPortRate_Type.__name__=_H
_ClagAggPortRate_Object=MibTableColumn
clagAggPortRate=_ClagAggPortRate_Object((1,3,6,1,4,1,9,9,225,1,3,1,1,2),_ClagAggPortRate_Type())
clagAggPortRate.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggPortRate.setStatus(_B)
_ClagAggPortList_ObjectIdentity=ObjectIdentity
clagAggPortList=_ClagAggPortList_ObjectIdentity((1,3,6,1,4,1,9,9,225,1,4))
_ClagAggPortListTable_Object=MibTable
clagAggPortListTable=_ClagAggPortListTable_Object((1,3,6,1,4,1,9,9,225,1,4,1))
if mibBuilder.loadTexts:clagAggPortListTable.setStatus(_B)
_ClagAggPortListEntry_Object=MibTableRow
clagAggPortListEntry=_ClagAggPortListEntry_Object((1,3,6,1,4,1,9,9,225,1,4,1,1))
if mibBuilder.loadTexts:clagAggPortListEntry.setStatus(_B)
class _ClagAggPortListPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,256))
_ClagAggPortListPorts_Type.__name__=_V
_ClagAggPortListPorts_Object=MibTableColumn
clagAggPortListPorts=_ClagAggPortListPorts_Object((1,3,6,1,4,1,9,9,225,1,4,1,1,1),_ClagAggPortListPorts_Type())
clagAggPortListPorts.setMaxAccess(_K)
if mibBuilder.loadTexts:clagAggPortListPorts.setStatus(_B)
_ClagAggPortListInterfaceIndexList_Type=CiscoInterfaceIndexList
_ClagAggPortListInterfaceIndexList_Object=MibTableColumn
clagAggPortListInterfaceIndexList=_ClagAggPortListInterfaceIndexList_Object((1,3,6,1,4,1,9,9,225,1,4,1,1,2),_ClagAggPortListInterfaceIndexList_Type())
clagAggPortListInterfaceIndexList.setMaxAccess(_K)
if mibBuilder.loadTexts:clagAggPortListInterfaceIndexList.setStatus(_B)
_ClagAggChannelIntf_ObjectIdentity=ObjectIdentity
clagAggChannelIntf=_ClagAggChannelIntf_ObjectIdentity((1,3,6,1,4,1,9,9,225,1,5))
_ClagAggChannelIfTable_Object=MibTable
clagAggChannelIfTable=_ClagAggChannelIfTable_Object((1,3,6,1,4,1,9,9,225,1,5,1))
if mibBuilder.loadTexts:clagAggChannelIfTable.setStatus(_B)
_ClagAggChannelIfEntry_Object=MibTableRow
clagAggChannelIfEntry=_ClagAggChannelIfEntry_Object((1,3,6,1,4,1,9,9,225,1,5,1,1))
clagAggChannelIfEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:clagAggChannelIfEntry.setStatus(_B)
_ClagAggChannelIfFastSwitchOver_Type=TruthValue
_ClagAggChannelIfFastSwitchOver_Object=MibTableColumn
clagAggChannelIfFastSwitchOver=_ClagAggChannelIfFastSwitchOver_Object((1,3,6,1,4,1,9,9,225,1,5,1,1,1),_ClagAggChannelIfFastSwitchOver_Type())
clagAggChannelIfFastSwitchOver.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggChannelIfFastSwitchOver.setStatus(_B)
class _ClagAggChannelIfMaxBundle_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClagAggChannelIfMaxBundle_Type.__name__=_W
_ClagAggChannelIfMaxBundle_Object=MibTableColumn
clagAggChannelIfMaxBundle=_ClagAggChannelIfMaxBundle_Object((1,3,6,1,4,1,9,9,225,1,5,1,1,2),_ClagAggChannelIfMaxBundle_Type())
clagAggChannelIfMaxBundle.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggChannelIfMaxBundle.setStatus(_B)
_ClagAggChannelIfMinLink_Type=Unsigned32
_ClagAggChannelIfMinLink_Object=MibTableColumn
clagAggChannelIfMinLink=_ClagAggChannelIfMinLink_Object((1,3,6,1,4,1,9,9,225,1,5,1,1,3),_ClagAggChannelIfMinLink_Type())
clagAggChannelIfMinLink.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggChannelIfMinLink.setStatus(_B)
class _ClagAggChannelIfHashDistAdminMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_O,2),(_P,3)))
_ClagAggChannelIfHashDistAdminMethod_Type.__name__=_H
_ClagAggChannelIfHashDistAdminMethod_Object=MibTableColumn
clagAggChannelIfHashDistAdminMethod=_ClagAggChannelIfHashDistAdminMethod_Object((1,3,6,1,4,1,9,9,225,1,5,1,1,4),_ClagAggChannelIfHashDistAdminMethod_Type())
clagAggChannelIfHashDistAdminMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:clagAggChannelIfHashDistAdminMethod.setStatus(_B)
class _ClagAggChannelIfHashDistOperMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_O,2),(_P,3)))
_ClagAggChannelIfHashDistOperMethod_Type.__name__=_H
_ClagAggChannelIfHashDistOperMethod_Object=MibTableColumn
clagAggChannelIfHashDistOperMethod=_ClagAggChannelIfHashDistOperMethod_Object((1,3,6,1,4,1,9,9,225,1,5,1,1,5),_ClagAggChannelIfHashDistOperMethod_Type())
clagAggChannelIfHashDistOperMethod.setMaxAccess(_K)
if mibBuilder.loadTexts:clagAggChannelIfHashDistOperMethod.setStatus(_B)
_ClagMIBNotifications_ObjectIdentity=ObjectIdentity
clagMIBNotifications=_ClagMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,225,2))
_ClagMIBConformance_ObjectIdentity=ObjectIdentity
clagMIBConformance=_ClagMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,225,3))
_ClagMIBCompliances_ObjectIdentity=ObjectIdentity
clagMIBCompliances=_ClagMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,225,3,1))
_ClagMIBGroups_ObjectIdentity=ObjectIdentity
clagMIBGroups=_ClagMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,225,3,2))
dot3adAggPortEntry.registerAugmentions((_A,_X))
clagAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
dot3adAggPortListEntry.registerAugmentions((_A,_Y))
clagAggPortListEntry.setIndexNames(*dot3adAggPortListEntry.getIndexNames())
clagAggProtocolGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,1))
clagAggProtocolGroup.setObjects((_A,_Z))
if mibBuilder.loadTexts:clagAggProtocolGroup.setStatus(_B)
clagAggPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,2))
clagAggPortGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:clagAggPortGroup.setStatus(_B)
clagAggDistributionGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,3))
clagAggDistributionGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:clagAggDistributionGroup.setStatus(_B)
clagAggDistributionMplsGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,4))
clagAggDistributionMplsGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:clagAggDistributionMplsGroup.setStatus(_B)
clagAggPortListGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,5))
clagAggPortListGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:clagAggPortListGroup.setStatus(_B)
clagAggMaxAggregatorsGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,6))
clagAggMaxAggregatorsGroup.setObjects((_A,_f))
if mibBuilder.loadTexts:clagAggMaxAggregatorsGroup.setStatus(_B)
clagAggRateGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,7))
clagAggRateGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:clagAggRateGroup.setStatus(_B)
clagAggChannelIfLacpGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,8))
clagAggChannelIfLacpGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:clagAggChannelIfLacpGroup.setStatus(_B)
clagAggChannelIfHashDistMethodGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,9))
clagAggChannelIfHashDistMethodGroup.setObjects(*((_A,_j),(_A,_k)))
if mibBuilder.loadTexts:clagAggChannelIfHashDistMethodGroup.setStatus(_B)
clagAggHashDistGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,10))
clagAggHashDistGlobalGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:clagAggHashDistGlobalGroup.setStatus(_B)
clagAggChannelIfMinLinkGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,11))
clagAggChannelIfMinLinkGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:clagAggChannelIfMinLinkGroup.setStatus(_B)
clagAggPortListInterfaceIndexGroup=ObjectGroup((1,3,6,1,4,1,9,9,225,3,2,12))
clagAggPortListInterfaceIndexGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:clagAggPortListInterfaceIndexGroup.setStatus(_B)
clagMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,225,3,1,1))
clagMIBCompliance.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:clagMIBCompliance.setStatus(_I)
clagMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,225,3,1,2))
clagMIBCompliance2.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:clagMIBCompliance2.setStatus(_I)
clagMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,225,3,1,3))
clagMIBCompliance3.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_J)))
if mibBuilder.loadTexts:clagMIBCompliance3.setStatus(_I)
clagMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,225,3,1,4))
clagMIBCompliance4.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_L)))
if mibBuilder.loadTexts:clagMIBCompliance4.setStatus(_I)
clagMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,225,3,1,5))
clagMIBCompliance5.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_L),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:clagMIBCompliance5.setStatus(_I)
clagMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,225,3,1,6))
clagMIBCompliance6.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_L),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_o)))
if mibBuilder.loadTexts:clagMIBCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ClagDistributionProtocol':ClagDistributionProtocol,'ClagDistributionAddressMode':ClagDistributionAddressMode,'ClagDistributionMplsProtocol':ClagDistributionMplsProtocol,'ClagAggregationProtocol':ClagAggregationProtocol,'ClagPortAdminStatus':ClagPortAdminStatus,'ciscoLagMIB':ciscoLagMIB,'clagMIBObjects':clagMIBObjects,'clagGlobalConfigObjects':clagGlobalConfigObjects,_b:clagAggDistributionProtocol,_c:clagAggDistributionAddressMode,_d:clagAggDistributionMplsProtocol,_f:clagAggMaxAggregators,_l:clagAggHashDistMethodGlobalConfig,'clagAgg':clagAgg,'clagAggProtocolTable':clagAggProtocolTable,'clagAggProtocolEntry':clagAggProtocolEntry,_Z:clagAggProtocolType,'clagAggPort':clagAggPort,'clagAggPortTable':clagAggPortTable,_X:clagAggPortEntry,_a:clagAggPortAdminStatus,_g:clagAggPortRate,'clagAggPortList':clagAggPortList,'clagAggPortListTable':clagAggPortListTable,_Y:clagAggPortListEntry,_e:clagAggPortListPorts,_n:clagAggPortListInterfaceIndexList,'clagAggChannelIntf':clagAggChannelIntf,'clagAggChannelIfTable':clagAggChannelIfTable,'clagAggChannelIfEntry':clagAggChannelIfEntry,_h:clagAggChannelIfFastSwitchOver,_i:clagAggChannelIfMaxBundle,_m:clagAggChannelIfMinLink,_j:clagAggChannelIfHashDistAdminMethod,_k:clagAggChannelIfHashDistOperMethod,'clagMIBNotifications':clagMIBNotifications,'clagMIBConformance':clagMIBConformance,'clagMIBCompliances':clagMIBCompliances,'clagMIBCompliance':clagMIBCompliance,'clagMIBCompliance2':clagMIBCompliance2,'clagMIBCompliance3':clagMIBCompliance3,'clagMIBCompliance4':clagMIBCompliance4,'clagMIBCompliance5':clagMIBCompliance5,'clagMIBCompliance6':clagMIBCompliance6,'clagMIBGroups':clagMIBGroups,_D:clagAggProtocolGroup,_E:clagAggPortGroup,_F:clagAggDistributionGroup,_G:clagAggDistributionMplsGroup,_J:clagAggPortListGroup,_L:clagAggMaxAggregatorsGroup,_Q:clagAggRateGroup,_R:clagAggChannelIfLacpGroup,_S:clagAggChannelIfHashDistMethodGroup,_T:clagAggHashDistGlobalGroup,_U:clagAggChannelIfMinLinkGroup,_o:clagAggPortListInterfaceIndexGroup})