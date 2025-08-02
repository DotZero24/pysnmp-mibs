_n='fsSnmpUdpPortMIBGroup'
_m='fsSnmpTrapMIBGroup'
_l='fsCommunityMIBGroup'
_k='fsSNMPTrapPort'
_j='fsSNMPGetSetPort'
_i='fsSysNetID'
_h='fsTrapDesStatus'
_g='fsTrapDesVersion'
_f='fsTrapDesCommunity'
_e='fsTrapDesIPAddress'
_d='fsTrapOnOff'
_c='fsTrapDescr'
_b='fsTrapAction'
_a='fsTrapDstEntryStatus'
_Z='fsTrapDstCommunity'
_Y='fsTrapDstMaxNumber'
_X='fsTrapDstSendTrapClass'
_W='fsWriteCommunityName'
_V='fsReadCommunityName'
_U='fsCommunityStatus'
_T='fsCommunityEnableIpAddrAuthen'
_S='fsCommunityUserIpAddr'
_R='fsCommunityWritable'
_Q='fsCommunityMaxNum'
_P='snmpv3-trap'
_O='snmpv2c-Trap'
_N='snmpv1-Trap'
_M='Community'
_L='fsTrapDesIndex'
_K='fsTrapName'
_J='fsTrapType'
_I='fsTrapDstAddr'
_H='fsCommunityName'
_G='DisplayString'
_F='read-write'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='FS-SNMP-AGENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
FSTrapType,=mibBuilder.importSymbols('FS-TC','FSTrapType')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TAddress','TextualConvention')
fsSnmpAgentMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,5))
if mibBuilder.loadTexts:fsSnmpAgentMIB.setRevisions(('2002-03-20 00:00',))
class Community(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsSnmpAgentMIBObjects_ObjectIdentity=ObjectIdentity
fsSnmpAgentMIBObjects=_FsSnmpAgentMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,1))
_FsSnmpCommunityObjects_ObjectIdentity=ObjectIdentity
fsSnmpCommunityObjects=_FsSnmpCommunityObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,1,1))
_FsCommunityMaxNum_Type=Integer32
_FsCommunityMaxNum_Object=MibScalar
fsCommunityMaxNum=_FsCommunityMaxNum_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,1),_FsCommunityMaxNum_Type())
fsCommunityMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCommunityMaxNum.setStatus(_A)
_FsCommunityTable_Object=MibTable
fsCommunityTable=_FsCommunityTable_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2))
if mibBuilder.loadTexts:fsCommunityTable.setStatus(_A)
_FsCommunityEntry_Object=MibTableRow
fsCommunityEntry=_FsCommunityEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2,1))
fsCommunityEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsCommunityEntry.setStatus(_A)
_FsCommunityName_Type=Community
_FsCommunityName_Object=MibTableColumn
fsCommunityName=_FsCommunityName_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2,1,1),_FsCommunityName_Type())
fsCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCommunityName.setStatus(_A)
class _FsCommunityWritable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readonly',1),('readwrite',2)))
_FsCommunityWritable_Type.__name__=_E
_FsCommunityWritable_Object=MibTableColumn
fsCommunityWritable=_FsCommunityWritable_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2,1,2),_FsCommunityWritable_Type())
fsCommunityWritable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCommunityWritable.setStatus(_A)
_FsCommunityUserIpAddr_Type=IpAddress
_FsCommunityUserIpAddr_Object=MibTableColumn
fsCommunityUserIpAddr=_FsCommunityUserIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2,1,3),_FsCommunityUserIpAddr_Type())
fsCommunityUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCommunityUserIpAddr.setStatus(_A)
_FsCommunityEnableIpAddrAuthen_Type=EnabledStatus
_FsCommunityEnableIpAddrAuthen_Object=MibTableColumn
fsCommunityEnableIpAddrAuthen=_FsCommunityEnableIpAddrAuthen_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2,1,4),_FsCommunityEnableIpAddrAuthen_Type())
fsCommunityEnableIpAddrAuthen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCommunityEnableIpAddrAuthen.setStatus(_A)
_FsCommunityStatus_Type=RowStatus
_FsCommunityStatus_Object=MibTableColumn
fsCommunityStatus=_FsCommunityStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,2,1,5),_FsCommunityStatus_Type())
fsCommunityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCommunityStatus.setStatus(_A)
_FsReadCommunityName_Type=DisplayString
_FsReadCommunityName_Object=MibScalar
fsReadCommunityName=_FsReadCommunityName_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,3),_FsReadCommunityName_Type())
fsReadCommunityName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsReadCommunityName.setStatus(_A)
_FsWriteCommunityName_Type=DisplayString
_FsWriteCommunityName_Object=MibScalar
fsWriteCommunityName=_FsWriteCommunityName_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,1,4),_FsWriteCommunityName_Type())
fsWriteCommunityName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWriteCommunityName.setStatus(_A)
_FsSnmpTrapObjects_ObjectIdentity=ObjectIdentity
fsSnmpTrapObjects=_FsSnmpTrapObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,1,2))
_FsTrapDstMaxNumber_Type=Integer32
_FsTrapDstMaxNumber_Object=MibScalar
fsTrapDstMaxNumber=_FsTrapDstMaxNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,1),_FsTrapDstMaxNumber_Type())
fsTrapDstMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTrapDstMaxNumber.setStatus(_A)
_FsTrapDstTable_Object=MibTable
fsTrapDstTable=_FsTrapDstTable_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,2))
if mibBuilder.loadTexts:fsTrapDstTable.setStatus(_A)
_FsTrapDstEntry_Object=MibTableRow
fsTrapDstEntry=_FsTrapDstEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,2,1))
fsTrapDstEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsTrapDstEntry.setStatus(_A)
_FsTrapDstAddr_Type=IpAddress
_FsTrapDstAddr_Object=MibTableColumn
fsTrapDstAddr=_FsTrapDstAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,2,1,1),_FsTrapDstAddr_Type())
fsTrapDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTrapDstAddr.setStatus(_A)
class _FsTrapDstCommunity_Type(Community):defaultValue=OctetString('public')
_FsTrapDstCommunity_Type.__name__=_M
_FsTrapDstCommunity_Object=MibTableColumn
fsTrapDstCommunity=_FsTrapDstCommunity_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,2,1,2),_FsTrapDstCommunity_Type())
fsTrapDstCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDstCommunity.setStatus(_A)
class _FsTrapDstSendTrapClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_FsTrapDstSendTrapClass_Type.__name__=_E
_FsTrapDstSendTrapClass_Object=MibTableColumn
fsTrapDstSendTrapClass=_FsTrapDstSendTrapClass_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,2,1,3),_FsTrapDstSendTrapClass_Type())
fsTrapDstSendTrapClass.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDstSendTrapClass.setStatus(_A)
_FsTrapDstEntryStatus_Type=RowStatus
_FsTrapDstEntryStatus_Object=MibTableColumn
fsTrapDstEntryStatus=_FsTrapDstEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,2,1,4),_FsTrapDstEntryStatus_Type())
fsTrapDstEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDstEntryStatus.setStatus(_A)
_FsTrapActionTable_Object=MibTable
fsTrapActionTable=_FsTrapActionTable_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,3))
if mibBuilder.loadTexts:fsTrapActionTable.setStatus(_A)
_FsTrapActionEntry_Object=MibTableRow
fsTrapActionEntry=_FsTrapActionEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,3,1))
fsTrapActionEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsTrapActionEntry.setStatus(_A)
_FsTrapType_Type=FSTrapType
_FsTrapType_Object=MibTableColumn
fsTrapType=_FsTrapType_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,3,1,1),_FsTrapType_Type())
fsTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTrapType.setStatus(_A)
class _FsTrapAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('sendtrap',2)))
_FsTrapAction_Type.__name__=_E
_FsTrapAction_Object=MibTableColumn
fsTrapAction=_FsTrapAction_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,3,1,2),_FsTrapAction_Type())
fsTrapAction.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTrapAction.setStatus(_A)
_FsTrapControlTable_Object=MibTable
fsTrapControlTable=_FsTrapControlTable_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,4))
if mibBuilder.loadTexts:fsTrapControlTable.setStatus(_A)
_FsTrapControlEntry_Object=MibTableRow
fsTrapControlEntry=_FsTrapControlEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,4,1))
fsTrapControlEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsTrapControlEntry.setStatus(_A)
class _FsTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsTrapName_Type.__name__=_G
_FsTrapName_Object=MibTableColumn
fsTrapName=_FsTrapName_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,4,1,1),_FsTrapName_Type())
fsTrapName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTrapName.setStatus(_A)
class _FsTrapDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsTrapDescr_Type.__name__=_G
_FsTrapDescr_Object=MibTableColumn
fsTrapDescr=_FsTrapDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,4,1,2),_FsTrapDescr_Type())
fsTrapDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTrapDescr.setStatus(_A)
class _FsTrapOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_FsTrapOnOff_Type.__name__=_E
_FsTrapOnOff_Object=MibTableColumn
fsTrapOnOff=_FsTrapOnOff_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,4,1,3),_FsTrapOnOff_Type())
fsTrapOnOff.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTrapOnOff.setStatus(_A)
_FsTrapDesTable_Object=MibTable
fsTrapDesTable=_FsTrapDesTable_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5))
if mibBuilder.loadTexts:fsTrapDesTable.setStatus(_A)
_FsTrapDesEntry_Object=MibTableRow
fsTrapDesEntry=_FsTrapDesEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5,1))
fsTrapDesEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsTrapDesEntry.setStatus(_A)
_FsTrapDesIndex_Type=Integer32
_FsTrapDesIndex_Object=MibTableColumn
fsTrapDesIndex=_FsTrapDesIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5,1,1),_FsTrapDesIndex_Type())
fsTrapDesIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTrapDesIndex.setStatus(_A)
_FsTrapDesIPAddress_Type=TAddress
_FsTrapDesIPAddress_Object=MibTableColumn
fsTrapDesIPAddress=_FsTrapDesIPAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5,1,2),_FsTrapDesIPAddress_Type())
fsTrapDesIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDesIPAddress.setStatus(_A)
_FsTrapDesCommunity_Type=Community
_FsTrapDesCommunity_Object=MibTableColumn
fsTrapDesCommunity=_FsTrapDesCommunity_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5,1,3),_FsTrapDesCommunity_Type())
fsTrapDesCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDesCommunity.setStatus(_A)
class _FsTrapDesVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_FsTrapDesVersion_Type.__name__=_E
_FsTrapDesVersion_Object=MibTableColumn
fsTrapDesVersion=_FsTrapDesVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5,1,4),_FsTrapDesVersion_Type())
fsTrapDesVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDesVersion.setStatus(_A)
_FsTrapDesStatus_Type=RowStatus
_FsTrapDesStatus_Object=MibTableColumn
fsTrapDesStatus=_FsTrapDesStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,2,5,1,5),_FsTrapDesStatus_Type())
fsTrapDesStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapDesStatus.setStatus(_A)
_FsSnmpUdpPortObjects_ObjectIdentity=ObjectIdentity
fsSnmpUdpPortObjects=_FsSnmpUdpPortObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,1,3))
_FsSNMPGetSetPort_Type=Integer32
_FsSNMPGetSetPort_Object=MibScalar
fsSNMPGetSetPort=_FsSNMPGetSetPort_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,3,1),_FsSNMPGetSetPort_Type())
fsSNMPGetSetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNMPGetSetPort.setStatus(_A)
_FsSNMPTrapPort_Type=Integer32
_FsSNMPTrapPort_Object=MibScalar
fsSNMPTrapPort=_FsSNMPTrapPort_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,3,2),_FsSNMPTrapPort_Type())
fsSNMPTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNMPTrapPort.setStatus(_A)
_FsSnmpNetObjects_ObjectIdentity=ObjectIdentity
fsSnmpNetObjects=_FsSnmpNetObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,1,4))
_FsSysNetID_Type=DisplayString
_FsSysNetID_Object=MibScalar
fsSysNetID=_FsSysNetID_Object((1,3,6,1,4,1,52642,1,1,10,2,5,1,4,1),_FsSysNetID_Type())
fsSysNetID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSysNetID.setStatus(_A)
_FsSnmpAgentMIBConformance_ObjectIdentity=ObjectIdentity
fsSnmpAgentMIBConformance=_FsSnmpAgentMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,2))
_FsSnmpAgentMIBCompliances_ObjectIdentity=ObjectIdentity
fsSnmpAgentMIBCompliances=_FsSnmpAgentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,2,1))
_FsSnmpAgentMIBGroups_ObjectIdentity=ObjectIdentity
fsSnmpAgentMIBGroups=_FsSnmpAgentMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,5,2,2))
fsCommunityMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,5,2,2,1))
fsCommunityMIBGroup.setObjects(*((_B,_Q),(_B,_H),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:fsCommunityMIBGroup.setStatus(_A)
fsSnmpTrapMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,5,2,2,2))
fsSnmpTrapMIBGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_I),(_B,_Z),(_B,_a),(_B,_J),(_B,_b),(_B,_K),(_B,_c),(_B,_d),(_B,_L),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:fsSnmpTrapMIBGroup.setStatus(_A)
fsSnmpUdpPortMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,5,2,2,3))
fsSnmpUdpPortMIBGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:fsSnmpUdpPortMIBGroup.setStatus(_A)
fsSnmpAgentMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,5,2,1,1))
fsSnmpAgentMIBCompliance.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:fsSnmpAgentMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:Community,'fsSnmpAgentMIB':fsSnmpAgentMIB,'fsSnmpAgentMIBObjects':fsSnmpAgentMIBObjects,'fsSnmpCommunityObjects':fsSnmpCommunityObjects,_Q:fsCommunityMaxNum,'fsCommunityTable':fsCommunityTable,'fsCommunityEntry':fsCommunityEntry,_H:fsCommunityName,_R:fsCommunityWritable,_S:fsCommunityUserIpAddr,_T:fsCommunityEnableIpAddrAuthen,_U:fsCommunityStatus,_V:fsReadCommunityName,_W:fsWriteCommunityName,'fsSnmpTrapObjects':fsSnmpTrapObjects,_Y:fsTrapDstMaxNumber,'fsTrapDstTable':fsTrapDstTable,'fsTrapDstEntry':fsTrapDstEntry,_I:fsTrapDstAddr,_Z:fsTrapDstCommunity,_X:fsTrapDstSendTrapClass,_a:fsTrapDstEntryStatus,'fsTrapActionTable':fsTrapActionTable,'fsTrapActionEntry':fsTrapActionEntry,_J:fsTrapType,_b:fsTrapAction,'fsTrapControlTable':fsTrapControlTable,'fsTrapControlEntry':fsTrapControlEntry,_K:fsTrapName,_c:fsTrapDescr,_d:fsTrapOnOff,'fsTrapDesTable':fsTrapDesTable,'fsTrapDesEntry':fsTrapDesEntry,_L:fsTrapDesIndex,_e:fsTrapDesIPAddress,_f:fsTrapDesCommunity,_g:fsTrapDesVersion,_h:fsTrapDesStatus,'fsSnmpUdpPortObjects':fsSnmpUdpPortObjects,_j:fsSNMPGetSetPort,_k:fsSNMPTrapPort,'fsSnmpNetObjects':fsSnmpNetObjects,_i:fsSysNetID,'fsSnmpAgentMIBConformance':fsSnmpAgentMIBConformance,'fsSnmpAgentMIBCompliances':fsSnmpAgentMIBCompliances,'fsSnmpAgentMIBCompliance':fsSnmpAgentMIBCompliance,'fsSnmpAgentMIBGroups':fsSnmpAgentMIBGroups,_l:fsCommunityMIBGroup,_m:fsSnmpTrapMIBGroup,_n:fsSnmpUdpPortMIBGroup})