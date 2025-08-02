_e='fsAddressNotificationMIBGroup'
_d='fsMacAddressMIBGroup'
_c='fsIfMacAddrRemovedEnable'
_b='fsIfMacAddrLearntEnable'
_a='fsMacNotiHisTimestamp'
_Z='fsMacNotiHisTableCurrentLength'
_Y='fsMacNotiHisTableMaxLength'
_X='fsMacNotificationInterval'
_W='fsMacNotiGlobalEnabled'
_V='fsMacAddressStatus'
_U='fsMacAddressType'
_T='fsMacAddressPort'
_S='fsAddressAvailableNum'
_R='fsFilterAddressCurrentNum'
_Q='fsStaticAddressCurrentNum'
_P='fsDynamicAddressCurrentNum'
_O='fsMacIfLearnIfIndex'
_N='Integer32'
_M='OctetString'
_L='fsMacNotiHisMacChangedMsg'
_K='fsMacNotiIfIndex'
_J='fsMacNotiHisIndex'
_I='read-create'
_H='fsMacAddress'
_G='fsMacAddressFdbId'
_F='Unsigned32'
_E='EnabledStatus'
_D='read-write'
_C='read-only'
_B='FS-ADDRESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp')
fsAddressMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,22))
if mibBuilder.loadTexts:fsAddressMIB.setRevisions(('2002-03-20 00:00',))
_FsAddressMIBObjects_ObjectIdentity=ObjectIdentity
fsAddressMIBObjects=_FsAddressMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,1))
_FsAddressManagementObjects_ObjectIdentity=ObjectIdentity
fsAddressManagementObjects=_FsAddressManagementObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,1,1))
_FsDynamicAddressCurrentNum_Type=Integer32
_FsDynamicAddressCurrentNum_Object=MibScalar
fsDynamicAddressCurrentNum=_FsDynamicAddressCurrentNum_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,1),_FsDynamicAddressCurrentNum_Type())
fsDynamicAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDynamicAddressCurrentNum.setStatus(_A)
_FsStaticAddressCurrentNum_Type=Integer32
_FsStaticAddressCurrentNum_Object=MibScalar
fsStaticAddressCurrentNum=_FsStaticAddressCurrentNum_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,2),_FsStaticAddressCurrentNum_Type())
fsStaticAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaticAddressCurrentNum.setStatus(_A)
_FsFilterAddressCurrentNum_Type=Integer32
_FsFilterAddressCurrentNum_Object=MibScalar
fsFilterAddressCurrentNum=_FsFilterAddressCurrentNum_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,3),_FsFilterAddressCurrentNum_Type())
fsFilterAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFilterAddressCurrentNum.setStatus(_A)
_FsAddressAvailableNum_Type=Integer32
_FsAddressAvailableNum_Object=MibScalar
fsAddressAvailableNum=_FsAddressAvailableNum_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,4),_FsAddressAvailableNum_Type())
fsAddressAvailableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAddressAvailableNum.setStatus(_A)
_FsMacAddressTable_Object=MibTable
fsMacAddressTable=_FsMacAddressTable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5))
if mibBuilder.loadTexts:fsMacAddressTable.setStatus(_A)
_FsMacAddressEntry_Object=MibTableRow
fsMacAddressEntry=_FsMacAddressEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5,1))
fsMacAddressEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:fsMacAddressEntry.setStatus(_A)
_FsMacAddressFdbId_Type=Unsigned32
_FsMacAddressFdbId_Object=MibTableColumn
fsMacAddressFdbId=_FsMacAddressFdbId_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5,1,1),_FsMacAddressFdbId_Type())
fsMacAddressFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacAddressFdbId.setStatus(_A)
_FsMacAddress_Type=MacAddress
_FsMacAddress_Object=MibTableColumn
fsMacAddress=_FsMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5,1,2),_FsMacAddress_Type())
fsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacAddress.setStatus(_A)
_FsMacAddressPort_Type=IfIndex
_FsMacAddressPort_Object=MibTableColumn
fsMacAddressPort=_FsMacAddressPort_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5,1,3),_FsMacAddressPort_Type())
fsMacAddressPort.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMacAddressPort.setStatus(_A)
class _FsMacAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('static',2),('filter',3)))
_FsMacAddressType_Type.__name__=_N
_FsMacAddressType_Object=MibTableColumn
fsMacAddressType=_FsMacAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5,1,4),_FsMacAddressType_Type())
fsMacAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMacAddressType.setStatus(_A)
_FsMacAddressStatus_Type=RowStatus
_FsMacAddressStatus_Object=MibTableColumn
fsMacAddressStatus=_FsMacAddressStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,1,5,1,5),_FsMacAddressStatus_Type())
fsMacAddressStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMacAddressStatus.setStatus(_A)
_FsAddressNotificationObjects_ObjectIdentity=ObjectIdentity
fsAddressNotificationObjects=_FsAddressNotificationObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,1,2))
_FsMacNotiGlobalEnabled_Type=EnabledStatus
_FsMacNotiGlobalEnabled_Object=MibScalar
fsMacNotiGlobalEnabled=_FsMacNotiGlobalEnabled_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,1),_FsMacNotiGlobalEnabled_Type())
fsMacNotiGlobalEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMacNotiGlobalEnabled.setStatus(_A)
class _FsMacNotificationInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FsMacNotificationInterval_Type.__name__=_F
_FsMacNotificationInterval_Object=MibScalar
fsMacNotificationInterval=_FsMacNotificationInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,2),_FsMacNotificationInterval_Type())
fsMacNotificationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMacNotificationInterval.setStatus(_A)
class _FsMacNotiHisTableMaxLength_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_FsMacNotiHisTableMaxLength_Type.__name__=_F
_FsMacNotiHisTableMaxLength_Object=MibScalar
fsMacNotiHisTableMaxLength=_FsMacNotiHisTableMaxLength_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,3),_FsMacNotiHisTableMaxLength_Type())
fsMacNotiHisTableMaxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMacNotiHisTableMaxLength.setStatus(_A)
_FsMacNotiHisTableCurrentLength_Type=Unsigned32
_FsMacNotiHisTableCurrentLength_Object=MibScalar
fsMacNotiHisTableCurrentLength=_FsMacNotiHisTableCurrentLength_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,4),_FsMacNotiHisTableCurrentLength_Type())
fsMacNotiHisTableCurrentLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacNotiHisTableCurrentLength.setStatus(_A)
_FsMacNotiHisTable_Object=MibTable
fsMacNotiHisTable=_FsMacNotiHisTable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,5))
if mibBuilder.loadTexts:fsMacNotiHisTable.setStatus(_A)
_FsMacNotiHisEntry_Object=MibTableRow
fsMacNotiHisEntry=_FsMacNotiHisEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,5,1))
fsMacNotiHisEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsMacNotiHisEntry.setStatus(_A)
class _FsMacNotiHisIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsMacNotiHisIndex_Type.__name__=_F
_FsMacNotiHisIndex_Object=MibTableColumn
fsMacNotiHisIndex=_FsMacNotiHisIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,5,1,1),_FsMacNotiHisIndex_Type())
fsMacNotiHisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacNotiHisIndex.setStatus(_A)
class _FsMacNotiHisMacChangedMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_FsMacNotiHisMacChangedMsg_Type.__name__=_M
_FsMacNotiHisMacChangedMsg_Object=MibTableColumn
fsMacNotiHisMacChangedMsg=_FsMacNotiHisMacChangedMsg_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,5,1,2),_FsMacNotiHisMacChangedMsg_Type())
fsMacNotiHisMacChangedMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacNotiHisMacChangedMsg.setStatus(_A)
_FsMacNotiHisTimestamp_Type=TimeStamp
_FsMacNotiHisTimestamp_Object=MibTableColumn
fsMacNotiHisTimestamp=_FsMacNotiHisTimestamp_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,5,1,3),_FsMacNotiHisTimestamp_Type())
fsMacNotiHisTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacNotiHisTimestamp.setStatus(_A)
_FsMacNotiIfCfgTable_Object=MibTable
fsMacNotiIfCfgTable=_FsMacNotiIfCfgTable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,6))
if mibBuilder.loadTexts:fsMacNotiIfCfgTable.setStatus(_A)
_FsMacNotiIfCfgEntry_Object=MibTableRow
fsMacNotiIfCfgEntry=_FsMacNotiIfCfgEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,6,1))
fsMacNotiIfCfgEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsMacNotiIfCfgEntry.setStatus(_A)
_FsMacNotiIfIndex_Type=IfIndex
_FsMacNotiIfIndex_Object=MibTableColumn
fsMacNotiIfIndex=_FsMacNotiIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,6,1,1),_FsMacNotiIfIndex_Type())
fsMacNotiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacNotiIfIndex.setStatus(_A)
class _FsIfMacAddrLearntEnable_Type(EnabledStatus):defaultValue=2
_FsIfMacAddrLearntEnable_Type.__name__=_E
_FsIfMacAddrLearntEnable_Object=MibTableColumn
fsIfMacAddrLearntEnable=_FsIfMacAddrLearntEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,6,1,2),_FsIfMacAddrLearntEnable_Type())
fsIfMacAddrLearntEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfMacAddrLearntEnable.setStatus(_A)
class _FsIfMacAddrRemovedEnable_Type(EnabledStatus):defaultValue=2
_FsIfMacAddrRemovedEnable_Type.__name__=_E
_FsIfMacAddrRemovedEnable_Object=MibTableColumn
fsIfMacAddrRemovedEnable=_FsIfMacAddrRemovedEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,6,1,3),_FsIfMacAddrRemovedEnable_Type())
fsIfMacAddrRemovedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfMacAddrRemovedEnable.setStatus(_A)
_FsMacIfLearnTable_Object=MibTable
fsMacIfLearnTable=_FsMacIfLearnTable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,7))
if mibBuilder.loadTexts:fsMacIfLearnTable.setStatus(_A)
_FsMacIfLearnEntry_Object=MibTableRow
fsMacIfLearnEntry=_FsMacIfLearnEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,7,1))
fsMacIfLearnEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:fsMacIfLearnEntry.setStatus(_A)
_FsMacIfLearnIfIndex_Type=IfIndex
_FsMacIfLearnIfIndex_Object=MibTableColumn
fsMacIfLearnIfIndex=_FsMacIfLearnIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,7,1,1),_FsMacIfLearnIfIndex_Type())
fsMacIfLearnIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMacIfLearnIfIndex.setStatus(_A)
class _FsMacIfLearnEnable_Type(EnabledStatus):defaultValue=1
_FsMacIfLearnEnable_Type.__name__=_E
_FsMacIfLearnEnable_Object=MibTableColumn
fsMacIfLearnEnable=_FsMacIfLearnEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,7,1,2),_FsMacIfLearnEnable_Type())
fsMacIfLearnEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMacIfLearnEnable.setStatus(_A)
class _FsMacGlobalLearnEnabled_Type(EnabledStatus):defaultValue=1
_FsMacGlobalLearnEnabled_Type.__name__=_E
_FsMacGlobalLearnEnabled_Object=MibScalar
fsMacGlobalLearnEnabled=_FsMacGlobalLearnEnabled_Object((1,3,6,1,4,1,52642,1,1,10,2,22,1,2,8),_FsMacGlobalLearnEnabled_Type())
fsMacGlobalLearnEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMacGlobalLearnEnabled.setStatus(_A)
_FsAddressTraps_ObjectIdentity=ObjectIdentity
fsAddressTraps=_FsAddressTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,2))
_FsAddressMIBConformance_ObjectIdentity=ObjectIdentity
fsAddressMIBConformance=_FsAddressMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,3))
_FsAddressMIBCompliances_ObjectIdentity=ObjectIdentity
fsAddressMIBCompliances=_FsAddressMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,3,1))
_FsAddressMIBGroups_ObjectIdentity=ObjectIdentity
fsAddressMIBGroups=_FsAddressMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,22,3,2))
fsMacAddressMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,22,3,2,1))
fsMacAddressMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_G),(_B,_H),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsMacAddressMIBGroup.setStatus(_A)
fsAddressNotificationMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,22,3,2,2))
fsAddressNotificationMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_J),(_B,_L),(_B,_a),(_B,_K),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:fsAddressNotificationMIBGroup.setStatus(_A)
macChangedNotification=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,22,2,1))
macChangedNotification.setObjects((_B,_L))
if mibBuilder.loadTexts:macChangedNotification.setStatus(_A)
fsAddressMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,22,3,1,1))
fsAddressMIBCompliance.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:fsAddressMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsAddressMIB':fsAddressMIB,'fsAddressMIBObjects':fsAddressMIBObjects,'fsAddressManagementObjects':fsAddressManagementObjects,_P:fsDynamicAddressCurrentNum,_Q:fsStaticAddressCurrentNum,_R:fsFilterAddressCurrentNum,_S:fsAddressAvailableNum,'fsMacAddressTable':fsMacAddressTable,'fsMacAddressEntry':fsMacAddressEntry,_G:fsMacAddressFdbId,_H:fsMacAddress,_T:fsMacAddressPort,_U:fsMacAddressType,_V:fsMacAddressStatus,'fsAddressNotificationObjects':fsAddressNotificationObjects,_W:fsMacNotiGlobalEnabled,_X:fsMacNotificationInterval,_Y:fsMacNotiHisTableMaxLength,_Z:fsMacNotiHisTableCurrentLength,'fsMacNotiHisTable':fsMacNotiHisTable,'fsMacNotiHisEntry':fsMacNotiHisEntry,_J:fsMacNotiHisIndex,_L:fsMacNotiHisMacChangedMsg,_a:fsMacNotiHisTimestamp,'fsMacNotiIfCfgTable':fsMacNotiIfCfgTable,'fsMacNotiIfCfgEntry':fsMacNotiIfCfgEntry,_K:fsMacNotiIfIndex,_b:fsIfMacAddrLearntEnable,_c:fsIfMacAddrRemovedEnable,'fsMacIfLearnTable':fsMacIfLearnTable,'fsMacIfLearnEntry':fsMacIfLearnEntry,_O:fsMacIfLearnIfIndex,'fsMacIfLearnEnable':fsMacIfLearnEnable,'fsMacGlobalLearnEnabled':fsMacGlobalLearnEnabled,'fsAddressTraps':fsAddressTraps,'macChangedNotification':macChangedNotification,'fsAddressMIBConformance':fsAddressMIBConformance,'fsAddressMIBCompliances':fsAddressMIBCompliances,'fsAddressMIBCompliance':fsAddressMIBCompliance,'fsAddressMIBGroups':fsAddressMIBGroups,_d:fsMacAddressMIBGroup,_e:fsAddressNotificationMIBGroup})