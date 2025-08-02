_n='qtechSnmpUdpPortMIBGroup'
_m='qtechSnmpTrapMIBGroup'
_l='qtechCommunityMIBGroup'
_k='qtechSNMPTrapPort'
_j='qtechSNMPGetSetPort'
_i='qtechSysNetID'
_h='qtechTrapDesStatus'
_g='qtechTrapDesVersion'
_f='qtechTrapDesCommunity'
_e='qtechTrapDesIPAddress'
_d='qtechTrapOnOff'
_c='qtechTrapDescr'
_b='qtechTrapAction'
_a='qtechTrapDstEntryStatus'
_Z='qtechTrapDstCommunity'
_Y='qtechTrapDstMaxNumber'
_X='qtechTrapDstSendTrapClass'
_W='qtechWriteCommunityName'
_V='qtechReadCommunityName'
_U='qtechCommunityStatus'
_T='qtechCommunityEnableIpAddrAuthen'
_S='qtechCommunityUserIpAddr'
_R='qtechCommunityWritable'
_Q='qtechCommunityMaxNum'
_P='snmpv3-trap'
_O='snmpv2c-Trap'
_N='snmpv1-Trap'
_M='Community'
_L='qtechTrapDesIndex'
_K='qtechTrapName'
_J='qtechTrapType'
_I='qtechTrapDstAddr'
_H='qtechCommunityName'
_G='DisplayString'
_F='read-write'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='QTECH-SNMP-AGENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
QtechTrapType,=mibBuilder.importSymbols('QTECH-TC','QtechTrapType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TAddress','TextualConvention')
qtechSnmpAgentMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,5))
if mibBuilder.loadTexts:qtechSnmpAgentMIB.setRevisions(('2002-03-20 00:00',))
class Community(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSnmpAgentMIBObjects_ObjectIdentity=ObjectIdentity
qtechSnmpAgentMIBObjects=_QtechSnmpAgentMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,1))
_QtechSnmpCommunityObjects_ObjectIdentity=ObjectIdentity
qtechSnmpCommunityObjects=_QtechSnmpCommunityObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,1,1))
_QtechCommunityMaxNum_Type=Integer32
_QtechCommunityMaxNum_Object=MibScalar
qtechCommunityMaxNum=_QtechCommunityMaxNum_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,1),_QtechCommunityMaxNum_Type())
qtechCommunityMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCommunityMaxNum.setStatus(_A)
_QtechCommunityTable_Object=MibTable
qtechCommunityTable=_QtechCommunityTable_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2))
if mibBuilder.loadTexts:qtechCommunityTable.setStatus(_A)
_QtechCommunityEntry_Object=MibTableRow
qtechCommunityEntry=_QtechCommunityEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2,1))
qtechCommunityEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechCommunityEntry.setStatus(_A)
_QtechCommunityName_Type=Community
_QtechCommunityName_Object=MibTableColumn
qtechCommunityName=_QtechCommunityName_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2,1,1),_QtechCommunityName_Type())
qtechCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCommunityName.setStatus(_A)
class _QtechCommunityWritable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readonly',1),('readwrite',2)))
_QtechCommunityWritable_Type.__name__=_E
_QtechCommunityWritable_Object=MibTableColumn
qtechCommunityWritable=_QtechCommunityWritable_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2,1,2),_QtechCommunityWritable_Type())
qtechCommunityWritable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCommunityWritable.setStatus(_A)
_QtechCommunityUserIpAddr_Type=IpAddress
_QtechCommunityUserIpAddr_Object=MibTableColumn
qtechCommunityUserIpAddr=_QtechCommunityUserIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2,1,3),_QtechCommunityUserIpAddr_Type())
qtechCommunityUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCommunityUserIpAddr.setStatus(_A)
_QtechCommunityEnableIpAddrAuthen_Type=EnabledStatus
_QtechCommunityEnableIpAddrAuthen_Object=MibTableColumn
qtechCommunityEnableIpAddrAuthen=_QtechCommunityEnableIpAddrAuthen_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2,1,4),_QtechCommunityEnableIpAddrAuthen_Type())
qtechCommunityEnableIpAddrAuthen.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCommunityEnableIpAddrAuthen.setStatus(_A)
_QtechCommunityStatus_Type=RowStatus
_QtechCommunityStatus_Object=MibTableColumn
qtechCommunityStatus=_QtechCommunityStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,2,1,5),_QtechCommunityStatus_Type())
qtechCommunityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCommunityStatus.setStatus(_A)
_QtechReadCommunityName_Type=DisplayString
_QtechReadCommunityName_Object=MibScalar
qtechReadCommunityName=_QtechReadCommunityName_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,3),_QtechReadCommunityName_Type())
qtechReadCommunityName.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechReadCommunityName.setStatus(_A)
_QtechWriteCommunityName_Type=DisplayString
_QtechWriteCommunityName_Object=MibScalar
qtechWriteCommunityName=_QtechWriteCommunityName_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,1,4),_QtechWriteCommunityName_Type())
qtechWriteCommunityName.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechWriteCommunityName.setStatus(_A)
_QtechSnmpTrapObjects_ObjectIdentity=ObjectIdentity
qtechSnmpTrapObjects=_QtechSnmpTrapObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,1,2))
_QtechTrapDstMaxNumber_Type=Integer32
_QtechTrapDstMaxNumber_Object=MibScalar
qtechTrapDstMaxNumber=_QtechTrapDstMaxNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,1),_QtechTrapDstMaxNumber_Type())
qtechTrapDstMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTrapDstMaxNumber.setStatus(_A)
_QtechTrapDstTable_Object=MibTable
qtechTrapDstTable=_QtechTrapDstTable_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,2))
if mibBuilder.loadTexts:qtechTrapDstTable.setStatus(_A)
_QtechTrapDstEntry_Object=MibTableRow
qtechTrapDstEntry=_QtechTrapDstEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,2,1))
qtechTrapDstEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechTrapDstEntry.setStatus(_A)
_QtechTrapDstAddr_Type=IpAddress
_QtechTrapDstAddr_Object=MibTableColumn
qtechTrapDstAddr=_QtechTrapDstAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,2,1,1),_QtechTrapDstAddr_Type())
qtechTrapDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTrapDstAddr.setStatus(_A)
class _QtechTrapDstCommunity_Type(Community):defaultValue=OctetString('public')
_QtechTrapDstCommunity_Type.__name__=_M
_QtechTrapDstCommunity_Object=MibTableColumn
qtechTrapDstCommunity=_QtechTrapDstCommunity_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,2,1,2),_QtechTrapDstCommunity_Type())
qtechTrapDstCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDstCommunity.setStatus(_A)
class _QtechTrapDstSendTrapClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_QtechTrapDstSendTrapClass_Type.__name__=_E
_QtechTrapDstSendTrapClass_Object=MibTableColumn
qtechTrapDstSendTrapClass=_QtechTrapDstSendTrapClass_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,2,1,3),_QtechTrapDstSendTrapClass_Type())
qtechTrapDstSendTrapClass.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDstSendTrapClass.setStatus(_A)
_QtechTrapDstEntryStatus_Type=RowStatus
_QtechTrapDstEntryStatus_Object=MibTableColumn
qtechTrapDstEntryStatus=_QtechTrapDstEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,2,1,4),_QtechTrapDstEntryStatus_Type())
qtechTrapDstEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDstEntryStatus.setStatus(_A)
_QtechTrapActionTable_Object=MibTable
qtechTrapActionTable=_QtechTrapActionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,3))
if mibBuilder.loadTexts:qtechTrapActionTable.setStatus(_A)
_QtechTrapActionEntry_Object=MibTableRow
qtechTrapActionEntry=_QtechTrapActionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,3,1))
qtechTrapActionEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechTrapActionEntry.setStatus(_A)
_QtechTrapType_Type=QtechTrapType
_QtechTrapType_Object=MibTableColumn
qtechTrapType=_QtechTrapType_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,3,1,1),_QtechTrapType_Type())
qtechTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTrapType.setStatus(_A)
class _QtechTrapAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('sendtrap',2)))
_QtechTrapAction_Type.__name__=_E
_QtechTrapAction_Object=MibTableColumn
qtechTrapAction=_QtechTrapAction_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,3,1,2),_QtechTrapAction_Type())
qtechTrapAction.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechTrapAction.setStatus(_A)
_QtechTrapControlTable_Object=MibTable
qtechTrapControlTable=_QtechTrapControlTable_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,4))
if mibBuilder.loadTexts:qtechTrapControlTable.setStatus(_A)
_QtechTrapControlEntry_Object=MibTableRow
qtechTrapControlEntry=_QtechTrapControlEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,4,1))
qtechTrapControlEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechTrapControlEntry.setStatus(_A)
class _QtechTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechTrapName_Type.__name__=_G
_QtechTrapName_Object=MibTableColumn
qtechTrapName=_QtechTrapName_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,4,1,1),_QtechTrapName_Type())
qtechTrapName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTrapName.setStatus(_A)
class _QtechTrapDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QtechTrapDescr_Type.__name__=_G
_QtechTrapDescr_Object=MibTableColumn
qtechTrapDescr=_QtechTrapDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,4,1,2),_QtechTrapDescr_Type())
qtechTrapDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechTrapDescr.setStatus(_A)
class _QtechTrapOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_QtechTrapOnOff_Type.__name__=_E
_QtechTrapOnOff_Object=MibTableColumn
qtechTrapOnOff=_QtechTrapOnOff_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,4,1,3),_QtechTrapOnOff_Type())
qtechTrapOnOff.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechTrapOnOff.setStatus(_A)
_QtechTrapDesTable_Object=MibTable
qtechTrapDesTable=_QtechTrapDesTable_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5))
if mibBuilder.loadTexts:qtechTrapDesTable.setStatus(_A)
_QtechTrapDesEntry_Object=MibTableRow
qtechTrapDesEntry=_QtechTrapDesEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5,1))
qtechTrapDesEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechTrapDesEntry.setStatus(_A)
_QtechTrapDesIndex_Type=Integer32
_QtechTrapDesIndex_Object=MibTableColumn
qtechTrapDesIndex=_QtechTrapDesIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5,1,1),_QtechTrapDesIndex_Type())
qtechTrapDesIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTrapDesIndex.setStatus(_A)
_QtechTrapDesIPAddress_Type=TAddress
_QtechTrapDesIPAddress_Object=MibTableColumn
qtechTrapDesIPAddress=_QtechTrapDesIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5,1,2),_QtechTrapDesIPAddress_Type())
qtechTrapDesIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDesIPAddress.setStatus(_A)
_QtechTrapDesCommunity_Type=Community
_QtechTrapDesCommunity_Object=MibTableColumn
qtechTrapDesCommunity=_QtechTrapDesCommunity_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5,1,3),_QtechTrapDesCommunity_Type())
qtechTrapDesCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDesCommunity.setStatus(_A)
class _QtechTrapDesVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_QtechTrapDesVersion_Type.__name__=_E
_QtechTrapDesVersion_Object=MibTableColumn
qtechTrapDesVersion=_QtechTrapDesVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5,1,4),_QtechTrapDesVersion_Type())
qtechTrapDesVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDesVersion.setStatus(_A)
_QtechTrapDesStatus_Type=RowStatus
_QtechTrapDesStatus_Object=MibTableColumn
qtechTrapDesStatus=_QtechTrapDesStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,2,5,1,5),_QtechTrapDesStatus_Type())
qtechTrapDesStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapDesStatus.setStatus(_A)
_QtechSnmpUdpPortObjects_ObjectIdentity=ObjectIdentity
qtechSnmpUdpPortObjects=_QtechSnmpUdpPortObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,1,3))
_QtechSNMPGetSetPort_Type=Integer32
_QtechSNMPGetSetPort_Object=MibScalar
qtechSNMPGetSetPort=_QtechSNMPGetSetPort_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,3,1),_QtechSNMPGetSetPort_Type())
qtechSNMPGetSetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNMPGetSetPort.setStatus(_A)
_QtechSNMPTrapPort_Type=Integer32
_QtechSNMPTrapPort_Object=MibScalar
qtechSNMPTrapPort=_QtechSNMPTrapPort_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,3,2),_QtechSNMPTrapPort_Type())
qtechSNMPTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNMPTrapPort.setStatus(_A)
_QtechSnmpNetObjects_ObjectIdentity=ObjectIdentity
qtechSnmpNetObjects=_QtechSnmpNetObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,1,4))
_QtechSysNetID_Type=DisplayString
_QtechSysNetID_Object=MibScalar
qtechSysNetID=_QtechSysNetID_Object((1,3,6,1,4,1,27514,1,1,10,2,5,1,4,1),_QtechSysNetID_Type())
qtechSysNetID.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechSysNetID.setStatus(_A)
_QtechSnmpAgentMIBConformance_ObjectIdentity=ObjectIdentity
qtechSnmpAgentMIBConformance=_QtechSnmpAgentMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,2))
_QtechSnmpAgentMIBCompliances_ObjectIdentity=ObjectIdentity
qtechSnmpAgentMIBCompliances=_QtechSnmpAgentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,2,1))
_QtechSnmpAgentMIBGroups_ObjectIdentity=ObjectIdentity
qtechSnmpAgentMIBGroups=_QtechSnmpAgentMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,5,2,2))
qtechCommunityMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,5,2,2,1))
qtechCommunityMIBGroup.setObjects(*((_B,_Q),(_B,_H),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:qtechCommunityMIBGroup.setStatus(_A)
qtechSnmpTrapMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,5,2,2,2))
qtechSnmpTrapMIBGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_I),(_B,_Z),(_B,_a),(_B,_J),(_B,_b),(_B,_K),(_B,_c),(_B,_d),(_B,_L),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:qtechSnmpTrapMIBGroup.setStatus(_A)
qtechSnmpUdpPortMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,5,2,2,3))
qtechSnmpUdpPortMIBGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:qtechSnmpUdpPortMIBGroup.setStatus(_A)
qtechSnmpAgentMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,5,2,1,1))
qtechSnmpAgentMIBCompliance.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:qtechSnmpAgentMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:Community,'qtechSnmpAgentMIB':qtechSnmpAgentMIB,'qtechSnmpAgentMIBObjects':qtechSnmpAgentMIBObjects,'qtechSnmpCommunityObjects':qtechSnmpCommunityObjects,_Q:qtechCommunityMaxNum,'qtechCommunityTable':qtechCommunityTable,'qtechCommunityEntry':qtechCommunityEntry,_H:qtechCommunityName,_R:qtechCommunityWritable,_S:qtechCommunityUserIpAddr,_T:qtechCommunityEnableIpAddrAuthen,_U:qtechCommunityStatus,_V:qtechReadCommunityName,_W:qtechWriteCommunityName,'qtechSnmpTrapObjects':qtechSnmpTrapObjects,_Y:qtechTrapDstMaxNumber,'qtechTrapDstTable':qtechTrapDstTable,'qtechTrapDstEntry':qtechTrapDstEntry,_I:qtechTrapDstAddr,_Z:qtechTrapDstCommunity,_X:qtechTrapDstSendTrapClass,_a:qtechTrapDstEntryStatus,'qtechTrapActionTable':qtechTrapActionTable,'qtechTrapActionEntry':qtechTrapActionEntry,_J:qtechTrapType,_b:qtechTrapAction,'qtechTrapControlTable':qtechTrapControlTable,'qtechTrapControlEntry':qtechTrapControlEntry,_K:qtechTrapName,_c:qtechTrapDescr,_d:qtechTrapOnOff,'qtechTrapDesTable':qtechTrapDesTable,'qtechTrapDesEntry':qtechTrapDesEntry,_L:qtechTrapDesIndex,_e:qtechTrapDesIPAddress,_f:qtechTrapDesCommunity,_g:qtechTrapDesVersion,_h:qtechTrapDesStatus,'qtechSnmpUdpPortObjects':qtechSnmpUdpPortObjects,_j:qtechSNMPGetSetPort,_k:qtechSNMPTrapPort,'qtechSnmpNetObjects':qtechSnmpNetObjects,_i:qtechSysNetID,'qtechSnmpAgentMIBConformance':qtechSnmpAgentMIBConformance,'qtechSnmpAgentMIBCompliances':qtechSnmpAgentMIBCompliances,'qtechSnmpAgentMIBCompliance':qtechSnmpAgentMIBCompliance,'qtechSnmpAgentMIBGroups':qtechSnmpAgentMIBGroups,_l:qtechCommunityMIBGroup,_m:qtechSnmpTrapMIBGroup,_n:qtechSnmpUdpPortMIBGroup})