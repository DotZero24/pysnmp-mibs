_e='qtechAddressNotificationMIBGroup'
_d='qtechMacAddressMIBGroup'
_c='qtechIfMacAddrRemovedEnable'
_b='qtechIfMacAddrLearntEnable'
_a='qtechMacNotiHisTimestamp'
_Z='qtechMacNotiHisTableCurrentLength'
_Y='qtechMacNotiHisTableMaxLength'
_X='qtechMacNotificationInterval'
_W='qtechMacNotiGlobalEnabled'
_V='qtechMacAddressStatus'
_U='qtechMacAddressType'
_T='qtechMacAddressPort'
_S='qtechAddressAvailableNum'
_R='qtechFilterAddressCurrentNum'
_Q='qtechStaticAddressCurrentNum'
_P='qtechDynamicAddressCurrentNum'
_O='qtechMacIfLearnIfIndex'
_N='Integer32'
_M='OctetString'
_L='qtechMacNotiHisMacChangedMsg'
_K='qtechMacNotiIfIndex'
_J='qtechMacNotiHisIndex'
_I='read-create'
_H='qtechMacAddress'
_G='qtechMacAddressFdbId'
_F='Unsigned32'
_E='EnabledStatus'
_D='read-write'
_C='read-only'
_B='QTECH-ADDRESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp')
qtechAddressMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,22))
if mibBuilder.loadTexts:qtechAddressMIB.setRevisions(('2002-03-20 00:00',))
_QtechAddressMIBObjects_ObjectIdentity=ObjectIdentity
qtechAddressMIBObjects=_QtechAddressMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,1))
_QtechAddressManagementObjects_ObjectIdentity=ObjectIdentity
qtechAddressManagementObjects=_QtechAddressManagementObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,1,1))
_QtechDynamicAddressCurrentNum_Type=Integer32
_QtechDynamicAddressCurrentNum_Object=MibScalar
qtechDynamicAddressCurrentNum=_QtechDynamicAddressCurrentNum_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,1),_QtechDynamicAddressCurrentNum_Type())
qtechDynamicAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDynamicAddressCurrentNum.setStatus(_A)
_QtechStaticAddressCurrentNum_Type=Integer32
_QtechStaticAddressCurrentNum_Object=MibScalar
qtechStaticAddressCurrentNum=_QtechStaticAddressCurrentNum_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,2),_QtechStaticAddressCurrentNum_Type())
qtechStaticAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaticAddressCurrentNum.setStatus(_A)
_QtechFilterAddressCurrentNum_Type=Integer32
_QtechFilterAddressCurrentNum_Object=MibScalar
qtechFilterAddressCurrentNum=_QtechFilterAddressCurrentNum_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,3),_QtechFilterAddressCurrentNum_Type())
qtechFilterAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFilterAddressCurrentNum.setStatus(_A)
_QtechAddressAvailableNum_Type=Integer32
_QtechAddressAvailableNum_Object=MibScalar
qtechAddressAvailableNum=_QtechAddressAvailableNum_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,4),_QtechAddressAvailableNum_Type())
qtechAddressAvailableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAddressAvailableNum.setStatus(_A)
_QtechMacAddressTable_Object=MibTable
qtechMacAddressTable=_QtechMacAddressTable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5))
if mibBuilder.loadTexts:qtechMacAddressTable.setStatus(_A)
_QtechMacAddressEntry_Object=MibTableRow
qtechMacAddressEntry=_QtechMacAddressEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5,1))
qtechMacAddressEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:qtechMacAddressEntry.setStatus(_A)
_QtechMacAddressFdbId_Type=Unsigned32
_QtechMacAddressFdbId_Object=MibTableColumn
qtechMacAddressFdbId=_QtechMacAddressFdbId_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5,1,1),_QtechMacAddressFdbId_Type())
qtechMacAddressFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacAddressFdbId.setStatus(_A)
_QtechMacAddress_Type=MacAddress
_QtechMacAddress_Object=MibTableColumn
qtechMacAddress=_QtechMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5,1,2),_QtechMacAddress_Type())
qtechMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacAddress.setStatus(_A)
_QtechMacAddressPort_Type=IfIndex
_QtechMacAddressPort_Object=MibTableColumn
qtechMacAddressPort=_QtechMacAddressPort_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5,1,3),_QtechMacAddressPort_Type())
qtechMacAddressPort.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechMacAddressPort.setStatus(_A)
class _QtechMacAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('static',2),('filter',3)))
_QtechMacAddressType_Type.__name__=_N
_QtechMacAddressType_Object=MibTableColumn
qtechMacAddressType=_QtechMacAddressType_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5,1,4),_QtechMacAddressType_Type())
qtechMacAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechMacAddressType.setStatus(_A)
_QtechMacAddressStatus_Type=RowStatus
_QtechMacAddressStatus_Object=MibTableColumn
qtechMacAddressStatus=_QtechMacAddressStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,1,5,1,5),_QtechMacAddressStatus_Type())
qtechMacAddressStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechMacAddressStatus.setStatus(_A)
_QtechAddressNotificationObjects_ObjectIdentity=ObjectIdentity
qtechAddressNotificationObjects=_QtechAddressNotificationObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,1,2))
_QtechMacNotiGlobalEnabled_Type=EnabledStatus
_QtechMacNotiGlobalEnabled_Object=MibScalar
qtechMacNotiGlobalEnabled=_QtechMacNotiGlobalEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,1),_QtechMacNotiGlobalEnabled_Type())
qtechMacNotiGlobalEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMacNotiGlobalEnabled.setStatus(_A)
class _QtechMacNotificationInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_QtechMacNotificationInterval_Type.__name__=_F
_QtechMacNotificationInterval_Object=MibScalar
qtechMacNotificationInterval=_QtechMacNotificationInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,2),_QtechMacNotificationInterval_Type())
qtechMacNotificationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMacNotificationInterval.setStatus(_A)
class _QtechMacNotiHisTableMaxLength_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_QtechMacNotiHisTableMaxLength_Type.__name__=_F
_QtechMacNotiHisTableMaxLength_Object=MibScalar
qtechMacNotiHisTableMaxLength=_QtechMacNotiHisTableMaxLength_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,3),_QtechMacNotiHisTableMaxLength_Type())
qtechMacNotiHisTableMaxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMacNotiHisTableMaxLength.setStatus(_A)
_QtechMacNotiHisTableCurrentLength_Type=Unsigned32
_QtechMacNotiHisTableCurrentLength_Object=MibScalar
qtechMacNotiHisTableCurrentLength=_QtechMacNotiHisTableCurrentLength_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,4),_QtechMacNotiHisTableCurrentLength_Type())
qtechMacNotiHisTableCurrentLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacNotiHisTableCurrentLength.setStatus(_A)
_QtechMacNotiHisTable_Object=MibTable
qtechMacNotiHisTable=_QtechMacNotiHisTable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,5))
if mibBuilder.loadTexts:qtechMacNotiHisTable.setStatus(_A)
_QtechMacNotiHisEntry_Object=MibTableRow
qtechMacNotiHisEntry=_QtechMacNotiHisEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,5,1))
qtechMacNotiHisEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechMacNotiHisEntry.setStatus(_A)
class _QtechMacNotiHisIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechMacNotiHisIndex_Type.__name__=_F
_QtechMacNotiHisIndex_Object=MibTableColumn
qtechMacNotiHisIndex=_QtechMacNotiHisIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,5,1,1),_QtechMacNotiHisIndex_Type())
qtechMacNotiHisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacNotiHisIndex.setStatus(_A)
class _QtechMacNotiHisMacChangedMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_QtechMacNotiHisMacChangedMsg_Type.__name__=_M
_QtechMacNotiHisMacChangedMsg_Object=MibTableColumn
qtechMacNotiHisMacChangedMsg=_QtechMacNotiHisMacChangedMsg_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,5,1,2),_QtechMacNotiHisMacChangedMsg_Type())
qtechMacNotiHisMacChangedMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacNotiHisMacChangedMsg.setStatus(_A)
_QtechMacNotiHisTimestamp_Type=TimeStamp
_QtechMacNotiHisTimestamp_Object=MibTableColumn
qtechMacNotiHisTimestamp=_QtechMacNotiHisTimestamp_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,5,1,3),_QtechMacNotiHisTimestamp_Type())
qtechMacNotiHisTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacNotiHisTimestamp.setStatus(_A)
_QtechMacNotiIfCfgTable_Object=MibTable
qtechMacNotiIfCfgTable=_QtechMacNotiIfCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,6))
if mibBuilder.loadTexts:qtechMacNotiIfCfgTable.setStatus(_A)
_QtechMacNotiIfCfgEntry_Object=MibTableRow
qtechMacNotiIfCfgEntry=_QtechMacNotiIfCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,6,1))
qtechMacNotiIfCfgEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechMacNotiIfCfgEntry.setStatus(_A)
_QtechMacNotiIfIndex_Type=IfIndex
_QtechMacNotiIfIndex_Object=MibTableColumn
qtechMacNotiIfIndex=_QtechMacNotiIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,6,1,1),_QtechMacNotiIfIndex_Type())
qtechMacNotiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacNotiIfIndex.setStatus(_A)
class _QtechIfMacAddrLearntEnable_Type(EnabledStatus):defaultValue=2
_QtechIfMacAddrLearntEnable_Type.__name__=_E
_QtechIfMacAddrLearntEnable_Object=MibTableColumn
qtechIfMacAddrLearntEnable=_QtechIfMacAddrLearntEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,6,1,2),_QtechIfMacAddrLearntEnable_Type())
qtechIfMacAddrLearntEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfMacAddrLearntEnable.setStatus(_A)
class _QtechIfMacAddrRemovedEnable_Type(EnabledStatus):defaultValue=2
_QtechIfMacAddrRemovedEnable_Type.__name__=_E
_QtechIfMacAddrRemovedEnable_Object=MibTableColumn
qtechIfMacAddrRemovedEnable=_QtechIfMacAddrRemovedEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,6,1,3),_QtechIfMacAddrRemovedEnable_Type())
qtechIfMacAddrRemovedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfMacAddrRemovedEnable.setStatus(_A)
_QtechMacIfLearnTable_Object=MibTable
qtechMacIfLearnTable=_QtechMacIfLearnTable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,7))
if mibBuilder.loadTexts:qtechMacIfLearnTable.setStatus(_A)
_QtechMacIfLearnEntry_Object=MibTableRow
qtechMacIfLearnEntry=_QtechMacIfLearnEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,7,1))
qtechMacIfLearnEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:qtechMacIfLearnEntry.setStatus(_A)
_QtechMacIfLearnIfIndex_Type=IfIndex
_QtechMacIfLearnIfIndex_Object=MibTableColumn
qtechMacIfLearnIfIndex=_QtechMacIfLearnIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,7,1,1),_QtechMacIfLearnIfIndex_Type())
qtechMacIfLearnIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMacIfLearnIfIndex.setStatus(_A)
class _QtechMacIfLearnEnable_Type(EnabledStatus):defaultValue=1
_QtechMacIfLearnEnable_Type.__name__=_E
_QtechMacIfLearnEnable_Object=MibTableColumn
qtechMacIfLearnEnable=_QtechMacIfLearnEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,7,1,2),_QtechMacIfLearnEnable_Type())
qtechMacIfLearnEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMacIfLearnEnable.setStatus(_A)
class _QtechMacGlobalLearnEnabled_Type(EnabledStatus):defaultValue=1
_QtechMacGlobalLearnEnabled_Type.__name__=_E
_QtechMacGlobalLearnEnabled_Object=MibScalar
qtechMacGlobalLearnEnabled=_QtechMacGlobalLearnEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,22,1,2,8),_QtechMacGlobalLearnEnabled_Type())
qtechMacGlobalLearnEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMacGlobalLearnEnabled.setStatus(_A)
_QtechAddressTraps_ObjectIdentity=ObjectIdentity
qtechAddressTraps=_QtechAddressTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,2))
_QtechAddressMIBConformance_ObjectIdentity=ObjectIdentity
qtechAddressMIBConformance=_QtechAddressMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,3))
_QtechAddressMIBCompliances_ObjectIdentity=ObjectIdentity
qtechAddressMIBCompliances=_QtechAddressMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,3,1))
_QtechAddressMIBGroups_ObjectIdentity=ObjectIdentity
qtechAddressMIBGroups=_QtechAddressMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,22,3,2))
qtechMacAddressMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,22,3,2,1))
qtechMacAddressMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_G),(_B,_H),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechMacAddressMIBGroup.setStatus(_A)
qtechAddressNotificationMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,22,3,2,2))
qtechAddressNotificationMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_J),(_B,_L),(_B,_a),(_B,_K),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:qtechAddressNotificationMIBGroup.setStatus(_A)
macChangedNotification=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,22,2,1))
macChangedNotification.setObjects((_B,_L))
if mibBuilder.loadTexts:macChangedNotification.setStatus(_A)
qtechAddressMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,22,3,1,1))
qtechAddressMIBCompliance.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:qtechAddressMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechAddressMIB':qtechAddressMIB,'qtechAddressMIBObjects':qtechAddressMIBObjects,'qtechAddressManagementObjects':qtechAddressManagementObjects,_P:qtechDynamicAddressCurrentNum,_Q:qtechStaticAddressCurrentNum,_R:qtechFilterAddressCurrentNum,_S:qtechAddressAvailableNum,'qtechMacAddressTable':qtechMacAddressTable,'qtechMacAddressEntry':qtechMacAddressEntry,_G:qtechMacAddressFdbId,_H:qtechMacAddress,_T:qtechMacAddressPort,_U:qtechMacAddressType,_V:qtechMacAddressStatus,'qtechAddressNotificationObjects':qtechAddressNotificationObjects,_W:qtechMacNotiGlobalEnabled,_X:qtechMacNotificationInterval,_Y:qtechMacNotiHisTableMaxLength,_Z:qtechMacNotiHisTableCurrentLength,'qtechMacNotiHisTable':qtechMacNotiHisTable,'qtechMacNotiHisEntry':qtechMacNotiHisEntry,_J:qtechMacNotiHisIndex,_L:qtechMacNotiHisMacChangedMsg,_a:qtechMacNotiHisTimestamp,'qtechMacNotiIfCfgTable':qtechMacNotiIfCfgTable,'qtechMacNotiIfCfgEntry':qtechMacNotiIfCfgEntry,_K:qtechMacNotiIfIndex,_b:qtechIfMacAddrLearntEnable,_c:qtechIfMacAddrRemovedEnable,'qtechMacIfLearnTable':qtechMacIfLearnTable,'qtechMacIfLearnEntry':qtechMacIfLearnEntry,_O:qtechMacIfLearnIfIndex,'qtechMacIfLearnEnable':qtechMacIfLearnEnable,'qtechMacGlobalLearnEnabled':qtechMacGlobalLearnEnabled,'qtechAddressTraps':qtechAddressTraps,'macChangedNotification':macChangedNotification,'qtechAddressMIBConformance':qtechAddressMIBConformance,'qtechAddressMIBCompliances':qtechAddressMIBCompliances,'qtechAddressMIBCompliance':qtechAddressMIBCompliance,'qtechAddressMIBGroups':qtechAddressMIBGroups,_d:qtechMacAddressMIBGroup,_e:qtechAddressNotificationMIBGroup})