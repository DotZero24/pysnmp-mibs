_c='myAddressNotificationMIBGroup'
_b='myMacAddressMIBGroup'
_a='myIfMacAddrRemovedEnable'
_Z='myIfMacAddrLearntEnable'
_Y='myMacNotiHisTimestamp'
_X='myMacNotiHisTableCurrentLength'
_W='myMacNotiHisTableMaxLength'
_V='myMacNotificationInterval'
_U='myMacNotiGlobalEnabled'
_T='myMacAddressStatus'
_S='myMacAddressType'
_R='myMacAddressPort'
_Q='myAddressAvailableNum'
_P='myFilterAddressCurrentNum'
_O='myStaticAddressCurrentNum'
_N='myDynamicAddressCurrentNum'
_M='Integer32'
_L='OctetString'
_K='myMacNotiHisMacChangedMsg'
_J='myMacNotiIfIndex'
_I='myMacNotiHisIndex'
_H='myMacAddress'
_G='myMacAddressFdbId'
_F='EnabledStatus'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='MY-ADDRESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
myAddressMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,22))
if mibBuilder.loadTexts:myAddressMIB.setRevisions(('2002-03-20 00:00',))
_MyAddressMIBObjects_ObjectIdentity=ObjectIdentity
myAddressMIBObjects=_MyAddressMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,1))
_MyAddressManagementObjects_ObjectIdentity=ObjectIdentity
myAddressManagementObjects=_MyAddressManagementObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,1,1))
_MyDynamicAddressCurrentNum_Type=Integer32
_MyDynamicAddressCurrentNum_Object=MibScalar
myDynamicAddressCurrentNum=_MyDynamicAddressCurrentNum_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,1),_MyDynamicAddressCurrentNum_Type())
myDynamicAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:myDynamicAddressCurrentNum.setStatus(_A)
_MyStaticAddressCurrentNum_Type=Integer32
_MyStaticAddressCurrentNum_Object=MibScalar
myStaticAddressCurrentNum=_MyStaticAddressCurrentNum_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,2),_MyStaticAddressCurrentNum_Type())
myStaticAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:myStaticAddressCurrentNum.setStatus(_A)
_MyFilterAddressCurrentNum_Type=Integer32
_MyFilterAddressCurrentNum_Object=MibScalar
myFilterAddressCurrentNum=_MyFilterAddressCurrentNum_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,3),_MyFilterAddressCurrentNum_Type())
myFilterAddressCurrentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:myFilterAddressCurrentNum.setStatus(_A)
_MyAddressAvailableNum_Type=Integer32
_MyAddressAvailableNum_Object=MibScalar
myAddressAvailableNum=_MyAddressAvailableNum_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,4),_MyAddressAvailableNum_Type())
myAddressAvailableNum.setMaxAccess(_C)
if mibBuilder.loadTexts:myAddressAvailableNum.setStatus(_A)
_MyMacAddressTable_Object=MibTable
myMacAddressTable=_MyMacAddressTable_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5))
if mibBuilder.loadTexts:myMacAddressTable.setStatus(_A)
_MyMacAddressEntry_Object=MibTableRow
myMacAddressEntry=_MyMacAddressEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5,1))
myMacAddressEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:myMacAddressEntry.setStatus(_A)
_MyMacAddressFdbId_Type=Unsigned32
_MyMacAddressFdbId_Object=MibTableColumn
myMacAddressFdbId=_MyMacAddressFdbId_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5,1,1),_MyMacAddressFdbId_Type())
myMacAddressFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacAddressFdbId.setStatus(_A)
_MyMacAddress_Type=MacAddress
_MyMacAddress_Object=MibTableColumn
myMacAddress=_MyMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5,1,2),_MyMacAddress_Type())
myMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacAddress.setStatus(_A)
_MyMacAddressPort_Type=IfIndex
_MyMacAddressPort_Object=MibTableColumn
myMacAddressPort=_MyMacAddressPort_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5,1,3),_MyMacAddressPort_Type())
myMacAddressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:myMacAddressPort.setStatus(_A)
class _MyMacAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('static',2),('filter',3)))
_MyMacAddressType_Type.__name__=_M
_MyMacAddressType_Object=MibTableColumn
myMacAddressType=_MyMacAddressType_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5,1,4),_MyMacAddressType_Type())
myMacAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:myMacAddressType.setStatus(_A)
_MyMacAddressStatus_Type=RowStatus
_MyMacAddressStatus_Object=MibTableColumn
myMacAddressStatus=_MyMacAddressStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,1,5,1,5),_MyMacAddressStatus_Type())
myMacAddressStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myMacAddressStatus.setStatus(_A)
_MyAddressNotificationObjects_ObjectIdentity=ObjectIdentity
myAddressNotificationObjects=_MyAddressNotificationObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,1,2))
_MyMacNotiGlobalEnabled_Type=EnabledStatus
_MyMacNotiGlobalEnabled_Object=MibScalar
myMacNotiGlobalEnabled=_MyMacNotiGlobalEnabled_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,1),_MyMacNotiGlobalEnabled_Type())
myMacNotiGlobalEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:myMacNotiGlobalEnabled.setStatus(_A)
class _MyMacNotificationInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MyMacNotificationInterval_Type.__name__=_E
_MyMacNotificationInterval_Object=MibScalar
myMacNotificationInterval=_MyMacNotificationInterval_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,2),_MyMacNotificationInterval_Type())
myMacNotificationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:myMacNotificationInterval.setStatus(_A)
class _MyMacNotiHisTableMaxLength_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_MyMacNotiHisTableMaxLength_Type.__name__=_E
_MyMacNotiHisTableMaxLength_Object=MibScalar
myMacNotiHisTableMaxLength=_MyMacNotiHisTableMaxLength_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,3),_MyMacNotiHisTableMaxLength_Type())
myMacNotiHisTableMaxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:myMacNotiHisTableMaxLength.setStatus(_A)
_MyMacNotiHisTableCurrentLength_Type=Unsigned32
_MyMacNotiHisTableCurrentLength_Object=MibScalar
myMacNotiHisTableCurrentLength=_MyMacNotiHisTableCurrentLength_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,4),_MyMacNotiHisTableCurrentLength_Type())
myMacNotiHisTableCurrentLength.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacNotiHisTableCurrentLength.setStatus(_A)
_MyMacNotiHisTable_Object=MibTable
myMacNotiHisTable=_MyMacNotiHisTable_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,5))
if mibBuilder.loadTexts:myMacNotiHisTable.setStatus(_A)
_MyMacNotiHisEntry_Object=MibTableRow
myMacNotiHisEntry=_MyMacNotiHisEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,5,1))
myMacNotiHisEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:myMacNotiHisEntry.setStatus(_A)
class _MyMacNotiHisIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MyMacNotiHisIndex_Type.__name__=_E
_MyMacNotiHisIndex_Object=MibTableColumn
myMacNotiHisIndex=_MyMacNotiHisIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,5,1,1),_MyMacNotiHisIndex_Type())
myMacNotiHisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacNotiHisIndex.setStatus(_A)
class _MyMacNotiHisMacChangedMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_MyMacNotiHisMacChangedMsg_Type.__name__=_L
_MyMacNotiHisMacChangedMsg_Object=MibTableColumn
myMacNotiHisMacChangedMsg=_MyMacNotiHisMacChangedMsg_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,5,1,2),_MyMacNotiHisMacChangedMsg_Type())
myMacNotiHisMacChangedMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacNotiHisMacChangedMsg.setStatus(_A)
_MyMacNotiHisTimestamp_Type=TimeStamp
_MyMacNotiHisTimestamp_Object=MibTableColumn
myMacNotiHisTimestamp=_MyMacNotiHisTimestamp_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,5,1,3),_MyMacNotiHisTimestamp_Type())
myMacNotiHisTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacNotiHisTimestamp.setStatus(_A)
_MyMacNotiIfCfgTable_Object=MibTable
myMacNotiIfCfgTable=_MyMacNotiIfCfgTable_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,6))
if mibBuilder.loadTexts:myMacNotiIfCfgTable.setStatus(_A)
_MyMacNotiIfCfgEntry_Object=MibTableRow
myMacNotiIfCfgEntry=_MyMacNotiIfCfgEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,6,1))
myMacNotiIfCfgEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:myMacNotiIfCfgEntry.setStatus(_A)
_MyMacNotiIfIndex_Type=IfIndex
_MyMacNotiIfIndex_Object=MibTableColumn
myMacNotiIfIndex=_MyMacNotiIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,6,1,1),_MyMacNotiIfIndex_Type())
myMacNotiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myMacNotiIfIndex.setStatus(_A)
class _MyIfMacAddrLearntEnable_Type(EnabledStatus):defaultValue=2
_MyIfMacAddrLearntEnable_Type.__name__=_F
_MyIfMacAddrLearntEnable_Object=MibTableColumn
myIfMacAddrLearntEnable=_MyIfMacAddrLearntEnable_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,6,1,2),_MyIfMacAddrLearntEnable_Type())
myIfMacAddrLearntEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:myIfMacAddrLearntEnable.setStatus(_A)
class _MyIfMacAddrRemovedEnable_Type(EnabledStatus):defaultValue=2
_MyIfMacAddrRemovedEnable_Type.__name__=_F
_MyIfMacAddrRemovedEnable_Object=MibTableColumn
myIfMacAddrRemovedEnable=_MyIfMacAddrRemovedEnable_Object((1,3,6,1,4,1,4881,1,1,10,2,22,1,2,6,1,3),_MyIfMacAddrRemovedEnable_Type())
myIfMacAddrRemovedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:myIfMacAddrRemovedEnable.setStatus(_A)
_MyAddressTraps_ObjectIdentity=ObjectIdentity
myAddressTraps=_MyAddressTraps_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,2))
_MyAddressMIBConformance_ObjectIdentity=ObjectIdentity
myAddressMIBConformance=_MyAddressMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,3))
_MyAddressMIBCompliances_ObjectIdentity=ObjectIdentity
myAddressMIBCompliances=_MyAddressMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,3,1))
_MyAddressMIBGroups_ObjectIdentity=ObjectIdentity
myAddressMIBGroups=_MyAddressMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,22,3,2))
myMacAddressMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,22,3,2,1))
myMacAddressMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_G),(_B,_H),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:myMacAddressMIBGroup.setStatus(_A)
myAddressNotificationMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,22,3,2,2))
myAddressNotificationMIBGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_I),(_B,_K),(_B,_Y),(_B,_J),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:myAddressNotificationMIBGroup.setStatus(_A)
macChangedNotification=NotificationType((1,3,6,1,4,1,4881,1,1,10,2,22,2,1))
macChangedNotification.setObjects((_B,_K))
if mibBuilder.loadTexts:macChangedNotification.setStatus(_A)
myAddressMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,22,3,1,1))
myAddressMIBCompliance.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:myAddressMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myAddressMIB':myAddressMIB,'myAddressMIBObjects':myAddressMIBObjects,'myAddressManagementObjects':myAddressManagementObjects,_N:myDynamicAddressCurrentNum,_O:myStaticAddressCurrentNum,_P:myFilterAddressCurrentNum,_Q:myAddressAvailableNum,'myMacAddressTable':myMacAddressTable,'myMacAddressEntry':myMacAddressEntry,_G:myMacAddressFdbId,_H:myMacAddress,_R:myMacAddressPort,_S:myMacAddressType,_T:myMacAddressStatus,'myAddressNotificationObjects':myAddressNotificationObjects,_U:myMacNotiGlobalEnabled,_V:myMacNotificationInterval,_W:myMacNotiHisTableMaxLength,_X:myMacNotiHisTableCurrentLength,'myMacNotiHisTable':myMacNotiHisTable,'myMacNotiHisEntry':myMacNotiHisEntry,_I:myMacNotiHisIndex,_K:myMacNotiHisMacChangedMsg,_Y:myMacNotiHisTimestamp,'myMacNotiIfCfgTable':myMacNotiIfCfgTable,'myMacNotiIfCfgEntry':myMacNotiIfCfgEntry,_J:myMacNotiIfIndex,_Z:myIfMacAddrLearntEnable,_a:myIfMacAddrRemovedEnable,'myAddressTraps':myAddressTraps,'macChangedNotification':macChangedNotification,'myAddressMIBConformance':myAddressMIBConformance,'myAddressMIBCompliances':myAddressMIBCompliances,'myAddressMIBCompliance':myAddressMIBCompliance,'myAddressMIBGroups':myAddressMIBGroups,_b:myMacAddressMIBGroup,_c:myAddressNotificationMIBGroup})